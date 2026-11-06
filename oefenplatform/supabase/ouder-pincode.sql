-- Pincode voor ouders (november 2026, idee Kim na de enquêtes).
-- Een ouder van een kind dat zelfstandig oefent, kan Mijn account, de
-- voortgang en de lijst met foute vragen afschermen met een pincode.
-- Aparte tabel zonder leesregels: enkel de server (service role) leest ze.
-- Voegt enkel een nieuwe, lege tabel toe; raakt niets van wat er al is.
create table if not exists public.ouder_pincodes (
  profile_id uuid primary key references public.profiles(id) on delete cascade,
  pin_hash text not null,
  gewijzigd_op timestamptz not null default now()
);
alter table public.ouder_pincodes enable row level security;
