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

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-tekstsoorten-en-teksttypes-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elke tekst af wat de zender van je wil: iets laten weten, iets laten "
                   "doen, je overtuigen, je iets laten voelen, of een verhaal vertellen.",
            waarom=[
                "Let op prescriptief: dat is de soort die je zegt wat je moet doen, zoals een "
                "bijsluiter of een recept. Een handleiding is dus geen informatieve tekst.",
                "Let op het verschil tussen informatief en opiniërend: een dossier legt uit, een "
                "lezersbrief vindt iets. Het woordje ik of een waardering verraadt het tweede.",
            ],
        ),
        dict(
            aanpak="Eén tekst kan meerdere doelen hebben. Lees ze in stukken en zet bij elk stuk het "
                   "doel, en zeg daarna wat het hoofddoel is.",
            waarom=[
                "Noem alle drie de doelen, want de tekst heeft drie delen. Let erop dat de oproep op "
                "het einde het hoofddoel verraadt: daar komt de podcast op uit.",
                "Noem ook welk doel het hoofddoel is, zoals het antwoord doet. De feiten in een "
                "recensie staan er om het oordeel te dragen, en dus niet omgekeerd.",
            ],
        ),
        dict(
            aanpak="De zender is niet altijd wie je ziet of hoort. Vraag je af wie betaalt en wie "
                   "beslist wat erin komt.",
            waarom=[
                "Noem beide delen: wie de echte zender is, en wat je daarmee doet. Dat tweede, een "
                "bron zoeken zonder belang, is wat de vraag uitdrukkelijk vraagt.",
                "Noem dat de soort je wel op je hoede zet. Zo zeg je niet dat de tekstsoort niets "
                "uitmaakt, maar dat ze iets anders zegt dan of de tekst waar is.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: het examen, wat literair kan zijn, en de "
                   "verwarring tussen feiten en tekstsoort.",
            waarom=[
                "Niet waar: ook een gesprek in de tussentaal of een tekst met dialect kan op het "
                "examen staan. Je moet die net kunnen plaatsen.",
                "Waar: literair gaat over de vorm en het effect, niet over de drager. Ook een strip, "
                "een lied of een film kan literair zijn.",
                "Niet waar: ook een persuasieve tekst kan vol feiten staan. Het doel beslist de "
                "soort, niet het aantal feiten.",
                None,
            ],
        ),
        dict(
            aanpak="Bij zelf schrijven blijf je het best bij één onderwerp en verander je enkel het "
                   "doel. Zo zie je zelf waar het verschil zit.",
            waarom=[
                "Noem ook waaraan men het verschil ziet, zoals gevraagd. De oproep, de toon en de "
                "overdrijving zijn de drie dingen om te benoemen.",
                "Noem beide soorten en zeg bij elk waarom. Dat de vorm zelf meedoet, is wat een tekst "
                "literair maakt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-onderwerp-hoofdgedachte-en-samenvatten-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Eén proef scheidt de twee: een onderwerp kan je in een paar woorden zeggen, een "
                   "hoofdgedachte is een hele zin met een bewering erin.",
            waarom=[
                "Let erop dat een onderwerp geen werkwoord nodig heeft en een hoofdgedachte wel. Waar "
                "je ja of nee op kan zeggen, is een hoofdgedachte.",
                None,
            ],
        ),
        dict(
            aanpak="Lees het stukje twee keer: eerst om te weten waarover het gaat, dan om te zien "
                   "wat de schrijver erover beweert. Let op het woord dat de bocht aankondigt.",
            waarom=[
                None,
                "Noem beide kanten in één zin: de voordelen en de reden om papier niet op te geven. "
                "Een hoofdgedachte die maar één kant noemt, mist de kern van deze tekst.",
                "Noem de twee punten apart, zoals gevraagd. Elk punt staat aan een kant van het "
                "woord toch.",
                "Let op het woord toch: dat kondigt de tegenstelling aan en zet de hoofdgedachte in "
                "de tweede helft van de tekst. Zulke signaalwoorden zijn je snelste weg naar de kern.",
            ],
        ),
        dict(
            aanpak="Notities en een mindmap dienen niet om alles op te schrijven maar om het verband "
                   "te zien. Hou dat bij beide vragen vast.",
            waarom=[
                "Noem alle drie de eisen, zoals gevraagd. Let erop dat afkortingen en telegramstijl "
                "mogen: notities hoeven geen volle zinnen te zijn.",
                "Noem dat je in een mindmap de verbanden ziet. Dat is het enige echte voordeel, en "
                "het is er een groot.",
            ],
        ),
        dict(
            aanpak="Een samenvatting is korter, in eigen woorden, zonder je mening. Die drie regels "
                   "beslissen alle vier de vragen van deze reeks.",
            waarom=[
                "Niet waar: in je eigen woorden is de kern van samenvatten. Letterlijk overnemen is "
                "citeren, en dan hoort er een bronvermelding bij.",
                "Waar: je mag hergroeperen, zolang de inhoud juist blijft. Soms wordt een "
                "samenvatting daardoor zelfs duidelijker dan het origineel.",
                "Niet waar: je mening hoort in een reactie of een bespreking, niet in een "
                "samenvatting. Een lezer moet uit je samenvatting niet kunnen opmaken wat jij ervan "
                "vindt.",
                "Noem allebei: wat er misliep en wat hij moet doen. Voorbeelden, herhalingen en "
                "anekdotes zijn het eerste dat eruit gaat.",
            ],
        ),
        dict(
            aanpak="Tel je woorden en schrijf eerst de hoofdgedachte op. Pas als die er staat, voeg je "
                   "toe wat er nog bij past binnen de dertig woorden.",
            waarom=[
                "Let erop dat de tegenstelling in je samenvatting moet blijven. Zonder het woord maar "
                "of toch staat er iets anders dan in de tekst.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-bronnen-beoordelen-betrouwbaarheid-nepnieuws-en-framing-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zes vragen, zes criteria. Hou ze in twee groepen: vragen over de bron zelf, en "
                   "vragen over wat jij ermee wil doen.",
            waarom=[
                "Let erop dat wie betaalt de scherpste vraag van de zes is. Daarmee ontdek je een "
                "belang, en een belang verklaart vaak wat er in de tekst staat.",
                "Let op de relevantie: dat is het enige criterium dat over jou gaat en niet over de "
                "bron. Een heel betrouwbare bron kan voor jouw opdracht toch onbruikbaar zijn.",
            ],
        ),
        dict(
            aanpak="Geef bij elke bron een oordeel én een reden. Vraag je telkens af wie belang heeft "
                   "bij het antwoord, en of de bevestiging echt onafhankelijk is.",
            waarom=[
                "Noem zowel de pluspunten als wat je nog nagaat. Een auteursnaam en studies zijn "
                "goede tekens, maar wie de studie betaalde, is de vraag die erbij hoort.",
                "Noem dat dezelfde zinnen op één bron wijzen. Onafhankelijke bevestiging betekent dat "
                "verschillende mensen het apart hebben nagegaan.",
                "Noem beide delen: je eerste stap en het vermoedelijke doel. Dat advertenties per "
                "bezoeker geld opleveren, verklaart waarom zulke berichten gemaakt worden.",
            ],
        ),
        dict(
            aanpak="Framing gaat over de woordkeuze bij hetzelfde feit. Zoek telkens het woord dat de "
                   "andere kant opwijst, en let ook op beelden en grafieken.",
            waarom=[
                "Let erop dat beide woorden hetzelfde feit beschrijven. Besparing en "
                "belastingverlaging gaan over dezelfde maatregel, enkel de kant verschilt.",
                "Noem allebei: het effect en dat de grafiek niet onwaar is. Het woord misleidend is "
                "hier scherper dan onwaar, en dat is precies wat deze vraag toetst.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat een mooie website bewijst, wanneer "
                   "ouderdom telt, en het verschil tussen reclame en propaganda.",
            waarom=[
                "Niet waar: een vormgeving kost een paar uur. Juist nepsites zien er vaak heel "
                "verzorgd uit, en dat is bewust.",
                "Niet waar: voor een cijfer over dit jaar is ze onbruikbaar, voor een gebeurtenis uit "
                "de geschiedenis niet. De actualiteit hangt van je vraag af.",
                None,
                "Niet waar, en het staat net omgekeerd: reclame stuurt je koopgedrag, propaganda je "
                "denken over mensen en machthebbers. De twee gebruiken wel dezelfde technieken.",
            ],
        ),
        dict(
            aanpak="Deze twee vragen gaan over jou. Hou vast dat een echokamer over de groep gaat en "
                   "een filterbubbel over het algoritme.",
            waarom=[
                "Noem het verschil uitdrukkelijk, zoals gevraagd. De groep tegenover de techniek is "
                "de scherpste manier om het te zeggen.",
                "Noem beide delen: waarom het gebeurt en wat je eraan doet. Dezelfde vragen stellen "
                "bij wat je graag leest, is het hele antwoord.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-communicatiemodel-en-ruis-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vul het model altijd in dezelfde orde in: wie, aan wie, wat, waarmee en waarvoor. "
                   "Het kanaal is het middel, het doel is het gewenste gevolg.",
            waarom=[
                "Let op het verschil tussen de boodschap en het doel: de boodschap is wat er staat, "
                "het doel is wat de club wil bereiken. Die twee worden het vaakst verward.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist: zit het bij de zender (doel) of bij de ontvanger (effect)? "
                   "Alles wat er bij jou gebeurt, is effect.",
            waarom=[
                "Let op de derde: de zender wilde waarschuwen en de mensen lachen. Dat is een effect, "
                "en het toont dat een boodschap haar doel kan missen.",
                "Noem van beide waar ze zitten, bij de zender of bij de ontvanger. Dat ze vaak maar "
                "niet altijd samenvallen, hoort erbij.",
            ],
        ),
        dict(
            aanpak="Eén vraag: zit de storing buiten de personen (externe ruis) of in hun hoofd "
                   "(interne ruis)? Geluid en techniek zijn buiten, gedachten en voorkennis zijn "
                   "binnen.",
            waarom=[
                None,
                "Let op het vakjargon: dat klinkt als iets in de tekst, maar het wordt ruis doordat de "
                "lezer de woorden niet kent. Het zit dus bij de persoon, en daarom is het interne "
                "ruis.",
            ],
        ),
        dict(
            aanpak="Zoek bij elke situatie het onderdeel van het model dat misliep: de zender, het "
                   "kanaal of de context. Benoem het met zijn naam.",
            waarom=[
                "Noem dat het bij de zender ligt. Dat is het ongemakkelijke deel van het antwoord, en "
                "net daarom vraagt de vraag ook bij wie.",
                "Noem het kanaal met naam. Het gaat hier niet over de tekst zelf: die kan perfect "
                "zijn en toch niemand bereiken.",
                "Noem de context. Dezelfde boodschap werkt anders in een krant, in een klas of tussen "
                "grappige filmpjes.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: waar ruis zit, wat bij de boodschap hoort, en "
                   "waarvoor het model dient.",
            waarom=[
                "Niet waar: ruis kan ook bij de zender zitten, zoals bij de verpleegkundige met zijn "
                "vaktaal, of in het kanaal.",
                "Waar: emoji's, opmaak en toon horen bij de boodschap. Ze veranderen wat er gezegd "
                "wordt, en dus ook het effect.",
                "Niet waar: het model werkt bij een gesprek, een filmpje, een affiche en een lied. "
                "Alles waarin iemand iets aan iemand wil overbrengen.",
                "Waar: in een gesprek wisselen de rollen voortdurend. Dat is ook waarom een gesprek "
                "minder ruis geeft dan een brief: je kan meteen bijvragen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-tekstopbouw-alineaverbanden-en-structuuraanduiders-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De eerste woorden van een alinea verraden het verband. Leer per verband één "
                   "signaalwoord, dan herken je de rest erbij.",
            waarom=[
                "Let op doel-middel: het woordje om kondigt dat aan. Dat is een ander verband dan "
                "oorzakelijk, ook al lijken ze op elkaar.",
                "Let op het verschil tussen oorzakelijk en voorwaardelijk: doordat zegt dat het echt "
                "gebeurd is, op voorwaarde dat zegt dat het nog moet gebeuren.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elke tekst af welke vragen hij achtereenvolgens beantwoordt. Die "
                   "reeks vragen is de structuur.",
            waarom=[
                "Let op het verschil tussen de probleem- en de onderzoeksstructuur: de eerste zoekt "
                "oplossingen, de tweede antwoordt op een onderzoeksvraag met een methode.",
                "Let op de handelingsstructuur: die geeft stappen in de orde waarin je ze uitvoert. "
                "Een recept en een handleiding volgen ze allebei.",
            ],
        ),
        dict(
            aanpak="Structuuraanduiders zijn de wegwijzers van een tekst. Leer per verband zijn "
                   "woorden, en let erop dat de inhoud het laatste woord heeft.",
            waarom=[
                None,
                "Let erop dat want redengevend is en dus hetzelfde doet als omdat. Het verschil zit "
                "enkel in de zinsbouw erna.",
                None,
                "Noem ook een voorbeeld, zoals de vraag vraagt. Dat het verband uit de inhoud volgt "
                "en niet uit het woord, is de kern van deze bundel.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat een alinea is, hoeveel structuren een "
                   "tekst kan hebben, en wat lay-out wel en niet zegt.",
            waarom=[
                None,
                "Niet waar: een lange tekst kan een probleemstructuur hebben met daarin een "
                "vergelijking en een stukje geschiedenis. Structuren kunnen in elkaar zitten.",
                "Niet waar: een mooie vormgeving zegt niets over de juistheid. Dat is dezelfde fout "
                "als bij een professioneel ogende website.",
                None,
            ],
        ),
        dict(
            aanpak="Bij zelf opbouwen hou je drie delen vast: de inleiding wekt interesse, het midden "
                   "werkt uit met één deelonderwerp per alinea, en het slot besluit.",
            waarom=[
                "Noem bij elk deel wat er concreet in komt. Een inleiding die enkel het onderwerp "
                "noemt, wekt nog geen interesse.",
                "Noem drie dingen, zoals gevraagd, en noem zeker het slot. Daar staat waar de tekst "
                "op uitdraait, en dat zegt je snel of hij nuttig is.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-argumentatie-en-drogredenen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Eén proef: kan iemand het nagaan en er ja of nee op antwoorden? Dan is het een "
                   "feit. Staat er een waardering in, zoals beste of te weinig, dan is het een mening.",
            waarom=[
                None,
                "Let op de derde: te veel of te weinig is altijd een mening, ook als er cijfers bij "
                "staan. Het cijfer is een feit, het oordeel erover niet.",
            ],
        ),
        dict(
            aanpak="Ontleed een betoog in vier delen: de stelling, de argumenten, het tegenargument "
                   "met de weerlegging, en de conclusie. Markeer ze in de tekst.",
            waarom=[
                None,
                "Let erop dat een verwijzing naar een studie met een aantal deelnemers "
                "wetenschappelijke argumentatie is. Een voorbeeld uit je eigen klas zou dat niet zijn.",
                "Noem beide delen: het tegenargument en hoe het weerlegd wordt. Dat de schrijver het "
                "zelf noemt, maakt zijn betoog juist sterker.",
                None,
            ],
        ),
        dict(
            aanpak="Zes drogredenen met elk een vorm. Vraag je af wat er mis is: gaat het over de "
                   "persoon, over de massa, over een nep-keuze, of over een voorspelde ramp?",
            waarom=[
                "Let op het vals dilemma: er worden twee keuzes gegeven terwijl er meer zijn. Het "
                "woordje ofwel is daar bijna altijd het teken van.",
                "Let op het hellend vlak: er wordt een ramp voorspeld zonder te laten zien hoe je "
                "daar zou komen. Een cirkelredenering gebruikt haar besluit als bewijs.",
            ],
        ),
        dict(
            aanpak="Drie vragen over wat een argument waard is. Hou vast dat samen stijgen nog geen "
                   "oorzaak is.",
            waarom=[
                "Noem drie vragen, zoals gevraagd, en noem zeker wie het betaalde. Dat is dezelfde "
                "vraag als bij het beoordelen van een bron.",
                "Noem het verschil tussen samenhang en oorzaak. En noem dat er een derde oorzaak kan "
                "zijn: hier bijvoorbeeld een groeiende bevolking in de gemeente.",
                "Noem alle drie de eisen, zoals gevraagd. Waar zijn is niet genoeg: een waar argument "
                "dat niets met de stelling te maken heeft, telt niet mee.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: cijfers in een betoog, de plaats van een "
                   "mening, en wat een betoog sterk maakt.",
            waarom=[
                "Niet waar: cijfers kunnen uit een slecht onderzoek komen of misleidend gepresenteerd "
                "zijn. Een cijfer is een argument en geen bewijs op zich.",
                "Niet waar: in een opiniestuk of een recensie hoort een mening er juist. Ze moet wel "
                "onderbouwd zijn, en in een samenvatting of een verslag hoort ze niet.",
                None,
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-literaire-begrippen-en-genres-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie hoofdgroepen met drie vragen: wordt er verteld (epiek), spreekt er een ik "
                   "over zijn binnenkant (lyriek), of wordt het gespeeld (dramatiek)?",
            waarom=[
                "Let op de klucht en de tragedie: beide zijn dramatiek, ook al is de ene om te lachen "
                "en de andere niet. De hoofdgroep gaat over de vorm, niet over de toon.",
            ],
        ),
        dict(
            aanpak="Negen genres. Leer ze aan hun kenmerk: dieren met een les, een beeld met een "
                   "waarheid, een held in verzen, brieven, een leven dat vormt.",
            waarom=[
                "Let op het verschil tussen de fabel en de parabel: in een fabel treden dieren op, in "
                "een parabel mensen in een alledaags beeld. Beide eindigen in een les.",
                "Let op de allegorie: daar staat alles voor iets anders, niet één ding zoals bij een "
                "symbool. Het hele verhaal is dan een beeld.",
                "Let op de sleutelroman: de lezer die de sleutel heeft, herkent echte personen. "
                "Daarom is zo'n roman soms een rechtszaak waard geweest.",
            ],
        ),
        dict(
            aanpak="Drie soorten humor, drie doelen: ironie zegt het omgekeerde, sarcasme wil raken, "
                   "satire wil een misstand aanklagen.",
            waarom=[
                "Noem dat sarcasme bedoeld is om te raken. Dat is het enige verschil met ironie, en "
                "het is een verschil in bedoeling en niet in vorm.",
                "Noem waar elk op mikt: de parodie op de vorm, de satire op de wereld. Met die twee "
                "woorden is het verschil in één zin gezegd.",
                None,
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: de lengte van genres, wat literair kan zijn, "
                   "en hoe streng een genre is.",
            waarom=[
                "Niet waar, en het is net omgekeerd: een novelle is korter dan een roman en langer "
                "dan een kortverhaal. De orde is kortverhaal, novelle, roman.",
                "Niet waar: ook een waargebeurd verhaal kan literair verteld zijn. Literair gaat over "
                "de vorm, non-fictie over de inhoud.",
                "Niet waar: een historische roman mag verzinnen, zolang de tijd geloofwaardig blijft. "
                "Een schrijver is geen historicus.",
                None,
                "Waar: dat is precies wat een stadssage werkt. Ze wordt doorverteld als iets dat "
                "iemands kennis is overkomen, en dat maakt haar geloofwaardig.",
            ],
        ),
        dict(
            aanpak="Twee open vragen over waarom je dit leert. Geef bij de eerste een voorbeeld, zoals "
                   "gevraagd.",
            waarom=[
                "Noem beide delen: wat gelaagdheid is en hoe het kan werken. Zonder voorbeeld blijft "
                "het een definitie.",
                "Noem dat je in één woord zegt wat anders een alinea kost. Dat is het praktische "
                "nut, en het geldt in elk vak met zijn eigen woorden.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-verhaalkenmerken-en-vertelperspectief-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Negen begrippen in drie groepen: over de personages, over de opbouw, en over wat "
                   "er terugkeert of verwijst.",
            waarom=[
                "Let op de antagonist en de antiheld: de eerste werkt tegen, de tweede is de "
                "hoofdpersoon zelf maar zonder heldhaftige kant. Ze beginnen met dezelfde letters en "
                "betekenen iets anders.",
                "Let op de pointe: die zit op het einde en keert je blik om. De climax is het "
                "spanningshoogtepunt en kan er al eerder liggen.",
                "Let op het verschil tussen een symbool en een motief: een symbool staat voor iets "
                "anders, een motief keert gewoon terug. Een terugkerend symbool is dan beide.",
            ],
        ),
        dict(
            aanpak="Bij het perspectief stel je altijd dezelfde vraag: wie weet wat? Wie alles weet, "
                   "is auctorieel; wie enkel binnen één hoofd kijkt, is personaal.",
            waarom=[
                "Let op de onbetrouwbare verteller: die bestaat enkel doordat je als lezer merkt dat "
                "er iets niet klopt. Dat is een van de sterkste effecten in de literatuur.",
                "Noem van beide wat ze weten over het einde. Dat is het onderscheid, en het verklaart "
                "waarom een vertellende ik commentaar kan geven op zijn jongere zelf.",
            ],
        ),
        dict(
            aanpak="Hou twee tijden apart: de vertelde tijd is hoe lang het verhaal duurt, de "
                   "verteltijd hoe veel bladzijden het krijgt. Hun verhouding geeft versnelling of "
                   "vertraging.",
            waarom=[
                None,
                "Let erop dat vertraging betekent dat er veel bladzijden over weinig tijd gaan. Een "
                "hele roman over één dag is daar het bekendste voorbeeld van.",
                "Noem van beide wat ze zijn, met een voorbeeld van een duur. Enkel het woord leestijd "
                "noemen is te weinig.",
                None,
            ],
        ),
        dict(
            aanpak="Een ruimte doet in een verhaal altijd iets. Vraag je af of ze de sfeer zet, de "
                   "klasse van de personages toont, of voor iets anders staat.",
            waarom=[
                "Noem beide delen: de functie en wat ze over de personages zegt. De ruimte als beeld "
                "van hun leven is wat de vraag zoekt.",
                "Noem alle vier met een voorbeeld, zoals gevraagd. Let erop dat sociale ruimte over "
                "de omgeving en de klasse gaat, niet over een plaats op de kaart.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat een personage kan zijn, wat een verteller "
                   "weet, en wat een niet-chronologische opbouw betekent.",
            waarom=[
                "Waar: ook een hoofdpersoon kan vlak zijn, zoals in veel spannende verhalen of "
                "strips. Vlak betekent weinig uitgewerkt, niet onbelangrijk.",
                "Niet waar: een ik-verteller kan enkel vermoeden wat anderen denken. Doet hij dat "
                "alsof hij het weet, dan maakt de schrijver er bewust een onbetrouwbare verteller "
                "van.",
                "Niet waar: een flashback of een begin in medias res is een keuze, niet een fout. "
                "Veel sterke romans zijn juist zo gebouwd.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-poezie-dichtvormen-strofen-en-rijm-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zes vormen, zes aantallen. Een hulpje bij de namen: distichon heeft di van twee, "
                   "kwatrijn kwa van vier, octaaf oct van acht.",
            waarom=[
                "Let op het sonnet met veertien verzen: dat is acht plus zes, dus een octaaf en een "
                "sextet. Precies op die grens zit de volta uit de vierde reeks.",
            ],
        ),
        dict(
            aanpak="Zes dichtvormen aan hun kenmerk: klagen, loven, vertellen met een refrein, een "
                   "woord in de eerste letters, verzen die terugkomen, of de vorm zelf als beeld.",
            waarom=[
                "Let op het verschil tussen een elegie en een ode: de ene rouwt, de andere eert. "
                "Beide zijn lyriek met een duidelijke toon.",
                "Let op het rondeel: daar keren hele verzen letterlijk terug, en niet enkel een rijm. "
                "Die herhaling is zijn hele werking.",
            ],
        ),
        dict(
            aanpak="Zet de rijmklanken als letters onder de verzen, dan zie je het schema meteen. "
                   "Zelfde letter betekent zelfde rijmklank.",
            waarom=[
                "Let op omarmend rijm: abba betekent dat het eerste en het laatste vers rijmen, met "
                "een paar erin omsloten. De naam zegt het zelf.",
                "Let op het verschil tussen assonantie en alliteratie: de eerste zit in de klinkers "
                "middenin de woorden, de tweede in de beginklank.",
                None,
            ],
        ),
        dict(
            aanpak="Bij vorm en klank kijk je naar waar de regels afbreken en waar het wit staat. Die "
                   "keuzes zijn bij een dichter nooit toevallig.",
            waarom=[
                "Noem het woord enjambement. De regel breekt af terwijl de zin doorgaat, en daardoor "
                "krijgt het laatste woord van de regel extra gewicht.",
                "Noem beide effecten: de aandacht en het vertragen. Wit op een bladzijde werkt als "
                "stilte in muziek.",
                None,
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wie in een gedicht spreekt, of een gedicht "
                   "moet rijmen, en de soorten rijm.",
            waarom=[
                "Niet waar: het lyrisch subject is de stem in het gedicht, en dat kan iemand anders "
                "zijn dan de dichter. Een dichter kan een kind of een dode laten spreken.",
                "Niet waar: dat heet vrije verzen, en een groot deel van de moderne poëzie is zo. "
                "Klank en ritme blijven er wel in meespelen.",
                None,
                "Waar, en bij vrouwelijk rijm volgt er nog een onbeklemtoonde lettergreep na. Dat "
                "verschil beslist hoe een vers eindigt: hard of zacht.",
            ],
        ),
        dict(
            aanpak="Twee opdrachten over de klank. Lees je eigen regels hardop, dan hoor je zelf of "
                   "de alliteratie werkt.",
            waarom=[
                "Noem wat je enkel hoort en niet ziet: alliteratie, assonantie en het ritme. Dat is "
                "waarom poëzie hardop gelezen hoort te worden.",
                "Onderstreep de herhaalde beginklank, zoals gevraagd. Let erop dat het om de klank "
                "gaat en niet om de letter: een c kan als een k of een s klinken.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-dramatiek-en-theatertekens-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Negen toneelvormen. Hou ze per tijd bij elkaar: de middeleeuwse spelen, de "
                   "klassieke vormen, en het theater van de twintigste eeuw.",
            waarom=[
                "Let op de moraliteit: daar zijn de personages vaak geen mensen maar deugden en "
                "ondeugden. De les is het hele punt van het stuk.",
                "Let op het verschil tussen het mirakelspel en het abel spel: het eerste is "
                "religieus, het tweede wereldlijk. Abel betekent trouwens edel of kunstig.",
                "Let op het verschil tussen absurd en episch theater: het eerste toont een wereld "
                "zonder logica, het tweede houdt je bewust op afstand om je te laten nadenken.",
            ],
        ),
        dict(
            aanpak="Theatertekens zijn alles wat je ziet en hoort naast de woorden. Vraag je af of het "
                   "bij het lichaam, bij de ruimte of bij de techniek hoort.",
            waarom=[
                "Let op proxemiek: dat is de afstand tussen de spelers. Dat is een teken dat een "
                "lezer van de tekst nooit ziet, en een toeschouwer meteen.",
                "Let op de paraverbale tekens: toon, tempo, volume en stiltes. Dezelfde zin kan daarmee "
                "het omgekeerde betekenen.",
            ],
        ),
        dict(
            aanpak="Bij een scène vraag je telkens: wat wordt hier getoond in plaats van gezegd? Noem "
                   "het theaterteken met zijn naam.",
            waarom=[
                "Noem beide delen: wat het zegt en hoe het teken heet. Dat de vervreemding getoond "
                "wordt en niet uitgesproken, is de kern.",
                "Noem ook hoe je het beoordeelt, zoals de vraag vraagt. De maatstaf is of de keuzes de "
                "tekst versterken, en niet of ze modern zijn.",
                "Noem de laag tekens die de opvoering toevoegt. Dat is waarom een toneeltekst om een "
                "voorstelling vraagt, zoals een partituur om muzikanten.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: de middeleeuwse spelen, wat episch theater "
                   "wil, en wat een theaterteken is.",
            waarom=[
                None,
                "Niet waar, en het is net omgekeerd: episch theater wil juist dat je niet wegzinkt in "
                "het verhaal. Brecht liet daarom borden en liederen de illusie doorbreken.",
                "Niet waar: muziek en geluid zijn theatertekens, net als licht en decor. Ze bepalen "
                "mee hoe je een scène leest.",
                None,
                "Niet waar: bij een opvoering komen alle theatertekens erbij. Een tekst lezen is maar "
                "een deel van de analyse.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-stijlfiguren-en-beeldspraak-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek bij elke zin wat er precies gebeurt: wordt iets vergeleken, vervangen, "
                   "bezield, overdreven of herhaald?",
            waarom=[
                "Let op het verschil tussen de eerste twee: het woordje als of zoals maakt het een "
                "vergelijking. Zonder dat woord vervangt het beeld de zaak, en dan is het een "
                "metafoor.",
                "Let op de litotes: die zegt minder dan ze bedoelt, met een ontkenning. Niet slecht "
                "betekent in zo'n geval uitstekend.",
                "Let op de anafoor: dezelfde woorden aan het begin van opeenvolgende delen. Het is een "
                "klassieke truc in toespraken, want de herhaling bouwt kracht op.",
            ],
        ),
        dict(
            aanpak="Eén vraag: zegt de figuur meer of minder dan er bedoeld wordt? Enkel de hyperbool "
                   "vergroot, de andere drie verzwakken.",
            waarom=[
                "Let erop dat een eufemisme verzwakt om een pijnlijke zaak te verzachten, zoals "
                "heengaan voor sterven. Litotes en understatement verzwakken om een ander effect.",
            ],
        ),
        dict(
            aanpak="Drie open vragen over waarom beeldspraak werkt. Geef bij de eerste van elk een "
                   "eigen voorbeeld, zoals gevraagd.",
            waarom=[
                "Noem het verschil en geef twee eigen voorbeelden, zoals gevraagd. Hetzelfde beeld in "
                "beide vormen zetten is de duidelijkste manier.",
                "Noem dat een beeld iets abstracts voelbaar maakt. Dat is het hele nut, en het is ook "
                "waarom een goede uitleg vaak een beeld gebruikt.",
                "Noem dat het beeld zijn kracht kwijt is. Een cliché is dus geen fout tegen de taal "
                "maar een gemiste kans.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: waar beeldspraak voorkomt, wat een paradox is, "
                   "en de betekenis van antropomorfisme.",
            waarom=[
                "Niet waar: ook in reclame, in de krant en in een gewoon gesprek zit beeldspraak. De "
                "voet van een berg en het hart van de stad zijn metaforen.",
                None,
                None,
                None,
                "Niet waar, en het staat net omgekeerd: bij antropomorfisme krijgt een dier of een ding "
                "menselijke eigenschappen. Dat is hetzelfde idee als een personificatie.",
            ],
        ),
        dict(
            aanpak="Twee eigen zinnen. Kies eerst de figuur, schrijf dan de zin, en lees na of de "
                   "figuur er echt in zit.",
            waarom=[
                "Let erop dat een personificatie een werkwoord nodig heeft dat alleen een mens kan "
                "doen, zoals beuken, fluisteren of klagen. Anders is het geen personificatie.",
                "Let erop dat de anafoor het herhaalde begin is. Drie keer hetzelfde woord vooraan is "
                "sterker dan twee, en meer dan drie wordt te veel.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-literaire-stromingen-van-de-middeleeuwen-tot-nu-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Twaalf stromingen, elk met één kernwoord. Hou de tegenstellingen vast: rede "
                   "tegenover gevoel, werkelijkheid tegenover vervorming.",
            waarom=[
                "Let op de barok: overvloed en vergankelijkheid samen. Het leven moet gevierd worden "
                "juist omdat het voorbijgaat.",
                "Let erop dat de romantiek een antwoord is op de verlichting. Elke stroming zet zich af "
                "tegen de vorige, en dat is de rode draad van de hele bundel.",
                "Let op het verschil tussen realisme en naturalisme: het naturalisme voegt een theorie "
                "toe, namelijk dat afkomst en omgeving het lot bepalen.",
                "Let op het magisch-realisme: het wonderlijke wordt er heel gewoon gebracht, zonder "
                "uitleg. Dat is het verschil met fantasie.",
            ],
        ),
        dict(
            aanpak="Zet de stromingen op een tijdlijn van de zestiende eeuw tot vandaag. Een anker: de "
                   "verlichting is de achttiende eeuw, het naturalisme het einde van de negentiende.",
            waarom=[
                "Let erop dat de romantiek tussen de verlichting en het naturalisme zit. Wie de "
                "romantiek te laat zet, haalt de hele rij door elkaar.",
            ],
        ),
        dict(
            aanpak="Zeg bij elke tekst de stroming en de reden. De reden is wat de kenmerken van die "
                   "stroming in de tekst zelf zijn.",
            waarom=[
                "Noem de kenmerken die je ziet: erfelijkheid, milieu en de taboeonderwerpen. Enkel de "
                "naam geven is maar de helft van het antwoord.",
                "Noem dat de illusie doorbroken wordt. Een verteller die toegeeft dat hij verzint, is "
                "het schoolvoorbeeld van het postmodernisme.",
                None,
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: hoe scherp een stroming begint, het verschil "
                   "tussen realisme en naturalisme, en of een schrijver bij één stroming hoort.",
            waarom=[
                "Niet waar: stromingen lopen in elkaar over, en de jaartallen in een handboek zijn "
                "hulplijnen. Vaak loopt de ene al terwijl de andere nog bezig is.",
                "Niet waar: het naturalisme is een scherpere vorm met een theorie erachter. Het "
                "realisme beschrijft, het naturalisme verklaart.",
                None,
                "Niet waar: het neorealisme richt zich juist wel op het alledaagse, op gewone mensen en "
                "gewone dingen.",
                None,
            ],
        ),
        dict(
            aanpak="Eén open vraag over het nut van dit alles. Noem zowel de eigen tijd van de tekst "
                   "als waartegen hij zich afzet.",
            waarom=[
                "Noem beide delen: de tekst in zijn tijd plaatsen, en zien waartegen hij reageert. Dat "
                "tweede is wat een stroming begrijpelijk maakt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-taalvarieteiten-registers-en-beleefdheid-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie soorten variatie met drie vragen: hangt ze samen met de streek (regionaal), "
                   "met de groep waartoe je hoort (sociaal), of met de situatie (situationeel)?",
            waarom=[
                "Let op ambtelijke taal: die hangt aan de situatie en niet aan een streek of een "
                "groep. Dezelfde ambtenaar spreekt thuis heel anders.",
                "Let op medisch jargon: dat hoort bij een beroepsgroep, dus sociaal. Het wordt pas "
                "situationeel wanneer je kijkt waar het gebruikt wordt.",
            ],
        ),
        dict(
            aanpak="Eén vraag: ken je de ontvanger persoonlijk, en hoe is de verhouding? Onbekend of "
                   "hoger in rang betekent formeel.",
            waarom=[
                None,
                "Let erop dat een mail aan de directie formeel blijft, ook als je die persoon dagelijks "
                "ziet. De rol beslist en niet de bekendheid.",
            ],
        ),
        dict(
            aanpak="Bij herschrijven verander je vier dingen: de aanspreking, de voornaamwoorden, de "
                   "volledige zinnen en de afsluiting. Doe ze één na één.",
            waarom=[
                "Let erop dat ook de aanspreking en de afsluiting erbij horen. Een formele zin met hey "
                "ervoor is nog niet formeel.",
                "Noem drie keuzes, zoals gevraagd. Afkortingen en emoji's weglaten is de makkelijkste "
                "winst, u gebruiken de belangrijkste.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elke situatie af of het register bij de verhouding past. Te formeel "
                   "klinkt kil, te informeel klinkt slordig.",
            waarom=[
                "Noem beide delen: het effect en hoe het verschijnsel heet. Dat jargon hier als ruis "
                "werkt, verbindt dit met het communicatiemodel.",
                "Noem dat de aanspreking met de verhouding botst. Het gaat niet om een fout tegen de "
                "taal maar om een misser tegen de situatie.",
                "Noem dat precisie er zwaarder weegt dan leesbaarheid. Dat is de reden, en het is ook "
                "waarom er naast een contract vaak een uitleg in gewone taal staat.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat standaardtaal wel en niet oplevert, of "
                   "beleefdheid overal gelijk is, en wat je doet bij twijfel.",
            waarom=[
                "Niet waar: standaardtaal is breder verstaanbaar, maar iemand kan er even onduidelijk "
                "mee zijn. Duidelijkheid hangt van de woordkeuze en de opbouw af.",
                "Niet waar: wat beleefd is, verschilt per taal en per cultuur. Hoe direct je mag zijn "
                "of hoe lang een aanspreking hoort te zijn, is nergens hetzelfde.",
                None,
                "Waar: te formeel valt veel minder op dan te informeel. Je kan daarna altijd nog "
                "losser worden als de ander dat doet.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-taal-en-identiteit-stereotypering-inclusie-en-non-verbale-communicatie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist: kan iedereen die erbij staat het volgen? Zo niet, dan sluit de "
                   "taal uit, ook als dat niet de bedoeling was.",
            waarom=[
                "Let erop dat uitsluiten niet hetzelfde is als kwaad bedoelen. Twee collega's in "
                "dialect doen niets verkeerd en sluiten toch iemand buiten.",
                "Let erop dat afkortingen uitleggen een kleine ingreep is met een groot effect. Inclusie "
                "zit vaak in zulke details.",
            ],
        ),
        dict(
            aanpak="Hou bij stereotypen drie woorden vast: versimpelen, overdrijven en veralgemenen. "
                   "Daaruit volgt waarom ze bijna altijd mislopen.",
            waarom=[
                "Noem alle drie de mechanismen en noem het veralgemenen. Daar zit de fout: van sommigen "
                "naar allen.",
                "Noem beide delen: wat er gebeurt en waarom het een probleem is. Dat kijkers de koppeling "
                "meenemen naar echte mensen, is de kern.",
                "Noem dat je op de inhoud afgaat in plaats van op de klank. Jezelf betrappen is de "
                "eerste stap, bijstellen de tweede.",
            ],
        ),
        dict(
            aanpak="Eén grens: paraverbaal is alles aan de stem, non-verbaal alles aan het lichaam en "
                   "het uiterlijk. De woorden zelf horen bij geen van de twee.",
            waarom=[
                "Let op kleding: dat is non-verbaal, want het zit niet in je stem. Alles wat je hoort "
                "zonder de woorden te verstaan, is paraverbaal.",
            ],
        ),
        dict(
            aanpak="Bij deze vragen weeg je de woorden tegen de signalen af. Spreken ze elkaar tegen, "
                   "dan vraag je door.",
            waarom=[
                "Noem dat je doorvraagt. Zeggen dat de signalen de woorden tegenspreken is de "
                "vaststelling; wat je ermee doet, is het antwoord.",
                "Noem dat toon en gezicht ontbreken. Dat is ook waarom emoji's ontstaan zijn: ze doen "
                "het werk van de intonatie.",
                "Noem drie signalen, zoals gevraagd, en denk aan je hele lichaam: ogen, armen en "
                "richting.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat een stereotype waard is, hoe schrijven "
                   "overkomt, en of non-verbaal ook buiten een gesprek speelt.",
            waarom=[
                "Niet waar: een stereotype is geen samenvatting maar een veralgemening. Het lijkt handig "
                "en het klopt juist voor de persoon voor je meestal niet.",
                None,
                "Niet waar: ook in een appje of een mail werken opmaak, hoofdletters, emoji's en zelfs "
                "de snelheid van antwoorden als signalen.",
                "Niet waar: kleding is non-verbale communicatie. Daarom denk je er bij een sollicitatie "
                "of een presentatie over na.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-klanken-spelling-diakritische-tekens-en-interpunctie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek altijd eerst de stam: ik-vorm van de tegenwoordige tijd. Bij hij komt er een t "
                   "bij, ook als de stam al op een d eindigt.",
            waarom=[
                "Let op hij antwoordt met dt: de stam is antwoord en de t van hij komt erbij. Bij ik "
                "verwacht staat er geen t, want de stam eindigt al op t.",
                "Let op verbrand en gebeurd: met het verlengingstrucje weet je of het een d of een t "
                "is. Verbrande met een d, gebeurde met een d, dus beide een d.",
                "Let erop dat de verleden tijd van werken op te gaat, want de stam eindigt op een k en "
                "die hoort bij het rijtje van 't kofschip.",
            ],
        ),
        dict(
            aanpak="Eén regel: talen en landen krijgen een hoofdletter, dagen en maanden niet. Dat is "
                   "anders dan in het Engels, en dat verklaart de meeste fouten.",
            waarom=[
                "Let erop dat Frans en Duits een hoofdletter krijgen omdat ze van een landnaam komen. "
                "December en dinsdag niet, hoe vaak je ze ook met een hoofdletter ziet staan.",
            ],
        ),
        dict(
            aanpak="Hou de diakritische tekens en de leestekens apart: een trema, een accent en een "
                   "apostrof horen bij het woord, een punt en een komma bij de zin.",
            waarom=[
                "Let op het trema: dat scheidt twee klinkers die anders samen gelezen worden, zoals in "
                "ruïne. Een koppelteken doet hetzelfde werk tussen twee woorddelen.",
                "Let op de dubbele punt: die kondigt aan wat volgt, een opsomming of een uitleg. De "
                "puntkomma scheidt twee zinnen die bij elkaar horen.",
            ],
        ),
        dict(
            aanpak="Verbeter in drie rondes: eerst de werkwoorden, dan de hoofdletters en de "
                   "apostroffen, en als laatste de komma's en de punt.",
            waarom=[
                "Let op twee dingen in deze zin: hij wordt met dt, en twintig met een kleine letter. "
                "Een getal in letters is een gewoon woord en krijgt geen hoofdletter.",
                "Let op de komma's: één na de bijzin vooraan, en één voor want. Voor een voegwoord als "
                "want of maar hoort een komma.",
                "Let op auto's met een apostrof en op 's morgens met een kleine m. En let op de orde: "
                "de tijdsbepaling staat beter vooraan dan achteraan.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: hoe spelling en uitspraak samenhangen, wat "
                   "meetelt als leesteken, en wat leestekens doen.",
            waarom=[
                "Niet waar: wordt klinkt als wort en toch staat er dt. De spelling volgt ook regels over "
                "de vorm van het woord, en niet enkel de klank.",
                "Waar: zonder spaties wordt een tekst onleesbaar, dus de spatie is wel degelijk een "
                "leesteken. Ze scheidt de woorden zoals een punt de zinnen.",
                "Niet waar: maanden en dagen blijven klein. Dat is dezelfde regel als in de tweede "
                "reeks.",
                "Waar, en een komma kan de betekenis omkeren. We eten, opa is iets heel anders dan we "
                "eten opa.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordsoorten-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Kijk niet naar het woord alleen maar naar wat het in die zin doet: iets benoemen, "
                   "iets beschrijven, een plaats aangeven of twee delen verbinden.",
            waarom=[
                "Let op het voorzetsel: dat staat voor een woordgroep en geeft een plaats of een "
                "verhouding. Onder, boven en van zijn de typische.",
                "Let op het bijwoord morgen: het zegt iets over het werkwoord en niet over een "
                "zelfstandig naamwoord. Dat is het verschil met een bijvoeglijk naamwoord.",
                "Let op erg in het is erg koud: het hoort bij koud en niet bij een zelfstandig "
                "naamwoord, dus is het een bijwoord. Erg koud weer zou het ook blijven.",
            ],
        ),
        dict(
            aanpak="Zes soorten voornaamwoorden. Vraag je af wat het woord doet: bezit aangeven, "
                   "terugwijzen naar het onderwerp, een bijzin inleiden, vragen of aanwijzen.",
            waarom=[
                "Let op het betrekkelijk voornaamwoord: dat begint een bijzin die iets zegt over het "
                "woord ervoor. Die en dat zijn de gewone vormen.",
                "Let op deze in de laatste: zonder zelfstandig naamwoord erachter blijft het een "
                "aanwijzend voornaamwoord. Het verwijst naar iets wat eerder genoemd is.",
            ],
        ),
        dict(
            aanpak="Drie soorten werkwoorden met drie vragen: zegt het zelf wat er gebeurt "
                   "(zelfstandig), helpt het een ander werkwoord (hulp), of verbindt het het onderwerp "
                   "met een eigenschap (koppel)?",
            waarom=[
                "Let op is in hij is leraar: daar verbindt het enkel, dus is het een koppelwerkwoord. "
                "In hij is gevallen helpt het, en dan is het een hulpwerkwoord.",
                "Let op worden en blijven: die horen bij de koppelwerkwoorden, net als zijn, lijken, "
                "schijnen, heten en dunken. Dat rijtje is de moeite om vanbuiten te kennen.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: waar woorden kunnen staan, of een woord altijd "
                   "dezelfde soort is, en of een hulpwerkwoord alleen kan.",
            waarom=[
                None,
                "Waar: in de man, groot en sterk, of in een uitdrukking als de prins waardig. Minder "
                "gewoon, maar het bestaat.",
                "Niet waar: het kan ook een persoonlijk voornaamwoord zijn, zoals in het regent of ik "
                "zie het. De zin beslist.",
                "Niet waar: een hulpwerkwoord helpt altijd een ander werkwoord. Hij heeft zonder meer "
                "is geen zin, tenzij heeft daar zelfstandig gebruikt wordt.",
            ],
        ),
        dict(
            aanpak="Twee open vragen over het nut. Hou vast dat de woordsoort uit de zin volgt en niet "
                   "uit het woordenboek.",
            waarom=[
                "Noem dat de zin beslist, met een voorbeeld. Dat is het hele antwoord, en het sluit "
                "aan bij de derde bewering van de vorige reeks.",
                "Noem het naamwoordelijk gezegde. Dat is waarom je dit nodig hebt, en de volgende "
                "bundel over zinsontleding bouwt er verder op.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-morfologie-samenstellingen-afleidingen-en-werkwoordstijden-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag: bestaan beide delen zelf als woord (samenstelling), of is er een "
                   "voor- of achtervoegsel aan vast gezet (afleiding)?",
            waarom=[
                "Let op vriendelijk en werker: -elijk en -er bestaan niet als woord, dus zijn het "
                "afleidingen. Bij boekenkast en zonnebloem staan er twee echte woorden.",
            ],
        ),
        dict(
            aanpak="Splits van buiten naar binnen: eerst het voorvoegsel eraf, dan de achtervoegsels, "
                   "en wat overblijft is het grondwoord.",
            waarom=[
                "Let op de orde van de achtervoegsels: eerst -baar, dan -heid. Elk achtervoegsel "
                "verandert de woordsoort, en dat is waarom die orde telt.",
                "Noem dat er zowel een voorvoegsel als achtervoegsels in zitten. Zo'n woord heet een "
                "afleiding met meerdere lagen.",
            ],
        ),
        dict(
            aanpak="Meervouden en verkleinwoorden volgen de klank. Zeg het woord hardop, dan hoor je "
                   "welke uitgang past.",
            waarom=[
                "Let op kinderen en auto's: het eerste krijgt een onregelmatig -eren, het tweede een "
                "apostrof omdat het op een losse klinker eindigt.",
                "Let op bloempje: na een m komt -pje, want bloemje is niet te zeggen. De klank voor de "
                "uitgang beslist tussen -je, -tje, -pje en -kje.",
            ],
        ),
        dict(
            aanpak="Elke tijd heeft twee vragen: is ze voltooid of onvoltooid, en speelt ze in het "
                   "verleden, het heden of de toekomst. Die twee samen geven de naam.",
            waarom=[
                "Let op het verschil tussen had gewerkt en heeft gewerkt: het hulpwerkwoord staat in de "
                "verleden of de tegenwoordige tijd, en dat beslist de naam.",
                "Let erop dat loop! geen tijd is maar een wijs. De gebiedende wijs staat buiten het "
                "rijtje van de acht tijden.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: de woorden verbuiging en vervoeging, "
                   "onregelmatige werkwoorden, en de meervouden.",
            waarom=[
                "Niet waar, en het staat omgekeerd: vervoegen doe je met werkwoorden, verbuigen met "
                "naamwoorden. Die twee woorden worden vaak verwisseld.",
                "Niet waar: zijn is het meest onregelmatige werkwoord van de taal. Ben, bent, is, was, "
                "waren en geweest komen van verschillende stammen.",
                "Waar: bij een scheidbaar werkwoord gaat het eerste deel naar achteren, zoals ik sta "
                "om zeven uur op. Dat is de reden dat je de persoonsvorm soms ver van de rest vindt.",
                "Niet waar: er zijn ook meervouden op -eren en op -a, zoals kinderen, eieren en musea. "
                "En sommige woorden veranderen van klank, zoals stad en steden.",
            ],
        ),
        dict(
            aanpak="Twee open vragen: één over de vorm en één over het effect. Noem bij de eerste "
                   "zowel sterk als zwak.",
            waarom=[
                "Noem beide delen: de klankverandering bij sterke werkwoorden, en de laatste klank van "
                "de stam bij zwakke. Het rijtje van 't kofschip hoort bij dat tweede.",
                "Noem dat de tijd de lezer helpt plaatsen. Het gaat dus niet om afwisseling voor de "
                "sier maar om duidelijkheid.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-zinsontleding-en-zinsbouw-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek altijd eerst de persoonsvorm, dan het onderwerp met wie of wat plus die "
                   "persoonsvorm. De rest van de zinsdelen volgt daarna.",
            waarom=[
                "Let op het meewerkend voorwerp: het antwoordt op aan wie of voor wie. Staat er aan "
                "voor, dan is het meteen duidelijk; zonder dat woordje moet je het zelf aanvullen.",
                "Let op het handelend voorwerp: dat komt enkel in een lijdende zin voor en begint met "
                "door. In de bedrijvende zin zou die postbode het onderwerp zijn.",
            ],
        ),
        dict(
            aanpak="Elk zinsdeel heeft zijn eigen vraag. Leer die vragen, dan hoef je niet te gokken.",
            waarom=[
                "Let erop dat je bij het onderwerp de persoonsvorm in je vraag meeneemt. Zonder dat "
                "kom je bij een lijdend voorwerp uit.",
            ],
        ),
        dict(
            aanpak="Tel de persoonsvormen: één betekent enkelvoudig, meer dan één betekent "
                   "samengesteld. Kijk dan naar het verbindingswoord om neven- of onderschikking te "
                   "zien.",
            waarom=[
                "Let op het verbindingswoord: en, maar en want schikken naast elkaar, omdat, als en "
                "dat schikken onder. Bij onderschikking staat de persoonsvorm van de bijzin achteraan.",
            ],
        ),
        dict(
            aanpak="Drie vragen over de volgorde. Geef bij de eerste een eigen voorbeeld, zoals "
                   "gevraagd.",
            waarom=[
                "Noem beide zinnen, met en zonder de bepaling vooraan. Zo zie je de omkering, en dat "
                "is wat inversie betekent.",
                "Noem het werkgeheugen van de lezer. Daar zit de reden, en het is ook waarom je bij "
                "nalezen lange tangconstructies opsplitst.",
                "Noem beide uitersten: te korte en te lange zinnen. Variatie is dus geen sier maar "
                "leesbaarheid.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: waar de persoonsvorm staat, welke zinsdelen "
                   "verplicht zijn, en waaruit het gezegde bestaat.",
            waarom=[
                None,
                "Niet waar: veel werkwoorden hebben er geen, zoals slapen of vallen. Een onderwerp en "
                "een persoonsvorm zijn de enige die altijd nodig zijn.",
                "Niet waar: er kunnen ook deelwoorden en infinitieven bij horen, zoals in hij heeft "
                "willen komen. Alles wat werkwoord is, hoort bij het gezegde.",
                "Waar: zoals gisteren of ik. Een zinsdeel wordt bepaald door zijn rol en niet door "
                "zijn lengte.",
                "Niet waar: een uitroepende zin eindigt met een uitroepteken. Een vraagteken hoort bij "
                "een vragende zin.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-semantiek-betekenisrelaties-gevoelswaarde-en-herkomst-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vijf relaties met vijf vragen: hetzelfde, het tegengestelde, dezelfde vorm met een "
                   "andere betekenis, de bovenliggende groep, of een voorbeeld uit die groep.",
            waarom=[
                "Let op de homoniemen: dezelfde vorm, twee betekenissen die niets met elkaar te maken "
                "hebben. Bij een bank om op te zitten en een bank voor je geld is er geen verband.",
                "Let op het verschil tussen hyperoniem en hyponiem: hyper is boven, hypo is onder. "
                "Meubel staat boven stoel, appel staat onder fruit.",
            ],
        ),
        dict(
            aanpak="Bij een contaminatie zijn twee uitdrukkingen door elkaar geschoven. Zoek de twee "
                   "die erin zitten, en kies er dan één.",
            waarom=[
                "Let erop dat je ook de juiste vorm moet geven. Uitprinten is printen of uitdraaien, "
                "en duur kosten is veel kosten of duur zijn.",
                "Noem van beide een voorbeeld, zoals gevraagd. Een pleonasme voegt een eigenschap toe "
                "die er al in zit, een tautologie herhaalt het hele woord met een ander woord.",
            ],
        ),
        dict(
            aanpak="Hou twee lagen apart: de denotatie is de kale betekenis, de connotatie is de "
                   "bijklank. Bij een woordkeuze gaat het bijna altijd over die tweede.",
            waarom=[
                "Noem beide lagen met hun naam. Dat de bijklank het oordeel stuurt nog voor de rest "
                "van de zin gelezen is, verbindt dit met framing.",
                "Let op herstructurering: dat is een eufemisme voor ontslagen. Zulke woorden komen "
                "vooral uit de taal van bedrijven en de politiek.",
                "Noem dat ze elkaars tegenpool zijn. Een dysfemisme is dus niet gewoon een grof woord "
                "maar een bewuste keuze om harder te klinken.",
            ],
        ),
        dict(
            aanpak="Zes begrippen over waar een woord vandaan komt. Let op de uitgangen: -isme wijst "
                   "op een invloed van buiten, neo op iets nieuws.",
            waarom=[
                "Let op het verschil tussen een anglicisme en een belgicisme: het eerste komt uit het "
                "Engels, het tweede bestaat enkel bij ons. Een bureelstoel is een belgicisme.",
                "Let op een purisme: dat is een zelfgemaakt woord om een leenwoord te vermijden, zoals "
                "beeldbrief voor foto. De meeste purismen hebben het nooit gehaald.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: of synoniemen echt uitwisselbaar zijn, of een "
                   "pleonasme fout is, en wat een bastaardwoord is.",
            waarom=[
                "Niet waar: de connotatie en het register verschillen vaak. Sterven, heengaan en de "
                "pijp uitgaan betekenen hetzelfde en passen in heel andere teksten.",
                "Niet waar: soms is het bewust, voor nadruk of ritme. In een goede tekst is het een "
                "keuze, in een slordige tekst een vergetelheid.",
                "Niet waar, en het is net omgekeerd: een bastaardwoord komt uit een andere taal en is "
                "aan onze spelling aangepast, zoals bureau of fabriek.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-schrijven-en-schriftelijke-interactie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elke opdracht af wat de lezer erna moet hebben: iets weten, iets "
                   "kunnen, jouw mening kennen, overtuigd zijn, of iets gevoeld hebben.",
            waarom=[
                "Let op het verschil tussen informatie geven en iets uitleggen: een brochure zegt wat "
                "er is, een stappenplan leert je iets doen.",
                "Let op de flyer: daar ligt de nadruk op de vorm en de aantrekkingskracht, dus op "
                "creatief zijn met taal. Overtuigen zit erin, maar de vorm doet het werk.",
            ],
        ),
        dict(
            aanpak="Zes criteria. Vraag je bij elke opmerking af waarover ze gaat: de opdracht, de "
                   "woorden, de zinnen, de toon, de spelling of de opbouw.",
            waarom=[
                "Let op taakvoltooiing: dat is het zwaarste criterium. Een prachtige tekst over het "
                "verkeerde onderwerp haalt het niet.",
                "Let erop dat register een apart criterium is. Een correcte tekst in de verkeerde toon "
                "verliest punten, en dat gaat over beleefdheid en niet over fouten.",
            ],
        ),
        dict(
            aanpak="Plan voor je schrijft. Drie vragen vooraf en een paar strategieën onderweg sparen "
                   "achteraf veel herschrijfwerk.",
            waarom=[
                "Noem alle drie en noem dat het de vragen van het communicatiemodel zijn. Zo zie je "
                "dat die theorie hier praktisch wordt.",
                "Noem drie strategieën, zoals gevraagd. Een schrijfplan met kernwoorden is de "
                "eenvoudigste en helpt het meest.",
                "Noem allebei: de fouten die een spellingcontrole niet vindt, en wat ze helemaal niet "
                "beoordeelt. Word in plaats van wordt is het klassieke voorbeeld.",
            ],
        ),
        dict(
            aanpak="Bij een formele mail staan vier dingen vast: het onderwerp, de aanspreking, de "
                   "inleiding met de feiten, en de slotgroet met je volledige naam.",
            waarom=[
                "Let erop dat je onderwerpregel kort en concreet is. Geachte mevrouw, meneer is de "
                "aanspreking als je niet weet wie het leest.",
                "Noem eerst de feiten en pas daarna je vraag, zoals het antwoord doet. Een datum en "
                "een bestelnummer maken een klacht meteen behandelbaar.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: of spelling apart telt, of één goed criterium "
                   "genoeg is, en wat er van je woordenschat verwacht wordt.",
            waarom=[
                None,
                "Niet waar: de criteria worden elk apart beoordeeld. Je doel bereiken is belangrijk en "
                "het dekt de spelling en de zinsbouw niet.",
                "Niet waar: men verwacht woorden die bij het onderwerp en het register passen. Dat "
                "betekent soms juist een precies, minder alledaags woord.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-spreken-en-gesprekken-voeren-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag: kan de ander het zien of horen (spreken), staat het op papier "
                   "(schrijven), of geldt het voor beide?",
            waarom=[
                "Let op taakvoltooiing: dat geldt bij allebei. Antwoorden op de gestelde opdracht is "
                "altijd het eerste criterium.",
                "Let erop dat register bij beide hoort. Je kiest je toon zowel in een mail als in een "
                "gesprek, en in beide gevallen beslist de verhouding.",
            ],
        ),
        dict(
            aanpak="Hou drie dingen apart aan je stem en je lichaam: de klanken (uitspraak), de "
                   "melodie (intonatie), en alles wat je laat zien (lichaamstaal).",
            waarom=[
                "Let op het verschil tussen uitspraak en intonatie: de eerste gaat over losse klanken, "
                "de tweede over de lijn van je zin. Een vraag hoor je aan de intonatie.",
                "Let erop dat een spreekplan met kernwoorden werkt en niet met volle zinnen. Wie zijn "
                "tekst voorleest, kijkt niemand aan.",
                None,
            ],
        ),
        dict(
            aanpak="Vier situaties die echt gebeuren. Bij elk is het antwoord hetzelfde soort: doe iets "
                   "zichtbaar, en doe niet alsof er niets aan de hand is.",
            waarom=[
                "Noem allebei, zoals gevraagd: wat je doet en wat je zeker niet doet. Sneller praten "
                "is de reflex, en juist de verkeerde.",
                "Noem drie strategieën, zoals gevraagd. Samenvatten wat je wel begreep, is de sterkste "
                "van de drie: de ander kan dan zelf aanvullen.",
                "Noem dat een korte denkpauze mag. Stilte voelt langer aan voor jou dan voor je "
                "gesprekspartner.",
                "Noem alle drie de stappen: bedanken, samenvatten en een afscheidsformule. Dat "
                "samenvatten is wat een afsluiting afrondt.",
            ],
        ),
        dict(
            aanpak="Een leeservaring is geen samenvatting. Noem wat het boek bij je deed en hang dat "
                   "op aan iets concreets uit het boek.",
            waarom=[
                "Let erop dat je je reactie onderbouwt met een personage, een scène of de "
                "verteltrant. Zonder dat anker klinkt elke leeservaring hetzelfde.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: wat vlotheid is, wat pauzes doen, en waar "
                   "beleefdheid geldt.",
            waarom=[
                "Niet waar: vlotheid is zonder haperen spreken, niet snel spreken. Te snel praten "
                "maakt je juist moeilijker te volgen.",
                None,
                None,
                "Niet waar: doorvragen en voortbouwen op wat de ander zegt, is precies wat het "
                "hoogste niveau van interactie kenmerkt. Enkel antwoorden blijft op het laagste "
                "niveau.",
                "Niet waar: ook in een gesprek gelden conventies, zoals iemand laten uitspreken en de "
                "juiste aanspreking kiezen.",
            ],
        ),
    ],
)
