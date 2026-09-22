# Leerbundels (pdf) bij de hoofdstukken

Hier staat per vak een map met de leerbundels: de theorie bij een hoofdstuk, met
tekeningen erbij, als pdf klaar om te uploaden.

De bestandsnaam is telkens de naam van het hoofdstuk, bijvoorbeeld
`getallenkennis.pdf`. Dat is geen toeval: op `/beheer/leerstof` kies je een vak,
sleep je alle pdf's er tegelijk in, en zoekt het platform op basis van die naam
zelf het juiste hoofdstuk erbij.

## Echte foto's in een bundel

Naast de tekeningen kan er ook echt beeldmateriaal in, met `bundel.foto(...)`.
Dat zet het bestand als base64 in de html, zodat de pdf achteraf nergens meer
naar hoeft te zoeken. Geef altijd een bronvermelding mee bij beeld dat niet van
Connectopia zelf is:

```python
("fig", bundel.foto("fotos/colosseum.jpg", bron="Foto: naam, CC BY-SA 4.0"),
 "Het Colosseum in Rome, gebouwd rond het jaar 80.")
```

Gebruik alleen beeld met een vrije licentie (publiek domein, CC0, CC BY of
CC BY-SA) of eigen foto's. Een foto die je zomaar van het internet plukt, mag
niet in lesmateriaal dat je verspreidt.

## Waarom er tekeningen in staan

Veel kinderen met een hoogbegaafd, ASS- of ADHD-profiel leren visueel: een
getallenlijn of een breukenstrook blijft hangen waar een alinea tekst dat niet
doet. Elke bundel legt daarom elk stuk theorie ook in beeld uit, en houdt de
bladspiegel rustig — weinig kleuren, veel wit, korte alinea's.

## De bundels opnieuw maken

In `bron/` staat waarmee ze gemaakt zijn:

- `stijl.css` — de huisstijl van het oefenplatform, in drukvorm.
- `svg.py` — de tekenhulpjes: getallenlijn, breukenstroken, procentraster,
  maatladder, klok, hoeken, vlakke figuren, ruimtefiguren, staaf-, lijn- en
  cirkeldiagram, dobbelsteen, stappenplan.
- `bundel.py` — zet een bundel-beschrijving om naar een html-bestand.
- `maak_<vak>.py` — de inhoud van alle bundels van dat vak.
- `pdf.js` — zet een html-bestand om naar pdf (via Playwright).

Zo maak je een heel vak opnieuw:

```
python3 maak_wiskunde.py       # schrijft één html-bestand per hoofdstuk
node pdf.js getallenkennis     # en zo verder, per hoofdstuk
```

Wil je enkel een zin aanpassen, verander die dan in het `maak_`-bestand van dat
vak en draai die twee regels opnieuw.
