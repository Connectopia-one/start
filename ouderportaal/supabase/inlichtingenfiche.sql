-- ============================================================
-- DE INLICHTINGENFICHE VOOR EEN KAMP
-- ============================================================
--
-- Kim, 9 oktober 2026. De fiche vroeg tot nu de naam, de geboortedatum,
-- allergieën, diagnoses, één noodcontact en twee vinkjes over foto's. Voor een
-- dag op een kamp is dat te dun: wie medicatie moet geven, wie het kind mag
-- ophalen en wat helpt als het te veel wordt, stond er niet in.
--
-- Dit bestand zet er zeven dingen bij. Draai het één keer in de sql-editor van
-- het ouderportaal (niet die van het oefenplatform: die twee hebben elk hun
-- eigen Supabase).
--
--   1. medicatie, met de dosis en het moment
--   2. de huisarts, naam en telefoonnummer
--   3. een tweede noodnummer, voor als het eerste niet opneemt
--   4. wie het kind mag ophalen, en of het alleen naar huis mag
--   5. eten buiten een allergie, zoals vegetarisch of geen varkensvlees
--   6. wat helpt als het je kind te veel wordt
--   7. school en leerjaar
--
-- Alles mag leeg blijven. Een gezin dat de fiche vorige week invulde, verliest
-- niets: de bestaande kolommen worden niet aangeraakt en de nieuwe beginnen
-- gewoon leeg.
--
-- Dit zijn gegevens van kinderen, dus ze vallen onder dezelfde regels als de
-- rest van de tabel: enkel het eigen gezin, het team en de beheerder kunnen ze
-- lezen. Die regels staan al op de tabel en gelden meteen ook voor deze
-- kolommen; er hoeft dus niets aan de policies te veranderen.
--
-- Let op: de sql-editor van Supabase draait dit bestand als één geheel. Gaat er
-- iets mis achteraan, dan wordt ook het begin teruggedraaid. Je krijgt dan een
-- rode melding en er is niets veranderd; plak het gerust opnieuw.

alter table public.kinderen add column if not exists medicatie text;
alter table public.kinderen add column if not exists huisarts_naam text;
alter table public.kinderen add column if not exists huisarts_telefoon text;
alter table public.kinderen add column if not exists noodcontact2_naam text;
alter table public.kinderen add column if not exists noodcontact2_telefoon text;
alter table public.kinderen add column if not exists ophalen text;
alter table public.kinderen
  add column if not exists alleen_naar_huis boolean not null default false;
alter table public.kinderen add column if not exists eten text;
alter table public.kinderen add column if not exists wat_helpt text;
alter table public.kinderen add column if not exists school text;
alter table public.kinderen add column if not exists leerjaar text;

-- Klaar. Ga naar ouders.connectopia.one, meld je aan en open "Mijn gezin":
-- de nieuwe vakjes staan er dan bij, onder de allergieën.
