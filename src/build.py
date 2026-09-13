"""Genera index.html a partir de src/template.html.

Incrusta el mapa de Centroamérica como <symbol> reutilizable, la banda de los
48 cantones y la ilustración de la red de solidaridad.
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
tpl = (RAIZ / "src" / "template.html").read_text(encoding="utf-8")

# Mapa: convierte el SVG generado en <symbol id="mapa-ca">, con relleno por país
# controlable desde CSS (--GTM, --NIC, etc.).
svg = (RAIZ / "img" / "ilustraciones" / "mapa-ca.svg").read_text(encoding="utf-8")
cuerpo = re.sub(r"^<svg[^>]*>|</svg>$", "", svg)
cuerpo = re.sub(r'<path class="pais" id="m-([A-Z]{3})"',
                lambda m: f'<path class="pais" style="fill:var(--{m.group(1)},var(--pais,#3F3F3F))"', cuerpo)
cuerpo = cuerpo.replace('<path class="ctx"', '<path class="ctx" style="fill:var(--ctx,#262626)"')
symbol = f'<symbol id="mapa-ca" viewBox="0 0 1600 1178">{cuerpo}</symbol>'

cantones = "".join(
    f'<i style="transition-delay:{i * 25}ms"></i>' for i in range(48)
)

# Islas de coherencia en Guatemala (coordenadas del mapa) y nodos externos.
islas = [
    (330, 420, "Periodismo independiente", -1),
    (440, 380, "Derechos humanos", 1),
    (300, 520, "Autoridades indígenas", -1),
    (470, 480, "Transparencia", 1),
    (400, 590, "Defensa legal", -1),
]
region = [(542, 574), (707, 480), (856, 659), (937, 879), (1243, 992)]
externos = [(1330, 190, "Cooperación internacional"), (1330, 360, "Filantropía")]

partes = []
for i, (x, y, _t, _l) in enumerate(islas):
    for ex, ey, _ in externos:
        cx = (x + ex) / 2
        partes.append(f'<path class="link" d="M{x},{y} Q{cx},{min(y, ey) - 160} {ex},{ey}"/>')
for (x, y) in region:
    gx, gy = islas[3][0], islas[3][1]
    partes.append(f'<path class="link" d="M{gx},{gy} Q{(gx + x) / 2},{(gy + y) / 2 - 90} {x},{y}"/>')
for ex, ey, t in externos:
    partes.append(
        f'<g class="ext"><circle cx="{ex}" cy="{ey}" r="22" fill="#FF7360"/>'
        f'<text x="{ex - 40}" y="{ey + 12}" font-size="40" font-weight="600" text-anchor="end">{t}</text></g>'
    )
for (x, y) in region:
    partes.append(f'<g class="isla"><circle class="halo" cx="{x}" cy="{y}" r="12"/><circle class="core" cx="{x}" cy="{y}" r="12"/></g>')
for x, y, t, lado in islas:
    tx = x - 30 if lado < 0 else x + 30
    anchor = "end" if lado < 0 else "start"
    partes.append(
        f'<g class="isla"><circle class="halo" cx="{x}" cy="{y}" r="16"/><circle class="core" cx="{x}" cy="{y}" r="16"/>'
        f'<text x="{tx}" y="{y + 11}" font-size="32" font-weight="500" text-anchor="{anchor}">{t}</text></g>'
    )
red = "".join(partes)

html = (tpl.replace("<!--MAPA-->", symbol)
           .replace("<!--CANTONES-->", cantones)
           .replace("<!--RED-->", red))

for c in "—–":
    assert c not in html, f"guion no permitido: {c!r}"

(RAIZ / "index.html").write_text(html, encoding="utf-8")
print("index.html", len(html) // 1024, "KB")
