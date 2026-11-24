"""Een Engelse tekst analyseren — pittig (🚀 Boost, Engels).

Eigen leesteksten op niveau B1/A2 met vragen die verder gaan dan letterlijk
lezen. Dezelfde vragen voor doorstroom en dubbele finaliteit."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

T1 = (
    "Read the text.\n\n"
    "(1) Last summer, the town of Kingsford closed its main street to cars every Saturday. "
    "(2) The council hoped that more people would walk and cycle to the shops. "
    "(3) At first, many shop owners were worried. They thought customers would stay away. "
    "(4) After three months, however, most shops sold more than before. "
    "(5) Only the hardware store lost customers, because people could not carry heavy things to their cars. "
    "(6) The council has now decided to keep the car-free Saturdays, but it will open a small car park near the hardware store."
)

T2 = (
    "Read the advertisement.\n\n"
    "SUMMER JOBS AT GREENWAY ZOO\n"
    "Are you 16 or older? Do you love animals? We are looking for students to help in our café and gift shop "
    "from 1 July to 31 August. You will work four days a week, from 10 a.m. to 4 p.m. "
    "Weekend work is paid extra. You don't need any experience, but you must speak English and one other language. "
    "Free entrance for your family during the summer!\n"
    "Send your CV and a short letter to jobs@greenwayzoo.co.uk before 15 May."
)

T3 = (
    "Read the two messages.\n\n"
    "Message A – from Lily: Hi Tom! Are you still coming to the cinema on Friday? The film starts at 8, so let's meet at the station at 7.30. "
    "My sister is coming too, I hope that's OK.\n\n"
    "Message B – from Tom: Hi Lily, sorry, I can't make it on Friday. My grandma is visiting us. "
    "What about Saturday afternoon? There's a show at 3. Say hi to your sister!"
)

T4 = (
    "Read the review.\n\n"
    "I visited the new climbing centre in Leeds with two friends last weekend. "
    "The walls are great for beginners, and the staff explained everything very clearly. "
    "The café, on the other hand, was a disappointment: the sandwiches were dry and very expensive. "
    "We paid £15 each for two hours, which I think is fair. "
    "I will definitely go back, but next time I'll bring my own lunch. ★★★★☆"
)

VRAGEN = [
    casus(T1, [
        mk("Wat is de hoofdgedachte van de tekst?",
           ["De autovrije zaterdag is een succes.", "Winkeliers willen absoluut geen autovrije straat.", "De ijzerwinkel moet verhuizen naar een parking.", "Fietsen is veel gezonder dan autorijden."], 0,
           "Zin 4 en 6: de meeste winkels verkopen meer, en het plan blijft."),
        mk("Welk verband legt however in zin 4?",
           ["een tegenstelling", "een voorbeeld bij zin 3", "een oorzaak van zin 3", "een opsomming na zin 3"], 0,
           "De winkeliers waren bang, maar het liep anders af."),
        tabel("Staat dit in de tekst?",
              [("De straat is elke dag autovrij.", F), ("De ijzerwinkel verloor klanten.", J), ("Er komt een kleine parking bij de ijzerwinkel.", J), ("Alle winkeliers waren van in het begin tevreden.", F)],
              "Lees nauwkeurig: every Saturday, at first many were worried."),
        inv("Naar welk woord verwijst They in zin 3? Schrijf het Engelse woord of de woordgroep.", ["shop owners", "many shop owners", "the shop owners"],
            "They verwijst naar de shop owners uit de zin ervoor."),
        mk("Waarom komt er een parking bij de ijzerwinkel?",
           ["Klanten kunnen zware spullen niet ver dragen.", "De gemeente wil weer auto's in de straat.", "De ijzerwinkel verkoopt meer dan andere winkels.", "Er is te weinig plaats voor fietsen."], 0,
           "Zin 5 geeft de reden, zin 6 de oplossing."),
    ]),
    casus(T2, [
        tabel("Kan deze persoon solliciteren?",
              [("Sara, 15 jaar, spreekt Engels en Frans.", F), ("Milan, 17 jaar, spreekt Engels en Nederlands, nog nooit gewerkt.", J), ("Jonas, 18 jaar, spreekt enkel Engels.", F)],
              "Je moet 16 zijn en twee talen spreken; ervaring is niet nodig.", ),
        inv("Hoeveel uur werk je per dag? Schrijf het getal.", ["6", "zes", "6 uur"],
            "From 10 a.m. to 4 p.m. is zes uur."),
        mk("Wat krijgt je familie?",
           ["gratis toegang in de zomer", "korting in het café van de zoo", "een gratis jaarabonnement voor de zoo", "extra loon voor elk weekend"], 0,
           "Free entrance for your family during the summer."),
        mk("Wat moet je opsturen?",
           ["een cv en een korte brief", "enkel een foto van jezelf", "een diploma en een rapport", "een brief van je ouders"], 0,
           "Send your CV and a short letter."),
        inv("Tot wanneer kan je solliciteren? Schrijf de datum zoals in de tekst.", ["15 May", "15 may", "before 15 May"],
            "Before 15 May: daarna is het te laat."),
    ]),
    casus(T3, [
        tabel("Klopt dit?",
              [("Tom gaat op vrijdag mee naar de film.", F), ("Lily's zus gaat ook mee.", J), ("Tom stelt zaterdagnamiddag voor.", J)],
              "Tom kan vrijdag niet en stelt zelf een ander moment voor."),
        mk("Waarom kan Tom vrijdag niet?",
           ["Zijn oma komt op bezoek.", "Hij moet die avond werken in de zoo.", "Hij vindt de film helemaal niet goed.", "Hij is ziek en moet thuisblijven."], 0,
           "My grandma is visiting us."),
        inv("Om hoe laat begint de film op zaterdag? Schrijf het uur als getal.", ["3", "15", "3 uur", "15 uur", "3 p.m."],
            "There's a show at 3."),
    ]),
    tabel("Welk soort lezen past bij deze opdracht?",
          [("Je zoekt in een treinregeling hoe laat de trein vertrekt.", "zoekend lezen"), ("Je wil weten waar een artikel ongeveer over gaat.", "globaal lezen"), ("Je moet een handleiding stap voor stap volgen.", "intensief lezen")],
          "Je leesstrategie hangt af van je doel.", ["zoekend lezen", "globaal lezen", "intensief lezen"]),
    mk("In een tekst staat: 'The museum is closed on Mondays. It opens at 9 on all other days.' Je wil op maandag om 10 uur gaan. Wat besluit je?",
       ["Je kan niet binnen.", "Je kan om 9 uur al binnen.", "Je kan binnen vanaf 10 uur.", "Je moet om 9 uur bellen."], 0,
       "De info staat niet letterlijk bij jouw vraag: je moet ze combineren."),
    tabel("Een reclame zegt: 'Buy two pizzas, get the third one free!' Klopt dit?",
          [("Wie drie pizza's neemt, betaalt er twee.", J), ("Wie één pizza neemt, krijgt er een gratis.", F), ("De tekst wil je overtuigen om meer te kopen.", J)],
          "Een reclame is een overtuigende tekst."),
    keuze("'Despite the rain, the match went on.' De wedstrijd werd [[*toch gespeeld|afgelast|uitgesteld]].",
          "Despite betekent ondanks."),
    sleep("Bij een leestekst lees je eerst de [[titel]] en de vragen. Dan zoek je de [[sleutelwoorden]] in de tekst. Wat niet letterlijk staat, leid je af uit het [[verband]] tussen zinnen.",
          ["einde", "vertaling"], "Een goede leesstrategie bespaart tijd."),
    mk("'Tickets are £12 for adults and half price for children under 12.' Hoeveel betaalt een kind van 10?",
       ["£6", "£12", "£24", "niets"], 0,
       "Half price van £12 is £6."),
    tabel("Lees de zin: 'Although she was tired, Maya finished her homework before dinner.' Klopt dit?",
          [("Maya was moe.", J), ("Maya maakte haar huiswerk na het eten.", F), ("Although drukt een tegenstelling uit.", J)],
          "Although = hoewel."),
    casus(T4, [
        tabel("Wat vindt de schrijver goed en wat niet?",
              [("de klimmuren", "goed"), ("het personeel", "goed"), ("het café", "niet goed"), ("de prijs", "goed")],
              "Lees de bijvoeglijke woorden: great, clearly, disappointment, fair.", ["goed", "niet goed"]),
        mk("Wat zal de schrijver de volgende keer anders doen?",
           ["eigen eten meebrengen", "alleen gaan klimmen", "langer dan twee uur blijven", "in het café eten"], 0,
           "Next time I'll bring my own lunch."),
        inv("Hoeveel betaalden de drie vrienden samen, in pond? Schrijf het getal.", ["45", "£45", "45 pond"],
            "£15 each, drie personen: 45 pond."),
        keuze("De schrijver geeft het klimcentrum [[*vier|vijf|drie]] sterren.",
              "Vier volle sterren en een lege."),
        mk("Voor wie is het klimcentrum vooral geschikt, volgens de tekst?",
           ["beginners", "profklimmers", "kleine kinderen", "ouderen"], 0,
           "The walls are great for beginners."),
    ]),
    tabel("Lees: 'The library is open from Monday to Friday. On Saturdays it closes at noon.' Klopt dit?",
          [("Op zaterdagnamiddag is de bib dicht.", J), ("Op zondag is de bib open.", F), ("Op woensdag is de bib open.", J)],
          "Noon is 12 uur 's middags; zondag wordt niet vermeld bij de open dagen."),
    mk("'Please do not feed the animals.' Waar lees je dit waarschijnlijk?",
       ["in een dierentuin", "in een bibliotheek", "in een zwembad", "in een klaslokaal"], 0,
       "Feed the animals: dieren voederen."),
    tabel("In een e-mail staat: 'I'm afraid I won't be able to attend the meeting.' Klopt dit?",
          [("De schrijver komt niet naar de vergadering.", J), ("De schrijver is echt bang.", F), ("I'm afraid maakt het bericht beleefder.", J)],
          "I'm afraid betekent hier 'helaas'."),
    sorteer("Feit of mening?", ["feit", "mening"],
            [("The film lasts two hours.", "feit"), ("The film is boring.", "mening"), ("The shop opens at 9.", "feit"), ("This is the best pizza in town.", "mening")],
            "Een feit kan je controleren, een mening niet."),
    keuze("'Unless it rains, we will play outside.' Ze spelen binnen [[*als het regent|als de zon schijnt|altijd]].",
          "Unless = tenzij."),
]
