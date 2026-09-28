# Nieuwsbrief najaar 2026

Een nieuwsbrief op één A4, voor de gezinnen die al eens bij ons kwamen: wat er
veranderd is (vzw, nieuwe locaties, oefenplatform), wat er dit schooljaar te
doen is, de kampen van de herfst- en kerstvakantie, en het bedankje met de
code DANKJEWEL.

## De twee bestanden

- `nieuwsbrief-najaar-2026.png` — dit plak je in een mail of zet je op
  Facebook en Instagram.
- `nieuwsbrief-najaar-2026.pdf` — deze print je, of hang je aan een mail.

## Iets aanpassen

Alle tekst staat in `bron/nieuwsbrief.html`. Je verandert daar gewoon de
woorden tussen de `<` en `>` tekens door. Daarna maak je de nieuwe versie zo:

    cd bron
    node render.js

Het script zegt zelf of alles nog op één blad past:

- `ok` betekent dat het past.
- `PAST NIET` betekent dat de tekst over de voettekst valt. Haal dan een paar
  woorden weg tot er weer `ok` staat.

Wil je een scherpere afbeelding (bijvoorbeeld om te laten drukken):

    DSF=3 node render.js

## Wat je zeker nakijkt als je het later hergebruikt

- De **kampdata** en de **thema's** in het groene blok.
- De **einddatum van de korting** (nu 31 december 2026), op één plaats in het
  oranje blok.
- De code **DANKJEWEL** zelf. Die staat bewust niet op de website: hij werkt
  juist omdat hij persoonlijk is. Ouders vermelden hem in het boodschapvak van
  het aanvraagformulier, en jij trekt het bedrag er zelf af.
