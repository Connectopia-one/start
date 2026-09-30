-- ============================================================
-- 🚀 BOOST SPLITST IN TWEE: doorstroom en dubbele finaliteit
-- ============================================================
-- Vanaf de tweede graad is Boost geen één categorie meer. De examencommissie
-- splitst daar in doorstroomfinaliteit en dubbele finaliteit, met eigen
-- vakfiches: doorstroom heeft Nederlands 1 en Nederlands 2 en kiest tussen
-- wiskunde gevorderd en wiskunde basis, dubbele finaliteit heeft gewoon
-- Nederlands en gewoon wiskunde. Dat is andere leerstof, dus twee categorieën.
--
-- Op de startpagina blijft Boost wél één knop. De keuze tussen de twee komt
-- een stap later, op /niveaus/boost.
--
-- Dit bestand doet twee dingen:
--   1. hoofdstukken die nu nog op 'boost' staan verhuizen naar
--      'boost-doorstroom' (de vier voorbeeldhoofdstukken uit schema.sql
--      stonden daar; als je die al weggehaald hebt, verhuist er gewoon niets);
--   2. de databank de twee nieuwe categorieën laten toe, en 'boost' niet meer.
--
-- Voer het één keer uit in de SQL Editor van je Supabase-project van het
-- oefenplatform. Een tweede keer draaien is ongevaarlijk.

-- 1. Eerst verhuizen, anders zou de nieuwe controle hieronder afketsen op een
--    hoofdstuk dat nog 'boost' draagt. Zo mislukt dit bestand liever luid dan
--    dat een hoofdstuk stil onvindbaar wordt.
update public.hoofdstukken set niveau = 'boost-doorstroom' where niveau = 'boost';

-- 2. De toegelaten categorieën. Deze lijst moet gelijk blijven met die in
--    schema.sql, basis.sql en uitdagingshoek.sql.
alter table public.hoofdstukken drop constraint if exists hoofdstukken_niveau_check;
alter table public.hoofdstukken add constraint hoofdstukken_niveau_check
  check (niveau in ('basis', 'start', 'spark', 'boost-doorstroom',
                    'boost-dubbele-finaliteit', 'beyond', 'hoekje'));

-- De onderwijsdoelen op /onderwijsdoelen blijven wél per knop van de
-- startpagina staan ('start', 'spark', 'boost', 'beyond'): bij Boost horen de
-- doelen van allebei de finaliteiten onder hetzelfde kopje. Aan
-- doelbestanden.sql verandert er dus niets.
