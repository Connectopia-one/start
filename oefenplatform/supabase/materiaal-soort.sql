-- ============================================================
-- LEUKE EXTRA'S — soort en schoolniveau bij het materiaal
-- ============================================================
-- Kim, 9 november 2026: de pagina Leuke extra's heeft nu vier grote knoppen
-- (spellen, links, documenten, filmpjes) en zet alles per schoolniveau.
-- Hiermee krijgt elk item uit Beheer > Materiaal twee kolommen bij:
--   soort         links, documenten of filmpjes
--   schoolniveau  lager, middelbaar of iedereen
--
-- Er wordt niets verwijderd. Wat er al stond, krijgt vanzelf een soort: een
-- pdf wordt een document, een link blijft een link, en alles staat eerst
-- onder "Voor iedereen". Dat kan je daarna per item aanpassen op
-- /beheer/materiaal.
--
-- Eén keer uitvoeren in de SQL Editor van het Supabase-project van het
-- oefenplatform. Een tweede keer draaien kan geen kwaad.

alter table public.materiaal add column if not exists soort text;
alter table public.materiaal add column if not exists schoolniveau text not null default 'iedereen';

update public.materiaal
  set soort = case when type = 'pdf' then 'documenten' else 'links' end
  where soort is null;

alter table public.materiaal alter column soort set default 'links';

alter table public.materiaal drop constraint if exists materiaal_soort_check;
alter table public.materiaal add constraint materiaal_soort_check
  check (soort in ('links', 'documenten', 'filmpjes'));

alter table public.materiaal drop constraint if exists materiaal_schoolniveau_check;
alter table public.materiaal add constraint materiaal_schoolniveau_check
  check (schoolniveau in ('lager', 'middelbaar', 'iedereen'));
