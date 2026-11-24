"""Boodschappen doen en de tafel dekken — pittig (🛠️ Boost dubbele finaliteit, gezondheidszorg en welzijn).

Eigen vragen strikt binnen gz_boodschappen, met een zelfgetekende lege plaats
aan tafel (bovenaanzicht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL

TD = Prent("tafel-plaats", "Een plaats aan tafel, van bovenaf gezien", "een bord in het midden met vijf lege plaatsen errond, met letters A tot E; de persoon zit aan de onderkant")
TD.rect(100, 60, 800, 520, "#f6efe0", DONKER, 20, 3)
TD.cirkel(500, 350, 130, "white", DONKER, 4); TD.cirkel(500, 350, 85, "white", "#bbb", 2)
TD.rect(400, 560, 200, 20, "#c9a878", DONKER, 4, 2)               # rand van de tafel waar je zit
TD.tekst(500, 615, "hier zit je", 22)
LET = {"A": (300, 350), "B": (700, 350), "C": (720, 170), "D": (500, 165), "E": (780, 500)}
for t, (x, y) in LET.items():
    TD.cirkel(x, y, 42, "none", "#999", 2)
    TD.letter(x, y, t)
U = "tafel-plaats.svg"
Z = {t: Prent.rond(x, y, 44) for t, (x, y) in LET.items()}

VRAGEN = [
    klik("Je dekt voor een warme maaltijd. Klik op de plaats van het mes.", U, [Z["B"]],
         "Het mes ligt rechts van het bord, met de snijkant naar het bord."),
    klik("Klik op de plaats van het glas.", U, [Z["C"]],
         "Het glas staat rechtsboven, aan de kant van het mes."),
    klik("Klik op de plaats van het dessertbestek.", U, [Z["D"]],
         "Het dessertbestek ligt boven het bord, klaar voor na de maaltijd."),
    klik("Klik op de plaats van de vork.", U, [Z["A"]],
         "De vork ligt links, tegenover het mes."),
    tabel("Helpt dit tegen voedselverspilling?",
          [("je maaltijden vooraf plannen", J), ("je koelkast organiseren", J), ("in het groot kopen wat je niet opkrijgt", F), ("de juiste porties serveren", J)],
          "In het groot kopen leidt juist tot verspilling als je het niet op tijd opkrijgt."),
    volgorde("Je maakt een boodschappenlijst. Zet de stappen in de juiste volgorde.",
             ["kijken wat je al in huis hebt", "het menu van de week bepalen", "rekening houden met het aantal personen"],
             "Eerst kijken wat er al staat."),
    mk("Waarom is drie halen, twee betalen niet altijd een besparing?",
       ["het derde pak kan bederven voor je het gebruikt", "promoties zijn altijd duurder dan gewone prijzen", "je mag in een promotie nooit prijzen vergelijken", "de winkel rekent het derde pak later toch aan"],
       0, "Wat je weggooit, heb je eerst betaald."),
    sorteer("Milieubewuste of economische keuze?", ["milieubewust", "economisch"],
            [("een eigen draagtas meenemen", "milieubewust"), ("prijzen vergelijken", "economisch"), ("seizoensgroenten van dichtbij kopen", "milieubewust"), ("niet meer kopen dan je opkrijgt", "economisch"), ("producten met weinig verpakking kiezen", "milieubewust")],
            "Kostenbewust kopen is vergelijken, gericht kiezen en niet te veel kopen."),
    mk("Waarom zijn aardbeien in de winter minder milieuvriendelijk?",
       ["ze vragen veel transport of verwarming", "ze bevatten in de winter veel meer suiker", "ze zijn in de winter altijd bedorven", "ze passen niet in een gewone koelbox"],
       0, "Groenten en fruit van het seizoen en van dichtbij hebben minder transport en verwarming nodig."),
    keuze("Een koelbox bij het winkelen houdt [[*de koudeketen|de prijs|de verpakking]] in stand van de winkel tot thuis.",
          "Zo blijven koude waren koel."),
    koppel("Koppel het restje aan wat een creatieve kok ervan maakt.",
           [("oud brood", "wentelteefjes"), ("groenten die al wat langer liggen", "soep")],
           ["een nieuwe boodschappenlijst"],
           "Van restjes maak je nieuwe gerechten."),
    mk("Je yoghurt is twee dagen over de THT. Wat bedoelt men met 'gebruik je zintuigen'?",
       ["eerst kijken, ruiken en proeven", "hem meteen in de vuilnisbak gooien", "hem nog een week in de kast zetten", "de datum met een stift aanpassen"],
       0, "Veel voedsel is na de THT nog prima."),
    tabel("Klopt dit over voedselverspilling?",
          [("Verspilling kost ook geld.", J), ("Grote porties helpen tegen verspilling.", F), ("Bijnemen kan altijd nog.", J)],
          "Wat op het bord blijft liggen, gaat meestal de vuilnisbak in."),
    inv("Hoe noem je het weggooien van eten dat nog goed was? Eén woord.", ["voedselverspilling", "verspilling"], "Voedselverspilling."),
    tabel("Hoort dit bij een gedekte ontbijttafel?",
          [("een bord", J), ("een mes", J), ("een soeplepel", F), ("een tas of een glas", J)],
          "Je dekt wat de maaltijd vraagt."),
    mk("Waarom wijst de snijkant van het mes naar het bord?",
       ["zo wijst ze niet naar je buur", "zo blijft het mes langer scherp", "zo kan je sneller snijden", "zo valt het mes niet van tafel"],
       0, "Een kwestie van veiligheid en beleefdheid."),
    tabel("Klopt dit over de gedekte tafel?",
          [("Het glas staat links van het bord.", F), ("Het servet ligt op het bord of links ernaast.", J), ("Je dekt meer bestek dan nodig, voor de zekerheid.", F)],
          "Alles wat je dekt, moet je ook afwassen."),
    tabel("Maakt dit een tafel aantrekkelijk?",
          [("een propere tafel", J), ("een bloem of kaars", J), ("een vuile vaatdoek op tafel", F), ("een nette schikking", J)],
          "Een vuile vaatdoek bederft meteen de hele indruk."),
    keuze("Voor de gasten aanschuiven, controleer je of [[*alles proper is|het eten koud is|de stoelen gelijk staan met de muur]].",
          "Propere borden, proper bestek en een propere tafel."),
    keuze("Een mooi gedekte tafel [[*nodigt uit|kost meer eten|maakt de maaltijd korter]].",
          "Ze maakt van eten een rustig en aangenaam moment."),
    tabel("Is dit een gezinsmaaltijd die je dekt?",
          [("het ontbijt", J), ("de warme maaltijd", J), ("de broodlunch", J), ("een snoepje in de auto", F)],
          "Ook het klassieke diner."),
    casus("In de leefgroep maakt Lotte de boodschappen voor zes jongeren. Ze vertrekt zonder lijst, koopt drie kilo gehakt in promotie en laat het een uur in de warme auto liggen. Thuis blijkt er al gehakt in de vriezer te liggen.", [
        tabel("Wat had Lotte beter gedaan?",
              [("eerst kijken wat er al in huis is", J), ("een koelbox meenemen", J), ("nog meer gehakt kopen", F)],
              "Plannen en de koudeketen bewaren."),
        keuze("Met een [[*boodschappenlijst|kassaticket|promotiefolder]] had ze gerichter gekocht.", "Met een lijst koop je wat je nodig hebt."),
        mk("Waarom was de promotie hier geen goede keuze?",
           ["ze kocht meer dan de groep kon opeten", "gehakt mag nooit in promotie verkocht worden", "zes jongeren eten nooit gehakt", "promoties gelden niet voor een leefgroep"],
           0, "Een promotie is geen besparing als het eten bederft."),
    ]),
    mk("Waarom plan je de maaltijden van de week vooraf?",
       ["je koopt precies wat nodig is", "je hoeft dan nooit meer te koken", "de winkel geeft dan altijd korting", "je kan dan alles in het groot kopen"],
       0, "Wie weet wat hij gaat koken, gooit minder weg."),
    inv("Wat neem je mee naar de winkel om de koude waren koel te houden? Eén woord.", ["koelbox", "een koelbox", "koeltas", "een koeltas"], "Een koelbox."),
    tabel("Hoort dit bij een tafel voor een warme maaltijd?",
          [("een bord", J), ("een vork", J), ("een glas", J), ("een boek", F)],
          "Een boek hoort niet op een gedekte tafel."),
    keuze("Het mes ligt rechts, omdat je meestal met je [[*rechterhand|linkerhand|vork]] snijdt.", "Mes rechts, vork links."),
    keuze("Het servet ligt links naast het bord, [[*onder de vork|op het glas|boven het dessertbestek]].", "Of gewoon op het bord."),
    open_("Leg uit hoe je bij het boodschappen doen tegelijk milieubewust en economisch handelt. Geef twee voorbeelden.",
          "Je neemt een eigen draagtas mee en kiest groenten van het seizoen, dat is goed voor het milieu. Je vergelijkt prijzen en koopt niet meer dan je nodig hebt, dat bespaart geld."),
]
