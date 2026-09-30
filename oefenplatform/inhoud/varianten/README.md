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
| `spark-nederlands-varianten.json` | Nederlands | Woordsoorten en woordvorming, Zinsdelen zinssoorten en congruentie (elk deel 1 en 2) |
| `spark-frans-varianten.json` | Frans | De twee grammaticathema's (elk deel 1 en 2) |
| `spark-engels-varianten.json` | Engels | De twee grammaticathema's (elk deel 1 en 2) |
| `boost-doorstroom-nederlands-varianten.json` | Nederlands | De woordsoorten, de werkwoorden en woordvorming, de zinsdelen, de spelling (elk deel 1 en 2) |
| `boost-dubbele-finaliteit-nederlands-varianten.json` | Nederlands | Dezelfde vier thema's, maar dan bij dubbele finaliteit |
| `boost-doorstroom-engels-varianten.json` | Engels | De zeven grammaticathema's (elk deel 1 en 2) |

De spellinghoofdstukken van Nederlands ✨ Spark zitten hier niet bij: hun
wisselende woorden staan in `spark/bron/nl_spelling.py` zelf en zijn al
geïmporteerd met `spark-nederlands-spelling-varianten.json`.

De twee bestanden van Nederlands 🚀 Boost bevatten precies dezelfde vragen: de
bouwscripts van doorstroom en van dubbele finaliteit lezen dezelfde thema's.
Ze dragen wel elk hun eigen categorie mee, dus ze gaan elkaar niet in de weg.
Je hebt ze allebei nodig.

**Let op bij het schrijven.** Geen enkele ronde mag twee keer dezelfde vraag
tonen binnen één hoofdstuk; `variantenwerk.py` rekent dat na over álle
rondes, samen met de vragen die geen varianten hebben. En een vraag krijgt
alleen wisselende woorden als de leerstof in de **regel** zit en niet in het
woord. Wat een begrip of een uitdrukking toetst, blijft zoals het is.
