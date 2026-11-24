"""Voedsel bewaren — pittig (🛠️ Boost dubbele finaliteit, gezondheidszorg en welzijn).

Eigen vragen strikt binnen gz_bewaren, met een zelfgetekende open koelkast."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL

KK = Prent("koelkast-zones", "Een open koelkast", "een koelkast met drie legplanken, een lade onderaan en een open deur met vakjes, met letters A tot E")
KK.rect(250, 60, 360, 540, "#f4f8fb", DONKER, 16, 4)        # kast
for y in (180, 300, 420):
    KK.lijn(262, y, 598, y, "#9ab", 6)                       # legplanken
KK.rect(275, 460, 310, 120, "#dfeee0", DONKER, 10, 3)      # groentelade
KK.rect(640, 60, 170, 540, "#f4f8fb", DONKER, 16, 4)       # deur
for y in (170, 300, 430):
    KK.rect(655, y, 140, 60, "#e6ecf2", DONKER, 6, 2)        # deurvakken
LET = {"A": (430, 120), "B": (430, 240), "C": (430, 360), "D": (430, 520), "E": (725, 250)}
for t, (x, y) in LET.items():
    KK.letter(x, y, t)
U = "koelkast-zones.svg"
Z = {t: Prent.rond(x, y, 40) for t, (x, y) in LET.items()}

VRAGEN = [
    klik("Klik op de letter bij de koudste plaats in de koelkast.", U, [Z["C"]],
         "Koude lucht zakt: onderaan, net boven de groentelade, is het het koudst."),
    klik("Klik op de letter bij de plaats waar je verse vis legt.", U, [Z["C"]],
         "Vlees en vis horen op de koudste plaats."),
    klik("Klik op de letter bij de minst koude plaats, waar sauzen en dranken mogen staan.", U, [Z["E"]],
         "De deur is de minst koude plaats."),
    klik("Klik op de letter bij de plaats waar groenten en fruit langer vers blijven.", U, [Z["D"]],
         "In de groentelade is het iets minder koud."),
    mk("Waarom is het onderaan in de koelkast kouder dan bovenaan?",
       ["koude lucht is zwaarder en zakt", "de lamp zit onderaan", "de deur gaat onderaan minder open", "de groentelade maakt koude"],
       0, "Daarom is het in de deur het minst koud."),
    sorteer("Waar bewaar je dit?", ["koelkast", "koele berging", "vriezer"],
            [("gehakt voor vanavond", "koelkast"), ("een zak aardappelen", "koele berging"), ("diepvriesgroenten", "vriezer"), ("uien", "koele berging"), ("verse patisserie", "koelkast")],
            "Aardappelen, uien en conserven horen in een koele berging."),
    tabel("Is dit een kenmerk van een goede koele berging?",
          [("donker", J), ("droog", J), ("warm", F), ("goed verlucht", J)],
          "Warmte wil je er net niet."),
    koppel("Koppel de afkorting aan haar betekenis.",
           [("FIFO", "eerst in, eerst uit"), ("FEFO", "wat eerst vervalt, gaat eerst weg"), ("THT", "ten minste houdbaar tot"), ("TGT", "te gebruiken tot")],
           ["te bewaren tot"],
           "THT gaat over kwaliteit, TGT over veiligheid."),
    sorteer("Wat doe je met dit product?", ["weggooien", "eerst kijken en ruiken"],
            [("yoghurt met TGT van gisteren", "weggooien"), ("koekjes met THT van vorige week", "eerst kijken en ruiken"), ("gehakt met TGT van eergisteren", "weggooien"), ("rijst met THT van vorige maand", "eerst kijken en ruiken")],
            "Na de TGT is een product niet meer veilig. Na de THT gebruik je je zintuigen."),
    mk("Twee pakken melk: één kocht je vorige week en vervalt over tien dagen, één kocht je gisteren en vervalt morgen. Welk gebruik je eerst volgens FEFO?",
       ["het pak dat morgen vervalt", "het pak van vorige week", "het pak dat het meest vol is", "het pak dat vooraan staat"],
       0, "First Expired, First Out: wat het eerst vervalt, gaat eerst weg."),
    mk("Je bergt nieuwe blikken tomaten op in de voorraadkast. Hoe doe je dat volgens FIFO?",
       ["de oude blikken vooraan zetten", "de nieuwe blikken vooraan zetten", "alle blikken door elkaar zetten", "de oude blikken weggooien"],
       0, "Zo gebruik je vanzelf eerst wat er al stond."),
    tabel("Klopt dit over THT en TGT?",
          [("THT en TGT betekenen hetzelfde.", F), ("Na de TGT gooi je het product weg.", J), ("Na de THT is een product meestal nog veilig.", J)],
          "THT gaat over kwaliteit, TGT over veiligheid."),
    mk("Waarom groeien kiemen trager in de koelkast?",
       ["de koude haalt een levensvoorwaarde weg", "er is helemaal geen voedsel voor kiemen in de koelkast", "het licht gaat uit als de deur dicht is", "de koelkast doodt meteen alle kiemen"],
       0, "De temperatuur is een levensvoorwaarde van micro-organismen."),
    keuze("Een geopende bokaal augurken zet je [[*in de koelkast|terug in de voorraadkast|in de zon]].",
          "Zodra hij open is, komt er lucht bij en kunnen micro-organismen groeien."),
    tabel("Klopt dit over invriezen?",
          [("Je vriest alleen verse waren in.", J), ("Ingevroren voedsel blijft oneindig lang goed.", F), ("Diepvriesgroente blijft enkele maanden goed.", J)],
          "Invriezen stopt het bederf, maar maakt niets opnieuw vers."),
    mk("Hoe ontdooi je een kippenfilet het veiligst?",
       ["in de koelkast", "op het aanrecht", "in de zon", "in lauw water"],
       0, "In de koelkast blijft het vlees koud terwijl het ontdooit."),
    keuze("Ontdooid gehakt [[*vries je niet opnieuw in|vries je meteen opnieuw in|laat je een dag buiten liggen]].",
          "Bij het ontdooien groeien de kiemen weer."),
    tabel("Schrijf je dit op een doos die de vriezer in gaat?",
          [("de inhoud", J), ("de datum", J), ("het aantal personen", J), ("de prijs", F)],
          "De prijs hoeft er niet op."),
    tabel("Is dit een reden om restjes in een afgesloten doos te bewaren?",
          [("kiemen blijven buiten", J), ("geuren blijven binnen", J), ("het koelt sneller af", F), ("het droogt niet uit", J)],
          "Een gesloten doos koelt juist trager af."),
    volgorde("Je komt thuis met boodschappen. Zet het opbergen in een goede volgorde.",
             ["koele en diepvrieswaren meteen opbergen", "de oude voorraad naar voren schuiven", "droge waren in de voorraadkast zetten"],
             "Koele waren eerst, dan FIFO toepassen."),
    keuze("Bloem, pasta en rijst blijven goed op een [[*droge en donkere|vochtige en warme|lichte en natte]] plaats.",
          "Daarvoor dient een voorraadkast."),
    casus("Bij het opruimen van de koelkast in de leefgroep vindt Ines: rauw gehakt in de deur, sla bovenaan, een open pot pesto in de voorraadkast en een doos soep in de vriezer zonder etiket.", [
        tabel("Wat moet Ines aanpassen?",
              [("het gehakt naar onderaan, de koudste plaats", J), ("de open pesto in de koelkast zetten", J), ("de sla in de groentelade leggen", J), ("de soep uit de vriezer weggooien omdat ze bevroren is", F)],
              "De soep is bevroren in orde, maar krijgt best nog een etiket."),
        inv("Wat schrijft Ines naast de inhoud zeker op de soepdoos? Eén woord.", ["datum", "de datum"], "De datum."),
        mk("Waarom hoort rauw gehakt niet in de deur?",
           ["de deur is de minst koude plaats", "de deur is net de koudste plaats", "gehakt past nooit in de vakjes van de deur", "het gehakt wordt er veel te droog"],
           0, "Rauw gehakt hoort onderaan, waar het het koudst is."),
    ]),
    tabel("Is dit een bewaarplaats voor voedsel?",
          [("de koelkast", J), ("de vriezer", J), ("de vaatwasser", F), ("een voorraadkast", J)],
          "In de wasmachine of de vaatwasser hoort geen voedsel."),
    tabel("Hou je hier rekening mee bij het bewaren?",
          [("het soort voedingsmiddel", J), ("de bewaarplaats", J), ("de houdbaarheid", J), ("de kleur van de doos", F)],
          "Wat het is, waar het hoort en tot wanneer het goed blijft."),
    keuze("Verse patisserie met room hoort [[*in de koelkast|in de voorraadkast|in de koele berging]].",
          "Ze bevat room en eieren."),
    keuze("Eieren kunnen in [[*de deur|de vriezer|de groentelade]] van de koelkast.",
          "De deur is de minst koude plaats en volstaat voor eieren."),
    inv("Hoe noem je het principe waarbij wat het eerst vervalt, het eerst weggaat? Eén woord.", ["fefo", "het fefo"], "FEFO, First Expired, First Out."),
    open_("Leg het verschil uit tussen THT en TGT, met een voorbeeld.",
          "THT betekent ten minste houdbaar tot: na die datum kan de kwaliteit minderen, maar het is meestal nog veilig, zoals bij koekjes. TGT betekent te gebruiken tot: na die datum is het niet meer veilig, zoals bij gehakt."),
]
