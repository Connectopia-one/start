-- ============================================================
-- 🌍 BEYOND SPLITST IN TWEE: doorstroom en dubbele finaliteit
-- ============================================================
-- Net als bij Boost is Beyond geen één categorie meer. De examencommissie zet
-- de derde graad in vier lijsten, maar die vallen bij ons in twee categorieën
-- uiteen. De doorstroomfiches noemen bovenaan zelf zowel de
-- domeinoverschrijdende richtingen (economie-wiskunde, humane wetenschappen,
-- Latijn, moderne talen, wetenschappen-wiskunde) als de domeingebonden
-- (bedrijfswetenschappen, welzijnswetenschappen), dus die horen samen. De
-- basisvorming van de dubbele finaliteit en commerciële organisatie vormen de
-- tweede categorie.
--
-- Op de startpagina blijft Beyond wél één knop. De keuze tussen de twee komt
-- een stap later, op /niveaus/beyond.
--
-- Dit bestand doet drie dingen, in deze volgorde:
--   1. de oude controle weghalen;
--   2. alle hoofdstukken die nu op 'beyond' staan verhuizen naar
--      'beyond-doorstroom' (geschiedenis, Nederlands en wiskunde gevorderd
--      komen alle drie van een doorstroomfiche);
--   3. de nieuwe controle zetten, die de twee nieuwe categorieën toelaat en
--      'beyond' niet meer.
--
-- Die volgorde is belangrijk. Verhuizen vóór het weghalen lukt niet: de oude
-- controle kent 'beyond-doorstroom' nog niet en weigert dan elke rij.
--
-- Je hoeft niets opnieuw te importeren. Stap 2 verhuist de hoofdstukken die er
-- al staan, mét de voortgang van de kinderen eraan. Zou je de vragenbestanden
-- opnieuw inladen, dan komt alles er een tweede keer bij te staan, want de
-- import zoekt een hoofdstuk op categorie én titel.
--
-- Voer het één keer uit in de SQL Editor van je Supabase-project van het
-- oefenplatform, en pas nadat de nieuwe versie van de site online staat. Een
-- tweede keer draaien is ongevaarlijk.

-- 1. De oude controle weg.
alter table public.hoofdstukken drop constraint if exists hoofdstukken_niveau_check;

-- 2. Nu pas verhuizen.
update public.hoofdstukken set niveau = 'beyond-doorstroom' where niveau = 'beyond';

-- 3. De nieuwe controle. Deze lijst moet gelijk blijven met die in
--    schema.sql, basis.sql, uitdagingshoek.sql en boost-finaliteit.sql.
alter table public.hoofdstukken add constraint hoofdstukken_niveau_check
  check (niveau in ('basis', 'start', 'spark', 'boost-doorstroom',
                    'boost-dubbele-finaliteit', 'beyond-doorstroom',
                    'beyond-dubbele-finaliteit', 'hoekje'));

-- Blijft stap 3 haken, dan staat er nog een hoofdstuk met een categorie die
-- niet in de lijst staat. Deze regel toont welke:
--   select distinct niveau from public.hoofdstukken;

-- De onderwijsdoelen op /onderwijsdoelen blijven wél per knop van de
-- startpagina staan ('start', 'spark', 'boost', 'beyond'): bij Beyond horen de
-- doelen van allebei de finaliteiten onder hetzelfde kopje. Aan
-- doelbestanden.sql verandert er dus niets.
