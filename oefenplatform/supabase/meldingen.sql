-- ============================================================
-- MELDINGEN BIJ EEN HOOFDSTUK
-- ============================================================
-- Eén keer draaien in de SQL-editor van het oefenplatform-project.
--
-- Waarvoor: een ouder of een kind dat in een hoofdstuk iets ziet dat niet
-- klopt, kan dat ter plekke melden. De melding hangt aan het hoofdstuk en,
-- als ze die aanduiden, aan de vraag zelf. In Beheer staan ze allemaal op één
-- pagina, zodat je meteen weet waar je moet ingrijpen.
--
-- Wie mag wat: iedereen die een hoofdstuk kan zien, mag een melding
-- achterlaten, ook zonder account (de gratis hoofdstukken staan immers open).
-- Lezen, afvinken en wissen kan alleen jij als beheerder. Zo kan niemand de
-- meldingen van anderen opvragen.

create table if not exists public.meldingen (
  id uuid primary key default gen_random_uuid(),
  hoofdstuk_id uuid not null references public.hoofdstukken(id) on delete cascade,
  vraag_id uuid references public.vragen(id) on delete set null,
  profile_id uuid references public.profiles(id) on delete set null,
  soort text not null default 'fout'
    check (soort in ('fout', 'onduidelijk', 'te-moeilijk', 'te-makkelijk', 'andere')),
  bericht text not null check (char_length(bericht) between 1 and 2000),
  afgehandeld boolean not null default false,
  aangemaakt_op timestamptz not null default now()
);

create index if not exists meldingen_hoofdstuk_idx on public.meldingen (hoofdstuk_id);
create index if not exists meldingen_open_idx on public.meldingen (afgehandeld, aangemaakt_op desc);

alter table public.meldingen enable row level security;

drop policy if exists "iedereen mag melden" on public.meldingen;
create policy "iedereen mag melden" on public.meldingen
  for insert with check (
    -- Een melding hangt altijd aan een bestaand hoofdstuk, en nooit aan het
    -- account van iemand anders.
    exists (select 1 from public.hoofdstukken h where h.id = hoofdstuk_id)
    and (profile_id is null or profile_id = auth.uid())
    and afgehandeld = false
  );

drop policy if exists "beheerder leest meldingen" on public.meldingen;
create policy "beheerder leest meldingen" on public.meldingen
  for select using (public.is_beheerder());

drop policy if exists "beheerder werkt meldingen bij" on public.meldingen;
create policy "beheerder werkt meldingen bij" on public.meldingen
  for update using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "beheerder wist meldingen" on public.meldingen;
create policy "beheerder wist meldingen" on public.meldingen
  for delete using (public.is_beheerder());
