"""Biologische evolutie — pittig (Beyond dubbele finaliteit, natuurwetenschappen).

Pittige vragen biologie Beyond (zelfde prenten), enkel wat in nwd_evolutie staat, plus eigen vragen."""
from ..beyond_bio_themas import evolutie as E
from ..beyond_bio_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

_V = {"mutaties en allelfrequenties": "mutaties en genen"}

VRAGEN = kies(E.VRAGEN, [0, 1, 2, 3, 4, 5, 8, 9, 13, 14, 16, 18, 21, 22], _V) + [
    casus(
        "Onderzoekers vergelijken een stukje DNA van vier soorten met dat van de mens. Ze tellen hoeveel basen verschillen: "
        "chimpansee 12, gorilla 16, muis 60, kip 95.",
        [
            mk("Welke soort is het nauwst verwant met de mens?",
               ["de chimpansee", "de gorilla", "de veldmuis", "de kip, een vogel"], 0, "Het kleinste verschil in DNA."),
            keuze("De gemeenschappelijke voorouder van mens en kip leefde [[*langer|korter]] geleden dan die van mens en muis.",
                  "Een groter verschil in DNA wijst op een oudere splitsing."),
            keuze("Dit argument voor evolutie komt uit de [[*moleculaire biologie|paleontologie|anatomie]].", "Het gaat om DNA."),
            tabel("Klopt dit?", [
                ("De mens stamt af van de chimpansee van vandaag.", F),
                ("Mens en chimpansee delen een recente gemeenschappelijke voorouder.", J),
                ("Als anatomie en DNA dezelfde stamboom geven, is die stamboom betrouwbaarder.", J),
            ], "Twee onafhankelijke argumenten die hetzelfde zeggen, versterken elkaar."),
        ],
    ),
    sorteer("Uit welk vakgebied komt dit argument voor evolutie?", ["anatomie", "paleontologie", "moleculaire biologie"], [
        ["homologe voorpoten bij zoogdieren", "anatomie"], ["een fossiel van Archaeopteryx", "paleontologie"],
        ["dezelfde DNA-code bij alle organismen", "moleculaire biologie"], ["rudimentaire heupbeentjes bij een walvis", "anatomie"],
        ["een evolutiereeks van het paard", "paleontologie"], ["een klein verschil in DNA tussen twee soorten", "moleculaire biologie"],
    ], "Bouw, fossielen en DNA wijzen elk op verwantschap."),
    mk("Waarom vind je van de meeste soorten uit het verleden geen fossiel?",
       ["Fossiliseren is uitzonderlijk.", "Die soorten hebben nooit bestaan.", "Alle fossielen zijn al opgegraven.", "Fossielen lossen op in water."], 0,
       "Meestal vergaat een dood organisme volledig."),
    mk("In een evolutieboom staat de mens bovenaan, de bacterie onderaan. Wat betekent dat?",
       ["Niets over hoe ver ze ontwikkeld zijn.", "De mens is het verst geëvolueerd.", "De bacterie is het oudste nog levende dier.", "De bacterie zal ooit een mens worden."], 0,
       "De hoogte in een boom zegt niets over hoe 'ver' een soort staat."),
    inv("De aarde is ongeveer 4,6 miljard jaar oud. De eerste cellen ontstonden ongeveer 3,8 miljard jaar geleden. Hoeveel miljard jaar bestond de aarde toen al? Schrijf als decimaal getal.", ["0,8", "0.8"],
        "4,6 − 3,8 = 0,8."),
    keuze("Evolutie speelt zich af bij [[*populaties|één individu]] over vele generaties.", "Een individu houdt zijn genen."),
    keuze("Embryo's van verwante soorten lijken sterk op elkaar. Dat is het argument uit de [[*embryologie|paleontologie]].", "Embryologie."),
    keuze("Evolutie heeft [[*geen vooraf bepaald doel|een vooraf bepaald doel]].", "Ze werkt met wat er toevallig ontstaat."),
    keuze("De vleugel van een insect en de vleugel van een vogel zijn [[*analoog|homoloog]].", "Zelfde functie, andere bouw."),
    tabel("Klopt dit over de evolutietheorie?", [
        ("Ze steunt op waarnemingen en kan getoetst worden.", J), ("Ze is sinds Darwin niet meer veranderd.", F),
        ("Creationisme is geen wetenschappelijke theorie.", J), ("Alle organismen stammen af van een oercel.", J),
    ], "De theorie groeide met de kennis over genen en DNA."),
    volgorde("Zet deze gebeurtenissen in de juiste volgorde, van oud naar recent.", [
        "de aarde ontstaat", "de eerste cellen", "de eerste vogels zoals Archaeopteryx", "de eerste mensen",
    ], "Van 4,6 miljard jaar geleden tot vandaag."),
    koppel("Koppel elk evolutiebegrip aan zijn betekenis.", [
        ["fossiel", "versteende rest of afdruk"], ["overgangsvorm", "fossiel met kenmerken van twee groepen"],
        ["rudimentair orgaan", "orgaan zonder functie meer"], ["oercel", "eerste cel waaruit alle leven ontstond"],
    ], ["groep dieren van één soort in één gebied"], "Dat laatste is een populatie."),
    open_("Leg uit waarom de botten in de voorpoot van een hond, een vleermuis en een mens zo op elkaar lijken.",
          "Ze stammen af van een gemeenschappelijke voorouder met dezelfde botten. Bij elk dier kreeg die voorpoot later een andere functie.",
          "Homologe organen: dezelfde bouw, een andere functie."),
]
