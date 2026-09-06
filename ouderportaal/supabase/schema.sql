-- Ouderportaal Connectopia — databaseschema
-- Plak dit volledige bestand in het Supabase dashboard onder "SQL Editor" en klik "Run".
-- Kan meerdere keren veilig uitgevoerd worden (gebruikt "if not exists" / "or replace").

create extension if not exists pgcrypto;

-- ============================================================
-- TABELLEN
-- ============================================================

-- Eén rij per account (ouder of beheerder). De id komt overeen met auth.users.id.
create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  full_name text not null,
  role text not null default 'ouder' check (role in ('ouder', 'beheerder')),
  created_at timestamptz not null default now()
);

-- Klasjes / groepen.
create table if not exists public.klasjes (
  id uuid primary key default gen_random_uuid(),
  naam text not null,
  slug text not null unique,
  created_at timestamptz not null default now()
);

-- Per gezin, per klasje: welke toegang heeft dit gezin?
-- materiaal en fotos staan LOS van elkaar — dat is de privacy-scheiding.
create table if not exists public.toegang (
  id uuid primary key default gen_random_uuid(),
  profile_id uuid not null references public.profiles(id) on delete cascade,
  klasje_id uuid not null references public.klasjes(id) on delete cascade,
  materiaal boolean not null default true,
  fotos boolean not null default false,
  created_at timestamptz not null default now(),
  unique (profile_id, klasje_id)
);

-- Lesmateriaal: pdf, link of aankondiging.
create table if not exists public.materialen (
  id uuid primary key default gen_random_uuid(),
  klasje_id uuid not null references public.klasjes(id) on delete cascade,
  type text not null check (type in ('pdf', 'link', 'aankondiging')),
  titel text not null,
  inhoud text,
  bestandspad text,
  created_at timestamptz not null default now(),
  created_by uuid references public.profiles(id) on delete set null
);

-- Foto's — apart bewaard van lesmateriaal, met een eigen toegangsvlag.
create table if not exists public.fotos (
  id uuid primary key default gen_random_uuid(),
  klasje_id uuid not null references public.klasjes(id) on delete cascade,
  bestandspad text not null,
  bijschrift text,
  created_at timestamptz not null default now(),
  created_by uuid references public.profiles(id) on delete set null
);

-- ============================================================
-- HULPFUNCTIE
-- ============================================================

-- security definer: mag de profiles-tabel raadplegen zonder in een lus
-- met zijn eigen RLS-regels terecht te komen.
create or replace function public.is_beheerder()
returns boolean
language sql
security definer
set search_path = public
stable
as $$
  select exists (
    select 1 from public.profiles
    where id = auth.uid() and role = 'beheerder'
  );
$$;

-- ============================================================
-- ROW LEVEL SECURITY
-- ============================================================

alter table public.profiles enable row level security;
alter table public.klasjes enable row level security;
alter table public.toegang enable row level security;
alter table public.materialen enable row level security;
alter table public.fotos enable row level security;

drop policy if exists "eigen profiel lezen" on public.profiles;
create policy "eigen profiel lezen" on public.profiles for select
  using (id = auth.uid() or public.is_beheerder());

drop policy if exists "beheerder profiel beheer" on public.profiles;
create policy "beheerder profiel beheer" on public.profiles for all
  using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "klasjes lezen" on public.klasjes;
create policy "klasjes lezen" on public.klasjes for select
  using (
    public.is_beheerder() or exists (
      select 1 from public.toegang t
      where t.klasje_id = klasjes.id and t.profile_id = auth.uid()
    )
  );

drop policy if exists "klasjes beheer" on public.klasjes;
create policy "klasjes beheer" on public.klasjes for all
  using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "eigen toegang lezen" on public.toegang;
create policy "eigen toegang lezen" on public.toegang for select
  using (profile_id = auth.uid() or public.is_beheerder());

drop policy if exists "beheerder toegang beheer" on public.toegang;
create policy "beheerder toegang beheer" on public.toegang for all
  using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "materialen lezen" on public.materialen;
create policy "materialen lezen" on public.materialen for select
  using (
    public.is_beheerder() or exists (
      select 1 from public.toegang t
      where t.klasje_id = materialen.klasje_id
        and t.profile_id = auth.uid()
        and t.materiaal = true
    )
  );

drop policy if exists "materialen beheer" on public.materialen;
create policy "materialen beheer" on public.materialen for all
  using (public.is_beheerder()) with check (public.is_beheerder());

drop policy if exists "fotos lezen" on public.fotos;
create policy "fotos lezen" on public.fotos for select
  using (
    public.is_beheerder() or exists (
      select 1 from public.toegang t
      where t.klasje_id = fotos.klasje_id
        and t.profile_id = auth.uid()
        and t.fotos = true
    )
  );

drop policy if exists "fotos beheer" on public.fotos;
create policy "fotos beheer" on public.fotos for all
  using (public.is_beheerder()) with check (public.is_beheerder());

-- ============================================================
-- STORAGE (bestanden)
-- ============================================================

insert into storage.buckets (id, name, public)
values ('materialen', 'materialen', false)
on conflict (id) do nothing;

insert into storage.buckets (id, name, public)
values ('fotos', 'fotos', false)
on conflict (id) do nothing;

drop policy if exists "materiaal lezen" on storage.objects;
create policy "materiaal lezen" on storage.objects for select
  using (
    bucket_id = 'materialen' and (
      public.is_beheerder() or exists (
        select 1 from public.materialen m
        join public.toegang t on t.klasje_id = m.klasje_id
        where m.bestandspad = storage.objects.name
          and t.profile_id = auth.uid()
          and t.materiaal = true
      )
    )
  );

drop policy if exists "materiaal schrijven" on storage.objects;
create policy "materiaal schrijven" on storage.objects for insert
  with check (bucket_id = 'materialen' and public.is_beheerder());

drop policy if exists "materiaal verwijderen" on storage.objects;
create policy "materiaal verwijderen" on storage.objects for delete
  using (bucket_id = 'materialen' and public.is_beheerder());

drop policy if exists "fotos lezen storage" on storage.objects;
create policy "fotos lezen storage" on storage.objects for select
  using (
    bucket_id = 'fotos' and (
      public.is_beheerder() or exists (
        select 1 from public.fotos f
        join public.toegang t on t.klasje_id = f.klasje_id
        where f.bestandspad = storage.objects.name
          and t.profile_id = auth.uid()
          and t.fotos = true
      )
    )
  );

drop policy if exists "fotos schrijven" on storage.objects;
create policy "fotos schrijven" on storage.objects for insert
  with check (bucket_id = 'fotos' and public.is_beheerder());

drop policy if exists "fotos verwijderen" on storage.objects;
create policy "fotos verwijderen" on storage.objects for delete
  using (bucket_id = 'fotos' and public.is_beheerder());

-- ============================================================
-- JOUW EIGEN BEHEERDER-ACCOUNT
-- ============================================================
-- Maak eerst jezelf aan via Supabase dashboard -> Authentication -> Users -> Add user.
-- Kopieer daarna het "User UID" en vervang hieronder, en voer dan dit stukje apart uit:
--
-- insert into public.profiles (id, full_name, role)
-- values ('PLAK-HIER-JOUW-USER-UID', 'Kim', 'beheerder')
-- on conflict (id) do update set role = 'beheerder';
