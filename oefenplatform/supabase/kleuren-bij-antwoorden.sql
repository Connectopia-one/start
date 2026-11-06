-- Zachte kleuren bij de antwoorden, aan of uit per kind.
--
-- Febe en Margot vroegen in de enquête van november 2026 om groen bij een
-- juist antwoord. Andere kinderen hebben net rust bij een scherm zonder kleur.
-- Daarom, net als de voortgangsbalk (voortgangsbalk.sql), een keuze van de
-- ouder op /account, bij Mijn kinderen. Standaard uit: wie niets aanraakt,
-- ziet het platform zoals vandaag.
--
-- Dit bestand mag je zo vaak draaien als je wil.

alter table public.kinderen
  add column if not exists toon_kleuren boolean not null default false;

comment on column public.kinderen.toon_kleuren is
  'Kleurt na het nakijken het juiste antwoord lichtgroen en een fout gekozen antwoord lichtoranje. Standaard uit.';
