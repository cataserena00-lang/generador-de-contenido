# Paso a paso: pasar el Generador de contenido a un Proyecto de Claude Team

La pantalla de Claude puede variar un poco; los nombres de los botones son orientativos.
Hay dos lugares donde trabaja el equipo: el chat del Proyecto en claude.ai (redactar y revisar) y Claude Code sobre la carpeta (correr el build). Cada uno tiene su propio paso.

## Parte A. Proyecto en claude.ai (Team)
1. **Preparar los archivos.** Pedile a Claude Code que corra `python para_proyecto\armar_para_proyecto.py`. Revisá que `para_proyecto\subir\` tenga 13 archivos y que no esté `PARA_TOMAS_configurar_Vercel.md` (tiene un token).
2. **Crear el Proyecto.** En claude.ai, con la cuenta Team, Proyectos → nuevo. Nombre: "Generador de contenido". Descripción: "Contenido de prensa para la provincia. Módulo activo: Obras". Compartido con el equipo, no privado.
3. **Pegar las instrucciones.** Copiá todo `para_proyecto\INSTRUCCIONES_DEL_PROYECTO.md` (5.413 caracteres) en "Instrucciones del proyecto".
4. **Subir el conocimiento.** Subí los archivos de `para_proyecto\subir\`. Si el límite aprieta, sacá primero `codigo_plantilla.md` (78 KB) y después `codigo_pipeline.md`. No subas `salida\`, `deploy\index.html`, `entrada\_cache`, `assets\`, los PDF de "Listados por grupo" ni archivos con claves.
5. **Sumar a la segunda persona.** Compartí el Proyecto con su correo de la cuenta Team, con permiso para usar y editar.
6. **Probar.** En un chat nuevo del Proyecto pedí: "Con la muestra del parte, redactá el copy de Instagram de la obra Av. Patria". Tiene que respetar las reglas (sin "circuito", sin montos, con "Barrio") y no inventar datos.

## Parte B. Claude Code sobre la carpeta (para correr el build)
1. **Compartir la carpeta.** El código (`tools/`, `data/`, `entrada/`) solo está en tu computadora. Elegí una: compartir la carpeta del proyecto por OneDrive con la otra persona, o subir el código a un repositorio privado (sin `entrada\_cache`, `salida\` ni claves).
2. **Abrir la carpeta con Claude Code.** Cada persona la abre desde su cuenta. Claude lee `CLAUDE.md` solo y ya tiene el contexto, sin subir nada.
3. **Usarlo.** El build diario (`fetch_docs.py`, `parse_lista.py`, `build.py`) se corre acá. GitHub y Vercel siguen en tu cuenta y publicás solo vos.

## Parte C. Mantenerlo al día
1. Cuando cambie el parte, el código o los datos, pedile a Claude Code que corra de nuevo `armar_para_proyecto.py`.
2. Reemplazá en el Proyecto de claude.ai solo los archivos que cambiaron (normalmente `muestra_parte.json`, `historico_resumen.csv` y `modulo_obras.md`).
3. Al cerrar cada tarea, dejá un traspaso de 5 líneas y actualizá los pendientes en `modulo_obras.md` y en `CLAUDE.md`.
4. Avisale a la otra persona cuando subas cambios al Proyecto, para que no trabaje con archivos viejos.

## Parte D. Cuando sumen un tema nuevo
1. Escribí `modulo_<tema>.md` con la misma estructura que `modulo_obras.md`, más su esquema, su muestra y sus diccionarios.
2. Subilos al Proyecto.
3. Actualizá la tabla "Estado de módulos" en las instrucciones y en `CLAUDE.md`.
