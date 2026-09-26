# Wat je moet importeren, en in welke volgorde

Twaalf bestanden, telkens via **Beheer → Vakken → het vak → vragen importeren**.
Het vinkje **"Bestaande vragen vervangen"** staat per bestand hieronder. Doe elk
bestand **één keer**.

Let op: importeren met "vervangen" wist de ✅ per vraag (de voortgang) van dat
vak. De sterren per hoofdstuk blijven wel staan. Zolang de testgezinnen nog niet
begonnen zijn, kost dat niets.

## 🌱 Start

| # | Bestand | Vak | Vervangen |
|---|---------|-----|-----------|
| 1 | `start-engels.json` | Engels | **aan** |
| 2 | `start-geschiedenis.json` | Geschiedenis | **aan** |
| 3 | `start-nederlands.json` | Nederlands | **aan** |
| 4 | `start-aardrijkskunde.json` | Aardrijkskunde | **aan** |
| 5 | `start-nederlands-spelling.json` | Nederlands | **aan** |
| 6 | `start-wiskunde.json` | Wiskunde | **aan** |
| 7 | `start-wiskunde-extra.json` | Wiskunde | **uit** |
| 8 | `start-wiskunde-rekenen-en-breuken.json` | Wiskunde | **aan** |

Bij wiskunde is de volgorde belangrijk: 6 vervangt de oude vragen door de eerste
reeks, en 7 zet de tweede reeks erbij. Samen zijn dat weer 40 vragen per
hoofdstuk, ook voor Meetkunde. `wiskunde-meetkunde.json` heb je dus niet nodig.

Bij 5 en 8 verdwijnen de drie voorbeeldvragen die bij het opzetten van de
databank meegekomen zijn. Spelling houdt er 47 over, Rekenen en breuken 37.

## ✨ Spark

| # | Bestand | Vak | Vervangen |
|---|---------|-----|-----------|
| 9 | `spark-frans.json` | Frans | **aan** |
| 10 | `spark-nederlands.json` | Nederlands | **aan** |
| 11 | `spark-geschiedenis.json` | Geschiedenis | **aan** |
| 12 | `spark-wiskunde.json` | Wiskunde | **aan** |

Nummer 12 bevat ook Meetkunde en Metend rekenen, met de tekeningen erbij.
`wiskunde-meetkunde-metend.json` hoef je er dus niet meer apart bij te laden.

## En nog één ding buiten de vragen om

Draai `supabase/meldingen.sql` één keer in de SQL-editor van het oefenplatform.
Dat maakt de tabel voor de meldknop die nu onderaan elk hoofdstuk staat.

## 🔭 De uitdagingshoek (nieuw)

Die staat los van de lijst hierboven en heeft een eigen stappenplan, want er
hoort ook één keer een SQL-bestand bij. Zie `inhoud/hoekje/README.md`.
