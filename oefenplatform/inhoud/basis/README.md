# 🧱 Basis — de bouwstenen herhalen

Kim vroeg op 23 september 2026 om een heel eenvoudige basismodule voor
kinderen die de basis van wiskunde nog niet vlot beheersen. Basis is geen
leerjaar: het staat op de startpagina apart onder de vier categorieën, en een
kind uit eender welke categorie kan het gebruiken.

## Eenmalig: de databank laten weten dat "basis" bestaat

Voer `supabase/basis.sql` één keer uit in de SQL Editor van Supabase, vóór de
import. Anders weigert de databank hoofdstukken met niveau "basis".

## Importeren

Plak `wiskunde.json` in **Bulk-import: meerdere hoofdstukken tegelijk (JSON)**
op `/beheer/vakken`, onder het vak Wiskunde. Eén keer, niet twee keer: dan
staat alles dubbel.

| Hoofdstuk | Vragen | Leerbundel |
| --- | --- | --- |
| Maal en gedeeld door 10, 100 en 1000 — deel 1 (gratis) en 2 | 2 x 20 | maal-en-gedeeld-door-10-100-1000-basis.pdf |
| Maten omzetten — deel 1 en 2 | 2 x 20 | maten-omzetten-basis.pdf |
| Wiskundewoorden — deel 1 en 2 | 2 x 20 | wiskundewoorden-basis.pdf |
| Breuken, kommagetallen en gehele getallen — deel 1 en 2 | 2 x 20 | breuken-kommagetallen-en-gehele-getallen-basis.pdf |
| Delers en veelvouden: ggd en kgv — deel 1 en 2 | 2 x 20 | delers-en-veelvouden-ggd-en-kgv-basis.pdf |

De bundels staan in `../leerbundels/wiskunde/` en komen uit
`../leerbundels/bron/maak_basis.py`. Upload ze op `/beheer/leerstof` met
categorie 🧱 Basis; elke bundel hoort bij deel 1 én deel 2.

## Extra oefeningen: wiskunde-extra.json

Later op 23 september vroeg Kim extra oefeningen, zonder nieuwe leerbundels:
kommagetallen vergelijken, optellen en aftrekken (want kinderen dachten dat
0,7 kleiner is dan 0,65), en breuken in beeld. Die staan in een apart bestand,
`wiskunde-extra.json`, zodat `wiskunde.json` niet opnieuw geïmporteerd hoeft te
worden. Importeer het één keer op dezelfde manier.

| Hoofdstuk | Vragen |
| --- | --- |
| Kommagetallen vergelijken, optellen en aftrekken — deel 1 en 2 | 2 x 20 |
| Breuken in beeld — deel 1 en 2 | 2 x 20 |

Deze vragen gebruiken codes in de vraagtekst, die `components/Figuren.tsx`
omzet in een tekening of een sleepoefening. Er is dus geen nieuwe kolom in de
databank nodig.

- `{{figuur cirkel 3/8}}` tekent een cirkel (ook `strook` of `raster`) met 3 van de 8 stukken gekleurd.
- `{{kleur strook 10}}` bij een invulvraag: het kind kleurt zelf stukken in. Het antwoord is het aantal gekleurde stukken.
- `{{sleep klein-groot}}` (of `groot-klein`) bij een invulvraag: het kind sleept de opties in volgorde. De opties staan in de juiste volgorde, het antwoord is ze samen met " · " ertussen. Na het controleren tekent het platform waar ze echt op de getallenlijn liggen.

In `bron/reken.py` maken `figuur`, `kleur` en `sleep` die codes aan.

## Een vraag aanpassen

De vragen staan per thema in `bron/*.py`. Pas daar aan en draai dan:

```
python3 inhoud/basis/bron/bouw_basis.py
```

Dat rekent elke vraag na (zie `bron/reken.py`) en schrijft pas een nieuwe
`wiskunde.json` als alles klopt. Elke rekenvraag heeft een veld `reken` met wat
eruit moet komen; een vraag zonder getal (een definitie) krijgt `WOORD`.

Invulantwoorden mogen een komma bevatten ("0,25"). Het platform aanvaardt ook
"0.25" en "0,250", zie `normaliseerGetal` in `components/Quiz.tsx`.
