-- ============================================================
-- EXAMENS: per vraag bewaren wat het kind antwoordde
-- ============================================================
-- Kim, 24 november 2026: "we kunnen niet zien hoeveel ze halen op het examen
-- en wat ze fout doen en hun dus niet goed kunnen begeleiden."
--
-- Tot nu bewaarde een examen enkel hoeveel vragen erin zaten en hoeveel er
-- juist waren. Vanaf nu komt er per vraag bij: welke vraag (v), juist of fout
-- (j) en wat het kind antwoordde (g). Er wordt niets gewist of veranderd aan
-- de examens die er al staan; die houden gewoon hun score.
--
-- Voer dit één keer uit in de SQL Editor van het Supabase-project van het
-- OEFENPLATFORM. Een tweede keer draaien kan geen kwaad.

alter table public.examens
  add column if not exists antwoorden jsonb;

-- Nakijken: de kolom staat er, de bestaande examens zijn er allemaal nog.
select count(*) as examens, count(antwoorden) as met_antwoorden
  from public.examens;
