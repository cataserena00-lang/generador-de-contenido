# Plantilla del tablero (HTML, CSS y JavaScript)

Código fuente concatenado. Los secretos están ocultos como `***OCULTO***`.

## tools/plantilla.html

~~~~html
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Generador de contenido</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cdefs%3E%3CclipPath id='c'%3E%3Crect width='32' height='32' rx='5'/%3E%3C/clipPath%3E%3C/defs%3E%3Cg clip-path='url(%23c)'%3E%3Crect width='10.7' height='32' fill='%23bc1734'/%3E%3Crect x='10.66' width='10.7' height='32' fill='%23ffffff'/%3E%3Crect x='21.32' width='10.7' height='32' fill='%236caee5'/%3E%3C/g%3E%3Cg stroke='%23b8893a' stroke-width='1.5' stroke-linecap='round'%3E%3Cline x1='23.20' y1='16.00' x2='26.40' y2='16.00'/%3E%3Cline x1='22.24' y1='19.60' x2='25.01' y2='21.20'/%3E%3Cline x1='19.60' y1='22.24' x2='21.20' y2='25.01'/%3E%3Cline x1='16.00' y1='23.20' x2='16.00' y2='26.40'/%3E%3Cline x1='12.40' y1='22.24' x2='10.80' y2='25.01'/%3E%3Cline x1='9.76' y1='19.60' x2='6.99' y2='21.20'/%3E%3Cline x1='8.80' y1='16.00' x2='5.60' y2='16.00'/%3E%3Cline x1='9.76' y1='12.40' x2='6.99' y2='10.80'/%3E%3Cline x1='12.40' y1='9.76' x2='10.80' y2='6.99'/%3E%3Cline x1='16.00' y1='8.80' x2='16.00' y2='5.60'/%3E%3Cline x1='19.60' y1='9.76' x2='21.20' y2='6.99'/%3E%3Cline x1='22.24' y1='12.40' x2='25.01' y2='10.80'/%3E%3C/g%3E%3Ccircle cx='16' cy='16' r='5.2' fill='%23cfa55b' stroke='%239a6f27' stroke-width='.9'/%3E%3C/svg%3E">
<style>
/*__FONTS__*/
:root{
  --celeste:#6caee5; --rojo:#bc1734; --dorado:#cfa55b; --gris:#808080; --link:#2f7ec2;
  --ink:#3b3f46; --muted:#8a8f98; --bg:#f5f5f6; --card:#fff; --line:#e4e4e7;
  /* colores de eje (carteles de campaña) */
  --marino:#17233d; --amarillo:#eaab3b; --verde:#4da070; --verde-claro:#c6dfce; --celeste-eje:#bedff7;
}
*{box-sizing:border-box}
body{margin:0;font-family:Poppins,system-ui,sans-serif;background:var(--bg);color:var(--ink);font-size:14px;line-height:1.5}
header{background:#fff;padding:14px 24px 0;position:sticky;top:0;z-index:20;box-shadow:0 2px 14px #00000012}
header::after{content:"";display:block;height:5px;margin:12px -24px 0;background:linear-gradient(90deg,var(--celeste) 0 33.34%,var(--rojo) 33.34% 66.67%,var(--dorado) 66.67%)}
.top{display:flex;align-items:center;gap:18px;flex-wrap:wrap}
.top img{height:44px;display:block}
.top .ttl{border-left:1px solid var(--line);padding-left:18px}
h1{margin:0;font-weight:900;font-size:21px;line-height:1.1;color:var(--gris);letter-spacing:.2px}
.sub{color:var(--muted);font-size:12px;margin-top:3px;font-weight:600}
.kpis{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px}
.kpi{background:#fff;border:1px solid var(--line);border-top:4px solid var(--celeste);border-radius:10px;padding:5px 14px 6px;min-width:96px}
.kpi:nth-child(3n+2){border-top-color:var(--rojo)} .kpi:nth-child(3n){border-top-color:var(--dorado)}
.kpi b{display:block;font-size:21px;font-weight:900;line-height:1.15;color:var(--ink)}
.kpi span{font-size:11px;color:var(--muted);font-weight:600}
nav.tabs{display:flex;gap:6px;margin:12px 0 12px}
nav.tabs button{background:#fff;color:var(--gris);border:1px solid var(--line);border-radius:999px;padding:6px 18px;font:700 13px Poppins;cursor:pointer}
nav.tabs button.on{background:var(--rojo);color:#fff;border-color:var(--rojo)}
main{max-width:1180px;margin:0 auto;padding:18px 16px 40px}
footer{border-top:1px solid var(--line);background:#fff;padding:22px 16px;text-align:center}
footer img{height:46px;opacity:.95} footer p{margin:8px 0 0;font-size:11px;color:var(--muted);font-weight:600}
.filters{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:14px}
.filters h4{margin:0 0 6px;font-size:11px;text-transform:uppercase;letter-spacing:.7px;color:var(--gris);font-weight:800}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px}
.chip{border:1px solid var(--line);background:#fff;border-radius:999px;padding:4px 11px;font:700 12px Poppins;cursor:pointer;color:var(--ink)}
.chip small{opacity:.55;font-weight:700;margin-left:4px}
.chip.on{background:var(--rojo);color:#fff;border-color:var(--rojo)}
.chip.t-calle.on{background:var(--marino);border-color:var(--marino)} .chip.t-accesible.on{background:var(--amarillo);color:var(--marino);border-color:var(--amarillo)} .chip.t-plaza.on{background:var(--verde);border-color:var(--verde)}
.search{width:100%;max-width:320px;border:1px solid var(--line);border-radius:8px;padding:7px 10px;font:600 13px Poppins}
.search:focus,textarea:focus{outline:2px solid var(--celeste);outline-offset:0}
.count{font-size:12px;color:var(--muted);margin:2px 0 10px;font-weight:600} .count a{color:var(--link)}
.circ-head{margin:20px 0 8px;font-weight:900;font-size:16px;display:flex;gap:8px;align-items:baseline;color:var(--rojo)}
.circ-head small{font-weight:600;color:var(--gris);font-size:12px}
.card{background:var(--card);border:1px solid var(--line);border-left:6px solid var(--marino);border-radius:12px;margin-bottom:10px;overflow:hidden}
.card.e-accesible{border-left-color:var(--amarillo)} .card.e-plaza{border-left-color:var(--verde)}
.card>summary{list-style:none;cursor:pointer;padding:11px 14px;display:flex;gap:12px;align-items:center}
.card>summary:hover{background:#fafafa}
.card>summary::-webkit-details-marker{display:none}
.card .tt{flex:1;min-width:0}
.card .tt b{font-weight:700;font-size:14px;display:block;color:var(--ink)}
.card .tt span{font-size:12px;color:var(--muted);font-weight:600}
.tag{font-size:10.5px;font-weight:700;border-radius:6px;padding:2px 8px;white-space:nowrap}
.tag.calle{background:var(--celeste-eje);color:var(--marino)} .tag.accesible{background:#fbe9c2;color:#6b4a05} .tag.plaza{background:var(--verde-claro);color:#1f5a38}
.tag.foto{background:#e7f4ea;color:#1f6a35} .tag.sinfoto{background:#f1f1f1;color:#777} .tag.grupo{background:#f4e6c8;color:#7a5a1c}
.body{padding:4px 14px 16px;border-top:1px solid var(--line)}
.grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:18px;margin-top:12px}
@media(max-width:860px){.grid{grid-template-columns:1fr}.top .ttl{border-left:0;padding-left:0}}
.fmts{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.fmt{text-align:center}
.fmt canvas{width:100%;height:auto;border-radius:8px;border:1px solid var(--line);background:#eee;display:block}
.fmt .lbl{font-size:11px;font-weight:700;margin:5px 0 4px;color:var(--gris)}
.btn{border:0;border-radius:8px;padding:6px 12px;font:700 12px Poppins;cursor:pointer;background:var(--rojo);color:#fff}
.btn:hover{filter:brightness(1.08)}
.btn.sec{background:#efeff1;color:var(--ink)} .btn.ok{background:var(--verde)}
.btns{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}
.tx{margin-bottom:12px}
.tx .row{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;gap:8px}
.tx label{font-weight:800;font-size:12px;color:var(--gris)}
.tx .n{font-size:11px;color:var(--muted);font-weight:600} .tx .n.bad{color:var(--rojo);font-weight:800}
textarea{width:100%;border:1px solid var(--line);border-radius:8px;padding:8px 10px;font:600 12.5px/1.5 Poppins;resize:vertical;min-height:90px;color:var(--ink)}
.meta{font-size:12px;color:var(--muted);margin-top:10px;font-weight:600}
.meta a,details.doc summary{color:var(--link)}
details.doc{margin-top:8px;font-size:12px} details.doc summary{cursor:pointer;font-weight:700}
details.doc pre{white-space:pre-wrap;font:600 12px Poppins;background:#f7f7f8;border-radius:8px;padding:8px 10px}
.fotosel{display:flex;gap:6px;margin-top:8px;align-items:center;font-size:12px;font-weight:600}
.note{background:#fbf5e8;border:1px solid #ecd9a8;border-left:5px solid var(--dorado);border-radius:10px;padding:10px 14px;font-size:12.5px;margin-bottom:14px;font-weight:600}
.list{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin-bottom:12px}
.list h3{margin:0 0 6px;font-size:14px;font-weight:800;color:var(--rojo)} .list ul{margin:0;padding-left:18px} .list li{margin:2px 0;font-size:12.5px;font-weight:600}
.gen-grid{display:grid;gap:12px}
.titulo{display:flex;gap:8px;align-items:center;justify-content:space-between;padding:6px 10px;border:1px solid var(--line);border-radius:8px;margin-bottom:6px;font-weight:700;font-size:12.5px;background:#fafafa}
nav.tabs button.cal{margin-left:auto;background:#f0f0f1;color:#8a8f98;border-color:#e4e4e7}
nav.tabs button.cal.on{background:#8a8f98;color:#fff;border-color:#8a8f98}
.gris{background:#f3f3f4!important;border-color:#e0e0e2!important;border-left-color:#b8bcc4!important;color:#6f747d}
.gris h3{color:#6f747d!important}
.list .hint,.list h3 small{font-size:12px;color:var(--muted);font-weight:600}.list .hint{margin-bottom:6px}
</style>
</head>
<body>
<header>
  <div class="top"><img id="lockup" alt="Córdoba · Gobierno de la Provincia · Hacer para crecer"><div class="ttl"><h1>GENERADOR DE CONTENIDO</h1><div class="sub" id="sub"></div></div></div>
  <div class="kpis" id="kpis"></div>
  <nav class="tabs" id="tabs"></nav>
</header>
<main id="main"></main>
<footer><img id="lockup2" alt="Córdoba · Gobierno de la Provincia · Hacer para crecer"><p>Comunicación · Municipalidad de Córdoba · uso interno</p></footer>
<script>const DATA=/*__DATA__*/null;</script>
<script>
(()=>{
const CONT=DATA.contenido||{};
const P=DATA.parte, CIRC=DATA.circuitos, A=DATA.assets, FISCAL=(DATA.fiscal&&DATA.fiscal.cifras)||[];
const $=(s,r=document)=>r.querySelector(s), esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const nf=n=>String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g,'.');
const up=s=>s.toLocaleUpperCase('es-AR');
const EJES={
 calle:{nombre:'Calle por Calle – Córdoba Mejora',dark:'#17233d',pie:'#17233d',claro:'#bedff7',chip:'#17233d',acento:'#bedff7',emoji:'🛣️',wm:'wordmark-calle',logos:'logos-calle',tags:['#CallePorCalle','#CórdobaMejora','#HacerParaCrecer'],
   marco:'“Calle por Calle, Córdoba Mejora” es el programa que lleva adelante el Gobierno de la Provincia en conjunto con la Municipalidad de Córdoba e incluye trabajos de pavimentación, rehabilitación integral de calzadas, reparación de sectores deteriorados mediante bacheo con asfalto u hormigón, de acuerdo con las características y necesidades de cada intervención, y mantenimiento de calles de tierra.',
   corto:'Calle por Calle, Córdoba Mejora: pavimentación, rehabilitación de calzadas, bacheo y mantenimiento de calles.',
   cortos:['Calle por Calle, Córdoba Mejora: pavimentación, rehabilitación de calzadas, bacheo y mantenimiento de calles.','Calle por Calle, Córdoba Mejora: calles más cuidadas y barrios mejor conectados.','El programa Calle por Calle, Córdoba Mejora recupera las calles de la ciudad, cuadra a cuadra.'],
   contexto:'“Calle por Calle, Córdoba Mejora” incluye trabajos de pavimentación, rehabilitación integral de calzadas, reparación de sectores deteriorados mediante bacheo con asfalto u hormigón, de acuerdo con las características y necesidades de cada intervención, y mantenimiento de calles de tierra.'},
 accesible:{nombre:'Córdoba Accesible',corto:'Córdoba Accesible: una Córdoba inclusiva, pensada para todos.',
   cortos:['Córdoba Accesible: una Córdoba inclusiva, pensada para todos.','Con Córdoba Accesible, la ciudad suma rampas para que todos se muevan con autonomía.','Córdoba Accesible: más accesibilidad en el espacio público.'],dark:'#172743',pie:'#09467f',claro:'#bedff7',chip:'#eaab3b',acento:'#eaab3b',emoji:'♿',wm:'wordmark-accesible',logos:'logos-accesible',tags:['#CórdobaAccesible','#HacerParaCrecer'],
   marco:'Córdoba Accesible es el programa para una Córdoba inclusiva, pensada para todos: contempla la instalación de '+nf(P.programaRampas.total)+' rampas en el ejido capitalino y busca favorecer la autonomía, la movilidad y la integración de todos los vecinos.'},
 plaza:{nombre:'Nos vemos en la Plaza – Córdoba Mejora',corto:'Nos vemos en la Plaza, Córdoba Mejora: espacios verdes para el encuentro, el juego y el deporte.',
   cortos:['Nos vemos en la Plaza, Córdoba Mejora: espacios verdes para el encuentro, el juego y el deporte.','Nos vemos en la Plaza, Córdoba Mejora: plazas renovadas para jugar, encontrarse y disfrutar del aire libre.','Más plazas y espacios verdes para el barrio, con Nos vemos en la Plaza.'],dark:'#09467f',pie:'#09467f',claro:'#c6dfce',chip:'#c6dfce',acento:'#c6dfce',emoji:'🌳',wm:'wordmark-plaza',logos:'logos-plaza',tags:['#NosVemosEnLaPlaza','#CórdobaMejora','#HacerParaCrecer'],
   marco:'“Nos vemos en la Plaza, Córdoba Mejora” renueva plazas y espacios verdes de la ciudad: lugares de encuentro, deporte, juego y recreación que suman valor ambiental y social a los barrios, con espacios seguros donde los chicos pueden jugar y estar, como alternativa a los entornos de riesgo.'}
};
const TIPOS={mant:{label:'Mantenimiento de calles',corto:'Mant. de calles',eje:'calle'},frio:{label:'Bacheo en frío',corto:'Bacheo en frío',eje:'calle'},rampas:{label:'Rampas',corto:'Rampas',eje:'accesible'},bacheo:{label:'Bacheo con asfalto',corto:'Bacheo asfalto',eje:'calle'},
 rehab:{label:'Rehabilitación con asfalto',corto:'Rehab. asfalto',eje:'calle'},hormigon:{label:'Rehabilitación y bacheo con hormigón',corto:'Hormigón',eje:'calle'},pav:{label:'Pavimentación',corto:'Pavimentación',eje:'calle'},plaza:{label:'Plazas',corto:'Plazas',eje:'plaza'}};
const TIPO_ORDEN=['mant','frio','rampas','bacheo','rehab','hormigon','pav','plaza'];
const CIERRES_VIEJOS=['Con las cuentas en orden, Córdoba sostiene la obra pública en cada barrio.','El orden de las cuentas públicas permite que la obra siga llegando a los barrios.','Hacer para Crecer: cuentas en orden y obra a la vista en toda la ciudad.'];
const UMBRAL_NITIDEZ=800; // por debajo de este valor la foto se considera borrosa/pixelada
const CIERRES=['Con equilibrio fiscal, Córdoba sostiene la inversión en infraestructura para todos los cordobeses.','El equilibrio fiscal permite mantener la obra pública en toda la ciudad.','Cuentas en orden: la inversión en infraestructura llega a todos los cordobeses.','Equilibrio fiscal que se convierte en obra para cada cordobés.','Con las cuentas en orden, la obra pública sigue llegando a todos los barrios.','Hacer para Crecer: equilibrio fiscal para sostener la infraestructura de todos.','Sin ajuste ciego y con equilibrio fiscal: más infraestructura para todos.','El orden fiscal sostiene la obra pública de todos los cordobeses.'];
const CTAS=['Seguí el avance de las obras de tu barrio y compartí esta publicación con tus vecinos.','Compartí esta publicación y seguí cómo avanzan las obras en la ciudad.','Conocé cómo avanzan las obras de tu barrio.','Seguí las obras de Córdoba y compartilas con tus vecinos.'];
const pick=(arr,o,salt='')=>arr[hash((o.id||'')+salt)%arr.length];
const FMT={'1x1':[1080,1080,'Feed 1:1 · 1080×1080'],'4x5':[1080,1350,'Feed 4:5 · 1080×1350 (recomendado)'],'9x16':[1080,1920,'Stories/Reels 9:16 · 1080×1920']};
const hash=s=>[...s].reduce((a,c)=>(a*31+c.charCodeAt(0))>>>0,7);

/* ---------- datos derivados ---------- */
const sinBarras=s=>s==null?s:String(s).replace(/\s*\/\s*/g,' y ');
const ALIAS={'Gral. Arenales':'General Arenales','Gral. Paz':'General Paz','Gral Paz':'General Paz','Talleres (E)':'Talleres Este','Ombu':'Ombú'};
const obras=P.obras.map(o=>{
  const t=TIPOS[o.tipo], c=CIRC[o.circuito]||null, m=o.metricas||{};
  const fotos=(A.fotos[o.doc]||[]), doc=(A.docs[o.doc]||null), ali=s=>s&&(ALIAS[s]||s);
  const rawB=o.barrio||((o.tipo==='mant'||o.tipo==='pav')?o.sector:null);   // los barrios que el parte une con barra se nombran por separado
  const barrioList=rawB?rawB.split('/').map(s=>ali(s.trim())):null;
  return {...o,barrioList,via:sinBarras(o.via),entre:sinBarras(o.entre),sector:ali(sinBarras(o.sector)),barrio:ali(sinBarras(o.barrio)),eje:t.eje,circNombre:c,m,fotos,docTxt:doc,driveUrl:m.driveUrl};
});
const reales=obras.filter(o=>!o.grupo);
const dnde=o=>o.via?`${o.via}${o.entre?`, entre ${o.entre}`:''}`:o.sector;
const bar=o=>o.barrioList?o.barrioList.join(' y Barrio '):null;      // 'Barrio ' + bar(o) => 'Barrio A y Barrio B'
const BAR=o=>bar(o)?`Barrio ${bar(o)}`:null;
const lugarRampas=o=>/ y /.test(o.via)?`la esquina de ${o.via}`:o.via;
const esq=o=>o.metricas.esquinas;

function placaDe(o){
  const m=o.m,B=BAR(o); let valor=null,etiqueta=null,main=null,sub='',extra='';
  if(o.tipo==='rampas'){valor=nf(o.rampas);etiqueta=o.rampas===1?'Rampa en ejecución':'Rampas en ejecución';sub=o.via;}
  else if(o.tipo==='pav'){valor=nf(m.cuadras);etiqueta='Cuadras a pavimentar';sub=B;}
  else if(m.m2){valor=nf(m.m2);etiqueta='m² de '+({bacheo:'bacheo con asfalto',frio:'bacheo en frío',hormigon:'rehabilitación y bacheo con hormigón',rehab:'rehabilitación con asfalto'}[o.tipo]||'calzada intervenida');sub=o.via||B;extra=o.via?(B||''):'';}
  else if(m.ml){valor=nf(m.ml);etiqueta=o.tipo==='mant'?'metros lineales de calles de tierra':'metros lineales de calzada rehabilitada';sub=o.tipo==='mant'?B:(o.via||B);extra=o.tipo==='mant'?'':(B||'');}
  else if(o.tipo==='plaza'){main=o.via;sub='Renovación integral de espacios públicos';extra=B||'';}
  else if(o.tipo==='mant'||o.tipo==='frio'){main=TIPOS[o.tipo].label;sub=B;}
  else {main=TIPOS[o.tipo].label;sub=o.via;extra=B||'';}
  return {id:o.id,eje:o.eje,kicker:TIPOS[o.tipo].label,valor,etiqueta,main,sub,extra,fotos:o.fotos};
}
function tituloIG(o){
  const B=bar(o);
  switch(o.tipo){
    case 'rampas': return o.grupo?`CÓRDOBA ACCESIBLE: ${o.rampas} RAMPAS EN ${o.circuito==='1'?'LA ZONA CÉNTRICA':'LA AV. J. M. DE PUEYRREDÓN'}`:`CÓRDOBA ACCESIBLE: ${o.rampas} ${o.rampas===1?'RAMPA':'RAMPAS'} EN ${up(o.via)}`;
    case 'plaza': return `BARRIO ${up(B)}: RENOVACIÓN DE ${up(o.via)}`;
    case 'pav': return `BARRIO ${up(B)}: PAVIMENTACIÓN`;
    case 'mant': return `BARRIO ${up(B)}: MANTENIMIENTO DE CALLES`;
    default: return `BARRIO ${up(B)}: ${up(TIPOS[o.tipo].label)}`;
  }
}
function hecho(o){
  const m=o.m,B=BAR(o),en=B?`, en el ${B}`:'';
  switch(o.tipo){
    case 'rampas':
      if(o.grupo&&o.circuito==='1') return `En la zona céntrica de la ciudad avanzamos con la colocación de ${o.rampas} rampas en ${esq(o)} esquinas, entre ellas 12 de Octubre y San Martín, 27 de Abril y Marcelo T. de Alvear, Bulevar Mitre y San Martín, Deán Funes y Marcelo T. de Alvear, y Obispo Trejo e Hipólito Yrigoyen`;
      if(o.grupo) return `Avanzamos con la colocación de ${o.rampas} rampas en ${esq(o)} esquinas de la Av. J. M. de Pueyrredón: La Pampa, Río Negro, Santa Cruz y Misiones`;
      return `${pick(['Avanzamos con la colocación de','Colocamos','Se ejecutan'],o,'a')} ${o.rampas} ${o.rampas===1?'rampa':'rampas'} en ${lugarRampas(o)}`;
    case 'plaza': return `${pick(['Avanzan los trabajos de renovación de la','Continúa la renovación de la','Se trabaja en la puesta en valor de la'],o,'a')} ${o.via}${en}`;
    case 'mant': return m.ml?`${pick(['Avanza el mantenimiento de calles en el','Continúan las tareas de mantenimiento en el'],o,'a')} ${B}: las tareas abarcan ${nf(m.ml)} metros lineales de calles de tierra`:`${pick(['Avanzan las tareas de mantenimiento de calles en el','Continúa el mantenimiento de calles en el'],o,'a')} ${B}`;
    case 'frio': return `${pick(['Avanzan las tareas de bacheo en frío en el','Continúa el bacheo en frío en el'],o,'a')} ${B}${m.nocturno?', en horario nocturno':''}`;
    case 'bacheo': return `${pick(['Avanzan las tareas de bacheo con asfalto sobre','Continúan los trabajos de bacheo con asfalto sobre','Se ejecutan tareas de bacheo con asfalto sobre'],o,'a')} ${dnde(o)}${en}${m.m2?`, con ${nf(m.m2)} m² de calzada intervenida`:''}`;
    case 'rehab': return `Avanzan las tareas de rehabilitación con asfalto sobre ${dnde(o)}${en}${m.ml?`, con ${nf(m.ml)} metros lineales de calzada`:''}${m.nocturno?', en horario nocturno':''}`;
    case 'hormigon': return `${pick(['Avanzan las tareas de rehabilitación y bacheo con hormigón sobre','Continúan los trabajos de rehabilitación y bacheo con hormigón sobre','Se trabaja en la rehabilitación y el bacheo con hormigón sobre'],o,'a')} ${dnde(o)}${(o.nota||[]).filter(n=>/etapa/.test(n)).map(n=>` (${n})`).join('')}${en}${m.m2?`, con ${nf(m.m2)} m² intervenidos`:''}`;
    case 'pav': return `Avanza la obra de pavimentación en el ${B}, que alcanza ${m.cuadras} cuadras y tiene un plazo de ejecución de ${m.plazo} días calendario`;
  }
}
function contexto(o){ // una oración de contexto que explica para qué sirve la obra (de los docs y las memorias)
  switch(o.tipo){
    case 'pav': return pick(['La obra mejora el drenaje superficial de las aguas pluviales y el tránsito vehicular y peatonal, y deja materializadas las líneas de vereda.','Con la pavimentación, el barrio gana en desagüe, circulación vehicular y peatonal, y en consolidación urbana.'],o,'x');
    case 'bacheo': case 'frio': case 'hormigon': case 'rehab': return pick(['Las tareas permiten recuperar sectores deteriorados de la calzada y mejorar las condiciones de circulación de los vecinos.','Cada intervención recupera un sector deteriorado y mejora el tránsito de quienes circulan a diario por la zona.','El objetivo es devolverle a la calle mejores condiciones para circular con seguridad y comodidad.'],o,'x');
    case 'mant': return pick(['El mantenimiento mejora las condiciones de circulación y la conectividad de los vecinos del sector.','Las tareas mejoran la transitabilidad y la conectividad del sector.'],o,'x');
    case 'plaza': return /Pedro Vivas/.test(o.via)
      ?'La puesta en valor contempla la renovación de senderos, rampas de acceso para un ingreso inclusivo, mobiliario urbano, un patio de las infancias con juegos clásicos y adaptados, postas gimnásticas y parquización de los espacios verdes. Los trabajos se realizan de manera conjunta entre el Gobierno de la Provincia, la Municipalidad de Córdoba y EPEC.'
      :'';
    default: return '';
  }
}
function hechoX(o){ // versión corta: sin el detalle de calles
  const m=o.m,B=BAR(o),en=B?` (${B})`:'';
  switch(o.tipo){
    case 'rampas': return o.grupo?(o.circuito==='1'?`Avanzamos con la colocación de ${o.rampas} rampas en ${esq(o)} esquinas de la zona céntrica`:`Avanzamos con la colocación de ${o.rampas} rampas en ${esq(o)} esquinas de la Av. J. M. de Pueyrredón`):`Avanzamos con la colocación de ${o.rampas} ${o.rampas===1?'rampa':'rampas'} en ${lugarRampas(o)}`;
    case 'plaza': return `Avanzan los trabajos de renovación de la ${o.via}${en}`;
    case 'mant': return m.ml?`Avanza el mantenimiento de calles en el ${B}: ${nf(m.ml)} metros lineales de calles de tierra`:`Avanzan las tareas de mantenimiento de calles en el ${B}`;
    case 'bacheo': return `Avanza el bacheo con asfalto sobre ${o.via}${en}${m.m2?`: ${nf(m.m2)} m² intervenidos`:''}`;
    case 'frio': return `Avanza el bacheo en frío en el ${B}${m.nocturno?', en horario nocturno':''}`;
    case 'rehab': return `Avanza la rehabilitación con asfalto sobre ${o.via}${en}${m.ml?`: ${nf(m.ml)} metros lineales`:''}`;
    case 'hormigon': return `Avanza la rehabilitación y el bacheo con hormigón sobre ${o.via}${en}${m.m2?`: ${nf(m.m2)} m² intervenidos`:''}`;
    case 'pav': return `Avanza la pavimentación del ${B}: ${m.cuadras} cuadras, con un plazo de ${m.plazo} días calendario`;
  }
}
const pie=o=>BAR(o)?`📍 ${BAR(o)}\n\n`:'';
function textoIG(o){
  const e=EJES[o.eje], ctx=contexto(o), cierre=pick(CIERRES,o,'c');  // una frase política corta en cada copy, distinta según la obra
  return `${e.emoji} ${tituloIG(o)}\n\n${hecho(o)}.${ctx?'\n\n'+ctx:''}\n\n${pick(e.cortos,o,'m')}\n\n${pie(o)}${cierre?cierre+'\n\n':''}👉 ${pick(CTAS,o,'t')}\n\n${e.tags.join(' ')}`;
}
function textoX(o){
  const e=EJES[o.eje], cierre=pick(CIERRES,o,'c'), ht=e.tags.slice(0,2).join(' ');
  const h=hecho(o)+'.', hs=hechoX(o)+'.', t=`${e.emoji} ${tituloIG(o)}`;
  // del más completo al más resumido: se resume el mensaje, nunca se corta una frase
  const cx=cierre?[`${t}\n${h}\n${cierre}\n${ht}`]:[],cy=cierre?[`${t}\n${hs}\n${cierre}\n${ht}`]:[];
  const c=[...cx,`${t}\n${h}\n${ht}`,...cy,`${t}\n${hs}\n${ht}`,`${hs}\n${ht}`,`${t}\n${ht}`];
  return c.find(x=>x.length<=280)||hs;
}
/* texto de placa editable: líneas = [título] [dato] [lugar] [barrio] */
function textoPlaca(v){
  const l=v.valor?[up(v.kicker),`${v.valor} ${v.etiqueta}`,v.sub,v.extra]:[up(v.main||''),v.sub,v.extra];
  return l.filter(x=>x!=null&&x!=='').join('\n');
}
function leerPlaca(v,txt){ // vuelca el texto editado en la placa
  const L=txt.split('\n').map(s=>s.trim());
  if(v.valor){const m=(L[1]||'').match(/^(\S+)\s*(.*)$/)||[];v.kicker=L[0]||v.kicker;v.valor=m[1]||v.valor;v.etiqueta=m[2]||'';v.sub=L[2]||'';v.extra=L[3]||'';}
  else{v.main=L[0]||'';v.sub=L[1]||'';v.extra=L[2]||'';}
}

/* ---------- agregados ---------- */
const sum=(a,f)=>a.reduce((s,x)=>s+(f(x)||0),0);
const uniq=a=>[...new Set(a)];
const R={obras:reales.length};
const rampasObras=reales.filter(o=>o.tipo==='rampas');
R.rampas=sum(rampasObras,o=>o.rampas); R.esquinas=rampasObras.length;
const calleObras=reales.filter(o=>o.eje==='calle'); R.calle=calleObras.length;
const pavs=reales.filter(o=>o.tipo==='pav'); R.pav=pavs.length; R.cuadras=sum(pavs,o=>o.m.cuadras);
const plazas=reales.filter(o=>o.tipo==='plaza'); R.plazas=plazas.length;
const norm=s=>s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/\(.*?\)/g,'').replace(/ etapa ii| zona este/g,'').replace(/^policial.*/,'policial').replace(/\s+/g,' ').trim();
const barrios=uniq(reales.flatMap(o=>o.barrioList||[]).map(norm));
R.barrios=barrios.length;   // conservador: "al menos"
const lista=a=>a.length<2?a.join(''):a.slice(0,-1).join(', ')+' y '+a[a.length-1];
const redondo=(n,paso)=>Math.floor(n/paso)*paso;
const FINOK=P.finalizadas!=null;
const cnt=t=>reales.filter(o=>o.tipo===t).length;
const MODELO='El modelo cordobés prioriza el equilibrio fiscal orientado a la inversión en infraestructura, por encima del ajuste ciego: la obra pública se sostiene con las cuentas en orden.';
const GOB='el Gobierno de la Provincia en conjunto con la Municipalidad de Córdoba';
const SEGUIMIENTO=['Seguimiento diario de las obras','Los vecinos pueden consultar, de manera sencilla y con actualización diaria, el estado de las obras que se ejecutan en distintos sectores de la ciudad, tanto las que se encuentran en marcha como las finalizadas: [pegar enlace].'];

/* gacetilla: título, bajada (viñetas), primer párrafo, secciones con subtítulo y cierre, al estilo de prensa.cba.gov.ar */
const gacetilla=({titulo,bajada=[],lead,secciones=[],cierre})=>[titulo,bajada.map(s=>'• '+s).join('\n'),lead,...secciones.flatMap(([h,ps])=>[h,...ps]),cierre,SEGUIMIENTO[0],SEGUIMIENTO[1],'Material de descarga: [pegar enlace]'].filter(Boolean).join('\n\n');
const limpio=s=>String(s).replace(/(https?:\/\/\S+)|\s*\/\s*/g,(m,u)=>u||' y ');   // las barras pasan a "y", salvo en los links

function generales(){
  const G=[]; const tg=k=>EJES[k].tags.join(' '), ptos=nf(P.puestos), hoy=P.fecha_texto;
  const add=(id,titulo,eje,titulos,ig,x,placa,gac)=>G.push({id,titulo,eje,titulos:titulos.map(limpio),ig:limpio(ig),x:limpio(x),placa:{eje,fotos:[],extra:'',...placa},gac:limpio(gacetilla(gac))});
  const brs=`al menos ${R.barrios} barrios`;
  const cent=rampasObras.filter(o=>o.circuito==='1'&&!o.grupo), pue=rampasObras.filter(o=>o.circuito==='10G'&&!o.grupo);
  const esqTxt=a=>a.map(o=>`${o.via} (${o.rampas})`);
  const listaBarrios=a=>lista(uniq(a.map(bar).filter(Boolean)).map(b=>`Barrio ${b}`));

  add('g_total','Panorama general de obras','calle',
   [`Córdoba tiene ${R.obras} obras en ejecución en ${brs} de la ciudad`,`Hacer para Crecer: ${R.obras} obras en marcha y ${ptos} puestos de trabajo directos`,FINOK?`Con ${P.finalizadas} obras finalizadas, Córdoba mantiene ${R.obras} en ejecución`:`Córdoba mantiene ${R.obras} obras en ejecución en ${brs} de la ciudad`],
   `🏗️ ${R.obras} OBRAS EN EJECUCIÓN EN LA CIUDAD\n\nHoy, ${GOB} ejecutan ${R.obras} obras en ${brs} de la ciudad. Los trabajos generan ${ptos} puestos de trabajo directos y comprenden el mantenimiento y la reparación de calles, la pavimentación, la construcción de rampas de accesibilidad y la renovación de plazas.\n\n${MODELO}\n\n👉 Seguí el avance de las obras de tu barrio.\n\n#CórdobaMejora #HacerParaCrecer`,
   `🏗️ Hoy hay ${R.obras} obras en ejecución en ${brs} de Córdoba, con ${ptos} puestos de trabajo directos. Hacer para Crecer: obra pública en cada barrio. #CórdobaMejora #HacerParaCrecer`,
   {kicker:'Obras en ejecución',valor:String(R.obras),etiqueta:'Obras en ejecución en la ciudad',sub:`En ${brs}`,extra:`${ptos} puestos de trabajo directos`},
   {titulo:`Córdoba tiene ${R.obras} obras en ejecución en ${brs} de la ciudad`,
    bajada:[`Los trabajos generan ${ptos} puestos de trabajo directos.`,`Hacer para Crecer: la obra pública llega a cada barrio de Córdoba.`].concat(FINOK?[`Ya se finalizaron ${P.finalizadas} obras.`]:[]),
    lead:`Con el trabajo conjunto del Gobierno de la Provincia y la Municipalidad de Córdoba, hoy se ejecutan ${R.obras} obras en ${brs} de la ciudad, que generan ${ptos} puestos de trabajo directos.`,
    secciones:[['Qué obras se ejecutan',[`Las obras corresponden a mantenimiento de calles (${cnt('mant')}), bacheo en frío (${cnt('frio')}), bacheo con asfalto (${cnt('bacheo')}), rehabilitación con asfalto (${cnt('rehab')}), rehabilitación y bacheo con hormigón (${cnt('hormigon')}), pavimentación (${cnt('pav')}), rampas de accesibilidad en ${cnt('rampas')} esquinas y renovación de ${cnt('plaza')} plazas.`]],
               ['Hacer para Crecer, obra a obra',[FINOK?`Además de las obras en marcha, ya se finalizaron ${P.finalizadas}.`:null].filter(Boolean)],['Los programas',[EJES.calle.marco,EJES.accesible.marco,EJES.plaza.marco]]],
    cierre:MODELO});

  add('g_empleo','Puestos de trabajo directos','calle',
   [`Las obras en ejecución generan ${ptos} puestos de trabajo directos en Córdoba`,`Hacer para Crecer: ${ptos} puestos de trabajo directos en las obras de la ciudad`,`Obra pública y trabajo: ${R.obras} obras en marcha en ${brs}`],
   `👷 ${ptos} PUESTOS DE TRABAJO DIRECTOS\n\nLas ${R.obras} obras que hoy se ejecutan en la ciudad generan ${ptos} puestos de trabajo directos: mantenimiento de calles, bacheo, pavimentación, rampas de accesibilidad y renovación de plazas.\n\nHacer para Crecer significa obra pública que se convierte en trabajo para los cordobeses.\n\n${MODELO}\n\n#CórdobaMejora #HacerParaCrecer`,
   `👷 Las ${R.obras} obras en ejecución en Córdoba generan ${ptos} puestos de trabajo directos. Hacer para Crecer: obra pública y trabajo para los cordobeses. #CórdobaMejora #HacerParaCrecer`,
   {kicker:'Empleo',valor:ptos,etiqueta:'Puestos de trabajo directos',sub:`En ${R.obras} obras en ejecución`},
   {titulo:`Las obras en ejecución generan ${ptos} puestos de trabajo directos en Córdoba`,
    bajada:[`Hay ${R.obras} obras en marcha en ${brs} de la ciudad.`,'Hacer para Crecer: obra pública que se convierte en trabajo para los cordobeses.'],
    lead:`Las ${R.obras} obras que hoy ejecutan el Gobierno de la Provincia y la Municipalidad de Córdoba generan ${ptos} puestos de trabajo directos.`,
    secciones:[['Dónde se trabaja',[`Hay ${R.calle} frentes de obra de Calle por Calle, ${R.esquinas} esquinas con rampas de Córdoba Accesible y ${R.plazas} plazas en renovación, en ${brs}.`]]],
    cierre:MODELO});

  add('g_accesible','Córdoba Accesible – total de rampas','accesible',
   [`Córdoba Accesible: avanza la colocación de ${R.rampas} rampas en ${R.esquinas} esquinas`,`Una Córdoba inclusiva, pensada para todos: ${R.rampas} rampas en ejecución`,`${R.rampas} rampas en marcha para mejorar la movilidad peatonal en la ciudad`],
   `♿ CÓRDOBA ACCESIBLE: ${R.rampas} RAMPAS EN EJECUCIÓN\n\nHoy se ejecuta la colocación de ${R.rampas} rampas en ${R.esquinas} esquinas de la ciudad: ${cent.length} esquinas en la zona céntrica, con ${sum(cent,o=>o.rampas)} rampas, y ${pue.length} esquinas de la Av. J. M. de Pueyrredón, con ${sum(pue,o=>o.rampas)} rampas.\n\n${EJES.accesible.corto}\n\n${MODELO}\n\n${tg('accesible')}`,
   `♿ Córdoba Accesible: hoy se ejecutan ${R.rampas} rampas en ${R.esquinas} esquinas de la ciudad. Una Córdoba inclusiva, pensada para todos. #CórdobaAccesible #HacerParaCrecer`,
   {kicker:'Córdoba Accesible',valor:String(R.rampas),etiqueta:'Rampas en ejecución',sub:`En ${R.esquinas} esquinas de la ciudad`},
   {titulo:`Córdoba Accesible: avanza la colocación de ${R.rampas} rampas en ${R.esquinas} esquinas de la ciudad`,
    bajada:['Una Córdoba inclusiva, pensada para todos.',`El programa contempla la instalación de ${nf(P.programaRampas.total)} rampas en el ejido capitalino.`,'Hacer para Crecer: más accesibilidad en el espacio público.'],
    lead:`El Gobierno de la Provincia, en conjunto con la Municipalidad de Córdoba, avanza con el programa Córdoba Accesible: hoy se ejecuta la colocación de ${R.rampas} rampas en ${R.esquinas} esquinas de la ciudad.`,
    secciones:[['Dónde se trabaja',[`En la zona céntrica hay ${sum(cent,o=>o.rampas)} rampas en ${cent.length} esquinas: ${lista(esqTxt(cent))}.`,`En ${pue.length} esquinas de la Av. J. M. de Pueyrredón hay ${sum(pue,o=>o.rampas)} rampas: ${lista(esqTxt(pue))}.`]],
               ['Una Córdoba inclusiva, pensada para todos',[`Córdoba Accesible contempla la instalación de ${nf(P.programaRampas.total)} rampas en el ejido capitalino: se construirán ${nf(P.programaRampas.nuevas)} rampas nuevas, de las cuales ${nf(P.programaRampas.en_esquinas_sin_rampa)} se ubicarán en esquinas que hoy carecen de esta infraestructura, y se repararán otras ${P.programaRampas.reparadas} con daños menores.`,'El objetivo es favorecer la autonomía, la movilidad y la integración de todos los vecinos en el espacio público.']]],
    cierre:MODELO});

  add('g_calle','Calle por Calle – frentes de obra','calle',
   [`Calle por Calle: ${R.calle} frentes de obra en ${brs} de la ciudad`,`${R.calle} frentes de obra de reparación vial en ejecución en Córdoba`,`Hacer para Crecer: la rehabilitación de calles avanza en ${brs}`],
   `🛣️ CALLE POR CALLE: ${R.calle} FRENTES DE OBRA\n\nHoy, el programa Calle por Calle, Córdoba Mejora tiene ${R.calle} frentes de obra en ${brs} de la ciudad: ${cnt('hormigon')} de rehabilitación y bacheo con hormigón, ${cnt('mant')} de mantenimiento de calles, ${cnt('frio')} de bacheo en frío, ${cnt('bacheo')} de bacheo con asfalto, ${cnt('rehab')} de rehabilitación con asfalto y ${cnt('pav')} de pavimentación.\n\n${EJES.calle.corto}\n\n${MODELO}\n\n${tg('calle')}`,
   `🛣️ Calle por Calle: hoy hay ${R.calle} frentes de obra de reparación vial en ${brs} de Córdoba. Hacer para Crecer: obra pública en cada barrio. #CallePorCalle #HacerParaCrecer`,
   {kicker:'Calle por Calle',valor:String(R.calle),etiqueta:'Frentes de obra de reparación vial',sub:`En ${brs}`},
   {titulo:`Calle por Calle: ${R.calle} frentes de obra en ${brs} de la ciudad`,
    bajada:[`Hay ${cnt('hormigon')} frentes de rehabilitación y bacheo con hormigón y ${cnt('bacheo')} de bacheo con asfalto.`,`Se ejecutan ${cnt('pav')} obras de pavimentación, con ${R.cuadras} cuadras en total.`,'Hacer para Crecer: más calles en mejores condiciones para los cordobeses.'],
    lead:`El programa “Calle por Calle, Córdoba Mejora”, que lleva adelante ${GOB}, tiene hoy ${R.calle} frentes de obra en ${brs} de la ciudad.`,
    secciones:[['Qué se hace',[EJES.calle.contexto,`Hoy los trabajos incluyen mantenimiento de calles (${cnt('mant')}), bacheo en frío (${cnt('frio')}), bacheo con asfalto (${cnt('bacheo')}), rehabilitación con asfalto (${cnt('rehab')}), rehabilitación y bacheo con hormigón (${cnt('hormigon')}) y pavimentación (${cnt('pav')}).`]],
               ['Pavimentación',[`Las ${R.pav} obras de pavimentación en ejecución (${lista(pavs.map(o=>'Barrio '+bar(o)))}) alcanzan ${R.cuadras} cuadras.`]]],
    cierre:MODELO});

  add('g_cuadras','Pavimentación – cuadras','calle',
   [`Cinco obras de pavimentación alcanzan ${R.cuadras} cuadras en Córdoba`,`Calle por Calle: ${R.cuadras} cuadras en proceso de pavimentación`,`Hacer para Crecer: se pavimentan ${R.cuadras} cuadras en cinco barrios`],
   `🛣️ ${R.cuadras} CUADRAS A PAVIMENTAR\n\nLas ${R.pav} obras de pavimentación que hoy se ejecutan en la ciudad, en ${listaBarrios(pavs)}, alcanzan ${R.cuadras} cuadras: ${lista(pavs.map(o=>`${o.m.cuadras} en el Barrio ${bar(o)}`))}.\n\nLas obras mejoran el drenaje superficial de las aguas pluviales y el tránsito vehicular y peatonal, y dejan materializadas las líneas de vereda.\n\n${EJES.calle.corto}\n\n${MODELO}\n\n${tg('calle')}`,
   `🛣️ Cinco obras de pavimentación alcanzan ${R.cuadras} cuadras en ${listaBarrios(pavs)}. Más calles pavimentadas para los cordobeses. #CallePorCalle #HacerParaCrecer`,
   {kicker:'Pavimentación',valor:String(R.cuadras),etiqueta:'Cuadras a pavimentar',sub:`${R.pav} obras en ejecución`,extra:'En cinco barrios de la ciudad'},
   {titulo:`Cinco obras de pavimentación alcanzan ${R.cuadras} cuadras en Córdoba`,
    bajada:pavs.map(o=>`Barrio ${bar(o)}: ${o.m.cuadras} cuadras.`).concat(['Hacer para Crecer: más calles pavimentadas en los barrios.']),
    lead:`Las ${R.pav} obras de pavimentación que hoy ejecutan ${GOB} alcanzan ${R.cuadras} cuadras, en ${listaBarrios(pavs)}.`,
    secciones:[['Cada obra',pavs.map(o=>`Barrio ${bar(o)}: ${o.m.cuadras} cuadras, con un plazo de ejecución de ${o.m.plazo} días calendario.`)],
               ['Para qué',['Las obras mejoran el drenaje superficial de las aguas pluviales y el tránsito vehicular y peatonal, reducen los costos de mantenimiento de las calles de firme natural y dejan materializadas las líneas de vereda, con una mayor consolidación de la urbanización existente.']]],
    cierre:MODELO});

  const pl9=plazas.filter(o=>o.circuito==='9D'), plo=plazas.filter(o=>o.circuito!=='9D');
  add('g_plazas','Nos vemos en la Plaza – plazas en renovación','plaza',
   [`${R.plazas} plazas se renuevan en Córdoba: espacios verdes para el encuentro y el juego`,`Nos vemos en la Plaza: renovación de ${R.plazas} espacios públicos en la ciudad`,`Hacer para Crecer: plazas seguras para jugar, hacer deporte y estar`],
   `🌳 ${R.plazas} PLAZAS EN RENOVACIÓN\n\nHoy se renuevan ${R.plazas} plazas de la ciudad: ${pl9.length} en el Barrio ${bar(pl9[0])} y ${plo.length} en el Barrio ${bar(plo[0])}.\n\n${EJES.plaza.corto}\n\n${MODELO}\n\n${tg('plaza')}`,
   `🌳 Nos vemos en la Plaza: hoy se renuevan ${R.plazas} plazas en la ciudad, ${pl9.length} en el Barrio ${bar(pl9[0])} y ${plo.length} en el Barrio ${bar(plo[0])}. Espacios verdes para el encuentro y el juego. #NosVemosEnLaPlaza #CórdobaMejora`,
   {kicker:'Nos vemos en la Plaza',valor:String(R.plazas),etiqueta:'Plazas en renovación',sub:`En el Barrio ${bar(pl9[0])} y el Barrio ${bar(plo[0])}`},
   {titulo:`${R.plazas} plazas se renuevan en Córdoba: espacios verdes para el encuentro y el juego`,
    bajada:[`Hay ${pl9.length} plazas en el Barrio ${bar(pl9[0])} y ${plo.length} en el Barrio ${bar(plo[0])}.`,'Espacios seguros donde los chicos pueden jugar y estar, como alternativa a los entornos de riesgo.','Hacer para Crecer: ciudad más verde y más cercana.'],
    lead:`El programa “Nos vemos en la Plaza, Córdoba Mejora”, que impulsan ${GOB}, renueva hoy ${R.plazas} plazas de la ciudad.`,
    secciones:[['Dónde se trabaja',[`En el Barrio ${bar(pl9[0])}: ${lista(pl9.map(o=>o.via))}.`,`En el Barrio ${bar(plo[0])}: ${lista(plo.map(o=>o.via))}.`]],
               ['Valor ambiental y social',['La renovación de plazas y espacios verdes suma sostenibilidad y valor ambiental, y crea lugares de encuentro, deporte, juego y recreación para toda la comunidad. Son espacios seguros donde los chicos pueden jugar y estar, como alternativa a los entornos de riesgo.']]],
    cierre:MODELO});

  add('g_acum','Plan de pavimentación y programa de rampas','calle',
   [`Calle por Calle prevé ${nf(P.acumulados.cuadras_pavimentadas)} nuevas cuadras de pavimento en la ciudad`,`Hacer para Crecer: el plan contempla ${nf(P.acumulados.cuadras_pavimentadas)} nuevas cuadras de pavimento`,`${nf(P.acumulados.cuadras_pavimentadas)} cuadras de pavimento y ${nf(P.acumulados.rampas_programa)} rampas: los planes que transforman los barrios`],
   `🛣️ ${nf(P.acumulados.cuadras_pavimentadas)} NUEVAS CUADRAS DE PAVIMENTO\n\nEl plan Calle por Calle, Córdoba Mejora contempla la ejecución de ${nf(P.acumulados.cuadras_pavimentadas)} nuevas cuadras de pavimento en diversos barrios de la ciudad, mientras que Córdoba Accesible contempla la instalación de ${nf(P.acumulados.rampas_programa)} rampas en el ejido capitalino.\n\n${EJES.calle.corto}\n\n${MODELO}\n\n#CallePorCalle #CórdobaAccesible #HacerParaCrecer`,
   `🛣️ El plan Calle por Calle contempla ${nf(P.acumulados.cuadras_pavimentadas)} nuevas cuadras de pavimento, y Córdoba Accesible contempla ${nf(P.acumulados.rampas_programa)} rampas. Hacer para Crecer. #CallePorCalle #CórdobaAccesible`,
   {kicker:'Calle por Calle',valor:nf(P.acumulados.cuadras_pavimentadas),etiqueta:'Nuevas cuadras de pavimento previstas',sub:'Córdoba Mejora'},
   {titulo:`Calle por Calle prevé ${nf(P.acumulados.cuadras_pavimentadas)} nuevas cuadras de pavimento en la ciudad`,
    bajada:[`Córdoba Accesible contempla la instalación de ${nf(P.acumulados.rampas_programa)} rampas en el ejido capitalino.`,'Hacer para Crecer: obra pública que transforma los barrios.'],
    lead:`El plan “Calle por Calle, Córdoba Mejora”, que lleva adelante ${GOB}, contempla la ejecución de ${nf(P.acumulados.cuadras_pavimentadas)} nuevas cuadras de pavimento en diversos barrios de la ciudad.`,
    secciones:[['Las obras siguen en marcha',[`Hoy se ejecutan ${R.obras} obras en ${brs}, con ${R.cuadras} cuadras de pavimentación en proceso y ${R.rampas} rampas en ${R.esquinas} esquinas.`]]],
    cierre:MODELO});

  if(FINOK){
  const finRed=redondo(P.finalizadas,50);
  add('g_fin','Obras finalizadas y en ejecución','calle',
   [P.finalizadas%50===0?`Ya se finalizaron ${P.finalizadas} obras en la ciudad`:`Ya se finalizaron más de ${finRed} obras en la ciudad de Córdoba`,`Córdoba suma ${P.finalizadas} obras finalizadas y ${R.obras} en ejecución`,`${P.finalizadas+R.obras} obras entre finalizadas y en marcha: Hacer para Crecer`],
   `✅ ${P.finalizadas} OBRAS FINALIZADAS Y ${R.obras} EN EJECUCIÓN\n\nEl Gobierno de la Provincia y la Municipalidad de Córdoba suman ${P.finalizadas} obras finalizadas y ${R.obras} en ejecución en la ciudad: ${P.finalizadas+R.obras} obras en total.\n\n${MODELO}\n\n#CórdobaMejora #HacerParaCrecer`,
   `✅ Córdoba suma ${P.finalizadas} obras finalizadas y ${R.obras} en ejecución: ${P.finalizadas+R.obras} obras en total. Hacer para Crecer. #CórdobaMejora #HacerParaCrecer`,
   {kicker:'Obras',valor:String(P.finalizadas),etiqueta:'Obras finalizadas',sub:`${R.obras} más en ejecución`},
   {titulo:`Córdoba suma ${P.finalizadas} obras finalizadas y ${R.obras} en ejecución`,
    bajada:[`En total son ${P.finalizadas+R.obras} obras entre finalizadas y en marcha.`,'Hacer para Crecer: obra pública en toda la ciudad.'],
    lead:`El Gobierno de la Provincia, en conjunto con la Municipalidad de Córdoba, ya finalizó ${P.finalizadas} obras en la ciudad y mantiene otras ${R.obras} en ejecución.`,
    secciones:[['Obras que siguen en marcha',[`Las ${R.obras} obras en ejecución incluyen mantenimiento y reparación de calles, pavimentación, rampas de accesibilidad y renovación de plazas, en ${brs}.`]]],
    cierre:MODELO});
  }

  add('g_fiscal','Relato: modelo cordobés y obra pública','calle',
   [`El modelo cordobés sostiene ${R.obras} obras públicas en ${brs} de la ciudad`,`Orden fiscal, obra pública y trabajo: Hacer para Crecer`,`Equilibrio fiscal e inversión en infraestructura: así se ve el modelo cordobés`],
   `🏛️ ORDEN FISCAL, OBRA PÚBLICA\n\nHoy se ejecutan ${R.obras} obras en ${brs} de la ciudad, con ${R.rampas} rampas de accesibilidad, ${R.cuadras} cuadras de pavimentación y ${R.plazas} plazas en renovación.\n\n${MODELO}\n\nLa obra de cada día es la prueba visible de que el modelo cordobés funciona.\n\n#CórdobaMejora #HacerParaCrecer`,
   `🏛️ Hoy se ejecutan ${R.obras} obras en ${brs} de Córdoba. El modelo cordobés prioriza el equilibrio fiscal orientado a la inversión en infraestructura. #CórdobaMejora #HacerParaCrecer`,
   {kicker:'Modelo cordobés',valor:String(R.obras),etiqueta:'Obras en ejecución',sub:'Equilibrio fiscal orientado a la inversión en infraestructura'},
   {titulo:`El modelo cordobés sostiene ${R.obras} obras públicas en ${brs} de la ciudad`,
    bajada:[`${R.rampas} rampas de accesibilidad, ${R.cuadras} cuadras de pavimentación y ${R.plazas} plazas en renovación.`,'Hacer para Crecer: el equilibrio fiscal se convierte en obra.'],
    lead:`El Gobierno de la Provincia y la Municipalidad de Córdoba sostienen hoy ${R.obras} obras en ${brs} de la ciudad, que generan ${ptos} puestos de trabajo directos.`,
    secciones:[['El orden fiscal, en obras',[MODELO,'La obra de cada día es la prueba visible de que el modelo cordobés funciona.']]],
    cierre:'Hacer para Crecer: infraestructura, trabajo y cuentas en orden para los cordobeses.'});
  FISCAL.forEach((f,i)=>add('g_fiscal_'+i,'Cifra oficial: '+(f.titulo||i+1),'calle',[f.titulo||''],f.texto,f.texto.slice(0,280),{kicker:'Dato oficial',valor:f.valor||'',etiqueta:f.etiqueta||'',sub:f.fuente||''},{titulo:f.titulo||'',lead:f.texto,cierre:MODELO}));
  G.forEach(x=>{const c=(CONT.generales||{})[x.id];if(!c)return;
    if(c.titulos)x.titulos=c.titulos.map(limpio);if(c.ig)x.ig=limpio(c.ig);if(c.x)x.x=limpio(c.x);if(c.gac)x.gac=limpio(c.gac);if(c.placa)Object.assign(x.placa,c.placa);x.redactado=true;});
  return G;
}

/* ---------- placas (canvas) ---------- */
const imgCache=new Map(); const loadImg=src=>{if(imgCache.has(src))return imgCache.get(src);const p=new Promise((res,rej)=>{const i=new Image();i.onload=()=>res(i);i.onerror=rej;i.src=src});imgCache.set(src,p);return p};
const svgCache=new Map();
function svg(name){ if(!svgCache.has(name)){const t=A.svg[name];const vb=t.match(/viewBox="([\d.\- ]+)"/)[1].split(' ').map(Number);svgCache.set(name,loadImg('data:image/svg+xml;charset=utf-8,'+encodeURIComponent(t)).then(img=>({img,vb:{x:vb[0],y:vb[1],w:vb[2],h:vb[3]}})));}return svgCache.get(name);}
async function drawSvg(g,name,dx,dy,dw,dh){const {img}=await svg(name);g.drawImage(img,dx,dy,dw,dh);}
async function drawCrop(g,name,c,dx,dy,dw,dh){const {img,vb}=await svg(name);const k=img.naturalWidth/vb.w;g.drawImage(img,(c[0]-vb.x)*k,(c[1]-vb.y)*k,c[2]*k,c[3]*k,dx,dy,dw,dh);}
async function aspect(name){const {vb}=await svg(name);return vb.w/vb.h;}
function wrap(g,text,maxW){const out=[];for(const par of String(text).split('\n')){let line='';for(const w of par.split(' ')){const t=line?line+' '+w:w;if(g.measureText(t).width>maxW&&line){out.push(line);line=w}else line=t}out.push(line)}return out}
function layout(g,blocks,maxW,availH){
  blocks=blocks.filter(b=>b.t!=null&&b.t!=='');let k=1;
  for(let it=0;it<14;it++){
    let tot=0;const L=blocks.map(b=>{g.font=`${b.w} ${b.s*k}px Poppins`;const lines=wrap(g,b.up?up(b.t):b.t,maxW);const lh=b.s*k*(b.lh||1.12);tot+=lines.length*lh+(b.gap||0)*k;return {b,lines,lh,s:b.s*k}});
    if(tot-(blocks.at(-1).gap||0)*k<=availH||it===13)return {L,tot,k};k*=.93;
  }
}
function drawLayout(g,lay,x,y,align,maxW){
  let cy=y;
  for(const {b,lines,lh,s} of lay.L){g.font=`${b.w} ${s}px Poppins`;g.fillStyle=b.c;g.globalAlpha=b.op??1;g.textAlign=align;g.textBaseline='alphabetic';
    for(const ln of lines){g.fillText(ln,align==='center'?x+maxW/2:x,cy+s*.92);cy+=lh}
    cy+=(b.gap||0)*lay.k;}
  g.globalAlpha=1;
}
function cover(g,img,x,y,w,h){const r=Math.max(w/img.naturalWidth,h/img.naturalHeight),sw=w/r,sh=h/r;g.drawImage(img,(img.naturalWidth-sw)/2,(img.naturalHeight-sh)/2,sw,sh,x,y,w,h)}
function rrect(g,x,y,w,h,r){g.beginPath();g.moveTo(x+r,y);g.arcTo(x+w,y,x+w,y+h,r);g.arcTo(x+w,y+h,x,y+h,r);g.arcTo(x,y+h,x,y,r);g.arcTo(x,y,x+w,y,r);g.closePath()}

async function footer(g,W,H,e,story,eje,solo){
  const fh=W*.17, y1=story?H*.885:H, y0=y1-fh;  // stories: logos más abajo (queda ~11% libre abajo, cerca del mínimo que recomienda Meta)
  if(!solo){g.fillStyle=e.pie;g.fillRect(0,y0,W,H-y0);}
  const asp=await aspect(e.logos);
  let lx,lw;
  if(eje==='accesible'&&!solo){const ca=await aspect('cinta-pie-accesible');const cw=fh*ca;await drawSvg(g,'cinta-pie-accesible',0,y0,cw,fh);lx=cw+W*.03;lw=W-lx-W*.05;}
  else{lw=W*(eje==='plaza'?.90:.84);lx=(W-lw)/2;}
  const lh=lw/asp, ly=y0+(fh-lh)/2;
  await drawSvg(g,e.logos,lx,ly,lw,lh);
  return y0;
}
const TEMA={calle:{bg:'#17233d',panel:'#bedff7',ink:'#17233d',acc:'#bc1734',blk:'#bc1734',band:'#bc1734'},
  accesible:{bg:'#eaab3b',panel:'#bedff7',ink:'#09467f',acc:'#09467f',blk:'#e8d7b0',band:'#ffffff'},
  plaza:{bg:'#c6dfce',panel:'#ffffff',ink:'#09467f',acc:'#2f7a52',blk:'#ffffff',band:'#4da070'}};
function geo(W,H,y0,eje){const story=H>W*1.6,sh=eje==='plaza'?W*297/6917:0;
  const panelH=Math.round(y0*(story?.2:.25)),panelB=y0-sh-W*(eje==='plaza'?.02:story?.05:.035);return {story,sh,panelH,panelB,panelT:panelB-panelH}}
async function bloqueEje(g,W,e,T,x0,y,alignRight){ // bloque con el logotipo del eje, pegado al borde como en los carteles
  const wa=await aspect(e.wm),ww=W*.30,wh=ww/wa,pad=W*.035,bw=ww+pad*2,bh=wh+pad*2,x=alignRight?W-bw:0;
  g.fillStyle=T.blk;g.fillRect(x,y,bw,bh);await drawSvg(g,e.wm,x+pad,y+pad,ww,wh);}
function panelDatos(g,W,v,T,gm){
  const {panelT,panelH}=gm,px=W*.05,pw=W*.9,ip=W*.035;
  g.save();g.shadowColor='#0003';g.shadowBlur=W*.02;g.shadowOffsetY=W*.006;g.fillStyle=T.panel;rrect(g,px,panelT,pw,panelH,W*.022);g.fill();g.restore();
  if(v.valor){
    let s=Math.min(panelH*.62,W*.2);g.font=`800 ${s}px Poppins`;while(g.measureText(v.valor).width>W*.30&&s>10){s*=.94;g.font=`800 ${s}px Poppins`}
    const vw=g.measureText(v.valor).width;g.fillStyle=T.ink;g.textAlign='left';g.textBaseline='alphabetic';g.fillText(v.valor,px+ip,panelT+panelH/2+s*.36);
    const rx=px+ip+vw+W*.03,rw=px+pw-ip-rx;
    const lay=layout(g,[{t:v.etiqueta,w:800,s:W*.043,c:T.acc,up:true,lh:1.08,gap:W*.01},{t:v.sub||'',w:600,s:W*.034,c:'#17233d',lh:1.15,gap:W*.008},{t:v.extra||'',w:600,s:W*.026,c:'#17233d',op:.7}],rw,panelH-ip);
    drawLayout(g,lay,rx,panelT+(panelH-lay.tot)/2,'left',rw);
  } else {
    const lay=layout(g,[{t:v.main,w:800,s:W*.06,c:T.ink,up:true,lh:1.08,gap:W*.012},{t:v.sub||'',w:600,s:W*.036,c:'#17233d',lh:1.15,gap:W*.008},{t:v.extra||'',w:600,s:W*.026,c:'#17233d',op:.7}],pw-ip*2,panelH-ip);
    drawLayout(g,lay,px+ip,panelT+(panelH-lay.tot)/2,'left',pw-ip*2);
  }
}
/* Diseño A: foto en círculo con aro del eje */
async function photoCirculo(g,W,H,v,e,y0,topSafe,im){
  const eje=v.eje,T=TEMA[eje],gm=geo(W,H,y0,eje),{story,sh,panelT}=gm;
  g.fillStyle=T.bg;g.fillRect(0,0,W,y0);
  if(eje==='accesible')await drawCrop(g,'fondo-accesible',[0,0,1415,483],0,0,W*.5,W*.5*483/1415);
  if(eje==='plaza')await drawCrop(g,'fondo-plaza',[150,220,560,520],W*.04,topSafe+W*.03,W*.1,W*.1*520/560);
  const cTop=story?H*.115:topSafe+W*.03, ring=W*.085;
  let r=(panelT+W*.07-cTop)/2-ring; r=Math.min(r,W*.385);r=Math.max(r,W*.2);
  const cx=W/2, cy=cTop+ring+r;
  if(eje==='calle'){
    g.fillStyle='#bc1734';g.beginPath();g.arc(cx,cy,r+ring,0,7);g.fill();
    g.strokeStyle='#bedff7';g.lineWidth=ring*.62;g.beginPath();g.arc(cx,cy,r+ring*.5,0,7);g.stroke();
    g.strokeStyle='#17233d';g.lineWidth=W*.0065;g.setLineDash([W*.03,W*.024]);g.beginPath();g.arc(cx,cy,r+ring*.5,0,7);g.stroke();g.setLineDash([]);
  } else if(eje==='accesible'){
    g.fillStyle='#fff';g.beginPath();g.arc(cx,cy,r+ring*.55,0,7);g.fill();
    g.strokeStyle='#17233d';g.lineWidth=W*.012;g.beginPath();g.arc(cx,cy,r+ring*.55,0,7);g.stroke();
  } else {
    g.fillStyle='#89ba96';g.beginPath();g.arc(cx,cy,r+ring*.8,0,7);g.fill();
    g.fillStyle='#4da070';g.beginPath();g.arc(cx,cy,r+ring*.35,0,7);g.fill();
  }
  g.save();g.beginPath();g.arc(cx,cy,r,0,7);g.clip();cover(g,im,cx-r,cy-r,2*r,2*r);g.restore();
  await bloqueEje(g,W,e,T,0,topSafe,true);
  panelDatos(g,W,v,T,gm);
  if(eje==='plaza')await drawCrop(g,'fondo-plaza',[28,2475,6917,297],0,y0-sh,W,sh);
}
/* Diseño B: foto a sangre arriba con corte diagonal y banda de color */
async function photoMarco(g,W,H,v,e,y0,topSafe,im){
  const eje=v.eje,T=TEMA[eje],gm=geo(W,H,y0,eje),{sh,panelT}=gm;
  g.fillStyle=T.bg;g.fillRect(0,0,W,y0);
  const pb=panelT+W*.05,sl=W*.09,bd=W*.022;
  g.fillStyle=T.band;g.beginPath();g.moveTo(0,0);g.lineTo(W,0);g.lineTo(W,pb+bd);g.lineTo(0,pb+sl+bd);g.closePath();g.fill();
  g.save();g.beginPath();g.moveTo(0,0);g.lineTo(W,0);g.lineTo(W,pb);g.lineTo(0,pb+sl);g.closePath();g.clip();cover(g,im,0,0,W,pb+sl);g.restore();
  await bloqueEje(g,W,e,T,0,topSafe,false);
  panelDatos(g,W,v,T,gm);
  if(eje==='plaza')await drawCrop(g,'fondo-plaza',[28,2475,6917,297],0,y0-sh,W,sh);
}
/* Diseño C: foto completa con degradado y texto encima */
async function photoCompleta(g,W,H,v,e,y0,topSafe,im){
  const story=H>W*1.6, fullH=story?H:y0, ytxt=story?H*.885-W*.17-W*.015:y0;  // stories: la foto cubre todo el lienzo (sin azul liso abajo) y los logos van sobre el degradado
  cover(g,im,0,0,W,fullH);
  const gr=g.createLinearGradient(0,fullH*.3,0,fullH);const col=e.dark;
  gr.addColorStop(0,col+'00');gr.addColorStop(.5,col+'b0');gr.addColorStop(1,col+'f5');g.fillStyle=gr;g.fillRect(0,fullH*.3,W,fullH*.7);
  const wa=await aspect(e.wm), cw=W*.36, ch=cw/wa, pad=W*.025, cx=W*.05, cy=topSafe+W*.04;
  g.fillStyle=e.chip;rrect(g,cx,cy,cw+pad*2,ch+pad*2,W*.02);g.fill();await drawSvg(g,e.wm,cx+pad,cy+pad,cw,ch);
  const bm=W*.06, mw=W-bm*2;
  const bl=[{t:v.kicker,w:600,s:W*.032,c:e.acento,up:true,gap:W*.012}];
  if(v.valor)bl.push({t:`${v.valor} ${v.etiqueta}`,w:800,s:W*.085,c:'#fff',lh:1.05,gap:W*.02});else bl.push({t:v.main,w:800,s:W*.085,c:'#fff',lh:1.05,gap:W*.02});
  if(v.sub)bl.push({t:v.sub,w:600,s:W*.04,c:'#fff',gap:W*.012});if(v.extra)bl.push({t:v.extra,w:600,s:W*.03,c:'#fff',op:.8});
  const lay=layout(g,bl,mw,ytxt*.55);drawLayout(g,lay,bm,ytxt-W*.04-lay.tot+(bl.at(-1).gap||0),'left',mw);
  return story?'full':undefined;
}
const ESTILOS={circulo:photoCirculo,marco:photoMarco,completa:photoCompleta};
async function photoPlate(g,W,H,v,e,y0,topSafe,fotoIdx,estilo){
  const im=await loadImg(v.fotos[fotoIdx%v.fotos.length]);
  const k=(estilo&&estilo!=='sugerido')?estilo:window.__estiloSugerido(v,im);
  return await ESTILOS[k](g,W,H,v,e,y0,topSafe,im);
}
async function brandPlate(g,W,H,v,e,y0,topSafe,eje){
  const bm=W*.07,mw=W-bm*2;
  const blocks=(col1,col2,col3)=>{const b=[];
    if(v.valor){b.push({t:v.valor,w:800,s:W*.26,c:col1,lh:1,gap:W*.01});b.push({t:v.etiqueta,w:800,s:W*.052,c:col2,up:true,gap:W*.025});}
    else b.push({t:v.main,w:800,s:W*.085,c:col1,up:true,lh:1.08,gap:W*.025});
    if(v.sub)b.push({t:v.sub,w:600,s:W*.042,c:col3,gap:W*.012});
    if(v.extra)b.push({t:v.extra,w:600,s:W*.032,c:col3,op:.75});return b;};
  if(eje==='calle'){
    const wa=await aspect(e.wm),ww=W*.36,wh=ww/wa,arcW=W*.42,arcH=arcW*520/1445;
    const bh=topSafe+W*.045+wh+arcH+W*.025;
    g.fillStyle='#fff';g.fillRect(0,0,W,y0);g.fillStyle=e.dark;g.fillRect(0,0,W,bh);
    await drawCrop(g,'fondo-calle',[3713,0,1956,680],W*.58,bh,W*.42,W*.42*680/1956);
    await drawCrop(g,'fondo-calle',[0,1729,1445,520],0,bh-arcH,arcW,arcH);
    await drawSvg(g,e.wm,bm,topSafe+W*.045,ww,wh);
    const top=bh+W*.05, lay=layout(g,blocks('#17233d','#bd1635','#17233d'),mw,y0-top-W*.04);
    drawLayout(g,lay,bm,top+(y0-top-W*.04-lay.tot)/2,'left',mw);
  } else if(eje==='accesible'){
    const wa=await aspect(e.wm),ww=W*.60,wh=ww/wa;
    const yh=topSafe>0?2*topSafe+wh:Math.max(W*1408/2835,wh+W*.09);const sc=yh/1408,iw=2835*sc; // stories: bloque simétrico, el logotipo queda centrado y fuera de la zona segura
    g.fillStyle='#fff';g.fillRect(0,0,W,y0);
    g.save();g.beginPath();g.rect(0,0,W,yh);g.clip();await drawCrop(g,'fondo-accesible',[0,0,2835,1408],(W-Math.max(iw,W))/2,0,Math.max(iw,W),yh);g.restore();
    await drawSvg(g,e.wm,(W-ww)/2,(yh-wh)/2,ww,wh);
    const top=yh+W*.03,hh=y0-top-W*.03;
    const b=[];
    if(v.valor)b.push({t:v.valor,w:800,s:W*.27,c:'#09467f',lh:1,gap:W*.012});else b.push({t:v.main,w:800,s:W*.085,c:'#09467f',up:true,gap:W*.02});
    const lay0=layout(g,b,mw,hh*.62);
    const pillH=v.valor?W*.1:0;const rest=[];if(v.sub)rest.push({t:v.sub,w:600,s:W*.04,c:'#17233d',gap:W*.01});if(v.extra)rest.push({t:v.extra,w:600,s:W*.03,c:'#17233d',op:.75});
    const lay1=layout(g,rest,mw,hh-lay0.tot-pillH-W*.03);
    const tot=lay0.tot+(v.valor?pillH+W*.025:0)+lay1.tot;let y=top+Math.max(0,(hh-tot)/2);
    drawLayout(g,lay0,bm,y,'center',mw);y+=lay0.tot;
    if(v.valor){g.font=`600 ${W*.05}px Poppins`;const tw=Math.min(mw,g.measureText(v.etiqueta).width+W*.1);g.fillStyle='#bedff7';rrect(g,(W-tw)/2,y,tw,pillH,W*.012);g.fill();g.fillStyle='#09467f';g.textAlign='center';g.fillText(v.etiqueta,W/2,y+pillH*.68);y+=pillH+W*.025;}
    drawLayout(g,lay1,bm,y,'center',mw);
  } else {
    const wa=await aspect(e.wm),ww=W*.50,wh=ww/wa,gh=topSafe+wh+W*.09,sh=W*297/6917;
    g.fillStyle='#fff';g.fillRect(0,0,W,y0);
    await drawCrop(g,'fondo-plaza',[5900,28,1000,700],W*.60,gh+W*.005,W*.40,W*.40*700/1000);
    g.fillStyle='#c6dfce';g.fillRect(0,0,W,gh);
    await drawCrop(g,'fondo-plaza',[150,220,560,520],W*.87,topSafe+W*.03,W*.10,W*.10*520/560);
    await drawCrop(g,'fondo-plaza',[1440,2120,580,350],W*.74,gh-W*.17,W*.19,W*.19*350/580);
    await drawSvg(g,e.wm,bm,topSafe+W*.075,ww,wh);
    await drawCrop(g,'fondo-plaza',[28,2475,6917,297],0,y0-sh,W,sh);
    const top=gh+W*.05,hh=y0-sh-top-W*.03;
    const lay=layout(g,blocks('#09467f','#4da070','#17233d'),mw,hh);drawLayout(g,lay,bm,top+(hh-lay.tot)/2,'left',mw);
  }
}
async function renderPlaca(canvas,v,fmt,fotoIdx=0,estilo='sugerido'){
  await document.fonts.load('800 40px Poppins');await document.fonts.load('600 40px Poppins');
  const [W,H]=FMT[fmt],g=canvas.getContext('2d');canvas.width=W;canvas.height=H;
  const story=fmt==='9x16',e=EJES[v.eje],topSafe=story?H*.14:0,y1=story?H*.885:H,y0=y1-W*.17;
  g.fillStyle='#fff';g.fillRect(0,0,W,H);
  let full=false;
  if(v.fotos&&v.fotos.length&&estilo!=='sinfoto')full=(await photoPlate(g,W,H,v,e,y0,topSafe,fotoIdx,estilo))==='full';else await brandPlate(g,W,H,v,e,y0,topSafe,v.eje);
  await footer(g,W,H,e,story,v.eje,full);
}
function descargar(canvas,nombre){canvas.toBlob(b=>{const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=nombre+'.png';document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},500)},'image/png')}
async function copiar(txt,btn){try{await navigator.clipboard.writeText(txt)}catch{const t=document.createElement('textarea');t.value=txt;document.body.appendChild(t);t.select();document.execCommand('copy');t.remove()}const o=btn.textContent;btn.textContent='¡Copiado!';btn.classList.add('ok');setTimeout(()=>{btn.textContent=o;btn.classList.remove('ok')},1200)}

/* ---------- calidad de foto: el diseño "Sugerido" ---------- */
const calCache=new Map();
function medirFoto(im){ // nitidez (varianza del laplaciano sobre una miniatura) y resolución
  const w=320,h=Math.max(1,Math.round(w*im.naturalHeight/im.naturalWidth)),c=document.createElement('canvas');c.width=w;c.height=h;
  const g=c.getContext('2d');g.drawImage(im,0,0,w,h);const d=g.getImageData(0,0,w,h).data,L=new Float32Array(w*h);
  for(let i=0;i<w*h;i++)L[i]=.299*d[i*4]+.587*d[i*4+1]+.114*d[i*4+2];
  let s=0,s2=0,n=0;for(let y=1;y<h-1;y++)for(let x=1;x<w-1;x++){const i=y*w+x,v=4*L[i]-L[i-1]-L[i+1]-L[i-w]-L[i+w];s+=v;s2+=v*v;n++}
  const m=s/n;return {nitidez:s2/n-m*m,ancho:im.naturalWidth,alto:im.naturalHeight,vertical:im.naturalHeight>im.naturalWidth*1.1};
}
window.__estiloSugerido=(v,im)=>{
  const q=calCache.get(im.src)||calCache.set(im.src,medirFoto(im)).get(im.src);
  const baja=Math.min(q.ancho,q.alto)<720||q.nitidez<UMBRAL_NITIDEZ;
  if(baja)return 'circulo';                 // chica o pixelada: recortada en círculo disimula la falta de definición
  if(q.vertical)return 'completa';          // vertical y nítida: a pantalla completa
  return ['completa','marco','circulo'][hash(v.id||'')%3]; // horizontal y nítida: variedad
};

/* ---------- históricos y contenidos periódicos ---------- */
const HIST=(DATA.hist||[]).slice().sort((a,b)=>a.fecha<b.fecha?-1:1);
const VENT=[[7,'la última semana','Lectura semanal'],[10,'los últimos 10 días','Lectura a 10 días'],[15,'los últimos 15 días','Lectura a 15 días'],[30,'el último mes','Lectura mensual']];
function habiles(ini,fin){let n=0;for(const d=new Date(ini);d<=fin;d.setDate(d.getDate()+1)){const w=d.getDay();if(w&&w<6)n++}return n}
function ventana(N){
  const fin=new Date(P.fecha+'T00:00:00'),ini=new Date(fin);ini.setDate(ini.getDate()-(N-1));const req=habiles(ini,fin);
  const dias=HIST.filter(d=>{const t=new Date(d.fecha+'T00:00:00');return t>=ini&&t<=fin});
  const prom=a=>a.reduce((s,x)=>s+x,0)/a.length;
  return {N,k:dias.length,completo:dias.length>=req,unicas:uniq(dias.flatMap(d=>d.ids)).length,   // una esquina con varias rampas es una sola obra
    promEjec:Math.round(prom(dias.map(d=>d.enEjecucion))),promPuestos:Math.round(prom(dias.map(d=>d.puestos))),
    finPeriodo:dias.length>1&&dias.at(-1).finalizadas!=null&&dias[0].finalizadas!=null?dias.at(-1).finalizadas-dias[0].finalizadas:null,req};
}
function periodicos(){
  const out=[];
  VENT.forEach(([N,per,nombre])=>{
    const w=ventana(N);
    if(!w.completo){out.push({id:'p_'+N,titulo:nombre,estado:`Faltan partes: hay ${w.k} de los ${w.req} días hábiles del período. Pasame los partes que faltan y se arma solo.`,w});return}
    const cap=s=>s[0].toUpperCase()+s.slice(1), U=w.unicas, F=w.finPeriodo;
    const titulos=uniq([
      `En ${per} se ejecutaron ${U} obras en la ciudad de Córdoba`,
      `En ${per}, en promedio, hubo ${w.promEjec} obras en ejecución por día en la ciudad`,
      `En ${per}, en promedio, las obras generaron ${nf(w.promPuestos)} puestos de trabajo directos por día`,
      F>0?`En ${per} se finalizaron ${F} obras en Córdoba`:null,
      FINOK?(P.finalizadas%50===0?`Ya se finalizaron ${P.finalizadas} obras en la ciudad`:`Ya se finalizaron más de ${redondo(P.finalizadas,50)} obras en la ciudad`):null
    ].filter(Boolean)).map(limpio);
    const dato=`En ${per}, el Gobierno de la Provincia y la Municipalidad de Córdoba ejecutaron ${U} obras distintas en la ciudad. En promedio, hubo ${w.promEjec} obras en ejecución por día y las obras generaron ${nf(w.promPuestos)} puestos de trabajo directos por día${F>0?`. En ese período se finalizaron ${F} obras`:''}`;
    out.push({id:'p_'+N,titulo:nombre,w,eje:'calle',titulos,
      ig:limpio(`📊 ${up(cap(per))}: ${U} OBRAS EN LA CIUDAD\n\n${dato}.\n\n${MODELO}\n\n#CórdobaMejora #HacerParaCrecer`),
      x:limpio(`📊 En ${per}, en promedio, hubo ${w.promEjec} obras en ejecución por día en Córdoba y las obras generaron ${nf(w.promPuestos)} puestos de trabajo directos por día. Hacer para Crecer. #CórdobaMejora #HacerParaCrecer`),
      placa:{eje:'calle',fotos:[],extra:'',kicker:nombre,valor:String(U),etiqueta:`Obras en ${per}`,sub:`${w.promEjec} en ejecución por día, en promedio`},
      gac:limpio(gacetilla({titulo:titulos[0],bajada:[`En promedio, hubo ${w.promEjec} obras en ejecución por día.`,`Las obras generaron ${nf(w.promPuestos)} puestos de trabajo directos por día, en promedio.`,'Hacer para Crecer: obra pública sostenida en toda la ciudad.'],
        lead:`${cap(dato)}.`,secciones:[['Los programas',[EJES.calle.marco,EJES.accesible.marco,EJES.plaza.marco]]],cierre:MODELO}))});
  });
  Object.entries(CONT.periodicos||{}).forEach(([id,c])=>{
    const ex=out.find(p=>p.id===id);
    const pz=ex&&!ex.estado?ex:null;
    const nuevo={id,titulo:c.titulo||(ex&&ex.titulo)||id,eje:c.eje||'calle',titulos:(c.titulos||[]).map(limpio),ig:limpio(c.ig||''),x:limpio(c.x||''),gac:limpio(c.gac||''),placa:{eje:c.eje||'calle',fotos:[],extra:'',...(c.placa||{})},redactado:true,w:ex&&ex.w};
    if(ex)out[out.indexOf(ex)]=nuevo;else out.push(nuevo);
  });
  const ord=id=>{const m=id.match(/^p_(\d+)(?:_(\w+))?$/);return m?[VENT.findIndex(v=>v[0]==+m[1]),['','plazas','rampas','pav','calle'].indexOf(m[2]||'')]:[99,0]};
  out.sort((a,b)=>{const x=ord(a.id),y=ord(b.id);return x[0]-y[0]||x[1]-y[1]});
  return out;
}

/* ---------- UI ---------- */
const S={tab:'obras',circ:null,tipo:null,foto:null,q:''};const ESTILOS_UI=[['sugerido','Sugerido'],['circulo','Círculo'],['marco','Marco'],['completa','Foto completa'],['sinfoto','Sin foto']];
const placaHTML=(id,v)=>`<div class="fmts">${Object.entries(FMT).map(([k,f])=>`<div class="fmt"><div class="lbl">${f[2]}</div><canvas data-fmt="${k}"></canvas><div class="btns" style="justify-content:center"><button class="btn" data-dl="${k}">Bajar PNG</button></div></div>`).join('')}</div>
 <div class="btns"><button class="btn sec" data-dlall>Bajar las 3 placas</button></div>
 ${v.fotos&&v.fotos.length?`<div class="fotosel">Diseño: ${ESTILOS_UI.map(([k,l],i)=>`<button class="btn ${i?'sec':''}" data-estilo="${k}">${l}</button>`).join('')}</div><div class="fotosel" data-sug></div>`:''}
 ${v.fotos&&v.fotos.length>1?`<div class="fotosel">Foto: ${v.fotos.map((_,i)=>`<button class="btn sec" data-foto="${i}">${i+1}</button>`).join('')}</div>`:''}`;
function txHTML(ig,x,pl,gac,titulos){return `
 ${titulos&&titulos.length?`<div class="tx"><div class="row"><label>Opciones de título</label></div>${titulos.map(t=>`<div class="titulo"><span>${esc(t)}</span><button class="btn sec" data-copytxt="${esc(t)}">Copiar</button></div>`).join('')}</div>`:''}
 <div class="tx"><div class="row"><label>Copy de Instagram</label><button class="btn" data-copy="ig">Copiar</button></div><textarea data-t="ig" rows="11">${esc(ig)}</textarea></div>
 <div class="tx"><div class="row"><label>Texto para X <span class="n" data-n></span></label><button class="btn" data-copy="x">Copiar</button></div><textarea data-t="x" rows="5">${esc(x)}</textarea></div>
 <div class="tx"><div class="row"><label>Texto de la placa <span class="n">(editable: cambia la placa)</span></label><button class="btn" data-copy="pl">Copiar</button></div><textarea data-t="pl" rows="4">${esc(pl)}</textarea></div>${gac?`<div class="tx"><div class="row"><label>Gacetilla de prensa</label><button class="btn" data-copy="gac">Copiar</button></div><textarea data-t="gac" rows="16">${esc(gac)}</textarea></div>`:'' }`;}
function wire(card,id,v){
  const state={foto:0,estilo:'sugerido',done:false};
  const draw=()=>card.querySelectorAll('canvas').forEach(c=>renderPlaca(c,v,c.dataset.fmt,state.foto,state.estilo));
  const sug=card.querySelector('[data-sug]');
  const mostrarSug=async()=>{if(!sug)return;const im=await loadImg(v.fotos[state.foto%v.fotos.length]);const q=calCache.get(im.src)||calCache.set(im.src,medirFoto(im)).get(im.src);const k=window.__estiloSugerido(v,im);
    sug.textContent=`Sugerido: ${{circulo:'Círculo',marco:'Marco',completa:'Foto completa'}[k]} · foto de ${q.ancho}×${q.alto}px, ${q.vertical?'vertical':'horizontal'}, nitidez ${Math.round(q.nitidez)}`;};
  card.addEventListener('toggle',()=>{if(card.open&&!state.done){state.done=true;draw();mostrarSug()}});
  card.addEventListener('click',ev=>{const b=ev.target.closest('button');if(!b)return;
    if(b.dataset.dl){const c=card.querySelector(`canvas[data-fmt="${b.dataset.dl}"]`);descargar(c,`${id}_${b.dataset.dl}`)}
    else if(b.dataset.dlall){[...card.querySelectorAll('canvas')].forEach((c,i)=>setTimeout(()=>descargar(c,`${id}_${c.dataset.fmt}`),i*400))}
    else if(b.dataset.foto!==undefined){state.foto=+b.dataset.foto;draw();mostrarSug()}
    else if(b.dataset.estilo){state.estilo=b.dataset.estilo;card.querySelectorAll('[data-estilo]').forEach(x=>x.classList.toggle('sec',x!==b));draw()}
    else if(b.dataset.copytxt!==undefined){copiar(b.dataset.copytxt,b)}
    else if(b.dataset.copy){copiar(card.querySelector(`textarea[data-t="${b.dataset.copy}"]`).value,b)}});
  const x=card.querySelector('textarea[data-t="x"]'),n=card.querySelector('[data-n]');const cnt=()=>{n.textContent=x.value.length+'/280';n.classList.toggle('bad',x.value.length>280)};x.addEventListener('input',cnt);cnt();
  const pl=card.querySelector('textarea[data-t="pl"]');let tm;pl.addEventListener('input',()=>{leerPlaca(v,pl.value);clearTimeout(tm);tm=setTimeout(draw,350)});  // el texto editado se refleja en la placa
}
function obraCard(o){
  const v=placaDe(o),e=EJES[o.eje];
  const el=document.createElement('details');el.className='card e-'+o.eje;
  const tit=o.tipo==='plaza'?o.via:(o.via||o.sector)+(o.entre?` · entre ${o.entre}`:'');
  el.innerHTML=`<summary><div class="tt"><b>${esc(tit)}</b><span>${esc(TIPOS[o.tipo].label)}${bar(o)?' · Barrio '+esc(bar(o)):''}${o.tipo==='rampas'&&!o.grupo?` · ${o.rampas} ${o.rampas===1?'rampa':'rampas'}`:''}${o.grupo?` · grupo de ${esq(o)} esquinas, ${o.rampas} rampas`:''}</span></div>
   ${o.grupo?'<span class="tag grupo">Grupo</span>':''}<span class="tag ${o.fotos.length?'foto':'sinfoto'}">${o.fotos.length?'Con foto':'Sin foto'}</span><span class="tag ${o.eje}">${esc(e.nombre.split(' – ')[0])}</span></summary>
   <div class="body"><div class="grid"><div>${placaHTML(o.id,v)}</div><div>${txHTML(textoIG(o),textoX(o),textoPlaca(v))}</div></div>
   <div class="meta">Parte: circuito ${esc(o.circuito)}${o.circNombre?' · '+esc(o.circNombre):''} · ${o.driveUrl?`<a href="${esc(o.driveUrl)}" target="_blank" rel="noopener">Doc/archivo en Drive</a>`:'sin link de Drive'}</div>
   ${o.docTxt?`<details class="doc"><summary>Texto original del doc</summary><pre>${esc(o.docTxt)}</pre></details>`:''}</div>`;
  wire(el,o.id,v);return el;
}
function renderObras(root){
  const f=reales.filter(o=>(!S.circ||o.circuito===S.circ)&&(!S.tipo||o.tipo===S.tipo)&&(!S.foto||(S.foto==='con')===(o.fotos.length>0))&&(!S.q||norm([o.via,o.sector,o.barrio,o.entre,o.circNombre,o.circuito].filter(Boolean).join(' ')).includes(norm(S.q))));
  const grupos=obras.filter(o=>o.grupo&&(!S.circ||o.circuito===S.circ)&&(!S.tipo||o.tipo===S.tipo)&&(!S.foto||(S.foto==='con')===(o.fotos.length>0)));
  const circs=uniq(reales.map(o=>o.circuito)).sort((a,b)=>parseInt(a)-parseInt(b)||a.localeCompare(b));
  const cn=c=>reales.filter(o=>o.circuito===c).length, nCon=reales.filter(o=>o.fotos.length).length;
  root.innerHTML=`<div class="filters"><h4>Circuito del parte · tocá para filtrar</h4><div class="chips" id="fc">${circs.map(c=>`<button class="chip ${S.circ===c?'on':''}" data-c="${c}">${c}<small>${cn(c)}</small></button>`).join('')}</div>
   <h4>Tipo de obra</h4><div class="chips" id="ft">${TIPO_ORDEN.map(t=>`<button class="chip t-${TIPOS[t].eje} ${S.tipo===t?'on':''}" data-t="${t}">${TIPOS[t].corto}<small>${reales.filter(o=>o.tipo===t).length}</small></button>`).join('')}</div>
   <h4>Foto</h4><div class="chips" id="ff"><button class="chip ${S.foto==='con'?'on':''}" data-f="con">Con foto<small>${nCon}</small></button><button class="chip ${S.foto==='sin'?'on':''}" data-f="sin">Sin foto<small>${reales.length-nCon}</small></button></div>
   <input class="search" placeholder="Buscar calle, barrio…" value="${esc(S.q)}" id="q"></div>
   <div class="count">${f.length} de ${reales.length} obras${S.circ||S.tipo||S.foto||S.q?' · <a href="#" id="clr">limpiar filtros</a>':''}</div><div id="list"></div>`;
  const list=$('#list',root);const byC={};f.concat(grupos).forEach(o=>(byC[o.circuito]??=[]).push(o));
  Object.keys(byC).sort((a,b)=>parseInt(a)-parseInt(b)||a.localeCompare(b)).forEach(c=>{
    const h=document.createElement('div');h.className='circ-head';h.innerHTML=`${esc(c)} <small>${esc(CIRC[c]||'(sin nombre en data/circuitos.json)')} · ${byC[c].filter(o=>!o.grupo).length} obras</small>`;list.appendChild(h);
    byC[c].sort((a,b)=>(b.grupo?1:0)-(a.grupo?1:0)||TIPO_ORDEN.indexOf(a.tipo)-TIPO_ORDEN.indexOf(b.tipo)).forEach(o=>list.appendChild(obraCard(o)));});
  root.onclick=ev=>{const b=ev.target.closest('.chip');if(b&&b.dataset.c){S.circ=S.circ===b.dataset.c?null:b.dataset.c;renderObras(root)}else if(b&&b.dataset.t){S.tipo=S.tipo===b.dataset.t?null:b.dataset.t;renderObras(root)}else if(b&&b.dataset.f){S.foto=S.foto===b.dataset.f?null:b.dataset.f;renderObras(root)}else if(ev.target.id==='clr'){ev.preventDefault();S.circ=S.tipo=S.foto=null;S.q='';renderObras(root)}};
  $('#q',root).oninput=ev=>{S.q=ev.target.value;clearTimeout(S._t);S._t=setTimeout(()=>{renderObras(root);const q=$('#q',root);q.focus();q.setSelectionRange(q.value.length,q.value.length)},250)};
}
function tarjetaContenido(gx,rotulo){
  const el=document.createElement('details');el.className='card e-'+gx.eje;
  el.innerHTML=`<summary><div class="tt"><b>${esc(gx.titulo)}</b><span>${esc(gx.placa.valor||'')} ${esc(gx.placa.etiqueta||'')}</span></div><span class="tag ${gx.eje}">${rotulo}</span></summary>
   <div class="body"><div class="grid"><div>${placaHTML(gx.id,gx.placa)}</div><div>${txHTML(gx.ig,gx.x,textoPlaca(gx.placa),gx.gac,gx.titulos)}</div></div></div>`;
  wire(el,gx.id,gx.placa);return el;
}
function renderGenerales(root){
  root.innerHTML=`<div class="note">Estos contenidos se calculan <b>sumando el parte del día</b> (${R.obras} obras, ${R.rampas} rampas, ${R.cuadras} cuadras de las memorias). Sin montos ni cifras fiscales: el relato del modelo cordobés va con los mensajes oficiales.</div><div class="gen-grid" id="gl"></div>`;
  generales().forEach(gx=>$('#gl',root).appendChild(tarjetaContenido(gx,'General')));
}
function renderPeriodicos(root){
  const F=P.finalizadas||0, m50=redondo(F,50), prox=m50+50;
  root.innerHTML=`<div class="note">Los contenidos periódicos se arman acumulando los partes diarios guardados: <b>${HIST.length} ${HIST.length===1?'parte cargado':'partes cargados'}</b> (${HIST.map(h=>h.fecha).join(', ')}). Cada día que me pases un parte nuevo se suma al histórico.</div>
   <div class="list"><h3>Números redondos para titulares</h3><ul>
    ${FINOK?`<li>${F%50===0?`<b>Ya se finalizaron ${F} obras</b> en la ciudad: número redondo para titular.`:`Obras finalizadas: ${F}. Titular posible hoy: “Ya se finalizaron más de ${m50} obras”. Faltan ${prox-F} para llegar a ${prox}.`}</li>`:'<li>El parte de hoy no trae el total de obras finalizadas: no se arman titulares con ese dato.</li>'}
    <li>Obras en ejecución hoy: ${R.obras}. Puestos de trabajo directos: ${nf(P.puestos)}.</li></ul></div><div class="gen-grid" id="gl"></div>`;
  periodicos().forEach(p=>{
    if(p.estado){const d=document.createElement('div');d.className='list';d.innerHTML=`<h3>${esc(p.titulo)}</h3><div style="font-size:12.5px;color:var(--muted);font-weight:600">${esc(p.estado)}</div>`;$('#gl',root).appendChild(d);return}
    $('#gl',root).appendChild(tarjetaContenido(p,'Periódico'));});
}
function renderCalidad(root){
  // textos publicables que se revisan
  const T=[];reales.concat(obras.filter(o=>o.grupo)).forEach(o=>{const v=placaDe(o);T.push([o.id+' · Instagram',textoIG(o)],[o.id+' · X',textoX(o)],[o.id+' · placa',textoPlaca(v)])});
  generales().concat(periodicos().filter(p=>!p.estado)).forEach(g=>{T.push([g.id+' · Instagram',g.ig],[g.id+' · X',g.x],[g.id+' · gacetilla',g.gac],[g.id+' · placa',textoPlaca(g.placa)]);g.titulos.forEach((t,i)=>T.push([g.id+' · título '+(i+1),t]))});
  const test=(re)=>T.filter(([,t])=>re.test(t)).map(([n])=>n);
  const reglas=[['No menciona “circuito” ni “seccional”',test(/circuito|seccional/i)],['No menciona montos ni signos de pesos',test(/\$|presupuesto|monto/i)],['No usa barras “/” (salvo en links)',T.filter(([,t])=>/\//.test(t.replace(/https?:\/\/\S+/g,''))).map(([n])=>n)],['No menciona asistencia social en textos de obras',test(/asistencia social/i)],['Las piezas generales y periódicas no repiten la misma frase larga',(()=>{const c={};T.filter(([n])=>/^(g_|p_)/.test(n)&&!/· X$/.test(n)&&!/· placa$/.test(n)).forEach(([n,t])=>new Set(t.split(/(?<=[.!?])\s+/).filter(s=>s.length>70)).forEach(s=>{(c[s]=c[s]||[]).push(n.split(' ')[0])}));return Object.entries(c).filter(([,v])=>v.length>2).map(([s,v])=>s.slice(0,40)+'… ('+v.length+' piezas)')})()],['Los textos de X no superan 280 caracteres',T.filter(([n,t])=>/· X$/.test(n)&&t.length>280).map(([n])=>n)],['Los textos de X no terminan cortados (…)',T.filter(([n,t])=>/· X$/.test(n)&&/…/.test(t)).map(([n])=>n)],['Las obras con barrio lo nombran con la palabra “Barrio”',reales.filter(o=>bar(o)&&!new RegExp('Barrio '+bar(o).replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).test(textoIG(o))&&o.tipo!=='rampas').map(o=>o.id)]];
  const sf=reales.filter(o=>!o.fotos.length), sd=reales.filter(o=>!o.docTxt), sm=reales.filter(o=>!['rampas','plaza'].includes(o.tipo)&&!o.m.m2&&!o.m.ml&&!o.m.cuadras), sb=reales.filter(o=>!bar(o));
  const nm=o=>esc((o.via||o.sector)+(o.entre?` (${o.entre})`:''));
  const L=(t,a,hint)=>`<div class="list"><h3>${t} <small>(${a.length})</small></h3>${hint?`<div class="hint">${hint}</div>`:''}<ul>${a.map(x=>`<li>${x}</li>`).join('')||'<li>Nada pendiente</li>'}</ul></div>`;
  root.innerHTML=`<div class="note gris">Chequeo automático de los textos publicables y datos que faltan. No se rellena ningún dato: lo que falta queda fuera del texto.</div>
   <div class="list gris"><h3>Reglas de redacción</h3><ul>${reglas.map(([n,bad])=>`<li>${bad.length?'✖':'✔'} ${n}${bad.length?` — <b>${bad.length}</b> casos: ${esc(bad.slice(0,4).join(', '))}${bad.length>4?'…':''}`:''}</li>`).join('')}</ul><div class="hint">${T.length} textos revisados.</div></div>
   ${L('Avisos y contradicciones (parte vs. docs)',P.avisos.map(esc))}
   ${L('Obras sin foto (placa solo texto)',sf.map(nm),'Soltá la foto como <code>entrada/'+P.fecha+'/fotos/&lt;id-obra&gt;.jpg</code> o agregá el link de Drive en el parte.')}
   ${L('Obras sin texto de Drive',sd.map(nm))}
   ${L('Obras sin magnitud (m², cuadras o metros)',sm.map(nm),'Con un dato de magnitud el texto y la placa ganan una cifra concreta.')}
   ${L('Obras sin barrio informado',sb.map(nm),'Se nombran por calle o esquina; si el parte trae el barrio, se usa siempre.')}`;
}
function renderHeader(){
  const lk='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(A.svg['gobierno-color']);$('#lockup').src=lk;$('#lockup2').src=lk;
  $('#sub').textContent=P.fecha_texto+' · parte de obras';
  $('#kpis').innerHTML=[[P.enEjecucion,'en ejecución'],[P.finalizadas??'—','finalizadas'],[nf(P.puestos),'puestos directos'],[R.barrios,'barrios (mínimo)'],[R.rampas,'rampas'],[R.cuadras,'cuadras (memorias)']].map(([a,b])=>`<div class="kpi"><b>${a}</b><span>${b}</span></div>`).join('');
  const tabs=[['obras','Contenidos de obras del día'],['generales','Contenidos generales del día'],['periodicos','Contenidos periódicos'],['calidad','Chequeo de calidad']];
  $('#tabs').innerHTML=tabs.map(([k,l])=>`<button data-k="${k}" class="${S.tab===k?'on':''}${k==='calidad'?' cal':''}">${l}</button>`).join('');
  $('#tabs').onclick=ev=>{const b=ev.target.closest('button');if(b){S.tab=b.dataset.k;go()}};
}
function go(){renderHeader();const m=$('#main');m.onclick=null;({obras:renderObras,generales:renderGenerales,periodicos:renderPeriodicos,calidad:renderCalidad})[S.tab](m)}
go();
})();
</script>
</body>
</html>
~~~~
