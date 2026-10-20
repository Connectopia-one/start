-- Een logo bij de organisaties die iemand aanbracht voor de gids.
-- Plak dit volledige bestand in het Supabase dashboard onder "SQL Editor" en klik "Run".
-- Dezelfde Supabase als het ouderportaal. Kan meerdere keren veilig uitgevoerd worden.
--
-- Het logo zelf staat in de open bak "social" (die van In de kijker), in de map gids/.
-- Hier bewaren we enkel waar het staat.

alter table public.gids_aanmeldingen
  add column if not exists logo text check (char_length(logo) <= 300);

-- Bezoekers mogen het logo lezen, net als naam, omschrijving, regio en link.
grant select (id, naam, omschrijving, regio, link, logo)
  on public.gids_aanmeldingen to anon, authenticated;

notify pgrst, 'reload schema';

select 'het logo kan nu bij de gids' as resultaat, count(*) as aantal
  from public.gids_aanmeldingen;
