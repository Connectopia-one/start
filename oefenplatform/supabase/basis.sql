-- ============================================================
-- 🧱 BASIS — een vijfde categorie voor herhaling van de bouwstenen
-- ============================================================
-- Naast Start, Spark, Boost en Beyond is er nu ook "Basis": herhaling van wat
-- een kind al gezien heeft maar nog niet vlot kan (de komma verschuiven, maten
-- omzetten, breuken, de namen van de bewerkingen, ggd en kgv).
--
-- De databank laat per hoofdstuk alleen de gekende categorieën toe. Voer dit
-- één keer uit in de SQL Editor van je Supabase-project, vóór je de
-- basishoofdstukken importeert. Een tweede keer draaien is niet erg.

-- 'hoekje' hoort hier ook in, ook al gaat dit bestand daar niet over. Zowel dit
-- bestand als uitdagingshoek.sql zet deze regel opnieuw, en wie ze in de andere
-- volgorde draait zou anders 'hoekje' weer wegnemen. Bij een oefenplatform waar
-- de uitdagingshoek al gevuld is, zou dat bovendien niet eens lukken: er staan
-- dan rijen die de nieuwe regel overtreden. Houd de twee lijsten dus gelijk.
alter table public.hoofdstukken drop constraint if exists hoofdstukken_niveau_check;
alter table public.hoofdstukken add constraint hoofdstukken_niveau_check
  check (niveau in ('basis', 'start', 'spark', 'boost-doorstroom',
                    'boost-dubbele-finaliteit', 'beyond', 'hoekje'));
