-- ============================================================
-- EEN BEDANKJE VOOR EEN MELDING BLIJFT WEG NA WEGKLIKKEN
-- ============================================================
-- Eén keer draaien in de SQL-editor van het oefenplatform-project, ná
-- melding-antwoord.sql.
--
-- Waarvoor: Kim op 10 november 2026: "deze meldingen blijven precies voor
-- eeuwig staan, als ik ze weg klik blijven ze terug komen [...] na 1 keer te
-- lezen en weg te klikken moeten deze weg gaan."
--
-- Wegklikken werd enkel in de browser onthouden. Op een andere computer, gsm
-- of na het wissen van de browsergegevens kwam het bedankje dus terug. Vanaf
-- nu zet het kruisje het moment van wegklikken bij de melding zelf, en wat
-- weggeklikt is, komt nergens meer terug.
--
-- Eén kolom erbij. Er komt geen nieuwe schrijfregel: het wegklikken gebeurt
-- op de server (app/melding-actions.ts), die eerst nagaat dat de melding van
-- de ingelogde persoon zelf is.

alter table public.meldingen
  add column if not exists gezien_op timestamptz;
