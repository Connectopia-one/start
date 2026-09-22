# -*- coding: utf-8 -*-
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg

CSS = pathlib.Path(__file__).parent.joinpath("stijl.css").read_text(encoding="utf-8")

plaatswaarde = """
<table style="width:100%;border-collapse:collapse;font-family:'IBM Plex Sans',sans-serif;font-size:10.5pt;">
  <tr>
    <th style="border:1px solid #e4ded0;background:rgba(47,93,80,.09);padding:6px 4px;color:#234539;font-weight:600;">miljoen</th>
    <th style="border:1px solid #e4ded0;background:rgba(47,93,80,.09);padding:6px 4px;color:#234539;font-weight:600;">honderd&shy;duizend</th>
    <th style="border:1px solid #e4ded0;background:rgba(47,93,80,.09);padding:6px 4px;color:#234539;font-weight:600;">tien&shy;duizend</th>
    <th style="border:1px solid #e4ded0;background:rgba(47,93,80,.09);padding:6px 4px;color:#234539;font-weight:600;">duizend</th>
    <th style="border:1px solid #e4ded0;background:rgba(47,93,80,.09);padding:6px 4px;color:#234539;font-weight:600;">honderd</th>
    <th style="border:1px solid #e4ded0;background:rgba(47,93,80,.09);padding:6px 4px;color:#234539;font-weight:600;">tien</th>
    <th style="border:1px solid #e4ded0;background:rgba(47,93,80,.09);padding:6px 4px;color:#234539;font-weight:600;">een</th>
  </tr>
  <tr>
    <td style="border:1px solid #e4ded0;padding:9px 4px;text-align:center;font-size:15pt;font-weight:600;color:#23291f;">2</td>
    <td style="border:1px solid #e4ded0;padding:9px 4px;text-align:center;font-size:15pt;font-weight:600;color:#c17f2b;">6</td>
    <td style="border:1px solid #e4ded0;padding:9px 4px;text-align:center;font-size:15pt;font-weight:600;color:#23291f;">4</td>
    <td style="border:1px solid #e4ded0;padding:9px 4px;text-align:center;font-size:15pt;font-weight:600;color:#23291f;">5</td>
    <td style="border:1px solid #e4ded0;padding:9px 4px;text-align:center;font-size:15pt;font-weight:600;color:#23291f;">1</td>
    <td style="border:1px solid #e4ded0;padding:9px 4px;text-align:center;font-size:15pt;font-weight:600;color:#23291f;">3</td>
    <td style="border:1px solid #e4ded0;padding:9px 4px;text-align:center;font-size:15pt;font-weight:600;color:#23291f;">0</td>
  </tr>
</table>
"""

afrond_lijn = svg.getallenlijn(470, 3700, 3800, [
    (3700, "3 700", svg.INK, False),
    (3750, "helft", svg.DIM, False),
    (3800, "3 800", svg.INK, False),
    (3748, "3 748", svg.AMBER, True),
])

komma_lijn = svg.getallenlijn(470, 4.0, 5.0, [
    (4.0, "4", svg.INK, False),
    (4.2, "4,2", svg.DIM, False),
    (4.3, "4,3", svg.AMBER, True),
    (4.4, "4,4", svg.DIM, False),
    (5.0, "5", svg.INK, False),
])

negatief_lijn = svg.getallenlijn(470, -10, 10, [
    (-10, "-10", svg.INK, False),
    (-8, "-8", "#a6432f", True),
    (-5, "-5", "#a6432f", True),
    (0, "0", svg.INK, False),
    (5, "5", svg.FOREST, False),
    (10, "10", svg.INK, False),
])

HTML = f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>Leerbundel — Getallenkennis</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=IBM+Plex+Sans:wght@400;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<div class="kop">
  <div class="vak">Wiskunde · 🌱 Start — 5de en 6de leerjaar</div>
  <h1>Getallenkennis</h1>
  <p class="onder">Wat getallen betekenen, hoe je ze leest en hoe je ze met elkaar vergelijkt.</p>
</div>

<section>
  <h2><span class="nr">1</span> Grote getallen lezen</h2>
  <p>Elk cijfer in een getal heeft een eigen plaats, en die plaats bepaalt hoeveel het cijfer waard is. Een 6 vooraan is veel meer waard dan een 6 achteraan.</p>
  <figure>
    {plaatswaarde}
    <figcaption>In 2 645 130 staat de 6 op de plaats van de honderdduizendtallen. Die 6 is dus 600 000 waard.</figcaption>
  </figure>
  <p>Je leest zo'n getal van links naar rechts, in groepjes van drie: <strong>twee miljoen — zeshonderdvijfenveertigduizend — honderddertig</strong>. Daarom laten we telkens een spatie tussen de groepjes.</p>
  <div class="weetje"><b>💡 Weetje.</b> Die spatie is geen punt en geen komma. In het Engels schrijven ze wel een komma (2,645,130), en in een rekenmachine staat er soms niets tussen. Hetzelfde getal, een andere gewoonte.</div>
</section>

