# Frans 🌱 Start

Frans is de achtste vakdiscipline van de minimumdoelen van het lager onderwijs
en het laatste vak dat bij 🌱 Start nog ontbrak. In Vlaanderen begint Frans in
het vijfde leerjaar, dus voor de meeste kinderen is dit hun eerste vreemde taal
op papier.

**Zeven hoofdstukken van twintig vragen, samen 140 vragen.**

| Hoofdstuk | Waarover |
|-----------|----------|
| Woorden voor elke dag | getallen, kleuren, dagen, maanden, groeten |
| Mezelf voorstellen | naam, leeftijd, waar je woont, je gezin, tu tegenover vous |
| Être en avoir | de twee werkwoorden zijn en hebben, en wanneer je welk gebruikt |
| De tegenwoordige tijd | de werkwoorden op -er, plus aller en faire |
| Zinnen bouwen | le en la, un en une, ne … pas, vragen stellen, woordvolgorde |
| Op school en onderweg | schoolgerief, de klas, de weg vragen in de stad |
| Een tekstje lezen | een echte Franse tekst met vragen erover |

## Wat er wel en niet in staat

- **Alleen de schriftelijke kant**: lezen, schrijven en woordenschat. Luisteren
  en spreken horen ook bij de doelen, maar die kan dit platform niet toetsen.
  Datzelfde geldt bij Frans ✨ Spark.
- **Geen grammaticale vaktaal.** "Le of la?" in plaats van "bepaal het geslacht
  van het substantief".
- **Elke leesvraag staat op een echt Frans zinnetje of tekstje**, niet op een
  losse vertaaloefening. Het laatste hoofdstuk draagt een volledige tekst
  ("Le samedi, Camille ne va pas à l'école…") met een woordenlijst eronder.
- **Accenten hoeven niet.** Het platform vergelijkt een invulantwoord van een
  taalvak zonder accenten en toont de juiste schrijfwijze als tip; zie
  `components/Quiz.tsx`. In de uitleg staat het accent er wél bij, want dat is
  wat een kind moet zien.

## Bijwerken

De vragen staan in `bron/frans.py`, één lijst per hoofdstuk. Daarna:

    python3 inhoud/start/bron/bouw_frans.py

Het script schrijft pas als alles klopt. Het kijkt na of elk hoofdstuk twintig
vragen heeft, of geen vraag twee keer staat (ook niet elders in 🌱 Start), of
elk meerkeuzeantwoord naar een bestaande optie wijst, of elke vraag uitleg
heeft, of je niet kan gokken op de langste optie of op waar, en of elk woord
tussen sterretjes in de woordenlijst staat en omgekeerd.

## Importeren

`frans.json` gaat via **Beheer → Vakken → 🌱 Start → Frans → vragen
importeren**, met het vinkje **"Bestaande vragen vervangen" aan**. Het vak
Frans bestaat al, want ✨ Spark gebruikt het ook.
