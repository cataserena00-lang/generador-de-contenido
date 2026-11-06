# Módulo OBRAS · parte diario de obras (Municipalidad de Córdoba)

Primer módulo del generador. Del "parte de obras" (LISTA DE DIFUSIÓN, texto pegado cada día) se arma un tablero HTML autocontenido con copys de Instagram, textos para X (máx. 280), texto de placa editable, gacetillas y placas PNG (1:1, 4:5, 9:16) de tres ejes: Calle por Calle, Córdoba Accesible y Nos vemos en la Plaza.
Arriba del contenido va una barra de contexto con la zona y el período (Hoy en marino, Semana en dorado) y tres pestañas: Obra por obra, Resumen (con toda la ciudad, al final van las «Otras lecturas»: 7, 10, 15 y 30 días y por tipo: plazas, rampas, pavimentación) y Chequeo (gris). Los datos del parte están plegados al pie de la columna lateral.
Archivos de este módulo: esquema_parte.md, muestra_parte.json, historico_resumen.csv, dic_circuitos.csv, dic_barrio_circuito.csv, dic_pavimentacion.csv, dic_rubros.csv, dic_campos_parte.csv, reglas_parte.md, marca_resumen.md, codigo_pipeline.md, codigo_plantilla.md.

## Flujo de cada día
1. Guardar el parte tal cual en `entrada/<fecha>/lista.txt`.
2. `python tools/fetch_docs.py <fecha>`: baja los Google Docs (compartidos con enlace) a `entrada/_cache`.
3. `python tools/parse_lista.py <fecha>`: genera `parte.json`. El total leído debe igualar el encabezado del parte.
4. Cargar `finalizadas` del día en `data/finalizadas.json` (stock acumulado; sin dato nuevo se arrastra el anterior).
5. Redactar a mano `entrada/<fecha>/redactar.py` → `contenido.json` (generales, periódicos, por tipo de obra). Los copys por obra son automáticos, con variantes rotativas.
6. `python tools/build.py <fecha>`: `salida/<fecha>/tablero.html` y copia a `deploy/index.html`.
7. Verificar en el navegador: sin errores de consola, Chequeo de calidad todo ✔, X ≤ 280.
8. Mostrar el resultado y pedir confirmación antes de publicar.

## Reglas de datos del parte
- Esquina = UNA obra (con N rampas). Rampas siempre sin barrio; las placas dicen "Rampas en ejecución".
- Rubro = título de la sección. Calle y entre-calles: "e/", "entre", " e ". Notas: Nocturno, 2.ª intervención, 3.ª etapa.
- Barrio: el del parte. En Mantenimiento y Bacheo en frío la línea entera es el barrio. Pavimentación: barrio, cuadras y plazo de `data/memorias.json`.
- Circuito: el código del parte gana ("-6ª" = 6A). Es dato interno y nunca se publica.
- Plazas: se deduplican por nombre dentro del día; alias en la plantilla (ALIAS) y en parse_lista.py (PLAZA_ALIAS).
- `finalizadas` es un stock acumulado: solo para acumulados. 1.100 cuadras y 2.100 rampas son planes ("prevé", "contempla").
- Periódicos: ventanas por días hábiles (no hay parte los fines de semana); si faltan partes se avisa. "Obras distintas" = ids únicos.
- Puestos de trabajo, finalizadas y presupuesto son datos de toda la ciudad.

## Reglas de redacción del módulo
- Orden institucional: "Gobierno de la Provincia en conjunto con la Municipalidad de Córdoba". Tono de prensa.cba.gov.ar. Sin números sueltos.
- Cada copy de IG y X lleva UNA línea política corta y variada: con equilibrio fiscal se sostiene la inversión en infraestructura de todos los cordobeses. No repetir la misma frase en todos lados.
- Las definiciones largas de programa van solo en gacetillas; en IG, una línea.
- Gacetillas generales y periódicas: título, bajada con viñetas, lead, subtítulos y un párrafo variado de "Seguimiento diario de las obras" con https://claude.ai/artifact/Xbxitst4ZDhQrsBjckBWRu (de inspiración, nunca copiado igual).
- Sin "asistencia social" en textos de obra. Textos de X nunca cortados: se resume el mensaje, no se trunca la frase.

