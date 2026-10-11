-- ============================================================
-- ACTIVITEITEN EN DEELNAMES
-- ============================================================
--
-- Kim op 11 oktober 2026: "ik zou eigenlijk echt een apart blad willen hebben,
-- ik kan desnoods de kinderen met een knop zelf in de juiste categorie
-- indelen? Mss dat ik als de inlichtingsfiche ingevuld is ik kan aanduiden bij
-- welk kamp of les dit kind hoort? En zo kan een kind bij verschillende dingen
-- aangeduid zijn, kinderen die zowel naar lessen en kampen komen enzo."
--
-- Daarom twee tabellen. `activiteiten` is de lijst met kampdagen, lessen en
-- werkingen; `deelnames` koppelt een kind aan zo'n activiteit. Een kind mag in
-- zoveel activiteiten staan als nodig, en een activiteit heeft zoveel kinderen
-- als nodig. Dat is iets anders dan wat een ouder op het inschrijfformulier
-- aankruiste: dat blijft in `aanvragen` staan en is een aanvraag, geen
-- deelname. Hier staat wat Kim zelf bevestigd heeft.
--
-- Dit bestand mag meerdere keren gedraaid worden.

create table if not exists public.activiteiten (
  id uuid primary key default gen_random_uuid(),
  naam text not null,
  -- kamp, les, pluswerking, plusklas, ... Vrije tekst, zodat er geen migratie
  -- nodig is als er een soort bijkomt.
  soort text not null default 'kamp',
  -- Eén dag heeft een datum; een wekelijkse les niet. Daarom mag die leeg
  -- blijven: de lijst zet de dagen op volgorde en de rest erachter.
  datum date,
  plaats text,
  -- Een kamp dat voorbij is, verdwijnt niet maar gaat naar het archief, zodat
  -- de lijst van vorig jaar leesbaar blijft.
  archief boolean not null default false,
  created_at timestamptz not null default now()
);

create table if not exists public.deelnames (
  activiteit_id uuid not null
    references public.activiteiten(id) on delete cascade,
  kind_id uuid not null references public.kinderen(id) on delete cascade,
  -- Iets dat enkel voor deze activiteit geldt: "komt pas om 10u", "gaat met
  -- de buren mee naar huis".
  notitie text,
  created_at timestamptz not null default now(),
  primary key (activiteit_id, kind_id)
);

create index if not exists deelnames_kind_idx on public.deelnames (kind_id);

alter table public.activiteiten enable row level security;
alter table public.deelnames enable row level security;

-- Het team mag de lijsten lezen, want zij staan op een kampdag mee in de zaal.
-- Aanmaken, wijzigen en verwijderen blijft bij de beheerder.
drop policy if exists "activiteiten lezen" on public.activiteiten;
create policy "activiteiten lezen" on public.activiteiten for select
  using (public.is_staff());

drop policy if exists "activiteiten beheer" on public.activiteiten;
create policy "activiteiten beheer" on public.activiteiten for all
  using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "deelnames lezen" on public.deelnames;
create policy "deelnames lezen" on public.deelnames for select
  using (public.is_staff());

drop policy if exists "deelnames beheer" on public.deelnames;
create policy "deelnames beheer" on public.deelnames for all
  using (public.is_beheerder()) with check (public.is_beheerder());

notify pgrst, 'reload schema';

-- Zo zie je aan een rij dat het gelukt is, in plaats van aan
-- "Success. No rows returned".
select
  (select count(*) from public.activiteiten) as activiteiten,
  (select count(*) from public.deelnames) as deelnames,
  'activiteiten.sql is gedraaid' as resultaat;
