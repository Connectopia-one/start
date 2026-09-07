-- Oefenplatform Connectopia — databaseschema
-- Plak dit volledige bestand in het Supabase dashboard onder "SQL Editor" en klik "Run".
-- Kan meerdere keren veilig uitgevoerd worden (gebruikt "if not exists" / "or replace").
--
-- Dit is een NIEUW, apart Supabase-project — los van het ouderportaal.

create extension if not exists pgcrypto;

-- ============================================================
-- TABELLEN
-- ============================================================

-- Eén rij per account. De id komt overeen met auth.users.id.
create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  full_name text not null,
  role text not null default 'ouder' check (role in ('ouder', 'beheerder')),
  -- gratis volledige toegang voor gezinnen van de externe plusklas
  is_plusklas boolean not null default false,
  -- schooljaar waarvoor betaald werd, bv. "2026-2027" — null = geen betaalde toegang
  toegang_schooljaar text,
  created_at timestamptz not null default now()
);

-- Toegangscodes die je deelt met plusklas-gezinnen bij registratie — geeft
-- automatisch gratis volledige toegang, zonder dat je elk account apart moet aanvinken.
create table if not exists public.plusklas_codes (
  code text primary key,
  label text,
  actief boolean not null default true,
  created_at timestamptz not null default now()
);

-- Vakken (Nederlands, Wiskunde, ...).
-- rekenmachine: toont een tabblad met de GeoGebra-rekenmachine bij elk hoofdstuk
-- van dit vak (aan voor bv. Wiskunde/Natuurwetenschappen, uit voor Nederlands).
create table if not exists public.vakken (
  id uuid primary key default gen_random_uuid(),
  naam text not null,
  slug text not null unique,
  volgorde int not null default 0,
  rekenmachine boolean not null default false,
  created_at timestamptz not null default now()
);

-- Migratie voor databases die dit bestand al eerder draaiden vóór "rekenmachine" bestond.
alter table public.vakken add column if not exists rekenmachine boolean not null default false;

-- Hoofdstukken per vak. Het eerste/gratis hoofdstuk is publiek zichtbaar als
-- gratis proefhoofdstuk; de rest vereist volledige toegang.
-- niveau: gebaseerd op de vakfiches van het Belgisch onderwijs, maar bedoeld
-- als KUNNEN-categorie, niet als vaste leeftijds-/leerjaarindeling:
--   start = 5de/6de leerjaar, spark = 1ste/2de middelbaar,
--   boost = 3de/4de middelbaar, beyond = 5de/6de middelbaar.
create table if not exists public.hoofdstukken (
  id uuid primary key default gen_random_uuid(),
  vak_id uuid not null references public.vakken(id) on delete cascade,
  titel text not null,
  volgnummer int not null default 0,
  gratis boolean not null default false,
  niveau text not null default 'start' check (niveau in ('start', 'spark', 'boost', 'beyond')),
  created_at timestamptz not null default now(),
  unique (vak_id, volgnummer)
);

-- Migratie voor databases die dit bestand al eerder draaiden vóór "niveau" bestond.
alter table public.hoofdstukken add column if not exists niveau text not null default 'start';
do $$
begin
  if not exists (
    select 1 from pg_constraint where conname = 'hoofdstukken_niveau_check'
  ) then
    alter table public.hoofdstukken add constraint hoofdstukken_niveau_check
      check (niveau in ('start', 'spark', 'boost', 'beyond'));
  end if;
end $$;

-- Interactieve vragen per hoofdstuk.
-- type: 'meerkeuze' | 'invultekst' | 'waarofniet'
-- opties: bij meerkeuze een array van keuzeteksten, bv. ["12", "14", "16"]
-- antwoord: bij meerkeuze de index (bv. 1) of tekst; bij invultekst het juiste
--           antwoord als tekst; bij waarofniet true/false.
create table if not exists public.vragen (
  id uuid primary key default gen_random_uuid(),
  hoofdstuk_id uuid not null references public.hoofdstukken(id) on delete cascade,
  volgnummer int not null default 0,
  type text not null check (type in ('meerkeuze', 'invultekst', 'waarofniet')),
  vraag text not null,
  opties jsonb,
  antwoord jsonb not null,
  uitleg text,
  created_at timestamptz not null default now(),
  unique (hoofdstuk_id, volgnummer)
);

