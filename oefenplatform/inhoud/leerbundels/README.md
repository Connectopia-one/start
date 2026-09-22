# Leerbundels (pdf) bij de hoofdstukken

Hier staat per vak een map met de leerbundels: de theorie bij een hoofdstuk, met
tekeningen erbij, als pdf klaar om te uploaden.

De bestandsnaam is telkens de naam van het hoofdstuk, bijvoorbeeld
`getallenkennis.pdf`. Dat is geen toeval: op `/beheer/leerstof` kies je een vak,
sleep je alle pdf's er tegelijk in, en zoekt het platform op basis van die naam
zelf het juiste hoofdstuk erbij.

## Waarom er tekeningen in staan

Veel kinderen met een hoogbegaafd, ASS- of ADHD-profiel leren visueel: een
getallenlijn of een breukenstrook blijft hangen waar een alinea tekst dat niet
doet. Elke bundel legt daarom elk stuk theorie ook in beeld uit, en houdt de
bladspiegel rustig — weinig kleuren, veel wit, korte alinea's.

## De bundels opnieuw maken

In `bron/` staat waarmee ze gemaakt zijn:

- `stijl.css` — de huisstijl van het oefenplatform, in drukvorm.
- `svg.py` — tekenhulpjes voor getallenlijnen, breukenstroken en het procentraster.
- `maak_<hoofdstuk>.py` — de inhoud van één bundel; die schrijft een html-bestand.
- `pdf.js` — zet dat html-bestand om naar pdf (via Playwright).

Zo gaat dat:

```
python3 maak_getallenkennis.py     # schrijft getallenkennis.html
node pdf.js getallenkennis         # schrijft getallenkennis.pdf
```

Wil je enkel een zin aanpassen, dan hoef je de pdf niet opnieuw te maken: je kan
ook gewoon de tekst in het `maak_`-bestand veranderen en die twee regels opnieuw
draaien.
