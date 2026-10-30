# Cómo se asigna cada dato del parte (reglas del tablero original)

Estas reglas las implementa `tools/parse_lista.py`.

## 1. Rubro
- El rubro es el título de cada sección: Mantenimiento de calles, Bacheo en frío, Rampas, Bacheo con asfalto,
  Rehabilitación con asfalto, Rehabilitación y bacheo con hormigón, Pavimentación, Plazas.
- Cada línea numerada pertenece al último título visto. "EN EJECUCIÓN" o "TERMINADAS" debajo del título fija el estado.
- Una línea sin número no es un ítem, salvo las rampas, que se detectan por el "· N rampas".
- Un link suelto se pega al ítem anterior. Un link en la misma línea va a ese ítem.

## 2. Calle, entre-calles y nota
- Se separan por "e/" o "entre". Si la línea solo trae "A y B", queda como esquina.
- Notas: "(Nocturno)", "(2da intervención)" y "3er etapa" pasan a nota. En rampas, la nota es la cantidad ("3 rampas").
- Rampas: "x" se convierte en "y"; "J:M." o "J.Mm" quedan como "J. M.".

## 3. Barrio
- "BARRIO:xxx" (o "B°", "Barrio xxx") es el barrio.
- En Mantenimiento y Bacheo en frío la línea completa es el barrio, salvo que sea una calle con "e/" o "entre" (no se infiere).
- Si no hay barrio, se toma el de otro ítem del mismo parte con el mismo código. Si tampoco, "Sin barrio informado".
- Las rampas van siempre "Sin barrio informado": no se les infiere barrio.
- Se normaliza sin mayúsculas ni tildes y se muestra la primera grafía que aparece en el parte.

## 4. Circuito (código), en este orden
1. Código explícito del parte ("-14N", "-9", "-1"): gana siempre.
2. Línea que termina en "-" sin código (solo rampas): hereda el de la rampa anterior (inferido).
3. Sin código pero con barrio: el código de otro ítem del mismo barrio en ese parte (inferido).
4. Tabla barrio→circuito (último recurso). Tolera "Etapa II" al final y "B°"/"Barrio" al inicio.
5. Código explícito que no existe como circuito: se descarta, se usa el de la tabla y se marca "revisar".
6. Sin código y sin barrio en la tabla: sin circuito ("?").

## 5. Nombre del circuito
Sale de la tabla (`data/circuitos.json`), no del parte: el primer nombre registrado para ese código.

## 6. Actualización de la tabla barrio→circuito
- El código del parte gana: si un parte trae un barrio con otro código que la tabla, se corrige.
- Excepción 1: un código sin letra (ej. "-9") no pisa uno con letra del mismo barrio.
- Excepción 2: un código inválido no se toma.

## Dónde puede fallar
- Rampas: muestran el circuito pero no se sabe el barrio.
- Ítems sin código tomados de la tabla: pueden estar desactualizados.
- Barrios que no están en la tabla (Villa Aspacia, Gral. Paz): quedan con el código del parte, sin control cruzado.

## Ajustes propios de este generador (marcados en "Chequeo de calidad")
- Pavimentación: si el parte no informa barrio, se usa el que figura en la memoria descriptiva de la obra, antes que
  inferirlo por código (un circuito agrupa varios barrios).
- Los textos publicables nunca nombran el circuito: hablan de barrios.
