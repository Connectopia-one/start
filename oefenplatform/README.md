# Oefenplatform Connectopia

Een online oefenplatform waar kinderen interactief kunnen oefenen op de leerstof van de
examencommissie — per vak opgedeeld in hoofdstukken met meerkeuzevragen, waar/niet-waar-vragen
en invuloefeningen.

**Toegangsmodel:**
- Van elk vak is het **eerste hoofdstuk gratis** te proberen, voor iedereen — ook zonder account.
- Kinderen van de **externe plusklas** hebben gratis **volledige** toegang (via een toegangscode
  bij registratie).
- Andere ouders kunnen **volledige toegang vrijgeven voor €50 per schooljaar** (via Mollie,
  betaald per schooljaar opnieuw) — die opbrengsten gaan volledig naar vzw Connectopia.

Dit is een volledig apart platform/project, los van het ouderportaal (`ouderportaal/`) — met een
eigen Supabase-project en een eigen login-systeem waarop ouders zichzelf kunnen registreren.

**Categorieën (niveaus):** vóór een kind een vak kiest, kiest het eerst een categorie — gebaseerd
op de vakfiches van het Belgisch onderwijs, maar bewust bedoeld als een **kunnen**-indeling, niet
als een strikte leeftijds- of leerjaarregel. Een kind mag gerust een categorie hoger of lager
oefenen dan de klas waarin het zit:

| Categorie | Leerjaar |
|---|---|
| 🌱 Start | 5de & 6de leerjaar |
| ✨ Spark | 1ste & 2de middelbaar |
| 🚀 Boost | 3de & 4de middelbaar |
| 🌍 Beyond | 5de & 6de middelbaar |

Elk hoofdstuk hoort bij precies één categorie (ingesteld bij het aanmaken in `/beheer/vakken`).
Een vak zoals "Wiskunde" kan best hoofdstukken in meerdere categorieën hebben.

## Hoe dit werkt

- **Next.js** — de website zelf (deze map).
- **Supabase** — een NIEUW, apart gratis account voor de database en het login-systeem
  (gebruik niet hetzelfde Supabase-project als het ouderportaal).
- **Mollie** — voor het innen van de betalingen richting de vzw.
- **Vercel** — om de site online te zetten.

## Eenmalige opzet

### 1. Supabase-project aanmaken

1. Ga naar [supabase.com](https://supabase.com) en maak een **nieuw** project aan (regio EU voor
   GDPR), los van het ouderportaal-project.
2. Open **SQL Editor**, plak de volledige inhoud van [`supabase/schema.sql`](./supabase/schema.sql)
   en klik **Run**. Dit maakt de tabellen, beveiligingsregels aan, én een voorbeeldvak
   ("Nederlands") met één gratis hoofdstuk en drie voorbeeldvragen, zodat de site meteen iets
   toont.
3. Onder **Authentication → Providers**, zorg dat e-mail/wachtwoord aan staat (standaard aan).
   Onder **Authentication → Settings** kan je kiezen of je e-mailbevestiging wil vereisen bij
   registratie (standaard aan — ouders krijgen dan een bevestigingsmail).

### 2. Mollie-account aanmaken

