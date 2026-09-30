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
-- Dit bestand doet drie dingen, in deze volgorde:
--   1. de oude controle weghalen;
--   2. hoofdstukken die nu nog op 'boost' staan verhuizen naar
--      'boost-doorstroom' (de voorbeeldhoofdstukken uit schema.sql stonden
--      daar; als je die al weggehaald hebt, verhuist er gewoon niets);
--   3. de nieuwe controle zetten, die de twee nieuwe categorieën toelaat en
--      'boost' niet meer.
--
-- Die volgorde is belangrijk. Verhuizen vóór het weghalen lukt niet: de oude
-- controle kent 'boost-doorstroom' nog niet en weigert dan elke rij.
--
-- Voer het één keer uit in de SQL Editor van je Supabase-project van het
-- oefenplatform. Een tweede keer draaien is ongevaarlijk.

-- 1. De oude controle weg.
alter table public.hoofdstukken drop constraint if exists hoofdstukken_niveau_check;

-- 2. Nu pas verhuizen.
update public.hoofdstukken set niveau = 'boost-doorstroom' where niveau = 'boost';

-- 3. De nieuwe controle. Deze lijst moet gelijk blijven met die in
--    schema.sql, basis.sql en uitdagingshoek.sql.
alter table public.hoofdstukken add constraint hoofdstukken_niveau_check
  check (niveau in ('basis', 'start', 'spark', 'boost-doorstroom',
                    'boost-dubbele-finaliteit', 'beyond', 'hoekje'));

-- Blijft stap 3 haken, dan staat er nog een hoofdstuk met een categorie die
-- niet in de lijst staat. Deze regel toont welke:
--   select distinct niveau from public.hoofdstukken;

-- De onderwijsdoelen op /onderwijsdoelen blijven wél per knop van de
-- startpagina staan ('start', 'spark', 'boost', 'beyond'): bij Boost horen de
-- doelen van allebei de finaliteiten onder hetzelfde kopje. Aan
-- doelbestanden.sql verandert er dus niets.
