# Flyer voor professionals

Een kennismakingsflyer voor kinesisten, logopedisten, coaches, auticoaches,
artsen, neurologen en andere begeleiders. A5 (148 × 210 mm), twee kanten.

## Wat staat er

- `flyer-professionals.pdf` — beide kanten in één bestand, klaar voor de drukker
- `flyer-professionals-voorkant.png` — 300 dpi, om digitaal door te sturen
- `flyer-professionals-achterkant.png` — 300 dpi, idem

**Voorkant:** wie we zijn, wat we niet zijn, en de vier dingen die we
organiseren. **Achterkant:** wat een professional eraan heeft, wat we hem of
haar graag bezorgen (folders digitaal, een poster, flyers op papier), en de
contactgegevens met een QR-code naar www.connectopia.one.

## Aanpassen

Alles staat in `bron/`. De teksten in `voor.html` en `achter.html`, de kleuren
en de maten in `stijl.css`. Opnieuw maken:

```
cd bron
PW=$(npm root -g)/playwright HTML=voor.html   OUT=../flyer-professionals-voorkant.png   PDF=voor.pdf   DSF=3.125 node render.js
PW=$(npm root -g)/playwright HTML=achter.html OUT=../flyer-professionals-achterkant.png PDF=achter.pdf DSF=3.125 node render.js
python3 -c "import pymupdf; d=pymupdf.open('voor.pdf'); d.insert_pdf(pymupdf.open('achter.pdf')); d.save('../flyer-professionals.pdf')"
```

`render.js` waarschuwt zelf als de tekst te lang wordt en onder de voettekst
schuift. Wordt een stuk tekst langer, kort dan iets anders in of verklein een
marge in `stijl.css`; de bladzijde mag niet hoger worden dan 794 pixels.

De QR-code (`bron/qr.svg`) wijst naar `https://www.connectopia.one/` en is
nagelezen met OpenCV op de gedrukte bladzijde. Verandert het adres, maak hem
dan opnieuw met `qrcode` en lees hem opnieuw na: niet elke QR-versie wordt
even goed herkend.

## Kleuren en fonts

Dezelfde als de website (`website/app/globals.css`): crème #fbf6ea,
donkergroen #2f4a22, paars #5e2d91, oranje #d96e25, Nunito en Caveat.
De foto is `startpagina.jpg` van de website. Het logo is dat van Kim.
