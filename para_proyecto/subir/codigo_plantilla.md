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
/* cabecera: marca, título grande con la última actualización y el selector de módulo; debajo, la franja tricolor y la barra de vista */
header{background:#fff;padding:12px 20px 0;position:sticky;top:0;z-index:20;box-shadow:0 2px 14px #00000012}
.top{display:flex;align-items:center;gap:18px;flex-wrap:wrap}
.top img{height:38px;display:block}
.top .ttl{border-left:1px solid var(--line);padding-left:18px;min-width:0}
h1{margin:0;font-weight:900;font-size:24px;line-height:1.1;color:var(--marino);letter-spacing:.2px}
.sub{color:var(--muted);font-size:12.5px;font-weight:600;margin-top:3px} .sub b{color:var(--ink);font-weight:700}
/* navegación entre módulos (tipo de contenido): a la derecha, el módulo actual resaltado */
nav.mods{margin-left:auto;display:inline-flex;gap:3px;background:#f3f3f4;border-radius:999px;padding:3px}
nav.mods a{padding:7px 18px;border-radius:999px;font:700 13.5px Poppins;color:var(--gris);text-decoration:none}
nav.mods a:hover{color:var(--ink)} nav.mods a.on{background:var(--marino);color:#fff}
.cinta{height:4px;margin:12px -20px 0;background:linear-gradient(90deg,var(--celeste) 0 33.34%,var(--rojo) 33.34% 66.67%,var(--dorado) 66.67%)}
/* barra de vista: cruza toda la hoja. Primero se elige qué ver (Obra por obra, Resumen); Chequeo queda como enlace discreto a la derecha */
.vista{display:flex;align-items:flex-end;gap:6px;flex-wrap:wrap;padding-top:8px;margin:0 -20px;padding-left:20px;padding-right:20px;background:#fff}
.vista .tab{border:0;background:transparent;padding:9px 18px 11px;border-radius:10px 10px 0 0;font:700 15px Poppins;color:var(--gris);position:relative;cursor:pointer;line-height:1.2;text-align:left}
.vista .tab small{display:block;font-size:11px;font-weight:600;opacity:.8;margin-top:1px}
.vista .tab.on{color:var(--marino);background:var(--bg)}
.vista .tab.on::after{content:"";position:absolute;left:18px;right:18px;top:0;height:3px;border-radius:0 0 3px 3px;background:var(--rojo)}
.vista .tab:focus-visible{outline:2px solid var(--celeste);outline-offset:-2px}
.vista .chequeo{margin-left:auto;align-self:center;border:0;background:transparent;font:600 12.5px Poppins;color:var(--muted);display:inline-flex;align-items:center;gap:7px;padding:6px 10px;border-radius:8px;margin-bottom:6px;cursor:pointer}
.vista .chequeo .dot{width:9px;height:9px;border-radius:50%;background:#2e8b57;box-shadow:0 0 0 3px #2e8b5722}
.vista .chequeo.avisos .dot{background:var(--amarillo);box-shadow:0 0 0 3px #eaab3b33}
.vista .chequeo:hover,.vista .chequeo.on{background:#f3f3f4;color:var(--ink)}
/* período: pertenece a la vista elegida (fila completa, arriba de la columna lateral y del contenido) */
.perbar{grid-column:1 / -1;display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:-2px 0 2px}
.perbar .lbl{font-size:10.5px;font-weight:800;letter-spacing:.7px;text-transform:uppercase;color:var(--gris);margin-right:4px}
.pchip{border:1px solid var(--line);background:#fff;border-radius:999px;padding:6px 14px;font:700 12.5px Poppins;color:var(--ink);cursor:pointer;display:inline-flex;align-items:baseline;gap:6px}
.pchip small{font-weight:600;color:var(--muted);font-size:11px}
.pchip:hover{border-color:#c9ccd3}
.pchip.on{background:var(--marino);border-color:var(--marino);color:#fff} .pchip.on small{color:#ffffffb3}
.pchip.semana.on{background:var(--dorado);border-color:var(--dorado);color:var(--marino)} .pchip.semana.on small{color:#17233dcc}
.pchip:disabled{opacity:.5;cursor:not-allowed}
/* rótulo de contexto: dónde estoy (zona, período con sus fechas y alcance). El período se marca con el color de siempre: marino el día, dorado la semana */
.ctx{display:flex;align-items:baseline;justify-content:space-between;gap:8px 16px;flex-wrap:wrap;margin:2px 0 12px}
.ctx .l1{font-size:19px;font-weight:900;line-height:1.2;color:var(--marino)}
.ctx .l1 .sep{opacity:.4;font-weight:700;margin:0 6px}
.ctx .l1 .pt{font-weight:700;font-size:15px;color:var(--gris)}
.ctx.semana .l1 .pt{color:#9a7a3a}
.ctx .l2{font-size:12px;font-weight:600;color:var(--muted)}
.tag.dias{background:#f6ecd8;color:#6b4a05} .tag.circ{background:#f1f1f1;color:#6f747d}
/* cuerpo: columna lateral fija con los filtros y el área de trabajo a la derecha */
.wrap{display:grid;grid-template-columns:250px minmax(0,1fr);gap:18px;max-width:1900px;margin:0 auto;padding:14px 16px 40px}
aside{position:sticky;top:calc(var(--hh,52px) + 12px);align-self:start;max-height:calc(100vh - var(--hh,52px) - 24px);overflow:auto;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 12px 6px;scrollbar-width:thin}
aside h4{margin:0 0 5px;font-size:10.5px;text-transform:uppercase;letter-spacing:.7px;color:var(--gris);font-weight:800}
aside .sec{margin-bottom:11px;padding-bottom:9px;border-bottom:1px solid var(--line)} aside .sec:last-child{border-bottom:0}
aside .chips{gap:4px;margin-bottom:0}
aside .chip{padding:3px 9px;font-size:11.5px}
aside .zl{display:grid;grid-template-columns:1fr 1fr;gap:2px 4px} aside .zl .todo,aside .zl .subs{grid-column:1 / -1}
aside .zl button{display:flex;align-items:center;justify-content:space-between;width:100%;border:0;background:transparent;border-radius:7px;padding:3px 8px;font:700 12px Poppins;color:var(--ink);cursor:pointer;text-align:left}
aside .zl button:hover{background:#f3f3f4} aside .zl button.on{background:var(--rojo);color:#fff}
aside .zl button small{font-weight:700;opacity:.55}
aside .zl .subs{display:flex;flex-wrap:wrap;gap:3px;padding:3px 0 5px 10px}
aside .zl .subs .chip{padding:1px 8px;font-size:10.5px;background:#f3f3f4;color:#6f747d;border-color:#e6e6e8}
aside .zl .subs .chip.on{background:#8a8f98;color:#fff;border-color:#8a8f98}
aside details.datos summary{cursor:pointer;font-size:10.5px;text-transform:uppercase;letter-spacing:.7px;color:var(--gris);font-weight:800;list-style:revert}
aside .kpis{display:grid;grid-template-columns:1fr 1fr;gap:6px 8px;margin:8px 0 2px}
aside .kpi{display:flex;flex-direction:column;border-left:3px solid var(--celeste);padding-left:7px;line-height:1.15}
aside .kpi:nth-child(3n+2){border-left-color:var(--rojo)} aside .kpi:nth-child(3n){border-left-color:var(--dorado)}
aside .kpi b{font-size:15px;font-weight:900;color:var(--ink)} aside .kpi span{font-size:10.5px;color:var(--muted);font-weight:600}
aside .search{max-width:none;font-size:12.5px;padding:6px 9px}
aside .res{font-size:11.5px;color:var(--muted);font-weight:600;margin-top:6px;line-height:1.35}
aside .clr{font-size:11.5px;color:var(--link);font-weight:700;cursor:pointer;background:none;border:0;padding:0;margin-top:6px}
main{min-width:0}
@media(max-width:900px){.wrap{grid-template-columns:1fr}aside{position:static;max-height:none}}
@media(max-width:700px){.card>summary{flex-wrap:wrap;gap:6px}.card>summary .tt{flex:1 1 100%}}
.listbar{display:flex;align-items:center;justify-content:space-between;gap:10px;margin:2px 0 10px}
.listbar .count{margin:0}
h2.otras{margin:22px 0 10px;font-size:15px;font-weight:900;color:var(--gris);text-transform:uppercase;letter-spacing:.6px;border-top:1px solid var(--line);padding-top:14px}
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
.circ-head{margin:14px 0 6px;font-weight:900;font-size:16px;display:flex;gap:8px;align-items:baseline;color:var(--rojo)}
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
.tag.foto{background:#e7f4ea;color:#1f6a35} .tag.sinfoto{background:#f1f1f1;color:#777} .tag.generica{background:#eceef1;color:var(--marino)} .tag.grupo{background:#f4e6c8;color:#7a5a1c}
.body{padding:4px 14px 16px;border-top:1px solid var(--line)}
.grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:18px;margin-top:12px}
@media(max-width:1200px){.grid{grid-template-columns:1fr}} @media(max-width:860px){.top .ttl{border-left:0;padding-left:0}}
.fmts{display:grid;grid-template-columns:repeat(3,1fr);gap:10px} .fmts.con-p{grid-template-columns:repeat(4,1fr)}
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
.fotosel{display:flex;gap:6px;margin-top:8px;align-items:center;font-size:12px;font-weight:600;flex-wrap:wrap}
/* foto propia: se sube desde la tarjeta (queda en este navegador) y se encuadra arrastrando la placa */
.fotosel .mini{width:40px;height:40px;object-fit:cover;border-radius:6px;border:1px solid var(--line);background:#eee}
.fotosel label.btn{cursor:pointer} .fotosel input[type=file]{display:none}
.fotosel .enc{flex-basis:100%;font-size:11px;color:var(--muted);font-weight:600;display:flex;align-items:center;gap:6px} .fotosel .enc input{width:120px;margin:0}
.fotosel .aviso{font-size:11px;color:var(--rojo);font-weight:700}
/* miniaturas de foto: las del parte, la propia y, en una tira aparte, las genéricas de la galería del rubro (assets/galeria/<rubro>/) */
.fotosel .mb{border:2px solid transparent;border-radius:9px;background:none;padding:2px;cursor:pointer;display:inline-flex;flex-direction:column;align-items:center;gap:1px;font:700 10.5px Poppins;color:var(--gris)}
.fotosel .mb img{width:56px;height:56px;object-fit:cover;border-radius:6px;display:block;background:#eee}
.fotosel .mb:hover{border-color:var(--line)} .fotosel .mb.on{border-color:var(--eje,var(--marino));color:var(--ink)}
.fotosel.gal{border-top:1px dashed var(--line);padding-top:6px} .fotosel.gal .gt{flex-basis:100%;font-size:11.5px;font-weight:700;color:var(--gris)}
.fotosel label.pie{display:inline-flex;align-items:center;gap:5px;margin-left:8px;font-weight:700;cursor:pointer} .fotosel label.pie input{margin:0;accent-color:var(--marino)}
.fotosel .genaviso{font-size:11.5px;font-weight:700;color:var(--marino);background:#eceef1;border-radius:6px;padding:3px 9px}
.fmt canvas.movible{cursor:grab} .fmt canvas.movible:active{cursor:grabbing}
.note{background:#fbf5e8;border:1px solid #ecd9a8;border-left:5px solid var(--dorado);border-radius:10px;padding:10px 14px;font-size:12.5px;margin-bottom:14px;font-weight:600}
.list{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin-bottom:12px}
.list h3{margin:0 0 6px;font-size:14px;font-weight:800;color:var(--rojo)} .list ul{margin:0;padding-left:18px} .list li{margin:2px 0;font-size:12.5px;font-weight:600}
.gen-grid{display:grid;gap:12px}
.titulo{display:flex;gap:8px;align-items:center;justify-content:space-between;padding:6px 10px;border:1px solid var(--line);border-radius:8px;margin-bottom:6px;font-weight:700;font-size:12.5px;background:#fafafa}
.gris{background:#f3f3f4!important;border-color:#e0e0e2!important;border-left-color:#b8bcc4!important;color:#6f747d}
.gris h3{color:#6f747d!important}
.list .hint,.list h3 small{font-size:12px;color:var(--muted);font-weight:600}.list .hint{margin-bottom:6px}
/* tamaño personalizado: control en la fila del período y cuarto recuadro de cada placa */
.tam{margin-left:auto;font-size:12px;font-weight:600;color:var(--muted);display:inline-flex;align-items:center;gap:6px;flex-wrap:wrap}
.tam b{color:var(--ink);font-weight:800} .tam .lnk{border:0;background:none;padding:0;color:var(--link);font:700 12px Poppins;cursor:pointer}
.tam .tamed{display:inline-flex;align-items:center;gap:6px;flex-wrap:wrap;background:#fff;border:1px solid var(--line);border-radius:10px;padding:5px 8px}
.tam .tamed[hidden]{display:none}
.tam select,.tam input{font:600 12px Poppins;border:1px solid var(--line);border-radius:6px;padding:3px 6px} .tam select{width:auto;max-width:100%} .tam input{width:72px}
.tam input.bad{border-color:var(--rojo);background:#fdecef;color:var(--rojo)} .tam .tammsg{flex-basis:100%;color:var(--rojo);font-weight:700;font-size:11.5px} .tam .tammsg:empty{display:none}
.fmt .pvac{font-size:10.5px;color:var(--rojo);font-weight:700;margin:-2px 0 4px;line-height:1.3}
.fmt .encp{font-size:10.5px;color:var(--muted);font-weight:600;display:flex;align-items:center;justify-content:center;gap:4px;margin-top:4px} .fmt .encp input{width:80px;margin:0}
</style>
</head>
<body>
<header>
  <div class="top"><img id="lockup" alt="Córdoba · Gobierno de la Provincia · Hacer para crecer"><div class="ttl"><h1>GENERADOR DE CONTENIDO</h1><div class="sub" id="sub"></div></div><nav class="mods" aria-label="Tipo de contenido"><a href="index.html" class="on" aria-current="page">Obras</a><a href="anuncios.html">Anuncios</a></nav></div>
  <div class="cinta"></div>
  <div class="vista" id="vista" role="tablist"></div>
</header>
<div class="wrap"><div class="perbar" id="per"></div><aside id="side"></aside><main><div class="ctx" id="ctx"></div><div id="main"></div></main></div>
<footer><img id="lockup2" alt="Córdoba · Gobierno de la Provincia · Hacer para crecer"><p>Comunicación · Municipalidad de Córdoba · uso interno</p></footer>
<script>const DATA=/*__DATA__*/null;</script>
<script>
(()=>{
const CONT=DATA.contenido||{};
const P=DATA.parte, CIRC=DATA.circuitos, A=DATA.assets, FISCAL=(DATA.fiscal&&DATA.fiscal.cifras)||[];
const GAL=A.galeria||{}, RUBRO_TXT=A.rubros_texto||{};   // galería de fotos genéricas por rubro (viene del build, assets/galeria/<rubro>/)
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
/* seccional = el número del código de circuito (7A, 7B y 7G son la seccional 7). Dato interno: sirve para agrupar y filtrar, nunca se publica. */
const secc=c=>{const m=String(c||'').match(/^\d+/);return m?m[0]:'?'};
const ordSecc=(a,b)=>(parseInt(a)||99)-(parseInt(b)||99)||String(a).localeCompare(String(b));
const enriquecer=o=>{
  const t=TIPOS[o.tipo], c=CIRC[o.circuito]||null, m=o.metricas||{};
  const fotos=(A.fotos[o.doc]||[]), doc=(A.docs[o.doc]||null), ali=s=>s&&(ALIAS[s]||s);
  const rawB=o.barrio||((o.tipo==='mant'||o.tipo==='pav')?o.sector:null);   // los barrios que el parte une con barra se nombran por separado
  const barrioList=rawB?rawB.split('/').map(s=>ali(s.trim())):null;
  return {...o,barrioList,via:sinBarras(o.via),entre:sinBarras(o.entre),sector:ali(sinBarras(o.sector)),barrio:ali(sinBarras(o.barrio)),eje:t.eje,circNombre:c,m,fotos,docTxt:doc,driveUrl:m.driveUrl,secc:secc(o.circuito)};
};
const obras=P.obras.map(enriquecer);
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
/* ---------- SMS: un solo mensaje (160 caracteres), con un link corto al final ----------
   Estructura: apertura según alcance + qué se hace y dónde + "Más info: [link]". El marcador [link] se cuenta como un link corto de LINK_LEN caracteres.
   Apertura: "tu barrio" si la obra tiene barrio; "tu sector" si no lo tiene (rampas) o si es el resumen de una zona; "tu ciudad" para la ciudad entera o una localidad. */
const SMS_MAX=160, LINK_LEN=22, LINK='[link]';
const smsLen=t=>String(t).replace(/\[link\]/g,'x'.repeat(LINK_LEN)).length;
const sinTildes=t=>String(t).replace(/[áéíóúÁÉÍÓÚ]/g,c=>({á:'a',é:'e',í:'i',ó:'o',ú:'u',Á:'A',É:'E',Í:'I',Ó:'O',Ú:'U'}[c]));
const SMS_AP={barrio:['Obras en tu barrio: ','Hacer para Crecer en tu barrio: ','Tu barrio avanza: '],sector:['Obras en tu sector: ','Hacer para Crecer en tu sector: ','Tu sector avanza: '],ciudad:['Obras en tu ciudad: ','Hacer para Crecer en tu ciudad: ','Tu ciudad avanza: ']};
const smsArmar=(alcance,cuerpos,key,apsFijas)=>{ // del cuerpo más completo al más corto, y de la apertura elegida a las más cortas: nunca se corta una frase
  const aps=apsFijas||SMS_AP[alcance]||SMS_AP.ciudad, ap0=aps[hash(key+'s')%aps.length], aps2=[ap0,...aps.filter(a=>a!==ap0)].sort((a,b)=>a===ap0?-1:b===ap0?1:a.length-b.length);
  const c=[];for(const b of cuerpos.filter(Boolean))for(const a of aps2)c.push(`${a}${b}. Más info: ${LINK}`);
  for(const b of cuerpos.filter(Boolean))c.push(`${b}. Más info: ${LINK}`);
  return c.find(x=>smsLen(x)<=SMS_MAX)||c.at(-1);
};
function textoSMS(o){
  const m=o.m,B=BAR(o),en=B?` en ${B}`:'',r=o.rampas,rr=r===1?'rampa':'rampas';
  // cuerpos sin verbo (la apertura ya dice que es una obra), del más completo al más corto; "sinB" va sin barrio, para la variante que abre con el nombre del barrio
  let largo,corto,sinB;
  switch(o.tipo){
    case 'rampas': largo=o.grupo?`${r} rampas de accesibilidad en ${esq(o)} esquinas de ${o.circuito==='1'?'la zona céntrica':'la Av. J. M. de Pueyrredón'}`:`${r} ${rr} de accesibilidad en ${lugarRampas(o)}`;corto=o.grupo?`${r} rampas en ${o.circuito==='1'?'la zona céntrica':'la Av. Pueyrredón'}`:`${r} ${rr} en ${o.via}`;break;
    case 'plaza': largo=`renovación integral de la ${o.via}${en}`;corto=`renovación de la ${o.via}${en}`;sinB=`renovación integral de la ${o.via}`;break;
    case 'mant': largo=`mantenimiento de calles de tierra${m.ml?` (${nf(m.ml)} metros lineales)`:''}${en}`;corto=`mantenimiento de calles${en}`;sinB=`mantenimiento de calles de tierra${m.ml?` (${nf(m.ml)} metros lineales)`:''}`;break;
    case 'frio': largo=`bacheo en frío${m.nocturno?' en horario nocturno':''}${en}`;corto=`bacheo en frío${en}`;sinB=`bacheo en frío${m.nocturno?' en horario nocturno':''}`;break;
    case 'bacheo': largo=`bacheo con asfalto sobre ${o.via}${m.m2?` (${nf(m.m2)} m²)`:''}${en}`;corto=`bacheo con asfalto en ${o.via}${en}`;sinB=`bacheo con asfalto sobre ${o.via}${m.m2?` (${nf(m.m2)} m²)`:''}`;break;
    case 'rehab': largo=`rehabilitación con asfalto sobre ${o.via}${m.ml?` (${nf(m.ml)} metros)`:''}${en}`;corto=`rehabilitación de ${o.via}${en}`;sinB=`rehabilitación con asfalto sobre ${o.via}${m.ml?` (${nf(m.ml)} metros)`:''}`;break;
    case 'hormigon': largo=`rehabilitación con hormigón sobre ${o.via}${m.m2?` (${nf(m.m2)} m²)`:''}${en}`;corto=`rehabilitación con hormigón en ${o.via}${en}`;sinB=`rehabilitación con hormigón sobre ${o.via}${m.m2?` (${nf(m.m2)} m²)`:''}`;break;
    case 'pav': largo=`pavimentación de ${m.cuadras} cuadras${en}`;corto=largo;sinB=`pavimentación de ${m.cuadras} cuadras`;break;
  }
  if(o.tipo!=='rampas'&&B&&hash((o.id||'')+'sb')%4===3)return smsArmar('barrio',[sinB,sinB&&sinB.replace(/ \(.*?\)/,'')],o.id||'',[`${B}: `]);   // una de cada cuatro abre con el nombre del barrio
  const alcance=o.tipo==='rampas'?'sector':(B?'barrio':'sector');
  return smsArmar(alcance,[largo,corto,corto&&corto.replace(/ en Barrio .*$/,'')],o.id||'');
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
    if(c.titulos)x.titulos=c.titulos.map(limpio);if(c.ig)x.ig=limpio(c.ig);if(c.x)x.x=limpio(c.x);if(c.gac)x.gac=limpio(c.gac);if(c.sms)x.sms=limpio(c.sms);if(c.placa)Object.assign(x.placa,c.placa);x.redactado=true;});
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
function layout(g,blocks,maxW,availH,fitW=false){   // fitW: además, ninguna palabra puede pasar del ancho (placas anchas)
  blocks=blocks.filter(b=>b.t!=null&&b.t!=='');let k=1;if(!blocks.length)return {L:[],tot:0,k};   // sin texto (por ejemplo, sin subtítulo)
  for(let it=0;it<(fitW?24:14);it++){
    let tot=0,ancho=true;const L=blocks.map(b=>{g.font=`${b.w} ${b.s*k}px Poppins`;const lines=wrap(g,b.up?up(b.t):b.t,maxW);if(fitW&&lines.some(l=>g.measureText(l).width>maxW))ancho=false;const lh=b.s*k*(b.lh||1.12);tot+=lines.length*lh+(b.gap||0)*k;return {b,lines,lh,s:b.s*k}});
    if((tot-(blocks.at(-1).gap||0)*k<=availH&&ancho)||it===(fitW?23:13))return {L,tot,k};k*=.93;
  }
}
function drawLayout(g,lay,x,y,align,maxW){
  let cy=y;
  for(const {b,lines,lh,s} of lay.L){g.font=`${b.w} ${s}px Poppins`;g.fillStyle=b.c;g.globalAlpha=b.op??1;g.textAlign=align;g.textBaseline='alphabetic';
    for(const ln of lines){g.fillText(ln,align==='center'?x+maxW/2:x,cy+s*.92);cy+=lh}
    cy+=(b.gap||0)*lay.k;}
  g.globalAlpha=1;
}
function cover(g,img,x,y,w,h,enc){ // recorte "cover"; enc = encuadre elegido a mano: fx, fy (0 a 1, qué parte de la foto se ve) y z (zoom)
  const e={fx:(enc&&enc.fx)??.5,fy:(enc&&enc.fy)??.5,z:(enc&&enc.z)||1},r=Math.max(w/img.naturalWidth,h/img.naturalHeight)*e.z,dw=img.naturalWidth*r,dh=img.naturalHeight*r;
  g.save();g.beginPath();g.rect(x,y,w,h);g.clip();g.drawImage(img,x-(dw-w)*e.fx,y-(dh-h)*e.fy,dw,dh);g.restore()}   // con zoom menor a 1 la foto no cubre el recuadro y se ve el fondo alrededor
function rrect(g,x,y,w,h,r){g.beginPath();g.moveTo(x+r,y);g.arcTo(x+w,y,x+w,y+h,r);g.arcTo(x+w,y+h,x,y+h,r);g.arcTo(x,y+h,x,y,r);g.arcTo(x,y,x+w,y,r);g.closePath()}

async function footer(g,W,H,e,story,eje,solo){
  const u=Math.min(W,H), land=W>H, fh=u*.17, y1=story?H*.885:H, y0=y1-fh;   // u: unidad base (en vertical y cuadrado es el ancho, así que nada cambia)  // stories: logos más abajo (queda ~11% libre abajo, cerca del mínimo que recomienda Meta)
  if(!solo){g.fillStyle=e.pie;g.fillRect(0,y0,W,H-y0);}
  const asp=await aspect(e.logos);
  let lx,lw;
  if(eje==='accesible'&&!solo){const ca=await aspect('cinta-pie-accesible');const cw=fh*ca;await drawSvg(g,'cinta-pie-accesible',0,y0,cw,fh);lx=cw+u*.03;lw=W-lx-u*.05;
    if(land){const l2=Math.min(lw,u*.92-cw);lx+=(lw-l2)/2;lw=l2}}   // apaisado: los logos miden lo mismo que en el cuadrado y van centrados en la franja
  else{lw=u*(eje==='plaza'?.90:.84);lx=(W-lw)/2;}
  const lh=lw/asp, ly=y0+(fh-lh)/2;
  await drawSvg(g,e.logos,lx,ly,lw,lh);
  return y0;
}
const TEMA={calle:{bg:'#17233d',panel:'#bedff7',ink:'#17233d',acc:'#bc1734',blk:'#bc1734',band:'#bc1734'},
  accesible:{bg:'#eaab3b',panel:'#bedff7',ink:'#09467f',acc:'#09467f',blk:'#e8d7b0',band:'#ffffff'},
  plaza:{bg:'#c6dfce',panel:'#ffffff',ink:'#09467f',acc:'#2f7a52',blk:'#ffffff',band:'#4da070'}};
function geo(W,H,y0,eje){const u=Math.min(W,H),story=H>W*1.6,sh=eje==='plaza'?W*297/6917:0;
  const panelH=Math.round(y0*(story?.2:.25)),panelB=y0-sh-u*(eje==='plaza'?.02:story?.05:.035);return {story,sh,panelH,panelB,panelT:panelB-panelH}}
async function bloqueEje(g,W,e,T,x0,y,alignRight,u=W){ // bloque con el logotipo del eje, pegado al borde como en los carteles
  const wa=await aspect(e.wm),ww=u*.30,wh=ww/wa,pad=u*.035,bw=ww+pad*2,bh=wh+pad*2,x=alignRight?W-bw:0;
  g.fillStyle=T.blk;g.fillRect(x,y,bw,bh);await drawSvg(g,e.wm,x+pad,y+pad,ww,wh);return y+bh}
function panelDatos(g,W,v,T,gm,u=W,rect=null){ // rect = [x, ancho] del panel (apaisado); sin rect, el panel a lo ancho de siempre
  const {panelT,panelH}=gm,px=rect?rect[0]:W*.05,pw=rect?rect[1]:W*.9,ip=u*.035,z=rect?1.3:1;   // z: en apaisado el panel es más grande y la letra también
  g.save();g.shadowColor='#0003';g.shadowBlur=u*.02;g.shadowOffsetY=u*.006;g.fillStyle=T.panel;rrect(g,px,panelT,pw,panelH,u*.022);g.fill();g.restore();
  if(rect&&(v.valor?pw<u*.95:true)){   // panel angosto de apaisado: el número arriba y las etiquetas debajo, todo dentro del panel
    const lay=layout(g,[{t:v.valor||'',w:800,s:u*.16,c:T.ink,lh:1,gap:u*.015},{t:v.valor?v.etiqueta:v.main,w:800,s:u*z*(v.valor?.043:.06),c:v.valor?T.acc:T.ink,up:true,lh:1.08,gap:u*.012},{t:v.sub||'',w:600,s:u*z*.036,c:'#17233d',lh:1.15,gap:u*.008},{t:v.extra||'',w:600,s:u*z*.026,c:'#17233d',op:.7}],pw-ip*2,panelH-ip*1.5,true);
    drawLayout(g,lay,px+ip,panelT+(panelH-lay.tot)/2,'left',pw-ip*2);
  } else if(v.valor){
    let s=Math.min(panelH*.62,u*.2);g.font=`800 ${s}px Poppins`;while(g.measureText(v.valor).width>(rect?pw/3:W*.30)&&s>10){s*=.94;g.font=`800 ${s}px Poppins`}
    const vw=g.measureText(v.valor).width;g.fillStyle=T.ink;g.textAlign='left';g.textBaseline='alphabetic';g.fillText(v.valor,px+ip,panelT+panelH/2+s*.36);
    const rx=px+ip+vw+u*.03,rw=px+pw-ip-rx;
    const lay=layout(g,[{t:v.etiqueta,w:800,s:u*z*.043,c:T.acc,up:true,lh:1.08,gap:u*.01},{t:v.sub||'',w:600,s:u*z*.034,c:'#17233d',lh:1.15,gap:u*.008},{t:v.extra||'',w:600,s:u*z*.026,c:'#17233d',op:.7}],rw,panelH-ip);
    drawLayout(g,lay,rx,panelT+(panelH-lay.tot)/2,'left',rw);
  } else {
    const lay=layout(g,[{t:v.main,w:800,s:u*z*.06,c:T.ink,up:true,lh:1.08,gap:u*.012},{t:v.sub||'',w:600,s:u*z*.036,c:'#17233d',lh:1.15,gap:u*.008},{t:v.extra||'',w:600,s:u*z*.026,c:'#17233d',op:.7}],pw-ip*2,panelH-ip);
    drawLayout(g,lay,px+ip,panelT+(panelH-lay.tot)/2,'left',pw-ip*2);
  }
}
/* aro del eje alrededor de la foto en círculo (el mismo en todas las formas) */
function aroCirculo(g,eje,cx,cy,r,ring,u){
  if(eje==='calle'){
    g.fillStyle='#bc1734';g.beginPath();g.arc(cx,cy,r+ring,0,7);g.fill();
    g.strokeStyle='#bedff7';g.lineWidth=ring*.62;g.beginPath();g.arc(cx,cy,r+ring*.5,0,7);g.stroke();
    g.strokeStyle='#17233d';g.lineWidth=u*.0065;g.setLineDash([u*.03,u*.024]);g.beginPath();g.arc(cx,cy,r+ring*.5,0,7);g.stroke();g.setLineDash([]);
  } else if(eje==='accesible'){
    g.fillStyle='#fff';g.beginPath();g.arc(cx,cy,r+ring*.55,0,7);g.fill();
    g.strokeStyle='#17233d';g.lineWidth=u*.012;g.beginPath();g.arc(cx,cy,r+ring*.55,0,7);g.stroke();
  } else {
    g.fillStyle='#89ba96';g.beginPath();g.arc(cx,cy,r+ring*.8,0,7);g.fill();
    g.fillStyle='#4da070';g.beginPath();g.arc(cx,cy,r+ring*.35,0,7);g.fill();
  }
}
/* Diseño A: foto en círculo con aro del eje */
async function photoCirculo(g,W,H,v,e,y0,topSafe,im){
  const eje=v.eje,T=TEMA[eje],gm=geo(W,H,y0,eje),{story,sh,panelT}=gm,u=Math.min(W,H);
  g.fillStyle=T.bg;g.fillRect(0,0,W,conPie(v)?y0:H);
  if(eje==='accesible')await drawCrop(g,'fondo-accesible',[0,0,1415,483],0,0,u*.5,u*.5*483/1415);
  if(eje==='plaza')await drawCrop(g,'fondo-plaza',[150,220,560,520],u*.04,topSafe+u*.03,u*.1,u*.1*520/560);
  const cTop=story?H*.115:topSafe+u*.03, ring=u*.085;
  const r0=(panelT+u*.07-cTop)/2-ring; let r=r0; r=Math.min(r,u*.385);r=Math.max(r,u*.2);
  const cx=W/2, cy=cTop+ring+r+(H>W*16/9&&r0>r?r0-r:0);   // historias más altas que 9:16: el círculo baja al centro del espacio que sobra
  aroCirculo(g,eje,cx,cy,r,ring,u);
  g.save();g.beginPath();g.arc(cx,cy,r,0,7);g.clip();cover(g,im,cx-r,cy-r,2*r,2*r,v._enc);g.restore();
  if(conPie(v))await bloqueEje(g,W,e,T,0,topSafe,true,u);
  panelDatos(g,W,v,T,gm,u);
  if(eje==='plaza')await drawCrop(g,'fondo-plaza',[28,2475,6917,297],0,y0-sh,W,sh);
}
/* Diseño B: foto a sangre arriba con corte diagonal y banda de color */
async function photoMarco(g,W,H,v,e,y0,topSafe,im){
  const eje=v.eje,T=TEMA[eje],gm=geo(W,H,y0,eje),{sh,panelT}=gm,u=Math.min(W,H);
  g.fillStyle=T.bg;g.fillRect(0,0,W,conPie(v)?y0:H);
  const pb=panelT+u*.05,sl=u*.09,bd=u*.022;
  g.fillStyle=T.band;g.beginPath();g.moveTo(0,0);g.lineTo(W,0);g.lineTo(W,pb+bd);g.lineTo(0,pb+sl+bd);g.closePath();g.fill();
  g.save();g.beginPath();g.moveTo(0,0);g.lineTo(W,0);g.lineTo(W,pb);g.lineTo(0,pb+sl);g.closePath();g.clip();cover(g,im,0,0,W,pb+sl,v._enc);g.restore();
  if(conPie(v))await bloqueEje(g,W,e,T,0,topSafe,false,u);
  panelDatos(g,W,v,T,gm,u);
  if(eje==='plaza')await drawCrop(g,'fondo-plaza',[28,2475,6917,297],0,y0-sh,W,sh);
}
/* wordmark del eje en una ficha redondeada (Foto completa) y bloques de texto en blanco sobre la foto */
async function chipEje(g,e,cx,cy,u){const wa=await aspect(e.wm), cw=u*.36, ch=cw/wa, pad=u*.025;
  g.fillStyle=e.chip;rrect(g,cx,cy,cw+pad*2,ch+pad*2,u*.02);g.fill();await drawSvg(g,e.wm,cx+pad,cy+pad,cw,ch);return cy+ch+pad*2}
function bloquesCompleta(v,e,u){
  const bl=[{t:v.kicker,w:600,s:u*.032,c:e.acento,up:true,gap:u*.012}];
  if(v.valor)bl.push({t:`${v.valor} ${v.etiqueta}`,w:800,s:u*.085,c:'#fff',lh:1.05,gap:u*.02});else bl.push({t:v.main,w:800,s:u*.085,c:'#fff',lh:1.05,gap:u*.02});
  if(v.sub)bl.push({t:v.sub,w:600,s:u*.04,c:'#fff',gap:u*.012});if(v.extra)bl.push({t:v.extra,w:600,s:u*.03,c:'#fff',op:.8});return bl}
/* Diseño C: foto completa con degradado y texto encima */
async function photoCompleta(g,W,H,v,e,y0,topSafe,im){
  const story=H>W*1.6, u=Math.min(W,H), fullH=story?H:y0, ytxt=story&&conPie(v)?H*.885-u*.17-u*.015:y0;   // sin pie, el degradado y el texto bajan hasta y0  // stories: la foto cubre todo el lienzo (sin azul liso abajo) y los logos van sobre el degradado
  cover(g,im,0,0,W,fullH,v._enc);
  const gr=g.createLinearGradient(0,fullH*.3,0,fullH);const col=e.dark;
  gr.addColorStop(0,col+'00');gr.addColorStop(.5,col+'b0');gr.addColorStop(1,col+'f5');g.fillStyle=gr;g.fillRect(0,fullH*.3,W,fullH*.7);
  if(conPie(v))await chipEje(g,e,u*.05,topSafe+u*.04,u);
  const bm=u*.06, mw=W-bm*2, bl=bloquesCompleta(v,e,u);
  const lay=layout(g,bl,mw,ytxt*.55);drawLayout(g,lay,bm,ytxt-u*.04-lay.tot+(bl.at(-1).gap||0),'left',mw);
  return story?'full':undefined;
}
const ESTILOS={circulo:photoCirculo,marco:photoMarco,completa:photoCompleta};
async function photoPlate(g,W,H,v,e,y0,topSafe,fotoIdx,estilo){
  const im=await loadImg(v.fotos[fotoIdx%v.fotos.length]);
  const k=(estilo&&estilo!=='sugerido')?estilo:window.__estiloSugerido(v,im,esGen(v,fotoIdx),formaDe(W,H));
  return await ESTILOS[k](g,W,H,v,e,y0,topSafe,im);
}
const bloquesMarca=(v,u,col1,col2,col3)=>{const b=[];   // texto de la placa sin foto: número grande o título, etiqueta, subtítulo y dato extra
    if(v.valor){b.push({t:v.valor,w:800,s:u*.26,c:col1,lh:1,gap:u*.01});b.push({t:v.etiqueta,w:800,s:u*.052,c:col2,up:true,gap:u*.025});}
    else b.push({t:v.main,w:800,s:u*.085,c:col1,up:true,lh:1.08,gap:u*.025});
    if(v.sub)b.push({t:v.sub,w:600,s:u*.042,c:col3,gap:u*.012});
    if(v.extra)b.push({t:v.extra,w:600,s:u*.032,c:col3,op:.75});return b;};
async function textoAccesible(g,v,u,x,top,mw,hh,align,W){   // centrado: la píldora va al centro del lienzo (W), como siempre
    const b=[];
    if(v.valor)b.push({t:v.valor,w:800,s:u*.27,c:'#09467f',lh:1,gap:u*.012});else b.push({t:v.main,w:800,s:u*.085,c:'#09467f',up:true,gap:u*.02});
    const lay0=layout(g,b,mw,hh*.62,align==='left');
    const pillH=v.valor?u*.1:0;const rest=[];if(v.sub)rest.push({t:v.sub,w:600,s:u*.04,c:'#17233d',gap:u*.01});if(v.extra)rest.push({t:v.extra,w:600,s:u*.03,c:'#17233d',op:.75});
    const lay1=layout(g,rest,mw,hh-lay0.tot-pillH-u*.03,align==='left');
    const tot=lay0.tot+(v.valor?pillH+u*.025:0)+lay1.tot;let y=top+Math.max(0,(hh-tot)/2);
    drawLayout(g,lay0,x,y,align,mw);y+=lay0.tot;
    if(v.valor){g.font=`600 ${u*.05}px Poppins`;const tw=Math.min(mw,g.measureText(v.etiqueta).width+u*.1),px=align==='center'?(W-tw)/2:x;g.fillStyle='#bedff7';rrect(g,px,y,tw,pillH,u*.012);g.fill();g.fillStyle='#09467f';g.textAlign='center';g.fillText(v.etiqueta,align==='center'?W/2:px+tw/2,y+pillH*.68);y+=pillH+u*.025;}
    drawLayout(g,lay1,x,y,align,mw);}
async function brandPlate(g,W,H,v,e,y0,topSafe,eje){
  const u=Math.min(W,H),bm=u*.07,mw=W-bm*2;
  const blocks=(col1,col2,col3)=>bloquesMarca(v,u,col1,col2,col3);
  if(eje==='calle'){
    const wm=conPie(v),wa=await aspect(e.wm),ww=u*.36,wh=ww/wa,arcW=u*.42,arcH=arcW*520/1445;
    const bh=wm?topSafe+u*.045+wh+arcH+u*.025:topSafe+u*.03+arcH;   // sin marcas: la banda queda solo con el arco y el título sube
    g.fillStyle='#fff';g.fillRect(0,0,W,y0);g.fillStyle=e.dark;g.fillRect(0,0,W,bh);
    await drawCrop(g,'fondo-calle',[3713,0,1956,680],W*.58+(W-u)*.42,bh,u*.42,u*.42*680/1956);
    await drawCrop(g,'fondo-calle',[0,1729,1445,520],0,bh-arcH,arcW,arcH);
    if(wm)await drawSvg(g,e.wm,bm,topSafe+u*.045,ww,wh);
    const top=bh+u*.05, lay=layout(g,blocks('#17233d','#bd1635','#17233d'),mw,y0-top-u*.04);
    drawLayout(g,lay,bm,top+(y0-top-u*.04-lay.tot)/2,'left',mw);
  } else if(eje==='accesible'){
    const wm=conPie(v),wa=await aspect(e.wm),ww=u*.60,wh=ww/wa;
    g.fillStyle='#fff';g.fillRect(0,0,W,y0);
    let yh;
    if(wm){yh=topSafe>0?2*topSafe+wh:Math.max(u*1408/2835,wh+u*.09);const sc=yh/1408,iw=2835*sc; // stories: bloque simétrico, el logotipo queda centrado y fuera de la zona segura
      g.save();g.beginPath();g.rect(0,0,W,yh);g.clip();await drawCrop(g,'fondo-accesible',[0,0,2835,1408],(W-Math.max(iw,W))/2,0,Math.max(iw,W),yh);g.restore();
      await drawSvg(g,e.wm,(W-ww)/2,(yh-wh)/2,ww,wh);}
    else{yh=topSafe+u*.2;const fh=W*1408/2835;   // sin marcas: una banda baja con el borde rayado (sin deformar el fondo) y el número sube
      g.save();g.beginPath();g.rect(0,0,W,yh);g.clip();await drawCrop(g,'fondo-accesible',[0,0,2835,1408],0,Math.min(0,yh-fh),W,fh);g.restore();}
    const top=yh+u*.03,hh=y0-top-u*.03;
    await textoAccesible(g,v,u,bm,top,mw,hh,'center',W);
  } else {
    const wm=conPie(v),wa=await aspect(e.wm),ww=u*.50,wh=ww/wa,gh=wm?topSafe+wh+u*.09:topSafe+u*.16,sh=W*297/6917;   // sin marcas: banda baja, el título sube
    g.fillStyle='#fff';g.fillRect(0,0,W,y0);
    await drawCrop(g,'fondo-plaza',[5900,28,1000,700],W*.60+(W-u)*.40,gh+u*.005,u*.40,u*.40*700/1000);
    g.fillStyle='#c6dfce';g.fillRect(0,0,W,gh);
    await drawCrop(g,'fondo-plaza',[150,220,560,520],W*.87+(W-u)*.13,topSafe+u*.03,u*.10,u*.10*520/560);
    if(wm){await drawCrop(g,'fondo-plaza',[1440,2120,580,350],W*.74+(W-u)*.26,gh-u*.17,u*.19,u*.19*350/580);
    await drawSvg(g,e.wm,bm,topSafe+u*.075,ww,wh);}
    else await drawCrop(g,'fondo-plaza',[1440,2120,580,350],W*.70+(W-u)*.30,topSafe+u*.035,u*.15,u*.15*350/580);   // el banco se achica para entrar en la banda baja
    await drawCrop(g,'fondo-plaza',[28,2475,6917,297],0,y0-sh,W,sh);
    const top=gh+u*.05,hh=y0-sh-top-u*.03;
    const lay=layout(g,blocks('#09467f','#4da070','#17233d'),mw,hh);drawLayout(g,lay,bm,top+(hh-lay.tot)/2,'left',mw);
  }
}
/* ---------- placas anchas: apaisado (W/H de 1,25 a 2,2) y banner (W/H de 2,2 a 3,2). Todo se mide en u = min(W,H), que acá es el alto ---------- */
// forma de la placa según la proporción: vertical (historia, H > 1,6 W, como siempre), cuadrado (de ahí a W/H < 1,25), apaisado y banner
const formaDe=(W,H)=>H>W*1.6?'vertical':W<H*1.25?'cuadrado':W<=H*2.2?'apaisado':'banner';
const pastoPlaza=(W,u)=>Math.min(W*297/6917,u*.08);   // franja de pasto de plaza: a lo ancho, sin pasar del 8 % del alto
// fondo blanco con la columna del eje a la izquierda y su gráfica, como en los carteles apaisados de cada programa.
// Devuelve el alto que ocupa la gráfica de arriba a la derecha (el texto queda debajo) y el alto del pasto de plaza.
async function columnaEje(g,W,A,v,e,colW,wm,u,banner){
  const eje=v.eje;let libre=0,sh=0;g.fillStyle='#fff';g.fillRect(0,0,W,A);
  if(eje==='calle'){
    g.fillStyle=e.dark;g.fillRect(0,0,colW,A);
    const aw=colW*.88,ah=Math.min(aw*520/1445,A*.32);await drawCrop(g,'fondo-calle',[0,1729,1445,520],0,A-ah,ah*1445/520,ah);
    const tw=Math.min(A*(banner?.62:.55),W*.3),th=tw*680/1956;await drawCrop(g,'fondo-calle',[3713,0,1956,680],W-tw,0,tw,th);libre=th;
    if(wm){const wa=await aspect(e.wm);let ww=colW*.7,wh=ww/wa;if(wh>(A-ah)*.6){wh=(A-ah)*.6;ww=wh*wa}await drawSvg(g,e.wm,(colW-ww)/2,(A-ah-wh)/2,ww,wh)}
  } else if(eje==='accesible'){
    g.fillStyle='#eaab3b';g.fillRect(0,0,colW,A);
    const t1=colW,t1h=Math.min(t1*485/1414,A*.3);await drawCrop(g,'fondo-accesible',[0,0,1414,485],0,0,t1h*1414/485,t1h);
    const t2=colW*.8,t2h=Math.min(t2*372/1126,A*.25),t2w=t2h*1126/372;await drawCrop(g,'fondo-accesible',[1709,1034,1126,372],colW-t2w,A-t2h,t2w,t2h);
    if(wm){const wa=await aspect(e.wm);let ww=colW*.78,wh=ww/wa;if(wh>A*.4){wh=A*.4;ww=wh*wa}await drawSvg(g,e.wm,(colW-ww)/2,(A-wh)/2,ww,wh)}
  } else {
    sh=pastoPlaza(W,u);g.fillStyle='#c6dfce';g.fillRect(0,0,colW,A);
    await drawCrop(g,'fondo-plaza',[150,220,560,520],colW*.08,A*.07,u*.1,u*.1*520/560);
    const fw=Math.min(A*.32,W*.2);await drawCrop(g,'fondo-plaza',[5900,28,1000,700],W-fw*1.08,0,fw,fw*.7);libre=fw*.7;
    const bw=Math.min(colW*.3,u*.19);await drawCrop(g,'fondo-plaza',[1440,2120,580,350],colW-bw*1.25,A-sh-bw*350/580,bw,bw*350/580);
    await drawCrop(g,'fondo-plaza',[28,2475,6917,297],0,A-sh,W,sh);
    if(wm){const wa=await aspect(e.wm);let ww=colW*.74,wh=ww/wa;if(wh>A*.4){wh=A*.4;ww=wh*wa}await drawSvg(g,e.wm,(colW-ww)/2,(A-sh-wh)/2-A*.04,ww,wh)}
  }
  return {libre,sh};
}
const TINTAS={calle:['#17233d','#bd1635','#17233d'],plaza:['#09467f','#4da070','#17233d'],accesible:['#09467f','#09467f','#17233d']};
// texto sin foto en un recuadro (x, y, ancho, alto): centrado en vertical y alineado a la izquierda
async function textoMarca(g,v,u,x,y,w,h,W){
  if(v.eje==='accesible')return textoAccesible(g,v,u,x,y,w,h,'left',W);
  const lay=layout(g,bloquesMarca(v,u,...TINTAS[v.eje]),w,h,true);drawLayout(g,lay,x,y+Math.max(0,(h-lay.tot)/2),'left',w);}
// apaisado sin foto: columna del eje con el wordmark, texto en el blanco y pie a lo ancho
async function anchaMarca(g,W,H,v,e,u,A){
  const pie=conPie(v),colW=pie?Math.min(A*.62,W*.34):Math.min(A*.3,W*.16);   // sin marcas, la columna queda como una franja de color
  const {libre,sh}=await columnaEje(g,W,A,v,e,colW,pie,u,false);
  const x0=colW+u*.08,x1=W-u*.08,top=Math.max(u*.06,libre*.9),bot=A-sh-u*.06;
  await textoMarca(g,v,u,x0,top,x1-x0,bot-top,W);}
// apaisado con círculo: foto en círculo en el tercio izquierdo, panel de datos en los dos tercios derechos
async function anchaCirculo(g,W,H,v,e,u,A,im){
  const eje=v.eje,T=TEMA[eje],pie=conPie(v),sh=eje==='plaza'?pastoPlaza(W,u):0;
  g.fillStyle=T.bg;g.fillRect(0,0,W,A);
  if(eje==='accesible')await drawCrop(g,'fondo-accesible',[0,0,1415,483],0,0,u*.5,u*.5*483/1415);
  if(eje==='plaza')await drawCrop(g,'fondo-plaza',[150,220,560,520],u*.04,u*.03,u*.1,u*.1*520/560);
  const ring=u*.06,r=Math.min(u*.36,(A-sh)/2-ring-u*.04,W*.19),cx=Math.max(W/6,r+ring+u*.07),cy=(A-sh)/2;   // diámetro u*0,72 (menos si con el pie no entra)
  aroCirculo(g,eje,cx,cy,r,ring,u);
  g.save();g.beginPath();g.arc(cx,cy,r,0,7);g.clip();cover(g,im,cx-r,cy-r,2*r,2*r,v._enc);g.restore();
  const xL=Math.max(W/3,cx+r+ring+u*.07),xR=W-u*.05,bEnd=pie?await bloqueEje(g,W,e,T,0,0,true,u):0;
  const top=bEnd+u*.05,bot=A-sh-u*.06,ph=Math.min(bot-top,u*.55);
  panelDatos(g,W,v,T,{panelT:top+(bot-top-ph)/2,panelH:ph},u,[xL,xR-xL]);
  if(eje==='plaza')await drawCrop(g,'fondo-plaza',[28,2475,6917,297],0,A-sh,W,sh);}
// apaisado con marco: foto a sangre en el 45 % izquierdo, corte diagonal vertical con la banda del eje y panel a la derecha
async function anchaMarco(g,W,H,v,e,u,A,im){
  const eje=v.eje,T=TEMA[eje],pie=conPie(v),sh=eje==='plaza'?pastoPlaza(W,u):0,xb=W*.45,sl=u*.09,bd=u*.022,xt=xb+sl;
  g.fillStyle=T.bg;g.fillRect(0,0,W,A);
  g.fillStyle=T.band;g.beginPath();g.moveTo(0,0);g.lineTo(xt+bd,0);g.lineTo(xb+bd,A);g.lineTo(0,A);g.closePath();g.fill();
  g.save();g.beginPath();g.moveTo(0,0);g.lineTo(xt,0);g.lineTo(xb,A);g.lineTo(0,A);g.closePath();g.clip();cover(g,im,0,0,xt,A,v._enc);g.restore();
  if(pie)await bloqueEje(g,W,e,T,0,0,false,u);
  const xL=xt+bd+u*.06,xR=W-u*.05,top=u*.08,bot=A-sh-u*.08,ph=Math.min(bot-top,u*.55);
  panelDatos(g,W,v,T,{panelT:top+(bot-top-ph)/2,panelH:ph},u,[xL,xR-xL]);
  if(eje==='plaza')await drawCrop(g,'fondo-plaza',[28,2475,6917,297],0,A-sh,W,sh);}
// apaisado con foto completa: foto a sangre, degradado del eje desde abajo y desde la izquierda, texto abajo a la izquierda
async function anchaCompleta(g,W,H,v,e,u,A,im){
  cover(g,im,0,0,W,A,v._enc);const col=e.dark;
  const gb=g.createLinearGradient(0,A*.3,0,A);gb.addColorStop(0,col+'00');gb.addColorStop(.5,col+'90');gb.addColorStop(1,col+'f0');g.fillStyle=gb;g.fillRect(0,A*.3,W,A*.7);
  const gl=g.createLinearGradient(0,0,W*.68,0);gl.addColorStop(0,col+'e0');gl.addColorStop(.55,col+'80');gl.addColorStop(1,col+'00');g.fillStyle=gl;g.fillRect(0,0,W*.68,A);
  const top=conPie(v)?await chipEje(g,e,u*.05,u*.04,u)+u*.04:u*.06;
  const bm=u*.06,mw=Math.min(W*.56,W-bm*2),bl=bloquesCompleta(v,e,u),lay=layout(g,bl,mw,Math.min(A*.62,A-u*.05-top),true);
  drawLayout(g,lay,bm,A-u*.05-lay.tot+(bl.at(-1).gap||0),'left',mw);}
const ANCHOS={circulo:anchaCirculo,marco:anchaMarco,completa:anchaCompleta};
// banner: tira de logos de alto u*0,22 pegada al borde derecho (abajo), en el color del pie del eje
async function tiraLogos(g,W,H,e,u){const asp=await aspect(e.logos),th=u*.22,lh=th*.42,lw=lh*asp,tw=lw+u*.12;
  g.fillStyle=e.pie;g.fillRect(W-tw,H-th,tw,th);await drawSvg(g,e.logos,W-tw+u*.06,H-th+(th-lh)/2,lw,lh);return {tw,th}}
// banner sin foto: columna del eje, título en una o dos líneas, subtítulo a la derecha y la tira de logos
async function bannerMarca(g,W,H,v,e,u){
  const pie=conPie(v),colW=pie?u*.62:u*.3,{libre,sh}=await columnaEje(g,W,H,v,e,colW,pie,u,true);
  const lt=pie?await tiraLogos(g,W,H,e,u):null;
  const x0=colW+u*.07,x1=W-u*.07,top=Math.max(u*.08,libre*.95),bot=H-sh-(lt?lt.th+u*.05:u*.08),hh=bot-top;
  const tw=(x1-x0)*.58,sx=x0+tw+u*.05,sw=x1-sx,[c1,c2,c3]=TINTAS[v.eje];
  if(v.eje==='accesible')await textoAccesible(g,Object.assign({},v,{sub:'',extra:''}),u*1.25,x0,top,tw,hh,'left',W);
  else{const b=v.valor?[{t:v.valor,w:800,s:u*.3,c:c1,lh:1,gap:u*.02},{t:v.etiqueta,w:800,s:u*.075,c:c2,up:true}]:[{t:v.main,w:800,s:u*.14,c:c1,up:true,lh:1.08}];
    const lay=layout(g,b,tw,Math.min(hh,v.valor?u*.6:u*.14*1.08*2.05),true);drawLayout(g,lay,x0,top+Math.max(0,(hh-lay.tot)/2),'left',tw)}   // el título no pasa de dos líneas
  const sb=[{t:v.sub||'',w:600,s:u*.08,c:c3,lh:1.15,gap:u*.02},{t:v.extra||'',w:600,s:u*.06,c:c3,op:.75}];
  if(v.sub||v.extra){const lay=layout(g,sb,sw,hh,true);g.fillStyle=c2;g.fillRect(sx-u*.03,top+Math.max(0,(hh-lay.tot)/2),u*.008,lay.tot);drawLayout(g,lay,sx,top+Math.max(0,(hh-lay.tot)/2),'left',sw)}}
// banner con foto completa: foto a sangre con degradado desde la izquierda, título a la izquierda y logos a la derecha
async function bannerCompleta(g,W,H,v,e,u,im){
  cover(g,im,0,0,W,H,v._enc);const col=e.dark;
  const gl=g.createLinearGradient(0,0,W*.62,0);gl.addColorStop(0,col+'f0');gl.addColorStop(.6,col+'a0');gl.addColorStop(1,col+'00');g.fillStyle=gl;g.fillRect(0,0,W*.62,H);
  const pie=conPie(v),top=pie?await chipEje(g,e,u*.06,u*.07,u)+u*.05:u*.08;
  if(pie)await tiraLogos(g,W,H,e,u);
  const mw=W*.46,bl=[{t:v.valor?`${v.valor} ${v.etiqueta}`:v.main,w:800,s:u*.12,c:'#fff',lh:1.05,gap:u*.02}];if(v.sub)bl.push({t:v.sub,w:600,s:u*.055,c:'#fff'});
  const hh=H-u*.08-top,lay=layout(g,bl,mw,hh,true);drawLayout(g,lay,u*.06,top+Math.max(0,(hh-lay.tot)/2),'left',mw);}
async function placaAncha(g,W,H,v,e,fotoIdx,estilo,forma){
  const u=Math.min(W,H),pie=conPie(v),A=pie&&forma==='apaisado'?H-u*.17:H;   // A: alto útil sobre el pie (el banner no lleva franja)
  let k='sinfoto',im=null;
  if(v.fotos&&v.fotos.length&&estilo!=='sinfoto'){im=await loadImg(v.fotos[fotoIdx%v.fotos.length]);const gen=esGen(v,fotoIdx);
    k=(estilo&&estilo!=='sugerido')?estilo:window.__estiloSugerido(v,im,gen,forma);
    if(forma==='banner'&&k!=='completa'&&k!=='sinfoto')k=window.__estiloSugerido(v,im,gen,'banner');}   // Círculo y Marco no entran en banner
  if(forma==='banner')return k==='completa'?bannerCompleta(g,W,H,v,e,u,im):bannerMarca(g,W,H,v,e,u);
  if(k==='sinfoto')await anchaMarca(g,W,H,v,e,u,A);else await ANCHOS[k](g,W,H,v,e,u,A,im);
  if(pie)await footer(g,W,H,e,false,v.eje,false);
}
async function renderPlaca(canvas,v,fmt,fotoIdx=0,estilo='sugerido'){
  await document.fonts.load('800 40px Poppins');await document.fonts.load('600 40px Poppins');
  const [W,H]=fmtWH(fmt),g=canvas.getContext('2d');canvas.width=W;canvas.height=H;
  // sin pie (conPie(v) falso): no hay franja ni logos y el contenido baja hasta y1 (en historias se mantiene el margen inferior de la zona segura)
  const forma=formaDe(W,H),u=Math.min(W,H),story=forma==='vertical',e=EJES[v.eje],topSafe=story?H*.14:0,y1=story?H*.885:H,y0=conPie(v)?y1-u*.17:y1;
  g.fillStyle='#fff';g.fillRect(0,0,W,H);
  if(forma==='apaisado'||forma==='banner')return placaAncha(g,W,H,v,e,fotoIdx,estilo,forma);
  let full=false;
  if(v.fotos&&v.fotos.length&&estilo!=='sinfoto')full=(await photoPlate(g,W,H,v,e,y0,topSafe,fotoIdx,estilo))==='full';else await brandPlate(g,W,H,v,e,y0,topSafe,v.eje);
  if(conPie(v))await footer(g,W,H,e,story,v.eje,full);
}
/* pie con marcas (franja, logos institucionales, cinta de accesible y wordmark del eje): se apaga por pieza con el tilde "Pie con marcas" (v._pie=false) */
const conPie=v=>v._pie!==false;
function descargar(canvas,nombre){try{canvas.toBlob(b=>{const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=nombre+'.png';document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},500)},'image/png')}catch(e){alert('No se puede bajar esta placa con el tablero abierto como archivo local: el navegador bloquea las fotos sueltas de la galería. Abrilo desde el sitio publicado o con un servidor local.')}}
/* ---------- vista previa nítida y tamaño personalizado (mismo código en Obras y Anuncios) ----------
   Cada formato tiene dos canvas: el completo (lienzo(c), fuera de pantalla, a 1080 px o al tamaño elegido), que es el que se descarga,
   y el visible (c), al tamaño en que se muestra × devicePixelRatio, al que se copia el completo con suavizado de alta calidad.
   Si la reducción pasa de 2x se hace por mitades, para que la foto no se vea dentada. Al redimensionar la ventana se vuelve a copiar. */
const lienzo=c=>c._full??=document.createElement('canvas');
function mostrar(c){const f=c._full;if(!f||!f.width||!c.isConnected)return;const cw=c.clientWidth;if(!cw)return;
  const dpr=window.devicePixelRatio||1,tw=Math.max(1,Math.round(cw*dpr)),th=Math.max(1,Math.round(tw*f.height/f.width));
  let src=f;while(src.width/tw>2){const m=document.createElement('canvas');m.width=Math.max(tw,Math.round(src.width/2));m.height=Math.max(th,Math.round(src.height/2));
    const mg=m.getContext('2d');mg.imageSmoothingEnabled=true;mg.imageSmoothingQuality='high';mg.drawImage(src,0,0,m.width,m.height);src=m}
  if(c.width!==tw)c.width=tw;if(c.height!==th)c.height=th;const g=c.getContext('2d');g.imageSmoothingEnabled=true;g.imageSmoothingQuality='high';g.clearRect(0,0,tw,th);g.drawImage(src,0,0,tw,th)}
let _rs;window.addEventListener('resize',()=>{clearTimeout(_rs);_rs=setTimeout(()=>document.querySelectorAll('canvas').forEach(c=>{if(c._full)mostrar(c)}),150)});
// tamaño personalizado: uno por módulo, guardado en este navegador (gc_tam_obras). Si todavía no hay, se toma el de la clave
// compartida de antes (gc_tam_personalizado), para no perder lo que el equipo ya había elegido.
const TAM_KEY='gc_tam_obras', TAM_KEY_VIEJA='gc_tam_personalizado';
// presets agrupados por red: [red, [[nombre, ancho, alto], …]]. El valor de cada opción es ancho×alto.
// Los presets con un lado menor a 600 px (portadas y cabeceras) se exportan al doble, con la misma proporción.
const TAM_REDES=[['Instagram',[['Feed',1080,1080],['Feed',1080,1350],['Historia',1080,1920]]],
  ['Facebook',[['Publicación',1200,630],['Cuadrada',1080,1080],['Historia',1080,1920],['Portada',820,312]]],
  ['X',[['Publicación',1600,900],['Publicación',1200,675],['Cabecera',1500,500]]],
  ['LinkedIn',[['Publicación',1200,627],['Cuadrada',1080,1080],['Portada',1584,396]]],
  ['WhatsApp',[['Estado',1080,1920],['Imagen',1080,1080]]],
  ['TikTok',[['',1080,1920]]],
  ['YouTube',[['Miniatura',1280,720],['Comunidad',1080,1080]]],
  ['Pinterest',[['',1000,1500]]],
  ['Pantalla y web',[['HD',1920,1080],['4K',3840,2160],['Vertical HD',1080,1920]]]];
const TAM_PRESETS=TAM_REDES.flatMap(([red,ps])=>ps.map(([n,w0,h0])=>{const x=Math.min(w0,h0)<600?2:1;return {red,n:n?`${red} · ${n}`:red,corto:n||red,w0,h0,w:w0*x,h:h0*x,x}}));
const TAM_MSG='El tamaño personalizado va de 600 a 4000 px por lado y de 1:2,2 (alto hasta 2,2 veces el ancho) a 3,2:1 (ancho hasta 3,2 veces el alto)';
// rango: lados de 600 a 4000 px y proporción de 1:2,2 (vertical) a 3,2:1 (banner). Las cuatro formas están en formaDe()
const tamValido=(w,h)=>Number.isInteger(w)&&Number.isInteger(h)&&w>=600&&w<=4000&&h>=600&&h<=4000&&h<=w*2.2&&w<=h*3.2;
const tamLeer=k=>{try{const t=JSON.parse(localStorage.getItem(k)||'null');return t&&tamValido(t.w,t.h)?{w:t.w,h:t.h,...(t.preset?{preset:String(t.preset)}:{})}:null}catch(e){return null}};
let TAM=null;try{TAM=localStorage.getItem(TAM_KEY)!=null?tamLeer(TAM_KEY):tamLeer(TAM_KEY_VIEJA)}catch(e){}
const fmtWH=k=>k==='p'?[TAM.w,TAM.h]:FMT[k];                       // 'p' = el recuadro Personalizado
const fmtNombre=k=>k==='p'&&TAM?`${TAM.w}x${TAM.h}`:k;             // nombre del PNG: <id>_<ancho>x<alto>
const tamPreset=()=>TAM&&TAM.preset&&TAM_PRESETS.some(p=>p.n===TAM.preset&&p.w===TAM.w&&p.h===TAM.h)?TAM.preset:'a medida';
const tamTxt=()=>TAM?`${TAM.w}×${TAM.h}`:'sin definir';
const tamDesc=()=>TAM?`${TAM.w}×${TAM.h} (${tamPreset()}, ${formaDe(TAM.w,TAM.h)})`:'sin definir';   // para el Chequeo y el control
const tamNota=(w,h)=>w/h>3.2||h/w>2.2?`fuera de rango (${w/h>=1?(w/h).toFixed(1).replace('.0','').replace('.',',')+':1':'1:'+(h/w).toFixed(1).replace('.0','').replace('.',',')})`:'';   // por qué un preset está deshabilitado
const tamHTML=()=>{const pi=TAM?TAM_PRESETS.findIndex(p=>p.n===tamPreset()&&p.w===TAM.w&&p.h===TAM.h):-1;
  const opt=(p,i)=>{const ok=tamValido(p.w,p.h);return `<option value="${p.w}x${p.h}" data-preset="${p.n}" ${i===pi?'selected':''} ${ok?'':'disabled'}>${p.corto} ${p.w0}×${p.h0}${p.x>1?` (se exporta a ${p.w}×${p.h})`:''}${ok?'':' · '+tamNota(p.w,p.h)}</option>`};
  return `<span class="tam" data-tamctl>Tamaño personalizado: <b data-tamtxt>${tamTxt()}</b>${TAM?` <span data-tampre>(${tamPreset()}, ${formaDe(TAM.w,TAM.h)})</span>`:''} · <button type="button" class="lnk" data-tamabrir>${TAM?'cambiar':'elegir'}</button>
  <span class="tamed" hidden><select data-tampreset>${TAM_REDES.map(([red])=>`<optgroup label="${red}">${TAM_PRESETS.map((p,i)=>p.red===red?opt(p,i):'').join('')}</optgroup>`).join('')}<option value="" ${pi<0?'selected':''}>A medida</option></select>
  <label>Ancho <input type="number" data-tamw min="600" max="4000" step="1" value="${TAM?TAM.w:1080}"></label> × <label>Alto <input type="number" data-tamh min="600" max="4000" step="1" value="${TAM?TAM.h:1080}"></label> px
  <button type="button" class="btn" data-tamok>Aplicar</button>${TAM?'<button type="button" class="btn sec" data-tamquitar>Quitar tamaño</button>':''}<button type="button" class="btn sec" data-tamx>Cerrar</button><span class="tammsg" data-tammsg></span></span></span>`};
function tamWire(root){ // se engancha una sola vez al contenedor de la fila del período o de campaña (el control se redibuja adentro)
  const el=s=>root.querySelector(s), leer=()=>[+el('[data-tamw]').value,+el('[data-tamh]').value];
  const marcar=()=>{const [w,h]=leer(),ok=tamValido(w,h);el('[data-tamw]').classList.toggle('bad',!ok);el('[data-tamh]').classList.toggle('bad',!ok);el('[data-tammsg]').textContent=ok?'':TAM_MSG;return ok};
  const guardar=()=>{try{TAM?localStorage.setItem(TAM_KEY,JSON.stringify(TAM)):localStorage.setItem(TAM_KEY,'null')}catch(e){}
    const c=el('[data-tamctl]');if(c)c.outerHTML=tamHTML();window.dispatchEvent(new Event('gc-tam'))};
  const aplicar=()=>{if(!marcar())return;const [w,h]=leer(),o=el('[data-tampreset]').selectedOptions[0],pre=o&&o.value===`${w}x${h}`?o.dataset.preset:null;TAM={w,h,...(pre?{preset:pre}:{})};guardar()};
  root.addEventListener('click',ev=>{const b=ev.target.closest('button');if(!b||!b.closest('[data-tamctl]'))return;
    if(b.dataset.tamabrir!==undefined){const ed=el('.tamed');ed.hidden=!ed.hidden}else if(b.dataset.tamok!==undefined)aplicar();else if(b.dataset.tamquitar!==undefined){TAM=null;guardar()}else if(b.dataset.tamx!==undefined)el('.tamed').hidden=true});
  root.addEventListener('change',ev=>{if(ev.target.dataset.tampreset===undefined||!ev.target.value)return;const [w,h]=ev.target.value.split('x');el('[data-tamw]').value=w;el('[data-tamh]').value=h;aplicar()});
  root.addEventListener('input',ev=>{if(ev.target.dataset.tamw===undefined&&ev.target.dataset.tamh===undefined)return;el('[data-tampreset]').value='';marcar()});
  root.addEventListener('keydown',ev=>{if(ev.key==='Enter'&&ev.target.closest('[data-tamctl] .tamed'))aplicar()});
}
async function copiar(txt,btn){try{await navigator.clipboard.writeText(txt)}catch{const t=document.createElement('textarea');t.value=txt;document.body.appendChild(t);t.select();document.execCommand('copy');t.remove()}const o=btn.textContent;btn.textContent='¡Copiado!';btn.classList.add('ok');setTimeout(()=>{btn.textContent=o;btn.classList.remove('ok')},1200)}

/* ---------- calidad de foto: el diseño "Sugerido" ---------- */
const calCache=new Map();
function medirFoto(im){ // nitidez (varianza del laplaciano sobre una miniatura) y resolución
  const w=320,h=Math.max(1,Math.round(w*im.naturalHeight/im.naturalWidth)),c=document.createElement('canvas');c.width=w;c.height=h;
  const g=c.getContext('2d');g.drawImage(im,0,0,w,h);let d;
  try{d=g.getImageData(0,0,w,h).data}catch(e){return {nitidez:null,ancho:im.naturalWidth,alto:im.naturalHeight,vertical:im.naturalHeight>im.naturalWidth*1.1}} // archivo local: el navegador no deja leer los píxeles de una foto suelta
  const L=new Float32Array(w*h);
  for(let i=0;i<w*h;i++)L[i]=.299*d[i*4]+.587*d[i*4+1]+.114*d[i*4+2];
  let s=0,s2=0,n=0;for(let y=1;y<h-1;y++)for(let x=1;x<w-1;x++){const i=y*w+x,v=4*L[i]-L[i-1]-L[i+1]-L[i-w]-L[i+w];s+=v;s2+=v*v;n++}
  const m=s/n;return {nitidez:s2/n-m*m,ancho:im.naturalWidth,alto:im.naturalHeight,vertical:im.naturalHeight>im.naturalWidth*1.1};
}
window.__estiloSugerido=(v,im,gen,forma)=>{ // gen: la foto es genérica de la galería (se saltea el umbral de resolución); forma: la del lienzo (formaDe)
  const q=calCache.get(im.src)||calCache.set(im.src,medirFoto(im)).get(im.src);
  const borrosa=q.nitidez!=null&&q.nitidez<UMBRAL_NITIDEZ;
  const baja=gen?borrosa:(Math.min(q.ancho,q.alto)<720||borrosa);
  if(forma==='banner')return !baja&&!q.vertical?'completa':'sinfoto';   // banner: solo Foto completa (horizontal y nítida) o Sin foto
  if(forma==='apaisado'){if(baja||q.vertical)return 'circulo';return ['completa','marco'][hash(v.id||'')%2]}
  if(baja)return 'circulo';                 // chica o pixelada: recortada en círculo disimula la falta de definición
  if(q.vertical)return 'completa';          // vertical y nítida: a pantalla completa
  if(gen)return ['completa','marco'][hash(v.id||'')%2]; // genérica horizontal y nítida: Foto completa o Marco
  return ['completa','marco','circulo'][hash(v.id||'')%3]; // horizontal y nítida: variedad
};
const esGen=(v,i)=>{const x=(v._items||[])[v.fotos&&v.fotos.length?i%v.fotos.length:0];return !!x&&x.origen==='galeria'};

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
      sms:smsArmar('ciudad',[`en ${per} se ejecutaron ${U} obras en Córdoba, con ${nf(w.promPuestos)} puestos de trabajo por día`,`en ${per} se ejecutaron ${U} obras en Córdoba`,`${U} obras en ${per}`],'p_'+N),
      gac:limpio(gacetilla({titulo:titulos[0],bajada:[`En promedio, hubo ${w.promEjec} obras en ejecución por día.`,`Las obras generaron ${nf(w.promPuestos)} puestos de trabajo directos por día, en promedio.`,'Hacer para Crecer: obra pública sostenida en toda la ciudad.'],
        lead:`${cap(dato)}.`,secciones:[['Los programas',[EJES.calle.marco,EJES.accesible.marco,EJES.plaza.marco]]],cierre:MODELO}))});
  });
  Object.entries(CONT.periodicos||{}).forEach(([id,c])=>{
    const ex=out.find(p=>p.id===id);
    const pz=ex&&!ex.estado?ex:null;
    const nuevo={id,titulo:c.titulo||(ex&&ex.titulo)||id,eje:c.eje||'calle',titulos:(c.titulos||[]).map(limpio),ig:limpio(c.ig||''),x:limpio(c.x||''),gac:limpio(c.gac||''),sms:c.sms?limpio(c.sms):(ex&&ex.sms)||null,placa:{eje:c.eje||'calle',fotos:[],extra:'',...(c.placa||{})},redactado:true,w:ex&&ex.w};
    if(ex)out[out.indexOf(ex)]=nuevo;else out.push(nuevo);
  });
  const ord=id=>{const m=id.match(/^p_(\d+)(?:_(\w+))?$/);return m?[VENT.findIndex(v=>v[0]==+m[1]),['','plazas','rampas','pav','calle'].indexOf(m[2]||'')]:[99,0]};
  out.sort((a,b)=>{const x=ord(a.id),y=ord(b.id);return x[0]-y[0]||x[1]-y[1]});
  return out;
}

/* ---------- alcance: zona (seccional, subcircuito) y período (hoy, semana) ----------
   La zona y el período se eligen arriba y valen para todo el tablero. Seccional y circuito son datos internos: agrupan, filtran y rotulan la interfaz, pero no entran en ningún texto. */
const S={tab:'obras',secc:null,circ:null,per:'hoy',tipo:null,foto:null,q:''};
function diasSemana(){const fin=new Date(P.fecha+'T00:00:00'),ini=new Date(fin);ini.setDate(ini.getDate()-6);return {dias:HIST.filter(d=>{const t=new Date(d.fecha+'T00:00:00');return t>=ini&&t<=fin}),w:ventana(7)}}
let _sem=null;
function obrasSemana(){ // obras distintas de los últimos 7 días: cada una con los datos de su último parte y en cuántos partes apareció
  if(_sem)return _sem;const {dias}=diasSemana(),by={},n={};
  dias.forEach(d=>(d.obras||[]).forEach(o=>{by[o.id]=o;n[o.id]=(n[o.id]||0)+1}));
  if(!dias.some(d=>d.fecha===P.fecha))P.obras.forEach(o=>{by[o.id]=o;n[o.id]=(n[o.id]||0)+1});
  _sem=Object.values(by).map(o=>({...enriquecer(o),dias:n[o.id],k:Math.max(dias.length,1)}));return _sem;
}
const enZona=(o,z)=>z.circ?o.circuito===z.circ:z.secc?secc(o.circuito)===z.secc:true;
function alcance(z=S){const todas=(z.per==='semana'?obrasSemana():obras).filter(o=>enZona(o,z));return {todas,reales:todas.filter(o=>!o.grupo),grupos:todas.filter(o=>o.grupo)}}
const SECCS=uniq(reales.concat(obrasSemana().filter(o=>!o.grupo)).map(o=>o.secc)).sort(ordSecc);
const zonaId=z=>`z_${z.secc||'ciudad'}${z.circ?'_'+z.circ:''}_${z.per}`;
const zonaRotulo=z=>z.secc?`Seccional ${z.secc}${z.circ?' · circuito '+z.circ:''}`:'Toda la ciudad';
function resumenZona(z=S){ // pieza automática para una zona y un período: habla de barrios, nunca de la seccional
  const {reales:R2,grupos:G2}=alcance(z); if(!R2.length)return null;
  const sem=z.per==='semana', id=zonaId(z), k=s=>pick(s,{id},'z');
  const bs=uniq(R2.flatMap(o=>o.barrioList||[]));
  const lb=n=>bs.length>n?bs.slice(0,n).map(b=>'Barrio '+b).join(', ')+` y ${bs.length-n===1?'otro barrio':'otros '+(bs.length-n)+' barrios'}`:lista(bs.map(b=>'Barrio '+b));
  const donde=bs.length?`en ${lb(4)}`:(z.secc==='1'?'en la zona céntrica':'en el sector'), dondeCorto=bs.length?`en ${lb(2)}`:(z.secc==='1'?'en la zona céntrica':'en el sector');
  const por=TIPO_ORDEN.map(t=>[t,R2.filter(o=>o.tipo===t)]).filter(([,a])=>a.length);
  const nb=a=>uniq(a.flatMap(o=>o.barrioList||[])).length;
  const frase=(t,a)=>{const n=a.length;switch(t){
    case 'mant':return (nb(a)||n)===1?'mantenimiento de calles de tierra':`mantenimiento de calles en ${nb(a)||n} barrios`;
    case 'frio':return (nb(a)||n)===1?'bacheo en frío':`bacheo en frío en ${nb(a)||n} barrios`;
    case 'rampas':return `${sum(a,o=>o.rampas)} rampas de accesibilidad en ${n} ${n===1?'esquina':'esquinas'}`;
    case 'bacheo':return `${n} ${n===1?'frente':'frentes'} de bacheo con asfalto`;
    case 'rehab':return `${n} ${n===1?'frente':'frentes'} de rehabilitación con asfalto`;
    case 'hormigon':return `${n} ${n===1?'frente':'frentes'} de rehabilitación con hormigón`;
    case 'pav':return `pavimentación de ${sum(a,o=>o.m.cuadras)} cuadras`;
    case 'plaza':return `renovación de ${n} ${n===1?'plaza':'plazas'}`;}};
  const frases=por.map(([t,a])=>frase(t,a)), fr=lista(frases), frCorto=frases.length>2?frases.slice(0,2).join(', ')+', entre otras obras':lista(frases);
  const ejes=uniq(R2.map(o=>o.eje)), eje=ejes.length===1?ejes[0]:'calle', e=EJES[eje], U=R2.length;
  const {dias,w}=diasSemana(); const porDia=sem&&dias.length?Math.round(dias.map(d=>(d.obras||[]).filter(o=>!o.grupo&&enZona(o,z)).length).reduce((a,b)=>a+b,0)/dias.length):null;
  const cuando=sem?'En la última semana':'Hoy', obrasTxt=`${U} ${U===1?'obra':'obras'}`;
  const dato=sem?`${cuando}, ${GOB} ejecutaron ${obrasTxt} distintas ${donde}: ${fr}${porDia?`. En promedio hubo ${porDia} ${porDia===1?'obra':'obras'} en ejecución por día en la zona`:''}`
               :`${cuando}, ${GOB} ejecutan ${obrasTxt} ${donde}: ${fr}`;
  const cierre=k(CIERRES), cta=k(CTAS), tags=e.tags.join(' ');
  const titulos=uniq([`${U} ${U===1?'obra':'obras'} ${sem?'en la última semana':'en ejecución'} ${dondeCorto}`,`Hacer para Crecer: ${obrasTxt} ${donde}`,bs.length?`${bs.length===1?'El barrio':'Los barrios'} ${lista(bs.slice(0,3))}: ${frCorto}`:`${frCorto} ${donde}`].map(x=>x[0].toUpperCase()+x.slice(1))).map(limpio);
  const ig=limpio(`${e.emoji} ${up(obrasTxt)} ${up(sem?'ESTA SEMANA':'EN EJECUCIÓN')} ${up(dondeCorto)}\n\n${dato}.\n\n${k(e.cortos)}\n\n${cierre}\n\n👉 ${cta}\n\n${tags}`);
  const ht=e.tags.slice(0,2).join(' '), cab=`${e.emoji} ${sem?'Esta semana':'Hoy'}, ${obrasTxt} ${donde}: ${fr}.`, cab2=`${e.emoji} ${sem?'Esta semana':'Hoy'}, ${obrasTxt} ${dondeCorto}: ${frCorto}.`, cab3=`${e.emoji} ${sem?'Esta semana':'Hoy'}, ${obrasTxt} ${dondeCorto}.`;
  const x=limpio([`${cab}\n${cierre}\n${ht}`,`${cab}\n${ht}`,`${cab2}\n${cierre}\n${ht}`,`${cab2}\n${ht}`,`${cab3}\n${ht}`].find(t=>t.length<=280)||cab3);
  const smsAlc=bs.length===1?'barrio':'sector', smsCuando=sem?'esta semana ':'';
  const sms=limpio(smsArmar(smsAlc,[`${smsCuando}${obrasTxt} en marcha ${donde}: ${frCorto}`,`${smsCuando}${obrasTxt} en marcha ${dondeCorto}`,`${smsCuando}${obrasTxt} en marcha ${bs.length?'en '+lb(1):donde}`,`${obrasTxt} en marcha cerca tuyo`],id));
  const placa={eje,fotos:[],kicker:sem?'Lectura semanal':'Obras en ejecución',valor:String(U),etiqueta:sem?(U===1?'Obra en la última semana':'Obras en la última semana'):(U===1?'Obra en ejecución':'Obras en ejecución'),sub:bs.length?lb(3):(z.secc==='1'?'Zona céntrica':'En el sector'),extra:frCorto[0].toUpperCase()+frCorto.slice(1)};
  const gac=limpio(gacetilla({titulo:titulos[0],bajada:frases.map(f=>f[0].toUpperCase()+f.slice(1)+'.').concat(['Hacer para Crecer: obra pública en cada barrio.']),lead:`${dato}.`,
    secciones:[['Obra por obra',R2.map(o=>hecho(o)+'.')],['Los programas',ejes.map(x=>EJES[x].marco)]],cierre:MODELO}));
  const out={id,titulo:`Resumen ${sem?'de la semana':'del día'} · ${zonaRotulo(z)}`,eje,titulos,ig,x,sms,placa,gac,incompleto:sem&&!w.completo?w:null,U,bs,grupos:G2.length};
  const c=(CONT.zonas||{})[id]; if(c){if(c.titulos)out.titulos=c.titulos.map(limpio);if(c.ig)out.ig=limpio(c.ig);if(c.x)out.x=limpio(c.x);if(c.sms)out.sms=limpio(c.sms);if(c.gac)out.gac=limpio(c.gac);if(c.placa)Object.assign(out.placa,c.placa);out.redactado=true;}
  return out;
}
const smsDePlaca=gx=>{const v=gx.placa||{},low=t=>t?t[0].toLowerCase()+t.slice(1):'';const b=v.valor?`${v.valor} ${low(v.etiqueta)}`:low(v.main||'');return smsArmar('ciudad',[v.sub?`${b}, ${low(v.sub)}`:null,b].filter(Boolean),gx.id||'')};

/* ---------- foto propia y encuadre: viven en este navegador (localStorage), por obra o pieza ---------- */
const FOTO_KEY='gc_obras_fotos'; let FOTOS={}; try{FOTOS=JSON.parse(localStorage.getItem(FOTO_KEY)||'{}')}catch(e){}
const guardarFotos=()=>{try{localStorage.setItem(FOTO_KEY,JSON.stringify(FOTOS));return true}catch(e){return false}};
const reducirFoto=file=>new Promise((res,rej)=>{const fr=new FileReader();fr.onerror=rej;fr.onload=()=>{const i=new Image();i.onerror=rej;i.onload=()=>{const M=1600,k=Math.min(1,M/Math.max(i.width,i.height)),c=document.createElement('canvas');c.width=Math.round(i.width*k);c.height=Math.round(i.height*k);c.getContext('2d').drawImage(i,0,0,c.width,c.height);res(c.toDataURL('image/jpeg',.85))};i.src=fr.result};fr.readAsDataURL(file)});
// las fotos de la placa, en este orden: la propia (si hay), las del parte y las genéricas de la galería del rubro (origen 'galeria')
// k = clave del encuadre guardado: 'propia', 'p0', 'p1'… (parte) y 'g:<archivo>' (galería)
const galDe=r=>(r&&GAL[r])||[];
const fotosDe=(id,base,rubro)=>{const f=FOTOS[id];return [...(f&&f.data?[{src:f.data,origen:'propia',k:'propia'}]:[]),
  ...(base||[]).map((src,i)=>({src,origen:'parte',k:'p'+i,n:i+1})),...galDe(rubro).map(g=>({src:g.src,origen:'galeria',k:'g:'+g.nombre,nombre:g.nombre}))]};
// foto inicial: la propia o la del parte; si no hay ninguna, una genérica que rota por id de obra (para que no se repita en todas)
// foto inicial: una genérica elegida a mano (guardada en el navegador) manda; si no, la propia o la del parte; si no hay ninguna, una genérica que rota por id
// rotación de genéricas: las obras de un rubro sin foto del parte, en el orden en que salen en el tablero (toda la ciudad, hoy; después las que
// solo están en la semana), toman la genérica 1, 2, 3… y vuelven a empezar. Es fija por obra: no cambia con filtros, zona ni período.
let _rot=null;
function rotacion(){ if(_rot)return _rot; _rot={};const n={},
  ord=(a,b)=>(parseInt(a.circuito)-parseInt(b.circuito))||String(a.circuito).localeCompare(String(b.circuito))||(b.grupo?1:0)-(a.grupo?1:0)||TIPO_ORDEN.indexOf(a.tipo)-TIPO_ORDEN.indexOf(b.tipo);
  const hoy=reales.concat(obras.filter(o=>o.grupo)).sort(ord), ids=new Set(hoy.map(o=>o.id));
  const sem=obrasSemana().filter(o=>!ids.has(o.id)).sort((a,b)=>(b.dias||0)-(a.dias||0)||(b.grupo?1:0)-(a.grupo?1:0)||ordSecc(a.circuito,b.circuito)||TIPO_ORDEN.indexOf(a.tipo)-TIPO_ORDEN.indexOf(b.tipo));
  hoy.concat(sem).forEach(o=>{if(!o.fotos.length&&!(o.id in _rot)){_rot[o.id]=n[o.tipo]||0;n[o.tipo]=(n[o.tipo]||0)+1}});
  return _rot;}
// genéricas nítidas de un rubro, medidas en el navegador con la misma función que el Sugerido (nitidez >= UMBRAL_NITIDEZ).
// Las borrosas quedan fuera de la rotación automática si hay al menos una nítida; siguen en la tira para elegir a mano.
// Si no se puede medir (tablero abierto como archivo local), cuentan como nítidas.
const _nit={};
const galNitidas=r=>_nit[r]??=Promise.all(galDe(r).map(g=>loadImg(g.src).then(im=>{const q=calCache.get(im.src)||calCache.set(im.src,medirFoto(im)).get(im.src);return q.nitidez==null||q.nitidez>=UMBRAL_NITIDEZ?g.nombre:null}).catch(()=>g.nombre))).then(a=>new Set(a.filter(Boolean)));
// foto inicial: una genérica elegida a mano (guardada en el navegador) manda; si no, la propia o la del parte; si no hay ninguna, la genérica que le toca en la rotación
const fotoInicial=(id,items,nitidas)=>{const g=(FOTOS[id]||{}).gal,k=g?items.findIndex(x=>x.origen==='galeria'&&x.nombre===g):-1;
  if(k>=0)return k; if(items.some(x=>x.origen!=='galeria'))return 0; if(!items.length)return 0;
  const gen=items.map((x,i)=>[x,i]).filter(([x])=>x.origen==='galeria'), nit=nitidas?gen.filter(([x])=>nitidas.has(x.nombre)):gen, pool=nit.length?nit:gen;
  const r=rotacion()[id];return pool[(r!=null?r:hash(id||''))%pool.length][1]};   // las piezas por tipo (no son obras) rotan por id
const rubroTxt=r=>RUBRO_TXT[r]||(TIPOS[r]?TIPOS[r].label.toLowerCase():r);
const EJE_COLOR={calle:'#17233d',accesible:'#eaab3b',plaza:'#4da070'};
// piezas por tipo (generales y periódicos): usan la galería de su rubro
const rubroPieza=id=>/(^g_plazas$|_plazas$)/.test(id)?'plaza':/(^g_accesible$|_rampas$)/.test(id)?'rampas':/(^g_cuadras$|_pav$)/.test(id)?'pav':null;
const tagFoto=(conFoto,rubro)=>conFoto?['foto','Con foto']:galDe(rubro).length?['generica','Foto genérica']:['sinfoto','Sin foto'];
/* ---------- UI ---------- */const ESTILOS_UI=[['sugerido','Sugerido'],['circulo','Círculo'],['marco','Marco'],['completa','Foto completa'],['sinfoto','Sin foto']];
// tilde "Pie con marcas" (encendido por defecto): apagado, la placa sale sin franja, logos, cinta ni wordmark del eje
const pieHTML=v=>`<label class="pie"><input type="checkbox" data-pie ${conPie(v)?'checked':''}> Pie con marcas</label>`;
// recuadro Personalizado: misma placa al tamaño elegido, con su propio zoom (el encuadre se guarda también por tamaño)
const pBoxHTML=(v,st,nf,est)=>{if(!TAM)return '';const z=(st&&st.encP&&st.encP.z)||1;
  const fo=formaDe(TAM.w,TAM.h),noBanner=fo==='banner'&&nf&&(est==='circulo'||est==='marco');
  return `<div class="fmt p"><div class="lbl">Personalizado · ${TAM.w}×${TAM.h} · ${fo}</div>${noBanner?`<div class="pvac">Este diseño no entra en banner: sale con el Sugerido para banner</div>`:''}<canvas data-fmt="p" class="${nf&&est!=='sinfoto'?'movible':''}"></canvas><div class="btns" style="justify-content:center"><button class="btn" data-dl="p">Bajar PNG</button></div>${nf&&est!=='sinfoto'?`<div class="encp">zoom <input type="range" min="0.5" max="2.5" step="0.05" value="${z}" data-zoomp> <span data-zoomvp>${Math.round(z*100)}%</span></div>`:''}</div>`};
const placaHTML=(id,v,st)=>{const propia=!!(FOTOS[id]&&FOTOS[id].data), nf=(v.fotos||[]).length, est=(st&&st.estilo)||'sugerido', fi=(st&&st.foto)||0;
 const items=(st&&st.items)||[], cur=items[fi], mini=(x,i,l)=>`<button class="mb ${i===fi?'on':''}" data-foto="${i}" title="${esc(x.nombre||l)}" aria-label="${esc(l)}"><img src="${x.src}" alt="">${l?esc(l):''}</button>`;
 const propias=items.map((x,i)=>[x,i]).filter(([x])=>x.origen!=='galeria'), gen=items.map((x,i)=>[x,i]).filter(([x])=>x.origen==='galeria');
 return `<div class="placa-ui" style="--eje:${EJE_COLOR[v.eje]||EJE_COLOR.calle}"><div class="fmts${TAM?' con-p':''}">${Object.entries(FMT).map(([k,f])=>`<div class="fmt"><div class="lbl">${f[2]}</div><canvas data-fmt="${k}" class="${nf&&est!=='sinfoto'?'movible':''}"></canvas><div class="btns" style="justify-content:center"><button class="btn" data-dl="${k}">Bajar PNG</button></div></div>`).join('')}${pBoxHTML(v,st,nf,est)}</div>
 ${cur&&cur.origen==='galeria'&&est!=='sinfoto'?'<div class="fotosel"><span class="genaviso">Foto genérica del tipo de obra. Podés elegir otra o subir la tuya</span></div>':''}
 ${conPie(v)?'':'<div class="fotosel"><span class="genaviso">Sin marcas: revisá que la foto tampoco tenga cartel institucional</span></div>'}
 <div class="btns"><button class="btn sec" data-dlall>Bajar las ${TAM?4:3} placas</button></div>
 <div class="fotosel">${nf?`Diseño: ${ESTILOS_UI.map(([k,l])=>`<button class="btn ${k===est?'':'sec'}" data-estilo="${k}" ${TAM&&formaDe(TAM.w,TAM.h)==='banner'&&(k==='circulo'||k==='marco')?'title="Este diseño no entra en banner: el recuadro Personalizado sale con el Sugerido para banner"':''}>${l}</button>`).join('')}`:''}${pieHTML(v)}</div>${nf?'<div class="fotosel" data-sug></div>':''}
 ${propias.length?`<div class="fotosel">Foto: ${propias.map(([x,i])=>mini(x,i,x.origen==='propia'?'Propia':'Parte '+x.n)).join('')}</div>`:''}
 ${gen.length?`<div class="fotosel gal"><span class="gt">Fotos genéricas de ${esc(rubroTxt(v._rubro))}</span>${gen.map(([x,i],j)=>mini(x,i,'')).join('')}</div>`:''}
 <div class="fotosel">${propia?`<img class="mini" src="${FOTOS[id].data}" alt="">`:''}<label class="btn sec">${propia?'Cambiar foto propia':'Subir foto propia'}<input type="file" accept="image/*" data-subir></label>${propia?'<button class="btn sec" data-quitar>Quitar foto propia</button>':''}<span class="aviso" data-foto-aviso></span>
  ${nf&&est!=='sinfoto'?`<span class="enc">Encuadre: arrastrá la foto en la placa · zoom <input type="range" min="0.5" max="2.5" step="0.05" value="${(st&&st.enc&&st.enc.z)||1}" data-zoom> <span data-zoomv>${Math.round(((st&&st.enc&&st.enc.z)||1)*100)}%</span></span>`:''}</div></div>`};
function txHTML(ig,x,pl,gac,titulos,sms){return `
 ${titulos&&titulos.length?`<div class="tx"><div class="row"><label>Opciones de título</label></div>${titulos.map(t=>`<div class="titulo"><span>${esc(t)}</span><button class="btn sec" data-copytxt="${esc(t)}">Copiar</button></div>`).join('')}</div>`:''}
 <div class="tx"><div class="row"><label>Copy de Instagram</label><button class="btn" data-copy="ig">Copiar</button></div><textarea data-t="ig" rows="11">${esc(ig)}</textarea></div>
 <div class="tx"><div class="row"><label>Texto para X <span class="n" data-n></span></label><button class="btn" data-copy="x">Copiar</button></div><textarea data-t="x" rows="5">${esc(x)}</textarea></div>
 ${sms!=null?`<div class="tx"><div class="row"><label>Texto para SMS <span class="n" data-nsms></span></label><span><button class="btn sec" data-tildes title="Algunos proveedores cuentan 70 caracteres si el texto lleva tildes">Sin tildes</button> <button class="btn" data-copy="sms">Copiar</button></span></div><textarea data-t="sms" rows="3">${esc(sms)}</textarea><div class="n" style="font-size:11px;color:var(--muted);font-weight:600;margin-top:3px">Un solo mensaje: hasta ${SMS_MAX} caracteres, contando el marcador ${LINK} como un link corto de ${LINK_LEN}. Pegar el link recortado en lugar de ${LINK}.</div></div>`:''}
 <div class="tx"><div class="row"><label>Texto de la placa <span class="n">(editable: cambia la placa)</span></label><button class="btn" data-copy="pl">Copiar</button></div><textarea data-t="pl" rows="4">${esc(pl)}</textarea></div>${gac?`<div class="tx"><div class="row"><label>Gacetilla de prensa</label><button class="btn" data-copy="gac">Copiar</button></div><textarea data-t="gac" rows="16">${esc(gac)}</textarea></div>`:'' }`;}
function wire(card,id,v){
  const state={foto:0,estilo:'sugerido',done:false,base:(v.fotos||[]).slice(),items:[]};
  const armar=()=>{state.items=fotosDe(id,state.base,v._rubro);v._items=state.items;v.fotos=state.items.map(x=>x.src)};
  armar();state.foto=fotoInicial(id,state.items);v._pie=!(FOTOS[id]&&FOTOS[id].sinPie);   // el tilde se guarda por pieza en el navegador, como el encuadre
  const tagEl=card.querySelector(':scope > summary [data-ft]');
  const retag=()=>{if(!tagEl)return;const [c,t]=tagFoto(state.base.length>0||!!(FOTOS[id]&&FOTOS[id].data),v._rubro);tagEl.className='tag '+c;tagEl.textContent=t};
  const generica=()=>{const x=state.items[state.foto];return !!x&&x.origen==='galeria'&&state.estilo!=='sinfoto'};
  // encuadre de la foto que se está usando (propia, del parte o genérica), guardado en el navegador por obra y por foto
  const fkey=()=>(state.items[state.foto]||{k:'p0'}).k;
  const encDe=()=>((FOTOS[id]||{}).enc||{})[fkey()]||null;
  const kP=()=>`${fkey()}@${TAM.w}x${TAM.h}`;                                          // encuadre del personalizado: por foto y por tamaño
  const encP=()=>TAM?(((FOTOS[id]||{}).enc||{})[kP()]||encDe()):null;              // si todavía no se tocó, toma el de los tres formatos
  const draw=()=>{v._enc=encDe();const ep=encP();card.querySelectorAll(':scope > .body > .grid canvas').forEach(c=>{c.classList.toggle('movible',!!(v.fotos&&v.fotos.length)&&state.estilo!=='sinfoto');
    if(c.dataset.fmt==='p'&&!TAM)return;const vv=c.dataset.fmt==='p'?Object.assign({},v,{_enc:ep}):v;
    renderPlaca(lienzo(c),vv,c.dataset.fmt,state.foto,state.estilo).then(()=>mostrar(c))})};
  let sug=card.querySelector('[data-sug]');
  const refrescarUI=()=>{const box=card.querySelector(':scope > .body > .grid .placa-ui');if(!box)return;state.enc=encDe();state.encP=encP();box.outerHTML=placaHTML(id,v,state);sug=card.querySelector('[data-sug]');draw();mostrarSug()};
  const grid=card.querySelector(':scope > .body > .grid');
  grid.addEventListener('change',async ev=>{const inp=ev.target;
    if(inp.dataset.subir!==undefined&&inp.files&&inp.files[0]){try{const data=await reducirFoto(inp.files[0]);FOTOS[id]=Object.assign({},FOTOS[id]||{},{data});delete (FOTOS[id].enc||{}).propia;delete FOTOS[id].gal;const ok=guardarFotos();armar();state.foto=0;if(state.estilo==='sinfoto')state.estilo='sugerido';refrescarUI();retag();if(!ok)card.querySelector('[data-foto-aviso]').textContent='La foto se usa ahora pero no entró en la memoria del navegador (hay muchas guardadas): quitá otras.'}catch(e){card.querySelector('[data-foto-aviso]').textContent='No se pudo leer la imagen.'}}
    else if(inp.dataset.zoom!==undefined||inp.dataset.zoomp!==undefined)guardarFotos()
    else if(inp.dataset.pie!==undefined){v._pie=inp.checked;if(inp.checked){if(FOTOS[id])delete FOTOS[id].sinPie}else (FOTOS[id]??={}).sinPie=true;guardarFotos();refrescarUI()}});
  grid.addEventListener('input',ev=>{if(ev.target.dataset.zoomp!==undefined&&TAM){const zv=card.querySelector('[data-zoomvp]');if(zv)zv.textContent=Math.round(ev.target.value*100)+'%';
      const f=FOTOS[id]??={};(f.enc??={})[kP()]=Object.assign({},encP()||{},{z:+ev.target.value});if(!state._raf){state._raf=requestAnimationFrame(()=>{state._raf=null;draw()})}return}
    if(ev.target.dataset.zoom===undefined)return;const zv=card.querySelector('[data-zoomv]');if(zv)zv.textContent=Math.round(ev.target.value*100)+'%';const f=FOTOS[id]??={};(f.enc??={})[fkey()]=Object.assign({},f.enc[fkey()]||{},{z:+ev.target.value});if(!state._raf){state._raf=requestAnimationFrame(()=>{state._raf=null;draw()})}});
  let arr=null;const fmts=()=>card.querySelector(':scope > .body > .grid .fmts');
  grid.addEventListener('pointerdown',ev=>{const c=ev.target.closest('canvas');if(!c||!c.classList.contains('movible')||c.closest('.fmts')!==fmts())return;const pp=c.dataset.fmt==='p'&&TAM,e=(pp?encP():encDe())||{};const r=c.getBoundingClientRect();arr={x:ev.clientX,y:ev.clientY,fx:e.fx??.5,fy:e.fy??.5,w:r.width,h:r.height,k:pp?kP():fkey(),base:e};c.setPointerCapture(ev.pointerId);ev.preventDefault()});
  grid.addEventListener('pointermove',ev=>{if(!arr)return;const f=FOTOS[id]??={};const o=(f.enc??={})[arr.k]=Object.assign({},arr.base,f.enc[arr.k]||{});o.fx=Math.min(1,Math.max(0,arr.fx-(ev.clientX-arr.x)/arr.w*1.2));o.fy=Math.min(1,Math.max(0,arr.fy-(ev.clientY-arr.y)/arr.h*1.2));if(!state._raf){state._raf=requestAnimationFrame(()=>{state._raf=null;draw()})}});
  const finArr=()=>{if(arr){arr=null;guardarFotos()}};grid.addEventListener('pointerup',finArr);grid.addEventListener('pointercancel',finArr);
  const mostrarSug=async()=>{if(!sug)return;const im=await loadImg(v.fotos[state.foto%v.fotos.length]);const q=calCache.get(im.src)||calCache.set(im.src,medirFoto(im)).get(im.src);const k=window.__estiloSugerido(v,im,esGen(v,state.foto));
    sug.textContent=`Sugerido: ${{circulo:'Círculo',marco:'Marco',completa:'Foto completa'}[k]} · foto de ${q.ancho}×${q.alto}px, ${q.vertical?'vertical':'horizontal'}, ${q.nitidez==null?'nitidez no medible (archivo local)':'nitidez '+Math.round(q.nitidez)}${esGen(v,state.foto)?' · genérica':''}`;};
  const alTam=()=>{if(!card.isConnected){window.removeEventListener('gc-tam',alTam);return}if(state.done)refrescarUI()};window.addEventListener('gc-tam',alTam);   // cambió el tamaño personalizado
  card.addEventListener('toggle',async()=>{if(card.open&&!state.done){state.done=true;   // las miniaturas se arman al abrir la tarjeta
    if(galDe(v._rubro).length){state.nit=await galNitidas(v._rubro);state.foto=fotoInicial(id,state.items,state.nit)}refrescarUI()}});
  card.addEventListener('click',ev=>{const b=ev.target.closest('button');if(!b)return;
    const suf=()=>`${generica()?'_generica':''}${conPie(v)?'':'_sinmarca'}`;   // se descarga el canvas completo, no la vista previa
    if(b.dataset.dl){const c=card.querySelector(`:scope > .body > .grid canvas[data-fmt="${b.dataset.dl}"]`);if(c)descargar(lienzo(c),`${id}_${fmtNombre(b.dataset.dl)}${suf()}`)}
    else if(b.dataset.dlall!==undefined){[...card.querySelectorAll(':scope > .body > .grid canvas')].forEach((c,i)=>setTimeout(()=>descargar(lienzo(c),`${id}_${fmtNombre(c.dataset.fmt)}${suf()}`),i*400))}
    else if(b.dataset.quitar!==undefined){if(FOTOS[id]){delete FOTOS[id].data;delete (FOTOS[id].enc||{}).propia}guardarFotos();armar();state.foto=fotoInicial(id,state.items,state.nit);refrescarUI();retag()}
    else if(b.dataset.foto!==undefined){state.foto=+b.dataset.foto;const x=state.items[state.foto];   // la genérica elegida a mano se recuerda por obra, como el encuadre
      if(x&&x.origen==='galeria')(FOTOS[id]??={}).gal=x.nombre;else if(FOTOS[id])delete FOTOS[id].gal;guardarFotos();refrescarUI()}
    else if(b.dataset.estilo){state.estilo=b.dataset.estilo;refrescarUI()}
    else if(b.dataset.copytxt!==undefined){copiar(b.dataset.copytxt,b)}
    else if(b.dataset.copy){copiar(card.querySelector(`textarea[data-t="${b.dataset.copy}"]`).value,b)}});
  const x=card.querySelector('textarea[data-t="x"]'),n=card.querySelector('[data-n]');const cnt=()=>{n.textContent=x.value.length+'/280';n.classList.toggle('bad',x.value.length>280)};x.addEventListener('input',cnt);cnt();
  const sm=card.querySelector('textarea[data-t="sms"]'),ns=card.querySelector('[data-nsms]');
  if(sm){const cs=()=>{const L=smsLen(sm.value);ns.textContent=`${L}/${SMS_MAX}${/[áéíóúÁÉÍÓÚ]/.test(sm.value)?' · con tildes':' · sin tildes'}`;ns.classList.toggle('bad',L>SMS_MAX)};sm.addEventListener('input',cs);cs();
    card.querySelector('[data-tildes]').addEventListener('click',()=>{sm.value=sinTildes(sm.value);cs()});}
  const pl=card.querySelector('textarea[data-t="pl"]');let tm;pl.addEventListener('input',()=>{leerPlaca(v,pl.value);clearTimeout(tm);tm=setTimeout(draw,350)});  // el texto editado se refleja en la placa
}
function obraCard(o,ult){ // ult: fecha del último parte en que apareció (vista semanal)
  const v=placaDe(o),e=EJES[o.eje];v._rubro=o.tipo;
  const [tc,tt]=tagFoto(o.fotos.length>0||!!(FOTOS[o.id]&&FOTOS[o.id].data),o.tipo);   // el filtro Con foto / Sin foto sigue contando solo la foto del parte
  const el=document.createElement('details');el.className='card e-'+o.eje;
  const tit=o.tipo==='plaza'?o.via:(o.via||o.sector)+(o.entre?` · entre ${o.entre}`:'');
  el.innerHTML=`<summary><div class="tt"><b>${esc(tit)}</b><span>${esc(TIPOS[o.tipo].label)}${bar(o)?' · Barrio '+esc(bar(o)):''}${o.tipo==='rampas'&&!o.grupo?` · ${o.rampas} ${o.rampas===1?'rampa':'rampas'}`:''}${o.grupo?` · grupo de ${esq(o)} esquinas, ${o.rampas} rampas`:''}</span></div>
   ${o.grupo?'<span class="tag grupo">Grupo</span>':''}${o.dias!=null&&S.per==='semana'?`<span class="tag dias">en ${o.dias} de ${o.k} partes${ult?' · último '+ddmm(ult):''}</span><span class="tag circ">${esc(o.circuito)}</span>`:''}<span class="tag ${tc}" data-ft>${tt}</span><span class="tag ${o.eje}">${esc(e.nombre.split(' – ')[0])}</span></summary>
   <div class="body"><div class="grid"><div>${placaHTML(o.id,v)}</div><div>${txHTML(textoIG(o),textoX(o),textoPlaca(v),null,null,textoSMS(o))}</div></div>
   <div class="meta">Parte: circuito ${esc(o.circuito)}${o.circNombre?' · '+esc(o.circNombre):''} · ${o.driveUrl?`<a href="${esc(o.driveUrl)}" target="_blank" rel="noopener">Doc/archivo en Drive</a>`:'sin link de Drive'}</div>
   ${o.docTxt?`<details class="doc"><summary>Texto original del doc</summary><pre>${esc(o.docTxt)}</pre></details>`:''}</div>`;
  wire(el,o.id,v);return el;
}
function renderObras(root){
  const {reales:RZ,grupos:GZ}=alcance(), sem=S.per==='semana', {w,dias}=diasSemana();
  const f=RZ.filter(o=>(!S.tipo||o.tipo===S.tipo)&&(!S.foto||(S.foto==='con')===(o.fotos.length>0))&&(!S.q||norm([o.via,o.sector,o.barrio,o.entre,o.circNombre,o.circuito].filter(Boolean).join(' ')).includes(norm(S.q))));
  const grupos=GZ.filter(o=>(!S.tipo||o.tipo===S.tipo)&&(!S.foto||(S.foto==='con')===(o.fotos.length>0)));
  const reales=RZ, ult={};
  if(sem){dias.forEach(d=>(d.obras||[]).forEach(o=>{ult[o.id]=d.fecha}));if(!dias.some(d=>d.fecha===P.fecha))P.obras.forEach(o=>{ult[o.id]=P.fecha})}
  root.innerHTML=`${sem?`<div class="note">Vista semanal: obras distintas de los últimos 7 días, cada una con los datos de su último parte, ordenadas por cantidad de partes (lo que estuvo toda la semana, primero).${w.completo?'':` Faltan partes: hay ${w.k} de ${w.req} días hábiles.`} Los copys hablan de la obra; para el resumen de la semana, ver “Resumen”.</div>`:''}
   <div class="listbar"><div class="count">${f.length} de ${reales.length} obras${S.tipo||S.foto||S.q?' · <a href="#" id="clr">limpiar filtros</a>':''}</div>${f.length+grupos.length?'<button class="btn sec" id="abrir">Abrir todas</button>':''}</div><div id="list"></div>`;
  const list=$('#list',root), todas=f.concat(grupos);
  if(sem){ // semana: una sola lista, de más a menos partes
    todas.sort((a,b)=>(b.dias||0)-(a.dias||0)||(b.grupo?1:0)-(a.grupo?1:0)||ordSecc(a.circuito,b.circuito)||TIPO_ORDEN.indexOf(a.tipo)-TIPO_ORDEN.indexOf(b.tipo)).forEach(o=>list.appendChild(obraCard(o,ult[o.id])));
  }else{
    const byC={};todas.forEach(o=>(byC[o.circuito]??=[]).push(o));
    Object.keys(byC).sort((a,b)=>parseInt(a)-parseInt(b)||a.localeCompare(b)).forEach(c=>{
      const h=document.createElement('div');h.className='circ-head';h.innerHTML=`${esc(c)} <small>${esc(CIRC[c]||'(sin nombre en data/circuitos.json)')} · ${byC[c].filter(o=>!o.grupo).length} obras</small>`;list.appendChild(h);
      byC[c].sort((a,b)=>(b.grupo?1:0)-(a.grupo?1:0)||TIPO_ORDEN.indexOf(a.tipo)-TIPO_ORDEN.indexOf(b.tipo)).forEach(o=>list.appendChild(obraCard(o)));});
  }
  const ab=$('#abrir',root), cards=()=>[...list.querySelectorAll('details.card')];
  const rotular=()=>{if(ab)ab.textContent=cards().length&&cards().every(c=>c.open)?'Cerrar todas':'Abrir todas'};
  list.addEventListener('toggle',rotular,true);
  root.onclick=ev=>{if(ev.target.id==='clr'){ev.preventDefault();S.tipo=S.foto=null;S.q='';go()}
    else if(ev.target.id==='abrir'){const abrir=!cards().every(c=>c.open);cards().forEach(c=>{c.open=abrir});rotular()}};
}
function tarjetaContenido(gx,rotulo){
  const el=document.createElement('details');el.className='card e-'+gx.eje;gx.placa._rubro=rubroPieza(gx.id);
  el.innerHTML=`<summary><div class="tt"><b>${esc(gx.titulo)}</b><span>${esc(gx.placa.valor||'')} ${esc(gx.placa.etiqueta||'')}</span></div><span class="tag ${gx.eje}">${rotulo}</span></summary>
   <div class="body"><div class="grid"><div>${placaHTML(gx.id,gx.placa)}</div><div>${txHTML(gx.ig,gx.x,textoPlaca(gx.placa),gx.gac,gx.titulos,gx.sms!=null?gx.sms:smsDePlaca(gx))}</div></div></div>`;
  wire(el,gx.id,gx.placa);return el;
}
function renderGenerales(root){
  const sem=S.per==='semana', N=perN(S.per);
  if(N>7){ // lecturas de 10, 15 y 30 días: son de toda la ciudad
    const ps=periodicos().filter(p=>new RegExp('^p_'+N+'(_|$)').test(p.id)), v=VENT.find(x=>x[0]===N);
    root.innerHTML=`<div class="note">Resumen de <b>${esc(v?v[1]:N+' días')}</b> para toda la ciudad: la lectura general y las piezas por tipo de obra.${S.secc?' Las lecturas de 10, 15 y 30 días no se arman por zona.':''} Las demás lecturas están más abajo, en “Otras lecturas”.</div><div class="gen-grid" id="gl"></div><div id="otras"></div>`;
    ps.forEach(p=>{if(p.estado){const d=document.createElement('div');d.className='list';d.innerHTML=`<h3>${esc(p.titulo)}</h3><div style="font-size:12.5px;color:var(--muted);font-weight:600">${esc(p.estado)}</div>`;$('#gl',root).appendChild(d);return}$('#gl',root).appendChild(tarjetaContenido(p,'Periódico'))});
    renderPeriodicos($('#otras',root),ps.map(p=>p.id));return;}
  if(!S.secc){ // toda la ciudad: lo del período elegido y, al final, las otras lecturas
    let mostradas=[];
    if(!sem){
      root.innerHTML=`<div class="note">Estos contenidos se calculan <b>sumando el parte del día</b> (${R.obras} obras, ${R.rampas} rampas, ${R.cuadras} cuadras de las memorias). Sin montos ni cifras fiscales: el relato del modelo cordobés va con los mensajes oficiales.</div><div class="gen-grid" id="gl"></div><div id="otras"></div>`;
      generales().forEach(gx=>$('#gl',root).appendChild(tarjetaContenido(gx,'General')));
    }else{ // semana: las lecturas de 7 días
      const ps=periodicos().filter(p=>/^p_7(_|$)/.test(p.id));mostradas=ps.map(p=>p.id);
      root.innerHTML=`<div class="note">Resumen semanal de toda la ciudad: las lecturas de 7 días, con su texto para SMS. Las de 10, 15 y 30 días y las piezas por tipo están más abajo, en “Otras lecturas”.</div><div class="gen-grid" id="gl"></div><div id="otras"></div>`;
      ps.forEach(p=>{if(p.estado){const d=document.createElement('div');d.className='list';d.innerHTML=`<h3>${esc(p.titulo)}</h3><div style="font-size:12.5px;color:var(--muted);font-weight:600">${esc(p.estado)}</div>`;$('#gl',root).appendChild(d);return}$('#gl',root).appendChild(tarjetaContenido(p,'Semanal'))});
    }
    renderPeriodicos($('#otras',root),mostradas);return;}
  const rz=resumenZona();
  root.innerHTML=`<div class="note">Resumen ${sem?'de la última semana':'del día'} para <b>${esc(zonaRotulo(S))}</b>, armado automáticamente con las obras de la zona${rz&&rz.bs.length?` (${rz.bs.length} ${rz.bs.length===1?'barrio':'barrios'})`:''}. Los textos nombran barrios: nunca la seccional ni el circuito. Las lecturas de 10, 15 y 30 días y por tipo están en el Resumen de “Toda la ciudad”.${rz&&rz.incompleto?` <b>Ojo:</b> la semana tiene ${rz.incompleto.k} de ${rz.incompleto.req} partes.`:''}</div><div class="gen-grid" id="gl"></div>`;
  if(!rz){$('#gl',root).innerHTML=`<div class="list"><h3>Sin obras en esta zona</h3><div style="font-size:12.5px;color:var(--muted);font-weight:600">No hay obras ${sem?'en los últimos 7 días':'en el parte del día'} para ${esc(zonaRotulo(S))}.</div></div>`;return}
  $('#gl',root).appendChild(tarjetaContenido(rz,sem?'Semanal · zona':'Diario · zona'));
}
function renderPeriodicos(root,excluir=[]){ // "Otras lecturas" al pie del Resumen de toda la ciudad: 7, 10, 15 y 30 días y piezas por tipo
  const F=P.finalizadas||0, m50=redondo(F,50), prox=m50+50;
  root.innerHTML=`<h2 class="otras">Otras lecturas</h2><div class="note">Las lecturas periódicas se arman acumulando los partes diarios guardados: <b>${HIST.length} ${HIST.length===1?'parte cargado':'partes cargados'}</b> (${HIST.map(h=>ddmm(h.fecha)).join(', ')}). Cada día que me pases un parte nuevo se suma al histórico.</div>
   <div class="list"><h3>Números redondos para titulares</h3><ul>
    ${FINOK?`<li>${F%50===0?`<b>Ya se finalizaron ${F} obras</b> en la ciudad: número redondo para titular.`:`Obras finalizadas: ${F}. Titular posible hoy: “Ya se finalizaron más de ${m50} obras”. Faltan ${prox-F} para llegar a ${prox}.`}</li>`:'<li>El parte de hoy no trae el total de obras finalizadas: no se arman titulares con ese dato.</li>'}
    <li>Obras en ejecución hoy: ${R.obras}. Puestos de trabajo directos: ${nf(P.puestos)}.</li></ul></div><div class="gen-grid" id="pl"></div>`;
  periodicos().filter(p=>!excluir.includes(p.id)).forEach(p=>{
    if(p.estado){const d=document.createElement('div');d.className='list';d.innerHTML=`<h3>${esc(p.titulo)}</h3><div style="font-size:12.5px;color:var(--muted);font-weight:600">${esc(p.estado)}</div>`;$('#pl',root).appendChild(d);return}
    $('#pl',root).appendChild(tarjetaContenido(p,'Periódico'));});
}
function renderCalidad(root){
  // textos publicables que se revisan
  const T=[];reales.concat(obras.filter(o=>o.grupo)).forEach(o=>{const v=placaDe(o);T.push([o.id+' · Instagram',textoIG(o)],[o.id+' · X',textoX(o)],[o.id+' · placa',textoPlaca(v)],[o.id+' · SMS',textoSMS(o)])});
  obrasSemana().filter(o=>!P.obras.some(p=>p.id===o.id)).forEach(o=>T.push([o.id+' (semana) · SMS',textoSMS(o)],[o.id+' (semana) · X',textoX(o)]));
  const zonas=[];['hoy','semana'].forEach(per=>SECCS.forEach(sc=>{const r=resumenZona({secc:sc,circ:null,per});if(r)zonas.push(r)}));
  generales().concat(periodicos().filter(p=>!p.estado)).concat(zonas).forEach(g=>{T.push([g.id+' · Instagram',g.ig],[g.id+' · X',g.x],[g.id+' · gacetilla',g.gac],[g.id+' · placa',textoPlaca(g.placa)],[g.id+' · SMS',g.sms!=null?g.sms:smsDePlaca(g)]);g.titulos.forEach((t,i)=>T.push([g.id+' · título '+(i+1),t]))});
  const test=(re)=>T.filter(([,t])=>re.test(t)).map(([n])=>n);
  const SMS=T.filter(([n])=>/ · SMS$/.test(n));
  const reglas=[['No menciona “circuito”, “seccional” ni “subcircuito”',test(/circuito|seccional/i)],
    [`SMS de un solo mensaje (hasta ${SMS_MAX} caracteres, con link corto de ${LINK_LEN})`,SMS.filter(([,t])=>smsLen(t)>SMS_MAX).map(([n])=>n)],
    ['SMS: dice qué se hace antes del link y termina con el link',SMS.filter(([,t])=>!/\S.*\. Más info: \[link\]$/.test(t)).map(([n])=>n)],
['No menciona montos ni signos de pesos',test(/\$|presupuesto|monto/i)],['No usa barras “/” (salvo en links)',T.filter(([,t])=>/\//.test(t.replace(/https?:\/\/\S+/g,''))).map(([n])=>n)],['No menciona asistencia social en textos de obras',test(/asistencia social/i)],['Las piezas generales y periódicas no repiten la misma frase larga',(()=>{const c={};T.filter(([n])=>/^(g_|p_)/.test(n)&&!/· X$/.test(n)&&!/· placa$/.test(n)).forEach(([n,t])=>new Set(t.split(/(?<=[.!?])\s+/).filter(s=>s.length>70)).forEach(s=>{(c[s]=c[s]||[]).push(n.split(' ')[0])}));return Object.entries(c).filter(([,v])=>v.length>2).map(([s,v])=>s.slice(0,40)+'… ('+v.length+' piezas)')})()],['Los textos de X no superan 280 caracteres',T.filter(([n,t])=>/· X$/.test(n)&&t.length>280).map(([n])=>n)],['Los textos de X no terminan cortados (…)',T.filter(([n,t])=>/· X$/.test(n)&&/…/.test(t)).map(([n])=>n)],['Las obras con barrio lo nombran con la palabra “Barrio”',reales.filter(o=>bar(o)&&!new RegExp('Barrio '+bar(o).replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).test(textoIG(o))&&o.tipo!=='rampas').map(o=>o.id)]];
  const sf=reales.filter(o=>!o.fotos.length&&!galDe(o.tipo).length), sg=reales.filter(o=>!o.fotos.length&&galDe(o.tipo).length), sd=reales.filter(o=>!o.docTxt), sm=reales.filter(o=>!['rampas','plaza'].includes(o.tipo)&&!o.m.m2&&!o.m.ml&&!o.m.cuadras), sb=reales.filter(o=>!bar(o));
  const nm=o=>esc((o.via||o.sector)+(o.entre?` (${o.entre})`:''));
  const L=(t,a,hint)=>`<div class="list"><h3>${t} <small>(${a.length})</small></h3>${hint?`<div class="hint">${hint}</div>`:''}<ul>${a.map(x=>`<li>${x}</li>`).join('')||'<li>Nada pendiente</li>'}</ul></div>`;
  root.innerHTML=`<div class="note gris">Chequeo automático de los textos publicables y datos que faltan. No se rellena ningún dato: lo que falta queda fuera del texto.</div>
   <div class="list gris"><h3>Reglas de redacción</h3><ul>${reglas.map(([n,bad])=>`<li>${bad.length?'✖':'✔'} ${n}${bad.length?` — <b>${bad.length}</b> casos: ${esc(bad.slice(0,4).join(', '))}${bad.length>4?'…':''}`:''}</li>`).join('')}</ul><div class="hint">${T.length} textos revisados.</div></div>
   ${L('Avisos y contradicciones (parte vs. docs)',P.avisos.map(esc))}
   ${L('Obras sin foto (placa solo texto)',sf.map(nm),'Soltá la foto como <code>entrada/'+P.fecha+'/fotos/&lt;id-obra&gt;.jpg</code> o agregá el link de Drive en el parte.')}
   ${sg.length?L('Obras sin foto del parte (salen con foto genérica)',sg.map(nm),'Su rubro tiene galería. Para usar la foto real, soltala como <code>entrada/'+P.fecha+'/fotos/&lt;id-obra&gt;.jpg</code> o agregá el link de Drive en el parte.'):''}
   <div class="list"><h3>Pie con marcas</h3><div class="hint">El tilde “Pie con marcas” se guarda por pieza en este navegador.</div><ul><li>Piezas con pie apagado: ${Object.values(FOTOS).filter(f=>f&&f.sinPie).length}</li></ul></div>
   <div class="list"><h3>Tamaño personalizado</h3><div class="hint">Se elige en la fila del período y vale para todo el tablero de Obras (se guarda en este navegador; Anuncios tiene el suyo).</div><ul><li>Tamaño personalizado: ${tamDesc()}</li></ul></div>
   <div class="list"><h3>Galería de fotos genéricas</h3><div class="hint">Las fotos van en <code>assets/galeria/&lt;rubro&gt;/</code> y entran al volver a correr el build.</div><ul><li>Rubros sin galería: ${esc(lista(TIPO_ORDEN.filter(t=>!galDe(t).length).map(t=>TIPOS[t].label))||'ninguno')}</li></ul></div>
   ${L('Obras sin texto de Drive',sd.map(nm))}
   ${L('Obras sin magnitud (m², cuadras o metros)',sm.map(nm),'Con un dato de magnitud el texto y la placa ganan una cifra concreta.')}
   ${L('Obras sin barrio informado',sb.map(nm),'Se nombran por calle o esquina; si el parte trae el barrio, se usa siempre.')}`;
}
function renderSide(){ // columna lateral: período y zona (valen para todo el tablero) y, en la pestaña de obras, tipo, foto y búsqueda
  const sem=S.per==='semana', base=sem?obrasSemana().filter(o=>!o.grupo):reales;
  const nS=x=>base.filter(o=>o.secc===x).length, subs=S.secc?uniq(base.filter(o=>o.secc===S.secc).map(o=>o.circuito)).sort(ordSecc):[];
  const nz=alcance().reales.length, nzOtro=alcance({...S,per:sem?'hoy':'semana'}).reales.length;
  const RZ=alcance().reales, nCon=RZ.filter(o=>o.fotos.length).length, obrasTab=S.tab==='obras';
  const zb=(x,label,n)=>`<button class="${x===null?'todo ':''}${(x===null?!S.secc:S.secc===x)?'on':''}" data-z="${x===null?'':x}"><span>${label}</span><small>${n}</small></button>`;
  $('#side').innerHTML=`
   <div class="sec"><h4>Zona</h4><div class="zl">${zb(null,'Toda la ciudad',base.length)}${SECCS.map(x=>zb(x,x==='?'?'Sin código':'Secc. '+x,nS(x))+(S.secc===x&&subs.length>1?`<div class="subs">${subs.map(c=>`<button class="chip ${S.circ===c?'on':''}" data-zc="${c}">${esc(c)}<small>${base.filter(o=>o.circuito===c).length}</small></button>`).join('')}</div>`:'')).join('')}</div>
    <div class="res">${esc(zonaRotulo(S))}: <b>${nz}</b> ${nz===1?'obra':'obras'} ${sem?'en la semana':'hoy'} · ${nzOtro} ${sem?'hoy':'en la semana'}</div></div>
   ${obrasTab?`<div class="sec"><h4>Tipo de obra</h4><div class="chips">${TIPO_ORDEN.map(t=>`<button class="chip t-${TIPOS[t].eje} ${S.tipo===t?'on':''}" data-t="${t}">${TIPOS[t].corto}<small>${RZ.filter(o=>o.tipo===t).length}</small></button>`).join('')}</div></div>
   <div class="sec"><h4>Foto</h4><div class="chips"><button class="chip ${S.foto==='con'?'on':''}" data-f="con">Con foto<small>${nCon}</small></button><button class="chip ${S.foto==='sin'?'on':''}" data-f="sin">Sin foto<small>${RZ.length-nCon}</small></button></div></div>
   <div class="sec"><input class="search" placeholder="Buscar calle, barrio…" value="${esc(S.q)}" id="q">${S.tipo||S.foto||S.q?'<button class="clr" data-clr>Limpiar filtros</button>':''}</div>`:''}
   <div class="sec"><details class="datos"${S.datos?' open':''}><summary>Datos del parte</summary><div class="kpis">${[[P.enEjecucion,'en ejecución'],[P.finalizadas??'—','finalizadas'],[nf(P.puestos),'puestos directos'],[R.barrios,'barrios (mínimo)'],[R.rampas,'rampas'],[R.cuadras,'cuadras (memorias)']].map(([a,b])=>`<div class="kpi"><b>${a}</b><span>${b}</span></div>`).join('')}</div></details></div>`;
  $('details.datos',$('#side')).ontoggle=ev=>{S.datos=ev.target.open};
  $('#side').onclick=ev=>{const b=ev.target.closest('button');if(!b)return;
    if(b.dataset.z!==undefined){S.secc=b.dataset.z||null;S.circ=null;go()}
    else if(b.dataset.zc){S.circ=S.circ===b.dataset.zc?null:b.dataset.zc;go()}
    else if(b.dataset.t){S.tipo=S.tipo===b.dataset.t?null:b.dataset.t;go()}
    else if(b.dataset.f){S.foto=S.foto===b.dataset.f?null:b.dataset.f;go()}
    else if(b.dataset.clr!==undefined){S.tipo=S.foto=null;S.q='';go()}};
  const q=$('#q');if(q)q.oninput=ev=>{S.q=ev.target.value;clearTimeout(S._t);S._t=setTimeout(()=>{renderObras($('#main'));renderSide();renderCtx();const q2=$('#q');q2.focus();q2.setSelectionRange(q2.value.length,q2.value.length)},250)};
}
/* fechas para la interfaz (no entran en textos publicables) */
const MESES=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];
const DIAS=['domingo','lunes','martes','miércoles','jueves','viernes','sábado'];
const fch=s=>new Date(s+'T00:00:00'), ddmm=s=>{const d=fch(s);return String(d.getDate()).padStart(2,'0')+'/'+String(d.getMonth()+1).padStart(2,'0')};
const iniSemana=()=>{const d=fch(P.fecha);d.setDate(d.getDate()-6);return d};
function rangoCorto(){const a=iniSemana(),b=fch(P.fecha);return a.getMonth()===b.getMonth()?`${String(a.getDate()).padStart(2,'0')} al ${ddmm(P.fecha)}`:`${String(a.getDate()).padStart(2,'0')}/${String(a.getMonth()+1).padStart(2,'0')} al ${ddmm(P.fecha)}`}
function rangoLargo(){const a=iniSemana(),b=fch(P.fecha);return a.getMonth()===b.getMonth()?`del ${a.getDate()} al ${b.getDate()} de ${MESES[b.getMonth()]}`:`del ${a.getDate()} de ${MESES[a.getMonth()]} al ${b.getDate()} de ${MESES[b.getMonth()]}`}
const perN=p=>p==='semana'?7:(+((/^d(\d+)$/.exec(p)||[])[1])||0); // 0 = hoy; 7 = semana; 10, 15 y 30 = lecturas periódicas (solo en Resumen)
function renderCtx(){ // rótulo de contexto: zona, período con sus fechas y alcance
  const sem=S.per==='semana', N=perN(S.per), {reales:RZ}=alcance(), {dias}=diasSemana(), d=fch(P.fecha);
  const c=$('#ctx');c.className='ctx '+(sem?'semana':'hoy');
  if(S.tab==='calidad'){c.innerHTML=`<div class="l1">Chequeo de calidad</div><div class="l2">Textos publicables y datos que faltan, revisados con las reglas del módulo</div>`;return}
  const zona=S.secc?(S.secc==='?'?'Sin código de zona':`Seccional ${S.secc}`)+(S.circ?` · subcircuito ${S.circ}`:''):'Toda la ciudad';
  if(N>7){const v=VENT.find(x=>x[0]===N),w=ventana(N);c.innerHTML=`<div class="l1">Toda la ciudad<span class="sep">·</span><span class="pt">Resumen de ${esc(v?v[1]:N+' días')}</span></div><div class="l2">${w.k} ${w.k===1?'parte':'partes'} de ${w.req} días hábiles${w.completo?` · ${w.unicas} obras distintas`:' · faltan partes'}</div>`;return}
  const nb=uniq(RZ.flatMap(o=>o.barrioList||[])).length, nO=RZ.length, res=S.tab==='generales';
  const per=sem?`${res?'Resumen de la semana':'Semana'} · ${rangoLargo()} · ${dias.length} ${dias.length===1?'parte':'partes'}`:`${res?'Resumen del día':'Hoy'} · parte del ${DIAS[d.getDay()]} ${d.getDate()} de ${MESES[d.getMonth()]}`;
  const alc=`${nO} ${nO===1?'obra':'obras'}${sem?(nO===1?' distinta':' distintas'):' en ejecución'} · ${nb} ${nb===1?'barrio':'barrios'}`;
  c.innerHTML=`<div class="l1">${esc(zona)}<span class="sep">·</span><span class="pt">${esc(per)}</span></div><div class="l2">${esc(alc)}</div>`;
}
function renderVista(){ // barra de vista (cruza toda la hoja) y, debajo, el período que esa vista admite
  const tabs=[['obras','Obra por obra','copys, placas y textos de cada obra'],['generales','Resumen','lecturas generales y periódicas']];
  const cal=S._cal; // resultado del chequeo (se calcula una vez, después del primer dibujo)
  $('#vista').innerHTML=tabs.map(([k,l,s])=>`<button role="tab" class="tab ${S.tab===k?'on':''}" data-k="${k}" aria-selected="${S.tab===k}">${l}<small>${s}</small></button>`).join('')+
   `<button class="chequeo ${S.tab==='calidad'?'on':''} ${cal&&cal.n?'avisos':''}" data-k="calidad" title="Chequeo de calidad"><span class="dot"></span>Chequeo de calidad${cal?(cal.n?` · ${cal.n} ${cal.n===1?'regla con casos':'reglas con casos'}`:' · todo ✔'):''}</button>`;
  $('#vista').onclick=ev=>{const b=ev.target.closest('button[data-k]');if(b){S.tab=b.dataset.k;go()}};
  const per=$('#per');
  if(S.tab==='calidad'){per.innerHTML='';per.hidden=true;return}
  per.hidden=false;
  const chips=S.tab==='obras'
    ?[['hoy','Hoy',ddmm(P.fecha),''],['semana','Últimos 7 días',rangoCorto(),'semana'],['fin','Finalizadas','próximamente','no']]
    :[['hoy','Del día',ddmm(P.fecha),''],['semana','Semana',rangoCorto(),'semana'],...[[10,'Últimos 10 días'],[15,'Últimos 15 días'],[30,'Último mes']].map(([N,l])=>{const w=ventana(N);return ['d'+N,l,w.completo?`${w.k} partes`:'faltan partes',w.completo?'':'no']})];
  per.innerHTML=`<span class="lbl">Período</span>`+chips.map(([k,l,s,c])=>`<button class="pchip ${c==='no'?'':c} ${S.per===k?'on':''}" data-per="${k}" ${c==='no'?'disabled title="'+(k==='fin'?'Todavía no hay datos de obras finalizadas por obra':'Faltan partes para armar esta lectura')+'"':''}>${l}<small>${s}</small></button>`).join('')+tamHTML();
  per.onclick=ev=>{const b=ev.target.closest('button[data-per]');if(b&&!b.disabled){S.per=b.dataset.per;go()}};
}
function renderHeader(){
  const lk='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(A.svg['gobierno-color']);$('#lockup').src=lk;$('#lockup2').src=lk;
  $('#sub').innerHTML=`Última actualización: <b>parte del ${esc(P.fecha_texto)}</b>`;
  renderVista();
  document.documentElement.style.setProperty('--hh',$('header').offsetHeight+'px');
  renderSide();renderCtx();
}
function go(){if(!['obras','generales','calidad'].includes(S.tab))S.tab='obras';
  if(S.tab!=='generales'&&perN(S.per)>7)S.per='hoy'; // las lecturas de 10, 15 y 30 días existen solo en Resumen
  renderHeader();const m=$('#main');m.onclick=null;({obras:renderObras,generales:renderGenerales,calidad:renderCalidad})[S.tab](m);
  if(!S._cal){S._cal={n:null};setTimeout(()=>{try{const d=document.createElement('div');renderCalidad(d);const li=[...d.querySelectorAll('.list.gris li')];S._cal={n:li.filter(x=>x.textContent.trim().startsWith('✖')).length}}catch(e){S._cal={n:null}}renderVista()},0)}}
window.addEventListener('resize',()=>document.documentElement.style.setProperty('--hh',$('header').offsetHeight+'px'));
tamWire($('#per'));
go();
})();
</script>
</body>
</html>
~~~~
