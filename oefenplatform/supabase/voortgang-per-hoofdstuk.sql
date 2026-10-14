-- Vinkjes en sterren die wegbleven bij de hoofdstukken achteraan
-- =============================================================
--
-- Een ouder meldde op 14 oktober 2026: "bij de oefenreeksen vanaf de reeks
-- Woordsoorten deel 1 wordt er niet meer afgecheckt dat je ze gemaakt hebt en
-- krijg je ook geen sterren meer."
--
-- De oorzaak zat niet in die hoofdstukken. Om de vinkjes te zetten vroeg de
-- pagina élk antwoord op dat dit kind ooit gaf, en de databank geeft op zo'n
-- vraag hoogstens een vast aantal rijen terug (standaard duizend), zonder
-- foutmelding. In "voortgang" staat één rij per beantwoorde vraag, dus een
-- kind dat zestien hoofdstukken een paar keer overdeed, zat boven die grens.
-- Wat erna kwam, viel buiten het antwoord en kreeg dus geen vinkje meer.
--
-- Deze functie laat de databank zelf groeperen: één rij per hoofdstuk, met de
-- laatste keer dat het kind er aan werkte. Dat zijn er hooguit zoveel als er
-- hoofdstukken op de pagina staan, dus de grens is niet meer in zicht.
--
-- Eén keer draaien in de sql-editor van het oefenplatform. Daarna werkt het
-- platform er meteen mee; tot dan haalt het de rijen zelf blok per blok op, en
-- staan de vinkjes er dus ook al.

create or replace function public.voortgang_per_hoofdstuk(
  p_kind uuid,
  p_hoofdstukken uuid[]
)
returns table (hoofdstuk_id uuid, laatst timestamptz)
language sql
stable
security definer
set search_path = public
as $$
  select v.hoofdstuk_id, max(v.beantwoord_op) as laatst
  from public.voortgang v
  where v.kind_id = p_kind
    and v.hoofdstuk_id = any (p_hoofdstukken)
  group by v.hoofdstuk_id
$$;

-- Enkel de server mag dit vragen. De pagina vraagt het via een serveractie die
-- eerst nakijkt of de ingelogde ouder dit kind mag bekijken; een bezoeker of
-- een ingelogde ouder komt er zelf niet aan.
revoke all on function public.voortgang_per_hoofdstuk(uuid, uuid[]) from public;
revoke all on function public.voortgang_per_hoofdstuk(uuid, uuid[]) from anon;
revoke all on function public.voortgang_per_hoofdstuk(uuid, uuid[]) from authenticated;
grant execute on function public.voortgang_per_hoofdstuk(uuid, uuid[]) to service_role;

-- De index die deze functie gebruikt staat al in schema.sql; dit zet hem erbij
-- voor een databank van vóór 27 september 2026.
create index if not exists voortgang_kind_hoofdstuk_idx
  on public.voortgang (kind_id, hoofdstuk_id);

select count(*) as hoofdstukken_met_werk
from (
  select distinct hoofdstuk_id from public.voortgang where hoofdstuk_id is not null
) t;