## Estilo visual del módulo
Poppins; colores y pies por eje en marca_resumen.md. Placas con 3 diseños de foto (Círculo, Marco, Completa), "Sugerido" por calidad de foto y "Sin foto". Historias 9:16 con zona segura. Favicon con la bandera de Córdoba. Título del tablero: GENERADOR DE CONTENIDO. "Chequeo de calidad" va gris, a la derecha.

### Galería de fotos genéricas por tipo de obra
- Ruta: `assets/galeria/<clave_rubro>/`. Claves de carpeta (iguales a TIPOS de la plantilla): `mant`, `frio`, `rampas`, `bacheo`, `rehab`, `hormigon`, `pav`, `plaza`.
- Sumar fotos: soltar los archivos (.jpg, .jpeg, .png o .webp) en la carpeta del rubro y volver a correr `python tools/build.py <fecha>`. No hace falta tocar código. El build las recomprime a 990 px de lado máximo (su tamaño real), JPEG calidad 75, las ordena por nombre de archivo e imprime el peso de `deploy/galeria/` y el del tablero. Una carpeta nueva solo sirve si su nombre es una de las claves.
- En la tarjeta, la fila "Foto:" muestra miniaturas ("Propia", "Parte 1", "Parte 2"…). Debajo va la tira "Fotos genéricas de <rubro>" con las de la galería, y la miniatura elegida lleva borde del color del eje. Si la obra no trae foto del parte ni propia, se elige sola una genérica que rota según el id de la obra, y debajo de la placa aparece "Foto genérica del tipo de obra. Podés elegir otra o subir la tuya". El diseño "Sin foto" sigue disponible. Las piezas por tipo (plazas, rampas y pavimentación) usan la galería de su rubro.
- Etiqueta "Foto genérica" (gris con texto marino) cuando la obra solo tiene genérica. El filtro Con foto / Sin foto sigue contando la foto del parte. El PNG bajado con una genérica lleva el sufijo `_generica`.
- Chequeo: "Obras sin foto del parte (salen con foto genérica)" para los rubros con galería y "Rubros sin galería: …" para saber qué carpetas faltan cargar.
- La galería ya no viaja dentro del tablero: el build escribe cada foto como archivo suelto en `deploy/galeria/<rubro>/<nombre>.jpg` (y una copia en `salida/<fecha>/galeria/`) y el tablero guarda solo las rutas relativas. Cada build borra y vuelve a escribir esas carpetas. Al publicar, hay que subir `deploy/galeria/` junto con `index.html`. Las rutas `/galeria/*` piden usuario y clave como el resto, porque el matcher del middleware es `/(.*)`.
- Abierto como archivo local (doble clic en `salida/<fecha>/tablero.html`), el tablero muestra las genéricas, pero no deja bajar el PNG con una genérica: el navegador bloquea las fotos sueltas y el tablero avisa. Para bajar placas con genérica, usar el sitio publicado o un servidor local (`python -m http.server` dentro de `deploy/`).
- Sugerido con una genérica: se saltea el umbral de 720 px y se decide por nitidez y orientación. Si es borrosa, Círculo; si es vertical, Foto completa; si es horizontal, Foto completa o Marco. Las fotos del parte y las propias siguen con la regla de siempre.
- Las fotos vienen del build, no del navegador. El encuadre y el zoom de cada genérica se guardan por obra y por foto, como los de las otras fotos. La genérica elegida a mano también se recuerda por obra en el navegador; al volver a una foto del parte o subir una propia, esa elección se borra.

## Errores ya resueltos (no repetir)
- Contar cada rampa como obra: la serie usa ítems. Falsos "faltan partes" por fines de semana. Mojibake: archivos UTF-8 sin BOM.
- `vercel.json` con BOM rompe el build. PowerShell 5.1 rompe `$` y comillas en parches: usar Python o el editor.
- Favicon con "#" sin codificar (usar %23). Bundle > 10 MB: las fotos se recomprimen a 1500 px.
- Subida web a GitHub: confirmar el commit solo cuando termina la barra de carga.
- Erratas del parte: "Gral." → General, "Ombu" → Ombú, "-6ª", "zz" sueltos, "Barrio:Barrio:".

