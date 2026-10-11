# Poster: welke vakken staan er voor jouw richting?

Een poster met **elke studierichting** en daaronder de vakken die vandaag op
het oefenplatform staan. Kim vroeg hem op 11 oktober 2026, omdat mensen haar
één voor één vragen of hún richting erbij zit.

Dit is iets anders dan de poster in `social/posts/` (8 oktober 2026): die telt
de vakken per categorie op, maar zegt niet voor wie ze zijn.

## Wat staat er

- `poster-richtingen-A4.pdf` — om zelf af te drukken op A4
- `poster-richtingen-A3.pdf` — dezelfde poster op A3, voor aan de muur
- `poster-richtingen.png` — scherpe afbeelding, om op het scherm te tonen
- `poster-richtingen.jpg` — lichtere afbeelding, om door te sturen

## Opnieuw maken

```
cd bron
python3 -I maak.py      # leest inhoud/ en schrijft poster.html
node render.js          # png, jpg en de A4-pdf
python3 -I maak-a3.py   # de A3-pdf uit de A4
```

`render.js` meet of alles nog op het blad past en zegt `ok` of `PAST NIET`.
Het getal `rek` is de witruimte die overblijft boven de groene voet; `teveel`
is wat er buiten het blad valt. Komt `teveel` boven 0, dan is er al tekst
weggevallen.

## Waar de richtingen vandaan komen

De tabel `RICHTINGEN` in `bron/maak.py` is overgenomen uit de **docstrings van
de bouwscripts** van het oefenplatform (`inhoud/<categorie>/bron/bouw_<vak>.py`),
en die geven bladzijde 1 van de vakfiche weer: daar staat voor welke
studierichtingen die fiche geldt.

**Gok dat nooit uit de naam van een vak.** De uitzonderingen die je anders
mist:

- De fiches Nederlands, Engels en Frans van 🚀 Boost doorstroom gelden voor
  vier richtingen, **niet voor moderne talen**: die heeft eigen, zwaardere
  talenfiches die wij nog niet hebben.
- Het vak natuurwetenschappen is er **niet** voor de richting
  natuurwetenschappen zelf: die legt haar wetenschappen af in drie aparte
  examens, biologie, chemie en fysica. Zo ook bij Beyond voor
  wetenschappen-wiskunde en Latijn-wiskunde.
- Humane wetenschappen van 🚀 Boost volgt **wiskunde basis**, de vier andere
  richtingen wiskunde gevorderd.
- Engels van 🌍 Beyond is gebouwd op de fiches van de domeingebonden
  richtingen, dus staat het enkel bij bedrijfswetenschappen en
  welzijnswetenschappen.

Twee vakken dekken iets ruimer dan de fiche van een richting vraagt; dat staat
als voetnoot op de poster zelf (`VOETNOTEN` in `maak.py`).

## Wat het script zelf nakijkt

- Elk vak dat op de poster genoemd wordt, moet als
  `inhoud/<categorie>/<vak>.json` bestaan. Zo niet: **FOUT**, en het script
  stopt.
- Elk vakbestand dat bestaat maar bij geen enkele richting staat, wordt gemeld
  met **LET OP**. Zo valt een nieuw vak meteen op.
- Elk vak moet een nette naam hebben in `NAMEN`.

Komt er een vak bij, zet het dan bij de richtingen van zijn fiche en draai het
script opnieuw. De tellingen bovenaan de poster komen uit `inhoud/` en volgen
vanzelf; ze gebruiken dezelfde telling als `social/posts/bron/maak_vakkenoverzicht.py`,
zodat de twee posters nooit een ander getal geven.
