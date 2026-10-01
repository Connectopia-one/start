# De databank van de website

Deze bestanden horen **niet** in de Supabase van het oefenplatform maar
in die van het **ouderportaal**: de website deelt die databank, zodat jij de
aanvragen daar in één scherm ziet staan.

Plakken in de SQL-editor, op Run klikken. **Opnieuw draaien mag altijd**; er
gaat niets verloren en er komt niets dubbel bij.

| bestand | wat het toevoegt | zonder dit |
| --- | --- | --- |
| `aanvragen.sql` | De tabel achter élk formulier op de site: een infovraag, een inschrijving, een terugbelverzoek, de winactie, een professional die zich meldt. Je leest ze in het ouderportaal bij Aanvragen. | Elk formulier op de website geeft een foutmelding. |
| `prikbord.sql` | Het prikbord waar ouders zelf een briefje ophangen, en de meldknop daarbij. | Het prikbord blijft leeg en een nieuw briefje raakt niet weg. |
| `social.sql` | De pagina In de kijker: de berichten van sociale media die op de site komen, en het bakje waar hun beelden in gaan. | De pagina toont enkel de berichten die in `content/inkijker.ts` staan, en insturen kan niet. |

## Waarom dat zo gescheiden is

Bezoekers van de website mogen in `aanvragen` wel iets **toevoegen** maar
niets **lezen** — er staan namen en leeftijden van kinderen in. Op het
prikbord geldt hetzelfde voor `volledige_naam` en `contact`: die twee zijn
voor jou, niet voor de bezoeker. Dat staat in de rechten onderaan elk
bestand. Zet die rechten niet ruimer.
