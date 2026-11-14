/*
  De wedstrijdquiz voor de Dag van de Wetenschap (zondag 15 november 2026).

  Kim, 14 november 2026: "ik doe morgen mee aan de dag van de wetenschap. ik
  dacht ouders mss op de ipad een quizje / mini enquete laten af te nemen en dat
  ze dan een kamp konden winnen." En daarna: enkel bereikbaar via het beheer,
  plus 4 vragen om te polsen wat ouders zoeken in een kamp.

  Het is één losse pagina (gewone HTML en JavaScript), zodat ze op de iPad
  ook blijft werken als de wifi even wegvalt: elke deelname wordt eerst op de
  iPad bewaard en daarna doorgestuurd naar /beheer/quiz/bewaar. Daar komt ze
  bij de aanvragen terecht, met als soort "wedstrijd".

  Vragen en teksten aanpassen: bovenaan het script, bij VRAGEN en KAMPVRAGEN.
  Let op: in deze tekst mogen geen backticks staan.
*/
export const QUIZ_HTML = String.raw`<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>Wetenschapsquiz Connectopia</title>
<style>
  :root{
    --groen:#2f8f6b; --groen-d:#1f6b4f; --oranje:#f39a2b; --geel:#ffd45c;
    --rood:#d9534f; --tekst:#23313a; --zacht:#f4f8f5; --rand:#d7e3dc;
  }
  *{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
  html,body{margin:0;height:100%}
  body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    color:var(--tekst);background:linear-gradient(160deg,#e9f6ef 0%,#fff7e8 100%);min-height:100vh;
    -webkit-user-select:none;user-select:none}
  input,textarea{-webkit-user-select:text;user-select:text}
  .wrap{max-width:820px;margin:0 auto;padding:28px 24px 80px;min-height:100vh;display:flex;flex-direction:column}
  .kop{display:flex;align-items:center;gap:12px;margin-bottom:18px}
  .logo{width:52px;height:52px;border-radius:50%;background:var(--groen);color:#fff;display:grid;place-items:center;font-size:28px;flex:none}
  .merk{font-weight:800;font-size:22px;color:var(--groen-d)}
  .merk small{display:block;font-weight:500;font-size:14px;color:#5b6b73}
  .kaart{background:#fff;border-radius:22px;box-shadow:0 8px 30px rgba(31,107,79,.12);padding:32px;flex:1;display:flex;flex-direction:column}
  h1{font-size:40px;line-height:1.1;margin:0 0 12px}
  h2{font-size:30px;line-height:1.2;margin:0 0 18px}
  p{font-size:19px;line-height:1.5;margin:0 0 14px}
  .groot{font-size:22px}
  .knop{appearance:none;border:0;border-radius:16px;padding:20px 26px;font-size:22px;font-weight:700;cursor:pointer;
    background:var(--groen);color:#fff;box-shadow:0 4px 0 var(--groen-d);transition:transform .05s}
  .knop:active{transform:translateY(3px);box-shadow:0 1px 0 var(--groen-d)}
  .knop.oranje{background:var(--oranje);box-shadow:0 4px 0 #c97412}
  .knop.licht{background:var(--zacht);color:var(--groen-d);box-shadow:0 4px 0 var(--rand)}
  .knop.klein{font-size:17px;padding:12px 16px}
  .knop:disabled{opacity:.45}
  .rij{display:flex;gap:12px;flex-wrap:wrap;align-items:center}
  .onder{margin-top:auto;padding-top:22px;display:flex;justify-content:space-between;gap:12px;align-items:center}
  .badge{display:inline-block;background:var(--geel);color:#5a4300;font-weight:800;border-radius:999px;padding:8px 16px;font-size:17px;margin-bottom:16px}
  .hero{text-align:center;justify-content:center}
  .hero .emoji{font-size:90px;line-height:1;margin-bottom:10px}
  .opties{display:grid;gap:14px;margin-top:8px}
  .optie{appearance:none;text-align:left;border:3px solid var(--rand);background:#fff;border-radius:16px;padding:18px 20px;font-size:21px;font-weight:600;color:var(--tekst);cursor:pointer}
  .optie.juist{border-color:var(--groen);background:#e3f5ec}
  .optie.fout{border-color:var(--rood);background:#fbe9e8}
  .optie:disabled{cursor:default}
  .uitleg{margin-top:18px;background:var(--zacht);border-radius:14px;padding:16px 18px;font-size:18px;line-height:1.5}
  .voortgang{height:10px;background:var(--zacht);border-radius:99px;overflow:hidden;margin-bottom:22px}
  .voortgang div{height:100%;background:var(--oranje);transition:width .3s}
  label.veld{display:block;font-weight:700;font-size:18px;margin:16px 0 6px}
  input[type=text],input[type=email],input[type=tel],input[type=number],input[type=password]{width:100%;font-size:20px;padding:15px 16px;border:2px solid var(--rand);border-radius:12px;background:#fff;color:var(--tekst)}
  input:focus{outline:none;border-color:var(--groen)}
  .fout-tekst{color:var(--rood);font-weight:600;font-size:16px;margin-top:6px;min-height:1em}
  .chips{display:flex;flex-wrap:wrap;gap:10px}
  .chip{appearance:none;border:2px solid var(--rand);background:#fff;border-radius:999px;padding:12px 18px;font-size:18px;font-weight:600;color:var(--tekst);cursor:pointer}
  .chip.aan{background:var(--groen);border-color:var(--groen);color:#fff}
  .kind{display:flex;align-items:center;gap:12px;margin:8px 0;flex-wrap:wrap}
  .kind span{font-weight:600;font-size:18px;min-width:70px}
  select{font-size:19px;padding:12px;border:2px solid var(--rand);border-radius:12px;background:#fff;color:var(--tekst)}
  .stepper{display:flex;align-items:center;gap:14px}
  .stepper b{font-size:26px;min-width:30px;text-align:center}
  .vink{display:flex;gap:14px;align-items:flex-start;background:var(--zacht);border-radius:14px;padding:16px;margin-top:14px;cursor:pointer}
  .vink input{width:30px;height:30px;flex:none;margin:2px 0 0;accent-color:var(--groen)}
  .vink div{font-size:17px;line-height:1.5}
  .klein-tekst{font-size:15px;color:#5b6b73;line-height:1.5}
  .score{font-size:64px;font-weight:900;color:var(--oranje);margin:6px 0}
  .geheim{position:fixed;right:0;bottom:0;width:70px;height:70px}
  .verborgen{display:none!important}
  table{border-collapse:collapse;width:100%;font-size:14px}
  th,td{border-bottom:1px solid var(--rand);padding:8px 6px;text-align:left;vertical-align:top}
  th{background:var(--zacht)}
  .tabelvak{overflow:auto;max-height:45vh;border:1px solid var(--rand);border-radius:12px;margin:12px 0}
  textarea{width:100%;height:160px;font-size:13px;font-family:ui-monospace,Menlo,monospace;border:2px solid var(--rand);border-radius:12px;padding:10px}
  .melding{font-weight:700;color:var(--groen-d);min-height:1.4em;font-size:17px}
  .confetti{position:fixed;top:-20px;width:12px;height:18px;border-radius:3px;pointer-events:none;animation:val 2.6s linear forwards}
  @keyframes val{to{transform:translateY(110vh) rotate(720deg);opacity:.8}}
</style>
</head>
<body>
<div class="wrap">
  <div class="kop">
    <div class="logo" aria-hidden="true">🔬</div>
    <div class="merk">Connectopia<small>Dag van de Wetenschap</small></div>
  </div>
  <main class="kaart" id="scherm"></main>
</div>
<div class="geheim" id="geheim" aria-hidden="true"></div>

<script>
(function(){
"use strict";

/* ====== Teksten en vragen (hier aanpassen) ====== */
var PRIJS = "een gratis kamp bij Connectopia";
var CONTACT = "info@matmgroep.com";
var PINCODE = "2026";

var VRAGEN = [
  { v:"Hoeveel poten heeft een spin?",
    o:["6 poten","8 poten","10 poten"], j:1,
    u:"Een spin heeft 8 poten. Insecten hebben er 6, dus een spin is geen insect maar een spinachtige." },
  { v:"Wat is het grootste orgaan van je lichaam?",
    o:["Je hart","Je lever","Je huid","Je hersenen"], j:2,
    u:"Je huid! Bij een volwassene weegt die zo'n 3 tot 4 kilo en ze beschermt je hele lichaam." },
  { v:"Waarom drijft een ijsblokje in je glas water?",
    o:["Omdat het koud is","Omdat ijs lichter is dan hetzelfde volume water","Omdat er altijd lucht in zit"], j:1,
    u:"Water zet uit als het bevriest. Daardoor is ijs minder dicht dan water en blijft het drijven. Zo vriezen vijvers van boven naar onder dicht en overleven de vissen." },
  { v:"Hoe lang doet het licht van de zon erover om de aarde te bereiken?",
    o:["Ongeveer 1 seconde","Ongeveer 8 minuten","Ongeveer 1 dag"], j:1,
    u:"Ongeveer 8 minuten. Als je naar de zon kijkt (doe dat nooit rechtstreeks!), zie je dus eigenlijk de zon van 8 minuten geleden." }
];
/* Polsen wat ouders zoeken in een kamp of hobby: geen juist of fout, meerdere keuzes mogen. */
var KAMPVRAGEN = [
  { v:"Welk soort kamp of hobby zou je kind het leukst vinden?",
    o:["Wetenschap en proefjes","Robots, techniek en programmeren","Bouwen en uitvinden","Natuur en buiten ontdekken","Creatief en kunst","Een mix van alles"] },
  { v:"In welke vakantie zoek je een kamp?",
    o:["Krokusvakantie","Paasvakantie","Zomervakantie","Herfstvakantie","Kerstvakantie"] },
  { v:"Wat past het best bij jullie gezin?",
    o:["Kampen met volle dagen","Kampen met halve dagen","Opvang voor en na het kamp","Een vaste hobby op woensdagnamiddag","Een vaste hobby op zaterdag","Dichtbij huis"] },
  { v:"Wat vind je het belangrijkst aan een kamp of hobby?",
    o:["Kleine groepjes","Begeleiders die mijn kind begrijpen","Uitdaging op het niveau van mijn kind","Nieuwe vriendjes maken","Gewoon veel plezier","Een betaalbare prijs"] }
];
var SCHIFTING = "Schiftingsvraag: hoeveel mensen doen vandaag mee aan deze quiz?";

var INTERESSES = ["Kampen","Plusklas","Ontdekclub","Young Engineers"];
var LEEFTIJDEN = ["jonger dan 6"].concat([6,7,8,9,10,11,12,13,14,15].map(function(n){return n+" jaar"})).concat(["ouder dan 15"]);

/* ====== Opslag ====== */
var SLEUTEL = "connectopia-dvdw-2026";
var geheugen = [];
function leesLokaal(){
  try{ var r = localStorage.getItem(SLEUTEL); if(r){ return JSON.parse(r)||[]; } }catch(e){}
  return geheugen;
}
function schrijfLokaal(lijst){
  geheugen = lijst;
  try{ localStorage.setItem(SLEUTEL, JSON.stringify(lijst)); }catch(e){}
}

/* Elke deelname gaat naar het beheer van het ouderportaal (bij de aanvragen).
   Lukt dat even niet (geen wifi), dan blijft ze op de iPad bewaard en
   proberen we het om de 30 seconden opnieuw. */
var BEWAAR_ADRES = "/beheer/quiz/bewaar";
var bezig = false;
function synchroniseer(){
  if(bezig) return;
  var open = leesLokaal().filter(function(x){ return !x._online; });
  if(!open.length) return;
  bezig = true;
  var i = 0;
  (function volgende(){
    if(i >= open.length){ bezig = false; return; }
    var rec = open[i++];
    var kopie = {}; for(var k in rec){ if(k.charAt(0) !== "_") kopie[k] = rec[k]; }
    fetch(BEWAAR_ADRES, { method:"POST", headers:{"Content-Type":"application/json"}, credentials:"same-origin", body: JSON.stringify(kopie) })
      .then(function(r){
        if(!r.ok) throw new Error("status " + r.status);
        return r.json();
      })
      .then(function(d){
        if(!d || d.ok !== true) throw new Error("niet bewaard");
        var l = leesLokaal();
        l.forEach(function(x){ if(x.id === rec.id) x._online = true; });
        schrijfLokaal(l);
        volgende();
      })
      .catch(function(){ bezig = false; });
  })();
}
setInterval(synchroniseer, 30000);
window.addEventListener("online", synchroniseer);

/* ====== Hulpjes ====== */
var S = document.getElementById("scherm");
function el(tag, attrs, kinderen){
  var n = document.createElement(tag);
  if(attrs){ for(var a in attrs){
    if(a === "tekst") n.textContent = attrs[a];
    else if(a === "klik") n.addEventListener("click", attrs[a]);
    else if(a === "klasse") n.className = attrs[a];
    else n.setAttribute(a, attrs[a]);
  }}
  (kinderen||[]).forEach(function(k){ if(k) n.appendChild(typeof k === "string" ? document.createTextNode(k) : k); });
  return n;
}
function toon(nodes){ S.innerHTML = ""; nodes.forEach(function(n){ if(n) S.appendChild(n); }); window.scrollTo(0,0); }
function stip(){ return Date.now().toString(36) + Math.random().toString(36).slice(2,7); }

/* ====== Toestand per deelnemer ====== */
var st, resetTimer = null;
function nieuw(){
  st = { antwoorden:[], score:0, naam:"", email:"", tel:"", gemeente:"", kinderen:[""], interesses:[], schifting:"", toestemming:false, kamp:KAMPVRAGEN.map(function(){ return []; }) };
}

/* ====== Schermen ====== */
function start(){
  clearTimeout(resetTimer);
  nieuw();
  S.className = "kaart hero";
  toon([
    el("div",{klasse:"emoji",tekst:"🧪"}),
    el("h1",{tekst:"Speel mee en win " + PRIJS + "!"}),
    el("p",{klasse:"groot",tekst:VRAGEN.length + " wetenschapsvragen en " + KAMPVRAGEN.length + " vragen over kampen en hobby's. Klaar in 3 minuten."}),
    el("div",{klasse:"rij",style:"justify-content:center;margin-top:18px"},[
      el("button",{klasse:"knop oranje",tekst:"Start de quiz",klik:function(){ vraag(0); }})
    ]),
    el("p",{klasse:"klein-tekst",style:"margin-top:26px",tekst:"Weet je het antwoord niet? Zoek het samen met je kind op onze posters!"})
  ]);
}

function vraag(i){
  S.className = "kaart";
  var q = VRAGEN[i];
  var uitleg = el("div",{klasse:"uitleg verborgen"});
  var verder = el("button",{klasse:"knop verborgen",tekst: i < VRAGEN.length-1 ? "Volgende vraag" : "Bijna klaar",klik:function(){
    if(i < VRAGEN.length-1) vraag(i+1); else kampIntro();
  }});
  var knoppen = q.o.map(function(t, k){
    return el("button",{klasse:"optie",tekst:t,klik:function(){
      knoppen.forEach(function(b, n){
        b.disabled = true;
        if(n === q.j) b.classList.add("juist");
        else if(n === k) b.classList.add("fout");
      });
      var goed = (k === q.j);
      st.antwoorden[i] = q.o[k];
      if(goed) st.score++;
      uitleg.textContent = (goed ? "Juist! " : "Bijna! ") + q.u;
      uitleg.classList.remove("verborgen");
      verder.classList.remove("verborgen");
    }});
  });
  toon([
    el("div",{klasse:"voortgang"},[el("div",{style:"width:"+Math.round((i)/(VRAGEN.length+KAMPVRAGEN.length+2)*100)+"%"})]),
    el("div",{klasse:"badge",tekst:"Vraag " + (i+1) + " van " + VRAGEN.length}),
    el("h2",{tekst:q.v}),
    el("div",{klasse:"opties"},knoppen),
    uitleg,
    el("div",{klasse:"onder"},[
      el("button",{klasse:"knop licht klein",tekst:"Opnieuw beginnen",klik:start}),
      verder
    ])
  ]);
}

function kampIntro(){
  S.className = "kaart hero";
  toon([
    el("div",{klasse:"emoji",tekst:"🏕️"}),
    el("div",{klasse:"badge",tekst:"Je had er " + st.score + " van de " + VRAGEN.length + " juist!"}),
    el("h1",{tekst:"Nu nog 4 snelle vragen over kampen en hobby's"}),
    el("p",{klasse:"groot",tekst:"Hier is er geen juist of fout. Zo weten wij welke kampen en hobby's jullie graag zouden zien."}),
    el("div",{klasse:"rij",style:"justify-content:center;margin-top:18px"},[
      el("button",{klasse:"knop oranje",tekst:"Verder",klik:function(){ kampvraag(0); }})
    ])
  ]);
}

function kampvraag(i){
  S.className = "kaart";
  var q = KAMPVRAGEN[i];
  var gekozen = st.kamp[i];
  var stap = VRAGEN.length + i;
  var chips = q.o.map(function(t){
    var c = el("button",{type:"button",klasse:"chip" + (gekozen.indexOf(t) > -1 ? " aan" : ""),tekst:t,klik:function(){
      var p = gekozen.indexOf(t);
      if(p > -1){ gekozen.splice(p,1); c.classList.remove("aan"); }
      else { gekozen.push(t); c.classList.add("aan"); }
    }});
    return c;
  });
  toon([
    el("div",{klasse:"voortgang"},[el("div",{style:"width:"+Math.round(stap/(VRAGEN.length+KAMPVRAGEN.length+2)*100)+"%"})]),
    el("div",{klasse:"badge",tekst:"Vraag over kampen en hobby's " + (i+1) + " van " + KAMPVRAGEN.length}),
    el("h2",{tekst:q.v}),
    el("p",{klasse:"klein-tekst",tekst:"Tik alles aan wat past. Meerdere keuzes mogen."}),
    el("div",{klasse:"chips"},chips),
    el("div",{klasse:"onder"},[
      el("button",{klasse:"knop licht klein",tekst:"Opnieuw beginnen",klik:start}),
      el("button",{klasse:"knop",tekst: i < KAMPVRAGEN.length-1 ? "Volgende vraag" : "Verder",klik:function(){
        if(i < KAMPVRAGEN.length-1) kampvraag(i+1); else schiftingScherm();
      }})
    ])
  ]);
}

function schiftingScherm(){
  var inp = el("input",{type:"number",inputmode:"numeric",min:"0",placeholder:"Jouw schatting"});
  inp.value = st.schifting;
  var fout = el("div",{klasse:"fout-tekst"});
  toon([
    el("div",{klasse:"voortgang"},[el("div",{style:"width:"+Math.round((VRAGEN.length+KAMPVRAGEN.length)/(VRAGEN.length+KAMPVRAGEN.length+2)*100)+"%"})]),
    el("div",{klasse:"badge",tekst:"Bijna klaar!"}),
    el("h2",{tekst:SCHIFTING}),
    el("p",{tekst:"Bij een gelijke stand wint wie het dichtst bij het echte aantal zit."}),
    inp, fout,
    el("div",{klasse:"onder"},[
      el("button",{klasse:"knop licht klein",tekst:"Opnieuw beginnen",klik:start}),
      el("button",{klasse:"knop",tekst:"Naar je gegevens",klik:function(){
        var w = inp.value.trim();
        if(w === "" || isNaN(Number(w)) || Number(w) < 0){ fout.textContent = "Vul een getal in."; return; }
        st.schifting = String(Math.round(Number(w)));
        gegevens();
      }})
    ])
  ]);
}

function gegevens(){
  var naam = el("input",{type:"text",autocomplete:"name",placeholder:"Voornaam en naam"}); naam.value = st.naam;
  var email = el("input",{type:"email",autocomplete:"email",autocapitalize:"off",placeholder:"naam@voorbeeld.be"}); email.value = st.email;
  var tel = el("input",{type:"tel",autocomplete:"tel",placeholder:"04.. .. .. .."}); tel.value = st.tel;
  var gem = el("input",{type:"text",placeholder:"Bijvoorbeeld Hasselt"}); gem.value = st.gemeente;
  var fout = el("div",{klasse:"fout-tekst"});

  var kinderVak = el("div");
  var aantal = el("b",{tekst:String(st.kinderen.length)});
  function tekenKinderen(){
    aantal.textContent = String(st.kinderen.length);
    kinderVak.innerHTML = "";
    st.kinderen.forEach(function(lft, n){
      var s = el("select");
      s.appendChild(el("option",{value:"",tekst:"Kies leeftijd"}));
      LEEFTIJDEN.forEach(function(L){ var o = el("option",{value:L,tekst:L}); if(L === lft) o.selected = true; s.appendChild(o); });
      s.addEventListener("change", function(){ st.kinderen[n] = s.value; });
      kinderVak.appendChild(el("div",{klasse:"kind"},[el("span",{tekst:"Kind " + (n+1)}), s]));
    });
  }
  tekenKinderen();

  var chips = INTERESSES.map(function(t){
    var c = el("button",{type:"button",klasse:"chip" + (st.interesses.indexOf(t) > -1 ? " aan" : ""),tekst:t,klik:function(){
      var p = st.interesses.indexOf(t);
      if(p > -1){ st.interesses.splice(p,1); c.classList.remove("aan"); }
      else { st.interesses.push(t); c.classList.add("aan"); }
    }});
    return c;
  });

  var vinkInp = el("input",{type:"checkbox",id:"toestemming"}); vinkInp.checked = st.toestemming;
  var vink = el("label",{klasse:"vink","for":"toestemming"},[
    vinkInp,
    el("div",{},[
      el("b",{tekst:"Ik doe mee aan de wedstrijd en ga akkoord (verplicht). "}),
      "Connectopia vzw mag mijn gegevens gebruiken om mij te contacteren als ik win en om mij info te sturen over activiteiten van Connectopia. Ik kan dit altijd stopzetten en mijn gegevens laten wissen via " + CONTACT + ". We geven je gegevens nooit aan anderen."
    ])
  ]);

  function bewaarVelden(){
    st.naam = naam.value.trim(); st.email = email.value.trim(); st.tel = tel.value.trim();
    st.gemeente = gem.value.trim(); st.toestemming = vinkInp.checked;
  }

  toon([
    el("div",{klasse:"voortgang"},[el("div",{style:"width:"+Math.round((VRAGEN.length+KAMPVRAGEN.length+1)/(VRAGEN.length+KAMPVRAGEN.length+2)*100)+"%"})]),
    el("h2",{tekst:"Laatste stap: hoe kunnen we je bereiken als je wint?"}),
    el("label",{klasse:"veld",tekst:"Naam ouder"}), naam,
    el("label",{klasse:"veld",tekst:"E-mailadres"}), email,
    el("label",{klasse:"veld",tekst:"Telefoonnummer"}), tel,
    el("label",{klasse:"veld",tekst:"Gemeente (mag je leeg laten)"}), gem,
    el("label",{klasse:"veld",tekst:"Hoeveel kinderen heb je?"}),
    el("div",{klasse:"stepper"},[
      el("button",{type:"button",klasse:"knop licht klein",tekst:"−",klik:function(){ if(st.kinderen.length>1){ st.kinderen.pop(); tekenKinderen(); } }}),
      aantal,
      el("button",{type:"button",klasse:"knop licht klein",tekst:"+",klik:function(){ if(st.kinderen.length<8){ st.kinderen.push(""); tekenKinderen(); } }})
    ]),
    kinderVak,
    el("label",{klasse:"veld",tekst:"Waar heb je interesse in? (meerdere mag)"}),
    el("div",{klasse:"chips"},chips),
    vink,
    fout,
    el("div",{klasse:"onder"},[
      el("button",{klasse:"knop licht klein",tekst:"Opnieuw beginnen",klik:start}),
      el("button",{klasse:"knop oranje",tekst:"Verstuur en doe mee",klik:function(){
        bewaarVelden();
        var f = [];
        if(st.naam.length < 2) f.push("je naam");
        if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(st.email)) f.push("een geldig e-mailadres");
        if(st.tel.replace(/[^0-9]/g,"").length < 9) f.push("je telefoonnummer");
        if(st.kinderen.some(function(k){ return !k; })) f.push("de leeftijd van elk kind");
        if(!st.toestemming) f.push("het vinkje voor de wedstrijd");
        if(f.length){ fout.textContent = "Vul nog in: " + f.join(", ") + "."; return; }
        opslaan();
      }})
    ])
  ]);
}

function opslaan(){
  var nu = new Date();
  var rec = {
    id: stip(),
    tijdstip: nu.toISOString(),
    datum: nu.toLocaleString("nl-BE"),
    naam: st.naam, email: st.email, telefoon: st.tel, gemeente: st.gemeente,
    aantalKinderen: st.kinderen.length, leeftijden: st.kinderen.join(", "),
    interesses: st.interesses.join(", "),
    score: st.score + "/" + VRAGEN.length,
    antwoorden: st.antwoorden.join(" | "),
    schifting: st.schifting,
    kampSoort: st.kamp[0].join("; "),
    kampVakantie: st.kamp[1].join("; "),
    kampVorm: st.kamp[2].join("; "),
    kampBelangrijk: st.kamp[3].join("; "),
    toestemming: "ja"
  };
  var lijst = leesLokaal(); lijst.push(rec); schrijfLokaal(lijst);
  synchroniseer();
  bedankt();
}

function confetti(){
  var kleuren = ["#2f8f6b","#f39a2b","#ffd45c","#5bb6e6","#e86aa6"];
  for(var i=0;i<60;i++){
    var c = document.createElement("div");
    c.className = "confetti";
    c.style.left = Math.random()*100 + "vw";
    c.style.background = kleuren[i % kleuren.length];
    c.style.animationDelay = (Math.random()*0.8) + "s";
    document.body.appendChild(c);
    (function(n){ setTimeout(function(){ n.remove(); }, 3800); })(c);
  }
}

function bedankt(){
  S.className = "kaart hero";
  var sec = 25;
  var teller = el("p",{klasse:"klein-tekst"});
  function tik(){
    teller.textContent = "Dit scherm gaat over " + sec + " seconden vanzelf terug naar het begin.";
    if(sec-- <= 0){ start(); return; }
    resetTimer = setTimeout(tik, 1000);
  }
  toon([
    el("div",{klasse:"emoji",tekst:"🎉"}),
    el("h1",{tekst:"Dankjewel " + st.naam.split(" ")[0] + ", je doet mee!"}),
    el("div",{klasse:"score",tekst:st.score + "/" + VRAGEN.length}),
    el("p",{klasse:"groot",tekst: st.score === VRAGEN.length ? "Alles juist, echte wetenschappers!" : "Goed gedaan, wetenschap is samen ontdekken!"}),
    el("p",{tekst:"Maak je kans op " + PRIJS + ". Als je wint, nemen we persoonlijk contact met je op."}),
    el("p",{tekst:"Meer weten? Kijk op www.connectopia.one of mail naar " + CONTACT + "."}),
    el("div",{klasse:"rij",style:"justify-content:center;margin-top:10px"},[
      el("button",{klasse:"knop",tekst:"Volgende ouder",klik:start})
    ]),
    teller
  ]);
  confetti();
  tik();
}

/* ====== Beheer (5 keer tikken rechtsonder) ====== */
var tikken = 0, tikTimer = null;
document.getElementById("geheim").addEventListener("click", function(){
  tikken++; clearTimeout(tikTimer);
  tikTimer = setTimeout(function(){ tikken = 0; }, 1500);
  if(tikken >= 5){ tikken = 0; pinScherm(); }
});

function pinScherm(){
  clearTimeout(resetTimer);
  S.className = "kaart";
  var p = el("input",{type:"password",inputmode:"numeric",placeholder:"Pincode"});
  var fout = el("div",{klasse:"fout-tekst"});
  toon([
    el("h2",{tekst:"Beheer"}),
    el("p",{tekst:"Geef de pincode om de deelnemers te bekijken."}),
    p, fout,
    el("div",{klasse:"onder"},[
      el("button",{klasse:"knop licht klein",tekst:"Terug",klik:start}),
      el("button",{klasse:"knop",tekst:"Open",klik:function(){ if(p.value === PINCODE) beheer(); else fout.textContent = "Verkeerde pincode."; }})
    ])
  ]);
  p.focus();
}

var KOLOMMEN = [["datum","Datum"],["naam","Naam"],["email","E-mail"],["telefoon","Telefoon"],["gemeente","Gemeente"],["aantalKinderen","Aantal kinderen"],["leeftijden","Leeftijden"],["interesses","Interesses"],["score","Score"],["schifting","Schifting"],["antwoorden","Antwoorden"],["kampSoort","Soort kamp of hobby"],["kampVakantie","Vakantie"],["kampVorm","Kampvorm"],["kampBelangrijk","Belangrijk"],["toestemming","Toestemming"]];
function csv(lijst){
  function cel(v){ v = String(v == null ? "" : v); return /[";\n]/.test(v) ? '"' + v.replace(/"/g,'""') + '"' : v; }
  var r = [KOLOMMEN.map(function(k){ return k[1]; }).join(";")];
  lijst.forEach(function(x){ r.push(KOLOMMEN.map(function(k){ return cel(x[k[0]]); }).join(";")); });
  return r.join("\n");
}
function kopieer(tekst, melding, vak){
  vak.value = tekst; vak.classList.remove("verborgen");
  function handmatig(){ vak.focus(); vak.select(); melding.textContent = "Tekst staat hieronder geselecteerd: tik op Kopieer of houd ingedrukt."; }
  try{
    navigator.clipboard.writeText(tekst).then(function(){ melding.textContent = "Gekopieerd! Plak het in een mail of in Excel."; }, handmatig);
  }catch(e){ handmatig(); }
}

function beheer(){
  S.className = "kaart";
  var lijst = leesLokaal();
  var online = lijst.filter(function(x){ return x._online; }).length;
  var melding = el("div",{klasse:"melding"});
  var vak = el("textarea",{klasse:"verborgen",readonly:"readonly"});
  var tabel = el("table");
  var kop = el("tr"); ["Datum","Naam","E-mail","Telefoon","Kinderen","Interesses","Score","Schifting"].forEach(function(t){ kop.appendChild(el("th",{tekst:t})); });
  tabel.appendChild(kop);
  lijst.slice().reverse().forEach(function(x){
    var r = el("tr");
    [x.datum,x.naam,x.email,x.telefoon,x.leeftijden,x.interesses,x.score,x.schifting].forEach(function(t){ r.appendChild(el("td",{tekst:t})); });
    tabel.appendChild(r);
  });
  var wisVak = el("div",{klasse:"verborgen uitleg"},[
    el("p",{tekst:"Zeker dat je alle deelnemers van dit toestel wil wissen? Kopieer de lijst eerst!"}),
    el("div",{klasse:"rij"},[
      el("button",{klasse:"knop klein",style:"background:#d9534f;box-shadow:0 4px 0 #a33b38",tekst:"Ja, wis alles",klik:function(){ schrijfLokaal([]); beheer(); }}),
      el("button",{klasse:"knop licht klein",tekst:"Nee",klik:function(){ wisVak.classList.add("verborgen"); }})
    ])
  ]);
  toon([
    el("h2",{tekst:"Deelnemers: " + lijst.length}),
    el("p",{klasse:"klein-tekst",tekst:"Doorgestuurd naar de aanvragen in het beheer: " + online + " van " + lijst.length + ". " + (online < lijst.length ? "De rest wordt vanzelf doorgestuurd zodra er internet is." : "Alles is binnen.")}),
    el("div",{klasse:"rij"},[
      el("button",{klasse:"knop klein",tekst:"Kopieer voor Excel",klik:function(){ kopieer(csv(lijst), melding, vak); }}),
      el("button",{klasse:"knop licht klein",tekst:"Kopieer e-mailadressen",klik:function(){ kopieer(lijst.map(function(x){ return x.email; }).join("; "), melding, vak); }}),
      el("button",{klasse:"knop licht klein",tekst:"Wis lijst",klik:function(){ wisVak.classList.remove("verborgen"); }})
    ]),
    melding, vak, wisVak,
    el("div",{klasse:"tabelvak"},[tabel]),
    el("div",{klasse:"onder"},[
      el("button",{klasse:"knop",tekst:"Terug naar de quiz",klik:start})
    ])
  ]);
}

synchroniseer();
start();
})();
</script>
</body>
</html>
`;
