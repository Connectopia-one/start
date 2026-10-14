-- ============================================================
-- DE EXAMENSTER — drie keer een examen zonder fouten
-- ============================================================
-- Kim op 14 oktober 2026: "misschien moeten ze als ze minstens 3 x feilloos,
-- dus zonder fouten, een examen afleggen toch een examensticker krijgen?"
--
-- Tot nu hield het examen niets bij. Dat was met opzet: een examen loopt over
-- hoofdstukken die een kind nog niet maakte, en het hoort die vinkjes en
-- sterren niet in te kleuren. Dat blijft zo. Een afgelegd examen komt in een
-- eigen tabel terecht, náást de voortgang, en raakt er niets van aan.
--
-- De ster hangt aan het vak binnen een niveau: drie feilloze examens van
-- wiskunde ✨ Spark geven de examenster van wiskunde ✨ Spark.
--
-- Voer dit één keer uit in de SQL Editor van het Supabase-project van het
-- OEFENPLATFORM. Een tweede keer draaien kan geen kwaad.


-- ------------------------------------------------------------
-- 1. De tabel
-- ------------------------------------------------------------
-- Eén rij per afgelegd examen. We bewaren hoeveel vragen erin zaten en hoeveel
-- er juist waren; feilloos is dus juist = aantal. Zo kan je later ook zien
-- hoe een kind evolueert, en niet enkel of het de ster haalde.
create table if not exists public.examens (
  id uuid primary key default gen_random_uuid(),
  kind_id uuid not null references public.kinderen(id) on delete cascade,
  vak_id uuid not null references public.vakken(id) on delete cascade,
  niveau text not null,
  aantal integer not null,
  juist integer not null,
  -- Feilloos rekent de databank zelf uit, zodat tellen één vraag blijft.
  feilloos boolean generated always as (aantal > 0 and juist = aantal) stored,
  afgelegd_op timestamptz not null default now()
);

-- Voor een databank waar de tabel al stond zonder die kolom.
alter table public.examens
  add column if not exists feilloos boolean
  generated always as (aantal > 0 and juist = aantal) stored;

create index if not exists examens_kind_vak_idx
  on public.examens (kind_id, vak_id, niveau);

create index if not exists examens_feilloos_idx
  on public.examens (kind_id, feilloos);


-- ------------------------------------------------------------
-- 2. Wie mag wat?
-- ------------------------------------------------------------
-- Dezelfde regels als bij de stickers: een ouder leest en schrijft enkel voor
-- zijn eigen kinderen, de beheerder mag alles, en een begeleider leest mee bij
-- de kinderen van de plusklas.
alter table public.examens enable row level security;

drop policy if exists "eigen kind examens lezen" on public.examens;
create policy "eigen kind examens lezen" on public.examens for select
  using (
    public.is_beheerder() or exists (
      select 1 from public.kinderen k
       where k.id = examens.kind_id and k.profile_id = auth.uid()
    )
  );

drop policy if exists "eigen kind examens toevoegen" on public.examens;
create policy "eigen kind examens toevoegen" on public.examens for insert
  with check (
    public.is_beheerder() or exists (
      select 1 from public.kinderen k
       where k.id = examens.kind_id and k.profile_id = auth.uid()
    )
  );

drop policy if exists "beheerder examens beheer" on public.examens;
create policy "beheerder examens beheer" on public.examens for all
  using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "begeleider plusklasexamens lezen" on public.examens;
create policy "begeleider plusklasexamens lezen" on public.examens for select
  using (public.is_begeleider() and public.is_plusklas_kind(kind_id));


-- ------------------------------------------------------------
-- 3. Klaar
-- ------------------------------------------------------------
-- Vanaf nu telt het platform de feilloze examens per vak. Bij het derde komt
-- de examenster, op het examen zelf en bij de verzamelbadges.

select count(*) as examens_bewaard from public.examens;
