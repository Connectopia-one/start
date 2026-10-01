# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Nederlands 🌍 Beyond.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere teksten om in te delen, andere zinnen om te ontleden, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een oordeel
verantwoorden, een beeld in eigen woorden omschrijven). Wie hier iets
bijschrijft, legt het eerst naast `../../beyond/nederlands.json` en naast de
twee vakfiches.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond". Het voorvoegsel is nodig omdat leerbundels en oefenbundels in
dezelfde bronmap gerenderd worden en anders dezelfde bestandsnaam zouden
krijgen.

Geen enkel citaat hieronder is van een bestaande auteur. Waar een voorbeeldzin
of een voorbeeldregel staat, is die zelf geschreven en staat er geen naam bij.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Nederlands"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een oordeel: zeg niet alleen wát je vindt, maar ook waaróm, met een begrip uit de leerstof.",
    "Bij een voorbeeldzin: lees ze eerst hardop, dan hoor je vaak al waar het antwoord zit.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-tekstsoorten-en-teksttypes-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Tekstsoorten en teksttypes",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke tekstsoort?",
             opdracht="Schrijf bij elke tekst de tekstsoort die het hoofddoel het best dekt.",
             oefeningen=[
                 ("rij", [("een bijsluiter bij een geneesmiddel", "prescriptief"),
                          ("een verslag van een schooluitstap", "narratief"),
                          ("een affiche voor een goed doel", "persuasief")], "Welke soort?", WW),
                 ("rij", [("een lezersbrief over het fietspadenbeleid", "opiniërend"),
                          ("een dossier over de werking van een batterij", "informatief"),
                          ("een kortverhaal in een jeugdtijdschrift", "literair")], "Welke soort?", WW),
             ]),
        dict(kop="Meer dan één doel",
             opdracht="Noteer bij elke tekst alle doelen die erin zitten.",
             oefeningen=[
                 ("open", "Een podcast van een natuurvereniging vertelt het verhaal van een "
                          "gewonde bosuil, legt uit hoe een opvangcentrum werkt en vraagt op het "
                          "einde om lid te worden.",
                  "Narratief (het verhaal van de uil), informatief (hoe het opvangcentrum werkt) en "
                  "persuasief (de oproep om lid te worden).", 3),
                 ("open", "Een recensie van een restaurant beschrijft de gerechten en de prijzen, "
                          "en besluit dat het de moeite niet is.",
                  "Informatief (de gerechten en de prijzen) en opiniërend (het oordeel op het einde). "
                  "Het hoofddoel is opiniërend.", 3),
             ]),
        dict(kop="Wie is de zender?",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Een energiebedrijf laat een klimaatwetenschapper in een filmpje uitleggen "
                          "waarom aardgas een tussenstap is. Wie is de echte zender, en wat doe je "
                          "met die vaststelling?",
                  "De wetenschapper spreekt, maar het energiebedrijf is de echte zender: het betaalt "
                  "en kiest wat er gezegd wordt. Je leest het filmpje dus als persuasief en je zoekt "
                  "een tweede bron die geen belang heeft bij het antwoord.", 4),
                 ("open", "Waarom zegt de tekstsoort op zich niets over de betrouwbaarheid?",
                  "Een informatieve tekst kan fout zijn en een persuasieve tekst kan waar zijn. De "
                  "soort zet je wel op je hoede: bij een persuasieve tekst weet je dat de zender iets "
                  "van je wil.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De lees- en luisterteksten op het examen zijn altijd in het "
                          "Standaardnederlands.", False),
                 ("waar", "Een strip kan een literaire tekst zijn.", True),
                 ("waar", "Een tekst met veel feiten is daarom een informatieve tekst.", False),
                 ("waar", "Dezelfde vragen over zender, doel en publiek gelden bij een luistertekst.", True),
             ]),
        dict(kop="Zelf schrijven",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Schrijf over hetzelfde onderwerp (de schoolbibliotheek) één persuasieve en "
                          "één informatieve zin. Zet erbij waaraan men het verschil ziet.",
                  "Bijvoorbeeld persuasief: Kom eindelijk eens langs in de bibliotheek, je weet niet "
                  "wat je mist. Informatief: De schoolbibliotheek is elke middag open van twaalf tot "
                  "één. Het verschil zit in de oproep, de toon en de overdrijving.", 5),
                 ("open", "Een stand-upcomedian vertelt over zijn jeugd met veel woordspelingen. Welke "
                          "twee soorten herken je, en waarom?",
                  "Narratief, want hij vertelt een verhaal, en literair, want de vorm zelf (de "
                  "woordspelingen, het ritme) is een deel van het effect.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-onderwerp-hoofdgedachte-en-samenvatten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Onderwerp, hoofdgedachte en samenvatten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Onderwerp of hoofdgedachte?",
             opdracht="Noteer bij elke formulering of het een onderwerp of een hoofdgedachte is.",
             oefeningen=[
                 ("rij", [("het openbaar vervoer", "onderwerp"),
                          ("de bus is te duur voor wie hem het hardst nodig heeft", "hoofdgedachte"),
                          ("slaaptekort bij jongeren", "onderwerp")], "Wat is het?", W),
                 ("rij", [("wie te weinig slaapt, presteert slechter op school", "hoofdgedachte"),
                          ("zwerfvuil in de bermen", "onderwerp"),
                          ("statiegeld zou het zwerfvuil fors terugdringen", "hoofdgedachte")],
                  "Wat is het?", W),
             ]),
        dict(kop="Van tekst naar kern",
             opdracht="Lees het stukje en antwoord.",
             oefeningen=[
                 ("tekst", "<em>Steeds meer scholen zetten hun boeken digitaal. Dat scheelt gewicht in "
                           "de boekentas en de uitgever kan een hoofdstuk bijwerken zonder te "
                           "herdrukken. Toch blijkt uit toetsen dat leerlingen een tekst op papier "
                           "beter onthouden. Wie digitaal werkt, scrollt sneller door en leest "
                           "oppervlakkiger. Een school die overstapt, doet er dus goed aan het lezen "
                           "op papier niet helemaal los te laten.</em>"),
                 ("kort", "Wat is het onderwerp?", "digitale schoolboeken", WL),
                 ("open", "Wat is de hoofdgedachte? Schrijf ze in één zin.",
                  "Digitale schoolboeken hebben voordelen, maar omdat leerlingen op papier beter "
                  "onthouden, moet een school het papieren lezen niet helemaal opgeven.", 3),
                 ("open", "Noteer de twee hoofdpunten die de hoofdgedachte ondersteunen.",
                  "Eén: digitaal scheelt gewicht en laat de uitgever bijwerken. Twee: uit toetsen "
                  "blijkt dat leerlingen op papier beter onthouden, omdat ze digitaal "
                  "oppervlakkiger lezen.", 3),
                 ("kort", "Welk signaalwoord kondigt de tegenstelling aan?", "toch", W),
             ]),
        dict(kop="Notities",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Noem drie eisen waaraan goede notities voldoen.",
                  "Ze sluiten aan bij de inhoud van de tekst, ze zijn duidelijk genoeg om er daarna "
                  "mee te werken, en ze mogen afkortingen, symbolen en telegramstijl bevatten.", 3),
                 ("open", "Wat is het voordeel van een mindmap boven een lijstje?",
                  "In een mindmap zie je de verbanden tussen de delen staan; een lijstje zet alles "
                  "onder elkaar zonder te tonen wat waarbij hoort.", 3),
             ]),
        dict(kop="Samenvatten",
             opdracht="Kruis aan of antwoord.",
             oefeningen=[
                 ("waar", "In een samenvatting mag je zinnen letterlijk overnemen.", False),
                 ("waar", "Een samenvatting mag de volgorde van de oorspronkelijke tekst veranderen.", True),
                 ("waar", "Je eigen mening hoort in een samenvatting thuis.", False),
                 ("open", "Een leerling levert een samenvatting in die bijna even lang is als het "
                          "origineel. Wat liep er mis, en wat moet hij doen?",
                  "Hoofd- en bijzaken zijn niet gescheiden. Hij moet de voorbeelden, de herhalingen en "
                  "de anekdotes schrappen en enkel de hoofdgedachte en de hoofdpunten laten staan.", 4),
             ]),
        dict(kop="Vat zelf samen",
             opdracht="Gebruik het tekstje van reeks 2.",
             oefeningen=[
                 ("open", "Vat het tekstje over digitale schoolboeken samen in maximaal dertig "
                          "woorden, in je eigen woorden.",
                  "Bijvoorbeeld: Digitale boeken zijn lichter en makkelijk bij te werken, maar wie van "
                  "een scherm leest, onthoudt minder. Scholen houden het papieren lezen dus het best "
                  "deels aan.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-bronnen-beoordelen-betrouwbaarheid-nepnieuws-en-framing-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Bronnen beoordelen: betrouwbaarheid, nepnieuws en framing",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk criterium?",
             opdracht="Noteer bij elke vraag welk beoordelingscriterium ze nagaat.",
             oefeningen=[
                 ("rij", [("Wie betaalt deze website?", "de zender en zijn belang"),
                          ("Staat dit ook in een andere bron?", "de bevestiging elders"),
                          ("Van wanneer is dit artikel?", "de actualiteit")], "Welk criterium?", WL),
                 ("rij", [("Heb ik dit nodig voor mijn opdracht?", "de relevantie voor mijn doel"),
                          ("Zijn dit feiten of meningen?", "feiten of meningen"),
                          ("Welke bronnen gebruikt de tekst zelf?", "de bronnen van de tekst")],
                  "Welk criterium?", WL),
             ]),
        dict(kop="Beoordeel de bron",
             opdracht="Schrijf telkens een oordeel mét reden.",
             oefeningen=[
                 ("open", "Je vindt een artikel over de voordelen van een voedingssupplement op de "
                          "site van de fabrikant. Er staat een naam van een auteur bij en er worden "
                          "twee studies genoemd. Wat besluit je?",
                  "De zender heeft belang bij het antwoord, dus je leest het als "
                  "bedrijfscommunicatie. De auteursnaam en de studies zijn pluspunten, maar je gaat "
                  "zelf na wie die studies uitvoerde en betaalde, en je zoekt een onafhankelijke "
                  "bron.", 5),
                 ("open", "Je vindt hetzelfde bericht op zes sites, telkens met dezelfde zinnen. "
                          "Waarom is dat geen zesvoudige bevestiging?",
                  "Dezelfde zinnen wijzen erop dat het zes keer dezelfde bron is, overgenomen zonder "
                  "controle. Bevestiging betekent dat onafhankelijke bronnen tot hetzelfde komen.", 4),
                 ("open", "Een anonieme account meldt dat een bekende winkelketen sluit, met een link "
                          "naar een onbekende site vol advertenties. Wat is je eerste stap, en wat is "
                          "waarschijnlijk het doel?",
                  "Eerste stap: kijken of een nieuwsredactie het ook bericht. Het doel is "
                  "waarschijnlijk bezoekers naar die site halen, want de advertenties leveren per "
                  "bezoeker geld op.", 4),
             ]),
        dict(kop="Framing",
             opdracht="Herschrijf of leg uit.",
             oefeningen=[
                 ("rij", [("besparing", "belastingverlaging"),
                          ("gelukzoeker", "vluchteling"),
                          ("klimaatontwrichting", "klimaatverandering")],
                  "Schrijf de tegenovergestelde framing van hetzelfde feit.", WW),
                 ("open", "Een grafiek bij een artikel heeft een zij-as die bij 95 begint. Wat doet "
                          "dat met de lezer, en is de grafiek daarmee onwaar?",
                  "Een klein verschil lijkt enorm. De cijfers kloppen wel, dus de grafiek is niet "
                  "onwaar; ze is misleidend. Dat is precies waarom een tekst vol feiten toch een "
                  "vertekend beeld kan geven.", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een professioneel ogende website is een bewijs van betrouwbaarheid.", False),
                 ("waar", "Informatie van vijf jaar oud is altijd onbruikbaar.", False),
                 ("waar", "Een publireportage moet herkenbaar zijn als betaalde inhoud.", True),
                 ("waar", "Propaganda wil je koopgedrag sturen en reclame je denken.", False),
             ]),
        dict(kop="Jezelf nakijken",
             opdracht="Beantwoord eerlijk en in volledige zinnen.",
             oefeningen=[
                 ("open", "Leg uit wat een echokamer is en wat een filterbubbel, en noem het verschil.",
                  "Een echokamer is een omgeving waarin je vooral je eigen mening terughoort. Een "
                  "filterbubbel is het gevolg van een algoritme dat je vooral toont wat bij je past, "
                  "waardoor je de rest niet meer ziet. Het eerste gaat over de groep, het tweede over "
                  "de techniek erachter.", 5),
                 ("open", "Waarom kijk je een bericht dat je eigen mening bevestigt minder streng na? "
                          "Wat doe je daaraan?",
                  "Omdat het geen weerstand oproept: het bevestigt wat je al dacht, dus je zoekt geen "
                  "fouten. Je lost het op door bij zo'n bericht bewust dezelfde vragen te stellen als "
                  "bij een bericht dat je tegenspreekt.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-communicatiemodel-en-ruis-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het communicatiemodel en ruis",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vul het model in",
             opdracht="Vul de tabel aan voor deze situatie: een sportclub stuurt een mail aan alle "
                      "leden om te melden dat de training verplaatst is.",
             oefeningen=[
                 ("tabel", ["Onderdeel", "In deze situatie"],
                  [["Zender", None], ["Ontvanger", None], ["Boodschap", None],
                   ["Kanaal", None], ["Doel", None]],
                  "Zender: de sportclub. Ontvanger: de leden. Boodschap: de training is verplaatst. "
                  "Kanaal: de mail. Doel: dat iedereen op het juiste moment komt opdagen.", WL),
             ]),
        dict(kop="Doel of effect?",
             opdracht="Noteer bij elke situatie of er sprake is van het doel of van het effect.",
             oefeningen=[
                 ("rij", [("de spot wil dat je het product koopt", "doel"),
                          ("jij onthoudt alleen het liedje", "effect"),
                          ("de waarschuwing doet mensen lachen", "effect")], "Wat is het?", W),
                 ("open", "Leg in twee zinnen uit waarom doel en effect niet hetzelfde zijn.",
                  "Het doel zit bij de zender: wat hij wil bereiken. Het effect zit bij de ontvanger: "
                  "wat de boodschap bij hem teweegbrengt. Ze vallen vaak maar niet altijd samen.", 3),
             ]),
        dict(kop="Externe of interne ruis?",
             opdracht="Noteer welke soort ruis er speelt.",
             oefeningen=[
                 ("rij", [("een drilboor voor het raam", "externe ruis"),
                          ("piekeren over een ruzie", "interne ruis"),
                          ("een slecht leesbaar lettertype", "externe ruis")], "Welke ruis?", WW),
                 ("rij", [("vakjargon dat de lezer niet kent", "interne ruis"),
                          ("een haperende videoverbinding", "externe ruis"),
                          ("vermoeidheid na een nachtje doorhalen", "interne ruis")], "Welke ruis?", WW),
             ]),
        dict(kop="Analyseer",
             opdracht="Schrijf telkens enkele zinnen.",
             oefeningen=[
                 ("open", "Een verpleegkundige legt in vaktaal uit wat een uitslag betekent. De "
                          "patiënt knikt maar begrijpt niets. Waar ging het mis, en bij wie?",
                  "Bij de zender: hij hield geen rekening met zijn ontvanger. De vaktaal werkte als "
                  "ruis. Komt een boodschap niet aan, dan ligt dat dus niet automatisch aan de "
                  "ontvanger.", 4),
                 ("open", "Een school stuurt een belangrijke mededeling enkel via een app die de "
                          "helft van de ouders niet gebruikt. Welk onderdeel van het model koos men "
                          "slecht, en wat is het gevolg?",
                  "Het kanaal. De helft van de ontvangers krijgt de boodschap nooit te zien, hoe goed "
                  "ze ook geschreven is.", 4),
                 ("open", "Een filmpje over een ernstig onderwerp staat tussen grappige filmpjes op "
                          "een platform. Welk onderdeel speelt hier mee en waarom?",
                  "De context waarin de boodschap landt. Wie net zat te lachen, schakelt niet meteen "
                  "om, en dat verandert het effect van het filmpje.", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Ruis zit altijd bij de ontvanger.", False),
                 ("waar", "Emoji's horen bij de boodschap.", True),
                 ("waar", "Het communicatiemodel gebruik je enkel bij geschreven teksten.", False),
                 ("waar", "Een zender kan tegelijk ontvanger zijn.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-tekstopbouw-alineaverbanden-en-structuuraanduiders-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Tekstopbouw, alineaverbanden en structuuraanduiders",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk verband?",
             opdracht="Noteer het verband dat de beginwoorden van de alinea aankondigen.",
             oefeningen=[
                 ("rij", [("Daar staat tegenover dat...", "tegenstellend"),
                          ("Daarom besloot de raad...", "concluderend"),
                          ("Om dat te bereiken, voerde men...", "doel-middel")], "Welk verband?", WW),
                 ("rij", [("Dat kwam doordat...", "oorzakelijk"),
                          ("Op voorwaarde dat...", "voorwaardelijk"),
                          ("In 1950, en later in 1970...", "chronologisch")], "Welk verband?", WW),
             ]),
        dict(kop="Welke vaste tekststructuur?",
             opdracht="Noteer welke van de negen structuren de tekst volgt.",
             oefeningen=[
                 ("rij", [("eerst de files, dan de oorzaken, dan de oplossingen", "de probleemstructuur"),
                          ("een vraag, een methode, resultaten, een besluit", "de onderzoeksstructuur"),
                          ("hoe de postbedeling in zestig jaar veranderde", "de ontwikkelingsstructuur")],
                  "Welke structuur?", WL),
                 ("rij", [("trein en auto naast elkaar op prijs en tijd", "de vergelijkingsstructuur"),
                          ("hoe je een lekke band plakt, stap voor stap", "de handelingsstructuur"),
                          ("de film beoordeeld op spel, beeld en muziek", "de evaluatiestructuur")],
                  "Welke structuur?", WL),
             ]),
        dict(kop="Structuuraanduiders",
             opdracht="Beantwoord kort.",
             oefeningen=[
                 ("kort", "Verwijswoorden en signaalwoorden heten samen...", "structuuraanduiders", WW),
                 ("kort", "Welk verband legt het signaalwoord 'want'?", "redengevend", W),
                 ("kort", "Ten eerste, ten tweede en tot slot wijzen op welk verband?", "opsommend", W),
                 ("open", "Waarom kan hetzelfde signaalwoord in twee teksten een ander verband "
                          "aangeven? Geef een voorbeeld.",
                  "Omdat het verband uit de inhoud volgt, niet uit het woord alleen. 'Dus' kan een "
                  "conclusie inleiden, maar ook gewoon de draad weer oppakken na een uitweiding.", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Eén alinea behandelt één deelonderwerp.", True),
                 ("waar", "Eén tekst kan maar één vaste tekststructuur bevatten.", False),
                 ("waar", "Een tekst met een goede lay-out heeft daarom ook een goede inhoud.", False),
                 ("waar", "Tussentitels maken een tekst toegankelijker.", True),
             ]),
        dict(kop="Zelf opbouwen",
             opdracht="Schrijf in volledige zinnen.",
             oefeningen=[
                 ("open", "Je schrijft een tekst over het afschaffen van huiswerk. Noteer in "
                          "steekwoorden wat er in je inleiding, je midden en je slot komt.",
                  "Inleiding: het onderwerp neerzetten en de interesse wekken, bijvoorbeeld met een "
                  "cijfer over hoeveel tijd leerlingen eraan besteden. Midden: de deelonderwerpen, "
                  "één per alinea, met de argumenten voor en tegen. Slot: het besluit, dus je "
                  "standpunt en wat eruit volgt.", 6),
                 ("open", "Noem drie dingen die je het eerst bekijkt om te weten of een lange tekst "
                          "nuttig voor je is.",
                  "De titel, de tussentitels en het slot. Samen zeggen ze waar de tekst over gaat en "
                  "waar hij op uitdraait.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-argumentatie-en-drogredenen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Argumentatie en drogredenen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Feit of mening?",
             opdracht="Noteer bij elke zin of het een feit of een mening is.",
             oefeningen=[
                 ("rij", [("de bibliotheek sluit om achttien uur", "feit"),
                          ("de bibliotheek zou langer open moeten", "mening"),
                          ("er kwamen vorig jaar 4 000 leden bij", "feit")], "Feit of mening?", W),
                 ("rij", [("dit is de beste beslissing van het jaar", "mening"),
                          ("de maatregel geldt vanaf september", "feit"),
                          ("jongeren lezen veel te weinig", "mening")], "Feit of mening?", W),
             ]),
        dict(kop="Ontleed het betoog",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("tekst", "<em>Onze school moet de middagpauze verlengen. Leerlingen eten nu in "
                           "twintig minuten, wat volgens een studie bij 1 200 scholieren samenhangt "
                           "met meer maagklachten. Wie zegt dat een langere pauze de lessen verkort, "
                           "vergeet dat de laatste les nu toch half verloren gaat door de drukte. "
                           "Een langere pauze is dus geen tijdverlies maar tijdwinst.</em>"),
                 ("kort", "Wat is de stelling?", "de middagpauze moet verlengd worden", WL),
                 ("kort", "Welke soort argumentatie gebruikt de tweede zin?", "wetenschappelijk onderzoek", WW),
                 ("open", "Welk tegenargument wordt genoemd, en hoe wordt het weerlegd?",
                  "Het tegenargument is dat een langere pauze de lessen verkort. Het wordt weerlegd "
                  "door te zeggen dat de laatste les nu toch half verloren gaat door de drukte.", 4),
                 ("kort", "Welke zin is de conclusie?", "de laatste zin", W),
             ]),
        dict(kop="Welke drogreden?",
             opdracht="Noteer de naam van de drogreden.",
             oefeningen=[
                 ("rij", [("iedereen doet het, dus het kan geen kwaad", "beroep op de massa"),
                          ("jij hebt geen diploma, dus zwijg", "persoonlijke aanval"),
                          ("ofwel ben je voor, ofwel tegen ons", "vals dilemma")], "Welke drogreden?", WL),
                 ("rij", [("als we dit toelaten, is morgen alles verloren", "het hellend vlak"),
                          ("dat is altijd zo geweest", "beroep op traditie"),
                          ("het klopt, want het staat er", "cirkelredenering")], "Welke drogreden?", WL),
             ]),
        dict(kop="Vragen bij een onderzoek",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Noem drie vragen die je stelt bij een argument dat naar onderzoek verwijst.",
                  "Wie voerde het onderzoek uit, hoeveel mensen namen eraan deel, en wie heeft het "
                  "betaald.", 3),
                 ("open", "In een gemeente steeg zowel het aantal ooievaars als het aantal "
                          "geboorten. Wat besluit je, en waarom?",
                  "Dat er samenhang is maar geen bewezen oorzaak. Twee dingen die samen stijgen, "
                  "hoeven elkaar niet te veroorzaken; er kan een derde oorzaak achter zitten.", 4),
                 ("open", "Wat maakt een argument sterk? Noem de drie eisen.",
                  "Het is waar, het is ter zake, en het is belangrijk genoeg. Een argument dat waar "
                  "is maar niets met de stelling te maken heeft, telt niet mee.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Argumenteren met cijfers is altijd betrouwbaar.", False),
                 ("waar", "Een mening hoort niet in een tekst thuis.", False),
                 ("waar", "Zelf tegenargumenten noemen maakt een betoog sterker.", True),
                 ("waar", "De conclusie hoort te volgen uit de argumenten die eraan voorafgaan.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-literaire-begrippen-en-genres-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Literaire begrippen en genres",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke hoofdgroep?",
             opdracht="Noteer epiek, lyriek of dramatiek.",
             oefeningen=[
                 ("rij", [("een novelle", "epiek"), ("een sonnet", "lyriek"),
                          ("een klucht", "dramatiek"), ("een kortverhaal", "epiek"),
                          ("een ode", "lyriek"), ("een tragedie", "dramatiek")], "Welke hoofdgroep?", W),
             ]),
        dict(kop="Welk genre?",
             opdracht="Noteer de naam van het genre.",
             oefeningen=[
                 ("rij", [("dieren treden op en er zit een les in", "de fabel"),
                          ("een alledaags beeld legt een geestelijke waarheid uit", "de parabel"),
                          ("een levenswijsheid in één of twee zinnen", "het aforisme")], "Welk genre?", WL),
                 ("rij", [("een lang verhalend gedicht over een held", "het epos"),
                          ("een verhaal in een verhaal", "de raamvertelling"),
                          ("alles in het verhaal staat voor iets anders", "de allegorie")], "Welk genre?", WL),
                 ("rij", [("een roman die volledig uit brieven bestaat", "de briefroman"),
                          ("echte personen achter verzonnen personages", "de sleutelroman"),
                          ("een roman over het opgroeien van een personage", "de Bildungsroman")],
                  "Welk genre?", WL),
             ]),
        dict(kop="Humor uit elkaar houden",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen ironie en sarcasme?",
                  "Ironie is het tegenovergestelde zeggen van wat je bedoelt. Sarcasme is ironie die "
                  "bijt: ze is bedoeld om iemand te raken.", 3),
                 ("open", "Wat is het verschil tussen een parodie en een satire?",
                  "Een parodie imiteert een stijl om er de draak mee te steken; ze mikt op de vorm. "
                  "Een satire hekelt een misstand; ze mikt op de wereld.", 3),
                 ("kort", "Hoe noem je humor waarin met iets pijnlijks gelachen wordt?", "zwarte humor", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een novelle is langer dan een roman.", False),
                 ("waar", "Literaire non-fictie is een tegenspraak.", False),
                 ("waar", "Een historische roman moet in alle details historisch kloppen.", False),
                 ("waar", "Eén roman kan tot meerdere genres tegelijk gerekend worden.", True),
                 ("waar", "Een stadssage wordt verteld alsof het echt gebeurd is.", True),
             ]),
        dict(kop="In eigen woorden",
             opdracht="Schrijf telkens enkele zinnen.",
             oefeningen=[
                 ("open", "Wat bedoelt men met de gelaagdheid van een tekst? Geef een voorbeeld van "
                          "hoe dat kan werken.",
                  "Dat er verschillende betekenislagen in zitten: je kan hem op meer dan één manier "
                  "lezen. Een verhaal over een lange tocht kan tegelijk gaan over een reis en over "
                  "het ouder worden van het hoofdpersonage.", 5),
                 ("open", "Waarom loont het om de juiste literaire term te gebruiken als je over een "
                          "boek praat?",
                  "Je zegt in één woord wat anders een alinea kost, en de ander weet meteen precies "
                  "wat je bedoelt.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-verhaalkenmerken-en-vertelperspectief-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Verhaalkenmerken en vertelperspectief",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Begrippen koppelen",
             opdracht="Noteer het begrip dat bij de omschrijving hoort.",
             oefeningen=[
                 ("rij", [("het personage dat de hoofdpersoon tegenwerkt", "de antagonist"),
                          ("een hoofdpersoon zonder heldhaftige eigenschappen", "de antiheld"),
                          ("een personage dat samenvalt met één eigenschap", "een type")],
                  "Welk begrip?", WL),
                 ("rij", [("een sprong naar iets dat eerder gebeurde", "een flashback"),
                          ("het hoogtepunt van de spanning", "de climax"),
                          ("de onverwachte wending op het einde", "de pointe")], "Welk begrip?", WL),
                 ("rij", [("een citaat vooraan in het boek", "het motto"),
                          ("iets concreets dat voor iets abstracts staat", "een symbool"),
                          ("iets dat door het hele verhaal terugkeert", "een motief")], "Welk begrip?", WL),
             ]),
        dict(kop="Welk vertelperspectief?",
             opdracht="Noteer het perspectief.",
             oefeningen=[
                 ("rij", [("de verteller weet alles en geeft commentaar", "auctorieel"),
                          ("je kijkt mee over de schouder van één personage", "personaal"),
                          ("de ik verzwijgt en verdraait dingen", "onbetrouwbaar")], "Welk perspectief?", WL),
                 ("open", "Wat is het verschil tussen een belevende en een vertellende ik-verteller?",
                  "De belevende ik staat middenin de gebeurtenissen en weet nog niet hoe het afloopt. "
                  "De vertellende ik kijkt terug en weet dat wel.", 3),
             ]),
        dict(kop="Tijd in het verhaal",
             opdracht="Beantwoord kort of in volledige zinnen.",
             oefeningen=[
                 ("kort", "Een hoofdstuk vat twintig jaar samen in één bladzijde. Hoe heet dat?",
                  "versnelling", W),
                 ("kort", "De verteltijd is veel langer dan de vertelde tijd. Hoe heet dat?",
                  "vertraging", W),
                 ("open", "Leg het verschil uit tussen vertelde tijd en verteltijd.",
                  "De vertelde tijd is de duur die het verhaal beslaat, bijvoorbeeld dertig jaar. De "
                  "verteltijd is de leestijd, dus de ruimte die de verteller eraan geeft.", 3),
                 ("kort", "Hoe noem je het beginnen middenin de gebeurtenissen?", "in medias res", WW),
             ]),
        dict(kop="Ruimte lezen",
             opdracht="Schrijf telkens enkele zinnen.",
             oefeningen=[
                 ("open", "Een roman speelt in een grauwe mijnstreek met eeuwig regenweer. Welke "
                          "functie heeft die ruimte, en wat zegt ze over de personages?",
                  "Ze is vooral sfeerscheppend: het weer en het landschap zetten de toon van "
                  "uitzichtloosheid. Ze zegt daarmee ook iets over de personages, die in diezelfde "
                  "beklemming leven.", 4),
                 ("open", "Noem de vier soorten ruimte en geef bij elk een voorbeeld van één regel.",
                  "Geografisch: de stad Gent. Sociaal: een villawijk tegenover een sociale woonblok. "
                  "Symbolisch: een gesloten kamer zonder ramen als beeld van benauwdheid. "
                  "Sfeerscheppend: een mistige haven bij nacht.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een vlak personage kan het hoofdpersonage zijn.", True),
                 ("waar", "Een ik-verteller weet altijd wat anderen denken.", False),
                 ("waar", "Een verhaal dat niet chronologisch verteld wordt, is slecht opgebouwd.", False),
                 ("waar", "Intertekstualiteit betekent dat een tekst naar een andere tekst verwijst.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-poezie-dichtvormen-strofen-en-rijm-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Poëzie: dichtvormen, strofen en rijm",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Hoeveel verzen?",
             opdracht="Noteer het aantal verzen.",
             oefeningen=[
                 ("rij", [("een sonnet", "veertien"), ("een haiku", "drie"),
                          ("een limerick", "vijf"), ("een distichon", "twee"),
                          ("een kwatrijn", "vier"), ("een octaaf", "acht")], "Hoeveel verzen?", W),
             ]),
        dict(kop="Welke vorm?",
             opdracht="Noteer de naam van de dichtvorm.",
             oefeningen=[
                 ("rij", [("een klaagzang om een verlies", "een elegie"),
                          ("een lofzang", "een ode"),
                          ("een verhalend gedicht met een refrein", "een ballade")], "Welke vorm?", WL),
                 ("rij", [("de eerste letters vormen samen een woord", "een acrostichon"),
                          ("bepaalde verzen keren letterlijk terug", "een rondeel"),
                          ("de vorm op de bladzijde speelt mee", "visuele poëzie")], "Welke vorm?", WL),
             ]),
        dict(kop="Rijm",
             opdracht="Noteer het rijmschema of de rijmsoort.",
             oefeningen=[
                 ("rij", [("aabb", "gepaard rijm"), ("abba", "omarmend rijm"),
                          ("abab", "gekruist rijm")], "Hoe heet dat schema?", WW),
                 ("rij", [("enkel de klinkers komen overeen", "assonantie"),
                          ("dezelfde beginklank bij opeenvolgende woorden", "alliteratie"),
                          ("klinker én medeklinkers komen overeen", "volrijm")], "Welke rijmsoort?", WW),
                 ("kort", "Hoe noem je alliteratie met één ander woord?", "stafrijm", W),
             ]),
        dict(kop="Vorm en klank bekijken",
             opdracht="Lees het fragment en antwoord. Het is een zelf geschreven voorbeeld.",
             oefeningen=[
                 ("tekst", "<em>de wind<br>draagt wat de bomen<br>niet meer houden</em>"),
                 ("open", "Wat valt op aan de vorm van deze drie regels?",
                  "De zin loopt over de versgrenzen heen. Dat heet een enjambement: de regel breekt "
                  "af terwijl de zin doorgaat.", 3),
                 ("open", "Een dichter zet één woord alleen op een regel, met veel wit eromheen. Wat "
                          "bereikt zij daarmee?",
                  "Het woord krijgt alle aandacht. Het wit dwingt de lezer te vertragen, en wat "
                  "alleen staat, weegt zwaarder.", 3),
                 ("kort", "Hoe noem je de wending in de gedachtegang van een sonnet?", "de volta", W),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het lyrisch subject is altijd de dichter zelf.", False),
                 ("waar", "Een gedicht zonder rijm en zonder vaste maat bestaat niet.", False),
                 ("waar", "Parlandopoëzie klinkt alsof iemand gewoon aan het praten is.", True),
                 ("waar", "Bij mannelijk rijm ligt de klemtoon op de laatste lettergreep.", True),
             ]),
        dict(kop="Zelf doen",
             opdracht="Schrijf in je eigen woorden.",
             oefeningen=[
                 ("open", "Waarom is het nuttig een gedicht hardop te lezen?",
                  "Klank en ritme komen pas dan tot hun recht. Alliteratie, assonantie en het "
                  "verschil tussen sterke en zwakke lettergrepen hoor je niet met je ogen.", 3),
                 ("open", "Schrijf zelf twee regels met alliteratie over de regen, en onderstreep de "
                          "herhaalde beginklank.",
                  "Een eigen antwoord. Voorbeeld: de regen rolt en ratelt op de ruiten, roffelt op "
                  "het rode dak. De herhaalde beginklank is de r.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-dramatiek-en-theatertekens-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Dramatiek en theatertekens",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke toneelvorm?",
             opdracht="Noteer de naam van de vorm.",
             oefeningen=[
                 ("rij", [("de hoofdfiguur gaat onafwendbaar ten onder", "de tragedie"),
                          ("een grof komisch stuk vol misverstanden", "de klucht"),
                          ("een stuk dat een zedenles uitbeeldt", "de moraliteit")], "Welke vorm?", WL),
                 ("rij", [("een heilige verricht een wonder", "het mirakelspel"),
                          ("een ernstig wereldlijk stuk uit de middeleeuwen", "het abel spel"),
                          ("vaste typen, maskers en veel improvisatie", "de commedia dell'arte")],
                  "Welke vorm?", WL),
                 ("rij", [("de wereld op het toneel heeft geen zinvolle logica", "het absurd theater"),
                          ("het publiek moet afstand houden en nadenken", "het episch theater"),
                          ("zang, dans en tekst dragen samen het verhaal", "de musical")], "Welke vorm?", WL),
             ]),
        dict(kop="Welk theaterteken?",
             opdracht="Noteer het theaterteken.",
             oefeningen=[
                 ("rij", [("de uitdrukking op het gezicht", "mimiek"),
                          ("de gebaren die een speler maakt", "gestiek"),
                          ("de afstand tussen de spelers", "proxemiek")], "Welk teken?", WW),
                 ("rij", [("een versleten koffer die een speler vasthoudt", "een rekwisiet"),
                          ("alles aan de stem behalve de woorden", "paraverbale tekens"),
                          ("een schijnwerper die één speler uitlicht", "de belichting")], "Welk teken?", WW),
             ]),
        dict(kop="Wat zegt de scène?",
             opdracht="Schrijf telkens enkele zinnen.",
             oefeningen=[
                 ("open", "Twee personages staan het hele stuk aan weerszijden van de scène en komen "
                          "nooit dichterbij. Wat zegt dat, en welk theaterteken is het?",
                  "De afstand tussen hen wordt zichtbaar gemaakt: hun vervreemding wordt in de ruimte "
                  "getoond in plaats van uitgesproken. Het theaterteken is de proxemiek.", 4),
                 ("open", "Een regisseur zet een klassiek stuk in een hedendaags kantoor. Wat doet "
                          "die ingreep, en hoe zou je ze beoordelen?",
                  "Ze legt een verband tussen toen en nu: de toeschouwer herkent het machtsspel in "
                  "zijn eigen wereld. Je beoordeelt ze door te kijken of de keuzes op scène de tekst "
                  "versterken of juist tegenspreken.", 4),
                 ("open", "Waarom is een toneeltekst nooit helemaal af op papier?",
                  "De opvoering voegt een hele laag tekens toe: stem, lichaam, decor, licht, geluid "
                  "en kostuum. Die laag staat niet in de tekst maar bepaalt wel wat de toeschouwer "
                  "ziet.", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het mysteriespel had een religieus onderwerp.", True),
                 ("waar", "Episch theater wil dat het publiek zich volledig inleeft.", False),
                 ("waar", "Sombere muziek onder een scène is geen theaterteken.", False),
                 ("waar", "Een polyloog is een gesprek tussen meer dan twee personages.", True),
                 ("waar", "Een toneeltekst lezen is hetzelfde als een opvoering analyseren.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-stijlfiguren-en-beeldspraak-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Stijlfiguren en beeldspraak",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke stijlfiguur?",
             opdracht="Noteer de naam. De voorbeeldzinnen zijn zelf geschreven.",
             oefeningen=[
                 ("rij", [("zijn woorden waren messen", "een metafoor"),
                          ("zij is zo stil als een steen", "een vergelijking"),
                          ("de wind fluisterde door de bomen", "een personificatie")],
                  "Welke stijlfiguur?", WL),
                 ("rij", [("het schreeuwende geel van de muren", "synesthesie"),
                          ("ik sterf van de honger", "een hyperbool"),
                          ("dat is niet slecht, voor uitstekend", "een litotes")], "Welke stijlfiguur?", WL),
                 ("rij", [("wij geloven, wij bouwen, wij blijven", "een anafoor"),
                          ("veel lawaai, weinig muziek", "een antithese"),
                          ("wie kan daar nu tegen zijn?", "een retorische vraag")], "Welke stijlfiguur?", WL),
             ]),
        dict(kop="Vergroten of verkleinen?",
             opdracht="Noteer of de stijlfiguur vergroot of verzwakt wat er bedoeld wordt.",
             oefeningen=[
                 ("rij", [("hyperbool", "vergroot"), ("litotes", "verzwakt"),
                          ("understatement", "verzwakt"), ("eufemisme", "verzwakt")],
                  "Vergroot of verzwakt?", WW),
             ]),
        dict(kop="In eigen woorden",
             opdracht="Schrijf telkens enkele zinnen.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen een vergelijking en een metafoor? Geef van "
                          "elk een zelf bedacht voorbeeld.",
                  "In een vergelijking staat een woordje als zoals of als; in een metafoor vervangt "
                  "het beeld de zaak. Bijvoorbeeld: hij rende als een haas (vergelijking) tegenover "
                  "hij was een haas op dat veld (metafoor).", 5),
                 ("open", "Waarom gebruikt een schrijver beeldspraak?",
                  "Een beeld maakt iets abstracts voelbaar: je ziet het voor je in plaats van het "
                  "enkel te begrijpen.", 3),
                 ("open", "Wat is het effect van een cliché in een tekst?",
                  "De zin leest vlot maar raakt niemand: het beeld is door veelvuldig gebruik zijn "
                  "kracht kwijt.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Beeldspraak komt enkel in poëzie voor.", False),
                 ("waar", "Stijlfiguren komen enkel in literaire teksten voor.", False),
                 ("waar", "Een paradox spreekt zichzelf tegen maar bevat toch een waarheid.", True),
                 ("waar", "Bij een parallellisme volgen twee zinnen hetzelfde bouwpatroon.", True),
                 ("waar", "Antropomorfisme betekent dat een mens eigenschappen van een dier krijgt.", False),
             ]),
        dict(kop="Zelf schrijven",
             opdracht="Schrijf je eigen zinnen.",
             oefeningen=[
                 ("open", "Schrijf één zin over een storm met een personificatie erin.",
                  "Een eigen antwoord. Voorbeeld: de storm beukte de hele nacht kwaad op de luiken.", 3),
                 ("open", "Schrijf een slogan voor een sportclub met een anafoor erin.",
                  "Een eigen antwoord. Voorbeeld: samen trainen, samen vallen, samen winnen.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-literaire-stromingen-van-de-middeleeuwen-tot-nu-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Literaire stromingen van de middeleeuwen tot nu",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke stroming?",
             opdracht="Noteer de naam van de stroming.",
             oefeningen=[
                 ("rij", [("de verheven liefde voor een onbereikbare vrouw", "de hoofse literatuur"),
                          ("teruggrijpen naar de klassieke oudheid", "de renaissance"),
                          ("overvloed, beweging en vergankelijkheid", "de barok")], "Welke stroming?", WL),
                 ("rij", [("de rede, de wetenschap en het eigen oordeel", "de verlichting"),
                          ("gevoel, verbeelding en verlangen naar het verre", "de romantiek"),
                          ("de werkelijkheid weergeven zoals ze is", "het realisme")], "Welke stroming?", WL),
                 ("rij", [("afkomst en omgeving bepalen het lot", "het naturalisme"),
                          ("de werkelijkheid vervormen om gevoel uit te drukken", "het expressionisme"),
                          ("de mens moet zijn eigen betekenis maken", "het existentialisme")],
                  "Welke stroming?", WL),
                 ("rij", [("het wonderlijke dringt de gewone wereld binnen", "het magisch-realisme"),
                          ("twijfel aan één grote waarheid", "het postmodernisme"),
                          ("associatie en experiment met taal en vorm", "de Vijftigers")],
                  "Welke stroming?", WL),
             ]),
        dict(kop="Plaats in de tijd",
             opdracht="Zet de stromingen in de juiste volgorde, van oud naar jong.",
             oefeningen=[
                 ("open", "Romantiek, renaissance, postmodernisme, naturalisme, verlichting.",
                  "Renaissance, verlichting, romantiek, naturalisme, postmodernisme.", 3),
             ]),
        dict(kop="Herken de stroming",
             opdracht="Schrijf telkens de stroming én de reden.",
             oefeningen=[
                 ("open", "Een roman over een arbeidersgezin dat ondanks alle pogingen niet uit de "
                          "armoede raakt, met veel aandacht voor ziekte en drank.",
                  "Het naturalisme: erfelijkheid en milieu sturen het verhaal, de hoofdfiguur is zwak, "
                  "en taboeonderwerpen worden niet vermeden.", 4),
                 ("open", "Een roman waarin de verteller halverwege zegt dat hij het verhaal zelf "
                          "verzint.",
                  "Het postmodernisme: de illusie van het verhaal wordt doorbroken en er klinkt "
                  "twijfel aan één grote waarheid.", 4),
                 ("open", "Een gedicht vol ongewone woordcombinaties, zonder hoofdletters en met "
                          "gebroken zinsbouw.",
                  "De Vijftigers: associatie en experiment met taal en vorm staan voorop.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een stroming begint en eindigt op een scherp af te lijnen jaartal.", False),
                 ("waar", "Realisme en naturalisme zijn precies hetzelfde.", False),
                 ("waar", "Avant-garde is een verzamelnaam voor stromingen die met de traditie breken.", True),
                 ("waar", "Het neorealisme keert zich af van het alledaagse.", False),
                 ("waar", "Een schrijver kan kenmerken van meerdere stromingen tegelijk gebruiken.", True),
             ]),
        dict(kop="Waarom dit kennen?",
             opdracht="Schrijf enkele zinnen.",
             oefeningen=[
                 ("open", "Waarom is het nuttig om de kenmerken van een stroming te kennen?",
                  "Je plaatst een tekst dan in zijn eigen tijd: je begrijpt waarom hij doet wat hij "
                  "doet, en waartegen hij zich afzet.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-taalvarieteiten-registers-en-beleefdheid-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Taalvariëteiten, registers en beleefdheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke variëteit?",
             opdracht="Noteer regionaal, sociaal of situationeel.",
             oefeningen=[
                 ("rij", [("een West-Vlaams dialect", "regionaal"),
                          ("jongerentaal", "sociaal"),
                          ("ambtelijke taal", "situationeel")], "Welke soort?", WW),
                 ("rij", [("de taal van een sportcommentator", "situationeel"),
                          ("medisch vakjargon", "sociaal"),
                          ("het Limburgse dialect", "regionaal")], "Welke soort?", WW),
             ]),
        dict(kop="Formeel of informeel?",
             opdracht="Noteer het register dat past.",
             oefeningen=[
                 ("rij", [("een sollicitatiebrief", "formeel"),
                          ("een appje aan je zus", "informeel"),
                          ("een klacht bij een officiële instantie", "formeel")], "Welk register?", W),
                 ("rij", [("een mail aan de schooldirectie", "formeel"),
                          ("een praatje op een feestje", "informeel"),
                          ("een brief aan een verzekeraar", "formeel")], "Welk register?", W),
             ]),
        dict(kop="Herschrijven",
             opdracht="Schrijf de zin om naar het gevraagde register.",
             oefeningen=[
                 ("open", "Informeel: 'Hey, kan je ff laten weten of da nog doorgaat?' Herschrijf "
                          "formeel, aan een onbekende dienst.",
                  "Bijvoorbeeld: Geachte mevrouw, meneer, graag had ik vernomen of de activiteit "
                  "doorgaat. Alvast bedankt voor uw antwoord. Met vriendelijke groeten, gevolgd door "
                  "je naam.", 5),
                 ("open", "Noem drie keuzes die een tekst formeler maken.",
                  "U gebruiken in plaats van je, volledige zinnen schrijven, en afkortingen "
                  "vermijden.", 3),
             ]),
        dict(kop="Beoordeel de situatie",
             opdracht="Schrijf telkens enkele zinnen.",
             oefeningen=[
                 ("open", "Een arts schrijft een brief vol medische termen aan een patiënt. Wat is "
                          "het effect, en hoe heet het verschijnsel?",
                  "De patiënt haakt af en voelt zich buitengesloten. Het jargon werkt hier als een "
                  "variëteit die uitsluit, en voor de lezer ook als ruis.", 4),
                 ("open", "Een leerling begint een mail aan een leerkracht met 'Hey'. Wat is het "
                          "effect?",
                  "De aanspreking botst met de verhouding: ze is informeler dan de situatie toelaat, "
                  "en de ontvanger leest dat als slordig of te familiair.", 3),
                 ("open", "Waarom gebruikt een juridische tekst vaak moeilijke, vaste formuleringen?",
                  "Omdat precisie er zwaarder weegt dan leesbaarheid: een vaste formulering betekent "
                  "altijd exact hetzelfde, ook voor een rechter.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Wie standaardtaal spreekt, drukt zich altijd duidelijker uit.", False),
                 ("waar", "Beleefdheidsconventies zijn overal ter wereld dezelfde.", False),
                 ("waar", "Eén spreker kan verschillende variëteiten beheersen en afwisselen.", True),
                 ("waar", "Weet je het niet zeker, dan kies je het meest formele register.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-taal-en-identiteit-stereotypering-inclusie-en-non-verbale-communicatie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Taal en identiteit: stereotypering, inclusie en non-verbale communicatie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Insluiten of uitsluiten?",
             opdracht="Noteer of de taal in deze situatie insluit of uitsluit.",
             oefeningen=[
                 ("rij", [("twee collega's spreken dialect bij een nieuwe medewerker", "uitsluiten"),
                          ("een gemeente herschrijft haar brieven eenvoudiger", "insluiten"),
                          ("genderneutrale taal in een vacature", "insluiten")], "Wat gebeurt er?", WW),
                 ("rij", [("elitair taalgebruik in een openbaar debat", "uitsluiten"),
                          ("vakjargon tegen een buitenstaander", "uitsluiten"),
                          ("een vereniging die haar afkortingen uitlegt", "insluiten")],
                  "Wat gebeurt er?", WW),
             ]),
        dict(kop="Stereotypering",
             opdracht="Schrijf telkens enkele zinnen.",
             oefeningen=[
                 ("open", "Waarop zijn stereotypes gebaseerd, en waarom kloppen ze meestal niet?",
                  "Op versimpeling, overdrijving en veralgemening. Ze gelden hooguit voor sommigen "
                  "en worden op iedereen van een groep geplakt.", 4),
                 ("open", "Een personage in een sitcom spreekt met een zwaar accent en wordt als dom "
                          "neergezet. Wat gebeurt hier, en waarom is dat een probleem?",
                  "Taal wordt gekoppeld aan een karaktereigenschap. Het probleem is dat kijkers die "
                  "koppeling meenemen naar echte mensen met datzelfde accent.", 4),
                 ("open", "Je merkt dat je iemand op zijn accent beoordeelde. Wat doe je?",
                  "Je stelt je oordeel bij op wat hij zegt in plaats van op hoe hij klinkt.", 3),
             ]),
        dict(kop="Non-verbaal of paraverbaal?",
             opdracht="Noteer welke van de twee het is.",
             oefeningen=[
                 ("rij", [("oogcontact", "non-verbaal"), ("intonatie", "paraverbaal"),
                          ("kleding", "non-verbaal"), ("spreektempo", "paraverbaal"),
                          ("mimiek", "non-verbaal"), ("volume", "paraverbaal")], "Welke soort?", W),
             ]),
        dict(kop="Lezen wat er niet gezegd wordt",
             opdracht="Schrijf telkens enkele zinnen.",
             oefeningen=[
                 ("open", "Iemand zegt 'alles is in orde' met een gespannen stem en een afgewende "
                          "blik. Wat doe je met die boodschap?",
                  "Je weegt de woorden tegen de signalen af. De paraverbale en non-verbale signalen "
                  "spreken de woorden tegen, dus je vraagt door in plaats van het antwoord aan te "
                  "nemen.", 4),
                 ("open", "Waarom wordt ironie in een appje vaker verkeerd begrepen dan in een "
                          "gesprek?",
                  "De toon en het gezicht ontbreken. In een gesprek verraadt de intonatie dat je het "
                  "omgekeerde bedoelt; in geschreven taal moet een emoji of een woord dat werk doen.", 3),
                 ("open", "Noem drie signalen van een open, uitnodigende houding.",
                  "Oogcontact maken, de armen niet gekruist houden, en je naar de spreker toe "
                  "draaien.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een stereotype is een nuttige samenvatting en meestal correct.", False),
                 ("waar", "Woorden in hoofdletters typen wordt als schreeuwen opgevat.", True),
                 ("waar", "Non-verbale communicatie speelt enkel in gesproken gesprekken.", False),
                 ("waar", "Je kleding draagt niets bij aan je boodschap.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-klanken-spelling-diakritische-tekens-en-interpunctie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Klanken, spelling, diakritische tekens en interpunctie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Werkwoordspelling",
             opdracht="Schrijf de juiste vorm.",
             oefeningen=[
                 ("rij", [("hij (antwoorden, tt)", "antwoordt"), ("ik (verwachten, tt)", "verwacht"),
                          ("hij (worden, tt)", "wordt")], "Schrijf de vorm.", WW),
                 ("rij", [("hij heeft het (verbranden)", "verbrand"),
                          ("het is (gebeuren)", "gebeurd"),
                          ("zij heeft (antwoorden)", "geantwoord")], "Schrijf het deelwoord.", WW),
                 ("rij", [("de stam van reizen", "reis"), ("de stam van antwoorden", "antwoord"),
                          ("de verleden tijd van werken", "werkte")], "Vul aan.", WW),
             ]),
        dict(kop="Hoofdletter of niet?",
             opdracht="Noteer het woord met de juiste schrijfwijze.",
             oefeningen=[
                 ("rij", [("de taal van Frankrijk", "Frans"), ("de maand na november", "december"),
                          ("de taal van Duitsland", "Duits"), ("de dag na maandag", "dinsdag")],
                  "Schrijf het woord.", WW),
             ]),
        dict(kop="Welk teken?",
             opdracht="Noteer de naam van het diakritische teken of het leesteken.",
             oefeningen=[
                 ("rij", [("boven de i in ruïne", "een trema"), ("in zo'n", "een apostrof"),
                          ("in Noord-Frankrijk", "een koppelteken")], "Welk teken?", WW),
                 ("rij", [("kondigt een opsomming aan", "de dubbele punt"),
                          ("staat rond iemands letterlijke woorden", "de aanhalingstekens"),
                          ("sluit een mededelende zin af", "de punt")], "Welk teken?", WW),
             ]),
        dict(kop="Verbeter",
             opdracht="Schrijf de zin correct over.",
             oefeningen=[
                 ("open", "hij word morgen Twintig, en hij heeft dat zelf nog niet eens door",
                  "Hij wordt morgen twintig, en hij heeft dat zelf nog niet eens door.", 3),
                 ("open", "toen de bel ging zweeg iedereen want de les begon",
                  "Toen de bel ging, zweeg iedereen, want de les begon.", 3),
                 ("open", "ik heb drie autos gezien 's Morgens vroeg",
                  "Ik heb 's morgens vroeg drie auto's gezien.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De spelling van een woord volgt altijd precies de uitspraak.", False),
                 ("waar", "De spatie telt mee als interpunctieteken.", True),
                 ("waar", "Namen van maanden krijgen een hoofdletter.", False),
                 ("waar", "Leestekens bepalen mee de betekenis van een zin.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-woordsoorten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Woordsoorten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke woordsoort?",
             opdracht="Noteer de woordsoort van het vetgedrukte woord.",
             oefeningen=[
                 ("rij", [("de <b>tafel</b> staat scheef", "zelfstandig naamwoord"),
                          ("de <b>snelle</b> trein", "bijvoeglijk naamwoord"),
                          ("de kat zit <b>onder</b> de tafel", "voorzetsel")], "Welke soort?", WL),
                 ("rij", [("we vertrekken <b>morgen</b>", "bijwoord"),
                          ("brood <b>en</b> kaas", "voegwoord"),
                          ("<b>au</b>, dat doet pijn", "tussenwerpsel")], "Welke soort?", WL),
                 ("rij", [("<b>drie</b> boeken", "telwoord"),
                          ("het is <b>erg</b> koud", "bijwoord"),
                          ("de deur <b>van</b> het huis", "voorzetsel")], "Welke soort?", WL),
             ]),
        dict(kop="Welk voornaamwoord?",
             opdracht="Noteer het soort voornaamwoord.",
             oefeningen=[
                 ("rij", [("dat is <b>mijn</b> jas", "bezittelijk"),
                          ("hij wast <b>zich</b>", "wederkerig"),
                          ("de man <b>die</b> daar staat", "betrekkelijk")], "Welk soort?", WW),
                 ("rij", [("hij ziet <b>mij</b>", "persoonlijk"),
                          ("<b>welk</b> boek lees je?", "vragend"),
                          ("<b>deze</b> staat hier al jaren", "aanwijzend")], "Welk soort?", WW),
             ]),
        dict(kop="Welk soort werkwoord?",
             opdracht="Noteer zelfstandig, hulp- of koppelwerkwoord.",
             oefeningen=[
                 ("rij", [("hij <b>is</b> leraar", "koppelwerkwoord"),
                          ("hij <b>heeft</b> gelopen", "hulpwerkwoord"),
                          ("zij <b>schrijft</b> een brief", "zelfstandig werkwoord")],
                  "Welk soort?", WL),
                 ("rij", [("het <b>wordt</b> koud", "koppelwerkwoord"),
                          ("hij <b>blijft</b> rustig", "koppelwerkwoord"),
                          ("zij <b>zal</b> komen", "hulpwerkwoord")], "Welk soort?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een lidwoord kan voor een werkwoord staan.", False),
                 ("waar", "Een bijvoeglijk naamwoord kan achter het zelfstandig naamwoord staan.", True),
                 ("waar", "Het woord 'het' is altijd een lidwoord.", False),
                 ("waar", "Een hulpwerkwoord kan alleen in een zin staan.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf enkele zinnen.",
             oefeningen=[
                 ("open", "Hoe bepaal je van welke woordsoort een woord is? Waarom kan je dat niet "
                          "zomaar uit het woordenboek halen?",
                  "Je kijkt naar de rol die het woord in díe zin speelt. Hetzelfde woord kan in de "
                  "ene zin een lidwoord zijn en in de andere een voornaamwoord, dus de zin beslist.", 4),
                 ("open", "Waarom is het belangrijk te weten of een werkwoord een koppelwerkwoord is?",
                  "Het bepaalt of er een naamwoordelijk gezegde is, en dus hoe je de zin ontleedt.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-morfologie-samenstellingen-afleidingen-en-werkwoordstijden-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Morfologie: samenstellingen, afleidingen en werkwoordstijden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Samenstelling of afleiding?",
             opdracht="Noteer wat het woord is.",
             oefeningen=[
                 ("rij", [("boekenkast", "samenstelling"), ("vriendelijk", "afleiding"),
                          ("onmogelijk", "afleiding"), ("pannenkoek", "samenstelling"),
                          ("werker", "afleiding"), ("zonnebloem", "samenstelling")],
                  "Wat is het?", WW),
             ]),
        dict(kop="Ontleed het woord",
             opdracht="Splits het woord in zijn delen en noteer wat elk deel doet.",
             oefeningen=[
                 ("open", "onbereikbaarheid",
                  "on + bereik + baar + heid. On- is een voorvoegsel dat de betekenis omkeert, "
                  "bereik is het grondwoord, -baar maakt er een bijvoeglijk naamwoord van, en -heid "
                  "maakt daar weer een zelfstandig naamwoord van.", 4),
                 ("open", "onvriendelijkheid",
                  "on + vriend + elijk + heid. Het woord bevat dus zowel een voorvoegsel als een "
                  "achtervoegsel.", 3),
             ]),
        dict(kop="Meervoud en verkleinwoord",
             opdracht="Schrijf de gevraagde vorm.",
             oefeningen=[
                 ("rij", [("meervoud van kind", "kinderen"), ("meervoud van auto", "auto's"),
                          ("verkleinwoord van koning", "koninkje")], "Schrijf de vorm.", WW),
                 ("rij", [("meervoud van ei", "eieren"), ("verkleinwoord van bloem", "bloempje"),
                          ("verkleinwoord van huis", "huisje")], "Schrijf de vorm.", WW),
             ]),
        dict(kop="Welke werkwoordstijd?",
             opdracht="Noteer de tijd.",
             oefeningen=[
                 ("rij", [("hij had gewerkt", "voltooid verleden tijd"),
                          ("hij heeft gewerkt", "voltooid tegenwoordige tijd"),
                          ("hij zal komen", "onvoltooid toekomende tijd")], "Welke tijd?", WL),
                 ("rij", [("zij liepen naar huis", "onvoltooid verleden tijd"),
                          ("hij werkt in de tuin", "onvoltooid tegenwoordige tijd"),
                          ("loop!", "gebiedende wijs")], "Welke tijd of wijs?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Verbuiging slaat op werkwoorden en vervoeging op naamwoorden.", False),
                 ("waar", "Het werkwoord 'zijn' wordt volgens de gewone regels vervoegd.", False),
                 ("waar", "Een scheidbaar werkwoord valt in sommige zinnen uiteen.", True),
                 ("waar", "Elk Nederlands meervoud wordt met -en of -s gevormd.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf enkele zinnen.",
             oefeningen=[
                 ("open", "Wat is een sterk werkwoord, en hoe weet je of een zwak werkwoord -te of "
                          "-de krijgt?",
                  "Een sterk werkwoord verandert in de verleden tijd van klinker, zoals lopen en "
                  "liep. Bij een zwak werkwoord kijk je naar de laatste klank van de stam om te "
                  "weten of het -te of -de wordt.", 4),
                 ("open", "Waarom variëren goede schrijvers met werkwoordstijden?",
                  "De tijd stuurt hoe de lezer de gebeurtenis plaatst: wat nu bezig is, wat afgelopen "
                  "is en wat nog komt.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-zinsontleding-en-zinsbouw-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Zinsontleding en zinsbouw",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Ontleed de zin",
             opdracht="Noteer het gevraagde zinsdeel.",
             oefeningen=[
                 ("rij", [("De leraar gaf de leerlingen gisteren een toets. (onderwerp)", "de leraar"),
                          ("Hij geeft zijn zus een boek. (lijdend voorwerp)", "een boek"),
                          ("Aan mijn zus heb ik een brief geschreven. (meewerkend voorwerp)", "aan mijn zus")],
                  "Welk zinsdeel?", WL),
                 ("rij", [("De brief werd door de postbode bezorgd. (handelend voorwerp)", "door de postbode"),
                          ("Gisteren las ik een boek. (bijwoordelijke bepaling)", "gisteren"),
                          ("Zij schreef een lange mail. (persoonsvorm)", "schreef")], "Welk zinsdeel?", WL),
             ]),
        dict(kop="Welke vraag?",
             opdracht="Noteer de vraag waarmee je het zinsdeel vindt.",
             oefeningen=[
                 ("rij", [("het onderwerp", "wie of wat plus de persoonsvorm"),
                          ("het meewerkend voorwerp", "aan wie of voor wie"),
                          ("de bijwoordelijke bepaling", "wanneer, waar of hoe")], "Welke vraag?", WL),
             ]),
        dict(kop="Enkelvoudig of samengesteld?",
             opdracht="Noteer wat de zin is, en bij samengestelde zinnen ook of het neven- of "
                      "onderschikking is.",
             oefeningen=[
                 ("rij", [("Hij komt en zij blijft.", "samengesteld, nevenschikking"),
                          ("Ik blijf thuis omdat het regent.", "samengesteld, onderschikking"),
                          ("De bus rijdt om acht uur.", "enkelvoudig")], "Wat is het?", WL),
             ]),
        dict(kop="Volgorde",
             opdracht="Schrijf telkens enkele zinnen.",
             oefeningen=[
                 ("open", "Wat is inversie? Geef een eigen voorbeeld met een vooropgeplaatste "
                          "bepaling.",
                  "Inversie is de omkering waarbij het onderwerp achter de persoonsvorm belandt. "
                  "Bijvoorbeeld: Na de pauze vertrok de hele groep. Zonder de bepaling vooraan zou "
                  "het zijn: De hele groep vertrok na de pauze.", 4),
                 ("open", "Wat is een tangconstructie, en waarom maakt een lange tangconstructie een "
                          "zin moeilijker?",
                  "Twee bij elkaar horende delen staan ver uit elkaar. De lezer moet het eerste deel "
                  "onthouden tot het tweede eindelijk komt, en dat kost werkgeheugen.", 4),
                 ("open", "Waarom is variatie in zinsbouw een beoordelingscriterium bij schrijven?",
                  "Afwisseling houdt een tekst levendig. Alleen maar korte zinnen klinken gehakt, "
                  "alleen maar lange zinnen vermoeien.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "In een Nederlandse bijzin staat de persoonsvorm meestal achteraan.", True),
                 ("waar", "Elke zin heeft verplicht een lijdend voorwerp.", False),
                 ("waar", "Het werkwoordelijk gezegde bestaat enkel uit de persoonsvorm.", False),
                 ("waar", "Een zinsdeel kan uit één woord bestaan.", True),
                 ("waar", "Een uitroepende zin eindigt met een vraagteken.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-semantiek-betekenisrelaties-gevoelswaarde-en-herkomst-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Semantiek: betekenisrelaties, gevoelswaarde en herkomst",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke betekenisrelatie?",
             opdracht="Noteer synoniemen, antoniemen, homoniemen, hyperoniem of hyponiem.",
             oefeningen=[
                 ("rij", [("warm en koud", "antoniemen"), ("beginnen en starten", "synoniemen"),
                          ("bank om op te zitten of geld te halen", "homoniemen")], "Welke relatie?", WW),
                 ("rij", [("meubel tegenover stoel", "hyperoniem"), ("appel onder fruit", "hyponiem"),
                          ("vroeg en laat", "antoniemen")], "Welke relatie?", WW),
             ]),
        dict(kop="Taalfouten",
             opdracht="Noteer de naam van de fout of het verschijnsel, en schrijf het correct.",
             oefeningen=[
                 ("rij", [("uitprinten", "contaminatie, printen"),
                          ("optelefoneren", "contaminatie, opbellen"),
                          ("duur kosten", "contaminatie, veel kosten")], "Wat is het?", WL),
                 ("open", "Wat is het verschil tussen een pleonasme en een tautologie? Geef van elk "
                          "een voorbeeld.",
                  "Een pleonasme voegt iets toe dat al in het woord zit, zoals een witte schimmel. "
                  "Een tautologie zegt hetzelfde twee keer met andere woorden, zoals nooit ofte "
                  "nimmer.", 4),
             ]),
        dict(kop="Denotatie en connotatie",
             opdracht="Schrijf telkens enkele zinnen.",
             oefeningen=[
                 ("open", "Waarom kiest een journalist bewust tussen 'betoger' en 'relschopper'?",
                  "De denotatie ligt dicht bij elkaar, maar de connotatie verschilt sterk. De "
                  "bijklank stuurt het oordeel van de lezer nog voor die de rest van de zin gelezen "
                  "heeft.", 4),
                 ("rij", [("heengaan", "eufemisme"), ("herstructurering", "eufemisme"),
                          ("geklungel", "negatieve connotatie")], "Wat is het?", WW),
                 ("open", "Wat is een dysfemisme, en hoe verhoudt het zich tot een eufemisme?",
                  "Een dysfemisme maakt iets ruwer of harder dan nodig; een eufemisme verzacht juist. "
                  "Ze zijn elkaars tegenpool en allebei een keuze van de schrijver.", 3),
             ]),
        dict(kop="Herkomst",
             opdracht="Noteer het begrip.",
             oefeningen=[
                 ("rij", [("een woord uit een andere taal", "een leenwoord"),
                          ("een wending uit het Engels", "een anglicisme"),
                          ("een woord dat alleen in België bestaat", "een belgicisme")],
                  "Welk begrip?", WL),
                 ("rij", [("appen, googelen, streamen", "neologismen"),
                          ("een verouderd woord", "een archaïsme"),
                          ("een zelf gevormd woord tegen een leenwoord", "een purisme")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een synoniem kan je altijd zomaar in de plaats van een ander woord zetten.", False),
                 ("waar", "Een pleonasme is altijd een fout.", False),
                 ("waar", "Een bastaardwoord bestaat van oudsher in het Nederlands.", False),
                 ("waar", "Een woord met een neutrale denotatie kan een negatieve connotatie krijgen.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-schrijven-en-schriftelijke-interactie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Schrijven en schriftelijke interactie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk tekstdoel?",
             opdracht="Noteer het tekstdoel van de opdracht.",
             oefeningen=[
                 ("rij", [("een brochure over een jeugdhuis", "informatie geven"),
                          ("een stappenplan voor een spel", "iets uitleggen"),
                          ("een recensie van een film", "je mening geven")], "Welk doel?", WL),
                 ("rij", [("een antirookpamflet", "overtuigen"),
                          ("een mail over je vakantiejob", "iets vertellen"),
                          ("een flyer voor een festival", "creatief zijn met taal")], "Welk doel?", WL),
             ]),
        dict(kop="Welk beoordelingscriterium?",
             opdracht="Noteer het criterium waar de opmerking over gaat.",
             oefeningen=[
                 ("rij", [("je tekst gaat niet over de gevraagde opdracht", "taakvoltooiing"),
                          ("je gebruikt tien keer hetzelfde woord", "woordenschat"),
                          ("je zinnen lopen niet", "grammatica en zinsbouw")], "Welk criterium?", WL),
                 ("rij", [("je mail klinkt veel te familiair", "register en beleefdheidsconventies"),
                          ("er staan dt-fouten in", "spelling en leestekengebruik"),
                          ("de tekst is één blok zonder alinea's", "tekstopbouw en lay-out")],
                  "Welk criterium?", WL),
             ]),
        dict(kop="Plannen",
             opdracht="Schrijf telkens enkele zinnen.",
             oefeningen=[
                 ("open", "Welke drie dingen bepaal je vóór je begint te schrijven?",
                  "Je doel, je ontvanger en je kanaal. Dat zijn de vragen van het "
                  "communicatiemodel, en ze bepalen je toon, je woordkeuze en je lengte.", 3),
                 ("open", "Noem drie schrijfstrategieën die je op weg helpen.",
                  "Een schrijfplan met kernwoorden maken, een vaste tekststructuur kiezen, en jezelf "
                  "vragen stellen over het onderwerp.", 3),
                 ("open", "Je mag op het examen een spellingcontrole gebruiken. Waarom lees je je "
                          "tekst dan toch nog zelf na?",
                  "Een spellingcontrole vindt geen fouten die toevallig bestaande woorden opleveren, "
                  "zoals word in plaats van wordt, en ze ziet niets van je structuur, je register of "
                  "je taakvoltooiing.", 4),
             ]),
        dict(kop="Een formele mail",
             opdracht="Werk de opdracht uit.",
             oefeningen=[
                 ("open", "Schrijf de onderwerpregel, de aanspreking en de slotgroet van een mail "
                          "waarin je een stageplaats aanvraagt bij een onbekend bedrijf.",
                  "Onderwerp: Aanvraag stageplaats, vijfde jaar. Aanspreking: Geachte mevrouw, "
                  "meneer. Slotgroet: Met vriendelijke groeten, gevolgd door je voornaam en "
                  "familienaam.", 5),
                 ("open", "Schrijf de eerste twee zinnen van een klacht aan een bedrijf over een "
                          "pakje dat nooit aankwam.",
                  "Bijvoorbeeld: Op 3 maart bestelde ik bij u een paar schoenen met bestelnummer "
                  "12345. Het pakje is tot op vandaag niet geleverd, en de zending is sinds 7 maart "
                  "niet meer te volgen. De inleiding zegt dus waarover je schrijft en wat er gebeurd "
                  "is; wat je vraagt, komt daarna.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Spelling en leestekengebruik zijn een apart criterium bij schrijven.", True),
                 ("waar", "Een tekst die zijn doel bereikt maar vol fouten staat, scoort op alle "
                          "criteria goed.", False),
                 ("waar", "Bij woordenschat verwacht men enkel eenvoudige woorden.", False),
                 ("waar", "Bij schriftelijke interactie reageer je op wat een ander schreef.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-spreken-en-gesprekken-voeren-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Spreken en gesprekken voeren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Spreken of schrijven?",
             opdracht="Noteer of het criterium bij spreken, bij schrijven of bij allebei hoort.",
             oefeningen=[
                 ("rij", [("lichaamstaal", "spreken"), ("spelling", "schrijven"),
                          ("taakvoltooiing", "allebei")], "Waar hoort het?", WW),
                 ("rij", [("uitspraak en intonatie", "spreken"), ("lay-out", "schrijven"),
                          ("register", "allebei")], "Waar hoort het?", WW),
             ]),
        dict(kop="Begrippen",
             opdracht="Noteer het begrip.",
             oefeningen=[
                 ("rij", [("de melodie en de klemtoon in je zinnen", "intonatie"),
                          ("de klanken van de taal correct vormen", "uitspraak"),
                          ("houding, gebaren en oogcontact samen", "lichaamstaal")], "Welk begrip?", WW),
                 ("kort", "Hoe noem je een plan met kernwoorden voor een spreekbeurt?", "een spreekplan", WW),
                 ("kort", "Hoeveel minuten voorbereiding krijg je voor het gesprek?", "vijftien", W),
             ]),
        dict(kop="Wat doe je?",
             opdracht="Schrijf telkens enkele zinnen.",
             oefeningen=[
                 ("open", "Je merkt tijdens je spreekbeurt dat je publiek je niet volgt. Wat doe je, "
                          "en wat doe je zeker niet?",
                  "Je herneemt het punt in andere woorden en je kijkt of het nu wel landt. Je praat "
                  "zeker niet sneller verder en je slaat de rest niet over.", 4),
                 ("open", "Je begrijpt iets niet in een gesprek. Noem drie strategieën.",
                  "Om verduidelijking vragen, samenvatten wat je wel begrepen hebt, en vragen of de "
                  "ander het wil herhalen. Doen alsof je het begrepen hebt loopt verderop vast.", 4),
                 ("open", "Je krijgt een vraag die je niet verwacht had. Wat doe je?",
                  "Je neemt even de tijd en antwoordt dan. Een korte denkpauze mag en klinkt beter "
                  "dan een halsoverkop antwoord.", 3),
                 ("open", "Hoe sluit je een gesprek beleefd af?",
                  "Je bedankt voor het gesprek, je vat kort samen waar jullie geraakt zijn, en je "
                  "gebruikt een gepaste afscheidsformule.", 3),
             ]),
        dict(kop="Je leeservaring verwoorden",
             opdracht="Werk uit in volledige zinnen.",
             oefeningen=[
                 ("open", "Kies een boek dat je gelezen hebt. Schrijf in vier zinnen wat het bij je "
                          "opriep en waarom, zonder het verhaal na te vertellen.",
                  "Een eigen antwoord. Let erop dat je je eigen reactie onderbouwt met iets uit het "
                  "boek: een personage, een scène, een manier van vertellen. Het verhaal navertellen "
                  "of de achterflap opzeggen is geen leeservaring.", 6),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Vlotheid betekent zo snel mogelijk spreken.", False),
                 ("waar", "Een bewuste pauze mag en maakt je betoog sterker.", True),
                 ("waar", "Een gesprek over een boek van de lectuurlijst kan op het examen komen.", True),
                 ("waar", "Wie nooit doorvraagt, haalt het hoogste niveau van interactie.", False),
                 ("waar", "Beleefdheidsconventies gelden alleen in geschreven taal.", False),
             ]),
    ],
)
