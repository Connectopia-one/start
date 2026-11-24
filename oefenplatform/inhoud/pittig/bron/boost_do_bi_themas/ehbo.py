"""Levensreddend handelen — pittig (🚀 Boost doorstroom, biologie).

Klikvragen op de romp en vragen over reanimatie en verslikking van natuurwetenschappen Boost doorstroom (met de prent), plus eigen casussen over bloedingen, brandwonden, shock en botbreuken uit bi_ehbo. Richtlijnen van het Rode Kruis."""
from ..boost_do_nw_themas import veilig as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [3, 4, 11, 12, 13, 14, 15, 21, 22, 27])
VRAGEN += [
    casus("In de keuken giet Arne per ongeluk kokend water over zijn onderarm. De huid wordt rood en er komen blaren op.", [
        tabel("Wat doe je bij de brandwond van Arne?",
              [("ongeveer twintig minuten koelen met lauw stromend water", J), ("er boter of tandpasta op doen", F), ("de blaren zelf openprikken", F), ("ringen en een horloge voorzichtig uittrekken voor de arm opzwelt", J)],
              "Koelen haalt de warmte weg; vette stoffen houden ze vast en een blaar beschermt de wonde."),
        mk("Waarom koel je met lauw water en niet met ijs?",
           ["IJs kan de huid nog meer beschadigen.", "Lauw water maakt de blaren sneller open zodat de wonde kan drogen.", "IJs zou de pijn helemaal wegnemen en dat mag niet bij een brandwond.", "Lauw water bevat meer zuurstof voor de huidcellen dan ijswater."], 0,
           "Te koud geeft schade en kan bij een grote wonde onderkoeling geven."),
    ]),
    casus("Op de speelplaats valt Lina met haar arm op een glasscherf. Er komt veel bloed uit de wonde.", [
        volgorde("Zet de eerste hulp in de juiste volgorde.",
                 ["Kijk of de plaats veilig is en trek handschoenen aan.", "Druk met een propere doek stevig op de wonde.", "Houd de arm hoger dan het hart.", "Laat 112 bellen als het bloeden niet stopt."],
                 "Eerst veiligheid, dan druk, hoogte en hulp."),
        tabel("Klopt dit over de bloeding van Lina?",
              [("Een arm hoger houden dan het hart remt het bloeden.", J), ("Handschoenen beschermen enkel Lina en niet de helper.", F), ("Een glasscherf die diep in de wonde zit, trek je er niet uit.", J)],
              "Handschoenen beschermen beide; een vastzittend voorwerp kan juist het bloed tegenhouden."),
    ]),
    sorteer("Doe je dit wel of niet?", ["Wel doen", "Niet doen"],
            [("een slachtoffer in shock iets te drinken geven", "Niet doen"), ("een bewusteloos slachtoffer dat normaal ademt in stabiele zijligging leggen", "Wel doen"), ("een vermoedelijk gebroken arm zelf rechtzetten", "Niet doen"), ("bij een nek- of rugletsel het slachtoffer laten liggen", "Wel doen"), ("iemand met een epileptische aanval stevig vasthouden", "Niet doen")],
            "Vaak is niets doen beter dan iets verkeerds: niet rechtzetten, niet drinken, niet vasthouden bij een aanval."),
    tabel("Welke tekens kunnen op shock wijzen?",
          [("een bleke, klamme huid", J), ("een snelle, zwakke pols", J), ("een rood, warm gezicht en trage hartslag", F), ("onrustig of suf worden", J)],
          "Bij shock krijgen de organen te weinig bloed."),
    mk("Iemand klaagt over drukkende pijn in de borst die uitstraalt naar de linkerarm. Wat doe je?",
       ["Je belt 112 en laat de persoon rusten.", "Je laat de persoon een stevige wandeling maken.", "Je geeft de persoon een groot glas koud water.", "Je wacht een uur af of de pijn vanzelf weggaat."], 0,
       "Dat kan een hartaanval zijn: snel hulp, geen inspanning."),
    casus("In het station zakt een man in elkaar. Hij reageert niet en ademt niet normaal. Er hangt een AED aan de muur.", [
        mk("Je kleeft de elektroden van de AED op de borst van de man. Wat doet het toestel dan?",
           ["Hij meet het hartritme en geeft enkel een schok als het nodig is.", "Hij geeft automatisch borstcompressies in de plaats van de helper.", "Hij belt zelf de hulpdiensten en wacht dan af.", "Hij meet de bloeddruk en geeft medicijnen via de huid."], 0,
           "Het toestel beslist zelf of er een schok nodig is."),
        tabel("Klopt dit over de AED?",
              [("Iemand zonder opleiding mag hem gebruiken.", J), ("Het toestel spreekt je stap voor stap toe.", J), ("Tijdens de schok raakt niemand het slachtoffer aan.", J), ("Je stopt de hartmassage voorgoed zodra de AED er is.", F)],
              "Na de schok ga je meteen door met hartmassage tot het toestel iets anders zegt."),
        mk("Je staat er alleen voor. Wat doe je eerst?",
           ["112 bellen met de luidspreker aan en hartmassage geven.", "Eerst de AED gaan halen en dan pas 112 bellen.", "Wachten tot er iemand anders bij komt die het beter kan.", "De man rechtop zetten tegen een muur zodat hij lucht krijgt."], 0,
           "Met de luidspreker aan kan de meldkamer je helpen terwijl je reanimeert."),
    ]),
    koppel("Welke eerste hulp hoort bij elke situatie?",
           [("een vermoedelijke botbreuk in een arm", "de arm steunen zoals hij ligt en hulp bellen"), ("hevige bloeding", "stevig drukken op de wonde"), ("brandwond", "twintig minuten koelen met lauw water"), ("verslikking zonder hoesten", "vijf slagen tussen de schouderbladen")],
           ["een glas water geven", "de blaar openprikken"], "Vier situaties, vier aanpakken."),
    keuze("Bij een hitteslag koel je het lichaam met [[*lauw water|ijsblokjes|alcohol]], zodat de bloedvaten niet dichtknijpen.",
          "Te koud vernauwt de bloedvaten in de huid, waardoor de warmte binnenblijft."),
    tabel("Wat vertel je zeker als je 112 belt?",
          [("waar je precies bent", J), ("wat er gebeurd is", J), ("hoeveel slachtoffers er zijn", J), ("de naam van je school", F)],
          "Met plaats, gebeurtenis en aantal kan de meldkamer de juiste hulp sturen."),
    mk("Waarom duw je bij een volwassene het borstbeen vijf tot zes centimeter in, en niet één?",
       ["Alleen zo pompt het hart genoeg bloed rond.", "Om de ribben te breken, zodat het hart vrij kan bewegen.", "Omdat de longen anders niet vanzelf opnieuw gaan ademen.", "Om de AED te helpen het hartritme beter te meten."], 0,
       "Te ondiep duwen pompt nauwelijks bloed naar de hersenen."),
    tabel("Klopt dit over reanimatie?",
          [("Je geeft 30 borstcompressies en dan 2 beademingen.", J), ("Je duwt ongeveer 100 tot 120 keer per minuut.", J), ("Je onderbreekt de hartmassage zo vaak mogelijk om te kijken.", F), ("Begint het slachtoffer weer normaal te ademen, dan leg je het in stabiele zijligging.", J)],
          "Zo min mogelijk onderbreken: elke pauze laat de bloeddruk zakken."),
    mk("Waarom kijk je bij een ongeval eerst of de plaats veilig is?",
       ["Een tweede slachtoffer helpt niemand.", "Zo kan je de schuldige van het ongeval aanwijzen.", "Omdat de hulpdiensten dat altijd als eerste vragen aan de telefoon.", "Zo weet je of het slachtoffer nog bij bewustzijn is."], 0,
       "Wie zelf gewond raakt, kan niet meer helpen en geeft de hulpdiensten extra werk."),
    tabel("Wat hoort in een eenvoudige verbanddoos?",
          [("steriele compressen", J), ("een rol kleefpleister", J), ("wegwerphandschoenen", J), ("pijnstillers voor iedereen", F)],
          "Geneesmiddelen horen niet in een gewone verbanddoos voor iedereen."),
    mk("Waarom is het nuttig dat zoveel mogelijk mensen kunnen reanimeren?",
       ["De eerste minuten tellen, en de hulpdiensten zijn er niet meteen.", "Dan hoeft er nooit meer een ziekenwagen te komen.", "Omdat het hart zonder hulp nooit meer begint te kloppen.", "Zo kunnen de hulpdiensten minder AED-toestellen kopen."], 0,
       "Elke minuut zonder hartmassage daalt de overlevingskans fors."),
]
