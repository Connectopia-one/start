# Poster om op te hangen

Een poster voor aan de muur, in scholen en op de plaatsen waar we werken.
Zelfde inhoud als de uitnodigingsmail in `drukwerk/uitnodiging/`, maar
**zonder de kortingscode**: die is persoonlijk en hoort niet aan een muur.

## Wat staat er

- `poster-connectopia-A4.pdf` — om zelf af te drukken op A4
- `poster-connectopia-A3.pdf` — dezelfde poster op A3, voor aan de muur
- `poster-connectopia.png` — scherpe afbeelding, 300 dpi
- `poster-connectopia.jpg` — lichtere afbeelding, om door te sturen

## Opnieuw maken

```
cd bron
node render.js          # png, jpg en de A4-pdf
python3 maak-a3.py      # de A3-pdf uit de A4
```

`render.js` meet zelf of de inhoud niet onder de groene voettekst schuift en
zegt `ok` of `PAST NIET`. Wil je een scherpere afbeelding, draai dan
`DSF=3.125 node render.js`.

## De qr-code

`bron/qr-aanbod.png` wijst naar https://www.connectopia.one/aanbod. Een
nieuwe maken met een ander adres:

```
python3 -c "import qrcode; qrcode.make('https://www.connectopia.one/aanbod').save('qr-aanbod.png')"
```

Scan hem daarna zelf eens na met je telefoon voor je laat drukken.

## De foto's

Vier vierkante foto's (1254 x 1254) uit de werking, dezelfde die Kim koos
voor de uitnodiging: `young-engineers-bouwpakket`, `pluswerking-tekenen`,
`plusklas-planeten` en `karton-brug-bouwen`. De vakjes zijn 40 x 40 mm, dus
even hoog als breed, en er wordt niets afgesneden. Een staande of liggende
foto past hier niet zonder dat er iets wegvalt.

## Wat je nakijkt als je hem later hergebruikt

- De **prijzen** in de vier kaartjes en bij de kampen.
- De **kampdata** en de thema's; die staan ook in `website/content/aanbod.ts`.
- De **dagen en uren** van de plusklas, de twee pluswerkingen en Young
  Engineers.
- Er staat bewust **geen korting** op. Zet er ook geen op: aan een muur kan
  iedereen hem meelezen.

Er bestaat ook een kleinere A5-versie om digitaal naar scholen te sturen, in
`drukwerk/school-poster/`.
