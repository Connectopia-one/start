-- Voorleesknop per kind (november 2026). Staat standaard uit.
-- Voegt enkel een lege kolom toe; raakt niets van wat er al is.
alter table public.kinderen add column if not exists toon_voorlezen boolean not null default false;
