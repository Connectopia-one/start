-- ============================================================
-- DE BESTAANDE GEZINNEN IN HUN GROEP ZETTEN
-- ============================================================
-- Kim op 7 oktober 2026: "Thian, Mauro, Dezly en Conny en Lucas komen via
-- iktest, plusklas is kids, ellena en mats, de rest komt via code
-- toptester2026."
--
-- De gezinnen die zich inschreven voor het platform onthield met welke code
-- dat gebeurde, staan onder "Nog geen groep". Dit bestand zet ze alsnog in de
-- juiste groep, op hun mailadres.
--
-- DRAAI EERST `groepen.sql`. Zonder dat bestand bestaat de kolom niet en stopt
-- dit script met een duidelijke melding.
--
-- Voer dit één keer uit in de SQL Editor van het Supabase-project van het
-- OEFENPLATFORM. Een tweede keer draaien kan geen kwaad: het zet gewoon
-- dezelfde waarden opnieuw.
--
-- Onderaan krijg je een lijstje te zien met per mailadres wat ermee gebeurde,
-- zodat je meteen ziet of er een adres niet gevonden is.


-- ------------------------------------------------------------
-- 1. Klopt de voorbereiding?
-- ------------------------------------------------------------
do $$
begin
  if not exists (
    select 1 from information_schema.columns
    where table_schema = 'public'
      and table_name = 'profiles'
      and column_name = 'plusklas_code'
  ) then
    raise exception
      'De kolom plusklas_code bestaat nog niet. Draai eerst groepen.sql.';
  end if;
end $$;


-- ------------------------------------------------------------
-- 2. De indeling
-- ------------------------------------------------------------
-- De codes zoeken we op zonder op hoofdletters te letten, zodat het niet
-- uitmaakt of ze in de databank als iktest of als IKTEST staan.
--
-- Let op de twee accounts van Thian: thiangoedgezelschap2@gmail.com en
-- thiangoedgezelschap3@gmail.com. Allebei naar iktest. Klopt dat niet, haal
-- dan de verkeerde regel hieronder weg voor je het script draait.
create temporary table indeling_tijdelijk (email text primary key, groep text)
  on commit drop;

insert into indeling_tijdelijk (email, groep) values
  -- iktest
  ('thiangoedgezelschap2@gmail.com', 'iktest'),
  ('thiangoedgezelschap3@gmail.com', 'iktest'),
  ('mauronoben@gmail.com',           'iktest'),
  ('dezlyhaesendonckx8@gmail.com',   'iktest'),
  ('conny.nulens1@telenet.be',       'iktest'),
  ('dm1nlucas@gmail.com',            'iktest'),

  -- de plusklas van Hasselt
  ('melissa.singh_nieuw@outlook.com', 'plusklas26hasselt'),
  ('mwai.zipporah@gmail.com',         'plusklas26hasselt'),
  ('kim.dussart@live.be',             'plusklas26hasselt'),

  -- de testgroep
  ('claeys.stoffels@gmail.com',   'toptester2026'),
  ('sarahsplingaer@hotmail.com',  'toptester2026'),
  ('elseke.jacobs@gmail.com',     'toptester2026'),
  ('louicy@gmail.com',            'toptester2026'),
  ('nele_somers86@hotmail.com',   'toptester2026'),
  ('marianne_vanroy@hotmail.com', 'toptester2026'),
  ('annick.ulburghs@hotmail.com', 'toptester2026'),
  ('marjolein.desmedt@gmail.com', 'toptester2026'),
  ('pcoolsaet@hotmail.com',       'toptester2026'),
  ('marlin078@gmail.com',         'toptester2026'),
  ('kimdussart87@gmail.com',      'toptester2026');


-- ------------------------------------------------------------
-- 3. Bestaan die drie codes wel?
-- ------------------------------------------------------------
-- Zo niet, dan zou de update er null van maken en kwam iedereen alsnog onder
-- "Nog geen groep" terecht. Beter meteen stoppen met een leesbare melding.
do $$
declare ontbreekt text;
begin
  select string_agg(distinct i.groep, ', ')
    into ontbreekt
    from indeling_tijdelijk i
   where not exists (
     select 1 from public.plusklas_codes c
      where lower(c.code) = i.groep
   );
  if ontbreekt is not null then
    raise exception
      'Deze codes staan niet in de tabel plusklas_codes: %. Kijk de schrijfwijze na bij Beheer, Plusklas-codes.',
      ontbreekt;
  end if;
end $$;


-- ------------------------------------------------------------
-- 4. Zetten maar
-- ------------------------------------------------------------
-- Het mailadres staat in auth.users, niet in profiles, dus we zoeken het gezin
-- daarlangs. Hoofdletters in een mailadres maken niet uit.
-- De koppeling aan plusklas_codes staat er als binnenste join, niet als
-- subvraag: zo kan er nooit per ongeluk null in de kolom belanden als een code
-- toch anders blijkt te heten. Dan gebeurt er gewoon niets, en zegt het
-- lijstje onderaan dat het niet gelukt is.
update public.profiles p
   set plusklas_code = c.code
  from auth.users u
  join indeling_tijdelijk i on i.email = lower(u.email)
  join public.plusklas_codes c on lower(c.code) = i.groep
 where p.id = u.id;


-- ------------------------------------------------------------
-- 5. Wat is er gebeurd?
-- ------------------------------------------------------------
-- Eén regel per mailadres uit de lijst hierboven. Staat er ergens
-- "niet gevonden", dan bestaat dat account niet onder dat adres: kijk het na
-- op een typfout en pas de lijst aan.
select
  i.email                                     as mailadres,
  i.groep                                     as bedoelde_groep,
  coalesce(p.full_name, '— niet gevonden —')  as gezin,
  coalesce(p.plusklas_code, '— geen groep —') as staat_nu_op,
  case
    when p.id is null then 'NIET GEVONDEN'
    when lower(coalesce(p.plusklas_code, '')) = i.groep then 'ok'
    else 'NIET GELUKT'
  end                                         as resultaat
from indeling_tijdelijk i
left join auth.users u on lower(u.email) = i.email
left join public.profiles p on p.id = u.id
order by i.groep, i.email;
