# -*- coding: utf-8 -*-
"""Uitdaging Sociale en gedragswetenschappen 🌍 Beyond (25 november 2026), in
de vormen van het examen van de Examencommissie: 40 vragen die ontwikkeling,
sociale psychologie, persoonlijkheid, opvoeding, communicatie, sociologie,
media en onderzoek door elkaar halen. Casussen, tabellen, keuzelijsten,
koppelen, sorteren, volgorde, vier klikvragen op twee zelf getekende
prenten en een open vraag. Geen nieuwe leerstof: alles staat in de
hoofdstukken van Sociale en gedragswetenschappen Beyond.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_sgw.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Sociale en gedragswetenschappen"
BESTAND = "beyond-sgw-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/sgw-beyond-uitdaging"
LIJNEN = "lijnenproef.svg"
BALLONNEN = "vier-ballonnen.svg"
# klikvakken: zie maak_prenten_beyond_sgw.py
LIJN_C = [79.5, 19.2, 11.0, 67.3]
BALLON = {"1": [4.0, 13.3, 44.0, 33.3], "2": [52.0, 13.3, 44.0, 33.3], "3": [4.0, 55.0, 44.0, 33.3], "4": [52.0, 55.0, 44.0, 33.3]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Een lijnenproef (prent)
    klik("Bekijk de kaart van de lijnenproef. Klik op de lijn die even lang is als de standaardlijn.",
         LIJNEN, [LIJN_C],
         "Lijn C is even lang als de standaardlijn. Alleen zie je het in zo'n proef meestal zonder twijfelen."),
    met_prent(LIJNEN, mk(
        "In de proef zeggen zes medeleerlingen, die in het complot zitten, luid 'B'. Daarna zegt ook Ella 'B', al ziet ze dat het C is. Welk soort conformisme is dit?",
        ["informatief conformisme, want ze twijfelt echt", "normatief conformisme, om erbij te horen", "inwilliging, want iemand stelde haar een verzoek", "gehoorzaamheid, want een gezagsfiguur gaf een bevel"],
        1,
        "Ella weet het juiste antwoord, maar past zich aan om erbij te horen: normatief conformisme. Er is geen verzoek en geen bevel.")),
    met_prent(LIJNEN, keuze(
        "Deze proef lijkt op het experiment van [[*Asch|Sherif|Milgram]]. Daarin was het juiste antwoord [[*duidelijk|onduidelijk]], wat het verschil is met het experiment van Sherif.",
        "Bij Sherif was het antwoord onduidelijk (een lichtpuntje dat leek te bewegen), dus volgden mensen de groep uit onzekerheid. Bij Asch zag iedereen het juiste antwoord.")),
    met_prent(LIJNEN, tabel(
        "Klopt dit over conformisme?",
        [
            ("Bij conformisme stelt niemand je rechtstreeks een vraag.", J),
            ("Wie alleen moet antwoorden, zonder groep, vergist zich bij deze kaart bijna nooit.", J),
            ("Gehoorzaamheid is de lichtste vorm van sociale druk.", F),
        ],
        "Sociale beïnvloeding loopt van licht (conformisme) over inwilliging naar zwaar (gehoorzaamheid aan een bevel).")),

    # Vier zinnen van een ouder (prent)
    klik("Bekijk de vier zinnen. Klik op de ik-boodschap.",
         BALLONNEN, [BALLON["2"]],
         "Zin 2 beschrijft het gedrag, het gevolg voor de ouder en het gevoel, zonder de tiener een etiket te geven: een ik-boodschap."),
    klik("Klik op de zin waarin de ouder actief luistert door te parafraseren.",
         BALLONNEN, [BALLON["3"]],
         "Zin 3 zegt in eigen woorden wat de tiener bedoelt en checkt of dat klopt: parafraseren, een vorm van actief luisteren."),
    met_prent(BALLONNEN, mk(
        "Waarom is zin 4 in verbindend communiceren een eis en geen verzoek?",
        ["Omdat de tiener niet vrij nee kan zeggen.", "Omdat de ouder er een gevoel in noemt.", "Omdat de zin in de jij-vorm staat.", "Omdat de ouder de tiener een vraag stelt en wacht."],
        0,
        "Bij een verzoek mag de ander nee zeggen. Met 'anders mag je niet weg' is er geen keuze meer: een eis.")),
    met_prent(BALLONNEN, mk(
        "In zin 1 verklaart de ouder het gedrag met 'jij bent gewoon lui'. Welke attributie is dat?",
        ["een externe attributie, want de oorzaak ligt in de situatie", "een interne attributie, want de oorzaak ligt in de persoon", "geen attributie, want er wordt niets verklaard", "een attributie aan het toeval"],
        1,
        "De ouder zoekt de oorzaak in een eigenschap van de tiener zelf: een interne attributie, en ook een stabiele.")),
    met_prent(BALLONNEN, tabel(
        "Klopt dit over de vier zinnen?",
        [
            ("Zin 1 is een jij-boodschap.", J),
            ("Een ik-boodschap legt de schuld bij de ander.", F),
            ("Ook toon en lichaamstaal geven deze zinnen mee richting.", J),
        ],
        "Een jij-boodschap plakt een etiket op de ander. Een ik-boodschap vertelt wat het gedrag met jou doet. Non-verbaal gedrag stuurt een gesprek mee.")),

    # Casus: Lina en haar systemen
    casus(
        "Lina is negen. Ze woont bij haar mama en haar broer. Haar juf belt soms met mama over haar huiswerk. Mama werkt in ploegen in een fabriek. Lina groeit op in een cultuur waar veel waarde gehecht wordt aan diploma's. Vorig jaar gingen haar ouders uit elkaar.",
        [
            tabel(
                "Bij welk systeem van Bronfenbrenner hoort elk stukje van Lina's leven?",
                [
                    ("haar gezin", "Microsysteem"),
                    ("de juf die met mama belt", "Mesosysteem"),
                    ("de ploegendienst van mama", "Exosysteem"),
                    ("het belang van diploma's in haar cultuur", "Macrosysteem"),
                    ("de scheiding van vorig jaar", "Chronosysteem"),
                ],
                "Het microsysteem is waar Lina zelf in zit. Het mesosysteem verbindt twee microsystemen. Het exosysteem raakt haar onrechtstreeks. Het macrosysteem is de cultuur, het chronosysteem de tijd en de veranderingen.",
                kolommen=["Microsysteem", "Mesosysteem", "Exosysteem", "Macrosysteem", "Chronosysteem"]),
            mk("Bij welke benadering van ontwikkeling hoort deze manier van kijken?",
               ["de systemische benadering", "de psychodynamische benadering", "de biologische benadering", "de behavioristische benadering"],
               0,
               "De systemische benadering kijkt naar alles wat rond iemand staat en op hem inwerkt."),
            keuze(
                "Lina rekent goed met echte blokjes, maar een som met letters lukt nog niet. Volgens Piaget zit ze in het [[*concreet-operationele|formeel-operationele|sensomotorische]] stadium.",
                "In het concreet-operationele stadium denkt een kind logisch over concrete dingen. Abstract denken met symbolen komt in het formeel-operationele stadium."),
        ],
    ),

    # Casus: thuis bij de familie Peeters
    casus(
        "Bij de familie Peeters is er veel warmte en wordt er veel gepraat. Er zijn ook duidelijke afspraken: om tien uur gaat de gsm in de keuken. Als de jongste driftig wordt, mag hij even op zijn kamer afkoelen.",
        [
            mk("Welke opvoedingsstijl past bij dit gezin?",
               ["de autoritaire stijl", "de autoritatieve stijl", "de toegeeflijke stijl", "de onverschillige stijl"],
               1,
               "Veel responsiviteit en warmte, samen met duidelijke grenzen: de democratisch-autoritatieve stijl."),
            keuze(
                "Even op de kamer afkoelen is een [[*time-out|ritueel|beloning]]. De vaste gsm-afspraak hoort bij de dimensie [[*gedragscontrole|psychologische controle|responsiviteit]].",
                "Een time-out haalt een kind even uit de situatie. Regels en grenzen over gedrag zijn gedragscontrole. Psychologische controle speelt met liefde en schuld."),
            mk("Het balansmodel kijkt naar draaglast en draagkracht. Wat verhoogt de draagkracht van dit gezin?",
               ["een grootmoeder die elke week komt helpen", "een ouder die zijn werk verliest", "een kind met een langdurige ziekte", "een verhuis naar een stad waar ze niemand kennen"],
               0,
               "Een grootmoeder die bijspringt is een beschermende factor: ze verhoogt de draagkracht. De andere situaties verzwaren de draaglast."),
        ],
    ),

    # Casus: de verkoper
    casus(
        "Een verkoper aan de deur probeert op drie manieren een abonnement te verkopen.",
        [
            tabel(
                "Welke techniek van inwilliging gebruikt hij?",
                [
                    ("Hij vraagt eerst of je een korte enquête wil invullen, en daarna of je een abonnement neemt.", "Voet-tussen-de-deur"),
                    ("Hij vraagt eerst of je een abonnement voor drie jaar wil, en na je nee of je een proefmaand neemt.", "Deur-in-het-gezicht"),
                    ("Je zegt ja tegen een goedkoop abonnement, en pas daarna komen de extra kosten erbij.", "Zodra-de-bal-aan-het-rollen-is"),
                ],
                "Voet-tussen-de-deur begint klein, deur-in-het-gezicht begint groot. Bij de zodra-de-bal-aan-het-rollen-is-techniek zeg je ja en wordt de voorwaarde daarna slechter.",
                kolommen=["Voet-tussen-de-deur", "Deur-in-het-gezicht", "Zodra-de-bal-aan-het-rollen-is"]),
            mk("Je hebt het dure abonnement toch genomen en zegt nu tegen iedereen dat het een heel goede keuze was. Welk verschijnsel zie je?",
               ["groepsdenken in een team", "het omstandereffect bij een ongeval", "cognitieve dissonantie verminderen", "sociale belemmering door toeschouwers"],
               2,
               "Je gedrag (betalen) botst met je twijfel. Door je mening bij te stellen, verklein je die spanning: dissonantiereductie, zoals Festinger beschreef."),
        ],
    ),

    # Casus: misdaad op tv
    casus(
        "Mevrouw Janssens kijkt elke avond naar misdaadreeksen en nieuws over inbraken. Ze denkt dat haar buurt erg onveilig is, ook al dalen de cijfers. Ondertussen onthult een krant dat de burgemeester geld van de stad voor zichzelf gebruikte.",
        [
            mk("Welke mediatheorie verklaart het beeld dat mevrouw Janssens van haar buurt heeft?",
               ["de injectienaaldtheorie", "de cultivatietheorie", "de agendasettingtheorie", "de theorie van de vierde macht"],
               1,
               "Wie heel veel tv kijkt, gaat de wereld zien zoals die op tv voorgesteld wordt. Dat is cultivatie, op lange termijn."),
            keuze(
                "Met het artikel over de burgemeester vervult de krant de [[*waakhondfunctie|ontspanningsfunctie|persuasieve functie]].",
                "Media die de macht controleren en misbruik aan het licht brengen, zijn de waakhond van de democratie."),
            tabel(
                "Klopt dit over media?",
                [
                    ("Agendasetting zegt vooral waarover we nadenken.", J),
                    ("De injectienaaldtheorie ziet het publiek als passief.", J),
                    ("Persvrijheid is overal ter wereld even groot.", F),
                ],
                "Agendasetting bepaalt welke onderwerpen belangrijk lijken. De oudste theorie, de injectienaald, ziet het publiek als een passieve ontvanger."),
        ],
    ),

    # Losse vragen door elkaar
    koppel(
        "Welke denker hoort bij elke benadering van ontwikkeling?",
        [
            ["de psychodynamische benadering", "Freud"],
            ["de behavioristische benadering", "Skinner"],
            ["de cognitieve benadering", "Piaget"],
            ["de humanistische benadering", "Maslow"],
        ],
        ["Bourdieu", "Weber"],
        "Freud kijkt naar wat binnenin drijft, Skinner naar zichtbaar gedrag, Piaget naar denken, Maslow naar wat iemand wil worden. Bourdieu en Weber zijn sociologen."),
    volgorde(
        "Zet de fasen van groepsvorming van Tuckman in de juiste volgorde.",
        ["oriëntatiefase", "machtsfase", "normeringsfase", "prestatiefase", "afscheidsfase"],
        "Eerst leer je elkaar kennen, dan botst het, dan maak je afspraken, dan werk je goed samen en tot slot ga je uit elkaar."),
    mk("Kenzo ziet een kans op een prijs en gaat er meteen voor, zonder aan het risico te denken. Welk systeem van Gray is vooral actief?",
       ["het BIS, dat op straf en gevaar reageert", "het BAS, dat op beloning reageert", "het Über-ich, dat de normen bewaakt", "het chronosysteem, dat over tijd gaat"],
       1,
       "Het BAS (behavioural approach system) reageert op beloning en zet je in beweging. Het BIS remt bij straf en gevaar."),
    keuze(
        "Volgens Freud volgt het Es het [[*lustprincipe|realiteitsprincipe|moraliteitsprincipe]] en het Ich het [[*realiteitsprincipe|lustprincipe|moraliteitsprincipe]].",
        "Het Es wil meteen bevrediging. Het Ich zoekt wat in de werkelijkheid haalbaar is. Het Über-ich bewaakt de normen."),
    sorteer(
        "Gaat de uitspraak over Marx of over Bourdieu?",
        ["Marx", "Bourdieu"],
        [
            ["Klassen ontstaan door het bezit van de productiemiddelen.", "Marx"],
            ["Kennis, taal en omgangsvormen geven voordeel op school.", "Bourdieu"],
            ["Arbeiders en bezitters staan tegenover elkaar.", "Marx"],
            ["Naast geld telt ook cultureel en sociaal kapitaal.", "Bourdieu"],
        ],
        "Marx deelt in op basis van bezit. Bourdieu voegt cultureel en sociaal kapitaal toe aan het economische."),
    tabel(
        "Welke soort sociale mobiliteit is het?",
        [
            ("Een poetsvrouw wordt na een opleiding verpleegkundige.", "Intragenerationeel"),
            ("De dochter van een fabrieksarbeider wordt advocate.", "Intergenerationeel"),
            ("Een bankbediende wordt in zijn eigen leven directeur van het filiaal.", "Intragenerationeel"),
        ],
        "Intragenerationeel gebeurt binnen het leven van één persoon. Intergenerationeel vergelijk je met de positie van de ouders.",
        kolommen=["Intragenerationeel", "Intergenerationeel"]),
    mk("Leerlingen die al goed lezen, lezen meer en worden nog beter. Wie het moeilijk heeft, leest minder en valt verder achter. Hoe heet dit?",
       ["het matheüseffect", "de meritocratie", "het omstandereffect", "de zelfactualisatie"],
       0,
       "Wie heeft, zal meer krijgen: het matheüseffect. Het is een argument voor gerichte steun in plaats van voor iedereen hetzelfde."),
    mk("Welke onderzoeksvraag haalt het criterium objectief?",
       ["Waarom is de schadelijke gsm-regel van de school zo fout?", "Hoeveel uur per dag zitten jongeren op hun gsm?", "Hoe kunnen we die luie jongeren van hun gsm afhalen?", "Waarom is gamen het grootste probleem van deze tijd?"],
       1,
       "Een objectieve vraag verraadt geen mening. Woorden als schadelijk, lui of grootste probleem kleuren de vraag al."),
    volgorde(
        "In welke volgorde doorloop je een onderzoek?",
        ["oriënteren", "voorbereiden", "uitvoeren", "rapporteren"],
        "Eerst verken je het onderwerp en stel je een vraag, dan plan je, dan verzamel en analyseer je gegevens en tot slot schrijf je het verslag."),
    mk("Welke visie op socialisatie hoort bij Talcott Parsons?",
       ["het symbolisch interactionisme", "het functionalisme", "de conflictsociologie", "de psychoanalyse"],
       1,
       "Parsons is een functionalist: socialisatie zorgt dat iedereen de normen opneemt en de samenleving goed draait. Mead hoort bij het symbolisch interactionisme."),
    tabel(
        "Klopt dit over trekken, de Big Five en HEXACO?",
        [
            ("Een lage score op een factor van de Big Five betekent dat die factor ontbreekt.", F),
            ("HEXACO voegt een factor integriteit toe aan de Big Five.", J),
            ("Temperament zie je al bij een baby.", J),
        ],
        "Een lage score is een plaats op de as, geen afwezigheid. HEXACO bouwt verder op de Big Five met integriteit erbij."),
    inv("Hoe heet bij Bandura het geloof in je eigen kunnen bij een bepaalde taak? Antwoord met één woord.",
        ["zelfeffectiviteit", "self-efficacy"],
        "Wie gelooft dat hij een taak aankan, begint er sneller aan en zet door. Dat is zelfeffectiviteit."),
    tabel(
        "Klassieke of operante conditionering?",
        [
            ("Een hond kwijlt al bij het geluid van de bel die altijd voor het eten klinkt.", "Klassiek"),
            ("Sofie krijgt een sticker als ze opruimt en ruimt daarna vaker op.", "Operant"),
            ("Little Albert wordt bang van een witte rat na een hard geluid telkens als hij ze ziet.", "Klassiek"),
            ("Een rat leert op een knop duwen omdat er dan voedsel komt.", "Operant"),
        ],
        "Bij klassieke conditionering koppel je twee prikkels. Bij operante conditionering leer je uit de gevolgen van je eigen gedrag: bekrachtiging of straf.",
        kolommen=["Klassiek", "Operant"]),
    keuze(
        "Wat een kind al alleen kan, is bij Vygotsky de [[*comfortzone|zone van de naaste ontwikkeling]]. Wat het met hulp van iemand anders kan, is de [[*zone van de naaste ontwikkeling|comfortzone]].",
        "Leren gebeurt het best in de zone van de naaste ontwikkeling: net iets moeilijker dan wat je alleen kan, met steun."),
    mk("Nina zegt na een slechte toets: 'Ik snap breuken nog niet, maar met oefenen lukt het wel.' Welke mindset heeft ze volgens Dweck?",
       ["een fixed mindset", "een growth mindset", "een externe locus of control", "een stabiele attributie"],
       1,
       "Wie gelooft dat kunnen groeit door inzet, heeft een growth mindset. Een fixed mindset ziet talent als iets dat vastligt."),
    mk("Een bestuur keurt een riskant plan goed. Niemand durft kritiek te geven, omdat ze de goede sfeer niet willen breken. Hoe heet dit?",
       ["groepsdenken", "sociale facilitatie", "het matheüseffect", "conformisme van Sherif"],
       0,
       "Bij groepsdenken neemt een groep een slechte beslissing om eensgezind te blijven."),
    tabel(
        "Welke functie van de media staat voorop?",
        [
            ("een documentaire over de Eerste Wereldoorlog", "Educatief"),
            ("een quiz op zaterdagavond", "Ontspanning"),
            ("het weerbericht", "Informatief"),
            ("een reclamespot voor een frisdrank", "Persuasief"),
        ],
        "Media informeren, leren je iets bij, ontspannen en proberen je te overtuigen.",
        kolommen=["Informatief", "Educatief", "Ontspanning", "Persuasief"]),
    mk("Een kind leert thuis van zijn ouders hoe je aan tafel eet en dankjewel zegt. Welke vorm van socialisatie is dat?",
       ["primaire socialisatie", "secundaire socialisatie", "sociale mobiliteit", "sociale stratificatie"],
       0,
       "De primaire socialisatie gebeurt vroeg in het gezin. Later volgen school, werk en vrienden: de secundaire socialisatie."),
    inv("In de LSD-methode om actief te luisteren staat de L voor ...",
        ["luisteren"],
        "LSD staat voor luisteren, samenvatten en doorvragen."),
    open_("Kies een maatschappelijk vraagstuk, zoals kinderarmoede. Beschrijf het probleem kort, geef één verklaring en stel één oplossing voor met een mogelijk ongewenst gevolg.",
          "Beschrijven: één op acht kinderen in Vlaanderen groeit op in armoede. Verklaren: werkloosheid of een laag inkomen van de ouders, samen met hoge woonkosten. Oplossing: een hogere kinderbijslag voor gezinnen met een laag inkomen. Ongewenst gevolg: het kost de overheid veel geld en lost de oorzaak, een laag inkomen, niet op.",
          "De vier redeneeractiviteiten zijn beschrijven, verklaren, oplossingen bedenken en oplossingen evalueren."),
]
