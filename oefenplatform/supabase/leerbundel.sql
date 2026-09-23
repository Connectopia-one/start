-- ============================================================
-- LEERBUNDEL — theorie mét afbeeldingen, in het platform zelf
-- ============================================================
-- Tot nu kon je bij een hoofdstuk enkel een PDF uploaden. Een leerbundel is
-- iets anders: je bouwt ze hier op uit blokjes — een tussentitel, een stuk
-- tekst, een weetje in een kadertje, of een afbeelding met een onderschrift.
-- Zo kan je uitleg afwisselen met beeld, wat voor veel kinderen een pak
-- duidelijker leest dan een lap tekst of een PDF die ze moeten downloaden.
--
-- Voer dit één keer uit in de SQL Editor van je Supabase-project. Draai je het
-- per ongeluk een tweede keer, dan is dat niet erg: alles staat op "maak enkel
-- aan als het nog niet bestaat".

create table if not exists public.leerbundel (
  id uuid primary key default gen_random_uuid(),
  hoofdstuk_id uuid not null references public.hoofdstukken(id) on delete cascade,
  volgnummer int not null default 1,
  soort text not null check (soort in ('titel', 'tekst', 'weetje', 'afbeelding')),
  -- tekst is de inhoud bij een titel, tekst of weetje, en het onderschrift bij
  -- een afbeelding (daar mag het leeg blijven).
  tekst text,
  afbeelding_pad text,
  created_at timestamptz not null default now()
);

create index if not exists leerbundel_hoofdstuk_idx
  on public.leerbundel (hoofdstuk_id, volgnummer);

alter table public.leerbundel enable row level security;

-- Zelfde toegang als de oefenvragen: een gratis hoofdstuk mag iedereen lezen,
-- de rest enkel wie volledige toegang heeft.
drop policy if exists "leerbundel lezen" on public.leerbundel;
create policy "leerbundel lezen" on public.leerbundel for select
  using (
    exists (
      select 1 from public.hoofdstukken h
      where h.id = leerbundel.hoofdstuk_id and h.gratis = true
    )
    or public.heeft_toegang(auth.uid())
  );

drop policy if exists "beheerder leerbundel beheer" on public.leerbundel;
create policy "beheerder leerbundel beheer" on public.leerbundel for all
  using (public.is_beheerder()) with check (public.is_beheerder());

-- De afbeeldingen zelf, in een eigen bucket met dezelfde regels.
insert into storage.buckets (id, name, public)
values ('leerbundel', 'leerbundel', false)
on conflict (id) do nothing;

drop policy if exists "leerbundel lezen storage" on storage.objects;
create policy "leerbundel lezen storage" on storage.objects for select
  using (
    bucket_id = 'leerbundel' and (
      public.is_beheerder() or exists (
        select 1 from public.leerbundel b
        join public.hoofdstukken h on h.id = b.hoofdstuk_id
        where b.afbeelding_pad = storage.objects.name
          and (h.gratis = true or public.heeft_toegang(auth.uid()))
      )
    )
  );

drop policy if exists "leerbundel schrijven" on storage.objects;
create policy "leerbundel schrijven" on storage.objects for insert
  with check (bucket_id = 'leerbundel' and public.is_beheerder());

drop policy if exists "leerbundel verwijderen" on storage.objects;
create policy "leerbundel verwijderen" on storage.objects for delete
  using (bucket_id = 'leerbundel' and public.is_beheerder());
