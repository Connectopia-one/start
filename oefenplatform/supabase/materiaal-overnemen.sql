-- ============================================================
-- LINKEN VAN HET OUDERPORTAAL OVERNEMEN OP "HANDIG MATERIAAL"
-- ============================================================
-- Het ouderportaal en het oefenplatform staan in twee APARTE Supabase-
-- projecten. Daarom kan je niet in één keer van de ene tabel naar de andere
-- kopiëren. Het gaat wel in drie stappen, zonder iets over te typen:
--
--   stap 1 en 2 draai je in het Supabase-project van het OUDERPORTAAL
--   stap 3 draai je in het Supabase-project van het OEFENPLATFORM
--
-- Let op één ding vooraf: het lesmateriaal in het ouderportaal staat achter
-- een login, per klasje. De pagina "Handig materiaal" is voor IEDEREEN
-- zichtbaar, ook zonder account. Wat je overzet, staat dus publiek. Daarom
-- laat stap 1 je eerst zien wat er staat, en maakt stap 2 één regel per link,
-- zodat je een regel die er niet op hoort gewoon kan weglaten.
--
-- PDF's gaan hier NIET mee. Die staan als bestand in de opslag van het
-- ouderportaal; een bestand verhuist niet met een SQL-regel. Wil je een pdf
-- ook op het oefenplatform, laad die dan opnieuw op via /beheer/materiaal.


-- ------------------------------------------------------------
-- STAP 1 — in het OUDERPORTAAL: kijken wat er staat
-- ------------------------------------------------------------
select k.naam as klasje,
       m.titel,
       m.inhoud as link,
       m.created_at
from public.materialen m
join public.klasjes k on k.id = m.klasje_id
where m.type = 'link'
  and coalesce(m.inhoud, '') <> ''
order by k.naam, m.created_at;


-- ------------------------------------------------------------
-- STAP 2 — in het OUDERPORTAAL: de regels laten schrijven
-- ------------------------------------------------------------
-- Dit verandert niets. Het maakt enkel de tekst die je in stap 3 plakt.
-- Het antwoord is één groot vak. Klik erop: Supabase toont de volledige
-- tekst opzij, met een knop om te kopiëren.
--
-- De naam van het klasje wordt de kop waaronder de link op de pagina komt.
-- Wil je ze allemaal onder één kop, vervang dan  quote_literal(k.naam)
-- door bijvoorbeeld  quote_literal('Handig om te weten')  .
select coalesce(string_agg(
         'insert into public.materiaal (groep, type, titel, link) select '
         || quote_literal(k.naam) || ', ''link'', '
         || quote_literal(m.titel) || ', '
         || quote_literal(m.inhoud)
         || ' where not exists (select 1 from public.materiaal'
         || ' where titel = ' || quote_literal(m.titel)
         || ' and link = ' || quote_literal(m.inhoud) || ');',
         E'\n' order by k.naam, m.created_at
       ), '-- Geen linken gevonden in het ouderportaal.'
       ) as plak_dit_in_het_oefenplatform
from public.materialen m
join public.klasjes k on k.id = m.klasje_id
where m.type = 'link'
  and coalesce(m.inhoud, '') <> '';


-- ------------------------------------------------------------
-- STAP 3 — in het OEFENPLATFORM: plakken en uitvoeren
-- ------------------------------------------------------------
-- Plak hier wat stap 2 je gaf en klik Run. Elke regel kijkt eerst of dezelfde
-- titel met hetzelfde webadres er al staat, dus je mag dit gerust twee keer
-- doen: je krijgt geen dubbels.
--
-- Daarna staan ze op  oefenplatform.connectopia.one/materiaal  en kan je ze
-- op  /beheer/materiaal  verder aanpassen of een omschrijving geven.
