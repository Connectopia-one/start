-- ============================================================
-- HANDIG MATERIAAL — de gratis linkenpagina op /materiaal
-- ============================================================
-- Hiermee kan je zelf links en documenten op de pagina "Handig materiaal"
-- zetten, net zoals je dat op het ouderportaal bij een klasje doet. Je beheert
-- ze op /beheer/materiaal; bezoekers zien ze op /materiaal.
--
-- Die pagina is met opzet voor iedereen zichtbaar, ook zonder account en
-- zonder betaling. Daarom mag iedereen hier lezen en enkel jij schrijven.
--
-- Voer dit één keer uit in de SQL Editor van je Supabase-project. Draai je het
-- per ongeluk een tweede keer, dan is dat niet erg: alles staat op "maak enkel
-- aan als het nog niet bestaat".

create table if not exists public.materiaal (
  id uuid primary key default gen_random_uuid(),
  -- De kop waaronder het op de pagina komt, bv. "Wiskunde". Typ je een groep
  -- die nog niet bestaat, dan verschijnt die er vanzelf bij.
  groep text not null default 'Allerlei',
  type text not null check (type in ('link', 'pdf')),
  titel text not null,
  -- Bij een link: het webadres. Bij een pdf blijft dit leeg.
  link text,
  -- Bij een pdf: waar het bestand in de opslag staat. Bij een link leeg.
  bestandspad text,
  -- Eén zin over wat je er vindt. Mag leeg blijven.
  omschrijving text,
  created_at timestamptz not null default now()
);

create index if not exists materiaal_groep_idx
  on public.materiaal (groep, created_at);

alter table public.materiaal enable row level security;

-- Lezen mag iedereen, ook wie niet ingelogd is.
drop policy if exists "materiaal lezen" on public.materiaal;
create policy "materiaal lezen" on public.materiaal for select
  using (true);

drop policy if exists "beheerder materiaal beheer" on public.materiaal;
create policy "beheerder materiaal beheer" on public.materiaal for all
  using (public.is_beheerder()) with check (public.is_beheerder());

-- De documenten zelf. Deze bucket staat op publiek, want de pagina is gratis
-- en een bezoeker zonder account moet het bestand gewoon kunnen openen.
insert into storage.buckets (id, name, public)
values ('materiaal', 'materiaal', true)
on conflict (id) do update set public = true;

drop policy if exists "materiaal lezen storage" on storage.objects;
create policy "materiaal lezen storage" on storage.objects for select
  using (bucket_id = 'materiaal');

drop policy if exists "materiaal schrijven" on storage.objects;
create policy "materiaal schrijven" on storage.objects for insert
  with check (bucket_id = 'materiaal' and public.is_beheerder());

drop policy if exists "materiaal verwijderen" on storage.objects;
create policy "materiaal verwijderen" on storage.objects for delete
  using (bucket_id = 'materiaal' and public.is_beheerder());
