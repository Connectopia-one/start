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

| bundel | hoort bij | blz. |
| --- | --- | --- |
| `wiskunde/oefenbundel-rekenen-en-breuken.pdf` | Wiskunde 🌱 Start — Rekenen en breuken | 4 + 1 antwoordblad |

Dat is het gratis proefhoofdstuk, met opzet: het is het enige stuk leerstof dat
iemand zonder account ziet.

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
python3 maak_oefeningen_rekenen.py
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
