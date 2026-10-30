// Acceso por usuario y contraseña (HTTP Basic) validado en el servidor.
// Las credenciales viven en variables de entorno de Vercel (TABLERO_USUARIO / TABLERO_CLAVE),
// nunca en el HTML. Si no están cargadas, el sitio queda cerrado.
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

export default function middleware(request) {
  const user = process.env.TABLERO_USUARIO;
  const pass = process.env.TABLERO_CLAVE;
  if (!user || !pass) return cerrado(503);

  const auth = request.headers.get('authorization') || '';
  if (auth.startsWith('Basic ')) {
    try {
      const dec = new TextDecoder().decode(Uint8Array.from(atob(auth.slice(6)), c => c.charCodeAt(0)));
      const i = dec.indexOf(':');
      if (i > -1 && igual(dec.slice(0, i), user) && igual(dec.slice(i + 1), pass)) {
        return new Response(null, { headers: { 'x-middleware-next': '1' } });
      }
    } catch (_) { /* credencial mal formada */ }
  }
  return cerrado(401, { 'www-authenticate': 'Basic realm="Tablero de obras", charset="UTF-8"' });
}
