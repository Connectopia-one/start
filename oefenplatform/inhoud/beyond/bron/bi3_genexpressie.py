# -*- coding: utf-8 -*-
"""Genexpressie: transcriptie en translatie — 🌍 Beyond, biologie.

Deel 1 gaat over de genetische code en over de transcriptie: wat een gen en
een codon zijn, hoe het pre-mRNA gemaakt en afgewerkt wordt, en wat er in de
initiatie, de elongatie en de terminatie gebeurt. Deel 2 gaat over de
translatie op het ribosoom en over de manieren waarop één gen toch
verschillende eiwitten kan opleveren.

De fiche vraagt dat de leerling een codon op een voorstelling van de
genetische code kan aflezen en in twee richtingen kan omzetten: van
nucleotiden naar aminozuren en terug. Daarom staan er in deel 1 en deel 2
vragen waarin een korte sequentie echt vertaald moet worden, en wordt daarbij
nooit naar een codon gevraagd dat een leerling uit het hoofd zou moeten
kennen, behalve het startcodon.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een gen?",
        opties=[
            "een stuk DNA met de code voor een product",
            "een volledig chromosoom met al zijn genen erop",
            "een eiwit dat het DNA leest",
            "een stuk RNA in het cytoplasma",
        ],
        antwoord=0,
        uitleg="Een gen is het stuk DNA dat de informatie voor één RNA of eiwit draagt. "
        "Het gebruik van die informatie heet genexpressie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een groepje van drie nucleotiden op het mRNA?",
        antwoord=["codon", "een codon", "triplet"],
        uitleg="Elk codon van drie nucleotiden staat voor één aminozuur of voor een stop. "
        "Op het tRNA heet het tegenovergestelde drietal het anticodon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met een gedegenereerde genetische code?",
        opties=[
            "verschillende codons geven hetzelfde aminozuur",
            "één codon geeft verschillende aminozuren",
            "de code is bij elke soort anders",
            "de code wordt in beide richtingen even goed gelezen",
        ],
        antwoord=0,
        uitleg="Er zijn 64 codons voor 20 aminozuren, dus hebben de meeste aminozuren er "
        "meerdere. Daardoor verandert een fout in het DNA niet altijd het eiwit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat de genetische code universeel is?",
        opties=[
            "bijna alle organismen gebruiken dezelfde codons",
            "elk organisme heeft zijn eigen codons en zijn eigen regels",
            "de code geldt alleen voor eukaryoten",
            "de code verandert bij elke celdeling",
        ],
        antwoord=0,
        uitleg="Een menselijk gen werkt daarom ook in een bacterie. Dat is net wat "
        "gentechnologie mogelijk maakt.",
    ),
    dict(
        type="invultekst",
        vraag="Welk codon van drie letters start de translatie?",
        antwoord=["AUG", "aug"],
        uitleg="AUG is het startcodon en codeert voor methionine. UAA, UAG en UGA zijn de "
        "drie stopcodons.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als er één nucleotide wegvalt vooraan een gen?",
        opties=[
            "het leesraam schuift en alle codons erna veranderen",
            "alleen dat ene codon verandert, de rest blijft gelijk",
            "er verandert niets aan het eiwit",
            "het gen wordt twee keer gelezen",
        ],
        antwoord=0,
        uitleg="De nucleotiden worden per drie gelezen vanaf het startcodon. Valt er één "
        "weg, dan verschuift het leesraam en is het hele eiwit erna anders.",
    ),
    dict(
        type="invultekst",
        vraag="Waar in de cel gebeurt de transcriptie bij een eukaryoot?",
        antwoord=["in de kern", "de kern", "kern"],
        uitleg="De transcriptie gebeurt in de kern, waar het DNA ligt. Het rijpe mRNA "
        "verlaat daarna de kern door een kernporie.",
    ),
    dict(
        type="waarofniet",
        vraag="Het mRNA wordt gemaakt door RNA-polymerase.",
        antwoord=True,
        uitleg="RNA-polymerase leest de antisense-streng en bouwt daarlangs het RNA. Het "
        "heeft, anders dan DNA-polymerase, geen primer nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er tijdens de initiatie van de transcriptie?",
        opties=[
            "transcriptiefactoren en polymerase binden op de promotor",
            "het mRNA krijgt zijn poly(A)-staart",
            "de introns worden uit het pre-mRNA geknipt en de exons geplakt",
            "het ribosoom bindt op het mRNA",
        ],
        antwoord=0,
        uitleg="De promotor is de aanlegplaats vlak voor het gen. Pas als de "
        "transcriptiefactoren er zitten, kan polymerase starten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met het pre-mRNA voor het de kern verlaat? Kruis alles aan wat juist is.",
        opties=[
            "de introns worden eruit geknipt",
            "er komt een cap en een poly(A)-staart op",
            "het wordt in aminozuren omgezet",
            "het wordt in twee strengen gelegd",
        ],
        antwoord=[0, 1],
        uitleg="Splicing haalt de introns eruit en plakt de exons aan elkaar. De 5'-cap en "
        "de poly(A)-staart beschermen het mRNA en helpen het ribosoom.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de stukken van een gen die in het rijpe mRNA blijven staan?",
        antwoord=["exonen", "exons", "exon"],
        uitleg="De exons blijven, de introns worden weggeknipt. Daarom is een rijp mRNA "
        "korter dan het gen waaruit het komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor een intron? Kruis alles aan wat juist is.",
        opties=[
            "het wordt uit het pre-mRNA geknipt",
            "het komt niet in het eiwit terecht",
            "het blijft in het rijpe mRNA staan",
            "het ligt altijd vooraan in een gen",
        ],
        antwoord=[0, 1],
        uitleg="Introns liggen tussen de exons in het gen. Ze worden tijdens de splicing "
        "verwijderd, dus staan ze niet in het rijpe mRNA en niet in het eiwit.",
    ),
    dict(
        type="waarofniet",
        vraag="Een prokaryote cel knipt introns uit haar mRNA voor ze het vertaalt.",
        antwoord=False,
        uitleg="Prokaryoten hebben vrijwel geen introns en geen kern. Hun mRNA wordt al "
        "vertaald terwijl het nog gemaakt wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat beëindigt de transcriptie?",
        opties=[
            "een terminatiesignaal achter het gen",
            "het startcodon van het mRNA",
            "het losmaken van de poly(A)-staart",
            "het binden van het eerste tRNA",
        ],
        antwoord=0,
        uitleg="Bij de terminatie komt polymerase op een signaal en laat het mRNA los. Dat "
        "mRNA is dan nog pre-mRNA en moet nog afgewerkt worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Het mRNA is complementair aan de streng die als matrijs gelezen werd.",
        antwoord=True,
        uitleg="Op elke base van de matrijs komt de complementaire RNA-base, met U in "
        "plaats van T. Daardoor is het mRNA gelijk aan de sense-streng.",
    ),
    dict(
        type="meerkeuze",
        vraag="De matrijsstreng leest TAC CGA. Welk mRNA hoort daarbij?",
        opties=[
            "AUG GCU",
            "ATG GCT",
            "UAC CGA",
            "AUC GGA",
        ],
        antwoord=0,
        uitleg="T geeft A, A geeft U, C geeft G en G geeft C. Let op dat er in RNA geen T "
        "staat maar U.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gen wordt altijd van 3' naar 5' op het mRNA opgebouwd.",
        antwoord=False,
        uitleg="Het mRNA wordt, net als nieuw DNA, van 5' naar 3' gebouwd. De matrijs "
        "wordt daarvoor in de andere richting gelezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat er bij een eukaryoot niet meteen een eiwit klaar na de transcriptie?",
        opties=[
            "het mRNA moet eerst afgewerkt worden en de kern uit",
            "er is geen mRNA nodig voor een eiwit",
            "het DNA moet eerst gekopieerd worden",
            "het ribosoom zit in de kern",
        ],
        antwoord=0,
        uitleg="Transcriptie en translatie zijn in ruimte en tijd gescheiden. Bij een "
        "prokaryoot gebeuren ze wel vlak na elkaar in hetzelfde compartiment.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een transcriptiefactor?",
        opties=[
            "een eiwit dat helpt beslissen of een gen gelezen wordt",
            "een stuk RNA dat het eiwit afwerkt",
            "een enzym dat aminozuren verbindt",
            "een deel van het ribosoom",
        ],
        antwoord=0,
        uitleg="Transcriptiefactoren binden bij de promotor en maken de start mogelijk of "
        "juist niet. Zo bepaalt een cel welke genen ze gebruikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben alle cellen van één mens gemeen, en waarin verschillen ze? Kruis alles aan wat juist is.",
        opties=[
            "ze hebben hetzelfde DNA",
            "ze brengen niet dezelfde genen tot expressie",
            "ze hebben elk een ander aantal chromosomen",
            "ze maken alle eiwitten van het lichaam",
        ],
        antwoord=[0, 1],
        uitleg="Een spiercel en een zenuwcel hebben hetzelfde genoom. Dat ze er anders "
        "uitzien, komt doordat ze andere genen gebruiken; dat heet celspecifieke "
        "genexpressie.",
    ),
]

DEEL2 = [
    dict(
        type="invultekst",
        vraag="Waar in de cel gebeurt de translatie?",
        antwoord=["op het ribosoom", "ribosoom", "het ribosoom"],
        uitleg="De translatie gebeurt op de ribosomen, vrij in het cytoplasma of op het "
        "ruw endoplasmatisch reticulum. Daar wordt het mRNA in een aminozuurketen omgezet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaruit bestaat een ribosoom?",
        opties=[
            "uit rRNA en ribosomale proteïnen",
            "uit mRNA en tRNA",
            "uit DNA en histonen",
            "uit fosfolipiden en cholesterol",
        ],
        antwoord=0,
        uitleg="Een grote en een kleine subeenheid klikken rond het mRNA samen. Beide "
        "bestaan uit ribosomaal RNA met eiwitten erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een tRNA?",
        opties=[
            "een aminozuur naar het ribosoom brengen",
            "het mRNA van de kern naar buiten brengen",
            "het eiwit na de translatie afwerken",
            "de introns uit het mRNA knippen",
        ],
        antwoord=0,
        uitleg="Elk tRNA draagt één aminozuur en heeft een anticodon dat op het codon past. "
        "Zo komt het juiste aminozuur op de juiste plaats.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het drietal nucleotiden op een tRNA dat op het codon past?",
        antwoord=["anticodon", "het anticodon"],
        uitleg="Het anticodon is complementair aan het codon. Past het niet, dan blijft het "
        "tRNA niet zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het codon op het mRNA is GCU. Welk anticodon past daarop?",
        opties=[
            "CGA",
            "GCU",
            "CGT",
            "AGC",
        ],
        antwoord=0,
        uitleg="G past bij C, C bij G en U bij A. In RNA is er geen T, dus komt er een A "
        "tegenover de U.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij de activatie van een aminozuur?",
        opties=[
            "het wordt met ATP aan zijn tRNA gekoppeld",
            "het wordt in het ribosoom afgebroken",
            "het wordt aan het mRNA gehecht",
            "het wordt in de kern gevormd",
        ],
        antwoord=0,
        uitleg="Een enzym hangt het juiste aminozuur op het juiste tRNA, en dat kost "
        "energie. Pas daarna kan het tRNA naar het ribosoom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er op de A-plaats en de P-plaats van een ribosoom? Kruis alles aan wat juist is.",
        opties=[
            "op de A-plaats komt het nieuwe tRNA binnen",
            "op de P-plaats zit het tRNA met de groeiende keten",
            "op de A-plaats wordt het mRNA afgebroken",
            "op de P-plaats worden de introns geknipt",
        ],
        antwoord=[0, 1],
        uitleg="Het nieuwe tRNA komt op de A-plaats, de keten hangt aan het tRNA op de "
        "P-plaats. Daarna schuift het ribosoom één codon verder.",
    ),
    dict(
        type="invultekst",
        vraag="Welk enzym van het ribosoom legt de peptidebinding tussen twee aminozuren?",
        antwoord=["peptidyltransferase", "PT", "pt"],
        uitleg="Peptidyltransferase maakt de binding tussen het laatste aminozuur van de "
        "keten en het nieuwe. Zo groeit de keten aminozuur per aminozuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat beëindigt de translatie?",
        opties=[
            "een stopcodon en een release factor",
            "het laatste intron van het mRNA",
            "het losmaken van de poly(A)-staart",
            "het binden van een transcriptiefactor",
        ],
        antwoord=0,
        uitleg="Op een stopcodon past geen tRNA. Een release factor laat dan de keten en "
        "het ribosoom los.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stopcodon codeert voor een aminozuur dat de keten afsluit.",
        antwoord=False,
        uitleg="Een stopcodon codeert voor geen enkel aminozuur. Het is enkel een signaal "
        "om te stoppen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een polysoom?",
        opties=[
            "meerdere ribosomen op hetzelfde mRNA",
            "een ribosoom met meerdere mRNA's",
            "een keten van meerdere eiwitten",
            "een stuk DNA met meerdere genen",
        ],
        antwoord=0,
        uitleg="Verschillende ribosomen lezen hetzelfde mRNA na elkaar. Daardoor komen er "
        "in korte tijd veel kopieën van hetzelfde eiwit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het mRNA leest AUG GCU UAA. Hoeveel aminozuren heeft het eiwit?",
        opties=[
            "twee",
            "drie",
            "één",
            "zes",
        ],
        antwoord=0,
        uitleg="AUG en GCU geven elk een aminozuur, UAA is een stopcodon en geeft er geen. "
        "Dus blijven er twee over.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén aminozuur kan door meer dan één codon gevraagd worden.",
        antwoord=True,
        uitleg="Dat is precies wat een gedegenereerde code betekent. Leucine heeft er "
        "bijvoorbeeld zes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan één gen toch verschillende eiwitten opleveren? Kruis alles aan wat juist is.",
        opties=[
            "door alternatieve splicing van de exons",
            "doordat het eiwit achteraf nog bewerkt wordt",
            "door het leesraam met één plaats te verschuiven",
            "door het gen een tweede keer te kopiëren",
        ],
        antwoord=[0, 1],
        uitleg="Bij alternatieve splicing worden niet altijd dezelfde exons behouden, en "
        "na de translatie wordt de keten nog geknipt en geplooid. Een verschoven leesraam "
        "geeft geen bruikbaar eiwit maar een fout.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de bewerkingen die een eiwit ná de translatie nog ondergaat?",
        antwoord=[
            "posttranslationele modificatie",
            "posttranslationeel",
            "posttranslationele modificaties",
        ],
        uitleg="In het endoplasmatisch reticulum en het golgicomplex worden er groepen "
        "aangehangen, stukken afgeknipt en ketens geplooid. Pas daarna is het eiwit "
        "werkzaam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bewerkingen horen bij het afwerken van een eiwit? Kruis alles aan wat juist is.",
        opties=[
            "er worden sacharidegroepen aangehangen",
            "de keten wordt in haar vorm geplooid",
            "er worden introns uit de keten geknipt",
            "de keten wordt in DNA omgezet",
        ],
        antwoord=[0, 1],
        uitleg="Plooien, knippen en groepen aanhangen gebeuren na de translatie. Introns "
        "worden uit het mRNA geknipt, niet uit het eiwit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bepaalt de vorm van een eiwit zijn werking?",
        opties=[
            "alleen met de juiste vorm past het op zijn partner",
            "de vorm bepaalt hoeveel aminozuren erin zitten",
            "de vorm bepaalt welk gen gelezen wordt",
            "de vorm bepaalt in welke cel het eiwit zit",
        ],
        antwoord=0,
        uitleg="Een enzym past met zijn actief centrum op zijn substraat, een receptor op "
        "zijn hormoon. Gaat de vorm verloren, dan werkt het eiwit niet meer.",
    ),
    dict(
        type="waarofniet",
        vraag="De volgorde van de aminozuren in een eiwit volgt uit de volgorde van de nucleotiden in het gen.",
        antwoord=True,
        uitleg="Elk codon van drie nucleotiden geeft één aminozuur. Daarmee ligt de hele "
        "keten vast, en met die keten ook de vorm.",
    ),
    dict(
        type="waarofniet",
        vraag="Het DNA verlaat de kern om op het ribosoom gelezen te worden.",
        antwoord=False,
        uitleg="Het DNA blijft veilig in de kern. Het messenger-RNA is de boodschapper die "
        "de informatie naar het ribosoom brengt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een cel maakt plots veel meer van een bepaald eiwit. Wat is daarvoor de meest waarschijnlijke oorzaak?",
        opties=[
            "dat gen wordt vaker getranscribeerd",
            "dat gen is in het DNA verdwenen",
            "het eiwit heeft een andere vorm gekregen",
            "de cel heeft meer chromosomen gekregen",
        ],
        antwoord=0,
        uitleg="Hoe meer mRNA er van een gen gemaakt wordt, hoe meer eiwit de ribosomen "
        "ervan kunnen bouwen. Daarom werkt regulatie meestal op de transcriptie.",
    ),
]
