-- De overige vraagvormen van het examen van de Examencommissie:
--   volgorde   de stappen in de juiste volgorde zetten
--   koppelen   elk onderdeel links aan het juiste antwoord rechts koppelen
--   sorteren   kaartjes naar de juiste kolom slepen
--   sleepzin   woorden naar de lege vakken in een zin slepen
--   hotspot    op de juiste plaats in een prent klikken
--   open       een open antwoord, dat het kind zelf nakijkt met een voorbeeld
--   tekenen    tekenen op het scherm, ook zelf nagekeken
-- en een casus: een situatie die boven de vraag staat.
-- Zie lib/examenvormen.ts voor hoe ze bewaard worden.
--
-- Wat er verandert: de regel die zegt welke types een vraag mag hebben, krijgt
-- er zeven bij, en de tabel vragen krijgt een kolom casus. Aan de vragen die er
-- al staan verandert niets. Een tweede keer draaien maakt niets kapot.

do $$
declare
  regel text;
begin
  -- De oude regel weghalen, onder welke naam ze ook staat.
  for regel in
    select conname from pg_constraint
    where conrelid = 'public.vragen'::regclass
      and contype = 'c'
      and pg_get_constraintdef(oid) like '%type%meerkeuze%'
  loop
    execute format('alter table public.vragen drop constraint %I', regel);
  end loop;
end $$;

alter table public.vragen
  add constraint vragen_type_check
  check (type in (
    'meerkeuze', 'invultekst', 'waarofniet', 'tabel', 'keuzelijst',
    'volgorde', 'koppelen', 'sorteren', 'sleepzin', 'hotspot', 'open', 'tekenen'
  ));

alter table public.vragen add column if not exists casus text;
