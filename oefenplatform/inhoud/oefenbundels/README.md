# Oefenbundels (pdf) bij de hoofdstukken

Waar een leerbundel de theorie geeft, geeft een oefenbundel oefeningen om op
papier te maken: plaats om te schrijven, doorlopend genummerd, en achteraan een
antwoordblad op een eigen blad dat je eraf scheurt voor je de bundel aan een
kind geeft.

**De oefeningen zijn andere vragen dan die van het hoofdstuk op het scherm.**
Dezelfde leerstof en dezelfde woorden, maar andere getallen en andere
situaties. Wie de bundel invult en daarna online oefent, moet dus twee keer
nadenken. Kijk voor je iets bijschrijft het vragenbestand van het hoofdstuk na,
bijvoorbeeld `inhoud/start/wiskunde-rekenen-en-breuken.json`.

## Wat er klaar is

**🌱 Start en ✨ Spark zijn allebei volledig: 79 bundels, 1 275 oefeningen.**

Op 🌱 Start is er één bundel per hoofdstuk. Op ✨ Spark is er één bundel per
**thema**: deel 1 en deel 2 behandelen dezelfde leerstof, alleen met
moeilijkere vragen, dus dezelfde pdf gaat bij allebei. Net als bij de
leerbundels. De twee hoofdstukken begrijpend lezen staan wél los en hebben elk
hun eigen bundel.

| 🌱 Start | bundels | oefeningen | | ✨ Spark | bundels | oefeningen |
| --- | --- | --- | --- | --- | --- | --- |
| Wiskunde | 7 | 153 | | Wiskunde | 9 | 181 |
| Wetenschap en techniek | 7 | 112 | | Natuurwetenschappen | 10 | 162 |
| Engels | 6 | 99 | | Nederlands | 12 | 150 |
| Nederlands | 6 | 95 | | Frans | 10 | 118 |
| Geschiedenis | 3 | 43 | | Geschiedenis | 6 | 119 |
| Aardrijkskunde | 3 | 43 | | | | |
| **samen** | **32** | **545** | | **samen** | **47** | **730** |

Frans op ✨ Spark dekt **enkel de schriftelijke onderdelen**, net als de vragen
op het scherm.

Per vak en per categorie staat er een zip (`wiskunde-start.zip`,
`wiskunde-spark.zip`, `frans-spark.zip` …) en er is er één met alles erin
(`alle-oefenbundels.zip`). In allebei zit per vak een map, dus je kan er twee
naast elkaar uitpakken zonder dat de bestanden door elkaar lopen.

Waarom per categorie en niet enkel per vak: wie ✨ Spark aan het opladen is,
wil de bundels van 🌱 Start er niet bij, want die staan er al. `maak_zips.py`
haalt de categorie uit de bundel zelf, niet uit de bestandsnaam.

## Wat per vak anders is

**Taalvakken.** Het invulvakje staat breder dan bij wiskunde: "Wednesday" past
niet in een vakje dat voor een getal van twee cijfers gemaakt is. Dat zet je
per oefening met een vierde waarde bij `rij` of `kort`, bijvoorbeeld `"120px"`.

**Nederlands, lezen.** Er staat een eigen tekstje in de bundel met vragen die
alleen over die tekst gaan. Een leesvraag hoort op een echte tekst te staan en
niet op het begrip alleen.

**Nederlands, spelling.** Dat hoofdstuk heet in de databank "Hoofdstuk 1 —
Spelling: voorbeeld". Het raden op de bestandsnaam kan daar dus misgaan; kies
het hoofdstuk in dat geval zelf in het lijstje bij het uploaden.

**Wetenschap en techniek.** Hier staan tekenopdrachten in: een voedselketen,
een stroomkring, de maanstanden. Dat soort werk kan op papier en niet op een
scherm. Die bundels zijn daardoor vijf blad in plaats van vier.

**Aardrijkskunde.** Er staat bewust geen landkaart in om na te tekenen. Een
kaart uit het hoofd getekend klopt niet, en een kind mag geen foute vorm
inprenten. De tekenopdrachten gaan over een kompasroos en een legende.

**Alles van ✨ Spark.** De bestandsnaam eindigt op `-spark`. Dat is geen
versiering: Beheer → Leerstof leest die categorie en zoekt dan enkel in de
hoofdstukken van ✨ Spark. Zonder dat won "Meetkunde" van 🌱 Start het van
"Meetkunde — deel 1" van Spark, want het woord "deel" staat nooit in een
bestandsnaam en kostte de Spark-hoofdstukken punten. Geef een nieuwe
Spark-bundel dus altijd die uitgang.

**Natuurwetenschappen ✨ Spark.** Hier staan geen figuren uit `svg.py` in. Die
tekeningen dragen hun namen mee, en dat verklapt in een oefenbundel net het
antwoord. Wat getekend moet worden, tekent het kind zelf in een leeg kader.

**Nederlands en Frans, begrijpend lezen.** Die bundels dragen hun eigen tekst
mee, een andere dan die op het scherm, met vragen die alleen daarover gaan.
Een leesvraag hoort op een echte tekst te staan, en bij Frans op een echte
Franse tekst.

## Twee afspraken van Kim, 27 september 2026

**Breuken met een echte streep**, teller boven noemer, nooit met een schuine
streep: `bundel.breuk(3, 4)`, opgemaakt door `.breuk` in `stijl.css`. Een
schuine streep leest voor een kind niet als een breuk.

**Ruim plaats om te schrijven.** Veel van deze kinderen zijn motorisch minder
sterk en schrijven groter, dus de invulvakjes, de schrijflijnen en de
regelafstand zijn bewust royaal. Maak ze niet kleiner om een blad te sparen.

## Een oefenbundel maken

De beschrijving staat in `../leerbundels/bron/maak_oefeningen_*.py`, in een dict
`OEFENBUNDELS`. `../leerbundels/bron/oefenbundel.py` maakt er html van en zet
de opmaak in `../leerbundels/bron/oefen.css`, bovenop de gewone `stijl.css`, zodat
een oefenbundel er hetzelfde uitziet als een leerbundel.

De soorten oefeningen staan bovenaan `oefenbundel.py`: een korte som, een rij
sommen met letters, een rij tekeningen, een open vraag met schrijflijnen, een
keuzevraag, waar of niet waar, en een tabel om aan te vullen. Zet `{aantal}` in
de ondertitel en het echte aantal oefeningen komt er vanzelf in te staan.

Bouwen en nakijken, vanuit `../leerbundels/bron`:

```
python3 maak_oefeningen_wiskunde.py
node controle.js oefenbundel-rekenen-en-breuken
node pdf.js oefenbundel-rekenen-en-breuken
```

`python3 maak_alles.py wiskunde` doet hetzelfde voor alle bundels van een vak en
zet elke pdf meteen op zijn plaats.

## Hoe een bundel bij een hoofdstuk raakt

Net als een leerbundel: op `/beheer/leerstof` kies je het vak en sleep je de
pdf erin. De bestandsnaam begint met `oefenbundel-` en daarna de naam van het
hoofdstuk, zodat het platform zelf het juiste hoofdstuk vindt en het kind
"Oefenbundel rekenen en breuken" ziet staan naast de leerbundel.

Het vinkje **vervangen** staat alleen aan als er al iets met dezelfde titel bij
dat hoofdstuk hangt. Een oefenbundel komt dus naast de leerbundel te staan en
wist die niet.
