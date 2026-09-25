# Hoofdstukken voor ✨ Spark (1ste & 2de middelbaar)

Zelfde opzet als `../start`: één JSON-bestand per vak, klaar om te plakken in
**Bulk-import: meerdere hoofdstukken tegelijk (JSON)** op `/beheer/vakken`,
onder het juiste vak.

## Twee delen per thema

Kim koos op 22 september 2026 voor **twee hoofdstukken van 20 vragen per thema**
in plaats van één lang hoofdstuk:

- **deel 1** — de leerstof onder de knie krijgen
- **deel 2** — de moeilijkere vragen, voor wie deel 1 af heeft

Twee redenen. Twintig vragen is een portie die een kind afmaakt; veertig is er
een waar het halverwege uit valt. En een sticker verdien je per hoofdstuk dat je
volledig juist afwerkt (`registreerSticker` in `app/voortgang-actions.ts`), dus
twee delen geven twee stickers op dezelfde leerstof — én twee kansen, want één
fout in veertig vragen levert anders niets op.

De twee delen staan na elkaar in de lijst, want ze krijgen opeenvolgende
volgnummers bij de import.

## Leerbundels

Eén bundel per thema, niet per deel. Die upload je twee keer, één keer bij elk
deel, zodat een kind in deel 2 de theorie nog bij de hand heeft.

## geschiedenis.json

Gebaseerd op de officiële vakfiche **geschiedenis 1ste graad A-stroom** die Kim
bezorgde (geldig 2027). De fiche behandelt de prehistorie, het oude nabije
oosten en de klassieke oudheid, plus het historisch referentiekader en het
werken met bronnen.

