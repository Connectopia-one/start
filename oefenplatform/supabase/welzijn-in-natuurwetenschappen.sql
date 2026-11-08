-- De 14 hoofdstukken welzijnswetenschappen verhuizen naar het gewone vak
-- natuurwetenschappen (🌍 Beyond doorstroom).
--
-- Kim op 8 november 2026: "zo staat er 1 vak natuurwetenschappen dat je kan
-- aanpassen als het nodig is, en geen 2 aparte vakken." De vakfiche
-- welzijnswetenschappen bevat alles van de gewone fiche plus een blok over het
-- menselijk lichaam, dus het is één examen. De hoofdstukken krijgen in het vak
-- een blauwe kleur en het label "Enkel welzijnswetenschappen"; dat herkent de
-- site aan de titel "Welzijnswetenschappen: ..." (lib/welzijn.ts).
--
-- Wat er gebeurt:
--   1. een kopie van de huidige toestand in backup_welzijn_hoofdstukken;
--   2. de hoofdstukken krijgen het vak natuurwetenschappen en een volgnummer
--      achter de bestaande hoofdstukken van dat vak (het volgnummer moet per
--      vak uniek zijn, het staat in het webadres).
-- De hoofdstukken zelf, hun vragen, leerbundels en de voortgang van de
-- kinderen blijven: enkel vak_id en volgnummer veranderen. Niets wordt gewist.
-- Het oude vak blijft bestaan, maar zonder hoofdstukken verschijnt het niet
-- meer op de site.
--
-- Terugdraaien:
--   update public.hoofdstukken h
--      set vak_id = b.vak_id, volgnummer = b.volgnummer
--     from public.backup_welzijn_hoofdstukken b
--    where h.id = b.id;

create table if not exists public.backup_welzijn_hoofdstukken as
  select h.id, h.vak_id, h.volgnummer, h.titel, now() as bewaard_op
    from public.hoofdstukken h
    join public.vakken v on v.id = h.vak_id
   where v.slug = 'natuurwetenschappen-welzijnswetenschappen';

with doel as (
  select id from public.vakken where slug = 'natuurwetenschappen'
),
start as (
  select coalesce(max(h.volgnummer), 0) as hoogste
    from public.hoofdstukken h, doel
   where h.vak_id = doel.id
),
te_verhuizen as (
  select h.id,
         row_number() over (order by h.volgnummer) as rang
    from public.hoofdstukken h
    join public.vakken v on v.id = h.vak_id
   where v.slug = 'natuurwetenschappen-welzijnswetenschappen'
)
update public.hoofdstukken h
   set vak_id = doel.id,
       volgnummer = start.hoogste + t.rang
  from te_verhuizen t, doel, start
 where h.id = t.id;

-- Controle: hier moeten 14 rijen staan, allemaal in natuurwetenschappen.
select h.volgnummer, h.titel, v.slug as vak
  from public.hoofdstukken h
  join public.vakken v on v.id = h.vak_id
 where h.titel ilike 'Welzijnswetenschappen:%'
 order by h.volgnummer;
