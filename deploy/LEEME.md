# Publicar el tablero con usuario y contraseña (Vercel)

Esta carpeta es el proyecto completo:
- `index.html` el tablero (lo actualiza `python tools/build.py <fecha>`).
- `galeria/` las fotos genéricas por tipo de obra (las escribe el mismo build, como archivos sueltos). Se publican junto con `index.html`.

**La raíz del repo y `deploy/` tienen que ir siempre iguales.** Todavía no está confirmado cuál de las dos publica Vercel (Root Directory). Por eso la raíz lleva copias de `index.html`, `anuncios.html`, `middleware.js`, `vercel.json`, `robots.txt` y `galeria/`. El build copia `galeria/` a la raíz solo (y borra la copia anterior: la reconoce por `_copia_de_deploy_galeria.txt`). `index.html` y `anuncios.html` se siguen copiando a mano después de cada build.
- `middleware.js` pide usuario y contraseña en el servidor (HTTP Basic). Si las variables no están cargadas, el sitio responde 503 y queda cerrado.
- `vercel.json` evita que Google lo indexe y que se guarde en caché.

## Primera vez
1. Subir esta carpeta a Vercel (una de las dos):
   - **Con Node:** instalar Node.js, abrir una terminal en esta carpeta y correr `npx vercel` (inicia sesión en el navegador), luego `npx vercel --prod`.
   - **Sin Node:** subir la carpeta `deploy` a un repositorio **privado** de GitHub e importarlo desde vercel.com/new (Framework: "Other").
2. En Vercel: Project → Settings → Environment Variables, cargar (Production):
   - `TABLERO_USUARIO` = el usuario que quieras
   - `TABLERO_CLAVE` = la contraseña
3. Redeploy (Deployments → ⋯ → Redeploy). Desde ahí el link pide usuario y contraseña.

## Cada día
`python tools/build.py <fecha>` y volver a publicar (`npx vercel --prod`, o commit/push si usás GitHub).
Para cambiar la clave: editar las variables y hacer Redeploy.

