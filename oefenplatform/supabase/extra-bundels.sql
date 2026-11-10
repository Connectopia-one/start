-- ============================================================
-- EXTRA BUNDELS PER VAK — los van de hoofdstukken
-- ============================================================
-- Kim, 10 november 2026: per vak een aparte plek voor bundels die niet bij
-- één hoofdstuk horen, maar bij het hele vak. Bijvoorbeeld een examen op
-- papier (met verbetersleutel) of een lesbundel over het hele vak met
-- afbeeldingen.
--
-- Je zet ze erbij op /beheer/extra-bundels. Ze staan op de vakpagina
-- (/niveaus/<niveau>/<vak>) onder "Extra bundels".
--
-- Wie mag wat openen:
--   - een gewone bundel: iedereen met volledige toegang (net als de cursus);
--   - een bundel met "alleen_begeleiding" aan (bv. een verbetersleutel):
--     enkel jij en de begeleiders. Ouders en kinderen zien hem niet eens.
--
-- De opslagmap staat NIET op publiek. Het platform kijkt bij elke klik eerst
-- of je het bestand mag zien en maakt dan een link die één minuut werkt.
--
-- Eén keer uitvoeren in de SQL Editor van het Supabase-project van het
-- OEFENPLATFORM. Een tweede keer draaien kan geen kwaad.

create table if not exists public.extra_bundels (
  id uuid primary key default gen_random_uuid(),
  vak_id uuid not null references public.vakken(id) on delete cascade,
  -- De categorie, zoals bij de hoofdstukken: start, spark, boost-doorstroom, ...
  niveau text not null,
  -- examen, lesbundel of andere. Bepaalt het icoontje en de volgorde.
  soort text not null default 'examen'
    check (soort in ('examen', 'lesbundel', 'andere')),
  titel text not null,
  omschrijving text,
  bestandspad text not null,
  -- Aan = enkel voor beheerder en begeleiders (verbetersleutels).
  alleen_begeleiding boolean not null default false,
  created_at timestamptz not null default now()
);

create index if not exists extra_bundels_vak_idx
  on public.extra_bundels (vak_id, niveau, created_at);

alter table public.extra_bundels enable row level security;

-- Lezen: de gewone bundels mag iedereen in de lijst zien (de knop zelf vraagt
-- volledige toegang). Bundels voor de begeleiding enkel beheerder/begeleider.
drop policy if exists "extra bundels lezen" on public.extra_bundels;
create policy "extra bundels lezen" on public.extra_bundels for select
  using (not alleen_begeleiding or public.is_begeleider());

drop policy if exists "beheerder extra bundels beheer" on public.extra_bundels;
create policy "beheerder extra bundels beheer" on public.extra_bundels for all
  using (public.is_beheerder()) with check (public.is_beheerder());

-- De pdf's zelf. Niet publiek: geen leesregel, het platform haalt ze op met
-- de beheersleutel nadat het zelf de toegang nakeek.
insert into storage.buckets (id, name, public)
values ('extrabundels', 'extrabundels', false)
on conflict (id) do update set public = false;

drop policy if exists "extrabundels schrijven" on storage.objects;
create policy "extrabundels schrijven" on storage.objects for insert
  with check (bucket_id = 'extrabundels' and public.is_beheerder());

drop policy if exists "extrabundels verwijderen" on storage.objects;
create policy "extrabundels verwijderen" on storage.objects for delete
  using (bucket_id = 'extrabundels' and public.is_beheerder());
