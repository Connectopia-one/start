-- ============================================================
-- EEN ANTWOORD OP EEN MELDING
-- ============================================================
-- Eén keer draaien in de SQL-editor van het oefenplatform-project, ná
-- meldingen.sql.
--
-- Waarvoor: wie op de meldknop duwt, hoorde daarna niets meer. Kim op
-- 29 september 2026: "kan er als ik klik op afgehandeld bekomen dat er bij de
-- persoon die de melding gemaakt word ook een melding komt dat we dit bekeken
-- en behandeld hebben?"
--
-- Vanaf nu zet "Afgehandeld" ook het moment erbij, en mag je er een woordje
-- bij schrijven. Die persoon ziet dat de volgende keer bovenaan het
-- oefenplatform, bij zijn eigen melding. Er vertrekt geen mail.
--
-- Twee kolommen erbij, en één leesregel: wie ingelogd was toen hij meldde,
-- mag zijn éigen meldingen lezen. Wat anderen meldden blijft onzichtbaar.
-- Wie zonder account meldde, heeft geen account om iets aan te tonen; die
-- ziet dus niets, en dat staat ook zo in Beheer bij die melding.

alter table public.meldingen
  add column if not exists afgehandeld_op timestamptz;

alter table public.meldingen
  add column if not exists antwoord text
    check (antwoord is null or char_length(antwoord) <= 500);

create index if not exists meldingen_eigen_idx
  on public.meldingen (profile_id, afgehandeld_op desc);

-- Naast de regel voor de beheerder. Twee leesregels naast elkaar betekent:
-- wie aan één ervan voldoet, mag lezen.
drop policy if exists "melder leest zijn eigen meldingen" on public.meldingen;
create policy "melder leest zijn eigen meldingen" on public.meldingen
  for select using (profile_id = auth.uid());
