# Módulo ANUNCIOS · seguimiento de anuncios de gestión (Gobierno de la Provincia de Córdoba)

Segundo módulo del generador. De la base de seguimiento de anuncios (`Seguimiento_de_anuncios_ML.xlsx`, hoja "Tablero") se arma un tablero HTML autocontenido con placas y copys por localidad (IG, X, SMS, texto de placa y gacetilla), una ficha por anuncio y el Chequeo de calidad.
Archivos del módulo: `tools/parse_anuncios.py`, `tools/redactar_anuncios.py`, `tools/build_anuncios.py`, `tools/plantilla_anuncios.html`; `data/dic_localidades.csv`, `dic_departamentos.csv`, `dic_estado_anuncio.csv`, `dic_grafia.csv`; `assets/marca/cinta-tricolor.svg`.
Los dos tableros se enlazan desde la cabecera: "Obras" (`index.html`) y "Anuncios" (`anuncios.html`), con el módulo actual resaltado.

## Flujo semanal
1. Guardar la base nueva en `entrada/anuncios/Seguimiento_de_anuncios_ML.xlsx`.
2. `python tools/parse_anuncios.py entrada/anuncios/Seguimiento_de_anuncios_ML.xlsx <fecha>` → `entrada/anuncios/<fecha>/anuncios.json`. Revisar el total y los avisos (localidades fuera de la maestra, estados sin diccionario, duplicados).
3. Redacción con IA (solo cumplidos y en ejecución): con `ANTHROPIC_API_KEY` en el entorno (nunca en un archivo), `python tools/redactar_anuncios.py <fecha> --solo-nuevos`. La primera vez, o si cambian las reglas, probar con `--limite 30` y aprobar el tono antes de correr el total. Guarda cada 25 en `data/anuncios_textos.json`; lo revisado a mano no se pisa.
4. `python tools/build_anuncios.py <fecha>` → `salida/anuncios/<fecha>/tablero_anuncios.html` y copia a `deploy/anuncios.html`.
5. Verificar en el navegador: sin errores de consola, el Chequeo de calidad carga, una ficha abre, una edición sobrevive a recargar y "Exportar ediciones" baja un `contenido.json`.
6. Las ediciones del equipo viven en el navegador (localStorage) hasta exportarlas: copiar el `contenido.json` exportado a `entrada/anuncios/<fecha>/` y volver a correr el build.
7. Mostrar el resultado y pedir confirmación. No publicar sin un "sí" explícito.

## Reglas de datos
- Un anuncio = una meta (`Meta`). Los duplicados (mismo texto y localidad) quedan una sola vez y se avisan.
- Localidad y departamento salen de la maestra (`dic_localidades.csv`); si la base dice otro departamento, gana la maestra y se avisa. Grafía publicable: la de la base si trae tildes; si no, `dic_grafia.csv`.
- Estado: `dic_estado_anuncio.csv` traduce el estado desagregado a estado normalizado, etiqueta de placa y si es publicable. Si choca con la columna "Estado", gana "Estado" y se avisa.
- La inversión se lee y no se publica (solo se guarda `tiene_inversion`). El texto de placa automático es una propuesta: quita sujeto, verbo de anuncio y montos; lo dudoso queda en avisos.
- Textos con IA: `revisado=false` hasta que alguien los revise; el Chequeo los lista.

## Reglas de redacción del módulo
- Las de CLAUDE.md: sin montos ni "millones", sin "/", nunca "circuito" ni "seccional", no inventar nada.
- Sin "el gobernador", "Llaryora", "anunció", "prometió" ni "comprometió" en placas y titulares. Sustantivo adelante.
- Lo cumplido, en pasado o como hecho; lo que está en ejecución, en presente; nunca en futuro.

## Decisiones tomadas
- Redacción con IA una sola vez por meta, guardada en `data/anuncios_textos.json`; el build no llama a la API.
- La base, `entrada/anuncios/`, `data/anuncios_textos.json` y `deploy/anuncios.html` están en `.gitignore` mientras el repo de GitHub sea público.
- Navegación entre módulos en la cabecera; cada build copia su tablero a `deploy/` (`index.html` y `anuncios.html`).

## Pendientes
- Correr el pipeline con la base real: `Seguimiento_de_anuncios_ML.xlsx` no vino en el zip del módulo (se esperan 2639 anuncios).
- Redacción con IA: falta la clave en el entorno de trabajo; aprobar 10 resultados de la prueba de 30 antes del total (unos 2.244 pedidos).
- Pasar el repo a privado; recién ahí sacar del `.gitignore` lo necesario para publicar `anuncios.html`.
- `deploy/LEEME.md` todavía habla solo de `index.html`.

## Traspaso · primera versión del módulo (30/10)
- Hecho: código, diccionarios y cinta copiados (UTF-8 sin BOM); enlaces Obras y Anuncios en las dos cabeceras; `build_anuncios.py` copia a `deploy/anuncios.html`.
- Probado con una base inventada de 3 anuncios (ya borrada): parse, build, Chequeo, ficha, edición tras recargar, exportar y navegación, sin errores de consola. Obras sigue igual (cabecera de 48 px, Chequeo todo ✔).
- Archivos: tools/ (4 nuevos; en `plantilla.html` solo la cabecera), data/ (4 csv), assets/marca/cinta-tricolor.svg, deploy/index.html, .gitignore y este archivo.
- Estado: build de obras listo en la rama `claude/loving-albattani-pfeg17`, sin publicar. Anuncios todavía no corrió con datos reales.
- Dudas: falta la base xlsx y la clave de la API; confirmar si la base puede ir al repo (hoy es público).
