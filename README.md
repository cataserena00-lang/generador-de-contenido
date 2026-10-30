# Generador de contenido · Prensa

Convierte la información oficial del día en contenido de prensa: copys de Instagram, textos para X, texto de placa editable, gacetillas y placas PNG (1:1, 4:5, 9:16). Hoy tiene un módulo, OBRAS (parte diario de obras), y va a crecer a otros temas y a toda la provincia.

**Para trabajar con Claude Code:** abrí esta carpeta con Claude Code. Lee `CLAUDE.md` solo y ya tiene las reglas, el flujo y los pendientes. No hace falta explicarle nada de nuevo.

## Rutina diaria (módulo Obras)
1. Guardá el parte tal cual en `entrada/<fecha>/lista.txt`.
2. `python tools/fetch_docs.py <fecha>` baja los Google Docs (compartidos con enlace) a `entrada/_cache`.
3. `python tools/parse_lista.py <fecha>` genera `entrada/<fecha>/parte.json`.
4. Se redactan a mano los generales y periódicos en `entrada/<fecha>/redactar.py` (genera `contenido.json`).
5. `python tools/build.py <fecha>` arma `salida/<fecha>/tablero.html` y copia el resultado a `deploy/index.html`.
6. Se revisa el tablero (pestaña "Chequeo de calidad" en ✔) y recién ahí se publica.

Requisitos: Python 3 y PyMuPDF (`pip install pymupdf`) para leer PDF y comprimir fotos.

## Estructura
- `tools/` código: `plantilla.html`, `build.py`, `parse_lista.py`, `fetch_docs.py`.
- `data/` datos fijos (circuitos, barrios, memorias de pavimentación, finalizadas, reglas del parte).
- `assets/` marca (SVG, PNG, paleta) y fuentes Poppins.
- `entrada/` un parte por día; `entrada/_cache` guarda lo bajado de Drive (no se comparte).
- `salida/` tableros generados (se regeneran).
- `deploy/` lo que se publica: `index.html`, `middleware.js` (usuario y clave), `vercel.json`, `robots.txt`.
- `para_proyecto/` archivos livianos e instrucciones para el Proyecto de Claude Team (`PASO_A_PASO.md`).

## Reglas que no se negocian
- No se inventa ningún dato. Lo que falta queda fuera del texto y se avisa en el Chequeo de calidad.
- Nunca "circuito" ni "seccional" en un texto publicable: se habla de barrios, con la palabra "Barrio".
- Sin montos, sin "/" y sin claves ni tokens en ningún archivo.

## Publicación
Repo privado de GitHub `cataserena00-lang/generador-de-contenido` (contiene solo lo de `deploy/`) y proyecto de Vercel con el mismo nombre. Publica una sola persona, la titular de las cuentas. Acceso con usuario y clave (variables en Vercel; nunca en el código).
