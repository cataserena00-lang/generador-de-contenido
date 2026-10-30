# Esquema de los datos del día

Ver `dic_campos_parte.csv`. Cada día: `entrada/<fecha>/lista.txt` (pegado del parte) → `parte.json` → `contenido.json` (redactado a mano) → `salida/<fecha>/tablero.html`.

## Reglas de datos
- No se inventa ningún dato: lo que falta queda fuera del texto.
- Una esquina con varias rampas es UNA obra. `finalizadas` es un stock acumulado.
- 1.100 cuadras y 2.100 rampas son planes ('prevé', 'contempla').
- El circuito es dato interno; los textos hablan de barrios.

## Campos
- `fecha` (texto AAAA-MM-DD): Día del parte. Ej.: 2026-10-29
- `fecha_texto` (texto): Fecha escrita para el encabezado. Ej.: jueves 29 de octubre de 2026
- `enEjecucion` (entero): Obras en ejecución según el encabezado del parte (control contra los ítems leídos). Ej.: 61
- `puestos` (entero): Puestos de trabajo directos del día (dato de toda la ciudad). Ej.: 599
- `finalizadas` (entero o null): STOCK acumulado de obras finalizadas (no es del día); se usa solo para acumulados. Ej.: 192
- `acumulados` (objeto): Metas de plan: cuadras_pavimentadas 1100 y rampas_programa 2100. Son planes: se dice 'prevé' o 'contempla'
- `programaRampas` (objeto): Del doc del programa: total 2100, nuevas 2000, en_esquinas_sin_rampa 1317, reparadas 100
- `avisos` (lista de texto): Contradicciones parte vs. docs y códigos sin circuito; se muestran en 'Chequeo de calidad'
- `obras[].id` (texto): <tipo>_<slug de la calle o sector> (+ slug de entre-calles si hay duplicado). Ej.: hormigon_av-patria
- `obras[].tipo` (texto): mant, frio, rampas, bacheo, rehab, hormigon, pav, plaza. Ej.: hormigon
- `obras[].circuito` (texto): Código del parte (número + letra opcional). Dato interno: nunca se publica. Ej.: 6
- `obras[].via / entre` (texto o null): Calle y entre-calles (bacheo, rehab, hormigón, rampas, plazas). Ej.: Av. Patria / Av. 24 de Septiembre y Armenia
- `obras[].sector` (texto o null): Nombre del sector en mant, frio y pav. Ej.: Policial Etapa II
- `obras[].barrio` (texto o null): Barrio; en los textos siempre con el prefijo 'Barrio'. Ej.: Hogar Propio
- `obras[].rampas` (entero o null): Cantidad de rampas de la esquina (o del grupo). Ej.: 4
- `obras[].doc` (texto o null): Clave del Google Doc de la obra (fotos y texto en entrada/_cache). Ej.: av_patria
- `obras[].grupo` (booleano): true = resumen de rampas (zona céntrica o Pueyrredón); no cuenta como obra. Ej.: false
- `obras[].estado` (texto): ejecucion o terminada. Ej.: ejecucion
- `obras[].nota` (lista): Nocturno, 3.ª etapa, 2.ª intervención, o 'N rampas'
- `obras[].barrio_inferido / circ_inferido` (texto / booleano): Marcas de que el dato no vino en el parte
- `obras[].metricas` (objeto): driveUrl, m2, ml, cuadras, plazo, nocturno, esquinas. Si no hay dato, el texto no lleva magnitud
- `contenido.json` (objeto): Piezas redactadas a mano del día: generales{id:{titulos,ig,x,gac,placa}} y periodicos{id:{titulo,eje,titulos,ig,x,placa,gac}}
