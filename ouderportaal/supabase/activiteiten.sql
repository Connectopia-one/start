-- ============================================================
-- ACTIVITEITEN, AANWEZIGHEDEN EN CASH
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
-- Later die dag kwam de facturatie erbij: "als ik dan in billit gewoon kan
-- ingeven bijvoorbeeld 5 x les young engineer, of 4 x plusklas (...) zo kan ik
-- maandelijks aangeven wat hun factuur is", "kan ik dan ergens de
-- aanwezigheden aanduiden of de begeleiders" en "sommige ouders betalen cash.
-- Die centjes moet ik storten en dan linken aan 1 of meer facturen."
--
-- En: "of als ouders al betaald hebben (...) dat ik achteraf een voldaan
-- factuur kan sturen."
--
-- Vandaar drie dingen erbij: een factuurregel en een prijs per activiteit,
-- een aanwezigheid per deelname, en een boekje met wat er al betaald is,
-- cash of per overschrijving.
--
-- Dit bestand mag meerdere keren gedraaid worden: alles staat in "if not
-- exists". Draai het dus gerust opnieuw, ook als je het al eens gedraaid hebt.

create table if not exists public.activiteiten (
  id uuid primary key default gen_random_uuid(),
  naam text not null,
  -- kamp, les, pluswerking, plusklas, ... Vrije tekst, zodat er geen migratie
  -- nodig is als er een soort bijkomt.
  soort text not null default 'kamp',
  -- Eén dag heeft een datum; een wekelijkse les niet. Daarom mag die leeg
  -- blijven: de lijst zet de dagen op volgorde en de rest erachter. Voor het
  -- maandoverzicht is een datum wel nodig: zonder datum valt een activiteit in
  -- geen enkele maand.
  datum date,
  plaats text,
  -- Een kamp dat voorbij is, verdwijnt niet maar gaat naar het archief, zodat
  -- de lijst van vorig jaar leesbaar blijft.
  archief boolean not null default false,
  created_at timestamptz not null default now()
);

-- Wat er op de factuur komt te staan, bijvoorbeeld "Les Young Engineers".
-- Het maandoverzicht telt alles met dezelfde regel samen, dus die tekst hoort
-- gelijk te zijn bij elke dag van dezelfde reeks. Blijft ze leeg, dan wordt de
-- soort gebruikt.
alter table public.activiteiten add column if not exists factuurregel text;
-- Wat één keer meedoen kost, per kind. Mag leeg: dan rekent het overzicht geen
-- bedrag en typ je het zelf in Billit.
alter table public.activiteiten add column if not exists prijs numeric(8, 2);

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

-- De aanwezigheid van die dag: waar, niet waar, of leeg zolang niemand het
-- aanduidde. Leeg telt mee op de factuur, want een kind dat ingeschreven staat
-- en niet afgemeld is, komt. Enkel een uitdrukkelijke "afwezig" valt eraf.
alter table public.deelnames add column if not exists aanwezig boolean;

create index if not exists deelnames_kind_idx on public.deelnames (kind_id);

-- Geld dat al binnen is voor er een factuur bestaat: cash in de hand op een
-- kampdag, of een overschrijving die vooraf komt. Daarmee weet het
-- maandoverzicht of een factuur als voldaan verstuurd mag worden.
--
-- Bij cash blijft `gestort_op` leeg zolang het geld in de kas zit. Let op bij
-- het boeken: een storting is geen tweede inkomst, enkel geld dat van de kas
-- naar de rekening gaat.
create table if not exists public.ontvangsten (
  id uuid primary key default gen_random_uuid(),
  -- Van welk gezin. Mag leeg blijven staan als dat gezin ooit verdwijnt; het
  -- bedrag zelf mag niet uit het kasboek vallen.
  profile_id uuid references public.profiles(id) on delete set null,
  datum date not null default current_date,
  bedrag numeric(8, 2) not null,
  -- cash of overschrijving. Vrije tekst, zodat er later iets bij kan.
  wijze text not null default 'cash',
  opmerking text,
  -- Enkel voor cash: de dag waarop het naar de rekening ging.
  gestort_op date,
  created_at timestamptz not null default now()
);

create index if not exists ontvangsten_open_idx
  on public.ontvangsten (gestort_op);
create index if not exists ontvangsten_gezin_idx
  on public.ontvangsten (profile_id);

-- ============================================================
-- De twee hulpfuncties, voor de zekerheid
-- ============================================================
--
-- De regels hieronder steunen op is_staff() en is_beheerder(). Die staan in
-- schema.sql, maar dat bestand is niet meer gedraaid sinds de rol leerkracht
-- erbij kwam, en dan bestaat is_staff() nog niet: "function public.is_staff()
-- does not exist", en omdat de sql-editor alles als één geheel draait rolt dan
-- het hele bestand terug. Daarom staan ze hier ook. Create or replace: bestaan
-- ze al, dan verandert er niets aan.
--
-- Let op: dit is een kopie van wat in schema.sql staat. Verander je daar iets
-- aan de twee functies, verander het hier mee.

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

create or replace function public.is_staff()
returns boolean
language sql
security definer
set search_path = public
stable
as $$
  select exists (
    select 1 from public.profiles
    where id = auth.uid() and role in ('beheerder', 'leerkracht')
  );
$$;

alter table public.activiteiten enable row level security;
alter table public.deelnames enable row level security;
alter table public.ontvangsten enable row level security;

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

-- Het kasboek is geld: enkel de beheerder, ook om te lezen. Een begeleider
-- mag de aanwezigheden aanduiden, maar heeft hier niets te zoeken.
drop policy if exists "ontvangsten beheer" on public.ontvangsten;
create policy "ontvangsten beheer" on public.ontvangsten for all
  using (public.is_beheerder()) with check (public.is_beheerder());

notify pgrst, 'reload schema';

-- Zo zie je aan een rij dat het gelukt is, in plaats van aan
-- "Success. No rows returned".
select
  (select count(*) from public.activiteiten) as activiteiten,
  (select count(*) from public.deelnames) as deelnames,
  (select count(*) from public.ontvangsten) as ontvangsten,
  'activiteiten.sql is gedraaid' as resultaat;