<section>
  <h2><span class="nr">2</span> Afronden</h2>
  <p>Afronden is een getal vervangen door een rond getal dat er dicht bij ligt. Je kijkt naar het cijfer <em>rechts</em> van de plaats waarop je afrondt: is dat 5 of meer, dan ga je naar boven; is het minder dan 5, dan blijf je beneden.</p>
  <figure>
    {afrond_lijn}
    <figcaption>3 748 afgerond op honderdtallen wordt 3 700: het ligt links van de helft.</figcaption>
  </figure>
  <p>Op de getallenlijn zie je meteen waarom. 3 748 ligt tussen 3 700 en 3 800, maar nog net voor de helft. Afronden op duizendtallen geeft 4 000, want dan kijk je naar de 7.</p>
</section>

<section>
  <h2><span class="nr">3</span> Kommagetallen</h2>
  <p>Achter de komma gaat het tellen gewoon verder, maar in stukjes: tienden, honderdsten, duizendsten. <strong>0,7 is groter dan 0,65</strong>, want 0,7 is hetzelfde als 0,70.</p>
  <figure>
    {komma_lijn}
    <figcaption>Tussen 4,2 en 4,4 ligt 4,3 precies in het midden.</figcaption>
  </figure>
  <p>Vergelijk je twee kommagetallen, vul dan eerst aan met nullen tot ze evenveel cijfers achter de komma hebben. Dan lees je ze even makkelijk als gewone getallen.</p>
  <div class="weetje"><b>💡 Weetje.</b> Maal 10 schuift de komma één plaats naar rechts, delen door 10 één plaats naar links. 7,5 × 100 wordt dus 750.</div>
</section>

<section>
  <h2><span class="nr">4</span> Breuken</h2>
  <p>Een breuk is een geheel dat in gelijke stukken verdeeld is. Het onderste getal (de <strong>noemer</strong>) zegt in hoeveel stukken, het bovenste (de <strong>teller</strong>) hoeveel stukken je neemt.</p>
  <figure>
    {svg.breukstroken(470)}
    <figcaption>Hoe groter de noemer, hoe kleiner elk stukje. 1/5 is dus kleiner dan 1/3.</figcaption>
  </figure>
  <p>Staat boven en onder hetzelfde getal, dan heb je het hele ding: 4/4 is 1. En breuken die er anders uitzien kunnen evenveel waard zijn: 2/4 is hetzelfde als 1/2.</p>
</section>

<section>
  <h2><span class="nr">5</span> Procent</h2>
  <p>Procent betekent <em>per honderd</em>. 25% is dus 25 van de 100, of één vierde van het geheel.</p>
  <figure>
    {svg.procentraster(25, 215)}
    <figcaption>25 van de 100 vakjes gekleurd: dat is 25%, of 1/4.</figcaption>
  </figure>
  <p>Handige ankerpunten om vanuit te rekenen: 10% is delen door 10, 50% is de helft, 25% is een vierde. Wil je 20% van 250 weten, neem dan 10% (= 25) en verdubbel dat: 50.</p>
</section>

<section>
  <h2><span class="nr">6</span> Negatieve getallen</h2>
  <p>Links van de nul gaan de getallen verder met een minteken. Denk aan de temperatuur in de winter, of aan verdiepingen onder de grond.</p>
  <figure>
    {negatief_lijn}
    <figcaption>-5 ligt dichter bij nul dan -8, en is dus groter.</figcaption>
  </figure>
  <p>Dat is het stukje dat vaak verwart: bij negatieve getallen is het getal dat er het <em>grootst</em> uitziet, net het kleinste. -10 is kouder dan -3.</p>
</section>

<section>
  <h2><span class="nr">7</span> Deelbaarheid en priemgetallen</h2>
  <p>Je kan aan een getal zien of het deelbaar is, zonder te rekenen:</p>
  <div class="kader">
    <p style="margin:0 0 4px"><strong>Door 2</strong> — als het eindigt op 0, 2, 4, 6 of 8.</p>
    <p style="margin:0 0 4px"><strong>Door 5</strong> — als het eindigt op 0 of 5.</p>
    <p style="margin:0 0 4px"><strong>Door 3</strong> — tel de cijfers op; is die som deelbaar door 3, dan het hele getal ook. (471 → 4+7+1 = 12 → ja)</p>
    <p style="margin:0"><strong>Door 9</strong> — net hetzelfde, maar de som moet deelbaar zijn door 9.</p>
  </div>
  <p>Een <strong>priemgetal</strong> heeft precies twee delers: 1 en zichzelf. 2, 3, 5, 7, 11 en 13 zijn priemgetallen. Het getal 1 niet, want dat heeft er maar één.</p>
</section>

<div class="onthoud">
  <h2>Onthoud dit</h2>
  <ul>
    <li>De plaats van een cijfer bepaalt zijn waarde.</li>
    <li>Afronden: kijk naar het cijfer rechts ervan. 5 of meer gaat naar boven.</li>
    <li>0,7 is hetzelfde als 0,70 — vul aan met nullen voor je vergelijkt.</li>
    <li>Hoe groter de noemer, hoe kleiner het stukje.</li>
    <li>Procent is per honderd. 10% is delen door 10.</li>
    <li>Bij negatieve getallen is het grootst uitziende getal het kleinste.</li>
  </ul>
</div>

<div class="voet">
  <span>Connectopia vzw · oefenplatform.connectopia.one</span>
  <span>Leerbundel — Wiskunde, Getallenkennis</span>
</div>

</body>
</html>
"""

pathlib.Path(__file__).parent.joinpath("getallenkennis.html").write_text(HTML, encoding="utf-8")
print("html geschreven")
