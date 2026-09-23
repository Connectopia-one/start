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
