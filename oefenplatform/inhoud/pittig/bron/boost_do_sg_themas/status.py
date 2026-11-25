"""Sociale status en kansen in de samenleving — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_status: de zes statusfactoren en de impact van
een sociale positie op kansen, met sociale overerving en sociale mobiliteit.
Met een zelfgetekende ladder over twee generaties."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, ORANJE

LD = Prent("ladder-twee-generaties", "Vier gezinnen op de maatschappelijke ladder", "vier ladders, telkens met een ouder (grijs) en een kind (blauw), letters A tot D")
LD.tekst(30, 120, "hoog", 20, "start"); LD.tekst(30, 500, "laag", 20, "start")
GEZIN = [("A", 1, 4), ("B", 4, 4), ("C", 4, 1), ("D", 1, 1)]
for i, (t, ouder, kind) in enumerate(GEZIN):
    x = 150 + i * 215
    LD.lijn(x, 90, x, 520, DONKER, 4); LD.lijn(x + 90, 90, x + 90, 520, DONKER, 4)
    for k in range(5):
        LD.lijn(x, 110 + k * 100, x + 90, 110 + k * 100, DONKER, 3)
    def y(n):
        return 510 - (n - 1) * 130
    LD.cirkel(x - 25, y(ouder) - 40, 13, GRIJS, DONKER, 2); LD.rect(x - 36, y(ouder) - 26, 22, 30, GRIJS, DONKER, 5, 2)
    LD.cirkel(x + 115, y(kind) - 40, 13, BLAUW, DONKER, 2); LD.rect(x + 104, y(kind) - 26, 22, 30, BLAUW, DONKER, 5, 2)
    LD.letter(x + 45, 575, t)
U = "ladder-twee-generaties.svg"
Z = {t: [Prent.zone(110 + i * 215, 60, 170, 540)] for i, (t, o, k) in enumerate(GEZIN)}

YASMINE = ("Lees het verhaal.\n\n"
           "Yasmine groeide op in een gezin waar niemand hoger onderwijs volgde. Thuis spraken ze een andere taal dan op school, en er was geen geld voor bijles. "
           "Dankzij een studiebeurs en een leerkracht die in haar geloofde, werd ze de eerste in haar familie met een masterdiploma. "
           "Haar eerste job vond ze via een stage, waar een collega haar aanraadde bij een andere werkgever.")

VRAGEN = [
    klik("Bekijk de vier gezinnen: grijs is de ouder, blauw het kind. Klik op het gezin met opwaartse mobiliteit.", U, Z["A"], "Het kind klimt hoger dan de ouder."),
    klik("Klik op het gezin met neerwaartse mobiliteit.", U, Z["C"], "Ook afzakken is mobiliteit."),
    klik("Klik op een gezin waar de positie van de ouder gewoon doorgegeven wordt.", U, Z["B"] + Z["D"], "Sociale overerving of reproductie: hoog of laag blijft hoog of laag."),
    casus(YASMINE, [
        sorteer("Was dit voor Yasmine een drempel of een hefboom?", ["drempel", "hefboom"],
                [("thuis een andere taal dan op school", "drempel"), ("geen geld voor bijles", "drempel"), ("een studiebeurs", "hefboom"), ("een leerkracht die in haar geloofde", "hefboom")],
                "Haar startpositie woog mee, maar kon bijgestuurd worden."),
        keuze("Yasmine is de eerste in haar familie met een masterdiploma. Dat is [[*opwaartse|neerwaartse]] mobiliteit.", "Ze klimt op de ladder."),
        keuze("Via de collega van haar stage vond ze werk. Dat is de statusfactor [[*kenniskring|afkomst|geslacht]].", "Veel jobs komen via iemand die iemand kent."),
        mk("Wat toont het verhaal van Yasmine over een sociale positie?",
           ["ze weegt mee, maar beslist niet alles", "ze bepaalt volledig hoe een leven verloopt", "ze speelt geen enkele rol bij onderwijs", "ze kan nooit veranderen binnen één leven"],
           0, "Eigen keuzes, toeval en beleid spelen ook mee."),
    ]),
    tabel("Is dit een van de zes statusfactoren?",
          [("afkomst", J), ("beroep", J), ("lichaamslengte", F), ("kenniskring", J), ("geslacht", J), ("opleiding", J)],
          "Zes factoren; inkomen en vermogen tellen samen als één."),
    sorteer("Eerder toegewezen of eerder verworven?", ["toegewezen", "verworven"],
            [("afkomst", "toegewezen"), ("opleiding", "verworven"), ("geslacht", "toegewezen"), ("beroep", "verworven"), ("inkomen", "verworven")],
            "Beroep, opleiding en inkomen bouw je op."),
    koppel("Koppel het begrip over sociale status aan de uitleg.",
           [("sociale status", "het aanzien van een positie"), ("sociale mobiliteit", "opklimmen of afzakken op de ladder"), ("sociale overerving", "de positie van ouders werkt door bij de kinderen"), ("kenniskring", "de mensen die je kent")],
           ["het geld dat je elke maand verdient"], "Status en kansen."),
    tabel("Klopt dit over sociale status?",
          [("Alle statusfactoren wegen overal even zwaar.", F), ("Sociale mobiliteit kan enkel naar boven gaan.", F), ("Een sociale positie werkt door in de gezondheid.", J), ("Status bestaat doordat anderen aanzien geven.", J)],
          "Het gewicht verschilt per samenleving en per tijd."),
    mk("Twee mensen doen hetzelfde werk, maar de ene verdient meer. Welke statusfactor verschilt?",
       ["het inkomen", "het beroep, want ze doen ander werk", "de afkomst, want die verandert elk jaar", "het geslacht, want dat bepaalt het loon altijd"],
       0, "Het beroep is gelijk, het verschil zit in wat ze verdienen."),
    keuze("Inkomen is wat er maandelijks binnenkomt, [[*vermogen|beroep|opleiding]] is wat er opgebouwd is.", "Daarom staan ze samen als één factor."),
    keuze("Een samenleving waarin de positie van je ouders je toekomst bepaalt, heeft [[*lage|hoge]] sociale mobiliteit.", "Hoe sterker de positie wordt doorgegeven, hoe lager."),
    tabel("Kan deze maatregel de sociale mobiliteit vergroten?",
          [("gratis onderwijs", J), ("een studiebeurs", J), ("een goed openbaar vervoer", J), ("hoger inschrijvingsgeld voor scholen", F)],
          "Hoe lager de drempel, hoe meer kansen."),
    mk("Een gemeente opent gratis huiswerkklassen in een arme wijk. Wat hoopt ze vooral?",
       ["dat school een zwakke start goedmaakt", "dat iedereen er hetzelfde diploma krijgt", "dat afkomst er geen rol meer speelt", "dat de ouders er meteen meer verdienen"],
       0, "Een diploma kan een moeilijke startpositie deels compenseren."),
    keuze("Wie in zijn sportclub veel aanzien heeft, heeft dat [[*niet automatisch|automatisch]] ook op het werk.", "Status hangt aan de groep."),
    sleep("Sociale [[status]] is het aanzien van een positie. Opklimmen of afzakken heet sociale [[mobiliteit]]. Het doorgeven van een positie heet sociale [[overerving]].",
          ["rol", "socialisatie"], "Drie begrippen over kansen."),
    keuze("Een leerling kiest een richting omdat zijn ouders dat ook deden. Hier speelt zijn [[*sociale positie|temperament|body-image]].", "De verwachtingen van de omgeving sturen de keuze."),
    inv("Hoeveel factoren bepalen de sociale status? Schrijf het getal.", ["6", "zes"], "Afkomst, beroep, geslacht, inkomen en vermogen, kenniskring, opleiding."),
    tabel("Werkt een sociale positie door op dit terrein?",
          [("onderwijs", J), ("werk", J), ("wonen", J), ("de kleur van je ogen", F)],
          "Onderwijs-, werk- en woonkansen."),
    mk("Sam en Lotte werken even hard op school, maar Lotte haalt toch een hoger diploma. Welke verklaring past bij de sociale wetenschappen?",
       ["hun startpositie verschilde", "Sam deed eigenlijk helemaal geen moeite", "inzet speelt nooit een rol bij een diploma", "kansen zijn voor iedereen altijd gelijk"],
       0, "Twee mensen met dezelfde inzet kunnen van een andere plek vertrekken."),
    keuze("Een familie staat al generaties bekend in de streek. Het aanzien komt dan vooral van de [[*afkomst|opleiding|kenniskring]].", "Van de familienaam, niet van iets wat je zelf deed."),
    keuze("Opleiding en inkomen [[*versterken elkaar|staan los van elkaar]]: een diploma opent vaak beter betaald werk.", "De factoren werken samen."),
    tabel("Is dit een voorbeeld van neerwaartse mobiliteit?",
          [("iemand verliest zijn werk en zakt af", J), ("iemand wordt ziek en moet stoppen met werken", J), ("de eerste in het gezin met een diploma", F)],
          "Ook afzakken is mobiliteit."),
    tabel("Toegewezen of verworven bij deze persoon?",
          [("Mia is geboren in een rijke familie.", "toegewezen"), ("Tom werd na zijn studie arts.", "verworven"), ("Ali spaarde zelf een huis bij elkaar.", "verworven")],
          "Toegewezen krijg je bij je geboorte, verworven bouw je zelf op.", ["toegewezen", "verworven"]),
    keuze("Een openbaar vervoer dat tot in elke wijk rijdt, helpt vooral jongeren [[*zonder eigen wagen|met een eigen wagen]] om naar school of werk te gaan.", "Zo verlaagt het een drempel."),
    koppel("Koppel het terrein aan het voorbeeld van ongelijke kansen.",
           [("onderwijs", "minder vaak hoger onderwijs bij ouders zonder diploma"), ("wonen", "een kleine, vochtige huurwoning"), ("gezondheid", "minder vaak naar de tandarts gaan"), ("werk", "geen netwerk om een stage te vinden")],
           ["een andere lievelingskleur"], "Een sociale positie werkt op veel terreinen tegelijk."),
    keuze("Een kind van een arbeider wordt zelf arbeider, en zijn kind ook. Dat is sociale [[*reproductie|mobiliteit|acculturatie]].", "De positie wordt doorgegeven."),
    open_("Leg uit hoe twee kinderen met dezelfde talenten toch andere kansen kunnen krijgen. Gebruik minstens twee statusfactoren.",
          "Het ene kind groeit op in een gezin met veel geld en ouders met een diploma (afkomst, inkomen en opleiding van de ouders). Het kan bijles krijgen en heeft een netwerk dat helpt bij stages (kenniskring). Het andere kind spreekt thuis een andere taal en heeft dat netwerk niet. Hun startpositie verschilt, dus hun kansen ook."),
]
