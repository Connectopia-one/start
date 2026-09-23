-- ============================================================
-- ONDERWIJSDOELEN EN VAKFICHES — de documenten op /onderwijsdoelen
-- ============================================================
-- Op /onderwijsdoelen staat per niveau en per vak waarop onze oefeningen
-- steunen. Met deze tabel kan je daar het officiële document zelf bij zetten:
-- de vakfiche of de minimumdoelen als PDF, of een link.
--
-- We hosten die bewust zelf. Op de site van de Examencommissie staan honderden
-- fiches en zijn er een paar stappen nodig om er te geraken; dan weet een ouder
-- nog altijd niet wélke fiche wij gebruikt hebben. Door ze hier te zetten met
-- de datum erbij, ziet iedereen meteen waarop een hoofdstuk gebouwd is — en of
-- die versie nog de actuele is.
--
-- Je beheert ze op /beheer/doelen. De bestanden komen in dezelfde opslagmap
-- als "Handig materiaal", dus je hoeft daar niets extra voor te doen: heb je
-- materiaal.sql al gedraaid, dan is de opslag al in orde.
--
-- Voer dit één keer uit in de SQL Editor van je Supabase-project. Draai je het
-- per ongeluk een tweede keer, dan is dat niet erg: alles staat op "maak enkel
-- aan als het nog niet bestaat".

create table if not exists public.doelbestanden (
  id uuid primary key default gen_random_uuid(),
  -- Het niveau zoals op de startpagina: start, spark, boost of beyond.
  niveau text not null check (niveau in ('start', 'spark', 'boost', 'beyond')),
  -- Het vak zoals het op /onderwijsdoelen staat, bv. "Wiskunde". Laat je dit
  -- leeg, dan hoort het document bij het niveau als geheel.
  vak text,
  titel text not null,
  type text not null check (type in ('link', 'pdf')),
  link text,
  bestandspad text,
  -- Sinds wanneer deze versie geldt, bv. "1 september 2025". Gewone tekst,
  -- want op een fiche staat niet altijd een echte datum.
  geldig_sinds text,
  -- Eén zin extra, bv. welk deel van de fiche we gebruikt hebben.
  omschrijving text,
  volgnummer int not null default 1,
  created_at timestamptz not null default now()
);

create index if not exists doelbestanden_plek_idx
  on public.doelbestanden (niveau, vak, volgnummer);

alter table public.doelbestanden enable row level security;

-- Lezen mag iedereen, ook wie niet ingelogd is: /onderwijsdoelen staat open.
drop policy if exists "doelbestanden lezen" on public.doelbestanden;
create policy "doelbestanden lezen" on public.doelbestanden for select
  using (true);

drop policy if exists "beheerder doelbestanden beheer" on public.doelbestanden;
create policy "beheerder doelbestanden beheer" on public.doelbestanden for all
  using (public.is_beheerder()) with check (public.is_beheerder());

-- De opslagmap is dezelfde als die van "Handig materiaal". Staat die er nog
-- niet, dan maakt deze regel ze alsnog aan, zodat dit bestand ook op zichzelf
-- werkt als je materiaal.sql nog niet gedraaid hebt.
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
