-- ============================================================
-- HETZELFDE WEETJE MAAR ÉÉN KEER
-- ============================================================
-- Eén keer draaien in de SQL-editor van het oefenplatform-project, ná
-- weetjes.sql en weetjes-bericht.sql.
--
-- Waarvoor: op 8 oktober 2026 stond hetzelfde weetje eenentwintig keer in de
-- lijst, allemaal van hetzelfde kind. Ze wou het op het bord krijgen en zag
-- niet dat het al binnen was, dus stuurde ze het telkens opnieuw.
--
-- Dit bestand doet twee dingen: het ruimt de bestaande dubbels op, en het legt
-- daarna vast dat hetzelfde kind hetzelfde weetje geen tweede keer kan
-- insturen. Hoofdletters en extra spaties tellen daarbij niet mee, dus "Wist
-- je dat..." en "wist  je dat..." gelden als hetzelfde briefje.
--
-- Het oefenplatform houdt een dubbel weetje ook zelf al tegen en zegt dan
-- "dit hebben we al van je". Deze index staat daar naast: een controle in de
-- pagina alleen is nooit genoeg, want twee tabbladen of een trage
-- herlaadbeurt komen er langs.
--
-- Veilig om twee keer te draaien.

-- 1. De dubbels weg. Per kind en per weetje blijft er één over: dat wat al op
--    het bord hangt, en anders het oudste. Zo verdwijnt er nooit een briefje
--    van het prikbord, en blijft het antwoord dat jij er eventueel bij
--    schreef staan.
with genummerd as (
  select
    id,
    row_number() over (
      partition by profile_id, lower(regexp_replace(btrim(tekst), '\s+', ' ', 'g'))
      order by goedgekeurd desc, aangemaakt_op asc, id asc
    ) as plaats
  from public.weetjes
  where profile_id is not null
)
delete from public.weetjes w
using genummerd g
where w.id = g.id and g.plaats > 1;

-- 2. En vanaf nu kan het niet meer.
--    De bewerking hieronder staat ook in app/weetjes/acties.ts, in de functie
--    `gelijk`. Verandert de ene, verander dan ook de andere.
create unique index if not exists weetjes_geen_dubbels_idx
  on public.weetjes (profile_id, lower(regexp_replace(btrim(tekst), '\s+', ' ', 'g')))
  where profile_id is not null;
