-- ============================================================
-- HET WEETJESPRIKBORD
-- ============================================================
-- Eén keer draaien in de SQL-editor van het oefenplatform-project.
--
-- Waarvoor: kinderen sturen zelf een weetje in ("wist je dat een octopus drie
-- harten heeft?"). Jij leest het na en hangt het op. Pas dan staat het op het
-- prikbord, met de voornaam van het kind eronder.
--
-- Niets verschijnt vanzelf. Een ingestuurd weetje staat op goedgekeurd =
-- false, en die kolom kan alleen jij veranderen: de regels hieronder laten
-- een gewone bezoeker wel toevoegen, maar nooit bijwerken of wissen, en hij
-- ziet alleen wat jij opgehangen hebt.
--
-- Wat er van een kind bewaard wordt, is bewust weinig: een voornaam en, als
-- ze dat invullen, een leeftijd. Geen achternaam, geen klas, geen contact.
-- Het account waarmee ingestuurd werd staat er wel bij, zodat jij weet bij
-- wie je moet zijn als er iets mis is — dat staat nooit op het prikbord zelf.

create table if not exists public.weetjes (
  id uuid primary key default gen_random_uuid(),
  tekst text not null check (char_length(tekst) between 3 and 500),
  voornaam text check (voornaam is null or char_length(voornaam) between 1 and 40),
  leeftijd int check (leeftijd is null or leeftijd between 3 and 21),
  profile_id uuid references public.profiles(id) on delete set null,
  goedgekeurd boolean not null default false,
  aangemaakt_op timestamptz not null default now(),
  opgehangen_op timestamptz
);

create index if not exists weetjes_prikbord_idx
  on public.weetjes (goedgekeurd, opgehangen_op desc);

alter table public.weetjes enable row level security;

-- Iedereen ziet wat opgehangen is; jij ziet ook wat nog wacht.
drop policy if exists "opgehangen weetjes lezen" on public.weetjes;
create policy "opgehangen weetjes lezen" on public.weetjes
  for select using (goedgekeurd = true or public.is_beheerder());

-- Insturen kan met een account. Het weetje begint altijd ongoedgekeurd, en
-- niemand kan het op naam van een ander account zetten.
drop policy if exists "ingelogd weetje insturen" on public.weetjes;
create policy "ingelogd weetje insturen" on public.weetjes
  for insert to authenticated with check (
    goedgekeurd = false
    and opgehangen_op is null
    and (profile_id is null or profile_id = auth.uid())
  );

drop policy if exists "beheerder hangt weetjes op" on public.weetjes;
create policy "beheerder hangt weetjes op" on public.weetjes
  for update using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "beheerder wist weetjes" on public.weetjes;
create policy "beheerder wist weetjes" on public.weetjes
  for delete using (public.is_beheerder());
