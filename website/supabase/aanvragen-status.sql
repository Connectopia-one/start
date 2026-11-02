-- Aanvragen: wat er met een aanvraag gebeurde, en een archief
-- Plak dit in de SQL Editor van de Supabase van het OUDERPORTAAL en klik "Run".
-- Opnieuw draaien mag altijd; er gaat niets verloren.
--
-- Kim op 2 november 2026: "afgehandeld betekent niet dat dat bezig is. Ik heb
-- meer knoppen nodig: mail verstuurd, ingeschreven of niet ingeschreven,
-- behandeld of niet behandeld." En: ze wil aanvragen kunnen archiveren, met
-- het archief nog altijd verdeeld per soort.
--
-- "stappen" is een lijstje van wat er al gebeurde, bijvoorbeeld
-- {"mail verstuurd","ingeschreven"}. De namen staan in het ouderportaal in
-- lib/aanvraagstappen.ts; er kan er daar een bij zonder dat deze tabel
-- moet veranderen. "Behandeld" blijft de bestaande kolom afgehandeld.

alter table public.aanvragen
  add column if not exists stappen text[] not null default array[]::text[];

alter table public.aanvragen
  add column if not exists gearchiveerd boolean not null default false;

create index if not exists aanvragen_archief_idx
  on public.aanvragen (gearchiveerd, afgehandeld, created_at desc);