-- Opkuis + migratie voor databases die dit bestand al eerder draaiden vóór de
-- unique-regel hierboven bestond: dat liet dubbele voorbeeldvragen ontstaan bij
-- elke herhaalde run. Dit verwijdert dubbels (houdt de oudste per plek) en
-- voegt de regel dan alsnog toe. Veilig om te laten staan — doet niets meer
-- zodra er geen dubbels meer zijn.
delete from public.vragen a
using public.vragen b
where a.hoofdstuk_id = b.hoofdstuk_id
  and a.volgnummer = b.volgnummer
  and (a.created_at, a.id) > (b.created_at, b.id);

do $$
begin
  if not exists (
    select 1 from pg_constraint where conname = 'vragen_hoofdstuk_id_volgnummer_key'
  ) then
    alter table public.vragen add constraint vragen_hoofdstuk_id_volgnummer_key unique (hoofdstuk_id, volgnummer);
  end if;
end $$;

-- Kinderen — een gezinsaccount kan meerdere kinderen registreren (bv. broers/zussen).
create table if not exists public.kinderen (
  id uuid primary key default gen_random_uuid(),
  profile_id uuid not null references public.profiles(id) on delete cascade,
  naam text not null,
  created_at timestamptz not null default now()
);

-- Voortgang — één rij per beantwoorde vraag. Wordt nooit overschreven bij een
-- herkansing (blijft dus een geschiedenis), zodat een rapport ook evolutie kan tonen.
-- gegeven_antwoord: wat het kind precies invulde (index bij meerkeuze, tekst bij
-- invultekst, true/false bij waarofniet) — zodat ouders/beheerder dit kunnen naslaan.
create table if not exists public.voortgang (
  id uuid primary key default gen_random_uuid(),
  kind_id uuid not null references public.kinderen(id) on delete cascade,
  vraag_id uuid not null references public.vragen(id) on delete cascade,
  correct boolean not null,
  gegeven_antwoord jsonb,
  beantwoord_op timestamptz not null default now()
);

-- Migratie voor databases die dit bestand al eerder draaiden vóór "gegeven_antwoord" bestond.
alter table public.voortgang add column if not exists gegeven_antwoord jsonb;

-- Stickers — één rij per hoofdstuk dat een kind ooit volledig correct
-- afwerkte (100%). De unique-regel zorgt dat het slechts één keer geteld
-- wordt, ook als het kind het hoofdstuk later nog eens perfect maakt.
create table if not exists public.stickers (
  id uuid primary key default gen_random_uuid(),
  kind_id uuid not null references public.kinderen(id) on delete cascade,
  hoofdstuk_id uuid not null references public.hoofdstukken(id) on delete cascade,
  verdiend_op timestamptz not null default now(),
  unique (kind_id, hoofdstuk_id)
);

