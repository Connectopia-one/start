-- Prikbord Connectopia — databaseschema
-- Plak dit volledige bestand in het Supabase dashboard onder "SQL Editor" en klik "Run".
-- Dit is dezelfde Supabase als het ouderportaal; de tabellen staan los van elkaar.
-- Kan meerdere keren veilig uitgevoerd worden.

create extension if not exists pgcrypto;

-- ============================================================
-- TABELLEN
-- ============================================================

-- Eén rij per briefje dat op het prikbord hangt.
-- "naam" is de voornaam die op het briefje komt te staan, dus publiek.
-- "volledige_naam" en "contact" zijn voor ons, zodat we weten wie iets
-- ophing. Die twee zijn NIET publiek: bezoekers mogen die kolommen niet
-- lezen, zie de rechten onderaan.
create table if not exists public.prikbord_briefjes (
  id uuid primary key default gen_random_uuid(),
  bord text not null check (
    bord in ('zoekertjes', 'samenkomen', 'aanraders', 'uitgezocht', 'momenten')
  ),
  tekst text not null check (char_length(tekst) between 2 and 600),
  naam text check (char_length(naam) <= 60),
  volledige_naam text check (char_length(volledige_naam) <= 120),
  contact text check (char_length(contact) <= 120),
  wanneer text check (char_length(wanneer) <= 120),
  zichtbaar boolean not null default true,
  gemeld integer not null default 0,
  -- Heeft iemand van ons dit briefje al gezien? Het beheerscherm in het
  -- ouderportaal toont de nieuwe briefjes bovenaan en telt ze.
  gezien boolean not null default false,
  created_at timestamptz not null default now()
);

create index if not exists prikbord_briefjes_bord_idx
  on public.prikbord_briefjes (bord, created_at desc);

-- Voor een databank die al bestond voor "gezien" erbij kwam.
alter table public.prikbord_briefjes
  add column if not exists gezien boolean not null default false;
alter table public.prikbord_briefjes
  add column if not exists volledige_naam text;

-- Eén rij per melding "hier klopt iets niet".
create table if not exists public.prikbord_meldingen (
  id uuid primary key default gen_random_uuid(),
  briefje_id uuid not null references public.prikbord_briefjes(id) on delete cascade,
  reden text check (char_length(reden) <= 400),
  afgehandeld boolean not null default false,
  created_at timestamptz not null default now()
);

-- ============================================================
-- AUTOMATISCH VERBERGEN NA MELDINGEN
-- Vanaf DRIE meldingen gaat een briefje vanzelf van het bord. Het is niet
-- weg: jij ziet het bij beheer en kan het terugzetten of verwijderen.
-- Wil je een ander aantal? Verander de 3 hieronder en voer het bestand opnieuw uit.
-- ============================================================
create or replace function public.prikbord_tel_melding()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  update public.prikbord_briefjes
     set gemeld = gemeld + 1,
         zichtbaar = case when gemeld + 1 >= 3 then false else zichtbaar end
   where id = new.briefje_id;
  return new;
end;
$$;

drop trigger if exists prikbord_melding_geteld on public.prikbord_meldingen;
create trigger prikbord_melding_geteld
  after insert on public.prikbord_meldingen
  for each row execute function public.prikbord_tel_melding();

-- ============================================================
-- RECHTEN
-- Bezoekers van de website (de rol "anon") mogen:
--   - de zichtbare briefjes lezen, zonder de volledige naam en het mailadres
--   - een briefje ophangen
--   - een melding maken
-- Ze mogen niets wijzigen of verwijderen. Dat kan alleen via het beheer
-- in het ouderportaal, dat de service-role sleutel gebruikt.
-- ============================================================

alter table public.prikbord_briefjes enable row level security;
alter table public.prikbord_meldingen enable row level security;

drop policy if exists "iedereen leest zichtbare briefjes" on public.prikbord_briefjes;
create policy "iedereen leest zichtbare briefjes"
  on public.prikbord_briefjes for select
  to anon, authenticated
  using (zichtbaar);

drop policy if exists "iedereen hangt een briefje op" on public.prikbord_briefjes;
create policy "iedereen hangt een briefje op"
  on public.prikbord_briefjes for insert
  to anon, authenticated
  with check (true);

drop policy if exists "iedereen kan melden" on public.prikbord_meldingen;
create policy "iedereen kan melden"
  on public.prikbord_meldingen for insert
  to anon, authenticated
  with check (true);

-- Kolomrechten: de volledige naam en het mailadres blijven binnen.
revoke all on public.prikbord_briefjes from anon, authenticated;
grant select (id, bord, tekst, naam, wanneer, created_at)
  on public.prikbord_briefjes to anon, authenticated;
grant insert (bord, tekst, naam, volledige_naam, contact, wanneer)
  on public.prikbord_briefjes to anon, authenticated;

revoke all on public.prikbord_meldingen from anon, authenticated;
grant insert (briefje_id, reden) on public.prikbord_meldingen to anon, authenticated;
