# De databank van het oefenplatform

Elk bestand hieronder plak je één keer in de **SQL-editor** van het
Supabase-project van het **oefenplatform**, en dan klik je op Run.

**Twijfel je of je er eentje al gedraaid hebt? Draai het gewoon opnieuw.**
Alle bestanden hier zijn zo geschreven dat een tweede keer niets kapotmaakt
en niets dubbel zet. Dat is met opzet: het is veel makkelijker om ze alle
elf na elkaar te draaien dan te moeten onthouden welke al aan de beurt
geweest zijn. Dit geldt alleen voor de bestanden hier; een **vragenbestand**
importeren mag je wél maar één keer doen, tenzij je "vervangen" aanvinkt.

## In deze volgorde

| #   | bestand                | wat het toevoegt                                                                                                    |
| --- | ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 1   | `schema.sql`           | De basis: gezinnen, kinderen, vakken, hoofdstukken, vragen, antwoorden. Alles hangt hieraan, dus dit eerst.         |
| 2   | `leerbundel.sql`       | De theorie in het platform zelf, opgebouwd uit blokjes, naast de pdf die je kan opladen.                            |
| 3   | `materiaal.sql`        | De gratis linkenpagina `/materiaal`, die je beheert op `/beheer/materiaal`.                                         |
| 4   | `doelbestanden.sql`    | De officiële vakfiches en minimumdoelen bij `/onderwijsdoelen`.                                                     |
| 5   | `plusklasfiche.sql`    | De opvolgfiche per plusklaskind op `/begeleiding`.                                                                  |
| 6   | `basis.sql`            | 🧱 Basis als vijfde categorie, voor herhaling van de bouwstenen.                                                    |
| 7   | `uitdagingshoek.sql`   | 🔭 De uitdagingshoek als zesde categorie, met haar vier vakken.                                                     |
| 8   | `leestekst.sql`        | Een leestekst met woordenlijst boven de vragen, voor begrijpend lezen.                                              |
| 9   | `meldingen.sql`        | De meldknop onderaan een hoofdstuk, met het overzicht in Beheer → Meldingen.                                        |
| 10  | `weetjes.sql`          | Het weetjesprikbord: kinderen sturen in, jij keurt goed.                                                            |
| 11  | `weetjes-bericht.sql`  | Een antwoord van jou bij een ingestuurd weetje. Ná `weetjes.sql`.                                                   |
| 12  | `voortgang-blijft.sql` | Zorgt dat de voortgang van de kinderen blijft staan als je vragen vervangt.                                         |
| 13  | `dubbele-kinderen.sql` | Voegt kinderen samen die per ongeluk meerdere keren toegevoegd zijn. Enkel nodig als dat bij jou gebeurd is.        |
| 14  | `berichten.sql`        | Een bericht van jou aan alle ouders, bovenaan het platform. Beheer → Berichten.                                     |
| 15  | `voortgangsbalk.sql`   | Laat ouders per kind kiezen of er een voortgangsbalk bij de oefeningen staat.                                       |
| 16  | `melding-antwoord.sql` | Laat je bij "Afgehandeld" een woordje terugschrijven; de melder ziet dat bovenaan het platform. Ná `meldingen.sql`. |
| 17  | `groepen.sql`          | Splitst de opvolging op per plusklascode: de plusklas en de testgroepen in een eigen lijst. Ná `plusklasfiche.sql`. |

De volgorde telt maar op vier plaatsen: `schema.sql` moet eerst,
`weetjes-bericht.sql` moet ná `weetjes.sql`, `melding-antwoord.sql` ná
`meldingen.sql` en `groepen.sql` ná `plusklasfiche.sql`. De rest mag door
elkaar.

## Eén ding om te weten

`basis.sql` en `uitdagingshoek.sql` zetten allebei dezelfde regel opnieuw:
welke categorieën een hoofdstuk mag hebben. Daarom staat in allebei de
**volledige** lijst, hoekje inbegrepen. Voeg je ooit een categorie toe, pas
die lijst dan in allebei aan, anders neemt het ene bestand weg wat het
andere net toevoegde.
