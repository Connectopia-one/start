# Flyer naschoolse STEM op dinsdag

Eén blad over één ding: de naschoolse lessen Young Engineers op
dinsdagnamiddag, in de gebouwen van het Atheneum in Hasselt. Bedoeld om via
de basisschool mee te geven, digitaal of op papier.

Dit blad hoort bij het BOA-verhaal: de school hoeft zelf niets te
organiseren, wij halen de kinderen op en de les gaat door in het groot
atheneum. Daarom staat dat in een eigen vakje op de flyer, naast het
praktische.

## Wat staat er

- `flyer-stem-naschools-A5.pdf` — om uit te delen
- `flyer-stem-naschools-A4.pdf` — hetzelfde blad, groter
- `flyer-stem-naschools.png` — scherpe afbeelding, 300 dpi
- `flyer-stem-naschools.jpg` — lichtere afbeelding, om door te sturen

## Opnieuw maken

```
cd bron
node render.js        # png, jpg en de A5-pdf
python3 maak-a4.py    # de A4-pdf uit de A5
```

`render.js` meet zelf of de inhoud niet onder de groene voettekst schuift en
zegt `ok` of `PAST NIET`.

## De foto's

De fotostrook is twee liggende foto's (4:3) en één vierkante, in vakjes met
exact diezelfde verhouding, dus er wordt niets afgesneden. Wissel je er een
om, neem dan een foto met dezelfde verhouding of pas de breedte van de
kolom aan in `.strook`.

## Wat je nakijkt als je hem later hergebruikt

- Het **uur** (15u20 – 16u35) en de **prijs** (€20 per les).
- De zin **"Wij halen je kind op"**: die staat er als een vaste afspraak.
  Geldt dat niet voor elke school, pas hem dan aan.
- De qr-code in `bron/qr-proefles-ye.png` wijst naar
  https://www.connectopia.one/aanvraag/proefles-young-engineers en is met een
  decoder nagelezen. Verandert het adres, maak hem dan opnieuw en lees hem
  opnieuw na.
