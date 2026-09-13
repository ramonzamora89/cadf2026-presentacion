# El precio de decir la verdad

Presentación que acompaña el discurso inaugural de José Rubén Zamora en el Central America Donors Forum 2026 (CADF 2026).

Funciona como un lienzo con zoom: cada clic desplaza la cámara hacia la siguiente escena.

## Controles

| Acción | Tecla |
| --- | --- |
| Avanzar | clic, →, ↓, espacio, Enter, PageDown (control remoto) |
| Retroceder | ←, ↑, PageUp, Backspace, clic derecho, Shift + clic |
| Vista general | O |
| Pantalla completa | F |
| Notas del orador | N |
| Pantalla negra | B |
| Ir a una escena | agregar `#número` a la URL |

## Estructura

- `src/template.html`: contenido, estilos y lógica.
- `src/build.py`: genera `index.html` incrustando el mapa, la banda de los 48 cantones y la red de solidaridad.
- `img/coberturas/`: páginas del archivo de elPeriódico.
- `img/fotos/`, `img/personas/`: fotografías con licencia libre (ver créditos en la última escena).
- `img/ilustraciones/mapa-ca.svg`: Centroamérica, Natural Earth 1:50m.

Para regenerar después de editar la plantilla:

```
python3 src/build.py
```

## Créditos

- Archivo de elPeriódico (1996 a 2023).
- Fotografías vía Wikimedia Commons: elPeriódico (CC BY 3.0), Embajada de EE. UU. (dominio público), Kaldari (CC0), Nerdoguate (CC BY-SA 4.0).
- Cartografía: Natural Earth (dominio público). Tipografía: Poppins (SIL OFL 1.1).
- Sistema visual basado en el manual de marca de el_Archivo.
