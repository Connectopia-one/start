"""Motivatie en attributies — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_motivatie: intrinsieke en extrinsieke
motivatie, vermijdings- en toenaderingsgedrag, en attributies, intern of
extern en controleerbaar of niet. Met een zelfgetekend kruisschema."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, LICHTGROEN

KS = Prent("kruisschema-attributies", "Een kruisschema voor attributies", "een tabel met twee rijen (intern, extern) en twee kolommen (controleerbaar, niet controleerbaar), vakken A tot D")
KS.tekst(470, 100, "controleerbaar", 24, vet=True); KS.tekst(770, 100, "niet controleerbaar", 24, vet=True)
KS.tekst(200, 245, "intern", 24, "end", vet=True); KS.tekst(200, 485, "extern", 24, "end", vet=True)
VAK = {"A": (320, 130), "B": (620, 130), "C": (320, 370), "D": (620, 370)}
for t, (x, y) in VAK.items():
    KS.rect(x, y, 300, 240, "#eef3e6" if t in "AD" else "#ffffff", DONKER, 0, 3)
    KS.letter(x + 150, y + 120, t)
U = "kruisschema-attributies.svg"
Z = {t: [Prent.zone(x, y, 300, 240)] for t, (x, y) in VAK.items()}

RAPPORT = ("Lees het gesprek na het rapport.\n\n"
           "Ilias: « Ik had een 9 op 20 voor geschiedenis. Ik heb er gewoon geen aanleg voor. »\n"
           "Marie: « Ik had ook een 9. Ik ben pas de avond ervoor beginnen leren. Volgende keer plan ik beter. »\n"
           "Ilias: « Ik studeer trouwens alleen omdat mijn ouders me anders geen gsm meer geven. »")

VRAGEN = [
    klik("Bekijk het kruisschema. In welk vak hoort de verklaring 'ik heb te weinig gestudeerd'?", U, Z["A"], "De oorzaak ligt bij jou en je kan ze sturen."),
    klik("In welk vak hoort de verklaring 'ik heb er geen aanleg voor'?", U, Z["B"], "Aanleg ligt bij jou, maar je kan ze niet sturen."),
    klik("In welk vak hoort de verklaring 'ik had gewoon pech met de vragen'?", U, Z["D"], "Buiten jezelf en niet te sturen."),
    casus(RAPPORT, [
        sorteer("Welke attributie geeft deze leerling?", ["intern en controleerbaar", "intern en niet controleerbaar"],
                [("Ilias", "intern en niet controleerbaar"), ("Marie", "intern en controleerbaar")],
                "Allebei intern, maar alleen Marie kan iets veranderen."),
        mk("Wie heeft de meeste kans om het volgende keer beter te doen?",
           ["Marie, want ze wijst op iets wat ze kan sturen", "Ilias, want hij kent zijn grenzen al heel goed", "allebei evenveel, want ze hadden hetzelfde cijfer", "niemand, want attributies hebben geen invloed"],
           0, "Intern en controleerbaar geeft de meeste hoop op verbetering."),
        keuze("Ilias studeert voor de gsm. Dat is [[*extrinsieke|intrinsieke]] motivatie.", "De drijfveer komt van buiten."),
        keuze("Als Ilias blijft zeggen dat hij geen aanleg heeft, bouwt hij een [[*negatief zelfbeeld|realistisch zelfbeeld|hoge self-efficacy]] op.", "Attributies voeden je zelfbeeld."),
    ]),
    sorteer("Intrinsiek of extrinsiek?", ["intrinsiek", "extrinsiek"],
            [("Ze tekent omdat ze het heerlijk vindt.", "intrinsiek"), ("Hij poetst de auto voor tien euro.", "extrinsiek"), ("Ze leest een boek omdat het verhaal haar boeit.", "intrinsiek"), ("Hij leert om een goed rapport te halen.", "extrinsiek")],
            "Van binnenuit of van buitenaf."),
    sorteer("Welk doelgericht gedrag?", ["passief vermijden", "actief vermijden", "nastreven", "behouden"],
            [("Voor de toets ruimt hij plots zijn hele kamer op.", "actief vermijden"), ("Ze stelt haar taak uit en doet niets.", "passief vermijden"), ("Hij solliciteert voor een job die hij nog niet heeft.", "nastreven"), ("Ze traint om haar plaats in de ploeg te houden.", "behouden")],
            "Vermijdingsgedrag tegenover toenaderingsgedrag."),
    tabel("Klopt dit over motivatie?",
          [("Extrinsieke motivatie is altijd slecht.", F), ("Een beloning kan de intrinsieke motivatie verzwakken.", J), ("Intrinsieke motivatie houdt langer stand.", J), ("Attributies staan los van motivatie.", F)],
          "Soms is extrinsieke motivatie nodig om te starten."),
    mk("Waarom werkt straf op lange termijn minder goed dan een beloning?",
       ["straf zegt niet wat wel mag", "omdat straf nooit gedrag kan stoppen", "omdat een beloning altijd geld moet zijn", "omdat straf de intrinsieke motivatie verhoogt"],
       0, "Straf stopt gedrag, maar toont niet welk gedrag gewenst is."),
    keuze("Een leerling doet niets aan zijn taak, zodat hij zijn mislukking kan wijten aan 'niet geprobeerd'. Dat is [[*vermijdingsgedrag|toenaderingsgedrag|intrinsieke motivatie]] uit angst om te falen.", "Door niets te doen, kan hij de mislukking afwenden."),
    koppel("Koppel het begrip over motivatie aan de uitleg.",
           [("motivatie", "wat je in beweging zet"), ("attributie", "de verklaring die je geeft voor slagen of falen"), ("toenaderingsgedrag", "op een doel afgaan"), ("vermijdingsgedrag", "iets uit de weg gaan")],
           ["wat je lichaam doet bij schrik"], "Motivatie en attributies horen samen."),
    mk("Een leerling slaagt en zegt dat de toets makkelijk was. Wat gebeurt er met zijn self-efficacy?",
       ["ze groeit niet", "ze groeit sterk, want hij is geslaagd", "ze verandert in intrinsieke motivatie", "ze daalt altijd tot nul"],
       0, "Wie zijn succes niet aan zichzelf toeschrijft, leert er niet uit dat hij het kan."),
    keuze("Wie iets mag [[*kiezen|vermijden|uitstellen]] en snapt waarom het nuttig is, doet het liever: zo voed je de intrinsieke motivatie.", "Keuze en zin geven."),
    tabel("Is deze verklaring controleerbaar?",
          [("hoeveel je oefent", J), ("hoe je je voorbereidt", J), ("je aanleg", F), ("pech met de vragen", F)],
          "Inzet en aanpak kan je sturen."),
    keuze("Wie alle mislukkingen altijd extern verklaart, [[*hoeft nooit iets te veranderen|leert er het meest uit|wordt vanzelf intrinsiek gemotiveerd]].", "Dan blijft het resultaat hetzelfde."),
    inv("Een meisje leert sterrenbeelden omdat ze de sterren zo boeiend vindt. Welke motivatie is dat? Eén woord.", ["intrinsiek", "intrinsieke", "intrinsieke motivatie"], "Ze doet het om het plezier zelf."),
    mk("Hoe helpt een leerkracht een leerling die zegt 'ik ben gewoon dom'?",
       ["wijzen op wat hij wel kan sturen", "zeggen dat hij gelijk heeft en het opgeven", "hem een makkelijkere toets geven dan de anderen", "hem straffen omdat hij zo negatief is"],
       0, "De aandacht verleggen naar inzet en aanpak."),
    keuze("Toenaderingsgedrag heeft twee vormen: nastreven wat je niet hebt en [[*behouden wat je wel hebt|vermijden wat je vreest|uitstellen wat moet]].", "Beide zijn op een doel gericht."),
    tabel("Is deze attributie extern?",
          [("De leerkracht was streng.", J), ("Ik had te weinig geslapen omdat ik gamede.", F), ("De toets was oneerlijk.", J), ("Ik had pech.", J)],
          "Extern legt de oorzaak buiten jezelf."),
    sleep("Een attributie kan [[intern]] of extern zijn, en [[controleerbaar]] of niet. De gunstigste is intern en controleerbaar, want die laat [[verbetering]] toe.",
          ["extrinsiek", "aanleg"], "Zo bepaalt een attributie of je opnieuw probeert."),
    keuze("Twee leerlingen met hetzelfde cijfer kunnen het [[*heel anders|altijd hetzelfde]] verklaren.", "De een zegt pech, de ander te weinig geoefend."),
    keuze("Iemand die betaald wordt voor iets wat hij graag deed, gaat het soms minder graag doen. De beloning kan de [[*intrinsieke|extrinsieke]] motivatie verzwakken.", "Het plezier verschuift naar de beloning."),
    keuze("Motivatie is de drijfveer achter gedrag: waarom je iets [[*begint en volhoudt|vergeet|onderdrukt]].", "Wat je in beweging zet."),
    tabel("Is dit toenaderingsgedrag?",
          [("een diploma nastreven", J), ("je vriendschap onderhouden", J), ("een toets ontwijken door ziek te melden", F), ("je rijbewijs halen", J)],
          "Toenaderen is op een doel afgaan."),
    mk("Op het examen lees je hoe iemand een mislukking verklaart. Wat moet je dan doen?",
       ["benoemen welke het is en wat ze doet", "enkel zeggen of de leerling geslaagd is", "het cijfer van de toets herberekenen", "de leerling een betere attributie laten kiezen"],
       0, "Welke attributie het is, en wat ze doet met de motivatie."),
    keuze("Een leerling zegt: 'Ik slaagde omdat ik hard studeerde.' Die attributie is intern en [[*controleerbaar|niet controleerbaar|extern]].", "De oorzaak ligt bij hem en hij kan ze sturen."),
    keuze("Een externe attributie [[*klopt af en toe|klopt nooit]]: soms is een toets echt oneerlijk.", "Maar wie altijd extern verklaart, leert niets bij."),
    open_("Een leerling faalt voor een toets. Geef een ongunstige en een gunstige attributie en leg uit wat elk doet met de motivatie.",
          "Ongunstig: 'ik ben er gewoon niet goed in' (intern, niet controleerbaar). Hij ziet geen reden om opnieuw te proberen en zijn motivatie zakt. Gunstig: 'ik ben te laat begonnen met leren' (intern, controleerbaar). Hij weet wat hij kan veranderen en gaat volgende keer vroeger beginnen."),
]
