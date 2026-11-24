"""De marketingmix — pittig (🛠️ Boost dubbele finaliteit, EBW).

Eigen vragen strikt binnen eb_marketing, met een zelfgetekende affiche om de
onderdelen van de marketingmix op aan te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, LICHTGROEN, DONKER, ORANJE

AF = Prent("affiche-sapbar", "", "affiche van sapbar Fris aan het station, met vijf regels en letters A tot E")
AF.rect(110, 24, 780, 596, "#ffffff", ORANJE, 24, 4)
AF.tekst(500, 92, "Sapbar Fris", 46, vet=True, kleur=ORANJE)
AF.tekst(500, 132, "nieuw aan het station van Hasselt", 22)
REGELS = [
    ("A", "Verse smoothies met Limburgs fruit,", "in een beker die je terugbrengt."),
    ("B", "4,50 euro per smoothie,", "de tweede aan halve prijs."),
    ("C", "In de stationshal,", "elke werkdag vanaf 6 uur."),
    ("D", "Bestel vooraf in de app:", "je smoothie staat klaar als je trein vertrekt."),
    ("E", "Deel je foto met #sapbarfris", "en win een maand gratis smoothies."),
]
Y0, DY = 205, 86
for i, (t, r1, r2) in enumerate(REGELS):
    y = Y0 + i * DY
    AF.letter(170, y + 4, t)
    AF.tekst(210, y, r1, 22, "start")
    AF.tekst(210, y + 30, r2, 22, "start")
U = "affiche-sapbar.svg"
Z = {t: Prent.rond(170, Y0 + i * DY + 4, 30) for i, (t, _, _) in enumerate(REGELS)}

VRAGEN = [
    klik("Klik op de letter bij de P van prijs.", U, [Z["B"]],
         "4,50 euro en een korting op de tweede: de prijs en de prijsstrategie."),
    klik("Klik op de letter bij de P van plaats.", U, [Z["C"], Z["D"]],
         "De stationshal is de plaats waar de klant zijn smoothie koopt; ook de app is een kanaal. C en D zijn allebei juist."),
    klik("Klik op de letter bij de P van product.", U, [Z["A"]],
         "De kwaliteit en de verpakking horen bij het product."),
    klik("Klik op de letter bij de P van promotie.", U, [Z["E"]],
         "Een wedstrijd op sociale media brengt de sapbar onder de aandacht."),
    klik("Klik op de letter die het best past bij de C van convenience.", U, [Z["D"]],
         "Vooraf bestellen in de app maakt het voor de reiziger heel gemakkelijk."),
    casus("Bekijk de affiche van Sapbar Fris.", [
        mk("Welke doelgroep heeft Sapbar Fris wellicht vooral in gedachten?",
           ["reizigers en pendelaars aan het station", "gezinnen met kleine kinderen op vakantie", "bedrijven die grote voorraden fruit kopen", "senioren in een woonzorgcentrum"], 0,
           "Een sapbar in de stationshal met een app die de smoothie klaarzet voor je trein."),
        tabel("Bij welke C hoort deze regel van de affiche?",
              [("A: verse smoothies met Limburgs fruit", "customer"), ("B: de tweede aan halve prijs", "cost"), ("D: klaar als je trein vertrekt", "convenience"), ("E: deel je foto met de hashtag", "communication")],
              "Elke P heeft een C die hetzelfde zegt vanuit de klant.",
              kolommen=["customer", "cost", "convenience", "communication"]),
        keuze("De beker die je terugbrengt hoort bij de P van [[*product|promotie|plaats]].",
              "De verpakking is een deel van het product."),
    ]),
    koppel("Welke C hoort bij welke P?",
           [("product", "customer"), ("prijs", "cost"), ("plaats", "convenience"), ("promotie", "communication")],
           ["cash"], "Elke P heeft een C die hetzelfde zegt van de andere kant. Cash hoort er niet bij."),
    sorteer("Welke P hoort hierbij?", ["product", "prijs", "plaats", "promotie"],
            [("de garantie van twee jaar", "product"), ("een korting van 10 % bij betaling binnen acht dagen", "prijs"), ("een webshop met levering aan huis", "plaats"), ("een advertentie in de krant", "promotie"), ("het merk en het logo", "product"), ("een stand op een beurs", "promotie")],
            "Product, prijs, plaats en promotie samen vormen de marketingmix."),
    tabel("Klopt dit over de vier C's?",
          [("De C's bekijken de marketingmix vanuit de klant.", J), ("De vier C's vervangen de vier P's volledig.", F), ("Convenience betekent dat het product goedkoop is.", F), ("Communicatie is tweerichtingsverkeer.", J)],
          "De C's staan naast de P's. Convenience gaat over gemak, de prijs zit in cost."),
    tabel("Hoort dit bij de C van cost, de kost voor de klant?",
          [("de prijs van het product", J), ("de tijd die het hem kost", J), ("de moeite om er te komen", J), ("de winst van de verkoper", F)],
          "Cost is meer dan de prijs alleen."),
    mk("Een winkel met dure designerjassen verkoopt die met grote kortingen in een discountwinkel, zonder reclame. Wat loopt er mis?",
       ["De vier P's passen niet bij elkaar.", "Er is geen product in de marketingmix.", "De C van customer ontbreekt helemaal.", "De prijs is altijd de enige P die telt."], 0,
       "De P's horen samen: een duur merk in een goedkope winkel zonder passende promotie verkoopt niet."),
    keuze("Een te lage prijs kan de klant doen twijfelen aan de [[*kwaliteit|verpakking|plaats]].",
          "Goedkoop is niet altijd de beste keuze."),
    tabel("Hoort dit bij convenience voor een webshop?",
          [("een vlotte website", J), ("snelle levering", J), ("makkelijk terugsturen", J), ("een reclamespot op tv", F)],
          "De reclamespot hoort bij communication."),
    casus("Lees de situatie.\n\nEen fietsenmaker wil een elektrische fiets verkopen aan zestigplussers in zijn gemeente. Hij twijfelt tussen een advertentie op een sociale-mediaplatform voor tieners en een infoavond in het dienstencentrum met een gratis proefrit.", [
        mk("Welke promotie past het best bij zijn doelgroep?",
           ["de infoavond met een gratis proefrit", "de advertentie voor tieners op sociale media", "geen promotie, enkel een zo laag mogelijke prijs", "een kortingsbon voor scholieren en studenten"], 0,
           "Dezelfde marketingmix past niet bij elke doelgroep."),
        keuze("Mensen die op de infoavond hun vragen stellen, maken van de promotie [[*communicatie|distributie|productie]]: tweerichtingsverkeer.",
              "Communicatie is ook luisteren."),
        inv("Hoe noem je de groep mensen voor wie een product bedoeld is? Schrijf één woord.", ["doelgroep", "de doelgroep"],
            "De doelgroep."),
    ]),
    keuze("Een onderneming onderzoekt eerst de markt om te weten [[*wat de doelgroep wil|hoeveel winst ze vorig jaar maakte|wie haar leveranciers zijn]].",
          "Zonder dat is elke keuze een gok."),
    tabel("Welke P is dit voor een bakkerij?",
          [("een zuurdesembrood zonder bewaarmiddelen", "product"), ("een spaarkaart: elk tiende brood gratis", "prijs"), ("een broodautomaat aan de kerk", "plaats"), ("een folder in de brievenbus", "promotie")],
          "Herken in een voorbeeld telkens de vier P's.",
          kolommen=["product", "prijs", "plaats", "promotie"]),
    sleep("Distributie is een ander woord voor de P van [[plaats]]. De C van [[customer]] staat voor de klant.",
          ["promotie", "cost"], "Plaats is de weg naar de klant."),
    keuze("De P's kijken vanuit de [[*onderneming|klant]], de C's vanuit de [[*klant|onderneming]].",
          "Daarom gebruikt men ze naast elkaar."),
    open_("Een webshop voor sportschoenen wil beter scoren op de C van convenience. Geef twee concrete maatregelen.",
          "Bijvoorbeeld gratis levering binnen 24 uur, een eenvoudige website die snel werkt op de gsm, gratis en makkelijk terugsturen, of afhalen in een winkel in de buurt.",
          "Convenience gaat over hoe gemakkelijk de klant aan het product komt."),
    mk("Welk voorbeeld hoort bij de C van communication en niet louter bij promotie?",
       ["klanten laten reageren in een bevraging", "een grote affiche ophangen in de stationshal", "een reclamespot op de radio laten uitzenden", "folders in alle brievenbussen van de stad steken"], 0,
       "Bij communicatie hoort ook wat de klant terugzegt."),
    tabel("Hoort dit bij de P van promotie?",
          [("een advertentie in een tijdschrift", J), ("een actie in de winkel", J), ("de verpakking van het product", F), ("een post op sociale media", J)],
          "De verpakking hoort bij het product."),
    keuze("Een naam of teken waaraan de klant jouw product herkent, is een [[*merk|doelgroep|kanaal]].",
          "Het merk hoort bij de P van product."),
    mk("Een meubelzaak laat klanten in drie keer betalen zonder extra kosten. Welke P is dat?",
       ["prijs", "plaats", "product", "promotie"], 0,
       "Betalingsvoorwaarden horen bij de prijs."),
    tabel("Welke C past bij deze vraag van een klant?",
          [("Heb ik dit echt nodig?", "customer"), ("Wat kost het mij in geld en tijd?", "cost"), ("Hoe makkelijk geraak ik eraan?", "convenience"), ("Kan ik mijn vraag kwijt bij de winkel?", "communication")],
          "De vier C's zijn de vragen van de klant.",
          kolommen=["customer", "cost", "convenience", "communication"]),
    keuze("Een product voor jongeren vraagt een [[*andere|identieke]] marketingmix dan een product voor zestigplussers.",
          "De mix past zich aan de doelgroep aan."),
    keuze("Bij de P van prijs horen ook de [[*kortingen en betalingsvoorwaarden|verpakking en het merk|reclame en de beurzen]].",
          "Niet enkel het bedrag op het etiket."),
]
