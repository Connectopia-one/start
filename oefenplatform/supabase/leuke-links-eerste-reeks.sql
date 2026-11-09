-- ============================================================
-- LEUKE LINKS — eerste reeks gratis links (Kim, 9 november 2026)
-- ============================================================
-- Draai EERST materiaal-soort.sql. Daarna dit bestand, één keer, in de SQL
-- Editor van het Supabase-project van het oefenplatform.
-- Er wordt niets verwijderd. Een link die er voor hetzelfde schoolniveau al
-- staat, wordt overgeslagen, dus twee keer draaien kan geen kwaad.
-- Achteraf aanpassen of verwijderen kan op /beheer/materiaal.

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'KlasCement', 'https://www.klascement.net/', 'Gratis lesmateriaal van de Vlaamse overheid, gedeeld door leerkrachten: werkbladen om af te drukken, oefeningen en lesideeën voor elk vak.', 'links', 'lager'
where not exists (select 1 from public.materiaal where link = 'https://www.klascement.net/' and schoolniveau = 'lager');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'Computermeester', 'https://www.computermeester.be/', 'Honderden gratis oefenspelletjes voor wiskunde, taal en wereldoriëntatie, per leerjaar tot en met het 6de leerjaar.', 'links', 'lager'
where not exists (select 1 from public.materiaal where link = 'https://www.computermeester.be/' and schoolniveau = 'lager');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'Spelletjesplein', 'https://www.spelletjesplein.nl/', 'Gratis leerspelletjes voor rekenen, taal, aardrijkskunde en geschiedenis, verdeeld over meer dan 100 pleinen. Er staat reclame op.', 'links', 'lager'
where not exists (select 1 from public.materiaal where link = 'https://www.spelletjesplein.nl/' and schoolniveau = 'lager');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'De Maaltafels', 'https://www.demaaltafels.be/', 'De tafels van 1 tot 12 oefenen met opdrachten, spelletjes, een tempotoets en werkbladen, met een tafeldiploma op het einde. Er staat reclame op.', 'links', 'lager'
where not exists (select 1 from public.materiaal where link = 'https://www.demaaltafels.be/' and schoolniveau = 'lager');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'Klokrekenen', 'https://www.klokrekenen.be/', 'Zelf oefenbladen maken om de klok te leren lezen, digitaal of met wijzers, om af te drukken. Er staat reclame op.', 'links', 'lager'
where not exists (select 1 from public.materiaal where link = 'https://www.klokrekenen.be/' and schoolniveau = 'lager');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'Seterra', 'https://www.seterra.com/nl', 'Aardrijkskunde als spel: meer dan 400 kaartquizzen over landen, hoofdsteden, rivieren en vlaggen.', 'links', 'lager'
where not exists (select 1 from public.materiaal where link = 'https://www.seterra.com/nl' and schoolniveau = 'lager');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'Woordenlijst', 'https://woordenlijst.org/', 'De officiële spelling van de Taalunie. Twijfel je hoe je een woord schrijft of afbreekt? Hier zoek je het op.', 'links', 'lager'
where not exists (select 1 from public.materiaal where link = 'https://woordenlijst.org/' and schoolniveau = 'lager');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'Boekenzoeker', 'https://www.boekenzoeker.be/', 'Een boek vinden dat bij je leeftijd en je smaak past, met tips van lezers.', 'links', 'lager'
where not exists (select 1 from public.materiaal where link = 'https://www.boekenzoeker.be/' and schoolniveau = 'lager');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'VRT voor leerkrachten', 'https://www.vrt.be/nl/vrt-voor-leerkrachten', 'Lesmateriaal bij programma''s van de VRT, zoals Ketnet in de klas en EDUbox-lespakketten.', 'links', 'lager'
where not exists (select 1 from public.materiaal where link = 'https://www.vrt.be/nl/vrt-voor-leerkrachten' and schoolniveau = 'lager');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'Het Archief voor Onderwijs', 'https://onderwijs.hetarchief.be/', 'Gratis filmpjes en geluidsfragmenten van Vlaamse zenders en musea, zonder reclame. Leerkrachten maken een gratis account.', 'links', 'lager'
where not exists (select 1 from public.materiaal where link = 'https://onderwijs.hetarchief.be/' and schoolniveau = 'lager');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Studie- en oefentips', 'link', 'Huiswerk maken: 10 tips', 'https://www.oudersvannu.nl/kind/school/huiswerk-maken-10-tips', 'Tips voor ouders om een kind van de lagere school zelfstandig huiswerk te leren maken.', 'links', 'lager'
where not exists (select 1 from public.materiaal where link = 'https://www.oudersvannu.nl/kind/school/huiswerk-maken-10-tips' and schoolniveau = 'lager');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Studie- en oefentips', 'link', 'Huiswerktips voor ouders', 'https://www.zwijsen.nl/app/uploads/zwijsen-files/huiswerktips.pdf', 'Een overzichtelijke prent met tips over huiswerk op de lagere school: hoe je je kind helpt zonder het werk over te nemen.', 'links', 'lager'
where not exists (select 1 from public.materiaal where link = 'https://www.zwijsen.nl/app/uploads/zwijsen-files/huiswerktips.pdf' and schoolniveau = 'lager');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Studie- en oefentips', 'link', 'Examencommissie basisonderwijs', 'https://www.vlaanderen.be/een-getuigschrift-basisonderwijs-behalen-via-de-examencommissie-basisonderwijs', 'Alles over het getuigschrift basisonderwijs halen via de examencommissie: inschrijven, de examens en wat je moet kennen.', 'links', 'lager'
where not exists (select 1 from public.materiaal where link = 'https://www.vlaanderen.be/een-getuigschrift-basisonderwijs-behalen-via-de-examencommissie-basisonderwijs' and schoolniveau = 'lager');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'KlasCement', 'https://www.klascement.net/', 'Gratis lesmateriaal van de Vlaamse overheid, gedeeld door leerkrachten: werkbladen, oefeningen en lesideeën voor elk vak.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://www.klascement.net/' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'GeoGebra', 'https://www.geogebra.org/', 'Gratis wiskundeprogramma''s: grafieken tekenen, meetkunde en een rekenmachine, rechtstreeks in je browser.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://www.geogebra.org/' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'PhET-simulaties', 'https://phet.colorado.edu/nl/', 'Gratis simulaties voor fysica, chemie, biologie en wiskunde. Je ziet zelf wat er gebeurt als je iets verandert.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://phet.colorado.edu/nl/' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'Khan Academy in het Nederlands', 'https://nl.khanacademy.org/', 'Uitlegfilmpjes en oefeningen, vooral voor wiskunde, in je eigen tempo.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://nl.khanacademy.org/' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'Seterra', 'https://www.seterra.com/nl', 'Aardrijkskunde als spel: meer dan 400 kaartquizzen over landen, hoofdsteden, rivieren en vlaggen.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://www.seterra.com/nl' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'Woordenlijst', 'https://woordenlijst.org/', 'De officiële spelling van de Taalunie. Twijfel je hoe je een woord schrijft of afbreekt? Hier zoek je het op.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://woordenlijst.org/' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'Boekenzoeker', 'https://www.boekenzoeker.be/', 'Een boek vinden dat bij je leeftijd en je smaak past, ook voor jongeren tot 18 jaar.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://www.boekenzoeker.be/' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'VRT voor leerkrachten', 'https://www.vrt.be/nl/vrt-voor-leerkrachten', 'Lesmateriaal bij programma''s van de VRT, zoals EDUbox-lespakketten en filmpjes van KLAAR.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://www.vrt.be/nl/vrt-voor-leerkrachten' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Materiaal en oefensites', 'link', 'Het Archief voor Onderwijs', 'https://onderwijs.hetarchief.be/', 'Gratis filmpjes en geluidsfragmenten van Vlaamse zenders en musea, zonder reclame. Leerkrachten maken een gratis account.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://onderwijs.hetarchief.be/' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Studie- en oefentips', 'link', 'Fiches leren leren', 'https://pro.katholiekonderwijs.vlaanderen/download/content/54d83244-c542-4251-9d19-335631068999/attachments/fiches_leren_leren_voor_leerlingen.pdf', '25 korte fiches voor leerlingen: plannen, samenvatten, schema''s maken en jezelf controleren.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://pro.katholiekonderwijs.vlaanderen/download/content/54d83244-c542-4251-9d19-335631068999/attachments/fiches_leren_leren_voor_leerlingen.pdf' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Studie- en oefentips', 'link', 'Examencommissie secundair onderwijs: examens plannen', 'https://www.vlaanderen.be/examencommissiesecundaironderwijs/examens-plannen', 'Hoe je je examens bij de examencommissie plant en inschrijft, rechtstreeks bij de Vlaamse overheid.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://www.vlaanderen.be/examencommissiesecundaironderwijs/examens-plannen' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Studie- en oefentips', 'link', 'Efficiënt studeren', 'https://www.uantwerpen.be/nl/studentenleven/welzijn-voor-studenten/succesvol-studeren/studiestrategieen/', 'Studietips van de Universiteit Antwerpen: verwerken, onthouden en herhalen. Vooral handig in de 3de graad.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://www.uantwerpen.be/nl/studentenleven/welzijn-voor-studenten/succesvol-studeren/studiestrategieen/' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Studie- en oefentips', 'link', 'Haal het maximum uit je hersenen', 'https://www.durfdenken.be/nl/onderzoek-en-maatschappij/haal-het-maximum-uit-je-hersenen', 'Wat onderzoek zegt over slim leren, van de Universiteit Gent.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://www.durfdenken.be/nl/onderzoek-en-maatschappij/haal-het-maximum-uit-je-hersenen' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Studie- en oefentips', 'link', 'Hoe ga je om met stress?', 'https://www.durfdenken.be/nl/studentenleven/de-examenvragen-hoe-ga-je-om-met-stress', 'Tips van de Universiteit Gent om rustig te blijven in de examenperiode.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://www.durfdenken.be/nl/studentenleven/de-examenvragen-hoe-ga-je-om-met-stress' and schoolniveau = 'middelbaar');

insert into public.materiaal (groep, type, titel, link, omschrijving, soort, schoolniveau)
select 'Studie- en oefentips', 'link', 'Sidekick Sam Academy', 'https://www.sidekicksamacademy.be/nl/', 'Gratis lespakketten, filmpjes en podcasts over hoe jongeren zich voelen, zoals eenzaamheid, voor leerkrachten en ouders.', 'links', 'middelbaar'
where not exists (select 1 from public.materiaal where link = 'https://www.sidekicksamacademy.be/nl/' and schoolniveau = 'middelbaar');
