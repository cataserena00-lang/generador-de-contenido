# Módulo ANUNCIOS · seguimiento de anuncios de gestión (Gobierno de la Provincia de Córdoba)

Segundo módulo del generador. De la base de seguimiento de anuncios (`Seguimiento_de_anuncios_ML.xlsx`, hoja "Tablero") se arma un tablero HTML autocontenido con placas y copys por localidad (IG, X, SMS, texto de placa y gacetilla), una ficha por anuncio y el Chequeo de calidad.
Archivos del módulo: `tools/parse_anuncios.py`, `tools/redactar_anuncios.py`, `tools/build_anuncios.py`, `tools/plantilla_anuncios.html`; `data/dic_localidades.csv`, `dic_departamentos.csv`, `dic_estado_anuncio.csv`, `dic_grafia.csv`; `assets/marca/cinta-tricolor.svg`.
Los dos tableros se enlazan desde la cabecera: "Obras" (`index.html`) y "Anuncios" (`anuncios.html`), con el módulo actual resaltado.

## Flujo semanal
1. Guardar la base nueva en `entrada/anuncios/Seguimiento_de_anuncios_ML.xlsx`.
2. `python tools/parse_anuncios.py entrada/anuncios/Seguimiento_de_anuncios_ML.xlsx <fecha>` → `entrada/anuncios/<fecha>/anuncios.json`. Revisar el total y los avisos (localidades fuera de la maestra, estados sin diccionario, duplicados).
3. Redacción (solo cumplidos y en ejecución): con `ANTHROPIC_API_KEY` en el entorno (nunca en un archivo), `python tools/redactar_anuncios.py <fecha> --solo-nuevos`. La primera vez, o si cambian las reglas, probar con `--limite 30` y aprobar el tono antes de correr el total. Guarda cada 25 en `data/anuncios_textos.json`; lo revisado a mano no se pisa. Sin clave, la redacción la hace Claude Code a mano con las mismas reglas (bloque SISTEMA del script más los ajustes de abajo), en tandas de 100, con `modelo: "claude-code"`.
4. `python tools/build_anuncios.py <fecha>` → `salida/anuncios/<fecha>/tablero_anuncios.html` y copia a `deploy/anuncios.html`. Para publicar, copiar también `deploy/index.html` y `deploy/anuncios.html` a la raíz del repo (Vercel publica la raíz).
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
- Lo cumplido, en pasado o como hecho; lo que está en ejecución, en presente; nunca en futuro. El estado de la base manda sobre lo que diga el texto; si se contradicen, va en "duda".
- Ajustes aprobados el 30/10: el titular empieza con sujeto explícito ("La Provincia", "Córdoba" o "El Gobierno de Córdoba"), nunca "Se terminó" ni el gobernador. Con "Fondos entregados", la placa nombra el destino ("Dos centros de abordaje de las adicciones"), no el aporte ("Fondos para…").

## Decisiones tomadas
- Redacción con IA una sola vez por meta, guardada en `data/anuncios_textos.json`; el build no llama a la API.
- El repo de GitHub quedó **público por decisión del equipo el 30/10**, pendiente de pasarlo a privado. Se publica `anuncios.html` (raíz y `deploy/`) y se suben `anuncios.json` y `data/anuncios_textos.json`, que ya van completos dentro del tablero. Solo el xlsx original (con la columna de inversión) queda fuera (`.gitignore`).
- Navegación entre módulos en la cabecera; cada build copia su tablero a `deploy/` (`index.html` y `anuncios.html`).

## Placas: selección de anuncios y diseño aprobado (2026-11-02, rama novedades)
- En cada tarjeta de localidad y de departamento hay un panel "Anuncios en la placa" con una casilla por anuncio. Uno solo → placa individual (etiqueta en píldora de contorno, título grande, bajada); varios → lista "Lo que ya es una realidad:" / "Lo que está en marcha:" con tilde por ítem (hasta cinco se leen bien). Sin elegir, la localidad muestra los 5 sugeridos del ranking y el departamento la placa con el total. La selección se guarda en el navegador y sale en "Exportar ediciones" (`seleccion`); se puede precargar en `contenido.json → seleccion` con el id de la pieza (`l_<estado>_<localidad>`, `d_<estado>_<DEPARTAMENTO>`).
- Al cambiar la selección se descarta la edición anterior del texto de placa de esa pieza (items o placaTxt) y se rearma todo: placa, IG, X y SMS.
- Paleta aprobada: Cumplimos en celeste (por defecto), marino, azul, dorado o blanco (fondo blanco, todo en azul); En marcha en verde o blanco (todo en verde). Ícono de campaña en la banda (tilde o flecha). La capital se nombra "en la ciudad de Córdoba" y no lleva pie; los departamentos "en el departamento X".
- Estilo aprobado para los ítems y títulos de placa: primera persona del plural y verbo adelante ("Construimos el polideportivo", "Llevamos gas natural al parque industrial"). Los textos redactados con IA siguen siendo sustantivos; se corrigen a mano en "Texto de la placa" o en `contenido.json → anuncios → {meta: {placa, bajada, etiquetaPlaca}}`. `bajada` vacía deja la placa sin tercera línea.
- Precargados en `entrada/anuncios/2026-10-30/contenido.json`: Berrotarán (5 anuncios, textos aprobados), departamento Río Cuarto (selección y 5 líneas aprobadas), ciudad de Córdoba (altonivel de Ejército Argentino, meta 35). La meta 129 (residencias de la SeNAF) figura como cumplida en la base, no como en marcha: se dejó con el texto aprobado pero sin forzar el estado.
- Foto en la placa (2026-11-02): en cada tarjeta, "Subir foto" (se reduce a 1600 px y queda en este navegador, aparte de las ediciones; no sale en Exportar ediciones) y tres diseños: Sin foto, Foto arriba (la foto ocupa la parte alta y se funde en el color; sugerido para listas) y Foto completa (la foto cubre el panel y el texto se apoya abajo sobre un degradado que arranca donde empieza el texto; sugerido para placas individuales). Encuadre: se arrastra la foto dentro de la placa (en cualquiera de los tres formatos) y hay un control de zoom; el encuadre se guarda con la foto. Con Foto completa y lista, el texto deja libre al menos el 40 % superior del panel. Los PNG salen con la foto. Si el navegador no tiene lugar para guardarla, avisa y la usa igual en la sesión.

