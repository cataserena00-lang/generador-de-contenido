# GENERADOR DE CONTENIDO · Prensa, Gobierno de la Provincia de Córdoba

Este archivo lo lee cualquier Claude Code que abra la carpeta, sin importar la cuenta. Es el contexto compartido del equipo (2 personas). Las mismas reglas están en las instrucciones del Proyecto de Claude Team (`para_proyecto/INSTRUCCIONES_DEL_PROYECTO.md`).

## Alcance
El generador convierte información oficial del día en contenido de prensa: copys de Instagram, textos para X (máx. 280), texto de placa editable, gacetillas, placas PNG (1:1, 4:5, 9:16) y lecturas periódicas. Hoy hay un solo módulo, OBRAS (parte diario de obras). Va a crecer en módulos de otros temas y a toda la provincia.
Las demás carpetas (`tablero`, `tablero-electoral-planificador`, `tablero-viviendas-serca`) son otros proyectos: no se tocan.

## Dónde está cada cosa
- Código: `tools/` (`fetch_docs.py`, `parse_lista.py`, `build.py`, `plantilla.html`). Datos fijos: `data/`. Marca: `assets/`. Partes: `entrada/<fecha>/`. Salida: `salida/`. Publicación: `deploy/`.
- Detalle del módulo de obras (flujo, reglas de datos, errores resueltos, pendientes): `para_proyecto/subir/modulo_obras.md`. Leerlo antes de trabajar en obras.
- Marca resumida: `para_proyecto/subir/marca_resumen.md`. Esquema de datos: `para_proyecto/subir/esquema_parte.md`.
- Regenerar los archivos para el Proyecto de Claude: `python para_proyecto/armar_para_proyecto.py`.

## Regla innegociable
Nunca inventar datos: montos, cifras, metros, plazos, empleo, nombres, citas. Si falta un dato, el texto no lo lleva y se marca en el Chequeo de calidad. Ante una duda que pueda salir cara, preguntar antes.

## Flujo diario de obras
1. Guardar el parte tal cual en `entrada/<fecha>/lista.txt`.
2. `python tools/fetch_docs.py <fecha>` y `python tools/parse_lista.py <fecha>`. El total leído debe igualar el encabezado.
3. Cargar `finalizadas` en `data/finalizadas.json` (stock acumulado; sin dato nuevo se arrastra).
4. Redactar a mano `entrada/<fecha>/redactar.py` y correrlo: genera `contenido.json` (generales, periódicos, por tipo).
5. `python tools/build.py <fecha>`. Verificar en el navegador: sin errores de consola, Chequeo de calidad todo ✔, X ≤ 280.
6. Mostrar el resultado y pedir confirmación. No publicar sin un "sí" explícito.

## Reglas de redacción (todos los módulos)
- Jamás "circuito" ni "seccional" en textos publicables: hablar de barrios, siempre con "Barrio" delante.
- Sin montos ni signos de pesos. Sin "/" (usar "y"; los links quedan). Sin números sueltos.
- Orden institucional: "Gobierno de la Provincia en conjunto con la Municipalidad de Córdoba". Tono de prensa.cba.gov.ar.
- Una línea política corta y variada en cada copy de IG y X (con equilibrio fiscal se sostiene la inversión en infraestructura de todos los cordobeses). Las definiciones largas de programa, solo en gacetillas.
- Planes y metas: "prevé" o "contempla". X nunca cortado.

## Reglas de datos clave
- Una esquina es UNA obra. Rampas sin barrio; placas dicen "Rampas en ejecución".
- El código de circuito del parte gana ("-6ª" = 6A); es dato interno.
- `finalizadas` es un stock; 1.100 cuadras y 2.100 rampas son planes.
- Los periódicos cuentan días hábiles y avisan si faltan partes.

## Cuidados técnicos (Windows, PowerShell 5.1)
- Archivos en UTF-8 sin BOM (`vercel.json` con BOM rompe el build). Usar `PYTHONIOENCODING=utf-8`.
- PowerShell rompe `$` y comillas en parches multilínea: editar con el editor o con scripts de Python.
- No hay git, node ni PIL en esta máquina; se usa PyMuPDF para PDF e imágenes.
- Fotos del tablero: se recomprimen a 1500 px; el bundle debe quedar bajo 10 MB.

## Publicación
Repo privado de GitHub `cataserena00-lang/generador-de-contenido` y proyecto de Vercel con el mismo nombre. Se sube `deploy/index.html` por la web de GitHub y Vercel despliega solo (confirmar el commit al terminar la barra de carga). Acceso con Basic Auth: variables TABLERO_USUARIO y TABLERO_CLAVE en Vercel. Verificar despliegue Ready y que el sitio responde 401 sin credenciales.
Nunca escribir claves, tokens ni usuarios en archivos, chats ni documentos. Archivos con secretos (por ejemplo `PARA_TOMAS_configurar_Vercel.md`) no se suben ni se citan.

## Trabajo en equipo
- Un solo responsable del deploy: quien tiene las cuentas de GitHub y Vercel. La otra persona deja el build listo y avisa.
- No trabajar dos personas sobre el mismo día, parte o módulo a la vez: avisar al empezar y al cerrar.
- Al cerrar cada tarea, dejar un traspaso de 5 líneas: qué se hizo, qué queda, archivos tocados, estado (borrador, build listo o publicado), dudas. Actualizar los pendientes en `para_proyecto/subir/modulo_obras.md`.
- Cambios de código: uno por vez, con el motivo. Nada destructivo en git (reset --hard, push --force, checkout o clean sobre cambios ajenos, borrar ramas): solo commits nuevos.

## Pendientes y decisiones abiertas
- Plaza Barrios Unidos vs. Plaza Centro América: ¿son la misma? Agregar el alias solo con confirmación.
- Filtro y contenidos por seccional (número del código): la primera versión se eliminó; falta definir cómo será.
- Periódicos de 15 y 30 días: faltan partes.
- Alcance provincial: definir organismos, marcas, identificación de zona y quién valida los datos de cada fuente.
