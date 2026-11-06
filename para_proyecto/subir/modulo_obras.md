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
- Sumar fotos: soltar los archivos (.jpg, .jpeg, .png o .webp) en la carpeta del rubro y volver a correr `python tools/build.py <fecha>`. No hace falta tocar código. El build las recomprime a 1200 px, JPEG calidad 75, las ordena por nombre de archivo e imprime el peso de la galería y el del tablero. Una carpeta nueva solo sirve si su nombre es una de las claves.
- En la tarjeta, la fila "Foto:" muestra miniaturas ("Propia", "Parte 1", "Parte 2"…). Debajo va la tira "Fotos genéricas de <rubro>" con las de la galería, y la miniatura elegida lleva borde del color del eje. Si la obra no trae foto del parte ni propia, se elige sola una genérica que rota según el id de la obra, y debajo de la placa aparece "Foto genérica del tipo de obra. Podés elegir otra o subir la tuya". El diseño "Sin foto" sigue disponible. Las piezas por tipo (plazas, rampas y pavimentación) usan la galería de su rubro.
- Etiqueta "Foto genérica" (gris con texto marino) cuando la obra solo tiene genérica. El filtro Con foto / Sin foto sigue contando la foto del parte. El PNG bajado con una genérica lleva el sufijo `_generica`.
- Chequeo: "Obras sin foto del parte (salen con foto genérica)" para los rubros con galería y "Rubros sin galería: …" para saber qué carpetas faltan cargar.
- Las fotos vienen del build (van dentro del tablero), no del navegador. El encuadre y el zoom de cada genérica se guardan por obra y por foto, como los de las otras fotos.

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
- Galería de fotos genéricas: el tablero pesa 11,0 MB con la galería (pasa de 10 MB). Decidir: servir la galería como archivos sueltos en `deploy/galeria/` o achicar las fotos (a 742 px de lado el tablero pesaba 7,5 MB).

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
- Hecho: merge de origin/main en novedades (sin conflictos) y `git mv galeria assets/galeria`, con los originales intactos. Fotos por rubro: mant 4, frio 4, rampas 4, bacheo 4, rehab 4, hormigon 4, pav 9 y plaza 4 (37 PNG de 990×660 px a 96 dpi, unos 58 MB en el repo). Recomprimidas, la galería pesa 7,8 MB y el tablero total 11,0 MB (más de 10 MB). Se corrigió que `liviana()` midiera en puntos: con 96 dpi bajaba las PNG a 742×495. Para la galería ahora mide en píxeles (`por_pixel=True`) y quedan en 990×660; las fotos del parte no cambian.
- Verificado (29/10): en mant, frio, rampas, bacheo, hormigon, pav y plaza, una obra sin foto del parte sale con genérica y aviso, y la tira "Fotos genéricas de …" muestra todas las miniaturas. Rehab no tiene obras sin foto ese día: su tarjeta (con foto del parte) muestra la tira y el aviso aparece al elegir una genérica. Chequeo: "Rubros sin galería: ninguno", 45 obras "salen con foto genérica", 0 "solo texto", todo ✔. Sin errores de consola.
- Pendiente: el peso. Alternativas: servir la galería como archivos sueltos en `deploy/galeria/` (el HTML guardaría solo las rutas; el tablero vuelve a unos 3,2 MB) o volver a 742 px de lado (7,5 MB).
- Estado: build listo en novedades. Sin publicar; main no se tocó.
- Dudas: las genéricas miden 660 px de lado corto (menos de 720), así que "Sugerido" siempre elige Círculo con ellas; los otros diseños se eligen a mano. Las piezas generales y periódicas de plazas, rampas y pavimentación también salen con genérica.
