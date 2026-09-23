# Flyer en post voor de herfstkampen 2026

Gemaakt op 23 september 2026, in dezelfde huisstijl als de website en de andere
flyers.

| Bestand | Waarvoor |
| --- | --- |
| `kamp-herfst-flyer.pdf` | A5, om af te drukken of digitaal door te sturen |
| `kamp-herfst-flyer.png` | Dezelfde flyer als afbeelding, 300 dpi |
| `kamp-herfst-post.png` | 1080 x 1350, voor Instagram en Facebook |

De QR-code op de flyer wijst naar `https://www.connectopia.one/aanbod` en is
nagelezen met een decoder, dus hij scant.

## Wat erop staat

Elke dag van 9u tot 15u, 40 euro per dag, 6 tot 12 jaar. De thema's staan op de
kaartjes: **Young Engineer Held** in Hasselt, **Creatieve duizendpoot, van
techniek tot design** in Genk.

De adressen: Level X 28, Vilderstraat 28 in Hasselt, en T2 Campus, Thor Park 8040
in Genk.

## Opnieuw maken

```
cd bron
PW=$(npm root -g)/playwright HTML=flyer.html OUT=preview.png PDF=flyer.pdf DSF=3.125 node render.js
PW=$(npm root -g)/playwright node render-post.js
```

`render.js` waarschuwt zelf als de tekst onder de voettekst schuift.
De foto in de kop is `bron/hero.jpg`, een uitsnede van
`fotos-werking/werken-aan-de-groene-tafels.jpg`: kinderen van achteren, dus geen
herkenbare gezichten.
