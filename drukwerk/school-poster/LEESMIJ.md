# Poster voor scholen

Een A5-poster (148 × 210 mm) om naar scholen te sturen: wat Connectopia vzw
aanbiedt en wat het kost, zodat leerkrachten ouders kunnen doorverwijzen.

## Wat staat er

- `school-poster.pdf` — klaar voor de drukker of om digitaal door te sturen
- `school-poster.png` — dezelfde poster als afbeelding, 300 dpi

De vier werkingen met hun prijs:

| Werking | Prijs | Wanneer |
| --- | --- | --- |
| Externe plusklas | €50 per dag | Dinsdag 9u–15u, Atheneum Hasselt |
| Pluswerkingen | €25 per voormiddag | Woensdag & zaterdag 9u–12u, Genk en Hasselt |
| Young Engineers | €20 per les | Di, wo & za, lessen van 1u15, Hasselt en Genk |
| Vakantiekampen | €40 per dag | Elke schoolvakantie |

De QR-code (overgenomen van de herfstkamp-flyer) wijst naar
`https://www.connectopia.one/aanbod`.

## Aanpassen

Alles staat in `bron/poster.html` en `bron/stijl.css` (kleuren/fonts gedeeld
met de andere flyers). Opnieuw maken:

```
cd bron
PW=$(npm root -g)/playwright HTML=poster.html OUT=../school-poster.png PDF=poster.pdf DSF=3.125 node render.js
```

`render.js` waarschuwt als de inhoud onder de voettekst schuift of de
bladzijde hoger wordt dan 794 pixels — bij een prijswijziging past meestal
gewoon de tekst in de kaartjes, zonder dat er ruimte bijkomt.

## Kleuren en fonts

Dezelfde als de website en de andere flyers (`website/app/globals.css`):
crème #fbf6ea, donkergroen #2f4a22, paars #5e2d91, oranje #d96e25, blauw
#3d7cb0, Nunito en Caveat. De foto (`startpagina.jpg`) en het logo
(`logo-kim-transparant.png`) zijn hergebruikt uit de professionals-flyer.
