-- ============================================================
-- DE OPVOLGING OPSPLITSEN PER CODE — /begeleiding
-- ============================================================
-- Kim op 6 oktober 2026: "ik wou de groep van de plusklas apart opvolgen van
-- de testgroepen, maar iedereen staat overal."
--
-- Tot nu stond er op een gezin één vinkje, is_plusklas. Of je nu met
-- TOPTESTER2026, met iktest of met PLUSKLAS26HASSELT registreerde, je kwam in
-- hetzelfde opvolgscherm terecht. Vanaf nu onthoudt het profiel ook MET WELKE
-- code een gezin registreerde, en krijgt elke code zijn eigen scherm.
--
-- is_plusklas blijft bestaan en blijft doen wat het deed: het bepaalt of een
-- gezin gratis toegang heeft en of er een fiche is. De nieuwe kolom zegt
-- alleen bij welke groep het gezin hoort.
--
-- Gezinnen die zich vóór vandaag registreerden hebben nog geen groep. Die
-- staan in het scherm onder "Nog geen groep", en je zet ze er zelf bij met het
-- keuzelijstje op de fiche van een kind.
--
-- Voer dit één keer uit in de SQL Editor van het Supabase-project van het
-- OEFENPLATFORM. Een tweede keer draaien kan geen kwaad.


-- ------------------------------------------------------------
-- 1. De kolom
-- ------------------------------------------------------------
alter table public.profiles add column if not exists plusklas_code text;

-- De verwijzing naar de codetabel komt er apart bij, zodat dit bestand ook
-- draait op een databank waar de kolom al stond.
-- on update cascade: hernoem je ooit een code, dan schuiven de gezinnen mee.
-- on delete set null: verwijder je een code, dan blijven de gezinnen bestaan
-- en komen ze onder "Nog geen groep" te staan. Hun gratis toegang blijft.
do $$
begin
  if not exists (
    select 1 from pg_constraint where conname = 'profiles_plusklas_code_fkey'
  ) then
    alter table public.profiles
      add constraint profiles_plusklas_code_fkey
      foreign key (plusklas_code) references public.plusklas_codes(code)
      on update cascade on delete set null;
  end if;
end $$;

-- Zoeken per groep gaat zo over een index in plaats van over de hele tabel.
create index if not exists profiles_plusklas_code_idx
  on public.profiles (plusklas_code)
  where plusklas_code is not null;


-- ------------------------------------------------------------
-- 2. Wie mag de groep van een gezin lezen en veranderen?
-- ------------------------------------------------------------
-- Lezen: dat loopt al via de bestaande regels. Een begeleider mag de profielen
-- van plusklasgezinnen lezen (zie plusklasfiche.sql), en die regel geldt voor
-- alle kolommen van die rij, dus ook voor deze nieuwe.
--
-- Veranderen: enkel de beheerder, via de bestaande regel "beheerder profiel
-- beheer". Een begeleider ziet het keuzelijstje niet staan. Zo kan niemand per
-- ongeluk een gezin naar een andere groep schuiven.
--
-- Er is hier dus geen nieuwe policy nodig. Dit blok staat er alleen om dat
-- zwart op wit te zetten, zodat het later niet als een vergetelheid leest.


-- ------------------------------------------------------------
-- 3. Klaar
-- ------------------------------------------------------------
-- Nieuwe gezinnen krijgen hun groep automatisch bij het registreren.
-- De gezinnen die er al stonden zet je zelf bij een groep, op de fiche van een
-- van hun kinderen.
