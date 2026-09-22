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

## Invulvragen

Houd het antwoord op één woord zonder leestekens. `components/Quiz.tsx`
vergelijkt via `normaliseerAntwoord`: hoofdletters, een lidwoord vooraan en een
punt achteraan tellen niet mee, maar verder moet het exact kloppen.
