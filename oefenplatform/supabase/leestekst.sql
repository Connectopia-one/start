-- ============================================================
-- LEESTEKST — een tekst bovenaan een hoofdstuk, met woordenlijst
-- ============================================================
-- Voor begrijpend lezen: het kind leest eerst een tekst en beantwoordt daarna
-- vragen die alleen over die tekst gaan. De tekst blijft boven de vragen staan
-- zolang het kind ze nodig heeft.
--
-- Twee nieuwe kolommen op een hoofdstuk:
--   leestekst    de tekst zelf. Lege regel = nieuwe alinea. Een woord tussen
--                sterretjes (*echolocatie*) krijgt een stippellijntje en de
--                uitleg uit de woordenlijst.
--   woordenlijst de verklarende woordenlijst, als een lijstje
--                [{"woord": "...", "uitleg": "..."}]. Mag leeg blijven.
--
-- Een hoofdstuk zonder leestekst verandert niet: dan is er niets te zien.
--
-- Voer dit één keer uit in de SQL Editor van je Supabase-project, vóór je de
-- hoofdstukken met een leestekst importeert. Een tweede keer draaien kan geen
-- kwaad.

alter table public.hoofdstukken add column if not exists leestekst text;
alter table public.hoofdstukken add column if not exists woordenlijst jsonb;
