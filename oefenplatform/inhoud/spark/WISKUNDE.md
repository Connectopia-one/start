# Wiskunde voor ✨ Spark

Gebaseerd op de vakfiche **wiskunde 1ste graad A-stroom** (geldig 2027).

## De indeling

De fiche heeft zeven onderdelen. In het platform staan ze als negen
hoofdstukken, omdat meetkunde en metend rekenen apart staan:

| Fiche | Hoofdstuk in het platform |
| --- | --- |
| Probleemoplossend denken | Probleemoplossend denken |
| Wiskundige redeneringen en uitspraken | Wiskundige redeneringen en uitspraken |
| Getallenleer | Getallenleer |
| Meetkunde en metend rekenen | Meetkunde + Metend rekenen |
| Relaties en verandering | Relaties en verandering |
| Data en onzekerheid (statistiek) | Data en onzekerheid |
| Verzamelingen | Verzamelingen |

Daarnaast staat **Negatieve getallen en procenten** als gratis proefhoofdstuk.
Inhoudelijk hoort dat bij Getallenleer, maar het blijft apart staan omdat het
het enige is wat een bezoeker zonder account van Spark te zien krijgt.

Let op wat de fiche zelf zegt over **wiskundige redeneringen en uitspraken**:
dat zijn *geen losse opgaven*, maar iets wat in alle andere onderdelen verweven
zit. Bij bijna elk doel staat die zin er letterlijk bij. Het blijft een
hoofdstuk — notatie, de als-dan-relatie en het tegenvoorbeeld zijn te oefenen —
maar het is het kleinste, en die manier van redeneren komt ook in de andere
hoofdstukken terug.

## Bestaande hoofdstukken omzetten

Kim had de negen hoofdstukken al aangemaakt, elk als één geheel. Ze worden
opgesplitst in een deel 1 en een deel 2 van twintig vragen.

Dat hoeft ze **niet met de hand te hernoemen**. De bulk-import kent sinds
commit van 22 september 2026 een veld `hernoemVan`:

```json
{ "titel": "Getallenleer — deel 1", "hernoemVan": "Getallenleer", ... }
```

Staat het hoofdstuk nog onder de oude naam in de databank, dan wordt het
hernoemd in plaats van dat er een tweede naast komt. Zo blijven het volgnummer,
het webadres, de leerbundel, de stickers en de voortgang van de kinderen
behouden. Bestaat de nieuwe titel al, dan gebeurt er niets — een tweede import
is dus ongevaarlijk.

Het deel 2 krijgt wél een nieuw volgnummer, achteraan. In de lijst staat het
tóch onder zijn deel 1, want `lib/hoofdstukvolgorde.ts` sorteert op thema.

## Rekenvoorbeelden narekenen

Bij geschiedenis is een fout onderschrift vervelend; bij wiskunde is een fout
rekenvoorbeeld erger. Daarom staat elk getal dat een wiskundebundel beweert ook
in `../leerbundels/bron/controleer.py`, maar dan uitgerekend:

```
cd ../leerbundels/bron && python3 controleer.py
```

Zet je een nieuw voorbeeld in een bundel, zet het daar dan ook bij.

## Bestandsnamen van de bundels

Spark-bundels voor wiskunde krijgen het achtervoegsel `-spark`
(`getallenleer-spark.pdf`), want de onderwerpen overlappen met die van Start —
"meetkunde" bestaat in allebei de niveaus — en alle bundels van een vak staan
in dezelfde map.

## Stand van zaken

Alle negen hoofdstukken staan er, elk als een deel 1 en een deel 2 van twintig
vragen. Samen 18 hoofdstukken en 360 vragen in `wiskunde.json`.

| Hoofdstuk | Vragen | Bundel |
| --- | --- | --- |
| Negatieve getallen en procenten — deel 1 (gratis) en 2 | 2 x 20 | negatieve-getallen-en-procenten-spark.pdf |
| Getallenleer — deel 1 en 2 | 2 x 20 | getallenleer-spark.pdf |
| Probleemoplossend denken — deel 1 en 2 | 2 x 20 | probleemoplossend-denken-spark.pdf |
| Wiskundige redeneringen en uitspraken — deel 1 en 2 | 2 x 20 | redeneringen-en-uitspraken-spark.pdf |
| Meetkunde — deel 1 en 2 | 2 x 20 | meetkunde-spark.pdf |
| Metend rekenen — deel 1 en 2 | 2 x 20 | metend-rekenen-spark.pdf |
| Relaties en verandering — deel 1 en 2 | 2 x 20 | relaties-en-verandering-spark.pdf |
| Data en onzekerheid — deel 1 en 2 | 2 x 20 | data-en-onzekerheid-spark.pdf |
| Verzamelingen — deel 1 en 2 | 2 x 20 | verzamelingen-spark.pdf |

De vragen staan per thema in een eigen bestand onder `bron/`, met Nederlandse
uitleg erbij. `bron/bouw_wiskunde.py` zet ze samen in `wiskunde.json`; dat
script vervangt een thema dat er al in staat, dus het opnieuw draaien is
ongevaarlijk.

`controleer_wiskunde.py` rekent de antwoorden zelf opnieuw uit (264 stuks) en
waarschuwt bij een vraag met een getal erin die nog nergens nagekeken wordt.

Deel 1 van "Negatieve getallen en procenten" staat op `gratis: true` en is het
proefhoofdstuk: dat is wat iemand zonder account van wiskunde te zien krijgt.
De bundel erbij is daardoor ook zonder account leesbaar, dus die moet op zichzelf
kunnen staan — geen verwijzingen naar hoofdstukken die achter de login zitten.
