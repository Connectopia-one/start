# -*- coding: utf-8 -*-
from _basis import *

TITEL = "Lectuur: Erasmus, een humanist tussen twee werelden"
BRON = ("Een eigen tekst van Connectopia over het thema van de lectuuropdracht (het leven van Erasmus). Gebaseerd op: Erasmus, Moriae Encomium (1511) en zijn uitgave van het Nieuwe Testament (1516); de geschiedenis van het Collegium Trilingue in Leuven (1517). "
        "Wil je meer lezen, dan is de biografie Erasmus van Sandra Langereis uit de vakfiche een goede volgende stap.")
INLEIDING = "Deze tekst is geen Latijn. Hij helpt je bij de lectuuropdracht over Erasmus. Lees hem rustig en beantwoord dan de vragen."
ALINEAS = [
    "Een kind zonder plaats",
    "Desiderius Erasmus werd geboren in Rotterdam, rond 1466 of 1469: hij hield het jaartal zelf graag vaag. Hij was de buitenechtelijke zoon van een priester, en dat zou hem zijn hele leven achtervolgen. Na de dood van zijn ouders kwam hij als jonge man in het klooster van Steyn, bij Gouda, terecht. Daar ontdekte hij de klassieke schrijvers en leerde hij uitstekend Latijn, maar het kloosterleven paste niet bij hem.",
    "Reizen en schrijven",
    "Erasmus kreeg toestemming om het klooster te verlaten. Hij studeerde in Parijs en reisde zijn hele leven door Europa: naar Engeland, waar hij bevriend raakte met Thomas More, naar Italië, naar Leuven en naar Bazel. Hij schreef in het Latijn, en daardoor kon hij lezers bereiken van Spanje tot Polen. De boekdrukkunst, die nog vrij nieuw was, maakte hem tot een van de eerste bestsellerauteurs. Hij schreef duizenden brieven aan geleerden, vorsten en vrienden.",
    "In 1509 schreef hij, bij Thomas More in Londen, de Lof der Zotheid. De Latijnse titel Moriae Encomium is een woordspel op de naam More. In 1516 gaf hij het Nieuwe Testament uit in het Grieks, met een nieuwe Latijnse vertaling. Hij wilde terug naar de bronnen: ad fontes. Dat is typisch voor het humanisme. In 1517 hielp hij in Leuven het Collegium Trilingue oprichten, waar Latijn, Grieks en Hebreeuws werden onderwezen.",
    "Tussen Luther en de paus",
    "Erasmus bekritiseerde misbruiken in de Kerk: hebzuchtige geestelijken, bijgeloof en lege rituelen. Toen Maarten Luther vanaf 1517 de Kerk aanviel, dachten velen dat Erasmus aan zijn kant stond. Men zei zelfs dat Erasmus het ei gelegd had dat Luther uitbroedde. Maar Erasmus wilde de Kerk hervormen van binnenuit en hield niet van ruzie en geweld. Hij brak met Luther en bleef katholiek. Zo kreeg hij kritiek van beide kanten. Hij stierf in 1536 in Bazel.",
]
WOORDEN = Wl(
    ("buitenechtelijke", "geboren uit ouders die niet met elkaar getrouwd waren"),
    ("humanisme", "een stroming die de mens en de klassieke oudheid centraal stelt"),
    ("ad fontes", "terug naar de bronnen"),
    ("Collegium Trilingue", "het Drietalencollege in Leuven"),
)
VRAGEN = [
    mk("Waar werd Erasmus geboren?",
       ["in Rotterdam", "in Leuven", "in Bazel", "in Londen"], 0,
       "Hij noemde zichzelf Erasmus Roterodamus, Erasmus van Rotterdam."),
    mk("Waarom paste het kloosterleven niet bij Erasmus?",
       ["hij wilde liever studeren", "hij kon geen Latijn leren", "hij wilde trouwen", "hij werd er slecht behandeld"], 0,
       "In het klooster leerde hij wel goed Latijn, maar hij voelde zich er niet thuis. Hij kreeg toestemming om te vertrekken en ging studeren in Parijs."),
    tabel("Klopt dit over Erasmus?",
          [("Hij schreef in het Latijn.", J),
           ("Hij was bevriend met Thomas More.", J),
           ("Hij schreef zijn boeken in het Nederlands.", F),
           ("Hij bleef heel zijn leven in Rotterdam.", F)],
          "Erasmus reisde door heel Europa en schreef in het Latijn, zodat geleerden overal hem konden lezen."),
    mk("Welke uitvinding hielp Erasmus beroemd te worden?",
       ["de boekdrukkunst", "de telescoop", "de stoommachine", "het kompas"], 0,
       "De boekdrukkunst, rond 1450 in Europa ontwikkeld, maakte boeken veel goedkoper. Zo konden de werken van Erasmus snel overal verspreid worden."),
    keuze("De titel Moriae Encomium is een woordspel op de naam van [[*Thomas More|Maarten Luther|Galileo]]. Moria is Grieks voor [[*zotheid|wijsheid|vriendschap]].",
          "Erasmus schreef het boek bij Thomas More in Londen. Moria betekent dwaasheid, en het klinkt als More."),
    mk("Wat betekent ad fontes?",
       ["terug naar de bronnen", "naar de fonteinen van Rome", "vooruit naar de toekomst", "weg met de oude boeken"], 0,
       "De humanisten wilden de oude teksten in hun oorspronkelijke taal lezen. Daarom gaf Erasmus het Nieuwe Testament in het Grieks uit."),
    tabel("Welke talen werden onderwezen in het Collegium Trilingue?",
          [("Latijn", J),
           ("Grieks", J),
           ("Hebreeuws", J),
           ("Frans", F)],
          "Trilingue betekent drietalig. In Leuven leerde men vanaf 1517 de drie talen van de Bijbel en de oudheid."),
    mk("Wat bedoelde men met Erasmus legde het ei dat Luther uitbroedde?",
       ["Erasmus maakte de weg vrij voor Luther", "Erasmus was de leraar van Luther", "Erasmus had Luther verraden", "Erasmus en Luther schreven samen een boek"], 0,
       "De kritiek van Erasmus op de Kerk leek op die van Luther. Toch wilde Erasmus geen breuk, maar een hervorming van binnenuit."),
    mk("Waarom kreeg Erasmus kritiek van beide kanten?",
       ["hij koos geen kant", "hij schreef volgens hen slecht Latijn", "hij was rijk geworden", "hij wilde koning worden"], 0,
       "Voor de aanhangers van Luther was hij te voorzichtig, voor sommige katholieken te kritisch. Erasmus hield van matigheid en vrede."),
    open_("Welk verband zie je tussen het leven van Erasmus en zijn kritiek op de monniken in de Lof der Zotheid?",
          "Erasmus had zelf in een klooster gewoond en kende het kloosterleven van binnenuit. Het paste niet bij hem, en hij zag er bijgeloof, onwetendheid en lege regels. Als humanist vond hij studie en de echte bron van het geloof, de naastenliefde, belangrijker dan kapjes, gordels en vasten.",
          "Gebruik zijn tijd in het klooster van Steyn en zijn ideaal van ad fontes of naastenliefde."),
]