-- Leerstof — leerbundeltjes (meestal PDF's) met de theorie per hoofdstuk,
-- naast de online oefeningen. Volgt dezelfde toegang als de vragen van dat
-- hoofdstuk (gratis hoofdstuk = voor iedereen, anders volledige toegang nodig).
create table if not exists public.leerstof (
  id uuid primary key default gen_random_uuid(),
  hoofdstuk_id uuid not null references public.hoofdstukken(id) on delete cascade,
  titel text not null,
  bestandspad text not null,
  created_at timestamptz not null default now()
);

-- Betalingen — één rij per Mollie-poging. status wordt bijgewerkt door de
-- Mollie-webhook; profiles.toegang_schooljaar wordt pas gezet zodra status = 'betaald'.
create table if not exists public.betalingen (
  id uuid primary key default gen_random_uuid(),
  profile_id uuid not null references public.profiles(id) on delete cascade,
  schooljaar text not null,
  bedrag numeric(6,2) not null,
  mollie_payment_id text unique,
  status text not null default 'open' check (status in ('open', 'betaald', 'mislukt', 'geannuleerd', 'verlopen')),
  created_at timestamptz not null default now(),
  betaald_op timestamptz
);

-- ============================================================
-- HULPFUNCTIES
-- ============================================================

create or replace function public.is_beheerder()
returns boolean
language sql
security definer
set search_path = public
stable
as $$
  select exists (
    select 1 from public.profiles
    where id = auth.uid() and role = 'beheerder'
  );
$$;

-- Zelfde logica als lib/schooljaar.ts — schooljaar start in september.
create or replace function public.huidig_schooljaar()
returns text
language sql
stable
as $$
  select case
    when extract(month from now()) >= 8
      then extract(year from now())::text || '-' || (extract(year from now()) + 1)::text
    else (extract(year from now()) - 1)::text || '-' || extract(year from now())::text
  end;
$$;

-- Heeft dit account volledige toegang (niet enkel de gratis hoofdstukken)?
create or replace function public.heeft_toegang(check_uid uuid)
returns boolean
language sql
security definer
set search_path = public
stable
as $$
  select coalesce((
    select role = 'beheerder' or is_plusklas or toegang_schooljaar = public.huidig_schooljaar()
    from public.profiles
    where id = check_uid
  ), false);
$$;

-- ============================================================
-- ROW LEVEL SECURITY
-- ============================================================

alter table public.profiles enable row level security;
alter table public.plusklas_codes enable row level security;
alter table public.vakken enable row level security;
alter table public.hoofdstukken enable row level security;
alter table public.vragen enable row level security;
alter table public.betalingen enable row level security;
alter table public.kinderen enable row level security;
alter table public.voortgang enable row level security;
alter table public.stickers enable row level security;
alter table public.leerstof enable row level security;

drop policy if exists "eigen profiel lezen" on public.profiles;
create policy "eigen profiel lezen" on public.profiles for select
  using (id = auth.uid() or public.is_beheerder());

drop policy if exists "beheerder profiel beheer" on public.profiles;
create policy "beheerder profiel beheer" on public.profiles for all
  using (public.is_beheerder()) with check (public.is_beheerder());

-- plusklas_codes worden enkel gecontroleerd/beheerd via de server (service-role),
-- nooit rechtstreeks vanuit de browser gelezen of geschreven.
drop policy if exists "beheerder codes beheer" on public.plusklas_codes;
create policy "beheerder codes beheer" on public.plusklas_codes for all
  using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "vakken publiek lezen" on public.vakken;
create policy "vakken publiek lezen" on public.vakken for select
  using (true);

drop policy if exists "beheerder vakken beheer" on public.vakken;
create policy "beheerder vakken beheer" on public.vakken for all
  using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "hoofdstukken publiek lezen" on public.hoofdstukken;
create policy "hoofdstukken publiek lezen" on public.hoofdstukken for select
  using (true);

drop policy if exists "beheerder hoofdstukken beheer" on public.hoofdstukken;
create policy "beheerder hoofdstukken beheer" on public.hoofdstukken for all
  using (public.is_beheerder()) with check (public.is_beheerder());

-- Vragen: enkel zichtbaar als het hoofdstuk gratis is, of als de bezoeker
-- volledige toegang heeft (plusklas, betaald dit schooljaar, of beheerder).
drop policy if exists "vragen lezen" on public.vragen;
create policy "vragen lezen" on public.vragen for select
  using (
    exists (
      select 1 from public.hoofdstukken h
      where h.id = vragen.hoofdstuk_id and h.gratis = true
    )
    or public.heeft_toegang(auth.uid())
  );

drop policy if exists "beheerder vragen beheer" on public.vragen;
create policy "beheerder vragen beheer" on public.vragen for all
  using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "eigen betalingen lezen" on public.betalingen;
create policy "eigen betalingen lezen" on public.betalingen for select
  using (profile_id = auth.uid() or public.is_beheerder());

drop policy if exists "beheerder betalingen beheer" on public.betalingen;
create policy "beheerder betalingen beheer" on public.betalingen for all
  using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "eigen kinderen beheer" on public.kinderen;
create policy "eigen kinderen beheer" on public.kinderen for all
  using (profile_id = auth.uid() or public.is_beheerder())
  with check (profile_id = auth.uid() or public.is_beheerder());

drop policy if exists "eigen kind voortgang lezen" on public.voortgang;
create policy "eigen kind voortgang lezen" on public.voortgang for select
  using (
    public.is_beheerder() or exists (
      select 1 from public.kinderen k where k.id = voortgang.kind_id and k.profile_id = auth.uid()
    )
  );

drop policy if exists "eigen kind voortgang toevoegen" on public.voortgang;
create policy "eigen kind voortgang toevoegen" on public.voortgang for insert
  with check (
    public.is_beheerder() or exists (
      select 1 from public.kinderen k where k.id = voortgang.kind_id and k.profile_id = auth.uid()
    )
  );

drop policy if exists "beheerder voortgang beheer" on public.voortgang;
create policy "beheerder voortgang beheer" on public.voortgang for all
  using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "eigen kind stickers lezen" on public.stickers;
create policy "eigen kind stickers lezen" on public.stickers for select
  using (
    public.is_beheerder() or exists (
      select 1 from public.kinderen k where k.id = stickers.kind_id and k.profile_id = auth.uid()
    )
  );

drop policy if exists "eigen kind stickers toevoegen" on public.stickers;
create policy "eigen kind stickers toevoegen" on public.stickers for insert
  with check (
    public.is_beheerder() or exists (
      select 1 from public.kinderen k where k.id = stickers.kind_id and k.profile_id = auth.uid()
    )
  );

drop policy if exists "beheerder stickers beheer" on public.stickers;
create policy "beheerder stickers beheer" on public.stickers for all
  using (public.is_beheerder()) with check (public.is_beheerder());

-- Leerstof: zelfde toegangslogica als vragen (zie "vragen lezen" hierboven).
drop policy if exists "leerstof lezen" on public.leerstof;
create policy "leerstof lezen" on public.leerstof for select
  using (
    exists (
      select 1 from public.hoofdstukken h
      where h.id = leerstof.hoofdstuk_id and h.gratis = true
    )
    or public.heeft_toegang(auth.uid())
  );

drop policy if exists "beheerder leerstof beheer" on public.leerstof;
create policy "beheerder leerstof beheer" on public.leerstof for all
  using (public.is_beheerder()) with check (public.is_beheerder());

-- ============================================================
-- OPSLAG (bestanden)
-- ============================================================

insert into storage.buckets (id, name, public)
values ('leerstof', 'leerstof', false)
on conflict (id) do nothing;

drop policy if exists "leerstof lezen storage" on storage.objects;
create policy "leerstof lezen storage" on storage.objects for select
  using (
    bucket_id = 'leerstof' and (
      public.is_beheerder() or exists (
        select 1 from public.leerstof l
        join public.hoofdstukken h on h.id = l.hoofdstuk_id
        where l.bestandspad = storage.objects.name
          and (h.gratis = true or public.heeft_toegang(auth.uid()))
      )
    )
  );

drop policy if exists "leerstof schrijven" on storage.objects;
create policy "leerstof schrijven" on storage.objects for insert
  with check (bucket_id = 'leerstof' and public.is_beheerder());

drop policy if exists "leerstof verwijderen" on storage.objects;
create policy "leerstof verwijderen" on storage.objects for delete
  using (bucket_id = 'leerstof' and public.is_beheerder());

-- ============================================================
-- JOUW EIGEN BEHEERDER-ACCOUNT
-- ============================================================
-- Registreer jezelf eerst gewoon via de site (/registreren). Zoek daarna je
-- User UID op via Supabase dashboard -> Authentication -> Users, en voer uit:
--
-- update public.profiles set role = 'beheerder' where id = 'PLAK-HIER-JOUW-USER-UID';

-- ============================================================
-- VOORBEELDINHOUD (mag je aanpassen of verwijderen via /beheer)
-- ============================================================

insert into public.vakken (naam, slug, volgorde)
values ('Nederlands', 'nederlands', 1)
on conflict (slug) do nothing;

insert into public.hoofdstukken (vak_id, titel, volgnummer, gratis)
select id, 'Hoofdstuk 1 — Spelling: voorbeeld', 1, true
from public.vakken where slug = 'nederlands'
on conflict (vak_id, volgnummer) do nothing;

insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 1, 'meerkeuze',
  'Welk woord is correct gespeld?',
  '["hij wordt", "hij word", "hij wort"]'::jsonb,
  '0'::jsonb,
  'Bij de tegenwoordige tijd, 3de persoon enkelvoud, krijgt het werkwoord een -t: "hij wordt".'
from public.hoofdstukken h
join public.vakken v on v.id = h.vak_id
where v.slug = 'nederlands' and h.volgnummer = 1
on conflict (hoofdstuk_id, volgnummer) do nothing;

insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 2, 'waarofniet',
  '"Ik heb gisteren naar de winkel gegaan" is correct Nederlands.',
  null,
  'false'::jsonb,
  'Het moet zijn: "Ik ben gisteren naar de winkel gegaan" — "gaan" gebruikt "zijn" als hulpwerkwoord.'
from public.hoofdstukken h
join public.vakken v on v.id = h.vak_id
where v.slug = 'nederlands' and h.volgnummer = 1
on conflict (hoofdstuk_id, volgnummer) do nothing;

insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 3, 'invultekst',
  'Vul het juiste woord in: De kat ligt ___ de mat. (op / aan)',
  null,
  '"op"'::jsonb,
  '"Op de mat" is de juiste voorzetselcombinatie hier.'
from public.hoofdstukken h
join public.vakken v on v.id = h.vak_id
where v.slug = 'nederlands' and h.volgnummer = 1
on conflict (hoofdstuk_id, volgnummer) do nothing;

-- Wiskunde en Natuurwetenschappen — telkens één hoofdstuk per categorie
-- (start/spark/boost/beyond), zodat er een volledige testpagina is over alle
-- niveaus heen. Enkel het "start"-hoofdstuk is gratis, zoals bij Nederlands.

insert into public.vakken (naam, slug, volgorde, rekenmachine)
values ('Wiskunde', 'wiskunde', 2, true)
on conflict (slug) do nothing;

insert into public.vakken (naam, slug, volgorde, rekenmachine)
values ('Natuurwetenschappen', 'natuurwetenschappen', 3, true)
on conflict (slug) do nothing;

-- Voor bestaande installaties die deze vakken al eerder aanmaakten (dus vóór
-- "rekenmachine" bestond): alsnog aanzetten voor Wiskunde/Natuurwetenschappen.
update public.vakken set rekenmachine = true where slug in ('wiskunde', 'natuurwetenschappen');

insert into public.hoofdstukken (vak_id, titel, volgnummer, gratis, niveau)
select id, 'Rekenen en breuken', 1, true, 'start' from public.vakken where slug = 'wiskunde'
on conflict (vak_id, volgnummer) do nothing;
insert into public.hoofdstukken (vak_id, titel, volgnummer, gratis, niveau)
select id, 'Negatieve getallen en procenten', 2, false, 'spark' from public.vakken where slug = 'wiskunde'
on conflict (vak_id, volgnummer) do nothing;
insert into public.hoofdstukken (vak_id, titel, volgnummer, gratis, niveau)
select id, 'Vergelijkingen en de stelling van Pythagoras', 3, false, 'boost' from public.vakken where slug = 'wiskunde'
on conflict (vak_id, volgnummer) do nothing;
insert into public.hoofdstukken (vak_id, titel, volgnummer, gratis, niveau)
select id, 'Afgeleiden en goniometrie', 4, false, 'beyond' from public.vakken where slug = 'wiskunde'
on conflict (vak_id, volgnummer) do nothing;

insert into public.hoofdstukken (vak_id, titel, volgnummer, gratis, niveau)
select id, 'Ons lichaam en planten', 1, true, 'start' from public.vakken where slug = 'natuurwetenschappen'
on conflict (vak_id, volgnummer) do nothing;
insert into public.hoofdstukken (vak_id, titel, volgnummer, gratis, niveau)
select id, 'Cellen en toestanden van materie', 2, false, 'spark' from public.vakken where slug = 'natuurwetenschappen'
on conflict (vak_id, volgnummer) do nothing;
insert into public.hoofdstukken (vak_id, titel, volgnummer, gratis, niveau)
select id, 'Fotosynthese en atomen', 3, false, 'boost' from public.vakken where slug = 'natuurwetenschappen'
on conflict (vak_id, volgnummer) do nothing;
insert into public.hoofdstukken (vak_id, titel, volgnummer, gratis, niveau)
select id, 'Erfelijkheid en natuurkunde', 4, false, 'beyond' from public.vakken where slug = 'natuurwetenschappen'
on conflict (vak_id, volgnummer) do nothing;

-- Wiskunde — Start
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 1, 'meerkeuze', 'Wat is 3/4 van 100?', '["50", "75", "80"]'::jsonb, '1'::jsonb,
  '3/4 van 100 = 100 : 4 x 3 = 75.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'wiskunde' and h.volgnummer = 1
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 2, 'waarofniet', 'Een rechthoek heeft 4 rechte hoeken.', null, 'true'::jsonb,
  'Een rechthoek heeft per definitie 4 hoeken van 90°.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'wiskunde' and h.volgnummer = 1
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 3, 'invultekst', '7 x 9 = ___', null, '"63"'::jsonb, '7 x 9 = 63.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'wiskunde' and h.volgnummer = 1
on conflict (hoofdstuk_id, volgnummer) do nothing;

-- Wiskunde — Spark
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 1, 'meerkeuze', 'Wat is -5 + 8?', '["3", "-3", "13"]'::jsonb, '0'::jsonb,
  '-5 + 8 = 3.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'wiskunde' and h.volgnummer = 2
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 2, 'waarofniet', 'Een negatief getal vermenigvuldigd met een negatief getal geeft een positief resultaat.', null, 'true'::jsonb,
  'Min keer min is plus.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'wiskunde' and h.volgnummer = 2
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 3, 'invultekst', '20% van 150 is ___', null, '"30"'::jsonb, '20% van 150 = 150 : 100 x 20 = 30.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'wiskunde' and h.volgnummer = 2
on conflict (hoofdstuk_id, volgnummer) do nothing;

-- Wiskunde — Boost
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 1, 'meerkeuze', 'Los op: 2x + 3 = 11. x = ?', '["3", "4", "5"]'::jsonb, '1'::jsonb,
  '2x = 11 - 3 = 8, dus x = 4.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'wiskunde' and h.volgnummer = 3
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 2, 'waarofniet', 'De stelling van Pythagoras geldt enkel voor rechthoekige driehoeken.', null, 'true'::jsonb,
  'Pythagoras is specifiek voor rechthoekige driehoeken.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'wiskunde' and h.volgnummer = 3
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 3, 'invultekst', 'Bij een rechthoekige driehoek met rechthoekszijden 3 en 4 is de schuine zijde ___', null, '"5"'::jsonb,
  '3² + 4² = 9 + 16 = 25 = 5².'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'wiskunde' and h.volgnummer = 3
on conflict (hoofdstuk_id, volgnummer) do nothing;

-- Wiskunde — Beyond
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 1, 'meerkeuze', 'Wat is de afgeleide van x²?', '["x", "2x", "x²"]'::jsonb, '1'::jsonb,
  'De afgeleide van x^n is n·x^(n-1), dus van x² is dat 2x.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'wiskunde' and h.volgnummer = 4
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 2, 'waarofniet', 'sin(90°) = 1', null, 'true'::jsonb,
  'De sinus van 90° is inderdaad 1.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'wiskunde' and h.volgnummer = 4
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 3, 'invultekst', 'log(100) met grondtal 10 = ___', null, '"2"'::jsonb, '10² = 100, dus log₁₀(100) = 2.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'wiskunde' and h.volgnummer = 4
on conflict (hoofdstuk_id, volgnummer) do nothing;

-- Natuurwetenschappen — Start
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 1, 'meerkeuze', 'Welk orgaan pompt het bloed door je lichaam?', '["Longen", "Hart", "Maag"]'::jsonb, '1'::jsonb,
  'Het hart is de pomp van je bloedsomloop.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'natuurwetenschappen' and h.volgnummer = 1
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 2, 'waarofniet', 'Planten hebben licht nodig om te groeien.', null, 'true'::jsonb,
  'Planten gebruiken licht bij fotosynthese om te groeien.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'natuurwetenschappen' and h.volgnummer = 1
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 3, 'invultekst', 'Water bestaat uit waterstof en ___', null, '"zuurstof"'::jsonb,
  'Water (H₂O) bestaat uit waterstof en zuurstof.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'natuurwetenschappen' and h.volgnummer = 1
on conflict (hoofdstuk_id, volgnummer) do nothing;

-- Natuurwetenschappen — Spark
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 1, 'meerkeuze', 'Wat is de kleinste bouwsteen van een levend organisme?', '["Molecule", "Cel", "Atoom"]'::jsonb, '1'::jsonb,
  'De cel is de kleinste levende bouwsteen.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'natuurwetenschappen' and h.volgnummer = 2
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 2, 'waarofniet', 'Water kookt bij 100°C op zeeniveau.', null, 'true'::jsonb,
  'Bij normale luchtdruk kookt water bij 100°C.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'natuurwetenschappen' and h.volgnummer = 2
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 3, 'invultekst', 'De drie toestanden van materie zijn vast, vloeibaar en ___', null, '"gasvormig"'::jsonb,
  'Vast, vloeibaar en gasvormig zijn de drie klassieke toestanden van materie.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'natuurwetenschappen' and h.volgnummer = 2
on conflict (hoofdstuk_id, volgnummer) do nothing;

-- Natuurwetenschappen — Boost
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 1, 'meerkeuze', 'Wat produceren planten tijdens fotosynthese?', '["Zuurstof", "Stikstof", "Koolstofdioxide"]'::jsonb, '0'::jsonb,
  'Bij fotosynthese zetten planten CO₂ en water om in glucose en zuurstof.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'natuurwetenschappen' and h.volgnummer = 3
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 2, 'waarofniet', 'Een atoom bestaat uit protonen, neutronen en elektronen.', null, 'true'::jsonb,
  'Dat zijn de drie basisdeeltjes van een atoom.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'natuurwetenschappen' and h.volgnummer = 3
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 3, 'invultekst', 'Het scheikundig symbool voor het element goud is ___', null, '"Au"'::jsonb,
  'Au komt van het Latijnse "aurum" (goud).'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'natuurwetenschappen' and h.volgnummer = 3
on conflict (hoofdstuk_id, volgnummer) do nothing;

-- Natuurwetenschappen — Beyond
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 1, 'meerkeuze', 'Wat bepaalt de erfelijke eigenschappen van een organisme?', '["DNA", "RNA-polymerase", "Mitochondriën"]'::jsonb, '0'::jsonb,
  'DNA draagt de erfelijke informatie.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'natuurwetenschappen' and h.volgnummer = 4
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 2, 'waarofniet', 'De lichtsnelheid is ongeveer 300.000 km per seconde.', null, 'true'::jsonb,
  'De lichtsnelheid in vacuüm is ongeveer 300.000 km/s.'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'natuurwetenschappen' and h.volgnummer = 4
on conflict (hoofdstuk_id, volgnummer) do nothing;
insert into public.vragen (hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg)
select h.id, 3, 'invultekst', 'De SI-eenheid van kracht is de ___', null, '"newton"'::jsonb,
  'Kracht wordt uitgedrukt in newton (N).'
from public.hoofdstukken h join public.vakken v on v.id = h.vak_id
where v.slug = 'natuurwetenschappen' and h.volgnummer = 4
on conflict (hoofdstuk_id, volgnummer) do nothing;
