-- ============================================================
-- VOLLE OPVOLGING ENKEL WAAR JE ZE NODIG HEBT — /begeleiding
-- ============================================================
-- Kim op 14 oktober 2026: "ik moet ook enkel van de kindjes van de plusklas
-- code PLUSKLAS26HASSELT in detail kunnen opvolgen, en daar zou alles van bij
-- gehouden moeten worden. De andere is het leuk om zo in een tabel de
-- voortgang te zien maar daar moet geen zware opvolging bij zitten."
--
-- Tot nu kreeg elk gezin met een plusklascode dezelfde fiche: voortgang per
-- hoofdstuk, de opgeloste testen, opmerkingen en werk van thuis. Ook de
-- testgezinnen dus, en dat is zware opvolging voor niets.
--
-- Vanaf nu staat op elke code of die groep volle opvolging krijgt. Eén vinkje,
-- te zetten bij Beheer, Plusklas-codes, zodat het volgend schooljaar met een
-- nieuwe code gewoon weer kan.
--
-- Voer dit één keer uit in de SQL Editor van het Supabase-project van het
-- OEFENPLATFORM. Een tweede keer draaien kan geen kwaad.


-- ------------------------------------------------------------
-- 1. Het vinkje op een code
-- ------------------------------------------------------------
alter table public.plusklas_codes
  add column if not exists volledige_opvolging boolean not null default false;

comment on column public.plusklas_codes.volledige_opvolging is
  'Krijgt deze groep de volle fiche (opmerkingen, werk van thuis, opgeloste testen)? Anders enkel de tabel met de voortgang.';

-- De plusklas van Hasselt is de groep die je in detail opvolgt.
update public.plusklas_codes
   set volledige_opvolging = true
 where upper(code) = 'PLUSKLAS26HASSELT';


-- ------------------------------------------------------------
-- 2. De cijfers voor de tabel, door de databank zelf geteld
-- ------------------------------------------------------------
-- De tabel met de voortgang haalde tot nu élk antwoord van élk kind op om er
-- de aantallen uit te tellen. Dat is zwaar, en boven een duizend rijen geeft
-- de databank niet alles terug. Deze functie telt zelf en geeft één rij per
-- kind.
--
-- Bewust ZONDER "security definer": de functie werkt met de rechten van wie ze
-- vraagt, dus de regels van de databank blijven gelden. Een ouder krijgt zo
-- enkel de cijfers van zijn eigen kinderen, een begeleider die van de
-- plusklaskinderen, en jij die van allemaal.
create or replace function public.opvolging_per_kind()
returns table (
  kind_id uuid,
  aantal bigint,
  juist bigint,
  sterren bigint,
  laatst timestamptz
)
language sql
stable
set search_path = public
as $$
  select k.id,
         count(v.id),
         count(v.id) filter (where v.correct),
         (select count(*) from public.stickers s where s.kind_id = k.id),
         max(v.beantwoord_op)
  from public.kinderen k
  left join public.voortgang v on v.kind_id = k.id
  group by k.id
$$;

grant execute on function public.opvolging_per_kind() to authenticated;
grant execute on function public.opvolging_per_kind() to service_role;


-- ------------------------------------------------------------
-- 3. Klaar
-- ------------------------------------------------------------
-- Wat je nu ziet:
--   * PLUSKLAS26HASSELT: de volle fiche, zoals je ze kent.
--   * de andere groepen: de tabel met hun voortgang, zonder fiche.
-- Een groep verzetten doe je met het vinkje bij Beheer, Plusklas-codes.

select code, label, volledige_opvolging
from public.plusklas_codes
order by volledige_opvolging desc, created_at desc;
