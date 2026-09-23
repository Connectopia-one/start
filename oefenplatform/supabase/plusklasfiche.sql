-- ============================================================
-- OPVOLGFICHE VOOR DE PLUSKLAS — /begeleiding
-- ============================================================
-- Een achterliggende fiche per kind van de externe plusklas, waar jij en de
-- begeleiders opmerkingen bij schrijven, de voortgang apart opvolgen en werk
-- dat thuis gemaakt is als pdf bijhouden. Bedoeld om erbij te nemen op een
-- oudercontact.
--
-- WIE ZIET WAT
--   * De fiche is enkel voor jou (beheerder) en voor accounts met de nieuwe
--     rol "begeleider". Ouders en kinderen zien er NIETS van — ook niet hun
--     eigen fiche. Dat is met opzet: een begeleider moet vrijuit kunnen
--     noteren, en jij beslist zelf wat je op een oudercontact toont.
--   * Enkel kinderen van een gezin met een plusklascode (is_plusklas) komen
--     op de fiche. Van andere gezinnen kan een begeleider niets zien.
--
-- Voer dit één keer uit in de SQL Editor van het Supabase-project van het
-- OEFENPLATFORM. Een tweede keer draaien kan geen kwaad.


-- ------------------------------------------------------------
-- 1. De rol "begeleider"
-- ------------------------------------------------------------
-- Naast 'ouder' en 'beheerder'. Een begeleider komt NIET in /beheer: die kan
-- geen vakken, codes of betalingen aanraken, enkel de fiches.
alter table public.profiles drop constraint if exists profiles_role_check;
alter table public.profiles add constraint profiles_role_check
  check (role in ('ouder', 'beheerder', 'begeleider'));

create or replace function public.is_begeleider()
returns boolean
language sql
security definer
set search_path = public
stable
as $$
  select exists (
    select 1 from public.profiles
    where id = auth.uid() and role in ('beheerder', 'begeleider')
  );
$$;

-- Hoort dit kind bij een gezin dat met een plusklascode registreerde?
create or replace function public.is_plusklas_kind(check_kind uuid)
returns boolean
language sql
security definer
set search_path = public
stable
as $$
  select exists (
    select 1
    from public.kinderen k
    join public.profiles p on p.id = k.profile_id
    where k.id = check_kind and p.is_plusklas
  );
$$;


-- ------------------------------------------------------------
-- 2. Opmerkingen bij een kind
-- ------------------------------------------------------------
-- Eén rij per notitie. We bewaren de naam van wie schreef als gewone tekst
-- naast de verwijzing, zodat er bij een oudercontact nog altijd een naam
-- staat als dat account later verdwijnt.
create table if not exists public.kind_notities (
  id uuid primary key default gen_random_uuid(),
  kind_id uuid not null references public.kinderen(id) on delete cascade,
  -- De datum waarover de notitie gaat. Mag een andere dag zijn dan vandaag,
  -- bv. als je het pas 's avonds ingeeft.
  datum date not null default current_date,
  soort text not null default 'opmerking'
    check (soort in ('opmerking', 'afspraak', 'oudercontact')),
  tekst text not null,
  auteur_id uuid references public.profiles(id) on delete set null,
  auteur_naam text,
  created_at timestamptz not null default now()
);

create index if not exists kind_notities_kind_idx
  on public.kind_notities (kind_id, datum desc);


-- ------------------------------------------------------------
-- 3. Werk dat thuis gemaakt is
-- ------------------------------------------------------------
create table if not exists public.kind_documenten (
  id uuid primary key default gen_random_uuid(),
  kind_id uuid not null references public.kinderen(id) on delete cascade,
  titel text not null,
  bestandspad text not null,
  omschrijving text,
  datum date not null default current_date,
  auteur_id uuid references public.profiles(id) on delete set null,
  auteur_naam text,
  created_at timestamptz not null default now()
);

create index if not exists kind_documenten_kind_idx
  on public.kind_documenten (kind_id, datum desc);


-- ------------------------------------------------------------
-- 4. Wie mag wat
-- ------------------------------------------------------------
alter table public.kind_notities enable row level security;
alter table public.kind_documenten enable row level security;

-- Enkel beheerder en begeleider, en enkel bij een plusklaskind.
-- Er is met opzet GEEN leesregel voor ouders.
drop policy if exists "begeleider notities" on public.kind_notities;
create policy "begeleider notities" on public.kind_notities for all
  using (public.is_begeleider() and public.is_plusklas_kind(kind_id))
  with check (public.is_begeleider() and public.is_plusklas_kind(kind_id));

drop policy if exists "begeleider documenten" on public.kind_documenten;
create policy "begeleider documenten" on public.kind_documenten for all
  using (public.is_begeleider() and public.is_plusklas_kind(kind_id))
  with check (public.is_begeleider() and public.is_plusklas_kind(kind_id));

-- Om een fiche te kunnen tonen moet een begeleider ook het kind, de naam van
-- het gezin, de voortgang en de stickers kunnen lezen. Telkens enkel voor
-- plusklasgezinnen; de bestaande regels voor ouders en beheerder blijven staan.
drop policy if exists "begeleider plusklaskinderen lezen" on public.kinderen;
create policy "begeleider plusklaskinderen lezen" on public.kinderen for select
  using (public.is_begeleider() and public.is_plusklas_kind(id));

drop policy if exists "begeleider plusklasgezin lezen" on public.profiles;
create policy "begeleider plusklasgezin lezen" on public.profiles for select
  using (public.is_begeleider() and is_plusklas);

drop policy if exists "begeleider plusklasvoortgang lezen" on public.voortgang;
create policy "begeleider plusklasvoortgang lezen" on public.voortgang for select
  using (public.is_begeleider() and public.is_plusklas_kind(kind_id));

drop policy if exists "begeleider plusklasstickers lezen" on public.stickers;
create policy "begeleider plusklasstickers lezen" on public.stickers for select
  using (public.is_begeleider() and public.is_plusklas_kind(kind_id));


-- ------------------------------------------------------------
-- 5. De opslagmap voor het werk
-- ------------------------------------------------------------
-- Deze map staat NIET op publiek, anders dan die van "Handig materiaal":
-- hier zit werk van kinderen in. Het platform maakt telkens een tijdelijke
-- link aan om een document te openen.
insert into storage.buckets (id, name, public)
values ('kinddossier', 'kinddossier', false)
on conflict (id) do update set public = false;

drop policy if exists "kinddossier lezen" on storage.objects;
create policy "kinddossier lezen" on storage.objects for select
  using (bucket_id = 'kinddossier' and public.is_begeleider());

drop policy if exists "kinddossier schrijven" on storage.objects;
create policy "kinddossier schrijven" on storage.objects for insert
  with check (bucket_id = 'kinddossier' and public.is_begeleider());

drop policy if exists "kinddossier verwijderen" on storage.objects;
create policy "kinddossier verwijderen" on storage.objects for delete
  using (bucket_id = 'kinddossier' and public.is_begeleider());
