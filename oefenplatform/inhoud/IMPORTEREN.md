# Wat je moet importeren, en in welke volgorde

Twaalf bestanden, telkens via **Beheer → Vakken → het vak → vragen importeren**.
Het vinkje **"Bestaande vragen vervangen"** staat per bestand hieronder. Doe elk
bestand **één keer**.

Sinds 27 september 2026 mag dit ook als er al kinderen aan het werk zijn: wat ze
gemaakt hebben, blijft meetellen in hun voortgang. Wel is daarna niet meer na te
lezen wélk vraagje het precies was, en de ✅ per losse vraag verdwijnt. De
sterren per hoofdstuk en de balkjes blijven staan. Draai daarvoor eerst
`supabase/voortgang-blijft.sql`, als je dat nog niet gedaan hebt.

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

## 🌱 Start — de pittige hoofdstukken (28 september 2026)

| # | Bestand | Vak | Vervangen |
|---|---------|-----|-----------|
| 13 | `start-wiskunde-pittig.json` | Wiskunde | **aan** |
| 14 | `start-nederlands-pittig.json` | Nederlands | **aan** |
| 15 | `start-geschiedenis-pittig.json` | Geschiedenis | **aan** |
| 16 | `start-aardrijkskunde-pittig.json` | Aardrijkskunde | **aan** |
| 17 | `start-engels-pittig.json` | Engels | **aan** |
| 18 | `start-wetenschap-en-techniek-pittig.json` | Wetenschap en techniek | **aan** |

Naast elk gewoon hoofdstuk komt er één pittig hoofdstuk: "Getallenkennis —
pittig" en zo verder, telkens twintig moeilijkere vragen over dezelfde leerstof.
Samen zijn dat 31 hoofdstukken en 620 vragen. Ze raken de gewone hoofdstukken
niet aan, dus je mag deze bestanden op elk moment inladen, ook als de kinderen
al bezig zijn. Zie `pittig/README.md`.

## ✨ Spark

| # | Bestand | Vak | Vervangen |
|---|---------|-----|-----------|
| 9 | `spark-frans.json` | Frans | **aan** |
| 10 | `spark-nederlands.json` | Nederlands | **aan** |
| 11 | `spark-geschiedenis.json` | Geschiedenis | **aan** |
| 12 | `spark-wiskunde.json` | Wiskunde | **aan** |

Nummer 12 bevat ook Meetkunde en Metend rekenen, met de tekeningen erbij.
`wiskunde-meetkunde-metend.json` hoef je er dus niet meer apart bij te laden.

Heb je nummer 12 al gedaan en komt er later nog een verbetering aan wiskunde
✨ Spark bij? Dan mag je dat bestand gewoon opnieuw importeren, opnieuw met
**vervangen** aan. Twee keer hetzelfde bestand zonder dat vinkje zet alles
dubbel; mét het vinkje kan het geen kwaad.

Voor één zin die anders moet, hoef je trouwens niets meer te importeren. Bij
elke vraag in Beheer → Vakken staat nu een knopje **Aanpassen**: daarmee pas je
de vraag, de opties, het antwoord en de uitleg ter plekke aan. Dat is meestal
het snelste antwoord op een melding.

## En nog één ding buiten de vragen om

Draai `supabase/meldingen.sql` één keer in de SQL-editor van het oefenplatform.
Dat maakt de tabel voor de meldknop die nu onderaan elk hoofdstuk staat.

## 🔭 De uitdagingshoek (nieuw)

Die staat los van de lijst hierboven en heeft een eigen stappenplan, want er
hoort ook één keer een SQL-bestand bij. Zie `inhoud/hoekje/README.md`.
