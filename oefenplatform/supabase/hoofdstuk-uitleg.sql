-- Een korte uitleg onder de titel van een hoofdstuk.
--
-- Caroline en Marjolein schreven in de enquête van november 2026 dat het soms
-- zoeken is welk blokje je nodig hebt, en wat erachter zit. De titels zelf
-- blijven zoals ze zijn, want de leer- en oefenbundels en de imports hangen
-- aan die titels. Daarom een apart veld, dat Kim in Beheer → Vakken invult.
--
-- Zolang dit niet gedraaid is, tonen de pagina's gewoon geen uitleg.

alter table public.hoofdstukken add column if not exists korte_uitleg text;
