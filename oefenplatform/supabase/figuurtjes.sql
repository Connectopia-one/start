-- Figuurtjes (Kim, november 2026, na de enquête van Dalian: "punten verdienen
-- waar je iets mee kan doen"). Per kind, standaard uit.
-- Elk helemaal afgewerkt hoofdstuk geeft één sterretje; met de sterretjes kiest
-- een kind figuurtjes. De sterretjes zelf worden niet bewaard: ze volgen uit
-- de voortgang. Enkel welke figuurtjes het kind al koos, staat hier.
-- Voegt enkel lege kolommen toe; raakt niets van wat er al is.
alter table public.kinderen add column if not exists toon_figuurtjes boolean not null default false;
alter table public.kinderen add column if not exists figuurtjes text[] not null default '{}';
alter table public.kinderen add column if not exists figuurtje text;
