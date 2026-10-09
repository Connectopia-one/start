# -*- coding: utf-8 -*-
"""Argumentatieleer: redeneervormen en drogredenen.

Het laatste van twaalf thema's over filosofie. De fiche vraagt:

    de 4 basisvormen van voorwaardelijke redeneringen onderscheiden
    uitleggen welke basisvorm geldig en welke ongeldig is
    van een gegeven redenering bepalen of ze geldig of ongeldig is
    een eigen argumentatie opbouwen met de vier basisvormen
    drogredenen herkennen en benoemen in een gegeven voorbeeld
    de geldigheid van redeneringen beoordelen

De vier basisvormen staan letterlijk in de fiche: bevestiging van het
antecedens (modus ponens), bevestiging van het consequens, ontkenning van het
antecedens, en ontkenning van het consequens (modus tollens). De eerste en de
laatste zijn geldig, de twee in het midden niet. Dat is logica en geen
mening, dus daar valt niets aan te verzinnen.

De drogredenen noemt de fiche niet bij naam. Hieronder staan de klassieke, met
hun gangbare naam: op de persoon, de stroman, het beroep op een onbevoegde
autoriteit, de cirkel, de valse tweedeling, het hellend vlak, de overhaaste
generalisatie, het beroep op de massa en het beroep op de natuur. Die laatste
is het is-ought probleem van Hume uit het thema over de basisbegrippen van de
ethiek.

Deel 1 zijn de vier basisvormen en de geldigheid.
Deel 2 zijn de drogredenen.
"""