## Pendientes del módulo
- Plaza Barrios Unidos vs. Plaza Centro América: ¿son la misma? Con la confirmación, agregar el alias y recontar plazas y obras distintas.
- Periódicos de 15 días y mensual: faltan partes (11 y 22 días hábiles).
- Filtro y contenidos por seccional (número del código: 7A, 7B y 7G = 7): la primera versión se eliminó; falta definir cómo será.
- Códigos sin circuito registrado: dic_circuitos.csv cubre 14A, 5E, 7G y 9G; faltan 6A, 2R y 4.
- Galería de fotos genéricas: la rotación automática (hash del id módulo cantidad) reparte mal en rampas (11 de las 22 obras sin foto salen con `rampas/2.png`), y esa es la foto más borrosa de la galería (nitidez 491). Cambiar o sacar esa foto, o mejorar la rotación. Confirmar también desde qué carpeta publica Vercel: si publica la raíz del repo, hace falta `galeria/` también en la raíz.

## Traspaso · pasada de UX del tablero (30/10)
- Hecho: cabecera mínima (48 px); barra de contexto sticky con zona, período y fechas reales, y color por período; tres pestañas (Periódicos pasó al final de Resumen como «Otras lecturas»); fechas en el selector de período; KPIs plegados en «Datos del parte»; en Semana, tarjetas con «en N de 5 partes · último dd/mm», ordenadas por partes; botón Abrir/Cerrar todas.
- Archivos: tools/plantilla.html (solo CSS, body y funciones de interfaz; obraCard suma la fecha del último parte), salida y deploy/index.html, index.html de la raíz. Ningún generador de textos ni regla del Chequeo cambió.
- Antes: la plantilla subida era vieja (sin seccional ni SMS); se reconstruyó desde el index.html publicado. Las fotos y docs del 29/10 se sacaron del tablero publicado a entrada/_cache (no venían en el zip). Usar esta plantilla de ahora en adelante.
- Estado: build listo y verificado (sin errores de consola, Chequeo todo ✔, buscador conserva el foco, 3,2 MB); publicado en main a pedido de Tomás para verlo en Vercel.
- Pendiente y dudas: el repo figura público en GitHub (CLAUDE.md dice privado): pasarlo a privado. Las fotos se recomprimen dos veces (pérdida mínima); con el Drive original, volver a bajarlas con fetch_docs.py.

## Traspaso · galería de fotos genéricas por tipo de obra (06/11)
- Hecho: `galeria()` en build.py (assets/galeria/<rubro>/, 1200 px, JPEG 75, por nombre de archivo, peso de la galería y total en la salida). En la plantilla: fotos en orden propia, parte y galería; miniaturas rotuladas; tira "Fotos genéricas de <rubro>"; genérica automática que rota por id con su aviso; sufijo `_generica` en el PNG; tag "Foto genérica"; dos líneas nuevas en el Chequeo. Probado en el 29/10 con una galería temporal (3 de hormigón y 2 de plaza): hormigón con foto del parte (la del parte va primero), hormigón sin foto (genérica, aviso, cambio, encuadre y zoom), rampas sin galería (sin cambios) y encuadre que persiste al recargar. Sin errores de consola, Chequeo todo ✔.
- Pendiente: la galería se cargó (en main, en `galeria/` de la raíz) y se movió a `assets/galeria/` con git mv, sin tocar los originales. Ver la sección «Galería: fotos cargadas y build con genéricas (06/11)».
- Archivos: tools/build.py, tools/plantilla.html, deploy/index.html, index.html (raíz) y este archivo. Anuncios no cambia (no comparte plantilla ni build) y no se regeneró.
- Estado: subido a novedades (f40e7cd), sin publicar. Lo sigue la sección de abajo.
- Dudas: con las fotos reales, revisar el peso (cada foto suma unos 50 a 150 KB). La rotación de la genérica es fija por obra y la genérica elegida a mano no se recuerda al recargar (solo el encuadre). Las piezas generales y periódicas de plazas, rampas y pavimentación también salen con genérica: confirmar si se quiere así.

