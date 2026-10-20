-- De gids "Waar kan je terecht": organisaties die iemand aanbrengt
-- Plak dit volledige bestand in het Supabase dashboard onder "SQL Editor" en klik "Run".
-- Dit is dezelfde Supabase als het ouderportaal; de tabellen staan los van elkaar.
-- Kan meerdere keren veilig uitgevoerd worden.

create extension if not exists pgcrypto;

-- ============================================================
-- DE TABEL
-- Eén rij per organisatie die iemand via het formulier onderaan
-- /waar-kan-je-terecht aanbracht.
--
-- "volledige_naam" en "contact" zijn van wie het formulier invulde. Die
-- twee zijn NIET publiek: bezoekers mogen die kolommen niet lezen, zie de
-- rechten onderaan.
--
-- "zichtbaar" staat standaard op false. Een organisatie staat dus pas in
-- de gids als jij ze goedkeurt in het ouderportaal. Daar kan je de
-- omschrijving eerst nog aanpassen, zodat ze even lang is als de andere.
-- ============================================================

create table if not exists public.gids_aanmeldingen (
  id uuid primary key default gen_random_uuid(),
  naam text not null check (char_length(naam) between 2 and 120),
  omschrijving text not null check (char_length(omschrijving) between 10 and 400),
  regio text check (char_length(regio) <= 80),
  link text check (link like 'https://%' and char_length(link) <= 400),
  -- Brengt iemand zichzelf aan, of iemand anders?
  wie text not null default 'zelf' check (wie in ('zelf', 'iemand')),
  zichtbaar boolean not null default false,
  gezien boolean not null default false,
  volledige_naam text check (char_length(volledige_naam) <= 120),
  contact text check (char_length(contact) <= 120),
  -- Een logo in de open bak "social", map gids/. Zie gids-logo.sql.
  logo text check (char_length(logo) <= 300),
  created_at timestamptz not null default now()
);

create index if not exists gids_aanmeldingen_zichtbaar_idx
  on public.gids_aanmeldingen (zichtbaar);

-- ============================================================
-- RECHTEN
-- Bezoekers van de website (de rol "anon") mogen:
--   - de goedgekeurde organisaties lezen, zonder de naam en het mailadres
--     van wie ze aanbracht
--   - zelf een organisatie aanbrengen, die nog niet zichtbaar is
-- Ze mogen niets wijzigen of verwijderen, en ze kunnen hun aanmelding niet
-- zelf zichtbaar maken: "zichtbaar" staat niet in de lijst hieronder.
-- Goedkeuren gebeurt alleen via het beheer in het ouderportaal.
-- ============================================================

alter table public.gids_aanmeldingen enable row level security;

drop policy if exists "iedereen leest goedgekeurde organisaties" on public.gids_aanmeldingen;
create policy "iedereen leest goedgekeurde organisaties"
  on public.gids_aanmeldingen for select
  to anon, authenticated
  using (zichtbaar);

drop policy if exists "iedereen brengt een organisatie aan" on public.gids_aanmeldingen;
create policy "iedereen brengt een organisatie aan"
  on public.gids_aanmeldingen for insert
  to anon, authenticated
  with check (true);

revoke all on public.gids_aanmeldingen from anon, authenticated;
grant select (id, naam, omschrijving, regio, link, logo)
  on public.gids_aanmeldingen to anon, authenticated;
grant insert (naam, omschrijving, regio, link, wie, volledige_naam, contact)
  on public.gids_aanmeldingen to anon, authenticated;

-- De tussenlaag van Supabase laten herlezen welke tabellen er zijn.
notify pgrst, 'reload schema';

-- Zie je deze rij, dan staat de tabel er echt.
select 'gids_aanmeldingen staat klaar' as resultaat, count(*) as aantal
  from public.gids_aanmeldingen;
