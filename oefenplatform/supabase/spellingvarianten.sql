-- Wisselende woorden bij spellingvragen
-- Plak dit bestand in het Supabase dashboard onder "SQL Editor" en klik "Run".
-- Kan meerdere keren veilig uitgevoerd worden.
--
-- Waarom dit bestaat: een testgezin vroeg op 29 september 2026 of een kind dat
-- een hoofdstuk opnieuw maakt andere woorden kan krijgen. Kim bakende dat af op
-- 30 september 2026: enkel bij spelling, met een stuk of vijf woorden in
-- roulatie per vraag. Bij een inhoudsvraag blijft de leerstof de leerstof, maar
-- bij spelling zit de leerstof in de regel en niet in het woord, dus vijf
-- woorden onder dezelfde regel toetsen precies hetzelfde.

-- 1. De woorden zelf. Een lijstje met per beurt één alternatief; elk alternatief
--    vervangt alleen de velden die het zelf noemt, de rest blijft van de vraag.
--    Bijvoorbeeld:
--      [{"vraag": "Wat is het meervoud van 'kind'?",
--        "opties": ["kinderen", "kinds", "kindes", "kinderes"],
--        "antwoord": 0,
--        "uitleg": "..."}]
--    De vraag zelf is beurt 1; wat hier staat, zijn beurt 2, 3, 4 en 5.
alter table public.vragen add column if not exists varianten jsonb;

-- 2. Welke beurt een kind kreeg, bij het antwoord bewaard. Zonder deze kolom
--    zou een ouder die meekijkt de vraag over 'man' zien staan met het antwoord
--    'kinderen' eronder. null of 0 betekent: de vraag zelf.
alter table public.voortgang add column if not exists variant int;

-- Klaar. Er verandert niets aan bestaande vragen: zolang "varianten" leeg is,
-- ziet een kind altijd dezelfde vraag, net als vroeger.