## Traspaso · galería: fotos cargadas y build con genéricas (06/11)
- Hecho: merge de origin/main en novedades (sin conflictos) y `git mv galeria assets/galeria`, con los originales intactos. Fotos por rubro: mant 4, frio 4, rampas 4, bacheo 4, rehab 4, hormigon 4, pav 9 y plaza 4 (37 PNG de 990×660 px a 96 dpi, unos 56 MB en el repo). Recomprimidas, la galería pesa 7,8 MB y el tablero total 11,0 MB (más de 10 MB). Se corrigió que `liviana()` midiera en puntos: con 96 dpi bajaba las PNG a 742×495. Para la galería ahora mide en píxeles (`por_pixel=True`) y quedan en 990×660; las fotos del parte no cambian.
- Verificado (29/10): en mant, frio, rampas, bacheo, hormigon, pav y plaza, una obra sin foto del parte sale con genérica y aviso, y la tira "Fotos genéricas de …" muestra todas las miniaturas. Rehab no tiene obras sin foto ese día: su tarjeta (con foto del parte) muestra la tira y el aviso aparece al elegir una genérica. Chequeo: "Rubros sin galería: ninguno", 45 obras "salen con foto genérica", 0 "solo texto", todo ✔. Sin errores de consola.
- Pendiente: el peso. Resuelto en el traspaso siguiente: la galería pasó a archivos sueltos.
- Estado: subido a novedades (6cd002b), sin publicar. Lo sigue la sección de abajo.
- Dudas: las genéricas miden 660 px de lado corto (menos de 720), así que "Sugerido" siempre elige Círculo con ellas; los otros diseños se eligen a mano. Las piezas generales y periódicas de plazas, rampas y pavimentación también salen con genérica.

## Traspaso · galería como archivos sueltos, Sugerido y elección persistente (06/11)
- Hecho: `galeria()` escribe las genéricas en `deploy/galeria/<rubro>/<nombre>.jpg` (990 px, JPEG 75; se borra y se vuelve a escribir en cada build) y las copia a `salida/<fecha>/galeria/`. En el tablero van solo las rutas relativas. Tablero: 3,2 MB (antes 11,0 MB). `deploy/galeria/`: 5,8 MB en 37 JPG. En la plantilla: Sugerido sin umbral de 720 px para las genéricas (Foto completa o Marco si es horizontal y nítida); la genérica elegida a mano se guarda por obra (`gal` en `gc_obras_fotos`); si el lienzo no se puede leer (archivo local), no hay error de consola y el PNG avisa en vez de fallar.
- Middleware: `deploy/middleware.js` tiene `matcher: '/(.*)'` antes y después (sin cambios), así que cubre `/galeria/*` y la pide con usuario y clave. `deploy/vercel.json` aplica sus cabeceras (`noindex`, `no-store`) a `/(.*)`, también sin cambios. No se verificó en Vercel: esta sesión no tiene acceso al proyecto.
- Verificado (29/10, servido por HTTP desde `deploy/`): las 45 obras con genérica cargan sus miniaturas y dibujan la placa sin errores de consola ni respuestas fallidas, y el lienzo es legible. Sugerido: 21 Marco, 13 Foto completa y 11 Círculo, estas por `rampas/2.png`, que es borrosa. Hormigón en Rondeau: Marco. Una genérica elegida a mano persiste al recargar (también en una obra con foto del parte), y al volver a "Parte 1" se borra la elección. El PNG bajó como `hormigon_rondeau_4x5_generica.png`. Chequeo todo ✔, rubros sin galería: ninguno.
- Estado: build listo en novedades. Sin publicar; main no se tocó.
- Dudas: (1) Desde qué carpeta publica Vercel. El tablero apunta a `galeria/` al lado de `index.html`: si se publica `deploy/`, está bien; si se publica la raíz del repo (que tiene su propia copia de `index.html`), falta `galeria/` en la raíz y las genéricas no cargan. (2) La rotación en rampas cae seguido en `rampas/2.png`, que es borrosa. (3) Desde `salida/` abierto con doble clic no se pueden bajar PNG con genérica.
