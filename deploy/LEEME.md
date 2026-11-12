# Publicar el tablero con usuario y contraseña (Vercel)

Esta carpeta es el proyecto completo:
- `index.html` el tablero de obras (lo actualiza `python tools/build.py <fecha>`) y `anuncios.html` el de anuncios (`python tools/build_anuncios.py <fecha>`).
- `galeria/` las fotos genéricas por tipo de obra (las escribe el mismo build, como archivos sueltos). Se publican junto con `index.html`.

**La raíz del repo y `deploy/` tienen que ir siempre iguales.** Todavía no está confirmado cuál de las dos publica Vercel (Root Directory). Por eso la raíz lleva copias de `index.html`, `anuncios.html`, `middleware.js`, `vercel.json`, `robots.txt` y `galeria/`. El build copia `galeria/` a la raíz solo (y borra la copia anterior: la reconoce por `_copia_de_deploy_galeria.txt`). Cada build escribe además su html en la raíz (`index.html` desde obras, `anuncios.html` desde anuncios): la raíz y `deploy/` quedan iguales sin pasos manuales. `middleware.js`, `vercel.json` y `robots.txt` se copian a mano solo si cambian.
- `middleware.js` pide usuario y contraseña en el servidor (HTTP Basic). Cada persona tiene su credencial (ver "Quién puede entrar"). Si no hay ninguna cargada, el sitio responde 503 y queda cerrado.
- `vercel.json` evita que Google lo indexe y que se guarde en caché.

## Primera vez
1. Subir esta carpeta a Vercel (una de las dos):
   - **Con Node:** instalar Node.js, abrir una terminal en esta carpeta y correr `npx vercel` (inicia sesión en el navegador), luego `npx vercel --prod`.
   - **Sin Node:** subir la carpeta `deploy` a un repositorio **privado** de GitHub e importarlo desde vercel.com/new (Framework: "Other").
2. En Vercel: Project → Settings → Environment Variables, cargar en **Production** la variable `TABLERO_ACCESOS`, con una credencial por línea (ver "Quién puede entrar").
3. Redeploy (Deployments → ⋯ → Redeploy). Desde ahí el link pide usuario y contraseña.

## Cada día
`python tools/build.py <fecha>` y volver a publicar (`npx vercel --prod`, o commit/push si usás GitHub).

## Quién puede entrar
Cada persona entra con su propio usuario y su propia clave. Todas viven en la variable `TABLERO_ACCESOS` de Vercel, una por línea, con el formato `usuario:clave`:

```
unusuario:una-clave-larga
otrousuario:otra-clave-larga
```

- **Alta:** agregar una línea y hacer Redeploy.
- **Baja:** borrar esa línea y hacer Redeploy. A las demás personas no les cambia nada.
- **Cambio de clave:** editar esa línea y hacer Redeploy.

Detalles del formato: las líneas vacías y las que empiezan con `#` se ignoran (sirven para anotar quién es quién); la clave puede tener `:` adentro porque el corte es en el primero; no poner espacios al final; distingue mayúsculas de minúsculas.

`TABLERO_USUARIO` y `TABLERO_CLAVE` son la credencial compartida original y siguen valiendo mientras estén cargadas, así que nadie pierde el acceso al migrar. Cuando cada persona tenga la suya, conviene borrarlas: una clave que saben todos no se puede dar de baja por persona.

### Cuidados
- Las credenciales se cargan **solo** en Vercel. Nunca en el repositorio, en un documento, en un correo ni en un chat.
- A cada persona se le pasa su clave por un canal distinto del que lleva el link, y se le pide que no la reenvíe.
- Conviene una clave larga y al azar por persona, distinta de las que usa para otros sistemas.

### Generar una clave al azar
En PowerShell, una clave de 16 caracteres:

```
-join ((48..57)+(65..90)+(97..122) | Get-Random -Count 16 | % {[char]$_})
```

Correrlo una vez por persona, copiar el resultado a Vercel y a quien corresponda, y después cerrar la terminal para que no quede en pantalla ni en el historial.

