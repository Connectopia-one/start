"""Politieke filosofie: individu, gemeenschap en legitimiteit — pittig
(🌍 Beyond doorstroom, kunstbeschouwing en filosofie). Strikt binnen
beyond/bron/kfb_polfil1.py: liberalisme (Locke), socialisme (Marx),
egalitair liberalisme (Rawls), communitarisme (Sandel, Taylor, MacIntyre),
Locke en Rousseau, en legitimiteit bij Aristoteles, Hobbes en Schmitt."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, BLAUW, ORANJE, GEEL

# Prent: tijdlijn van politieke denkers -------------------------------------------------
TD = Prent("tijdlijn-politieke-denkers", "Politieke denkers op een tijdlijn",
           "een tijdlijn van 1600 tot 2000 met zes punten A tot F, bij 1651, 1690, 1762, 1848, 1922 en 1971")
X0, X1, J0, J1 = 80, 920, 1600, 2000


def xj(jaar):
    return X0 + (jaar - J0) / (J1 - J0) * (X1 - X0)


TD.pijl(X0 - 20, 340, X1 + 30, 340, DONKER, 4)
for jaar in range(1600, 2001, 50):
    TD.lijn(xj(jaar), 328, xj(jaar), 352, DONKER, 2)
    TD.tekst(xj(jaar), 385, str(jaar), 16)
PUNT = {}
for i, (letter, jaar) in enumerate((("A", 1651), ("B", 1690), ("C", 1762), ("D", 1848), ("E", 1922), ("F", 1971))):
    y = 230 if i % 2 == 0 else 160
    TD.lijn(xj(jaar), 340, xj(jaar), y + 20, DONKER, 2)
    TD.letter(xj(jaar), y, letter)
    TD.tekst(xj(jaar), 420 + (i % 2) * 26, str(jaar), 15, kleur=ORANJE, vet=True)
    PUNT[letter] = (xj(jaar), y)


def tz(l):
    x, y = PUNT[l]
    return [Prent.rond(x, y, 36)]


VRAGEN = [
    klik("Hobbes schreef Leviathan tijdens de Engelse burgeroorlog. Klik op dat jaar.", TD.bestand, tz("A"),
         "Leviathan verscheen in 1651."),
    klik("Klik op het jaar van het Communistisch Manifest van Marx en Engels.", TD.bestand, tz("D"),
         "Het Communistisch Manifest verscheen in 1848, in de tijd van de industriële revolutie."),
    klik("Klik op het jaar waarin Rawls A Theory of Justice schreef.", TD.bestand, tz("F"),
         "Rawls schreef het in 1971 in de Verenigde Staten. Het communitarisme reageerde er in de jaren 1980 op."),
    met_prent(TD.bestand, keuze("Punt B past bij [[*Locke|Schmitt|Rawls]], de grondlegger van het liberalisme. Punt E past bij [[*Schmitt|Rousseau|Hobbes]], een Duitse rechtsgeleerde uit de 20ste eeuw.",
              "Locke schreef in de 17de eeuw in Engeland, Schmitt in de 20ste eeuw in Duitsland.")),
    met_prent(TD.bestand, keuze("Rousseau, die schreef over de algemene wil, past bij punt [[*C|A|E]]. Aristoteles staat niet op deze tijdlijn, want hij leefde [[*in de 4de eeuw voor Christus|in de 19de eeuw|na Rawls]].",
              "Rousseau schreef Het sociaal contract in 1762.")),
    sorteer("Bij welke ideologie past deze uitspraak?", ["liberalisme", "egalitair liberalisme", "socialisme", "communitarisme"], [
        ["De staat moet vooral de vrijheid en het eigendom van het individu beschermen.", "liberalisme"],
        ["Vrijheid, maar ook eerlijke kansen voor wie arm geboren wordt.", "egalitair liberalisme"],
        ["De ongelijkheid tussen klassen moet weg.", "socialisme"],
        ["Het individu wordt gevormd door zijn gemeenschap en haar tradities.", "communitarisme"],
        ["Een beperkte staat, met natuurlijke rechten op leven, vrijheid en eigendom.", "liberalisme"],
        ["Gedeelde waarden geven mensen hun identiteit.", "communitarisme"],
    ], "Vier ideologieën met een ander antwoord op de vraag: individu of gemeenschap?"),
    koppel("Koppel de ideologie aan haar grondlegger of bekende denker.", [
        ["liberalisme", "John Locke"],
        ["socialisme", "Karl Marx"],
        ["egalitair liberalisme", "John Rawls"],
        ["communitarisme", "Michael Sandel"],
    ], ["Carl Schmitt"], "Schmitt hoort bij het thema legitimiteit, niet bij een van deze vier ideologieën."),
    tabel("Klopt dit over Locke en Rousseau?", [
        ("Locke ziet de mens in de natuurtoestand als vrij en gelijk.", J),
        ("Rousseau legt meer nadruk op de gemeenschap dan Locke.", J),
        ("De algemene wil is bij Rousseau de optelsom van alle eigenbelangen.", F),
        ("Volgens Locke mag het volk nooit in verzet komen tegen de regering.", F),
    ], "De algemene wil is gericht op het algemeen belang. Locke aanvaardt verzet als de regering de natuurlijke rechten schendt."),
    casus(
        "Een gemeente wil een oud park omvormen tot een parking. Een winkelier wil meer klanten en vindt dat elke eigenaar zelf moet kunnen beslissen. "
        "Buurtbewoners zeggen dat het park al honderd jaar het hart van de buurt is, waar feesten en markten plaatsvinden.",
        [
            tabel("Wie legt hier de nadruk op het individu en wie op de gemeenschap?", [
                ("de winkelier die zelf wil beslissen", "individu"),
                ("de buurtbewoners met hun feesten en markten", "gemeenschap"),
                ("een eigenaar die zijn grond vrij wil verkopen", "individu"),
            ], "In het politiek debat botsen eigen belang en gedeeld belang vaak.",
               kolommen=["individu", "gemeenschap"]),
            mk("Bij welke ideologie past de houding van de buurtbewoners het best?",
               ["communitarisme", "klassiek liberalisme", "egalitair liberalisme", "absolutisme"], 0,
               "Gedeelde tradities en de gemeenschap staan centraal."),
            keuze("De winkelier zou steun vinden bij [[*Locke|Rousseau|Sandel]], die de rechten van het individu, zoals eigendom, voorop stelt. De buurt zou eerder verwijzen naar de [[*algemene wil|oorlog van allen tegen allen|uitzonderingstoestand]] van Rousseau.",
                  "Locke staat voor het individu, Rousseau voor het algemeen belang."),
        ],
    ),
    sorteer("Welke denker past bij deze visie op legitimiteit?", ["Aristoteles", "Hobbes", "Schmitt"], [
        ["Een bestuur is goed als het het algemeen belang dient.", "Aristoteles"],
        ["Mensen staan hun vrijheid af aan een vorst in ruil voor veiligheid.", "Hobbes"],
        ["Soeverein is wie beslist over de uitzonderingstoestand.", "Schmitt"],
        ["De mens is van nature een politiek dier.", "Aristoteles"],
        ["Zonder staat is het leven eenzaam, arm, gemeen, wreed en kort.", "Hobbes"],
        ["Het politieke draait om het onderscheid tussen vriend en vijand.", "Schmitt"],
    ], "Drie denkers uit drie tijden over wat macht terecht maakt."),
    tabel("Goede of ontaarde vorm van bestuur volgens Aristoteles?", [
        ("koningschap", "goed"),
        ("tirannie", "ontaard"),
        ("aristocratie", "goed"),
        ("oligarchie", "ontaard"),
    ], "Een goede vorm dient het algemeen belang, een ontaarde vorm het eigenbelang van de heersers.",
       kolommen=["goed", "ontaard"]),
    mk("Een leger neemt de macht over. Burgers gehoorzamen enkel uit angst. Wat ontbreekt hier volgens de meeste filosofen?",
       ["legitimiteit", "macht van het leger", "een sterk leger", "geweld op straat"], 0,
       "Er is wel macht, maar geen aanvaarding of goede grond: geen legitieme macht."),
    keuze("Hobbes beschrijft de sterke staat in het boek [[*Leviathan|Politica|Het sociaal contract]], genoemd naar een [[*zeemonster|Griekse god|Romeinse keizer]].",
          "Leviathan verscheen in 1651."),
    mk("Waarom zeggen communitaristen dat het individu bij Rawls te los staat?",
       ["het kiest zonder zijn gemeenschap te kennen", "Rawls wil dat iedereen alleen op een eiland gaat wonen",
        "Rawls vindt dat mensen geen rechten mogen hebben", "Rawls schreef enkel over dieren en machines"], 0,
       "Achter de sluier van onwetendheid ken je je plaats en gemeenschap niet. Communitaristen vinden dat te abstract."),
    tabel("Klopt dit over Hobbes en Schmitt?", [
        ("Allebei geven ze een sterke staat veel macht.", J),
        ("Allebei leggen ze de nadruk op orde en veiligheid.", J),
        ("Allebei leefden ze in de klassieke oudheid.", F),
    ], "Hobbes leefde in de 17de eeuw, Schmitt in de 20ste eeuw."),
    sleep("Voor Hobbes is de macht legitiem omdat ze [[veiligheid]] brengt. Voor Aristoteles is een bestuur goed als het het [[algemeen]] belang dient.",
          ["vriend", "eigen"], "Twee verschillende gronden voor legitimiteit."),
    mk("Een regering roept de noodtoestand uit en schort rechten op. Iemand zegt: 'Nu zie je wie echt de macht heeft.' Bij wie past dit?",
       ["Schmitt", "Aristoteles", "Locke", "Sandel"], 0,
       "Voor Schmitt toont de uitzonderingstoestand wie de soeverein is."),
    inv("Hoe heet bij Rousseau de wil van de burgers samen, gericht op het algemeen belang? De ... wil", ["algemene"],
        "Die is meer dan de som van de eigenbelangen."),
    inv("Hoe heet bij Aristoteles de mens als wezen dat van nature in een gemeenschap leeft? Zoön ...", ["politikon"],
        "Zoön politikon betekent politiek dier."),
    mk("Welke ideologie ontstond als reactie op de harde omstandigheden van arbeiders tijdens de industriële revolutie?",
       ["socialisme", "communitarisme", "liberalisme", "egalitair liberalisme"], 0,
       "Lange werkdagen, kinderarbeid en armoede leidden tot de vraag naar meer gelijkheid."),
    keuze("Een macht is legitiem als burgers ze als [[*terecht en aanvaardbaar|sterk en angstaanjagend|rijk en oud]] zien. Dan volgen ze de regels ook zonder [[*dwang|wetten|verkiezingen]].",
          "Zonder legitimiteit moet een macht steeds meer geweld gebruiken."),
    volgorde("Zet deze ideologieën in de volgorde waarin ze ontstonden.", [
        "liberalisme", "socialisme", "egalitair liberalisme", "communitarisme",
    ], "Locke in de 17de eeuw, Marx in de 19de eeuw, Rawls in 1971, de communitaristen in de jaren 1980."),
    mk("Een partij zegt: 'De sterkste schouders dragen de zwaarste lasten, zodat ook wie arm geboren wordt eerlijke kansen krijgt, maar iedereen blijft vrij.' Welke ideologie?",
       ["egalitair liberalisme", "klassiek liberalisme", "communitarisme", "absolutisme van Hobbes"], 0,
       "Vrijheid en eerlijke kansen samen passen bij het egalitair liberalisme."),
    tabel("Plaats de denker in tijd en ruimte.", [
        ("Aristoteles", "oud-Griekenland"),
        ("Hobbes", "Engeland, 17de eeuw"),
        ("Schmitt", "Duitsland, 20ste eeuw"),
    ], "Aristoteles in de 4de eeuw voor Christus, Hobbes tijdens de Engelse burgeroorlog, Schmitt in Duitsland in de 20ste eeuw.",
       kolommen=["oud-Griekenland", "Engeland, 17de eeuw", "Duitsland, 20ste eeuw"]),
    keuze("Voor Aristoteles is de staat iets [[*natuurlijks|kunstmatigs|toevalligs]], want de mens is een politiek dier. Voor Hobbes is de staat eerder een [[*kunstmatig contract|natuurlijke familie|goddelijk geschenk]].",
          "Bij Hobbes ontstaat de staat pas door een afspraak om de natuurtoestand te verlaten."),
    mk("Welke uitspraak past bij het klassieke liberalisme?",
       ["een beperkte staat die de vrijheid beschermt", "een staat die zich met alles van de burgers bemoeit",
        "de gemeenschap beslist over elke vrijheid", "alle fabrieken worden gemeenschappelijk bezit"], 0,
       "Het klassieke liberalisme wil het individu beschermen tegen een te sterke staat."),
    tabel("Klopt dit over legitimiteit?", [
        ("Een legitieme macht heeft gezag: mensen gehoorzamen niet enkel uit angst.", J),
        ("Voor Aristoteles is elk bestuur van één persoon automatisch slecht.", F),
        ("Voor Hobbes is de vorst legitiem zolang hij vrede en veiligheid brengt.", J),
    ], "Koningschap is voor Aristoteles een goede vorm, zolang de koning het algemeen belang dient."),
    open_("Vergelijk de visie van Locke en Rousseau op de verhouding tussen individu en gemeenschap.",
          "Locke vertrekt van het individu met natuurlijke rechten op leven, vrijheid en eigendom. De staat bestaat om die rechten te beschermen, en als hij dat niet doet, mag het volk in verzet komen. Rousseau legt meer nadruk op de gemeenschap: via het sociaal contract vormen de burgers samen de algemene wil, gericht op het algemeen belang. Bij Locke staat het individu voorop, bij Rousseau het volk als geheel."),
]
