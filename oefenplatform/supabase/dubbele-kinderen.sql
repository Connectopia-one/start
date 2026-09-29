-- ============================================================
-- Dubbele kinderen samenvoegen  (29 september 2026)
-- ============================================================
--
-- Wat er misging: laadde de pagina "Mijn account" traag, dan klikten mensen
-- nog eens op Toevoegen. Elke klik maakte een nieuw kind aan, en verwijderen
-- kon niet. Sommige gezinnen hebben daardoor hetzelfde kind vier of vijf keer
-- staan.
--
-- Wat dit bestand doet: per gezin blijft van elke naam het OUDSTE kind over.
-- Alles wat aan de dubbels hing — opgeloste vragen, sterren, en de notities en
-- documenten van een plusklasfiche — wordt eerst naar dat ene kind verhuisd.
-- Er gaat dus geen enkel antwoord verloren; de voortgang van de dubbels komt
-- gewoon samen op één naam.
--
-- Hoofdletters en spaties tellen niet mee: "Nele", "nele " en "NELE" zijn
-- hetzelfde kind.
--
-- Je mag dit bestand gerust een tweede keer draaien. Staan er geen dubbels
-- meer, dan doet het niets.
--
-- Draaien: SQL editor van het OEFENPLATFORM, plakken, Run.

do $$
declare
  aantal int;
begin

  create temporary table blijft_over on commit drop as
  select
    id as blijver,
    profile_id,
    lower(btrim(naam)) as sleutel
  from (
    select
      id, profile_id, naam,
      row_number() over (
        partition by profile_id, lower(btrim(naam))
        order by created_at, id
      ) as rij
    from public.kinderen
  ) k
  where rij = 1;

  create temporary table gaat_weg on commit drop as
  select d.id as dubbel, b.blijver
  from public.kinderen d
  join blijft_over b
    on b.profile_id = d.profile_id
   and b.sleutel = lower(btrim(d.naam))
  where d.id <> b.blijver;

  select count(*) into aantal from gaat_weg;
  raise notice 'Dubbele kinderen gevonden: %', aantal;

  -- Opgeloste vragen verhuizen. Hier mag alles mee: dezelfde vraag twee keer
  -- beantwoord is geen probleem, dat is net de geschiedenis die we bewaren.
  update public.voortgang v
     set kind_id = g.blijver
    from gaat_weg g
   where v.kind_id = g.dubbel;

  -- Sterren verhuizen, maar één ster per hoofdstuk. Heeft de blijver die ster
  -- al, dan valt de dubbele ster weg bij het verwijderen hieronder.
  update public.stickers s
     set kind_id = g.blijver
    from gaat_weg g
   where s.kind_id = g.dubbel
     and not exists (
       select 1 from public.stickers a
        where a.kind_id = g.blijver
          and a.hoofdstuk_id = s.hoofdstuk_id
     );

  -- De plusklasfiche, als die tabellen bestaan.
  if to_regclass('public.kind_notities') is not null then
    update public.kind_notities n
       set kind_id = g.blijver
      from gaat_weg g
     where n.kind_id = g.dubbel;
  end if;

  if to_regclass('public.kind_documenten') is not null then
    update public.kind_documenten d
       set kind_id = g.blijver
      from gaat_weg g
     where d.kind_id = g.dubbel;
  end if;

  delete from public.kinderen k
   using gaat_weg g
   where k.id = g.dubbel;

  raise notice 'Dubbele kinderen verwijderd: %', aantal;

end $$;
