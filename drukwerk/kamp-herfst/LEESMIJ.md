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

## Wat er nog in moet

Drie dingen staan er bewust nog niet op, omdat ze nog niet vastlagen: **de uren,
de prijs en het thema per kamp**. Zodra die er zijn, komt er een strook onder de
twee datumkaartjes. Ook het adres van Level X 28 staat er nog niet volledig op,
enkel "Hasselt".

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
