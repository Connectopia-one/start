-- Twee nieuwe vraagvormen, zoals op het examen van de Examencommissie:
--   tabel       per rij een uitspraak, en per rij duid je juist of fout aan
--   keuzelijst  een zin met een keuzelijst op de plaats van een woord
-- Zie lib/vraagvorm.ts voor hoe ze bewaard worden.
--
-- Aan de kolommen verandert niets. Alleen de regel die zegt welke types een
-- vraag mag hebben, krijgt er twee bij. Zolang dit niet gedraaid is, weigert
-- de databank een tabel of een keuzelijst bij het importeren.
--
-- Een tweede keer draaien maakt niets kapot.

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
  check (type in ('meerkeuze', 'invultekst', 'waarofniet', 'tabel', 'keuzelijst'));
