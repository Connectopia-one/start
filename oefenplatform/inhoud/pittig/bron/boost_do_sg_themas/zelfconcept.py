"""Het zelfconcept: zelfbeeld en zelfwaardering — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_zelfconcept: zelfbeeld, zelfwaardering,
self-efficacy en body-image, de vier soorten zelfbeeld en de invloed op het
gedrag. Met vier zelfgetekende kaartjes."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, BLAUW, LICHTGROEN

VK = Prent("vier-leerlingen-zelfbeeld", "Wat ze zeggen en wat er werkelijk is", "vier kaartjes met een uitspraak en de werkelijkheid, letters A tot D")
KAART = [("A", 50, 70, ["« Ik ben slecht in wiskunde. »"], "rapport wiskunde: 16 op 20"),
         ("B", 510, 70, ["« Ik ben de beste in taal,", "ik hoef niet te leren. »"], "rapport taal: 8 op 20"),
         ("C", 50, 345, ["« Ik ben goed in Frans,", "maar spelling is mijn zwakke punt. »"], "Frans 15 op 20, spelling 9 op 20"),
         ("D", 510, 345, ["« Ik ben veel te dik. »"], "arts: gezond gewicht")]
for t, x, y, regels, echt in KAART:
    VK.rect(x, y, 440, 240, "#ffffff", DONKER, 10, 2)
    for i, r in enumerate(regels):
        VK.tekst(x + 220, y + 60 + i * 32, r, 21)
    VK.rect(x + 40, y + 140, 300, 50, "#eef3e6", "#8a8470", 8, 2)
    VK.tekst(x + 190, y + 172, echt, 19)
    VK.letter(x + 400, y + 205, t)
U = "vier-leerlingen-zelfbeeld.svg"
Z = {t: [Prent.zone(x, y, 440, 240)] for t, x, y, r, e in KAART}

YUNA = ("Lees het verhaal.\n\n"
        "Yuna (15) doet mee aan de schoolrevue. Bij het zingen voelt ze zich zeker, want vorig jaar ging het ook goed en de juf moedigt haar aan. "
        "Bij het dansen durft ze niet vooraan te staan: « Ik kan dat toch niet, » zegt ze, al heeft ze het nog nooit echt geprobeerd. "
        "Thuis zegt ze: « Ook als het mislukt, blijf ik iemand die de moeite waard is. »")

VRAGEN = [
    klik("Bekijk de vier kaartjes. Klik op het zelfbeeld dat vertekend is door onderschatting.", U, Z["A"], "Het beeld is slechter dan de werkelijkheid."),
    klik("Klik op het zelfbeeld dat vertekend is door overschatting.", U, Z["B"], "Ook overschatting is vertekend."),
    klik("Klik op het realistische zelfbeeld.", U, Z["C"], "Het beeld klopt met de werkelijkheid, sterke en zwakke kanten samen."),
    klik("Klik op het kaartje met een vertekend body-image.", U, Z["D"], "Het beeld in het hoofd wijkt af van het echte lichaam."),
    casus(YUNA, [
        sorteer("Hoe is de self-efficacy van Yuna voor deze taak?", ["hoog", "laag"],
                [("zingen", "hoog"), ("dansen", "laag")],
                "Self-efficacy is taakgebonden."),
        tabel("Welke bron voedt de self-efficacy van Yuna bij het zingen?",
              [("eerder zelf geslaagd zijn", J), ("aanmoediging krijgen", J), ("een dure jurk dragen", F)],
              "Eerdere successen en aanmoediging versterken het geloof dat je iets kan."),
        keuze("'Ook als het mislukt, blijf ik iemand die de moeite waard is.' Dat toont een stevige [[*zelfwaardering|self-efficacy|body-image]].", "Haar waarde als persoon hangt niet af van één taak."),
        mk("Wat doet de lage self-efficacy bij het dansen met het gedrag van Yuna?",
           ["ze probeert het niet eens", "ze danst daardoor net beter dan iedereen", "ze gaat daardoor meer zingen dan dansen", "ze krijgt daardoor een vertekend body-image"],
           0, "Wat je van jezelf denkt, stuurt wat je probeert."),
    ]),
    koppel("Koppel het deel van het zelfconcept aan de vraag die erbij hoort.",
           [("zelfbeeld", "wie denk ik dat ik ben?"), ("zelfwaardering", "hoeveel ben ik mezelf waard?"), ("self-efficacy", "kan ik deze taak aan?"), ("body-image", "hoe denk ik over mijn lichaam?")],
           ["hoe oud ben ik?"], "Vier delen van het zelfconcept."),
    sorteer("Welk deel van het zelfconcept speelt hier?", ["zelfbeeld", "zelfwaardering", "self-efficacy", "body-image"],
            [("'Ik ben verlegen en goed in tekenen.'", "zelfbeeld"), ("'Ik voel me niets waard.'", "zelfwaardering"), ("'Die toets kan ik wel aan.'", "self-efficacy"), ("Een jongere wil niet meer zwemmen omdat ze zich schaamt voor haar lichaam.", "body-image")],
            "Beschrijven, beoordelen, een taak aankunnen, en je lichaam."),
    tabel("Klopt dit over het zelfbeeld?",
          [("Een positief zelfbeeld is altijd realistisch.", F), ("Self-efficacy kan per vak verschillen.", J), ("Het zelfconcept ligt van jongs af vast.", F), ("Zelfwaardering en self-efficacy betekenen hetzelfde.", F)],
          "Positief kan ook te positief zijn."),
    mk("Waarom is het beter een kind te prijzen voor zijn inzet dan voor zijn talent?",
       ["inzet kan het zelf sturen", "omdat talent bij geen enkel kind voorkomt", "omdat inzet altijd tot de hoogste punten leidt", "omdat een kind dan nooit meer faalt"],
       0, "Wie geprezen wordt om inzet, leert dat oefenen loont."),
    keuze("Een kleuter denkt dat hij alles kan. Zijn zelfbeeld is vaak [[*te positief|te negatief|al helemaal realistisch]].", "Pas in de lagere school gaat hij zich vergelijken."),
    keuze("Het zelfbeeld verandert het sterkst in de [[*adolescentie|babytijd|late volwassenheid]].", "Een jongere vergelijkt zich volop met anderen."),
    mk("Mats gelooft niet dat hij een spreekbeurt kan geven. Wat doet zijn leraar het best?",
       ["hem eerst voor drie vrienden laten oefenen", "hem meteen een spreekbeurt van een uur laten geven", "hem nooit aanmoedigen om hem niet te verwennen", "de spreekbeurt overslaan zodat hij geen fout maakt"],
       0, "Elke gelukte stap is een ervaring van slagen."),
    tabel("Is dit een soort zelfbeeld?",
          [("positief", J), ("negatief", J), ("vertekend", J), ("realistisch", J), ("motorisch", F)],
          "Vier soorten."),
    keuze("Een kind leest vooral in de reacties van [[*anderen|zijn eigen genen|het weer]] wie het is.", "Daarom wegen opmerkingen van ouders en leerkrachten zwaar."),
    keuze("Bewerkte foto's op sociale media beïnvloeden het zelfconcept vooral omdat jongeren zich [[*ermee vergelijken|ermee verkleden|ervan vervelen]].", "De vergelijking doet het."),
    sleep("Het [[zelfbeeld]] beschrijft, de [[zelfwaardering]] beoordeelt, en de [[self-efficacy]] is het geloof dat je een taak aankan.",
          ["temperament", "identiteit"], "Drie delen van het zelfconcept."),
    mk("Noor (13) groeit in één jaar twaalf centimeter en vindt haar lichaam plots vreemd. Wat speelt hier vooral?",
       ["haar lichaam verandert snel", "ze gebruikt geen spiegel meer", "haar lichaam groeit niet meer", "haar body-image ontstaat pas na twintig"],
       0, "Een snel veranderend lichaam, plus vergelijken."),
    inv("Welk woord gebruik je voor alles wat je over jezelf denkt en voelt, samen? Eén woord.", ["zelfconcept", "het zelfconcept"], "Het zelfconcept: zelfbeeld, zelfwaardering, self-efficacy en body-image."),
    keuze("Iemand denkt dat hij alles kan en bereidt zich niet voor. Zijn zelfbeeld is vertekend door [[*overschatting|onderschatting]].", "Ook dat geeft problemen."),
    tabel("Heeft een hoge self-efficacy dit gevolg?",
          [("langer doorzetten bij tegenslag", J), ("moeilijke taken durven aangaan", J), ("nooit meer iets fout doen", F)],
          "Geloof dat het kan lukken, helpt doorzetten."),
    keuze("Een lage zelfwaardering zorgt er vaak voor dat iemand [[*minder durft te proberen|meer risico neemt|nooit iets voelt]].", "Wie zichzelf weinig waard vindt, stelt zich minder bloot."),
    keuze("Een man van 60 vindt zichzelf waardevol ondanks een mislukt project. Zijn [[*zelfwaardering|self-efficacy|body-image]] is stevig.", "Zijn waarde als persoon hangt niet af van één project."),
    mk("Waarom kijk je bij het zelfconcept telkens naar de invloed op het gedrag?",
       ["het bepaalt wat je probeert", "omdat het zelfconcept alleen in je hoofd blijft", "omdat gedrag en zelfconcept niets met elkaar te maken hebben", "omdat je gedrag het zelfconcept nooit kan veranderen"],
       0, "Het bepaalt wat je probeert, vermijdt en volhoudt."),
    tabel("Voedt dit de self-efficacy?",
          [("eerder zelf geslaagd zijn", J), ("iemand anders zien slagen", J), ("aanmoediging krijgen", J), ("altijd falen zonder hulp", F)],
          "Vier bronnen van vertrouwen."),
    keuze("Een vertekend zelfbeeld kan zowel onderschatting [[*als overschatting|als realisme]] zijn.", "Beide wijken af van de werkelijkheid."),
    keuze("Een jongere eet nauwelijks omdat ze zich te zwaar vindt, terwijl ze mager is. Dat is een vertekend [[*body-image|zelfconcept van het temperament|realistisch zelfbeeld]].", "Het beeld in haar hoofd klopt niet."),
    open_("Leg met een voorbeeld uit hoe een negatief zelfbeeld het gedrag van een leerling kan sturen.",
          "Bijvoorbeeld: Tim denkt dat hij slecht is in Frans. Bij een moeilijke oefening geeft hij snel op en hij vraagt geen hulp. Daardoor oefent hij minder en haalt hij lagere punten, wat zijn zelfbeeld weer bevestigt."),
]
