# Kant-en-klare hoofdstukken voor 🌱 Start (5de en 6de leerjaar)

In deze map staat per vak een bestand met hoofdstukken en vragen, klaar om te
importeren in het oefenplatform. Alles staat op niveau **start**, dat is de
categorie voor het 5de en 6de leerjaar.

| Bestand | Vak | Hoofdstukken | Vragen |
|---|---|---|---|
| `wiskunde.json` | Wiskunde | 6 | 120 |
| `wiskunde-extra.json` | Wiskunde, tweede reeks | 6 | 120 |
| `nederlands.json` | Nederlands | 5 | 100 |
| `nederlands-spelling.json` | Nederlands, het gratis proefhoofdstuk | 1 | 47 |
| `wetenschap-en-techniek.json` | Wetenschap en techniek | 4 | 80 |
| `aardrijkskunde.json` | Aardrijkskunde | 3 | 60 |
| `geschiedenis.json` | Geschiedenis | 3 | 120 |
| `engels.json` | Engels | 6 | 120 |

Elk hoofdstuk heeft 20 vragen, behalve geschiedenis: daar zijn het er 40 per
hoofdstuk. Samen 767 vragen.

**Spelling is het gratis proefhoofdstuk.** Dat hoofdstuk staat er al bij het
opzetten van de databank (zie `supabase/schema.sql`) met drie voorbeeldvragen, en
het is het enige wat iemand zonder account te zien krijgt. Het moet dus ook het
platform verkopen, en drie vragen doen dat niet. `nederlands-spelling.json` zet er
47 bij, en `inhoud/leerbundels/nederlands/spelling.pdf` is de leerbundel erbij.

Dat bestand gebruikt de titel die het hoofdstuk in `schema.sql` krijgt:
`Hoofdstuk 1 — Spelling: voorbeeld`. De bulk-import zoekt een hoofdstuk op zijn
titel, dus **importeer eerst en hernoem daarna**; andersom maakt de import een
tweede hoofdstuk aan.

**Wiskunde staat in twee bestanden.** `wiskunde.json` was al ingeladen toen de
tweede reeks er kwam, en opnieuw importeren zou alles dubbel zetten. Daarom staan
de 120 nieuwe vragen apart in `wiskunde-extra.json`, met dezelfde hoofdstuktitels.
Die tweede reeks komt er netjes bij. Begin je met een lege databank, importeer dan
gewoon eerst het ene bestand en daarna het andere; samen geeft dat 40 vragen per
hoofdstuk, net als bij geschiedenis.

## Waarop dit gebaseerd is

De indeling volgt de vakken en de domeinen van de **minimumdoelen van de Vlaamse
overheid** voor het basisonderwijs, die gelden sinds 1 september 2025. Die doelen
zijn vastgelegd voor drie momenten: het einde van het kleuteronderwijs, het einde
van het vierde leerjaar en het einde van het zesde leerjaar. Hier is gemikt op het
**einde van het zesde leerjaar**.

De zes hoofdstukken van wiskunde zijn de zes domeinen uit de minimumdoelen
(getallenkennis, bewerkingen, meten en metend rekenen, meetkunde, kansrekenen en
statistiek, en probleemoplossend denken). Nederlands volgt dezelfde logica
(lezen, schrijven, mondeling taalgebruik, taalsysteem en taalgebruik, literatuur),
en wetenschap en techniek ook (biologie, chemie, natuurkunde, techniek).

**Engels is een bewuste uitzondering.** In het Vlaamse basisonderwijs staat
Frans als tweede taal in de minimumdoelen, Engels niet: dat begint pas in het
secundair. Deze zes hoofdstukken staan er op vraag van Connectopia, om kinderen
van het 5de en 6de leerjaar een stevige basis te geven voor de start in het
middelbaar. Ze zijn opgebouwd naar wat een eerstejaars secundair verondersteld
wordt te kunnen: woordenschat, zichzelf voorstellen, to be en to have, de
tegenwoordige tijd, zinsbouw en taal voor op school en onderweg.

De **vragen zelf** zijn hier geschreven op maat van dat niveau; ze staan niet
letterlijk in de minimumdoelen. Kijk ze dus zeker eens na met je eigen leerplan
ernaast voor je ze bij de kinderen legt.

## Hoe je ze importeert

1. Ga naar **/beheer/vakken** in het oefenplatform.
2. Bestaat het vak nog niet? Maak het eerst aan met de knop bovenaan.
3. Klap bij dat vak het vak-blok open en zoek het veld voor de bulk-import.
4. Open hier het juiste bestand, selecteer **alles** en plak het in dat veld.
5. Klik op importeren.

Het eerste hoofdstuk van een categorie binnen een vak wordt automatisch gratis
gezet, zodat iedereen het kan uitproberen. Wil je een ander hoofdstuk gratis
maken, gebruik dan de knop "Gratis / Op slot" op diezelfde pagina.

Een hoofdstuk met een titel die al bestaat binnen dat vak krijgt de vragen erbij;
een nieuwe titel wordt een nieuw hoofdstuk.

## Zelf vragen bijschrijven

Elke vraag heeft een `type`:

- `meerkeuze` — met vier `opties`; `antwoord` is het **nummer** van het juiste
  antwoord, waarbij het eerste 0 is, het tweede 1, enzovoort.
- `waarofniet` — `antwoord` is `true` of `false`, zonder `opties`.
- `invultekst` — `antwoord` is de tekst die het kind moet typen. Hoofdletters,
  een lidwoord vooraan ("de longen" naast "longen") en een punt achteraan maken
  niet uit. Houd het antwoord toch kort en zonder spaties of komma's, anders is
  het te moeilijk om het precies juist te typen.

`uitleg` is de zin die het kind te zien krijgt na het antwoorden. Laat die nooit
weg: daar leert een kind het meest van.
