# -*- coding: utf-8 -*-
"""Sociale beïnvloeding: conformisme, inwilliging en gehoorzaamheid.

Het derde en laatste thema over sociale psychologie, en het zwaarste. De fiche
zet sociale beïnvloeding neer als een continuüm van niveaus van sociale druk:
van de zachte druk van een groep tot het bevel van een gezagsfiguur.

De lijstjes staan letterlijk in de fiche:

    toegeven aan sociale beïnvloeding: conformisme, inwilliging,
        gehoorzaamheid
    weerstand bieden: onafhankelijkheid, assertiviteit, trotseren
    theorieën over conformisme: het experiment van Muzafer Sherif, het
        experiment van Solomon Asch, het omstandereffect van John Darley en
        Bibb Latané
    beïnvloedingstechnieken: voet-tussen-de-deur, deur-in-het-gezicht,
        zodra-de-bal-aan-het-rollen-is, dat-is-nog-niet-alles
    theorieën over gehoorzaamheid: het experiment van Stanley Milgram, het
        Stanford gevangenisexperiment van Philip Zimbardo

Twee dingen om niet door elkaar te halen. Conformisme is de druk van een groep
zonder dat iemand iets vraagt; inwilliging is ja zeggen op een verzoek dat wel
gesteld wordt; gehoorzaamheid is doen wat een gezagsfiguur beveelt. En
informatief conformisme is meegaan omdat je de anderen gelooft, normatief
conformisme is meegaan omdat je erbij wil horen.

Deel 1 is conformisme en weerstand bieden.
Deel 2 is inwilliging en gehoorzaamheid.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom noemt de fiche sociale beïnvloeding een continuüm?",
        opties=[
            "omdat de sociale druk van licht tot zwaar loopt",
            "omdat iedereen er op dezelfde manier op reageert",
            "omdat ze alleen in grote groepen voorkomt",
            "omdat ze altijd van een gezagsfiguur komt",
        ],
        antwoord=0,
        uitleg="Een continuüm is een glijdende schaal. De druk van een groep die niets zegt, is lichter dan het bevel van een gezagsfiguur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie vormen van toegeven aan sociale beïnvloeding noemt de fiche?",
        opties=[
            "conformisme",
            "inwilliging",
            "gehoorzaamheid",
            "assertiviteit",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie. Assertiviteit hoort bij de andere kant: weerstand bieden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie vormen van weerstand bieden noemt de fiche?",
        opties=[
            "onafhankelijkheid",
            "assertiviteit",
            "trotseren",
            "inwilliging",
        ],
        antwoord=[0, 1, 2],
        uitleg="Onafhankelijkheid, assertiviteit en trotseren. Inwilliging is juist toegeven aan een verzoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is conformisme?",
        opties=[
            "je gedrag aanpassen aan een groep, zonder dat iets gevraagd is",
            "ja zeggen op een verzoek dat iemand je uitdrukkelijk stelt",
            "doen wat een gezagsfiguur je uitdrukkelijk beveelt",
            "je eigen mening volhouden tegen de groep in",
        ],
        antwoord=0,
        uitleg="Bij conformisme vraagt niemand iets. De aanwezigheid van de groep en haar normen volstaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen conformisme en inwilliging?",
        opties=[
            "bij inwilliging is er een verzoek, bij conformisme niet",
            "bij conformisme is er een verzoek, bij inwilliging niet",
            "conformisme komt van een gezagsfiguur, inwilliging van een groep",
            "conformisme gebeurt bewust, inwilliging gebeurt onbewust",
        ],
        antwoord=0,
        uitleg="Inwilliging is ja zeggen op een vraag die gesteld werd. Conformisme is meegaan met een groep die niets vraagt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is informatief conformisme?",
        opties=[
            "meegaan omdat je denkt dat de anderen het beter weten",
            "meegaan omdat je bij de groep wil blijven horen",
            "meegaan omdat een gezagsfiguur het vraagt",
            "meegaan omdat je er iets voor terugkrijgt",
        ],
        antwoord=0,
        uitleg="Informatief conformisme gaat over kennis: je gebruikt de groep als bron van informatie omdat je het zelf niet zeker weet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is normatief conformisme?",
        opties=[
            "meegaan omdat je erbij wil horen en niet wil opvallen",
            "meegaan omdat je denkt dat de groep het beter weet",
            "meegaan omdat de wet het voorschrijft",
            "meegaan omdat je er een beloning voor krijgt",
        ],
        antwoord=0,
        uitleg="Normatief conformisme gaat over de norm van de groep en over erbij horen, niet over wie het juist heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je staat in een vreemde stad en ziet iedereen voor een rood voetgangerslicht toch oversteken. Je doet mee, want zij kennen de stad. Welk conformisme is dit?",
        opties=[
            "informatief conformisme",
            "normatief conformisme",
            "inwilliging",
            "gehoorzaamheid",
        ],
        antwoord=0,
        uitleg="Je volgt de groep omdat je denkt dat zij beter weten hoe het hier werkt. Dat is informatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vindt een film eigenlijk niet goed, maar zegt met je vrienden mee dat hij mooi was. Welk conformisme is dit?",
        opties=[
            "normatief conformisme",
            "informatief conformisme",
            "inwilliging",
            "trotseren",
        ],
        antwoord=0,
        uitleg="Je weet zelf wat je vond. Je gaat mee om erbij te horen, en dat is normatief.",
    ),
    dict(
        type="invultekst",
        vraag="Meegaan met een groep omdat je denkt dat de anderen het beter weten, heet ... conformisme.",
        antwoord=["informatief", "informatieve"],
        uitleg="Informatief conformisme. Meegaan om erbij te horen is normatief conformisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="In het experiment van Muzafer Sherif moesten proefpersonen in het donker schatten hoeveel een lichtpuntje bewoog. Wat bleek?",
        opties=[
            "in groep schoven hun schattingen naar elkaar toe",
            "in groep gingen hun schattingen verder uiteen",
            "in groep bleven hun schattingen volledig gelijk",
            "in groep weigerden zij nog te schatten",
        ],
        antwoord=0,
        uitleg="Niemand wist het, dus iedereen keek naar de anderen. De groep vormde samen een norm. Dat is informatief conformisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="In het experiment van Solomon Asch moesten proefpersonen zeggen welke lijn even lang was als een voorbeeldlijn. Wat bleek?",
        opties=[
            "velen gaven een zichtbaar fout antwoord mee met de groep",
            "velen gaven altijd hun eigen, juiste antwoord",
            "velen weigerden nog te antwoorden in groep",
            "velen gaven een fout antwoord ook zonder groep",
        ],
        antwoord=0,
        uitleg="De juiste lijn was duidelijk te zien, en toch ging men mee met de anderen. Dat is normatief conformisme: niet uit de groep willen vallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het grote verschil tussen het experiment van Sherif en dat van Asch?",
        opties=[
            "bij Sherif was het antwoord onduidelijk, bij Asch duidelijk",
            "bij Asch was het antwoord onduidelijk, bij Sherif duidelijk",
            "bij Sherif was er een gezagsfiguur, bij Asch niet",
            "bij Asch waren er geen andere proefpersonen aanwezig",
        ],
        antwoord=0,
        uitleg="Daarom hoort Sherif bij informatief conformisme en Asch bij normatief: bij Asch wist men het juiste antwoord en ging men toch mee.",
    ),
    dict(
        type="invultekst",
        vraag="Het experiment met de lijnen, waarbij mensen een zichtbaar fout antwoord van de groep overnamen, is van Solomon ...",
        antwoord=["Asch"],
        uitleg="Solomon Asch. Het experiment met het lichtpuntje in het donker is van Muzafer Sherif.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt het omstandereffect van John Darley en Bibb Latané?",
        opties=[
            "hoe meer omstanders, hoe kleiner de kans dat iemand helpt",
            "hoe meer omstanders, hoe groter de kans dat iemand helpt",
            "hoe meer omstanders, hoe sneller de hulp komt",
            "het aantal omstanders maakt geen enkel verschil",
        ],
        antwoord=0,
        uitleg="Met veel omstanders voelt niemand zich nog persoonlijk verantwoordelijk. De verantwoordelijkheid verspreidt zich over de groep.",
    ),
    dict(
        type="waarofniet",
        vraag="Het omstandereffect komt doordat de verantwoordelijkheid zich over de aanwezigen verspreidt.",
        antwoord=True,
        uitleg="Waar. Iedereen denkt dat iemand anders wel zal ingrijpen, en daardoor grijpt niemand in.",
    ),
    dict(
        type="waarofniet",
        vraag="Iemand rechtstreeks aanspreken in een drukke straat helpt niet tegen het omstandereffect.",
        antwoord=False,
        uitleg="Niet waar. Zodra je iemand persoonlijk aanspreekt, kan hij de verantwoordelijkheid niet meer doorschuiven. Dat is de beste tegenzet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is assertiviteit als vorm van weerstand bieden?",
        opties=[
            "je eigen mening of grens rustig maar duidelijk zeggen",
            "je eigen mening voor jezelf houden in de groep",
            "openlijk tegen een gezagsfiguur ingaan",
            "je volledig door de groep laten sturen",
        ],
        antwoord=0,
        uitleg="Assertief is voor jezelf opkomen zonder de ander aan te vallen. Trotseren gaat een stap verder: openlijk ingaan tegen de druk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grotere en meer eensgezinde groep verhoogt de kans dat iemand conformeert.",
        antwoord=True,
        uitleg="Waar. De fiche vraagt naar de factoren die de bereidheid om te conformeren beïnvloeden. Grootte en eensgezindheid zijn er twee.",
    ),
    dict(
        type="waarofniet",
        vraag="Als er in de groep van Asch één persoon wel het juiste antwoord gaf, bleef de rest even sterk meegaan met de fout.",
        antwoord=False,
        uitleg="Niet waar. Eén medestander breekt de eensgezindheid, en het conformisme zakt sterk. Dat is een van de belangrijkste factoren.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is inwilliging?",
        opties=[
            "ja zeggen op een verzoek dat iemand je stelt",
            "meegaan met een groep die niets vraagt",
            "doen wat een gezagsfiguur beveelt",
            "je eigen grens duidelijk aangeven",
        ],
        antwoord=0,
        uitleg="Bij inwilliging is er een concreet verzoek. Daarom gaan de beïnvloedingstechnieken over inwilliging en niet over conformisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel beïnvloedingstechnieken noemt de fiche?",
        opties=[
            "vier",
            "drie",
            "vijf",
            "zes",
        ],
        antwoord=0,
        uitleg="Vier: voet-tussen-de-deur, deur-in-het-gezicht, zodra-de-bal-aan-het-rollen-is en dat-is-nog-niet-alles.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt de voet-tussen-de-deur-techniek?",
        opties=[
            "eerst een klein verzoek, daarna het grote",
            "eerst een heel groot verzoek, daarna een kleiner",
            "eerst een akkoord, daarna een hogere prijs",
            "eerst een prijs, daarna een extraatje erbij",
        ],
        antwoord=0,
        uitleg="Wie op iets kleins ja zegt, zegt daarna makkelijker ja op iets groter. Het eerste ja zet de deur al open.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt de deur-in-het-gezicht-techniek?",
        opties=[
            "eerst een heel groot verzoek, daarna een kleiner",
            "eerst een klein verzoek, daarna het grote",
            "eerst een akkoord, daarna een hogere prijs",
            "eerst een vraag, daarna een gratis geschenk",
        ],
        antwoord=0,
        uitleg="Het grote verzoek wordt geweigerd, en daarna lijkt het kleinere heel redelijk. De deur slaat eerst dicht, vandaar de naam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt de zodra-de-bal-aan-het-rollen-is-techniek?",
        opties=[
            "je zegt ja, en daarna blijkt de voorwaarde slechter",
            "je weigert eerst, en daarna komt een kleiner verzoek",
            "je krijgt een extraatje voor je kan antwoorden",
            "je zegt ja op iets kleins, en dan komt het grote",
        ],
        antwoord=0,
        uitleg="Het akkoord is er al, en dan komt er een kost bij. Omdat de bal rolt, trekken mensen hun ja niet meer in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt de dat-is-nog-niet-alles-techniek?",
        opties=[
            "je krijgt nog iets extra voor je kan antwoorden",
            "je krijgt eerst een veel te groot verzoek",
            "je zegt ja op iets kleins, en dan komt het grote",
            "je zegt ja, en daarna gaat de prijs omhoog",
        ],
        antwoord=0,
        uitleg="De verkoper doet er iets bij nog voor jij hebt kunnen weigeren. Dat voelt als een gunst, en een gunst wil je teruggeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand vraagt je eerst om een handtekening voor een goed doel, en een week later om vijftig euro. Welke techniek is dit?",
        opties=[
            "voet-tussen-de-deur",
            "deur-in-het-gezicht",
            "zodra-de-bal-aan-het-rollen-is",
            "dat-is-nog-niet-alles",
        ],
        antwoord=0,
        uitleg="Eerst iets kleins waar je moeilijk nee op zegt, daarna het echte verzoek. Dat is de voet tussen de deur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vereniging vraagt of je elke week kan komen helpen. Je zegt nee, en dan vragen ze of je één zaterdag kan komen. Welke techniek is dit?",
        opties=[
            "deur-in-het-gezicht",
            "voet-tussen-de-deur",
            "zodra-de-bal-aan-het-rollen-is",
            "dat-is-nog-niet-alles",
        ],
        antwoord=0,
        uitleg="Na het grote verzoek dat je weigerde, lijkt het kleine heel redelijk. Dat is de deur in het gezicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je spreekt een prijs af voor een tweedehandsfiets, en bij het betalen zegt de verkoper dat de verzending er nog bij komt. Welke techniek is dit?",
        opties=[
            "zodra-de-bal-aan-het-rollen-is",
            "dat-is-nog-niet-alles",
            "voet-tussen-de-deur",
            "deur-in-het-gezicht",
        ],
        antwoord=0,
        uitleg="Het akkoord stond al en daarna kwam de extra kost. Omdat je al ja zei, haak je moeilijker af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een verkoper zegt: deze set kost veertig euro, en kijk, ik doe er nog een tasje bij. Welke techniek is dit?",
        opties=[
            "dat-is-nog-niet-alles",
            "zodra-de-bal-aan-het-rollen-is",
            "voet-tussen-de-deur",
            "deur-in-het-gezicht",
        ],
        antwoord=0,
        uitleg="Er komt iets bij nog voor jij hebt geantwoord. Dat is de dat-is-nog-niet-alles-techniek.",
    ),
    dict(
        type="invultekst",
        vraag="De techniek waarbij eerst een klein verzoek komt en daarna het grote, heet de voet-tussen-de-...-techniek.",
        antwoord=["deur"],
        uitleg="De voet-tussen-de-deur-techniek. Haar tegenhanger is de deur-in-het-gezicht-techniek.",
    ),
    dict(
        type="waarofniet",
        vraag="De beïnvloedingstechnieken werken onder andere omdat mensen hun eigen ja achteraf willen goedpraten.",
        antwoord=True,
        uitleg="Waar. Dat is de cognitieve dissonantie na het instemmen met een verzoek, uit het vorige thema.",
    ),
    dict(
        type="waarofniet",
        vraag="De voet-tussen-de-deur en de deur-in-het-gezicht beginnen beide met een klein verzoek.",
        antwoord=False,
        uitleg="Niet waar. De voet tussen de deur begint klein, de deur in het gezicht begint juist heel groot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is gehoorzaamheid als vorm van sociale beïnvloeding?",
        opties=[
            "doen wat iemand met gezag je opdraagt",
            "meegaan met een groep die niets vraagt",
            "ja zeggen op een verzoek van een gelijke",
            "je eigen grens duidelijk aangeven",
        ],
        antwoord=0,
        uitleg="Bij gehoorzaamheid komt de druk van boven: van iemand met macht of gezag. Dat is het zwaarste punt op het continuüm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat onderzocht Stanley Milgram in zijn experiment?",
        opties=[
            "hoe ver mensen gaan op bevel van een gezagsfiguur",
            "hoe ver mensen meegaan met een groep van gelijken",
            "hoe snel een groep een eigen norm vormt",
            "hoe mensen een oorzaak aan gedrag toeschrijven",
        ],
        antwoord=0,
        uitleg="Proefpersonen moesten op bevel van de onderzoeker stroomstoten geven. Veel meer mensen dan verwacht gingen tot het hoogste niveau.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat onderzocht Philip Zimbardo in het Stanford gevangenisexperiment?",
        opties=[
            "wat een toegewezen rol met het gedrag van mensen doet",
            "wat een groep doet met de schatting van een lichtpuntje",
            "hoe mensen reageren op een verzoek van een verkoper",
            "hoe omstanders reageren bij een noodgeval",
        ],
        antwoord=0,
        uitleg="Studenten kregen de rol van bewaker of gevangene. Het experiment liep zo uit de hand dat het vroeger werd stopgezet dan gepland.",
    ),
    dict(
        type="invultekst",
        vraag="Het experiment waarin proefpersonen op bevel steeds zwaardere stroomstoten moesten geven, is van Stanley ...",
        antwoord=["Milgram"],
        uitleg="Stanley Milgram. Het gevangenisexperiment in Stanford is van Philip Zimbardo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factoren verhogen volgens de fiche de bereidheid om een gezagsfiguur te gehoorzamen?",
        opties=[
            "de gezagsfiguur is dichtbij aanwezig",
            "het slachtoffer is ver weg of niet te zien",
            "er is een gerespecteerde instelling achter de opdracht",
            "er is iemand anders die openlijk weigert",
        ],
        antwoord=[0, 1, 2],
        uitleg="Nabijheid van het gezag, afstand tot het slachtoffer en een instelling met aanzien verhogen de gehoorzaamheid. Iemand die weigert, verlaagt ze juist.",
    ),
    dict(
        type="waarofniet",
        vraag="Zowel het experiment van Milgram als dat van Zimbardo zou vandaag niet meer zo mogen worden uitgevoerd.",
        antwoord=True,
        uitleg="Waar. Beide brachten de proefpersonen in zware nood. Ze staan in de fiche als geschiedenis van het vak, niet als voorbeeld.",
    ),
    dict(
        type="waarofniet",
        vraag="Milgram en Zimbardo tonen dat alleen mensen met een slecht karakter tot zulk gedrag komen.",
        antwoord=False,
        uitleg="Niet waar. Juist het omgekeerde: gewone mensen gingen heel ver door de situatie waarin zij stonden. Dat is de kern van beide experimenten.",
    ),
]