DEEL1 = [
    dict(type="meerkeuze",
         vraag="Wat is het antecedens in de uitspraak: als het regent, is de straat nat?",
         opties=["het regent", "de straat is nat",
                 "als het regent", "de hele uitspraak samen"],
         antwoord=0,
         uitleg="Het antecedens gaat vooraf: het is het deel na het woordje als. Het consequens "
                "volgt: het deel na dan."),
    dict(type="meerkeuze",
         vraag="Wat is het consequens in die uitspraak?",
         opties=["de straat is nat", "het regent",
                 "als het regent", "de hele uitspraak samen"],
         antwoord=0,
         uitleg="Consequens komt van volgen. Het is wat volgens de uitspraak volgt als het "
                "antecedens waar is."),
    dict(type="meerkeuze",
         vraag="Als het regent, is de straat nat. Het regent. Welke vorm is dit?",
         opties=["bevestiging van het antecedens", "bevestiging van het consequens",
                 "ontkenning van het antecedens", "ontkenning van het consequens"],
         antwoord=0,
         uitleg="Je bevestigt het als-deel. Dat is de modus ponens, en die is geldig: de straat "
                "is nat."),
    dict(type="meerkeuze",
         vraag="Als het regent, is de straat nat. De straat is nat. Welke vorm is dit?",
         opties=["bevestiging van het consequens", "bevestiging van het antecedens",
                 "ontkenning van het consequens", "ontkenning van het antecedens"],
         antwoord=0,
         uitleg="Je bevestigt het dan-deel. Dat is ongeldig: de straat kan ook nat zijn van een "
                "schoonmaakwagen."),
    dict(type="meerkeuze",
         vraag="Als het regent, is de straat nat. Het regent niet. Welke vorm is dit?",
         opties=["ontkenning van het antecedens", "ontkenning van het consequens",
                 "bevestiging van het antecedens", "bevestiging van het consequens"],
         antwoord=0,
         uitleg="Je ontkent het als-deel. Ook dat is ongeldig: zonder regen kan de straat nog "
                "altijd nat zijn."),
    dict(type="meerkeuze",
         vraag="Als het regent, is de straat nat. De straat is niet nat. Welke vorm is dit?",
         opties=["ontkenning van het consequens", "ontkenning van het antecedens",
                 "bevestiging van het consequens", "bevestiging van het antecedens"],
         antwoord=0,
         uitleg="Je ontkent het dan-deel. Dat is de modus tollens, en die is geldig: het regent "
                "niet."),
    dict(type="meerkeuze",
         vraag="Welke twee van de vier basisvormen zijn geldig?",
         opties=["de modus ponens en de modus tollens",
                 "de bevestiging en de ontkenning van het antecedens",
                 "de bevestiging en de ontkenning van het consequens",
                 "de bevestiging van het consequens en de modus ponens"],
         antwoord=0,
         uitleg="Bevestig je het antecedens of ontken je het consequens, dan volgt het besluit "
                "met zekerheid. De twee andere vormen zijn drogredenen."),
    dict(type="meerkeuze",
         vraag="Wat betekent het dat een redenering geldig is?",
         opties=["als de premissen waar zijn, moet het besluit ook waar zijn",
                 "de premissen van de redenering zijn in werkelijkheid waar",
                 "het besluit van de redenering is in werkelijkheid waar",
                 "de redenering is door de meeste mensen aanvaard"],
         antwoord=0,
         uitleg="Geldigheid gaat over de vorm, niet over de inhoud. Een geldige redenering kan "
                "van onware premissen vertrekken."),
    dict(type="meerkeuze",
         vraag="Kan een geldige redenering een onwaar besluit hebben?",
         opties=["ja, als een van de premissen onwaar is",
                 "nee, een geldige redenering heeft altijd een waar besluit",
                 "nee, want een onwaar besluit maakt de vorm meteen ongeldig",
                 "ja, want geldigheid en waarheid hebben niets met elkaar te maken"],
         antwoord=0,
         uitleg="Geldig betekent dat het besluit volgt áls de premissen waar zijn. Vertrek je van "
                "iets onwaars, dan kom je netjes bij iets onwaars uit."),
    dict(type="meerkeuze",
         vraag="Als je studeert, slaag je. Je bent geslaagd. Dus heb je gestudeerd. Klopt die "
               "redenering?",
         opties=["nee, dit is een bevestiging van het consequens",
                 "ja, dit is een modus ponens en dus geldig",
                 "ja, dit is een modus tollens en dus geldig",
                 "nee, dit is een ontkenning van het antecedens"],
         antwoord=0,
         uitleg="Je kan ook geslaagd zijn met geluk of met voorkennis. Uit het gevolg volgt de "
                "oorzaak niet."),
    dict(type="meerkeuze",
         vraag="Als je studeert, slaag je. Je bent niet geslaagd. Dus heb je niet gestudeerd. "
               "Klopt die redenering?",
         opties=["ja, dit is een modus tollens en dus geldig",
                 "nee, dit is een bevestiging van het consequens",
                 "nee, dit is een ontkenning van het antecedens",
                 "ja, dit is een modus ponens en dus geldig"],
         antwoord=0,
         uitleg="Als studeren altijd tot slagen leidt en je niet geslaagd bent, kan je niet "
                "gestudeerd hebben. De vorm is geldig; of de eerste premisse waar is, is een "
                "andere vraag."),
    dict(type="meerkeuze",
         vraag="Welke uitspraken over geldigheid en waarheid kloppen?",
         opties=["geldigheid gaat over de vorm van de redenering",
                 "een redenering kan geldig zijn en toch van iets onwaars vertrekken",
                 "een ware conclusie maakt een redenering altijd geldig",
                 "een ongeldige redenering heeft altijd een onwaar besluit"],
         antwoord=[0, 1],
         uitleg="De eerste twee. Ook een ongeldige redenering kan per ongeluk bij iets waars "
                "uitkomen; ze bewijst het alleen niet."),
    dict(type="waarofniet",
         vraag="De modus ponens bevestigt het antecedens en is geldig.",
         antwoord=True,
         uitleg="Waar. Als P dan Q, en P, dus Q."),
    dict(type="waarofniet",
         vraag="De bevestiging van het consequens is een geldige redeneervorm.",
         antwoord=False,
         uitleg="Niet waar. Uit het gevolg volgt de voorwaarde niet: de straat kan ook nat zijn "
                "zonder regen."),
    dict(type="waarofniet",
         vraag="De ontkenning van het antecedens is een ongeldige redeneervorm.",
         antwoord=True,
         uitleg="Waar. Zonder regen kan de straat nog altijd nat zijn."),
    dict(type="waarofniet",
         vraag="Een geldige redenering heeft altijd een waar besluit.",
         antwoord=False,
         uitleg="Niet waar. Als een premisse onwaar is, kan het besluit onwaar zijn terwijl de "
                "vorm klopt."),
    dict(type="invultekst",
         vraag="Hoe heet het deel van een als-dan-uitspraak dat na het woordje als komt? Het ...",
         antwoord=["antecedens"],
         uitleg="Antecedens: wat voorafgaat."),
    dict(type="invultekst",
         vraag="Hoe heet het deel dat na dan komt? Het ...",
         antwoord=["consequens"],
         uitleg="Consequens: wat volgt."),
    dict(type="invultekst",
         vraag="Hoe heet de geldige vorm waarin je het antecedens bevestigt? Modus ...",
         antwoord=["ponens"],
         uitleg="Als P dan Q, en P, dus Q."),
    dict(type="invultekst",
         vraag="Hoe heet de geldige vorm waarin je het consequens ontkent? Modus ...",
         antwoord=["tollens"],
         uitleg="Als P dan Q, en niet Q, dus niet P."),
]

