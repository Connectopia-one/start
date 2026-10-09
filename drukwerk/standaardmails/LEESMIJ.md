# Drie standaardmails

Gevraagd door Kim op 9 oktober 2026. Platte tekst, om in haar eigen
mailprogramma te plakken en de vierkante haken aan te vullen.

| Bestand | Waarvoor |
| --- | --- |
| `1-kamp-bevestiging.txt` | Een plaats op een kamp bevestigen, met de inloggegevens voor de inlichtingenfiche |
| `2-professionals-aanvraag-ontvangen.txt` | Antwoord op een aanvraag via /professionals: ontvangen, en contact zodra de folders klaar zijn |
| `3-proefles-we-bellen-je.txt` | Antwoord op een aanvraag voor een gratis proefles: we bellen je op |

Alles tussen vierkante haken vult Kim zelf aan. De vaste gegevens staan er al
in: info@matmgroep.com, 0468 35 74 96, www.connectopia.one en
ouders.connectopia.one.

## Het rekeningnummer

In de kampmail staat BE61 0689 6047 3617 van Connectopia vzw, het nummer dat
ook op /steun-ons staat. Als inschrijvingen op een ander nummer moeten komen,
pas die regel dan aan.

## Wat de inlichtingenfiche vandaag vraagt

Nagekeken in `ouderportaal/app/portaal/gezin/page.tsx` en in
`ouderportaal/supabase/schema.sql`. Per gezin: telefoonnummer en adres. Per
kind: naam, geboortedatum, allergieën, "wat wij als begeleiders goed zouden
moeten weten", naam en telefoon van een noodcontact, en twee
toestemmingsvinkjes voor foto's (intern, en publiek).

Voor een kamp is dat dun. Wat er niet in staat:

- medicatie die tijdens de dag gegeven moet worden, met de dosis en het moment
- de huisarts
- een tweede noodnummer, voor als het eerste niet opneemt
- wie het kind mag ophalen, en of het alleen naar huis mag
- eten buiten een allergie (vegetarisch, geen varkensvlees)
- wat helpt als het je kind te veel wordt
- school en leerjaar

Ook: een ouder kan zijn eigen wachtwoord niet wijzigen en er is geen
"wachtwoord vergeten" op de loginpagina. Daarom staat in de kampmail dat Kim
het wachtwoord aanpast als ze het vraagt.