1. Maak een gratis account op [mollie.com](https://www.mollie.com), gekoppeld aan de vzw
   (rekeningnummer van de vzw invullen zodat betalingen daar terechtkomen).
2. Ga naar **Ontwikkelaars → API-sleutels** en kopieer eerst de **testsleutel** (begint met
   `test_...`) om alles uit te proberen zonder echt geld. Zodra alles werkt, schakel je over naar
   de **livesleutel** (`live_...`).

### 3. Omgevingsvariabelen

1. Kopieer `.env.local.example` naar `.env.local`.
2. Vul de Supabase-waarden in (Project Settings → API) en de Mollie-sleutel.
3. `NEXT_PUBLIC_SITE_URL` moet exact overeenkomen met waar de site online staat (zonder `/` op
   het einde) — Mollie gebruikt dit om bezoekers na betaling terug te sturen.

### 4. Jezelf beheerder maken

1. Registreer jezelf gewoon via de site op `/registreren` (laat het plusklas-code-veld leeg).
2. Bevestig je e-mailadres als dat gevraagd wordt.
3. Zoek je **User UID** op via Supabase dashboard → Authentication → Users.
4. Voer in de SQL Editor uit:
   ```sql
   update public.profiles set role = 'beheerder' where id = 'PLAK-HIER-JOUW-USER-UID';
   ```

### 5. Lokaal uitproberen (optioneel)

```bash
npm install
npm run dev
```
Open [http://localhost:3000](http://localhost:3000).

**Mollie-webhook lokaal testen:** Mollie moet je `/api/mollie/webhook` kunnen bereiken, wat niet
lukt op `localhost`. Gebruik hiervoor een tool als [ngrok](https://ngrok.com) tijdens het testen,
of test de betaalflow pas na het online zetten op Vercel.

### 6. Online zetten via Vercel

1. Nieuw project op [vercel.com](https://vercel.com), deze GitHub-repository, map
   `oefenplatform` als **Root Directory**.
2. Vul dezelfde omgevingsvariabelen in als in stap 3 — met `NEXT_PUBLIC_SITE_URL` op de
   uiteindelijke `vercel.app`-link (of je eigen domein, bv. `oefenen.connectopia.one`).
3. Klik **Deploy**.

## Dagelijks gebruik

Log in op `/beheer` met je beheerdersaccount:

- **Vakken beheren**: vakken en hoofdstukken toevoegen, per hoofdstuk instellen of het gratis is.
- Klik op een hoofdstuk om **vragen** toe te voegen — één voor één via het formulier, of in bulk
  door een JSON-lijst te plakken (handig als je vragen al voorbereidde met DeepSeek/Gemini — het
  gewenste formaat staat op die pagina).
- Op diezelfde pagina, onder **"Leerstof (theorie)"**: upload een PDF-leerbundel voor dat
  hoofdstuk. Kinderen zien die op een apart tabblad ("Leerstof") naast de oefeningen — met
  dezelfde toegang (gratis hoofdstuk = voor iedereen, anders volledige toegang nodig).
- **Plusklas-codes beheren**: maak een code aan (bv. `PLUSKLAS2026`) en deel die met
  plusklas-gezinnen. Wie zich daarmee registreert krijgt automatisch gratis volledige toegang.

Ouders registreren zichzelf op `/registreren` en kunnen op `/betalen` volledige toegang voor het
schooljaar vrijgeven.

## Voortgang &amp; score per kind

Op `/account` kan een ouder één of meerdere kinderen toevoegen (handig als broers/zussen allebei
oefenen via hetzelfde account). Bij het oefenen kiest men — indien er meer dan één kind is —
voor wie de score bijgehouden wordt; bij één kind gebeurt dit automatisch.

- **Ouders** zien op `/account/kinderen/[id]` een rapport per kind: score per hoofdstuk, en
  wanneer het laatst geoefend werd.
- **Jij (beheerder)** ziet op `/beheer/voortgang` een overzicht van alle kinderen, met score en
  aantal beantwoorde vragen, en kan doorklikken naar het rapport per kind.

Elke beantwoorde vraag wordt bewaard (ook bij herkansen) — zo blijft de volledige geschiedenis
zichtbaar, niet enkel de laatste poging. Zonder ingelogd account (bv. bij het gratis
proefhoofdstuk als bezoeker) wordt niets bijgehouden.

## Vraagtypes

| Type | `opties` | `antwoord` |
|---|---|---|
| `meerkeuze` | lijst met keuzeteksten | index van het juiste antwoord (0, 1, 2, ...) |
| `waarofniet` | — | `true` of `false` |
| `invultekst` | — | het juiste antwoord als tekst (hoofdletterongevoelig vergeleken) |

## Beperkingen van deze eerste versie

- Toegang is platformbreed (alles of niets betaald), niet per vak instelbaar — dat kan later
  verfijnd worden.
- Bij meerdere kinderen op één account moet er vóór het oefenen bewust het juiste kind gekozen
  worden — dat wordt onthouden per browser, maar niet automatisch herkend.
- Eén betaling geldt per account voor het volledige lopende schooljaar; verlenging naar een nieuw
  schooljaar vereist een nieuwe betaling (dit zetten we later eventueel om naar een herinnering per
  e-mail).
