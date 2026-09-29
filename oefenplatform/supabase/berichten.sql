-- ============================================================
-- EEN BERICHT VAN JOU AAN ALLE OUDERS
-- ============================================================
-- Eén keer draaien in de SQL-editor van het oefenplatform-project.
--
-- Waarvoor: jij schrijft in Beheer → Berichten één bericht ("er is een nieuw
-- onderdeel bij"), en elke ouder ziet dat bovenaan als ze het platform
-- openen. Net zoals jouw antwoord op een ingestuurd weetje bij het kind zelf
-- uitkomt.
--
-- Er vertrekt geen mail. Het bericht staat in het platform, niet in iemands
-- postvak. Een ouder kan het wegklikken; dat wordt in zijn eigen browser
-- onthouden, niet hier. Zet je het bericht op "uit", dan is het meteen bij
-- iedereen weg.

create table if not exists public.berichten (
  id uuid primary key default gen_random_uuid(),
  titel text not null check (char_length(titel) between 2 and 120),
  tekst text not null check (char_length(tekst) between 2 and 2000),
  -- de knop "Naar het nieuwe onderdeel", optioneel
  link text check (link is null or char_length(link) between 1 and 300),
  linktekst text check (linktekst is null or char_length(linktekst) between 1 and 60),
  actief boolean not null default true,
  aangemaakt_op timestamptz not null default now()
);

create index if not exists berichten_actief_idx
  on public.berichten (actief, aangemaakt_op desc);

alter table public.berichten enable row level security;

-- Iedereen die ingelogd is, leest de berichten die aan staan. Wie uitgelogd
-- is, ziet niets: dit gaat over onze eigen gezinnen, niet over bezoekers.
drop policy if exists "ouders lezen actieve berichten" on public.berichten;
create policy "ouders lezen actieve berichten" on public.berichten
  for select to authenticated using (actief = true or public.is_beheerder());

-- Schrijven kan alleen jij.
drop policy if exists "beheerder schrijft berichten" on public.berichten;
create policy "beheerder schrijft berichten" on public.berichten
  for all using (public.is_beheerder()) with check (public.is_beheerder());
