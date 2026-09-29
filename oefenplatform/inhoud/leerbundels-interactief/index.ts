// Gemaakt door inhoud/leerbundels/bron/maak_interactief.py — niet met de hand aanpassen.
// De sleutel is <niveau>/<vak-slug>/<hoofdstuk-slug>; zie lib/leerbundel.ts.

export const KLIKBARE_BUNDELS: Record<
  string,
  () => Promise<{ default: unknown }>
> = {
  "spark/frans/een-foto-of-afbeelding-beschrijven": () =>
    import("./frans--een-foto-of-afbeelding-beschrijven.json"),
  "spark/frans/een-franse-tekst-lezen": () =>
    import("./frans--een-franse-tekst-lezen.json"),
  "spark/frans/grammatica-lidwoorden-naamwoorden-en-voornaamwoorden": () =>
    import("./frans--grammatica-lidwoorden-naamwoorden-en-voornaamwoorden.json"),
  "spark/frans/grammatica-werkwoorden-tijden-en-zinsbouw": () =>
    import("./frans--grammatica-werkwoorden-tijden-en-zinsbouw.json"),
  "spark/frans/schrijven-berichten-uitnodigingen-en-mails": () =>
    import("./frans--schrijven-berichten-uitnodigingen-en-mails.json"),
  "spark/frans/tekstsoorten-signaalwoorden-en-verwijswoorden": () =>
    import("./frans--tekstsoorten-signaalwoorden-en-verwijswoorden.json"),
  "spark/frans/woordenschat-eten-wonen-kleding-en-dagelijkse-dingen": () =>
    import("./frans--woordenschat-eten-wonen-kleding-en-dagelijkse-dingen.json"),
  "spark/frans/woordenschat-getallen-tijd-weer-reizen-en-landen": () =>
    import("./frans--woordenschat-getallen-tijd-weer-reizen-en-landen.json"),
  "spark/frans/woordenschat-mensen-familie-gevoelens-en-gezondheid": () =>
    import("./frans--woordenschat-mensen-familie-gevoelens-en-gezondheid.json"),
  "spark/frans/woordenschat-school-beroepen-sport-en-vrije-tijd": () =>
    import("./frans--woordenschat-school-beroepen-sport-en-vrije-tijd.json"),
  "spark/geschiedenis/bronnen-kunst-en-beeldvorming": () =>
    import("./geschiedenis--bronnen-kunst-en-beeldvorming.json"),
  "spark/geschiedenis/de-prehistorie": () =>
    import("./geschiedenis--prehistorie.json"),
  "spark/geschiedenis/het-historisch-referentiekader": () =>
    import("./geschiedenis--historisch-referentiekader.json"),
  "spark/geschiedenis/het-oude-griekenland": () =>
    import("./geschiedenis--het-oude-griekenland.json"),
  "spark/geschiedenis/het-romeinse-rijk": () =>
    import("./geschiedenis--het-romeinse-rijk.json"),
  "spark/geschiedenis/mesopotamie-en-egypte": () =>
    import("./geschiedenis--mesopotamie-en-egypte.json"),
  "spark/natuurwetenschappen/cellen-weefsels-en-organen": () =>
    import("./natuurwetenschappen--cellen-weefsels-en-organen.json"),
  "spark/natuurwetenschappen/ecologie-en-biodiversiteit": () =>
    import("./natuurwetenschappen--ecologie-en-biodiversiteit.json"),
  "spark/natuurwetenschappen/energie-kracht-en-snelheid": () =>
    import("./natuurwetenschappen--energie-kracht-en-snelheid.json"),
  "spark/natuurwetenschappen/fotosynthese-en-de-plant": () =>
    import("./natuurwetenschappen--fotosynthese-en-de-plant.json"),
  "spark/natuurwetenschappen/het-menselijk-lichaam": () =>
    import("./natuurwetenschappen--het-menselijk-lichaam.json"),
  "spark/natuurwetenschappen/massadichtheid": () =>
    import("./natuurwetenschappen--massadichtheid.json"),
  "spark/natuurwetenschappen/materie-stoffen-en-mengsels": () =>
    import("./natuurwetenschappen--materie-stoffen-en-mengsels.json"),
  "spark/natuurwetenschappen/veilig-werken-meten-en-eenheden": () =>
    import("./natuurwetenschappen--veilig-werken-meten-en-eenheden.json"),
  "spark/natuurwetenschappen/voortplanting": () =>
    import("./natuurwetenschappen--voortplanting.json"),
  "spark/natuurwetenschappen/wetenschappelijk-onderzoek": () =>
    import("./natuurwetenschappen--wetenschappelijk-onderzoek.json"),
  "spark/nederlands/feiten-meningen-en-betrouwbaarheid": () =>
    import("./nederlands--feiten-meningen-en-betrouwbaarheid.json"),
  "spark/nederlands/literatuur-en-beeldspraak": () =>
    import("./nederlands--literatuur-en-beeldspraak.json"),
  "spark/nederlands/onderwerp-hoofdgedachte-en-hoofdpunten": () =>
    import("./nederlands--onderwerp-hoofdgedachte-en-hoofdpunten.json"),
  "spark/nederlands/register-taalvariatie-en-non-verbale-communicatie": () =>
    import("./nederlands--register-taalvariatie-en-non-verbale-communicatie.json"),
  "spark/nederlands/schrijven-spreken-en-gesprekken-voeren": () =>
    import("./nederlands--schrijven-spreken-en-gesprekken-voeren.json"),
  "spark/nederlands/spelling-leestekens-en-werkwoordsvormen": () =>
    import("./nederlands--spelling-leestekens-en-werkwoordsvormen.json"),
  "spark/nederlands/tekstsoorten-en-het-communicatiemodel": () =>
    import("./nederlands--tekstsoorten-en-het-communicatiemodel.json"),
  "spark/nederlands/tekststructuur-en-signaalwoorden": () =>
    import("./nederlands--tekststructuur-en-signaalwoorden.json"),
  "spark/nederlands/woordsoorten-en-woordvorming": () =>
    import("./nederlands--woordsoorten-en-woordvorming.json"),
  "spark/nederlands/zinsdelen-zinssoorten-en-congruentie": () =>
    import("./nederlands--zinsdelen-zinssoorten-en-congruentie.json"),
  "spark/wiskunde/data-en-onzekerheid": () =>
    import("./wiskunde--data-en-onzekerheid-spark.json"),
  "spark/wiskunde/getallenleer": () => import("./wiskunde--getallenleer.json"),
  "spark/wiskunde/meetkunde": () => import("./wiskunde--meetkunde-spark.json"),
  "spark/wiskunde/metend-rekenen": () =>
    import("./wiskunde--metend-rekenen-spark.json"),
  "spark/wiskunde/negatieve-getallen-en-procenten": () =>
    import("./wiskunde--negatieve-getallen-en-procenten-spark.json"),
  "spark/wiskunde/probleemoplossend-denken": () =>
    import("./wiskunde--probleemoplossend-denken-spark.json"),
  "spark/wiskunde/relaties-en-verandering": () =>
    import("./wiskunde--relaties-en-verandering-spark.json"),
  "spark/wiskunde/verzamelingen": () =>
    import("./wiskunde--verzamelingen-spark.json"),
  "spark/wiskunde/wiskundige-redeneringen-en-uitspraken": () =>
    import("./wiskunde--redeneringen-en-uitspraken-spark.json"),
  "start/aardrijkskunde/belgie": () =>
    import("./aardrijkskunde--belgie-landschap-en-streken.json"),
  "start/aardrijkskunde/belgie-landschap-en-streken": () =>
    import("./aardrijkskunde--belgie-landschap-en-streken.json"),
  "start/aardrijkskunde/europa-en-de-wereld": () =>
    import("./aardrijkskunde--europa-en-de-wereld.json"),
  "start/aardrijkskunde/kaartlezen-en-orientatie": () =>
    import("./aardrijkskunde--kaartlezen-en-orientatie.json"),
  "start/engels/de-tegenwoordige-tijd": () =>
    import("./engels--de-tegenwoordige-tijd.json"),
  "start/engels/mezelf-voorstellen": () =>
    import("./engels--mezelf-voorstellen.json"),
  "start/engels/op-school-en-onderweg": () =>
    import("./engels--op-school-en-onderweg.json"),
  "start/engels/to-be-en-to-have": () =>
    import("./engels--to-be-en-to-have.json"),
  "start/engels/woorden-voor-elke-dag": () =>
    import("./engels--woorden-voor-elke-dag.json"),
  "start/engels/zinnen-bouwen": () => import("./engels--zinnen-bouwen.json"),
  "start/geschiedenis/tijd-en-tijdlijn": () =>
    import("./geschiedenis--tijd-en-tijdlijn.json"),
  "start/geschiedenis/van-de-middeleeuwen-tot-nu": () =>
    import("./geschiedenis--van-de-middeleeuwen-tot-nu.json"),
  "start/geschiedenis/van-de-prehistorie-tot-de-romeinen": () =>
    import("./geschiedenis--van-de-prehistorie-tot-de-romeinen.json"),
  "start/nederlands/hoofdstuk-1-spelling-voorbeeld": () =>
    import("./nederlands--spelling.json"),
  "start/nederlands/lezen": () => import("./nederlands--lezen.json"),
  "start/nederlands/literatuur": () => import("./nederlands--literatuur.json"),
  "start/nederlands/schrijven": () => import("./nederlands--schrijven.json"),
  "start/nederlands/spelling": () => import("./nederlands--spelling.json"),
  "start/nederlands/spreken-en-luisteren": () =>
    import("./nederlands--spreken-en-luisteren.json"),
  "start/nederlands/taalsysteem-en-taalgebruik": () =>
    import("./nederlands--taalsysteem-en-taalgebruik.json"),
  "start/wetenschap-en-techniek/biologie-het-menselijk-lichaam": () =>
    import("./wetenschap-en-techniek--biologie-het-menselijk-lichaam.json"),
  "start/wetenschap-en-techniek/biologie-leven-en-ecologie": () =>
    import("./wetenschap-en-techniek--biologie-leven-en-ecologie.json"),
  "start/wetenschap-en-techniek/chemie-stoffen-en-mengsels": () =>
    import("./wetenschap-en-techniek--chemie-stoffen-en-mengsels.json"),
  "start/wetenschap-en-techniek/de-aarde-en-de-ruimte": () =>
    import("./wetenschap-en-techniek--de-aarde-en-de-ruimte.json"),
  "start/wetenschap-en-techniek/natuurkunde-energie-en-krachten": () =>
    import("./wetenschap-en-techniek--natuurkunde-energie-en-krachten.json"),
  "start/wetenschap-en-techniek/natuurkunde-licht-geluid-en-elektriciteit":
    () =>
      import("./wetenschap-en-techniek--natuurkunde-licht-geluid-en-elektriciteit.json"),
  "start/wetenschap-en-techniek/techniek-ontwerpen-en-maken": () =>
    import("./wetenschap-en-techniek--techniek-ontwerpen-en-maken.json"),
  "start/wiskunde/bewerkingen": () => import("./wiskunde--bewerkingen.json"),
  "start/wiskunde/getallenkennis": () =>
    import("./wiskunde--getallenkennis.json"),
  "start/wiskunde/kansrekenen-en-statistiek": () =>
    import("./wiskunde--kansrekenen-en-statistiek.json"),
  "start/wiskunde/meetkunde": () => import("./wiskunde--meetkunde.json"),
  "start/wiskunde/meten-en-metend-rekenen": () =>
    import("./wiskunde--meten-en-metend-rekenen.json"),
  "start/wiskunde/rekenen-en-breuken": () =>
    import("./wiskunde--rekenen-en-breuken.json"),
  "start/wiskunde/vraagstukken-en-problemen-oplossen": () =>
    import("./wiskunde--vraagstukken-en-problemen-oplossen.json"),
};
