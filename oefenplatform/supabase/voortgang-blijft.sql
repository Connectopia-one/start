-- ============================================================
-- DE VOORTGANG BLIJFT STAAN ALS JE VRAGEN VERVANGT
-- Eén keer draaien in de SQL-editor van het oefenplatform-project.
-- Kan meerdere keren veilig uitgevoerd worden.
-- ============================================================
--
-- Wat er misging: elk beantwoord vraagje in "voortgang" hing met een harde
-- band aan de vraag zelf, met "on delete cascade" erbij. Laad je een
-- vragenbestand opnieuw in met "vervangen" aan, dan wist het platform eerst de
-- oude vragen van dat hoofdstuk. De databank gooide daarbij stilletjes ook elk
-- antwoord weg dat aan zo'n vraag hing. Resultaat: alle kinderen op nul, terwijl
-- er aan de leerstof niets veranderd was.
--
-- Kim zag dat op 27 september 2026, net voor de tien testgezinnen beginnen.
--
-- Wat dit bestand doet:
--   1. bij elk antwoord wordt voortaan ook het hoofdstuk bewaard, los van de
--      vraag. Zo weten we nog altijd wat een kind gemaakt heeft, ook als die
--      ene vraag niet meer bestaat.
--   2. de band met de vraag wordt losser: verdwijnt de vraag, dan blijft de rij
--      staan met een lege vraag in plaats van te verdwijnen.
--
-- Wat je kwijt bent, blijft kwijt: dit herstelt niets van vóór vandaag.

-- ------------------------------------------------------------
-- 1. Het hoofdstuk bij elk antwoord
-- ------------------------------------------------------------
alter table public.voortgang
  add column if not exists hoofdstuk_id uuid references public.hoofdstukken(id) on delete cascade;

-- Voor alles wat er al staat: het hoofdstuk van de vraag overnemen.
update public.voortgang v
   set hoofdstuk_id = q.hoofdstuk_id
  from public.vragen q
 where q.id = v.vraag_id
   and v.hoofdstuk_id is null;

-- De schermen tellen per kind en per hoofdstuk; zonder deze index wordt dat
-- traag zodra er een schooljaar aan antwoorden in staat.
create index if not exists voortgang_kind_hoofdstuk_idx
  on public.voortgang (kind_id, hoofdstuk_id);

-- ------------------------------------------------------------
-- 2. Een lossere band met de vraag
-- ------------------------------------------------------------
-- De naam van de band is die van het schema; hij wordt eerst weggehaald en
-- daarna opnieuw gelegd, nu met "set null" in plaats van "cascade".
alter table public.voortgang drop constraint if exists voortgang_vraag_id_fkey;
alter table public.voortgang alter column vraag_id drop not null;
alter table public.voortgang
  add constraint voortgang_vraag_id_fkey
  foreign key (vraag_id) references public.vragen(id) on delete set null;
