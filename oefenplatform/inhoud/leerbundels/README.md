# Leerbundels (pdf) bij de hoofdstukken

Hier staat per vak een map met de leerbundels: de theorie bij een hoofdstuk, met
tekeningen erbij, als pdf klaar om te uploaden.

De bestandsnaam is telkens de naam van het hoofdstuk, bijvoorbeeld
`getallenkennis.pdf`. Dat is geen toeval: op `/beheer/leerstof` kies je een vak,
sleep je alle pdf's er tegelijk in, en zoekt het platform op basis van die naam
zelf het juiste hoofdstuk erbij.

## ✨ Spark — geschiedenis

`bron/maak_geschiedenis_spark.py` maakt de bundels voor het Spark-niveau, uit de
vakfiche geschiedenis 1ste graad A-stroom. Ze komen in dezelfde map
`geschiedenis/` terecht als die van Start; je houdt ze uit elkaar aan hun naam,
en in het beheer aan de categorie die je bovenaan kiest.

Geef zo'n bundel `niveau=SPARK` mee, anders zet de kop van de pdf "🌱 Start"
(de standaard in `bundel.py`).

**Eén bundel per thema, niet per deel.** Een thema bestaat uit een hoofdstuk
deel 1 en een hoofdstuk deel 2 met dezelfde leerstof en moeilijkere vragen. De
bundel hoort bij allebei, dus die upload je twee keer.

Klaar: `historisch-referentiekader.pdf` (4 blz) en `prehistorie.pdf` (5 blz).

## Echte foto's in een bundel

Naast de tekeningen kan er ook echt beeldmateriaal in, met `bundel.foto(...)`.
Dat zet het bestand als base64 in de html, zodat de pdf achteraf nergens meer
naar hoeft te zoeken. Geef altijd een bronvermelding mee bij beeld dat niet van
Connectopia zelf is:

```python
("fig", bundel.foto("fotos/colosseum.jpg", bron="Foto: naam, CC BY-SA 4.0"),
 "Het Colosseum in Rome, gebouwd rond het jaar 80.")
```

Gebruik alleen beeld met een vrije licentie (publiek domein, CC0, CC BY of
CC BY-SA) of eigen foto's. Een foto die je zomaar van het internet plukt, mag
niet in lesmateriaal dat je verspreidt.

Let op het verschil tussen het onderwerp en de foto. Een grotschildering, een
hiëroglief of een Romeinse muur is duizenden jaren oud en dus vrij van rechten,
maar de **foto** ervan is dat niet: wie die muur fotografeerde, heeft rechten op
dat beeld. Daarom staan er in de bundels van geschiedenis tekeningen in plaats
van foto's. Dat lost het rechtenprobleem op, en het leest vaak duidelijker —
een doorsnede van een Romeinse weg toont de vier lagen, een foto van kasseien
niet.

Bij aardrijkskunde geldt hetzelfde, met één uitzondering. Een landschap is een
schema zodra je het uitlegt: een doorsnede van de kust toont in één beeld dat
de polder lager ligt dan de zee, en dat ziet een kind op geen enkele luchtfoto.
Zulke dingen tekenen we dus.

Een **landkaart** tekenen we niet. Een kaart uit het hoofd natekenen wordt
scheef, en scheve grenzen horen niet in lesmateriaal. Komt er een kaart in een
bundel, dan is dat een echte kaart met een vrije licentie, met de bron erbij.

## Een kaart met haar legende

Kaarten zitten in `bron/fotos/`, samen met [`BRONNEN.md`](./bron/fotos/BRONNEN.md),
waarin per bestand staat waar het vandaan komt. Zet daar elke nieuwe afbeelding bij.

Gebruik `bundel.kaart(...)` in plaats van `bundel.foto(...)`:

```python
("fig", bundel.kaart("fotos/belgie-provincies-kaart.png",
                     "fotos/belgie-provincies-legende.png",
                     "Kaart: gemaakt met mapchart.net"),
 "Zoek jouw provincie eens op.")
```

De legende staat met opzet in een **apart bestand**, in kolommen naast elkaar.
Zou ze als smalle kolom naast de kaart staan, dan schaalt haar tekst mee met de
kaart en wordt ze op A4 een paar millimeter groot. Nu krijgen kaart en legende
allebei de volle breedte en blijft de tekst leesbaar.

Is de kaart staand (Europa loopt van de poolcirkel tot Noord-Afrika), dan passen
kaart en legende samen niet meer op één bladzijde. Geef de kaart dan een kleinere
`breedte=`, want een legende die van haar kaart wegvalt helpt niemand.

## Waarom er tekeningen in staan

Veel kinderen met een hoogbegaafd, ASS- of ADHD-profiel leren visueel: een
getallenlijn of een breukenstrook blijft hangen waar een alinea tekst dat niet
doet. Elke bundel legt daarom elk stuk theorie ook in beeld uit, en houdt de
bladspiegel rustig — weinig kleuren, veel wit, korte alinea's.

## De bundels opnieuw maken

In `bron/` staat waarmee ze gemaakt zijn:

- `stijl.css` — de huisstijl van het oefenplatform, in drukvorm.
- `svg.py` — de tekenhulpjes: getallenlijn, breukenstroken, procentraster,
  maatladder, klok, hoeken, vlakke figuren, ruimtefiguren, staaf-, lijn- en
  cirkeldiagram, dobbelsteen, stappenplan, en voor geschiedenis een
  grotschildering, stenen werktuigen, hiërogliefen, de piramides, een Griekse
  tempel, een amfitheater, een aquaduct, de doorsnede van een heirbaan, een
  burcht, een verlucht handschrift, een drukpers, een stoommachine en een
  mijnschacht. Voor aardrijkskunde komen daar nog bij: een doorsnede van de
  kust, het hoogteprofiel van België, een rivier van bron tot monding, een
  klimaatdiagram, een zeehaven, een stadsplan, de gewesten en provincies, de
  aardbol met de klimaatgordels, de seizoenen rond de zon, een bergprofiel met
  boom- en sneeuwgrens, zandduinen met een oase, de lagen van het regenwoud en
  een vulkaan in doorsnede. Voor spelling: 't kofschip, open en gesloten
  lettergrepen, de -t in de tegenwoordige tijd, en de vijf verkleinuitgangen.
- `bundel.py` — zet een bundel-beschrijving om naar een html-bestand.
- `maak_<vak>.py` — de inhoud van alle bundels van dat vak.
- `pdf.js` — zet een html-bestand om naar pdf (via Playwright).
- `maak_alles.py` — maakt alle bundels opnieuw en zet elke pdf bij zijn vak.
  Gebruik dit na elke aanpassing aan `stijl.css` of aan een tekening in `svg.py`,
  want die raken elke bundel en niet alleen die van het vak waaraan je werkte.
  Eén vak volstaat ook: `python3 maak_alles.py nederlands`.

Zo maak je een heel vak opnieuw:

```
python3 maak_wiskunde.py       # schrijft één html-bestand per hoofdstuk
node pdf.js getallenkennis     # en zo verder, per hoofdstuk
```

Wil je enkel een zin aanpassen, verander die dan in het `maak_`-bestand van dat
vak en draai die twee regels opnieuw.
