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

**Wiskunde 🌱 Start is volledig**, zeven bundels, één per hoofdstuk:

| bundel | hoort bij |
| --- | --- |
| `wiskunde/oefenbundel-rekenen-en-breuken.pdf` | Rekenen en breuken (het gratis proefhoofdstuk) |
| `wiskunde/oefenbundel-getallenkennis.pdf` | Getallenkennis |
| `wiskunde/oefenbundel-bewerkingen.pdf` | Bewerkingen |
| `wiskunde/oefenbundel-meten-en-metend-rekenen.pdf` | Meten en metend rekenen |
| `wiskunde/oefenbundel-meetkunde.pdf` | Meetkunde |
| `wiskunde/oefenbundel-kansrekenen-en-statistiek.pdf` | Kansrekenen en statistiek |
| `wiskunde/oefenbundel-vraagstukken-en-problemen-oplossen.pdf` | Vraagstukken en problemen oplossen |

**Engels 🌱 Start is volledig**, zes bundels, één per hoofdstuk: woorden voor
elke dag, mezelf voorstellen, to be en to have, de tegenwoordige tijd, zinnen
bouwen, op school en onderweg. Samen 99 oefeningen.

Bij een taalvak staat het invulvakje breder dan bij wiskunde: "Wednesday" past
niet in een vakje dat voor een getal van twee cijfers gemaakt is. Dat zet je per
oefening met een vierde waarde bij `rij` of `kort`, bijvoorbeeld `"120px"`.

Er staat een zip **per vak** (`wiskunde.zip`, `engels.zip`) en één met alles
erin (`alle-oefenbundels.zip`). In allebei zit per vak een map, dus je kan er
twee naast elkaar uitpakken zonder dat de bestanden door elkaar lopen.

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
