# -*- coding: utf-8 -*-
"""Sociale zekerheid, uitkeringen en herverdeling.

Het tweede thema uit "ik maak deel uit van een sociaal rechtvaardige
samenleving". Hier zitten de drie rijtjes die de fiche in dit blok oplegt.

De zes types uitkering binnen de sociale zekerheid, in de alfabetische
volgorde van de fiche zelf:
    arbeidsongevallenuitkering; jaarlijks vakantiegeld; rust- en
    overlevingspensioenen; uitkering beroepsziekte; werkloosheidsuitkering;
    ziekte- en invaliditeitsuitkering

De RSZ wordt gefinancierd via de werkgevers, de werknemers en de overheid.
Die drie samen, niet één van de drie.

Het onderscheid dat de fiche apart vraagt:
    vervangingsinkomen   vervangt een loon dat wegvalt (werkloosheid, ziekte,
                         pensioen)
    aanvullend inkomen   komt bovenop een inkomen (vakantiegeld, groeipakket)

En het systeem van herverdeling, in twee soorten:
    fiscaal    progressieve personenbelasting via belastingschijven;
               belastingvrijstellingen en -verminderingen; belastingheffingen
               op vermogen; indirecte belastingen met verschillende tarieven
    sociaal    leefloon; sociale woningen en huurpremies; energiepremies en
               renovatiesteun; studiebeurzen en vermindering inschrijvingsgeld;
               groeipakket; verhoogde tegemoetkoming in de gezondheidszorg;
               mobiliteitskortingen; kansentarieven voor sport en cultuur;
               uitkeringen met herverdelingseffect

Deel 1 is de sociale zekerheid en de zes uitkeringen.
Deel 2 is de herverdeling, fiscaal en sociaal.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Op welk principe steunt de sociale zekerheid volgens de fiche?",
        opties=[
            "solidariteit",
            "winst",
            "eigen verantwoordelijkheid",
            "vrijwilligheid",
        ],
        antwoord=0,
        uitleg="Wie werkt, draagt bij voor wie op dat moment niet kan werken. Dat is solidariteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staat de afkorting RSZ?",
        opties=[
            "Rijksdienst voor Sociale Zekerheid",
            "Rijksdienst voor Sociale Zorg",
            "Regeling Sociale Zekerheid",
            "Raad voor Sociale Zaken",
        ],
        antwoord=0,
        uitleg="De RSZ inde de bijdragen waarmee de sociale zekerheid betaald wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Door wie wordt de RSZ volgens de fiche gefinancierd?",
        opties=[
            "door de werkgevers, de werknemers en de overheid",
            "enkel door de werkgevers",
            "enkel door de werknemers",
            "door de werkgevers en de banken",
        ],
        antwoord=0,
        uitleg="Die drie samen. Op je loonbriefje zie je de bijdrage van de werknemer en die van de werkgever apart staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand verliest zijn werk en krijgt een maandelijks bedrag van de RVA. Welk type uitkering is dat?",
        opties=[
            "een werkloosheidsuitkering",
            "een arbeidsongevallenuitkering",
            "een uitkering beroepsziekte",
            "een ziekte- en invaliditeitsuitkering",
        ],
        antwoord=0,
        uitleg="Werkloosheid is een van de zes types in het rijtje van de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand valt van een ladder tijdens het werk en kan drie maanden niet werken. Welk type uitkering is dat?",
        opties=[
            "een arbeidsongevallenuitkering",
            "een ziekte- en invaliditeitsuitkering",
            "een uitkering beroepsziekte",
            "een werkloosheidsuitkering",
        ],
        antwoord=0,
        uitleg="Een ongeval tijdens het werk valt onder de arbeidsongevallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand wordt ziek door jarenlang met een schadelijke stof te werken. Welk type uitkering is dat?",
        opties=[
            "een uitkering beroepsziekte",
            "een arbeidsongevallenuitkering",
            "een werkloosheidsuitkering",
            "een rust- en overlevingspensioen",
        ],
        antwoord=0,
        uitleg="Geen plots ongeval maar een ziekte door het werk zelf. Dat is een beroepsziekte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand stopt met werken op pensioenleeftijd. Welk type uitkering is dat?",
        opties=[
            "een rustpensioen",
            "een overlevingspensioen",
            "een werkloosheidsuitkering",
            "een ziekte- en invaliditeitsuitkering",
        ],
        antwoord=0,
        uitleg="De fiche noemt rust- en overlevingspensioenen samen. Het overlevingspensioen is voor de partner na een overlijden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een vervangingsinkomen?",
        opties=[
            "een bedrag dat een weggevallen loon vervangt",
            "een bedrag dat bovenop je loon komt",
            "het loon van iemand die je tijdelijk vervangt",
            "het bedrag dat je werkgever inhoudt op je loon",
        ],
        antwoord=0,
        uitleg="Werkloosheid, ziekte en pensioen vervangen een loon dat er niet meer is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een aanvullend inkomen?",
        opties=[
            "een bedrag dat bovenop een inkomen komt",
            "een bedrag dat een weggevallen loon vervangt",
            "het loon van een tweede job",
            "het deel van je loon dat belast wordt",
        ],
        antwoord=0,
        uitleg="Het vakantiegeld en het groeipakket komen bovenop wat je al hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het jaarlijks vakantiegeld: vervangingsinkomen of aanvullend inkomen?",
        opties=[
            "een aanvullend inkomen",
            "een vervangingsinkomen",
            "geen van de twee",
            "beide, afhankelijk van je statuut",
        ],
        antwoord=0,
        uitleg="Het komt bovenop je loon en vervangt dus niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Een werkloosheidsuitkering is een vervangingsinkomen.",
        antwoord=True,
        uitleg="Ze neemt de plaats in van het loon dat weggevallen is.",
    ),
    dict(
        type="waarofniet",
        vraag="De RSZ wordt enkel door de werkgevers gefinancierd.",
        antwoord=False,
        uitleg="Door de werkgevers, de werknemers en de overheid samen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het jaarlijks vakantiegeld staat volgens de fiche bij de uitkeringen binnen de sociale zekerheid.",
        antwoord=True,
        uitleg="Het staat in het rijtje van zes, al is het een aanvullend inkomen en geen vervangingsinkomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een arbeidsongeval en een beroepsziekte zijn volgens de fiche hetzelfde.",
        antwoord=False,
        uitleg="Twee verschillende types uitkering: het ene komt van een ongeval, het andere van het werk zelf over langere tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitkeringen noemt de fiche binnen de sociale zekerheid?",
        opties=[
            "de werkloosheidsuitkering",
            "de ziekte- en invaliditeitsuitkering",
            "de arbeidsongevallenuitkering",
            "de studiebeurs",
        ],
        antwoord=[0, 1, 2],
        uitleg="De studiebeurs staat bij de sociale herverdelingsmaatregelen, niet bij de uitkeringen van de sociale zekerheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn een vervangingsinkomen?",
        opties=[
            "de werkloosheidsuitkering",
            "het rustpensioen",
            "de ziekte- en invaliditeitsuitkering",
            "het jaarlijks vakantiegeld",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het vakantiegeld komt bovenop een loon en is dus aanvullend.",
    ),
    dict(
        type="invultekst",
        vraag="Op welk principe steunt de sociale zekerheid? Antwoord met één woord.",
        antwoord=["solidariteit", "de solidariteit"],
        uitleg="Wie kan, draagt bij voor wie op dat moment niet kan.",
    ),
    dict(
        type="invultekst",
        vraag="Welke dienst int in België de bijdragen voor de sociale zekerheid? Antwoord met de afkorting.",
        antwoord=["RSZ", "rsz"],
        uitleg="De Rijksdienst voor Sociale Zekerheid, gefinancierd door werkgevers, werknemers en overheid.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een bedrag dat een weggevallen loon vervangt? Antwoord met één woord.",
        antwoord=["vervangingsinkomen", "een vervangingsinkomen"],
        uitleg="Het tegenovergestelde is een aanvullend inkomen, dat bovenop een inkomen komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een partner overlijdt en de achterblijvende partner krijgt een pensioen. Hoe heet dat?",
        opties=[
            "een overlevingspensioen",
            "een rustpensioen",
            "een uitkering beroepsziekte",
            "een arbeidsongevallenuitkering",
        ],
        antwoord=0,
        uitleg="De fiche noemt rust- en overlevingspensioenen samen als één type uitkering.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is herverdeling?",
        opties=[
            "de overheid verschuift middelen van sterkere naar zwakkere schouders",
            "de overheid verdeelt haar uitgaven gelijk over alle gemeenten",
            "de overheid verdeelt de belastingen over het jaar",
            "de overheid verdeelt het werk over de bedrijven",
        ],
        antwoord=0,
        uitleg="De fiche koppelt herverdeling aan het beperken van de sociale ongelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit welke twee soorten maatregelen bestaat het systeem van herverdeling?",
        opties=[
            "fiscale en sociale maatregelen",
            "directe en indirecte maatregelen",
            "federale en Vlaamse maatregelen",
            "tijdelijke en blijvende maatregelen",
        ],
        antwoord=0,
        uitleg="De fiche deelt het rijtje in die twee groepen op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een progressieve personenbelasting?",
        opties=[
            "wie meer verdient, betaalt een hoger percentage",
            "iedereen betaalt hetzelfde percentage",
            "wie meer verdient, betaalt een lager percentage",
            "het percentage stijgt elk jaar een beetje",
        ],
        antwoord=0,
        uitleg="Dat gebeurt via belastingschijven: elk stuk van je inkomen valt in een eigen schijf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt de progressieve belasting volgens de fiche in de praktijk?",
        opties=[
            "via belastingschijven",
            "via een vast tarief voor iedereen",
            "via een korting voor wie veel verdient",
            "via de btw op aankopen",
        ],
        antwoord=0,
        uitleg="Belastingschijven staan letterlijk in de fiche bij de progressieve personenbelasting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leefloon voor wie geen enkel inkomen heeft. Welke soort maatregel is dat?",
        opties=[
            "een sociale herverdelingsmaatregel",
            "een fiscale herverdelingsmaatregel",
            "een uitkering binnen de sociale zekerheid",
            "een inkomst van de overheid",
        ],
        antwoord=0,
        uitleg="Het leefloon is een sociale bijstandsuitkering en staat vooraan in het sociale rijtje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een belastingvermindering voor wie zijn dak isoleert. Welke soort maatregel is dat?",
        opties=[
            "een fiscale herverdelingsmaatregel",
            "een sociale herverdelingsmaatregel",
            "een diverse inkomst van de overheid",
            "een collectieve behoefte",
        ],
        antwoord=0,
        uitleg="Belastingvrijstellingen en -verminderingen staan in het fiscale rijtje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een studiebeurs en een vermindering van het inschrijvingsgeld. Welke soort maatregel is dat?",
        opties=[
            "een sociale herverdelingsmaatregel",
            "een fiscale herverdelingsmaatregel",
            "een aanvullend inkomen uit de sociale zekerheid",
            "een vergoeding voor een dienst",
        ],
        antwoord=0,
        uitleg="Ze staan samen in het sociale rijtje, naast het groeipakket en de energiepremies.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kansentarief voor de sportclub. Welke soort maatregel is dat?",
        opties=[
            "een sociale herverdelingsmaatregel",
            "een fiscale herverdelingsmaatregel",
            "een uitgave voor economische groei",
            "een indirecte belasting",
        ],
        antwoord=0,
        uitleg="Kansentarieven voor sport en cultuur staan in het sociale rijtje van de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het groeipakket?",
        opties=[
            "de Vlaamse steun voor gezinnen met kinderen",
            "een spaarplan voor jongeren",
            "een premie voor wie een huis bouwt",
            "een korting op het openbaar vervoer",
        ],
        antwoord=0,
        uitleg="Het staat in het sociale rijtje van de herverdelingsmaatregelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn er indirecte belastingen met verschillende tarieven?",
        opties=[
            "zodat noodzakelijke producten lichter belast worden dan luxe",
            "zodat elke winkel zijn eigen tarief kan kiezen",
            "zodat de overheid elk jaar meer kan innen",
            "zodat dure producten vrijgesteld blijven",
        ],
        antwoord=0,
        uitleg="Daarom staat deze maatregel in de fiche bij de fiscale herverdeling.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een progressieve belasting betaalt iedereen hetzelfde percentage.",
        antwoord=False,
        uitleg="Dan zou ze vlak zijn. Progressief betekent dat het percentage stijgt met het inkomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het leefloon is volgens de fiche een sociale bijstandsuitkering.",
        antwoord=True,
        uitleg="Zo staat het er, in het rijtje van de sociale herverdelingsmaatregelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een belastingheffing op vermogen is een sociale herverdelingsmaatregel.",
        antwoord=False,
        uitleg="Ze is fiscaal: ze werkt via de belastingen, niet via een uitkering of een premie.",
    ),
    dict(
        type="waarofniet",
        vraag="Uitkeringen zoals pensioenen hebben volgens de fiche een herverdelingseffect.",
        antwoord=True,
        uitleg="Ze staan met zoveel woorden in het sociale rijtje als uitkeringen met herverdelingseffect.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze noemt de fiche als fiscale herverdelingsmaatregel?",
        opties=[
            "de progressieve personenbelasting via belastingschijven",
            "belastingvrijstellingen en -verminderingen",
            "belastingheffingen op vermogen",
            "het groeipakket",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het groeipakket is sociaal. De vierde fiscale maatregel is die van de verschillende tarieven bij indirecte belastingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze noemt de fiche als sociale herverdelingsmaatregel?",
        opties=[
            "sociale woningen en huurpremies",
            "energiepremies en renovatiesteun",
            "de verhoogde tegemoetkoming in de gezondheidszorg",
            "de onroerende voorheffing",
        ],
        antwoord=[0, 1, 2],
        uitleg="De onroerende voorheffing is een belasting, dus een inkomst, geen sociale maatregel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet een belasting waarbij het percentage stijgt met het inkomen? Antwoord met één woord.",
        antwoord=["progressief", "progressieve"],
        uitleg="Ze werkt via belastingschijven.",
    ),
    dict(
        type="invultekst",
        vraag="Welke sociale bijstandsuitkering noemt de fiche voor wie geen inkomen heeft?",
        antwoord=["leefloon", "het leefloon"],
        uitleg="Het staat vooraan in het rijtje van de sociale herverdelingsmaatregelen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de Vlaamse steun voor gezinnen met kinderen? Antwoord met één woord.",
        antwoord=["groeipakket", "het groeipakket"],
        uitleg="Het staat in het sociale rijtje, naast de studiebeurzen en de energiepremies.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee gezinnen met hetzelfde loon, maar het ene krijgt een huurpremie en een kansentarief. Wat gebeurt hier?",
        opties=[
            "herverdeling via sociale maatregelen",
            "herverdeling via fiscale maatregelen",
            "een uitkering binnen de sociale zekerheid",
            "een vergoeding voor een dienst",
        ],
        antwoord=0,
        uitleg="Huurpremies en kansentarieven staan beide in het sociale rijtje van de herverdeling.",
    ),
]
