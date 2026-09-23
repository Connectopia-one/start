# De website van Connectopia

Dit is de publieke website: de startpagina en de acht onderdelen die eraan hangen.

## In het kort

Alle teksten staan in de map `content/`. Je hoeft geen code aan te raken om iets
te veranderen: open het juiste bestand, pas de tekst tussen de aanhalingstekens
aan, en sla op.

## Waar staat wat?

| Wat wil je aanpassen?                   | Bestand                      |
| --------------------------------------- | ---------------------------- |
| Naam, baseline, e-mailadres, het menu    | `content/site.ts`            |
| De teksten op de startpagina             | `content/home.ts`            |
| Ons aanbod: trajecten, data, prijzen     | `content/aanbod.ts`          |
| De wegwijzer voor ouders                 | `content/wegwijzer.ts`       |
| Ons verhaal, de kernwaarden, het team    | `content/over-ons.ts`        |
| De gids met diensten en organisaties     | `content/gids.ts`            |
| Blogberichten                            | `content/blog.ts`            |
| Het prikbord                             | `content/prikbord.ts`        |
| Sponsors en samenwerkingen               | `content/sponsors.ts`        |
| De winactie van het oefenplatform        | `content/winactie.ts`        |
| De kleuren van de hele site              | `app/globals.css`            |

## Een paar dingen die vaak voorkomen

**Een sponsor toevoegen.** Zet het logo in `public/sponsors/` en voeg in
`content/sponsors.ts` een regel toe met de bestandsnaam. Heb je nog geen logo,
laat `logo` dan weg: dan komt de naam in tekst te staan.

**Een blogbericht schrijven.** Voeg in `content/blog.ts` onderaan een blok toe.
Het bericht met de nieuwste datum komt vanzelf bovenaan. De tekst bouw je op
uit stukjes: `tekst` voor een alinea, `kop` voor een tussentitel, `lijst` voor
opsommingen, `afbeelding` voor een foto en `knop` voor een knop naar een andere
site. Bovenaan dat bestand staat uitgelegd hoe elk stukje eruitziet.

**Een foto bij een blogbericht.** Zet het bestand in `public/blog/` en vul in
`content/blog.ts` alleen de bestandsnaam in. Vul je er een `link` bij, dan is
de foto klikbaar.

**Een prijs of datum wijzigen.** Dat staat in `content/aanbod.ts`, bij het
traject zelf.

**Het ouderportaal en het oefenplatform.** Die staan op
`ouders.connectopia.one` en `oefenplatform.connectopia.one`. De adressen staan
in `content/site.ts` bij die twee onderdelen, in de regel `extern`. Verhuist er
ooit iets, dan pas je alleen die regel aan.

**Een extra instapmoment aankondigen.** Bij elk traject in `content/aanbod.ts`
staat een blok `instappen`, met een zin en een lijstje datums. Voeg er een datum
bij of pas de zin aan; laat je de datums leeg, dan toont de site alleen de zin.

**De gratis proefles.** De tekst en de knop staan bovenaan in
`content/aanbod.ts`, bij `proefles`.

**Een stap in de wegwijzer aanpassen.** Elke stap staat in
`content/wegwijzer.ts`. Naast de lijst `punten` kan een stap twee extra dingen
hebben: `nadruk` voor de zin die je wil laten opvallen (die komt in een gekleurd
kader) en `tip` voor een kadertje met een knop. Heeft een stap die niet nodig,
laat ze dan gewoon weg.

**De knoppen Inschrijven en Info aanvragen.** Die staan automatisch bij elk
traject in `content/aanbod.ts`. Voeg je een traject toe, geef het dan een
`slug` (kleine letters en streepjes, bijvoorbeeld `kerstkamp`) en de twee
knoppen en hun formulieren komen er vanzelf bij.

**De vragen op het formulier.** Die staan in `content/formulier.ts`, in de
lijst `velden`. Een vraag bijzetten is één regel; `verplicht: true` betekent
dat een ouder het veld moet invullen. De teksten van de drie soorten
aanvragen (info, inschrijven, proefles) staan in hetzelfde bestand.

**Waar een ingevuld formulier naartoe gaat.** Bovenaan `content/formulier.ts`
staat `verzenden`. Nu staat `webadres` op `null`: dan opent het formulier het
mailprogramma van de ouder met alle antwoorden er al in, klaar om naar
info@matmgroep.com te sturen. Er komt dus geen andere firma aan de gegevens,
maar de ouder moet wel een mailprogramma hebben. Wil je dat het formulier
rechtstreeks verstuurt, neem dan een formulierdienst en zet het webadres dat
je van hen krijgt bij `webadres`. Die dienst verwerkt dan gegevens van
kinderen, dus kies bewust en leg het vast in je privacyverklaring.

**De aankondigingsbalk weghalen.** In `content/home.ts` staat `aankondiging`.
Zet die op `null` en de groene balk verdwijnt.

## De huisstijl

De kleuren en letters staan bovenaan in `app/globals.css`. Ze komen uit de
flyers van Connectopia, zodat drukwerk en website er hetzelfde uitzien.

- Crème `#fbf6ea` als achtergrond, donkergroen `#2f4a22` voor titels en knoppen
- Paars `#5e2d91`, oranje `#d96e25` en blauw `#3d7cb0` als accenten
- Nunito voor alle tekst, Caveat voor de handgeschreven regels

## Lokaal bekijken

```bash
npm install
npm run dev
```

Daarna staat de site op http://localhost:3000.

```bash
npm run build   # controleert of alles klopt
npm run lint
```
