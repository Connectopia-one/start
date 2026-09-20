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
| De kleuren van de hele site              | `app/globals.css`            |

## Een paar dingen die vaak voorkomen

**Een sponsor toevoegen.** Zet het logo in `public/sponsors/` en voeg in
`content/sponsors.ts` een regel toe met de bestandsnaam. Heb je nog geen logo,
laat `logo` dan weg: dan komt de naam in tekst te staan.

**Een blogbericht schrijven.** Voeg in `content/blog.ts` onderaan een blok toe.
Het bericht met de nieuwste datum komt vanzelf bovenaan.

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
