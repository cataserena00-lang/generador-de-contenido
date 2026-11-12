// Acceso por usuario y contraseña (HTTP Basic) validado en el servidor.
// Las credenciales viven en variables de entorno de Vercel, nunca en el HTML ni en el repositorio:
//   TABLERO_ACCESOS                  una credencial por línea, con el formato usuario:clave (una por persona).
//                                    Las líneas vacías y las que empiezan con # se ignoran.
//   TABLERO_USUARIO / TABLERO_CLAVE  la credencial compartida original; sigue valiendo mientras esté cargada.
// Si no hay ninguna credencial cargada, el sitio queda cerrado.
export const config = { matcher: '/(.*)' };

const cerrado = (status, headers = {}) =>
  new Response(status === 503 ? 'Sitio no configurado.' : 'Acceso restringido.', {
    status,
    headers: { 'content-type': 'text/plain; charset=utf-8', 'cache-control': 'no-store', ...headers },
  });

function igual(a, b) {
  if (a.length !== b.length) return false;
  let r = 0;
  for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}

// Credenciales habilitadas. Se leen en cada pedido: al cambiar la variable y redesplegar, el cambio vale enseguida.
function accesos() {
  const lista = (process.env.TABLERO_ACCESOS || '')
    .split('\n')
    .map(l => l.trim())
    .filter(l => l && l[0] !== '#')
    .map(l => { const i = l.indexOf(':'); return i > 0 ? [l.slice(0, i), l.slice(i + 1)] : null; })
    .filter(c => c && c[1]);                                  // sin usuario o sin clave, la línea no habilita a nadie
  const user = process.env.TABLERO_USUARIO, pass = process.env.TABLERO_CLAVE;
  if (user && pass) lista.push([user, pass]);
  return lista;
}

export default function middleware(request) {
  const habilitados = accesos();
  if (!habilitados.length) return cerrado(503);

  const auth = request.headers.get('authorization') || '';
  if (auth.startsWith('Basic ')) {
    try {
      const dec = new TextDecoder().decode(Uint8Array.from(atob(auth.slice(6)), c => c.charCodeAt(0)));
      const i = dec.indexOf(':');                             // la clave puede tener ":": corta en el primero
      if (i > -1) {
        const usuario = dec.slice(0, i), clave = dec.slice(i + 1);
        if (habilitados.some(([u, c]) => igual(u, usuario) && igual(c, clave))) {
          return new Response(null, { headers: { 'x-middleware-next': '1' } });
        }
      }
    } catch (_) { /* credencial mal formada */ }
  }
  return cerrado(401, { 'www-authenticate': 'Basic realm="Tablero de obras", charset="UTF-8"' });
}
