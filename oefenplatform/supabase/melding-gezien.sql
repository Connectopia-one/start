-- ============================================================
-- BEDANKJE BIJ EEN MELDING: WEGKLIKKEN ONTHOUDEN
-- ============================================================
-- Eén keer draaien in de SQL-editor van het oefenplatform-project, ná
-- melding-antwoord.sql.
--
-- Kim, 17 november 2026: "de meldingen van een maand geleden blijven terug
-- komen." Het kruisje bij "Bedankt voor je melding" werd enkel in de browser
-- onthouden. Vanaf nu zet het ook het moment in de databank, zodat het
-- bedankje op geen enkel toestel meer terugkomt.
--
-- Eén kolom erbij, er wordt niets gewist of veranderd aan wat er al staat.
-- Het invullen gebeurt langs de server (app/melding-actions.ts), na de
-- controle dat het om je eigen melding gaat; daarvoor is geen nieuwe regel
-- nodig.

alter table public.meldingen
  add column if not exists gezien_op timestamptz;
