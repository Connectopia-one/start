# Folder externe plusklas

Eén blad over één ding: de externe plusklas op dinsdag, een volledige dag,
in de gebouwen van het Atheneum in Hasselt. Bedoeld om via de school mee te
geven, digitaal of op papier.

Zusterblad van `drukwerk/flyer-stem-naschools/`. Zelfde opbouw, groen in
plaats van blauw, zodat de twee naast elkaar als één familie lezen.

## Wat staat er

- `flyer-plusklas-A5.pdf` — om uit te delen
- `flyer-plusklas-A4.pdf` — hetzelfde blad, groter
- `flyer-plusklas.png` — scherpe afbeelding, 300 dpi
- `flyer-plusklas.jpg` — lichtere afbeelding, om door te sturen

## Opnieuw maken

```
cd bron
node render.js        # png, jpg en de A5-pdf
python3 maak-a4.py    # de A4-pdf uit de A5
```

## De foto's

De fotostrook is twee liggende foto's (4:3) en één vierkante, in vakjes met
exact diezelfde verhouding, dus er wordt niets afgesneden.

## Wat je nakijkt als je hem later hergebruikt

- De **prijs** (€50 per dag) en de regel over de **drie trajecten van tien
  dagen**.
- De regel **"Later instappen kan, ook nu nog"**; die veroudert het snelst.
- De qr-code in `bron/qr-proefles-plusklas.png` wijst naar
  https://www.connectopia.one/aanvraag/proefles-externe-plusklas en is met een
  decoder nagelezen.
