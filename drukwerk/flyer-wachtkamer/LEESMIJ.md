# Flyer voor de wachtkamer

Een flyer om uit te delen en in wachtkamers te leggen bij kinesisten,
logopedisten, coaches en artsen. Dezelfde opbouw als de poster in
`drukwerk/poster-ophangen/`, met twee verschillen:

- Het grote kampenblok is vervangen door **twee vakjes naast elkaar**: links
  de vakantiekampen kort, rechts wie we zijn en waarom we dit doen.
- Er staat een strook bij met waar we voor staan: **kennis en ervaring met HB
  en UHB, inclusief, prikkelarm, kleine groepen**. Die stond nergens op het
  drukwerk, terwijl het voor een ouder in een wachtkamer net het zinnetje is
  dat telt.

## Wat staat er

- `flyer-wachtkamer-A5.pdf` — om uit te delen
- `flyer-wachtkamer-A4.pdf` — dezelfde flyer, groter
- `flyer-wachtkamer.png` — scherpe afbeelding, 300 dpi
- `flyer-wachtkamer.jpg` — lichtere afbeelding, om door te sturen

## Opnieuw maken

```
cd bron
node render.js        # png, jpg en de A5-pdf
python3 maak-a4.py    # de A4-pdf uit de A5
```

`render.js` meet zelf of de inhoud niet onder de groene voettekst schuift en
zegt `ok` of `PAST NIET`. De flyer is **op A5 getekend** en wordt daarna naar
A4 geschaald; A4 en A5 hebben dezelfde verhouding, dus op A4 is het exact
hetzelfde blad, alleen groter. Zo blijft de tekst op A5 goed leesbaar.

## De tekst over Kim

Die komt uit haar eigen tekst op de website, `website/content/over-ons.ts`,
ingekort. Verander je daar iets, kijk dan ook hier. De regel **"Wij stellen
geen diagnoses en geven geen therapie"** blijft erop staan: dat is wat een
professional en een twijfelende ouder willen lezen, en het klopt.

## Wat je nakijkt als je hem later hergebruikt

- De **prijzen** in de vier kaartjes en bij de kampen.
- De regel **"Eerstvolgend: ..."** in het kampvakje; die veroudert het snelst.
- De qr-code in `bron/qr-aanbod.png` wijst naar
  https://www.connectopia.one/aanbod.
