-- In de kijker: berichten van sociale media op de website
-- Plak dit volledige bestand in het Supabase dashboard onder "SQL Editor" en klik "Run".
-- Dit is dezelfde Supabase als het ouderportaal; de tabellen staan los van elkaar.
-- Kan meerdere keren veilig uitgevoerd worden.

create extension if not exists pgcrypto;

-- ============================================================
-- DE TABEL
-- Eén rij per bericht dat op /in-de-kijker staat.
--
-- "volledige_naam" en "contact" vullen we alleen in als iemand van buiten
-- zijn bericht instuurt, zodat we weten wie het was. Die twee zijn NIET
-- publiek: bezoekers mogen die kolommen niet lezen, zie de rechten onderaan.
--
-- "zichtbaar" staat standaard op false. Een bericht dat iemand instuurt,
-- staat dus pas op de site als jij het goedkeurt in het ouderportaal.
-- ============================================================

create table if not exists public.kijker_posts (
  id uuid primary key default gen_random_uuid(),
  titel text check (char_length(titel) <= 120),
  tekst text not null check (char_length(tekst) between 2 and 600),
  van text not null check (char_length(van) between 2 and 80),
  kanaal text not null default 'anders' check (
    kanaal in ('facebook', 'instagram', 'linkedin', 'tiktok', 'youtube', 'anders')
  ),
  link text not null check (link like 'https://%' and char_length(link) <= 400),
  -- Het pad van het beeld in de bucket "social", of leeg voor een bericht
  -- zonder beeld. Het beeld zet jij erbij in het ouderportaal.
  beeld text check (char_length(beeld) <= 400),
  -- Een bericht van onszelf krijgt een ander kleurtje dan een bericht van
  -- iemand anders, zodat een lezer meteen ziet wie aan het woord is.
  eigen boolean not null default false,
  zichtbaar boolean not null default false,
  gezien boolean not null default false,
  volledige_naam text check (char_length(volledige_naam) <= 120),
  contact text check (char_length(contact) <= 120),
  created_at timestamptz not null default now()
);

create index if not exists kijker_posts_zichtbaar_idx
  on public.kijker_posts (zichtbaar, created_at desc);

-- ============================================================
-- RECHTEN
-- Bezoekers van de website (de rol "anon") mogen:
--   - de goedgekeurde berichten lezen, zonder de naam en het mailadres
--     van wie ze instuurde
--   - zelf een bericht insturen, dat nog niet zichtbaar is
-- Ze mogen niets wijzigen of verwijderen, en ze kunnen hun eigen bericht
-- niet zichtbaar maken: "zichtbaar" staat niet in de lijst hieronder, dus
-- blijft het op false staan. Goedkeuren gebeurt alleen via het beheer in
-- het ouderportaal, dat de service-role sleutel gebruikt.
-- ============================================================

alter table public.kijker_posts enable row level security;

drop policy if exists "iedereen leest zichtbare posts" on public.kijker_posts;
create policy "iedereen leest zichtbare posts"
  on public.kijker_posts for select
  to anon, authenticated
  using (zichtbaar);

drop policy if exists "iedereen stuurt een post in" on public.kijker_posts;
create policy "iedereen stuurt een post in"
  on public.kijker_posts for insert
  to anon, authenticated
  with check (true);

revoke all on public.kijker_posts from anon, authenticated;
grant select (id, titel, tekst, van, kanaal, link, beeld, eigen, created_at)
  on public.kijker_posts to anon, authenticated;
grant insert (titel, tekst, van, kanaal, link, volledige_naam, contact)
  on public.kijker_posts to anon, authenticated;

-- ============================================================
-- DE BEELDEN
-- Een open bak, want deze beelden staan toch op de website. Alleen jij
-- kan er iets in zetten of uit halen.
-- ============================================================

insert into storage.buckets (id, name, public)
values ('social', 'social', true)
on conflict (id) do update set public = true;

drop policy if exists "social schrijven" on storage.objects;
create policy "social schrijven" on storage.objects for insert
  with check (bucket_id = 'social' and public.is_beheerder());

drop policy if exists "social verwijderen" on storage.objects;
create policy "social verwijderen" on storage.objects for delete
  using (bucket_id = 'social' and public.is_beheerder());