DEEL2 = [
    dict(type="meerkeuze",
         vraag="Wat is een drogreden?",
         opties=["een argument dat overtuigend lijkt maar niet deugt",
                 "een argument dat niemand ooit overtuigt",
                 "een argument waarvan de premissen onwaar zijn",
                 "een argument dat van een verkeerde bron komt"],
         antwoord=0,
         uitleg="De schijn van een goed argument, zonder de kracht ervan. Daarom werken "
                "drogredenen zo goed in een discussie."),
    dict(type="meerkeuze",
         vraag="Je voorstel is niets waard, want je hebt zelf nooit gestudeerd. Welke drogreden?",
         opties=["op de persoon", "de stroman",
                 "de valse tweedeling", "het hellend vlak"],
         antwoord=0,
         uitleg="De aanval richt zich op wie het zegt in plaats van op wat er gezegd wordt. Een "
                "zwak argument blijft zwak, ook uit de mond van een professor."),
    dict(type="meerkeuze",
         vraag="Je wil minder vlees eten? Dus je wil dat niemand nog een boerderij heeft. Welke "
               "drogreden?",
         opties=["de stroman", "op de persoon",
                 "het beroep op de massa", "de cirkel"],
         antwoord=0,
         uitleg="Er wordt een standpunt in je mond gelegd dat je niet hebt ingenomen, en dát wordt "
                "dan bestreden."),
    dict(type="meerkeuze",
         vraag="Je bent ofwel voor dit plan, ofwel tegen vooruitgang. Welke drogreden?",
         opties=["de valse tweedeling", "de stroman",
                 "het hellend vlak", "de overhaaste generalisatie"],
         antwoord=0,
         uitleg="Er worden twee mogelijkheden voorgesteld terwijl er meer zijn. Je kan voor "
                "vooruitgang zijn en tegen dit plan."),
    dict(type="meerkeuze",
         vraag="Als we dit toelaten, staan we morgen alles toe. Welke drogreden?",
         opties=["het hellend vlak", "de valse tweedeling",
                 "de cirkel", "het beroep op de natuur"],
         antwoord=0,
         uitleg="De ene stap wordt zonder enige grond doorgetrokken tot een onvermijdelijke "
                "afgrond. Dat die glijbaan er is, moet je aantonen."),
    dict(type="meerkeuze",
         vraag="Dit boek vertelt de waarheid, want er staat in dat het de waarheid vertelt. Welke "
               "drogreden?",
         opties=["de cirkel", "het hellend vlak",
                 "op de persoon", "het beroep op de massa"],
         antwoord=0,
         uitleg="Wat bewezen moet worden, zit al in het bewijs. Je draait rond en komt niet "
                "vooruit."),
    dict(type="meerkeuze",
         vraag="Iedereen doet het, dus kan het geen kwaad. Welke drogreden?",
         opties=["het beroep op de massa", "de cirkel",
                 "de stroman", "de valse tweedeling"],
         antwoord=0,
         uitleg="Hoeveel mensen iets doen, zegt niets over of het mag. Veel vroegere gewoonten "
                "keuren wij vandaag af."),
    dict(type="meerkeuze",
         vraag="Een bekende zanger zegt dat dit middel werkt, dus werkt het. Welke drogreden?",
         opties=["het beroep op een onbevoegde autoriteit",
                 "de cirkelredenering over hetzelfde middel",
                 "het argument gericht op de persoon zelf",
                 "het hellend vlak naar steeds meer middelen"],
         antwoord=0,
         uitleg="Een deskundige aanhalen is geen fout; iemand aanhalen die op dit terrein geen "
                "deskundige is, wel."),
    dict(type="meerkeuze",
         vraag="Het is natuurlijk, dus het is goed. Welke drogreden?",
         opties=["het beroep op de natuur", "de stroman",
                 "de valse tweedeling", "het beroep op de massa"],
         antwoord=0,
         uitleg="Dit is het is-ought probleem van Hume in zakformaat: uit wat van nature zo is, "
                "volgt niet dat het zo moet zijn. Gif is ook natuurlijk."),
    dict(type="meerkeuze",
         vraag="Mijn twee buren rijden slecht, dus mensen uit die straat rijden slecht. Welke "
               "drogreden?",
         opties=["de overhaaste generalisatie",
                 "de cirkelredenering over die straat",
                 "het argument gericht op de buren zelf",
                 "het hellend vlak naar de hele gemeente"],
         antwoord=0,
         uitleg="Twee gevallen zijn te weinig om over een hele groep te besluiten. Dezelfde "
                "zwakte zit in de inductie bij Hume."),
    dict(type="meerkeuze",
         vraag="Welke uitspraken over drogredenen kloppen?",
         opties=["een drogreden kan een besluit hebben dat toevallig waar is",
                 "een drogreden overtuigt juist omdat ze op een goed argument lijkt",
                 "een drogreden is altijd met opzet gebruikt",
                 "een drogreden heeft altijd een onwaar besluit"],
         antwoord=[0, 1],
         uitleg="De eerste twee. Wie een drogreden gebruikt, doet dat vaak zonder het te merken, "
                "en het besluit kan om een andere reden best juist zijn."),
    dict(type="meerkeuze",
         vraag="Hoe weerleg je een drogreden het best in een gesprek?",
         opties=["benoem wat er aan de stap zelf mankeert",
                 "gebruik er zelf een die nog sterker klinkt",
                 "verklaar dat je gesprekspartner ongelijk heeft",
                 "verlaat het gesprek, want er valt niets aan te doen"],
         antwoord=0,
         uitleg="Niet harder spreken maar de sprong aanwijzen: waarom volgt het besluit niet uit "
                "wat er gezegd is?"),
    dict(type="waarofniet",
         vraag="Een drogreden lijkt overtuigend maar deugt niet.",
         antwoord=True,
         uitleg="Waar. De schijn van een goed argument, zonder de kracht ervan."),
    dict(type="waarofniet",
         vraag="Een argument op de persoon richten is een geldige manier van weerleggen.",
         antwoord=False,
         uitleg="Niet waar. Wie iets zegt, heeft met de kracht van het argument niets te maken."),
    dict(type="waarofniet",
         vraag="Bij een valse tweedeling worden er twee mogelijkheden voorgesteld terwijl er meer "
               "zijn.",
         antwoord=True,
         uitleg="Waar. Je wordt in een keuze geduwd die er niet is."),
    dict(type="waarofniet",
         vraag="Een drogreden heeft altijd een onwaar besluit.",
         antwoord=False,
         uitleg="Niet waar. Het besluit kan juist zijn; de redenering bewijst het alleen niet."),
    dict(type="invultekst",
         vraag="Hoe heet een argument dat overtuigend lijkt maar niet deugt?",
         antwoord=["een drogreden", "drogreden"],
         uitleg="De schijn zonder de kracht."),
    dict(type="invultekst",
         vraag="Hoe heet de drogreden waarbij je een standpunt bestrijdt dat de ander niet heeft "
               "ingenomen? De ...",
         antwoord=["stroman", "stromanargument"],
         uitleg="Je zet een pop van stro neer en slaat die om."),
    dict(type="invultekst",
         vraag="Hoe heet de drogreden waarbij wat bewezen moet worden al in het bewijs zit? De ...",
         antwoord=["cirkel", "cirkelredenering"],
         uitleg="Je draait rond en komt niet vooruit."),
    dict(type="invultekst",
         vraag="Hoe heet de drogreden die van één stap een onvermijdelijke glijbaan maakt? Het ...",
         antwoord=["hellend vlak"],
         uitleg="Dat die glijbaan er is, moet je eerst aantonen."),
]
