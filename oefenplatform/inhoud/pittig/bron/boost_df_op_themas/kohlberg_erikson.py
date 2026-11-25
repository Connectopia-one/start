"""Kohlberg en Erikson — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_kohlberg_erikson: de drie stadia van het moreel handelen
volgens Kohlberg, en de conflicten en krachten van de levensloopfasen
volgens Erikson."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik

KAR = ("Lees de situatie.\n\n"
       "Aan de uitgang van een supermarkt staat een kar vol eten voor de voedselbank. Drie jongeren zien dat er even niemand bij staat. "
       "Ilyas neemt niets: 'Als ze me zien, krijg ik een boete.' Sara neemt niets: 'Stelen mag niet, dat is de regel.' "
       "Tom neemt ook niets: 'Dit eten is voor mensen die het harder nodig hebben dan ik.'")

FAMILIE = ("Lees de situatie.\n\n"
           "Lena is vijftien. Ze probeert elke maand een andere kledingstijl, wisselt van vriendengroep en twijfelt welke studierichting bij haar past. "
           "Haar papa Mark (45) is trainer bij de jeugdploeg en zorgt met plezier voor zijn kinderen. "
           "Oma Rosa is tachtig en kijkt tevreden terug: 'Ik heb fouten gemaakt, maar ik ben blij met mijn leven.'")

VRAGEN = [
    sorteer("Welk stadium van Kohlberg?", ["pre-conventioneel", "conventioneel", "post-conventioneel"],
            [("'Ik ruim op, anders krijg ik geen dessert.'", "pre-conventioneel"), ("'Ik stop aan het rode licht, want dat is de wet.'", "conventioneel"), ("'Ik help de vluchteling, ook al mag het niet, want elk mens heeft recht op hulp.'", "post-conventioneel"), ("'Ik spiek niet, want als ik betrapt word, krijg ik een nul.'", "pre-conventioneel"), ("'Ik draag het clubtruitje, want zo doen we dat in onze ploeg.'", "conventioneel"), ("'Ik protesteer tegen een wet die mensen ongelijk behandelt.'", "post-conventioneel")],
            "Straf en beloning, regels en de groep, eigen waarden."),
    casus(KAR, [
        tabel("In welk stadium van Kohlberg redeneert elk?",
              [("Ilyas", "pre-conventioneel"), ("Sara", "conventioneel"), ("Tom", "post-conventioneel")],
              "Kijk waarom ze niets nemen, niet dát ze niets nemen.", ["pre-conventioneel", "conventioneel", "post-conventioneel"]),
        mk("Wie redeneert vanuit waarden die verder gaan dan de regel?",
           ["Tom", "Sara", "Ilyas", "niemand van de drie"],
           0, "Tom denkt aan rechtvaardigheid voor wie het eten nodig heeft."),
        keuze("Ilyas let vooral op [[*de straf|de wet|de mensenrechten]].", "Het gevolg voor hemzelf telt."),
        keuze("Sara neemt niets omdat [[*het de regel is|ze er een beloning voor krijgt|ze de regel onrechtvaardig vindt]].", "De regel geldt omdat het de regel is."),
    ]),
    tabel("Welk conflict van Erikson hoort bij deze fase?",
          [("de baby", "vertrouwen of wantrouwen"), ("de peuter", "autonomie of twijfel"), ("de kleuter", "initiatief of schuld"), ("het lagereschoolkind", "handvaardigheid of minderwaardigheid"), ("de adolescent", "identiteit of verwarring")],
          "Elke fase heeft twee polen.", ["vertrouwen of wantrouwen", "autonomie of twijfel", "initiatief of schuld", "handvaardigheid of minderwaardigheid", "identiteit of verwarring"]),
    koppel("Koppel het conflict aan de kracht die vrijkomt.",
           [("vertrouwen tegenover wantrouwen", "hoop"), ("autonomie tegenover twijfel en schaamte", "wil"), ("identiteit tegenover identiteitsverwarring", "trouw"), ("intimiteit tegenover isolatie", "liefde")],
           ["wijsheid"],
           "Wijsheid hoort bij integriteit tegenover wanhoop."),
    volgorde("Zet de conflicten van Erikson in de volgorde van de levensloop.",
             ["vertrouwen tegenover wantrouwen", "autonomie tegenover twijfel en schaamte", "initiatief tegenover schuld", "handvaardigheid tegenover minderwaardigheid", "identiteit tegenover identiteitsverwarring"],
             "Van baby tot adolescent."),
    volgorde("Zet de conflicten van de volwassenheid in de juiste volgorde.",
             ["intimiteit tegenover isolatie", "generativiteit tegenover stagnatie", "integriteit tegenover wanhoop"],
             "Vroege, midden- en late volwassenheid."),
    casus(FAMILIE, [
        keuze("Lena zit in het conflict [[*identiteit tegenover identiteitsverwarring|vertrouwen tegenover wantrouwen|integriteit tegenover wanhoop]].", "Ze zoekt wie ze is."),
        keuze("Mark toont [[*generativiteit|stagnatie|isolatie]].", "Hij geeft iets door aan de volgende generatie."),
        keuze("Oma Rosa toont [[*integriteit|wanhoop|isolatie]].", "Ze aanvaardt haar leven zoals het was."),
        inv("Welke kracht komt vrij als Lena haar conflict goed oplost? Eén woord.", ["trouw", "de trouw"], "Trouw: weten wie je bent en daarbij blijven."),
        keuze("Bij oma Rosa hoort de kracht [[*wijsheid|hoop|wil]].", "Integriteit tegenover wanhoop levert wijsheid op."),
    ]),
    mk("Een peuter wil per se zelf zijn schoenen aandoen. Welk conflict van Erikson zie je?",
       ["autonomie tegenover twijfel en schaamte", "vertrouwen tegenover wantrouwen", "generativiteit tegenover stagnatie", "handvaardigheid tegenover minderwaardigheid"],
       0, "Zelf willen en zelf kunnen: de kracht is de wil."),
    tabel("Klopt dit over Erikson?",
          [("Een conflict dat niet opgelost raakt, speelt later nog mee.", J), ("Erikson beschrijft de morele ontwikkeling.", F), ("Een goed opgelost conflict levert een kracht op.", J), ("Erikson werkt met stadia van straf en beloning.", F)],
          "Erikson beschrijft de persoonlijkheid, Kohlberg de moraal."),
    keuze("Een kind van negen voelt zich dom omdat het minder goed leest dan de anderen. Dat speelt in het conflict handvaardigheid tegenover [[*minderwaardigheid|wantrouwen|stagnatie]].", "Het lagereschoolkind vergelijkt wat het kan met de anderen."),
    keuze("Een kleuter die zelf een spel bedenkt en de leiding neemt, toont [[*initiatief|wantrouwen|stagnatie]].", "Initiatief tegenover schuld."),
    inv("Welke kracht hoort bij initiatief tegenover schuld? Eén woord.", ["doelgerichtheid", "de doelgerichtheid"], "Doelgerichtheid."),
    inv("Welke kracht hoort bij generativiteit tegenover stagnatie? Eén woord.", ["zorg", "de zorg"], "Zorg."),
    tabel("Hoort dit bij Kohlberg of bij Erikson?",
          [("straf en beloning", "Kohlberg"), ("identiteit", "Erikson"), ("de wet en de regels", "Kohlberg"), ("hoop en wil", "Erikson"), ("eigen principes", "Kohlberg")],
          "Moraal tegenover persoonlijkheid.", ["Kohlberg", "Erikson"]),
    keuze("Iemand in het conventionele stadium vindt vooral belangrijk [[*wat de groep en de regels zeggen|wat hij er zelf aan verdient|wat de mensenrechten vragen]].", "De groep en de regels geven de norm."),
    mk("Een tiener laat zijn vriend spieken omdat 'vrienden elkaar helpen en de groep dat verwacht'. Welk stadium van Kohlberg?",
       ["conventioneel", "pre-conventioneel", "post-conventioneel", "sensomotorisch"],
       0, "Wat de groep verwacht, bepaalt het gedrag."),
    mk("Waarom is een baby die telkens getroost wordt goed op weg in zijn eerste conflict?",
       ["hij leert dat de wereld te vertrouwen is", "hij leert snel dat huilen nooit en nergens iets oplevert", "hij wordt daardoor later minder slim", "hij hoeft daarna nooit meer te huilen"],
       0, "Vertrouwen tegenover wantrouwen; de kracht is hoop."),
    sleep("Kohlberg onderscheidt het [[pre-conventionele]], het [[conventionele]] en het [[post-conventionele]] stadium.",
          ["sensomotorische", "formeel-operationele"],
          "Sensomotorisch en formeel-operationeel komen van Piaget."),
    keuze("Volgens Kohlberg blijven veel mensen in het [[*conventionele|pre-conventionele]] stadium.", "Niet iedereen bereikt het post-conventionele."),
    tabel("Wat weegt hier mee? Welk stadium van Kohlberg?",
          [("een snoepje als beloning", "pre-conventioneel"), ("wat je ouders van je verwachten", "conventioneel"), ("rechtvaardigheid voor iedereen", "post-conventioneel"), ("de orde in de samenleving", "conventioneel")],
          "Eigen voordeel, de groep en de regels, of eigen waarden.", ["pre-conventioneel", "conventioneel", "post-conventioneel"]),
    keuze("Een man van tachtig vindt dat zijn leven mislukt is en dat het te laat is om iets te veranderen. Hij zit aan de kant van [[*wanhoop|integriteit|generativiteit]].", "Integriteit tegenover wanhoop."),
    mk("Een vrouw van vijfentwintig durft geen hechte relatie aan te gaan en trekt zich terug. Welk conflict?",
       ["intimiteit tegenover isolatie", "identiteit tegenover verwarring", "vertrouwen tegenover wantrouwen", "integriteit tegenover wanhoop"],
       0, "Een band aangaan zonder jezelf te verliezen; de kracht is liefde."),
    open_("Geef een eigen voorbeeld van iemand die redeneert in het post-conventionele stadium. Leg uit waarom het post-conventioneel is.",
          "Een verpleegkundige helpt een gewonde zonder papieren, ook al zegt de regel dat het niet mag. Ze weegt de regel af tegen haar waarde dat elk mens recht heeft op zorg."),
]
