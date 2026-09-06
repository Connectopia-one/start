# Ouderportaal Connectopia

Een beveiligde pagina waar ouders met een eigen account inloggen om lesmateriaal
(PDF's, links, aankondigingen) en foto's van het klasje van hun kind te bekijken.

**Belangrijk uitgangspunt:** lesmateriaal en foto's zijn volledig gescheiden.
Per gezin en per klasje kan je onafhankelijk instellen of ze het lesmateriaal
mogen zien, de foto's, allebei, of geen van beide — zo kan een gezin dat niet
fysiek naar het klasje komt wél het materiaal gebruiken, zonder foto's van
andere kinderen te zien.

## Hoe dit werkt

- **Next.js** — de website zelf (deze map).
- **Supabase** — gratis account voor de database, login-systeem en bestandsopslag.
- **Vercel** — gratis account om de site online te zetten, gekoppeld aan deze
  GitHub-repository (elke wijziging die hier gepusht wordt, verschijnt automatisch online).

Je hebt zelf geen technische kennis nodig om dit dagelijks te gebruiken: eenmaal
alles is opgezet, beheer je alles via het scherm onder **/beheer** in je browser.

## Eenmalige opzet

### 1. Supabase-project aanmaken

1. Ga naar [supabase.com](https://supabase.com) en maak een gratis account met je eigen e-mailadres.
2. Maak een nieuw project aan (kies bij voorkeur een regio in de EU, bv. Frankfurt, voor GDPR).
3. Onthoud het wachtwoord dat je instelt voor de database.

### 2. Database inrichten

1. Open in het Supabase dashboard **SQL Editor**.
2. Plak de volledige inhoud van [`supabase/schema.sql`](./supabase/schema.sql) en klik **Run**.
   Dit maakt alle tabellen, beveiligingsregels en de opslagruimtes (`materialen`, `fotos`) aan.

### 3. Je eigen beheerdersaccount aanmaken

1. Ga naar **Authentication → Users → Add user** en maak een account aan met jouw
   eigen e-mailadres en een wachtwoord.
2. Kopieer het **User UID** van dat account.
3. Ga terug naar **SQL Editor** en voer uit (met jouw UID ingevuld):
   ```sql
   insert into public.profiles (id, full_name, role)
   values ('PLAK-HIER-JOUW-USER-UID', 'Kim', 'beheerder')
   on conflict (id) do update set role = 'beheerder';
   ```

### 4. Omgevingsvariabelen

1. Kopieer `.env.local.example` naar `.env.local`.
2. Vul de 3 waarden in vanuit **Project Settings → API** in Supabase:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - `SUPABASE_SERVICE_ROLE_KEY` (geheim — nooit delen, nooit publiek zetten)

### 5. Lokaal uitproberen (optioneel)

```bash
npm install
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) en log in met je beheerdersaccount.

### 6. Online zetten via Vercel

1. Maak een gratis account op [vercel.com](https://vercel.com), bij voorkeur met inloggen via GitHub.
2. Klik **Add New → Project** en kies deze GitHub-repository; wijs de map `ouderportaal`
   aan als project-map ("Root Directory").
3. Vul bij **Environment Variables** dezelfde 3 waarden in als in stap 4.
4. Klik **Deploy**. Je krijgt een link zoals `ouderportaal-connectopia.vercel.app`.

### 7. Eigen domein koppelen (optioneel)

Wil je bijvoorbeeld `ouders.connectopia.one` gebruiken in plaats van de vercel.app-link:
1. Voeg dat domein toe bij je Vercel-project onder **Settings → Domains**.
2. Vercel toont een CNAME-record dat je moet toevoegen bij je domeinbeheer op one.com
   (**Domeinen → connectopia.one → DNS-instellingen**).
3. Na een paar minuten tot uren (DNS heeft tijd nodig) werkt de nieuwe link.

## Dagelijks gebruik

Log in op `/beheer` met je beheerdersaccount:
- **Klasjes** aanmaken.
- **Gezinnen** toevoegen: naam, e-mailadres en een tijdelijk wachtwoord — dat wachtwoord
  deel je zelf veilig met het gezin (bv. persoonlijk of via een aparte, beveiligde weg —
  niet zomaar in een open groepsbericht).
- Per gezin per klasje **lesmateriaal en foto's apart** aan- of uitzetten.
- Per klasje **PDF's, links en aankondigingen** toevoegen, en **foto's** uploaden.
- Onder **Team** accounts aanmaken voor werknemers ("leerkracht"-rol): zij loggen in op
  hetzelfde adres en komen op een beperkt scherm (`/team`) terecht waar ze foto's
  kunnen toevoegen en de inlichtingenfiches kunnen bekijken — klasjes en lesmateriaal
  blijven overal exclusief voor jou.

Ouders loggen in op de hoofdpagina (`/` of `/login`) met het e-mailadres en wachtwoord
dat ze van jou kregen. Via **"Kalender"** zien ze het volledige lesrooster van het
schooljaar, en via **"Mijn gezin"** vullen ze zelf hun contactgegevens en een
inlichtingenfiche per kind in (allergieën, diagnoses, noodcontact, toestemming
foto's/social media) — die kan jij als beheerder raadplegen op de gezinspagina onder
Beheer.

**Belangrijk:** allergieën en diagnoses zijn gevoelige persoonsgegevens (bijzondere
categorie onder de GDPR). De site zorgt dat enkel het gezin zelf en jij als beheerder
dit ooit kunnen zien, maar de wettelijke grondslag (toestemming) en een redelijke
bewaartermijn blijven jouw verantwoordelijkheid als vzw.

Voegde je dit later toe aan een al werkend project? Plak `supabase/schema.sql`
opnieuw in de SQL Editor en klik Run — het bestand is veilig om te herhalen en voegt
enkel ontbrekende tabellen/kolommen toe.

## Beperkingen van deze eerste versie

- Teamleden ("leerkracht"-rol) zien foto's en fiches van **alle** klasjes, niet enkel
  hun eigen klasje — dat kan later verfijnd worden als dat nodig blijkt.
- Een gezin kan zijn wachtwoord nog niet zelf wijzigen in de site — dat kan later
  toegevoegd worden.
- Wachtwoorden worden nu door jou ingesteld en persoonlijk doorgegeven; e-mail-
  uitnodigingen versturen kan later toegevoegd worden zodra er een e-mailservice
  gekoppeld is aan Supabase.