Klaar (240 vragen, alle zes de thema's uit de fiche):

| Hoofdstuk | Vragen | Leerbundel |
| --- | --- | --- |
| Het historisch referentiekader — deel 1 en 2 | 2 x 20 | historisch-referentiekader.pdf |
| De prehistorie — deel 1 en 2 | 2 x 20 | prehistorie.pdf |
| Mesopotamië en Egypte — deel 1 en 2 | 2 x 20 | mesopotamie-en-egypte.pdf |
| Het oude Griekenland — deel 1 en 2 | 2 x 20 | het-oude-griekenland.pdf |
| Het Romeinse Rijk — deel 1 en 2 | 2 x 20 | het-romeinse-rijk.pdf |
| Bronnen, kunst en beeldvorming — deel 1 en 2 | 2 x 20 | bronnen-kunst-en-beeldvorming.pdf |

De bundels staan in `../leerbundels/geschiedenis/` en komen uit
`../leerbundels/bron/maak_geschiedenis_spark.py`.

Importeer je dit bestand opnieuw, vink dan **"Bestaande vragen vervangen"** aan,
anders staat alles wat er al in zat een tweede keer in je databank.

## natuurwetenschappen.json

Gebaseerd op de officiële vakfiche **natuurwetenschappen eerste graad A-stroom**
die Kim bezorgde (geldig 2027). Die fiche telt drie delen, en het examen weegt
ze ook zo: biologie 47,5 %, chemie en fysica 32,5 %, onderzoek 20 %. Daarom
staan er vijf thema's biologie, drie chemie en fysica en twee onderzoek.

Klaar (400 vragen, tien thema's van 2 x 20):

| Hoofdstuk | Vragen | Leerbundel |
| --- | --- | --- |
| Cellen, weefsels en organen — deel 1 en 2 | 2 x 20 | cellen-weefsels-en-organen.pdf |
| Fotosynthese en de plant — deel 1 en 2 | 2 x 20 | fotosynthese-en-de-plant.pdf |
| Het menselijk lichaam — deel 1 en 2 | 2 x 20 | het-menselijk-lichaam.pdf |
| Voortplanting — deel 1 en 2 | 2 x 20 | voortplanting.pdf |
| Ecologie en biodiversiteit — deel 1 en 2 | 2 x 20 | ecologie-en-biodiversiteit.pdf |
| Materie, stoffen en mengsels — deel 1 en 2 | 2 x 20 | materie-stoffen-en-mengsels.pdf |
| Massadichtheid — deel 1 en 2 | 2 x 20 | massadichtheid.pdf |
| Energie, kracht en snelheid — deel 1 en 2 | 2 x 20 | energie-kracht-en-snelheid.pdf |
| Veilig werken, meten en eenheden — deel 1 en 2 | 2 x 20 | veilig-werken-meten-en-eenheden.pdf |
| Wetenschappelijk onderzoek — deel 1 en 2 | 2 x 20 | wetenschappelijk-onderzoek.pdf |

De vragen staan per thema in `bron/nw_*.py`;
`python3 bron/bouw_natuurwetenschappen.py` zet ze samen in het importbestand en
bewaakt onderweg de twintig vragen per deel, de opties, de vragen die dubbel
zouden staan en het aandeel meerkeuzevragen met meerdere juiste antwoorden.

`python3 controleer_natuurwetenschappen.py` rekent daarna élke berekening in de
vragen zelf na — massadichtheid, volumes, snelheden, omzettingen — en kijkt of
dát het aangeduide antwoord is.

Het eerste deel draagt `hernoemVan: "Cellen en toestanden van materie"`. Zo
neemt het het hoofdstuk over dat bij het opzetten van de databank al op ✨ Spark
stond (zie `supabase/schema.sql`), in plaats van er een restje met drie
voorbeeldvragen naast te laten staan.

De bundels staan in `../leerbundels/natuurwetenschappen/` en komen uit
`../leerbundels/bron/maak_natuurwetenschappen_spark.py`.

## nederlands.json

Gebaseerd op de officiële vakfiche **Nederlands eerste graad A-stroom** die Kim
bezorgde. Het examen weegt lezen en luisteren het zwaarst (60 %), daarna
schrijven en gesprekken (32 %) en spreken (8 %); literatuur en taalbeschouwing
komen bij de andere vaardigheden aan bod. Vier thema's gaan daarom over lezen en
luisteren, twee over schrijven, spreken en register, één over literatuur, en
drie over de ondersteunende kennis van het taalsysteem, die je bij alles nodig
hebt.

Klaar (400 vragen, tien thema's van 2 x 20):

| Hoofdstuk | Vragen | Leerbundel |
| --- | --- | --- |
| Onderwerp, hoofdgedachte en hoofdpunten — deel 1 en 2 | 2 x 20 | onderwerp-hoofdgedachte-en-hoofdpunten.pdf |
| Tekstsoorten en het communicatiemodel — deel 1 en 2 | 2 x 20 | tekstsoorten-en-het-communicatiemodel.pdf |
| Feiten, meningen en betrouwbaarheid — deel 1 en 2 | 2 x 20 | feiten-meningen-en-betrouwbaarheid.pdf |
| Tekststructuur en signaalwoorden — deel 1 en 2 | 2 x 20 | tekststructuur-en-signaalwoorden.pdf |
| Schrijven, spreken en gesprekken voeren — deel 1 en 2 | 2 x 20 | schrijven-spreken-en-gesprekken-voeren.pdf |
| Register, taalvariatie en non-verbale communicatie — deel 1 en 2 | 2 x 20 | register-taalvariatie-en-non-verbale-communicatie.pdf |
| Literatuur en beeldspraak — deel 1 en 2 | 2 x 20 | literatuur-en-beeldspraak.pdf |
| Spelling, leestekens en werkwoordsvormen — deel 1 en 2 | 2 x 20 | spelling-leestekens-en-werkwoordsvormen.pdf |
| Woordsoorten en woordvorming — deel 1 en 2 | 2 x 20 | woordsoorten-en-woordvorming.pdf |
| Zinsdelen, zinssoorten en congruentie — deel 1 en 2 | 2 x 20 | zinsdelen-zinssoorten-en-congruentie.pdf |

De vragen staan per thema in `bron/nl_*.py`; `python3 bron/bouw_nederlands.py`
zet ze samen in het importbestand en bewaakt de twintig vragen per deel, de
opties, de vragen die dubbel zouden staan en het aandeel meerkeuzevragen met
meerdere juiste antwoorden (hier 25 %, minstens twee per hoofdstuk).

Nederlands had op ✨ Spark nog geen hoofdstuk in de databank staan — het
voorbeeldhoofdstuk uit `supabase/schema.sql` staat op 🌱 Start — dus er wordt
niets hernoemd.

De bundels staan in `../leerbundels/nederlands/` en komen uit
`../leerbundels/bron/maak_nederlands_spark.py`.

## frans.json

Gebaseerd op de officiële vakfiche **Frans eerste graad A-stroom** die Kim
bezorgde. **Alleen de schriftelijke onderdelen.** Het examen telt vijf
onderdelen: luisteren (30 %), lezen (30 %), schrijven (2 x 8 %), spreken (8 %)
en twee gesprekken (2 x 8 %). Luisteren, spreken en de gesprekken vragen geluid
en een gesprekspartner, dus die oefen je hier niet. Wat hier wel staat — lezen,
schrijven, woordenschat en grammatica — is samen goed voor 46 % van de punten.
Dat staat zo in de leerbundels, op `/onderwijsdoelen` en hieronder, zodat
niemand denkt dat hij hiermee het hele examen oefent.

Twee thema's gaan over lezen (het zwaarste onderdeel dat hier kan), één over
schrijven, één over een foto of afbeelding beschrijven (dat vraagt de fiche bij
schrijven én bij literatuur), vier over de woordvelden van de fiche, en twee
over de grammaticale begrippen die de fiche opsomt.

Klaar (400 vragen, tien thema's van 2 x 20):

| Hoofdstuk | Vragen | Leerbundel |
| --- | --- | --- |
| Een Franse tekst lezen — deel 1 en 2 | 2 x 20 | een-franse-tekst-lezen.pdf |
| Tekstsoorten, signaalwoorden en verwijswoorden — deel 1 en 2 | 2 x 20 | tekstsoorten-signaalwoorden-en-verwijswoorden.pdf |
| Schrijven: berichten, uitnodigingen en mails — deel 1 en 2 | 2 x 20 | schrijven-berichten-uitnodigingen-en-mails.pdf |
| Een foto of afbeelding beschrijven — deel 1 en 2 | 2 x 20 | een-foto-of-afbeelding-beschrijven.pdf |
| Woordenschat: mensen, familie, gevoelens en gezondheid — deel 1 en 2 | 2 x 20 | woordenschat-mensen-familie-gevoelens-en-gezondheid.pdf |
| Woordenschat: eten, wonen, kleding en dagelijkse dingen — deel 1 en 2 | 2 x 20 | woordenschat-eten-wonen-kleding-en-dagelijkse-dingen.pdf |
| Woordenschat: school, beroepen, sport en vrije tijd — deel 1 en 2 | 2 x 20 | woordenschat-school-beroepen-sport-en-vrije-tijd.pdf |
| Woordenschat: getallen, tijd, weer, reizen en landen — deel 1 en 2 | 2 x 20 | woordenschat-getallen-tijd-weer-reizen-en-landen.pdf |
| Grammatica: lidwoorden, naamwoorden en voornaamwoorden — deel 1 en 2 | 2 x 20 | grammatica-lidwoorden-naamwoorden-en-voornaamwoorden.pdf |
| Grammatica: werkwoorden, tijden en zinsbouw — deel 1 en 2 | 2 x 20 | grammatica-werkwoorden-tijden-en-zinsbouw.pdf |

De vragen staan per thema in `bron/fr_*.py`; `python3 bron/bouw_frans.py` zet ze
samen in het importbestand en bewaakt de twintig vragen per deel, de opties, de
vragen die dubbel zouden staan en het aandeel meerkeuzevragen met meerdere
juiste antwoorden (hier 22 %, minstens twee per hoofdstuk).

Frans had op ✨ Spark nog geen hoofdstuk in de databank staan, dus er wordt
niets hernoemd: `frans.json` importeren met "Bestaande vragen vervangen" aan.

De bundels staan in `../leerbundels/frans/` en komen uit
`../leerbundels/bron/maak_frans_spark.py`.

## Meerkeuze met meer dan één juist antwoord

Bij de examencommissie staat er bij een meerkeuzevraag **niet** hoeveel
antwoorden juist zijn. Duid je er één aan terwijl er twee juist waren, dan is de
hele vraag fout — geen halve punten. Kim vroeg op 23 september 2026 om dat vanaf
✨ Spark te laten oefenen.

Daarom heeft **een kwart van de meerkeuzevragen van geschiedenis** (44 van de
178) meerdere juiste antwoorden. In de JSON is `antwoord` dan een lijstje
nummers in plaats van één nummer:

```json
{
  "type": "meerkeuze",
  "vraag": "Welke van deze horen bij het politieke domein?",
  "opties": ["Een koning die wetten uitvaardigt", "Een oorlog tussen twee steden",
             "Een tempel bouwen voor een god", "Graan verkopen op de markt"],
  "antwoord": [0, 1],
  "uitleg": "..."
}
```

Die vragen staan in `bron/meerdere_antwoorden.py`;
`python3 bron/zet_meerdere_antwoorden.py` zet ze in `geschiedenis.json` en
bewaakt dat elke vraag minstens twee juiste antwoorden heeft, dat de nummers
bestaan en dat het aandeel tussen 20 en 30 % blijft.

**In het platform** krijgen álle meerkeuzevragen van zo'n hoofdstuk
aankruisvakjes in plaats van bolletjes. Anders zou het vakje verklappen bij
welke vraag er meer dan één antwoord juist is, en dan oefent een kind net niet
waar het om gaat. Een vraag telt alleen juist als alle juiste antwoorden
aangeduid zijn en geen enkel fout. Zie `lib/antwoord.ts`.

Bij **natuurwetenschappen** is het meteen zo geschreven: 65 van de 290
meerkeuzevragen (22 %) hebben meerdere juiste antwoorden, en elk hoofdstuk
heeft er minstens twee. Bij de rekenvragen over massadichtheid en snelheid
gaat het dan over inzicht (wat drijft er, welke verbanden kloppen), niet over
één berekening.

Wiskunde blijft zoals het was: daar is dit niet van toepassing.

## Invulvragen

Houd het antwoord op één woord zonder leestekens. `components/Quiz.tsx`
vergelijkt via `normaliseerAntwoord`: hoofdletters, een lidwoord vooraan en een
punt achteraan tellen niet mee, maar verder moet het exact kloppen.

## Tekeningen bij een vraag (sinds 25 september 2026)

Meetkunde en metend rekenen stonden volledig in woorden. Nu staat bij de
meeste vragen een tekening, als een markering achteraan de vraagtekst:

    {{hoek 130}}              een hoek van 130°
    {{driehoek gelijkbenig}}  een gelijkbenige driehoek, met de streepjes erbij
    {{driehoek 50-60-?}}      een driehoek met die hoeken; ? blijft open
    {{vierhoek trapezium}}    een trapezium, met pijltjes op de evenwijdige zijden
    {{snijlijn 70}}           twee snijdende rechten; "neven" erachter zet het
                              vraagteken op de nevenhoek
    {{evenwijdig 65}}         twee evenwijdige rechten met een snijlijn; "binnen"
                              erachter vraagt naar de binnenhoek aan dezelfde kant
    {{cirkeldeel straal}}     een cirkel met de straal; "stil" laat het woord weg
    {{merkwaardig hoogtelijn}} een driehoek met die merkwaardige lijn
    {{assen ruit}}            een figuur met zijn symmetrieassen
    {{beweging rotatie}}      de figuur voor en na de transformatie
    {{maat rechthoek 7x3}}    een rechthoek met 7 cm en 3 cm erbij
    {{maat cirkel straal 5}}  een cirkel met een straal van 5 cm
    {{ruimte balk 5x3x2}}     een balk in schuine projectie
    {{ladder oppervlakte}}    de maatladder, met maal 100 per stap
    {{samengesteld halvecirkel 6}}  een vierkant met er een halve cirkel op

De volledige lijst met alles wat kan, staat bovenaan
`components/Tekeningen.tsx`. Twee regels om te onthouden:

1. **De tekst moet blijven kloppen zonder de tekening.** Op de pagina waar
   ouders meekijken staat alleen de tekst, en een schermlezer leest die ook.
   Schrijf de vraag dus alsof er geen tekening bij staat.
2. **Een tekening mag het antwoord niet verklappen.** Daarom bestaat
   `{{hoek 90 ?}}` (zonder het getal en zonder het vierkantje) en
   `{{merkwaardig bissectrice stil}}` (zonder het woord eronder).

`wiskunde-meetkunde-metend.json` bevat alleen die vier hoofdstukken, zodat je
ze kan bijwerken zonder de andere veertien opnieuw in te laden.

## Begrijpend lezen: een tekst bij een hoofdstuk

Een hoofdstuk kan een **leestekst** dragen. Die staat bij het oefenen boven de
vragen en blijft staan zolang het kind ze nodig heeft. Onderaan de tekst komt
een verklarende woordenlijst.

In het importbestand ziet dat er zo uit:

```json
{"hoofdstukken": [{
  "titel": "Begrijpend lezen — ...",
  "niveau": "start",
  "leestekst": "Eerste alinea.\n\nTweede alinea met een *moeilijk woord* erin.",
  "woordenlijst": [{"woord": "moeilijk woord", "uitleg": "wat het betekent"}],
  "vragen": [...]
}]}
```

* Een lege regel begint een nieuwe alinea.
* Een woord tussen sterretjes krijgt een stippellijntje; erop tikken toont de
  uitleg uit de woordenlijst meteen onder de tekst.
* Staat er niets over `leestekst` in het bestand, dan blijft een bestaande
  tekst gewoon staan.
* Kim moet `supabase/leestekst.sql` één keer gedraaid hebben.
* In Beheer kan de tekst ook met de hand aangepast worden, onderaan de pagina
  van het hoofdstuk. De woordenlijst gaat daar als `woord = uitleg`, één per
  regel.

De vragen en de teksten staan in `inhoud/start/bron/begrijpend_lezen.py` en
`inhoud/spark/bron/begrijpend_lezen_spark.py`. Bouwen en nakijken:

```
python3 inhoud/start/bron/bouw_begrijpend_lezen.py          # 🌱 Start
python3 inhoud/start/bron/bouw_begrijpend_lezen.py spark    # ✨ Spark
```

Die bouwer schrijft pas weg als alles klopt. Hij kijkt na of elk invulantwoord
letterlijk in de tekst staat, of elk gemarkeerd woord in de woordenlijst staat,
of het juiste antwoord niet stelselmatig de langste optie is, en of waar en
niet-waar in evenwicht zijn.
