-- Voortgangsbalk aan of uit, per kind.
--
-- Een ouder met twee kinderen meldde op 29 september 2026 dat hetzelfde
-- scherm bij het ene kind rust geeft en bij het andere frustratie. Het ene
-- kind was blij dat er géén balk bij de vragen staat en blokkeerde zodra het
-- zag hoeveel vragen er waren; het andere wou net weten hoe ver het al was,
-- omdat voorspelbaarheid helpt.
--
-- Daarom hangt de keuze niet aan het platform maar aan het kind. De ouder zet
-- ze op /account, bij Mijn kinderen.
--
-- De standaard is "uit": dat is hoe het platform er vandaag uitziet, dus voor
-- wie niets aanraakt verandert er niets.
--
-- Dit bestand mag je zo vaak draaien als je wil.

alter table public.kinderen
  add column if not exists toon_voortgang boolean not null default false;

comment on column public.kinderen.toon_voortgang is
  'Toont een voortgangsbalk bij de oefeningen van dit kind. Standaard uit.';
