-- ============================================================
-- EEN ANTWOORD OP EEN INGESTUURD WEETJE
-- ============================================================
-- Eén keer draaien in de SQL-editor van het oefenplatform-project, ná
-- weetjes.sql.
--
-- Waarvoor: een kind dat iets instuurt dat niet klopt of niet past, bleef tot
-- nu in het ongewisse zitten wachten of het ooit zou verschijnen. Vanaf nu kan
-- je een briefje "niet plaatsen" met een boodschapje erbij, en dat boodschapje
-- ziet dat kind terug op het prikbord, bij zijn eigen inzending.
--
-- Twee kolommen erbij, en de leesregel wordt verruimd zodat iemand zijn éigen
-- inzendingen kan zien, ook als ze nog niet opgehangen zijn. Wat anderen
-- instuurden blijft onzichtbaar tot het op het bord hangt.
--
-- En er komt één regel bij die een kind toelaat zijn eigen briefje te
-- verbeteren en opnieuw in te sturen. Die regel kan nooit een briefje op het
-- bord zetten: "goedgekeurd" moet zowel voor als na de wijziging false zijn,
-- dus ophangen blijft iets wat alleen jij doet.

alter table public.weetjes
  add column if not exists niet_geplaatst boolean not null default false;

alter table public.weetjes
  add column if not exists bericht text
    check (bericht is null or char_length(bericht) <= 500);

create index if not exists weetjes_eigen_idx on public.weetjes (profile_id, aangemaakt_op desc);

drop policy if exists "opgehangen weetjes lezen" on public.weetjes;
create policy "opgehangen weetjes lezen" on public.weetjes
  for select using (
    goedgekeurd = true
    or profile_id = auth.uid()
    or public.is_beheerder()
  );

-- Een kind mag zijn eigen briefje verbeteren zolang het niet opgehangen is.
-- Let op de tweede voorwaarde in "with check": zonder die regel zou iemand
-- zijn eigen weetje kunnen goedkeuren.
drop policy if exists "eigen weetje verbeteren" on public.weetjes;
create policy "eigen weetje verbeteren" on public.weetjes
  for update to authenticated
  using (profile_id = auth.uid() and goedgekeurd = false)
  with check (profile_id = auth.uid() and goedgekeurd = false);
