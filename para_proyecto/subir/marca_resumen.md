# Resumen de marca (reemplaza SVG, PNG y fuentes del repo)

Fuente de colores: `assets/marca/paleta.json`, extraída de los carteles .ai (valores de relleno exactos).
Los archivos gráficos (SVG/PNG, fuentes Poppins) viven en el repo y los usa `tools/build.py`; **no hace falta subirlos**.

## Tres ejes de comunicación
| Eje | Nombre en texto | Pie de placa | Hashtags | Emoji |
|---|---|---|---|---|
| calle | Calle por Calle, Córdoba Mejora | #17233d (marino) | #CallePorCalle #CórdobaMejora #HacerParaCrecer | 🛣️ |
| accesible | Córdoba Accesible | #09467f (azul) | #CórdobaAccesible #HacerParaCrecer | ♿ |
| plaza | Nos vemos en la Plaza, Córdoba Mejora | #09467f (azul), con logo extra EPEC | #NosVemosEnLaPlaza #CórdobaMejora #HacerParaCrecer | 🌳 |

Lema general: **Hacer para Crecer**. Encuadre: "Gobierno de la Provincia en conjunto con la Municipalidad de Córdoba".
Accesible: "Una Córdoba inclusiva, pensada para todos" (siempre "Rampas en ejecución", nunca "nuevas").

## Tipografía
Poppins: ExtraBold/Black para títulos y cifras, SemiBold/Bold para etiquetas. Licencia OFL.

## Formatos de placa (canvas, se bajan como PNG)
- Feed 1:1 = 1080×1080; Feed 4:5 = 1080×1350 (recomendado); Stories/Reels 9:16 = 1080×1920.
- Historia 9:16: zona segura, ~14 % libre arriba y el pie termina al 88,5 % del alto (contenido centrado, relleno amarillo arriba y azul abajo en el eje accesible).
- Pie de placa: franja de color del eje con la tira de logos institucionales; wordmark del eje arriba.

## Diseños con foto
- Círculo, Marco, Foto completa y Sin foto. "Sugerido" elige por la foto: chica (<720 px) o borrosa (nitidez <800) → Círculo; vertical y nítida → Completa; horizontal y nítida → rotativo.
- El texto de la placa se edita en pantalla y la placa se redibuja.
- Placa: [título] [dato/valor] [lugar] [barrio]; sin montos; barrio con la palabra "Barrio".

## Paleta por eje (de paleta.json)

**calle** — Calle por Calle - Córdoba Mejora
- marino: `#17233d`
- rojo: `#bd1635`
- rojo_alt: `#c01e3a`
- celeste: `#bedff7`
- celeste_medio: `#82b6e3`
- pie: `#17233d`
- texto_titulo: `#17233d`
- wordmark: `#ffffff`

**accesible** — Córdoba Accesible
- amarillo: `#eaab3b`
- crema: `#e8d7b0`
- azul: `#09467f`
- marino: `#172743`
- celeste: `#bedff7`
- celeste_medio: `#69acdf`
- rojo: `#bd1635`
- pie: `#09467f`
- texto_dato: `#09467f`
- wordmark: `#172743`

**plaza** — Nos vemos en la Plaza - Córdoba Mejora
- verde_claro: `#c6dfce`
- verde_medio: `#89ba96`
- verde: `#4da070`
- azul: `#09467f`
- marino: `#172743`
- pie: `#09467f`
- texto_titulo: `#09467f`
- wordmark: `#172743`
- logo_extra_pie: `EPEC`

## Medidas de los carteles originales (de _info.json)
| Eje | Cartel (pt) | Color del pie | Alto del pie | Relación de la tira de logos |
|---|---|---|---|---|
| calle | 5669×2835 | #17233d | 0.2066 | 11.747 |
| accesible | 2835×3458 | #09467f | 0.1452 | 11.538 |
| plaza | 6973×3515 | #09467f | 0.2113 | 14.695 |

## Qué hay en el repo (no subir)
`assets/marca/`: _favicon-32, _favicon-prueba, _info, _montaje-accesible, _montaje-calle, _montaje-plaza, cinta-pie-accesible, favicon-cordoba, fondo-accesible, fondo-calle, fondo-plaza, gobierno-color, logos-accesible, logos-calle, logos-plaza, paleta, wordmark-accesible, wordmark-calle, wordmark-plaza.
