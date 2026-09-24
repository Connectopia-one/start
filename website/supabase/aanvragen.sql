-- Aanvragen en inschrijvingen van de website — databaseschema
-- Plak dit volledige bestand in het Supabase dashboard onder "SQL Editor" en klik "Run".
-- Dit is dezelfde Supabase als het ouderportaal en als het prikbord.
-- Kan meerdere keren veilig uitgevoerd worden.

create extension if not exists pgcrypto;

-- ============================================================
-- DE TABEL
-- ============================================================

-- Eén rij per ingevuld formulier: een infovraag, een inschrijving, een
-- terugbelverzoek, een deelname aan de winactie of een professional die
-- zich meldt.
--
-- De antwoorden zelf staan samen in één kolom "gegevens", als een lijstje
-- van vraag en antwoord. Dat is met opzet: de vragen op het formulier
-- veranderen wel eens, en zo hoeft de tabel dan niet mee te veranderen.
--
-- Hier staan namen en leeftijden van kinderen in. Bezoekers van de website
-- mogen daarom wel iets toevoegen maar NIETS lezen; zie de rechten onderaan.
create table if not exists public.aanvragen (
  id uuid primary key default gen_random_uuid(),
  -- Waarover het gaat, zoals het in het onderwerp van de oude mail stond.
  onderwerp text not null check (char_length(onderwerp) between 2 and 200),
  -- info | inschrijven | proefles | terugbellen | winactie | professional
  soort text not null check (char_length(soort) between 2 and 40),
  gegevens jsonb not null,
  -- Heb jij dit al gezien? Het beheerscherm toont de nieuwe bovenaan.
  gezien boolean not null default false,
  -- Afgehandeld: opgebeld, ingeschreven, beantwoord.
  afgehandeld boolean not null default false,
  notitie text check (char_length(notitie) <= 2000),
  created_at timestamptz not null default now()
);

create index if not exists aanvragen_nieuw_idx
  on public.aanvragen (gezien, created_at desc);

-- ============================================================
-- RECHTEN
-- De website verstuurt met de publieke sleutel (de rol "anon"). Die mag
-- een aanvraag toevoegen en verder niets: niet lezen, niet wijzigen, niet
-- verwijderen. Lezen gebeurt alleen in het beheer van het ouderportaal,
-- dat met de service-role sleutel werkt en die regels overslaat.
-- ============================================================

alter table public.aanvragen enable row level security;

drop policy if exists "iedereen kan een aanvraag indienen" on public.aanvragen;
create policy "iedereen kan een aanvraag indienen"
  on public.aanvragen for insert
  to anon, authenticated
  with check (true);

revoke all on public.aanvragen from anon, authenticated;
grant insert (onderwerp, soort, gegevens) on public.aanvragen to anon, authenticated;
