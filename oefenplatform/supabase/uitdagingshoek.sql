-- ============================================================
-- 🔭 UITDAGINGSHOEK — een hoekje dat verder gaat dan de leerstof
-- ============================================================
-- Naast Basis, Start, Spark, Boost en Beyond komt er een zesde categorie:
-- "hoekje". Geen leerjaar en geen examenstof, maar vragen die er net naast
-- liggen — de ruimte, hoe een computer denkt, de geschiedenis van ons land,
-- en paradoxen die je hoofd kraken. Bedoeld voor kinderen die klaar zijn met
-- de gewone hoofdstukken en gewoon verder willen denken.
--
-- Dit bestand doet twee dingen:
--   1. de databank de nieuwe categorie laten toe;
--   2. de vier vakken van het hoekje aanmaken, zodat je ze niet met de hand
--      hoeft te typen.
--
-- Voer het één keer uit in de SQL Editor van je Supabase-project van het
-- oefenplatform, vóór je de vragenbestanden importeert. Een tweede keer
-- draaien is niet erg: er komt niets dubbel bij.

alter table public.hoofdstukken drop constraint if exists hoofdstukken_niveau_check;
alter table public.hoofdstukken add constraint hoofdstukken_niveau_check
  check (niveau in ('basis', 'start', 'spark', 'boost', 'beyond', 'hoekje'));

-- De vier vakken van het hoekje. Ze staan achteraan in de lijst (volgorde 90+),
-- zodat ze de gewone vakken niet voor de voeten lopen. Alleen bij "De ruimte"
-- staat de rekenmachine aan; daar komen af en toe grote getallen bij kijken.
insert into public.vakken (naam, slug, volgorde, rekenmachine)
values
  ('De ruimte',              'de-ruimte',              90, true),
  ('Coderen en computers',   'coderen-en-computers',   91, false),
  ('Geschiedenis van België','geschiedenis-van-belgie',92, false),
  ('Paradoxen en weetjes',   'paradoxen-en-weetjes',   93, false)
on conflict (slug) do nothing;
