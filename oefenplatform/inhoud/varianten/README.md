# Wisselende woorden

Wat hierin staat, zijn **uittreksels**: enkel de hoofdstukken die wisselende
woorden gekregen hebben, met al hun vragen. Ze staan apart zodat Kim niet het
hele vak opnieuw moet importeren om één hoofdstuk bij te werken.

De vragen zelf blijven staan waar ze horen, in `inhoud/<niveau>/<vak>.json`.
Deze bestanden worden daaruit gehaald door de scripts `varianten_*.py` in de
bron-mappen; een bestand hier met de hand aanpassen heeft dus geen zin.

Importeren gaat per bestand in **Beheer → Vakken**, bij het vak dat in de naam
staat, met **vervangen aan**. Het bestand draagt zelf de categorie, dus de
andere hoofdstukken van dat vak blijven ongemoeid.

Draai eenmalig `supabase/spellingvarianten.sql` voor het eerste van deze
bestanden. Dat is al gebeurd op 30 september 2026.

| Bestand | Vak | Hoofdstukken |
|---------|-----|--------------|
| `start-nederlands-varianten.json` | Nederlands | Taalsysteem en taalgebruik |
| `start-frans-varianten.json` | Frans | Être en avoir, De tegenwoordige tijd, Zinnen bouwen |
| `start-engels-varianten.json` | Engels | To be en to have, De tegenwoordige tijd, Zinnen bouwen |

**Let op bij het schrijven.** Geen enkele ronde mag twee keer dezelfde vraag
tonen binnen één hoofdstuk; `varianten_start.py` rekent dat na over álle
rondes, samen met de vragen die geen varianten hebben. En een vraag krijgt
alleen wisselende woorden als de leerstof in de **regel** zit en niet in het
woord. Wat een begrip of een uitdrukking toetst, blijft zoals het is.