## Pendientes
- Fotos de placas: hoy viven solo en el navegador de quien las subió. Si hace falta compartirlas, definir con el equipo una carpeta `entrada/anuncios/<fecha>/fotos/<id de pieza>.jpg` que el build incorpore.
- Pasar el repo de GitHub a privado (quedó público por decisión del equipo el 30/10).
- Redactar los 1.835 cumplidos y en ejecución del resto de los departamentos. Hoy esos llevan la placa automática y explican los ✖ del Chequeo (94 con montos, 469 SMS genéricos, 4 de la meta 1659 en marcha que dice "cumplido"); ninguno es de Capital, Río Cuarto ni San Justo.
- Revisar las 86 metas con "duda" de los tres departamentos redactados (estado contra etiqueta, posibles duplicados, fondos sin destino) y marcar `revisado: true` lo aprobado.
- Confirmar en Vercel que el despliegue quedó Ready y que `/anuncios.html` pide usuario y clave (desde esta sesión no se llega a vercel.app ni a la cuenta del proyecto).
- `deploy/LEEME.md` todavía habla solo de `index.html`.

## Traspaso · primera versión del módulo (30/10)
- Hecho: código, diccionarios y cinta copiados (UTF-8 sin BOM); enlaces Obras y Anuncios en las dos cabeceras; `build_anuncios.py` copia a `deploy/anuncios.html`.
- Probado con una base inventada de 3 anuncios (ya borrada): parse, build, Chequeo, ficha, edición tras recargar, exportar y navegación, sin errores de consola. Obras sigue igual (cabecera de 48 px, Chequeo todo ✔).
- Archivos: tools/ (4 nuevos; en `plantilla.html` solo la cabecera), data/ (4 csv), assets/marca/cinta-tricolor.svg, deploy/index.html, .gitignore y este archivo.
- Estado: build de obras listo en la rama `claude/loving-albattani-pfeg17`, sin publicar. Anuncios todavía no corrió con datos reales.
- Dudas: falta la base xlsx y la clave de la API; confirmar si la base puede ir al repo (hoy es público).

## Traspaso · redacción de Capital, Río Cuarto y San Justo y publicación (30/10)
- Hecho: base real parseada (2639 anuncios); 409 textos redactados a mano (cumplidos y en ejecución de Capital, Río Cuarto y San Justo) con los ajustes aprobados, en 4 tandas validadas; 86 con duda.
- Archivos: data/anuncios_textos.json, entrada/anuncios/2026-10-30/anuncios.json, anuncios.html e index.html (raíz y deploy/), .gitignore y este archivo.
- Verificado: anuncios.html 3,9 MB e index.html 3,2 MB; sin errores de consola; ficha, edición tras recargar, exportar y navegación Obras/Anuncios funcionan; Chequeo de obras todo ✔.
- Estado: publicado en main a pedido de Tomás (repo público por decisión del equipo). Falta confirmar en Vercel el Ready y el 401 en /anuncios.html.
- Dudas: las 86 metas con duda y los ✖ del Chequeo, que vienen todos de departamentos todavía sin redactar.

## Traspaso · placas con selección, diseño aprobado y foto (2026-11-02)
- Hecho: selección de anuncios por casilla (panel plegable "Anuncios en la placa"), placa individual o de lista según lo tildado, diseño de los carteles aprobados con paleta por campaña, "en la ciudad de Córdoba" para la capital, búsqueda de departamento o localidad en la columna lateral, y foto en la placa (Subir, Cambiar, Quitar; Foto arriba y Foto completa; encuadre arrastrando y zoom). Precargados Berrotarán, departamento Río Cuarto y ciudad de Córdoba con los textos aprobados.
- Archivos: tools/plantilla_anuncios.html, entrada/anuncios/2026-10-30/contenido.json (nuevo), deploy/anuncios.html, anuncios.html, este archivo.
- Estado: **publicado en main** (commits d5f6e14, 3956f94 vía PR #2 y 498be03); deploys de Vercel Ready en Production. La rama `novedades` quedó creada para los próximos cambios (los previews de Vercel responden "Sitio no configurado" hasta que las variables de usuario y clave se habiliten también para Preview).
- Dudas: ninguna abierta. La meta 129 (SeNAF) figura cumplida en la base; se dejó así.
