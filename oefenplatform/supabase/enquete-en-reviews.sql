-- ============================================================
-- ENQUÊTE EN REVIEWS
-- ============================================================
-- Eén keer draaien in de SQL-editor van het oefenplatform-project.
-- Mag gerust een tweede keer: niets gaat kapot en niets komt dubbel.
--
-- Waarvoor (Kim, 5 november 2026):
--   * De enquête is privé. Alleen jij leest de antwoorden, in Beheer →
--     Enquêtes en reviews. Ze staat nooit op het platform zelf.
--   * De review is voor iedereen, op het reviewbord (/reviews), in dezelfde
--     post-itstijl als de weetjes. Alleen echte reviews: insturen kan enkel
--     met een account, en niets komt op het bord voor jij het ophangt.
--   * Een testgezin dat allebei instuurde, krijgt pas gratis toegang als jij
--     op "Goedkeuren" klikt. Dan loopt de toegang tot en met 31 augustus 2027.
--   * Een gezin dat al betaalde, krijgt bij goedkeuring de vaste prijs van
--     20 euro per schooljaar, ook als de prijs later stijgt.
--
-- Nieuw op profiles:
--   gratis_tot   een einddatum voor gratis toegang. Staat er een datum, dan
--                heeft het gezin volledige toegang tot en met die dag, los van
--                de code of een betaling. Handig voor de goedgekeurde testers,
--                maar ook voor de nieuwe testers (5 december) en Katrien.
--   vaste_prijs_eur  de prijs die dit gezin blijft betalen (20 voor de
--                eerste kopers die de enquête en review invulden).

alter table public.profiles add column if not exists gratis_tot date;
alter table public.profiles add column if not exists vaste_prijs_eur int
  check (vaste_prijs_eur is null or vaste_prijs_eur between 0 and 500);

-- Een ouder kan zijn eigen profiel niet bijwerken (enkel jij, zie de regel
-- "beheerder profiel beheer" in schema.sql), dus deze twee kolommen kan
-- niemand anders dan jij veranderen.

-- Wie gratis_tot heeft, ziet ook de vragen van de betalende hoofdstukken.
-- Dezelfde functie staat in schema.sql; verander je de ene, verander dan ook
-- de andere.
create or replace function public.heeft_toegang(check_uid uuid)
returns boolean
language sql
security definer
set search_path = public
stable
as $$
  select coalesce((
    select role = 'beheerder' or is_plusklas
      or toegang_schooljaar = public.huidig_schooljaar()
      -- gratis toegang met een einddatum, zie enquete-en-reviews.sql
      or (gratis_tot is not null and gratis_tot >= (now() at time zone 'Europe/Brussels')::date)
    from public.profiles
    where id = check_uid
  ), false);
$$;

-- ------------------------------------------------------------
-- De enquête: één per account, privé.
-- ------------------------------------------------------------
create table if not exists public.enquetes (
  id uuid primary key default gen_random_uuid(),
  profile_id uuid not null unique references public.profiles(id) on delete cascade,
  antwoorden jsonb not null,
  ingestuurd_op timestamptz not null default now(),
  bijgewerkt_op timestamptz not null default now()
);

alter table public.enquetes enable row level security;

drop policy if exists "eigen enquête of beheerder lezen" on public.enquetes;
create policy "eigen enquête of beheerder lezen" on public.enquetes
  for select using (profile_id = auth.uid() or public.is_beheerder());

drop policy if exists "eigen enquête insturen" on public.enquetes;
create policy "eigen enquête insturen" on public.enquetes
  for insert to authenticated with check (profile_id = auth.uid());

drop policy if exists "eigen enquête aanpassen" on public.enquetes;
create policy "eigen enquête aanpassen" on public.enquetes
  for update using (profile_id = auth.uid()) with check (profile_id = auth.uid());

drop policy if exists "beheerder wist enquête" on public.enquetes;
create policy "beheerder wist enquête" on public.enquetes
  for delete using (public.is_beheerder());

-- ------------------------------------------------------------
-- De review: één per account, pas zichtbaar na ophangen.
-- ------------------------------------------------------------
create table if not exists public.reviews (
  id uuid primary key default gen_random_uuid(),
  profile_id uuid not null unique references public.profiles(id) on delete cascade,
  tekst text not null check (char_length(tekst) between 20 and 1200),
  sterren int not null check (sterren between 1 and 5),
  -- zoals het gezin het onder de review wil zien, bv. "Anja, mama van Thibo"
  naam_tonen text check (naam_tonen is null or char_length(naam_tonen) between 1 and 60),
  toestemming boolean not null check (toestemming = true),
  goedgekeurd boolean not null default false,
  niet_geplaatst boolean not null default false,
  bericht text,
  aangemaakt_op timestamptz not null default now(),
  opgehangen_op timestamptz
);

create index if not exists reviews_bord_idx
  on public.reviews (goedgekeurd, opgehangen_op desc);

alter table public.reviews enable row level security;

-- Iedereen ziet wat opgehangen is; je eigen review zie je altijd; jij alles.
drop policy if exists "opgehangen reviews lezen" on public.reviews;
create policy "opgehangen reviews lezen" on public.reviews
  for select using (goedgekeurd = true or profile_id = auth.uid() or public.is_beheerder());

drop policy if exists "eigen review insturen" on public.reviews;
create policy "eigen review insturen" on public.reviews
  for insert to authenticated with check (
    profile_id = auth.uid() and goedgekeurd = false and opgehangen_op is null
  );

-- Je eigen review aanpassen kan zolang hij niet hangt, en hij blijft dan
-- wachten: ophangen doet alleen jij.
drop policy if exists "eigen review aanpassen" on public.reviews;
create policy "eigen review aanpassen" on public.reviews
  for update using (profile_id = auth.uid() and goedgekeurd = false)
  with check (profile_id = auth.uid() and goedgekeurd = false and opgehangen_op is null);

drop policy if exists "beheerder hangt reviews op" on public.reviews;
create policy "beheerder hangt reviews op" on public.reviews
  for update using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "beheerder wist reviews" on public.reviews;
create policy "beheerder wist reviews" on public.reviews
  for delete using (public.is_beheerder());

-- ------------------------------------------------------------
-- Jouw goedkeuring: wanneer en wat het gezin kreeg.
-- ------------------------------------------------------------
create table if not exists public.beloningen (
  profile_id uuid primary key references public.profiles(id) on delete cascade,
  soort text not null check (soort in ('gratis_toegang', 'vaste_prijs')),
  goedgekeurd_op timestamptz not null default now()
);

alter table public.beloningen enable row level security;

drop policy if exists "eigen beloning of beheerder lezen" on public.beloningen;
create policy "eigen beloning of beheerder lezen" on public.beloningen
  for select using (profile_id = auth.uid() or public.is_beheerder());

drop policy if exists "beheerder beheert beloningen" on public.beloningen;
create policy "beheerder beheert beloningen" on public.beloningen
  for all using (public.is_beheerder()) with check (public.is_beheerder());
