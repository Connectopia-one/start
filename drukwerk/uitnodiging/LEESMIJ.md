# Uitnodiging najaar 2026

Twee afbeeldingen van één A4 elk, om onder elkaar in een mail te plakken naar
iedereen die ons ooit mailde of al eens op een kamp of een les was. Samen lezen
ze als één lange mail: blad 1 is wat we doen, blad 2 zijn de kampen en de
korting.

## De bestanden

- `uitnodiging-1-aanbod.jpg` en `uitnodiging-2-kampen.jpg` — **deze plak je in
  de mail.** Ze zijn met opzet lichter gemaakt, zodat de mail niet te zwaar
  wordt.
- `uitnodiging-1-aanbod.png` en `uitnodiging-2-kampen.png` — scherper, voor
  Facebook, Instagram of om te laten drukken.
- `uitnodiging-najaar-2026.pdf` — de twee bladen onder elkaar, om te printen of
  als bijlage mee te sturen.

## Iets aanpassen

Alle tekst staat in `bron/uitnodiging.html`. Je verandert daar gewoon de woorden
tussen de `<` en `>` tekens door. Daarna maak je de nieuwe versie zo:

    cd bron
    node render.js

Het script zegt per blad of alles er nog op past:

- `ok` betekent dat het past.
- `PAST NIET` betekent dat de tekst over de voettekst valt. Haal dan een paar
  woorden weg tot er weer `ok` staat.

Wil je scherpere afbeeldingen (bijvoorbeeld om te laten drukken):

    DSF=3 node render.js

## Welke foto's erop staan

- Blad 1, een foto per werking, alle drie vierkant (1254 x 1254), door Kim
  gekozen op 6 oktober 2026: `young-engineers-bouwpakket`,
  `pluswerking-tekenen`, `plusklas-planeten`.
- Blad 2: `bouwpakket-in-genk` en `werken-aan-de-groene-tafels` (liggend,
  1600 x 1200) plus `karton-brug-bouwen` (vierkant).

**De maten van de vakjes horen bij de vorm van de foto**, zodat er niets wordt
afgesneden. Op blad 1 is de kolom 58,67mm breed en het vakje even hoog, want de
foto's zijn vierkant. Op blad 2 staan de twee liggende foto's in kolommen van
58,67mm bij 44mm hoog, en de vierkante ernaast in een kolom van 44mm, zodat de
drie vakjes toch even hoog zijn.

Wil je een andere foto, zet ze dan in `bron/` en verander de bestandsnaam in
`uitnodiging.html`. Let op de vorm: een staande foto past nergens in deze
vakjes zonder dat de boven- en onderkant eraf gaan. Neem er liefst een waar
meerdere kinderen op staan; dat leest warmer dan een close-up van één paar
handen.

## Wat je zeker nakijkt als je het later hergebruikt

- De **kampdata** en de **thema's** in het groene blok op blad 2.
- De **einddatum van de korting** (nu 31 december 2026) en de code
  **DANKJEWEL**, allebei in het oranje blok. Die code staat bewust niet op de
  website: hij werkt juist omdat hij persoonlijk is. Ouders vermelden hem in
  het boodschapvak van het aanvraagformulier, en jij trekt het bedrag er zelf af.
- De **prijzen** op blad 1. Die komen uit `website/content/aanbod.ts`; veranderen
  ze daar, verander ze dan hier ook.
