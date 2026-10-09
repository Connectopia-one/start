# -*- coding: utf-8 -*-
"""Van natuurfilosofie naar wetenschap: falsificatie en demarcatie.

Het derde van twaalf thema's over filosofie, en het tweede stuk kennisleer.
Hier wordt de vraag van het vorige thema scherper: niet waar kennis vandaan
komt, maar wanneer iets wétenschap mag heten.

De lijstjes staan letterlijk in de fiche:

    hoe natuurfilosofie evolueerde naar wetenschap
    de betekenis en de theorie van filosofen voor het ontwikkelen van de
        wetenschappelijke methode: Aristoteles, Francis Bacon, Karl Popper
    het demarcatievraagstuk: verificatie en falsificatie
    pseudowetenschappen
    vaardigheden: een filosofische vraag formuleren, de AUB-methode, en
        reflecteren over de wetenschapsfilosofie aan de hand van aangereikte
        bronnen en een stappenplan (bijlage 2)

Bijlage 2 is het stappenplan om een filosofische tekst te analyseren, met drie
stappen: globaal en oriënterend lezen, grondig lezen, en reflectie. Het kind
krijgt die bijlage niet op het examen, maar de inhoud kan wel gevraagd worden.
Daarom staan er in deel 2 drie vragen over.

De fiche geeft bij Aristoteles en Bacon geen stellingen mee, enkel hun
betekenis voor de wetenschappelijke methode. De vragen hieronder blijven dus
bij wat zij aan die methode toevoegden; er is geen uitspraak of boek aan hen
toegeschreven dat de fiche niet noemt.

Deel 1 is de weg van natuurfilosofie naar wetenschap, met Aristoteles en Bacon.
Deel 2 zijn Popper, het demarcatievraagstuk en de pseudowetenschappen.
"""

DEEL1 = [
    dict(type="meerkeuze",
         vraag="Wat deed de natuurfilosofie al wat de mythologie niet deed?",
         opties=["een verklaring in de natuur zelf zoeken, waarover te redetwisten valt",
                 "haar verklaringen vastleggen in verhalen over goden en helden",
                 "haar uitspraken altijd eerst in een proefopstelling nameten",
                 "zich beperken tot vragen over goed en kwaad en niets anders"],
         antwoord=0,
         uitleg="De natuurfilosofie legt de oorzaak binnen de natuur, en haar verklaring valt "
                "daardoor te betwisten. Dat is de eerste stap naar wetenschap."),
    dict(type="meerkeuze",
         vraag="Wat kwam er in de stap van natuurfilosofie naar wetenschap bij?",
         opties=["een vaste methode, met systematische waarneming",
                 "de proef, waarmee je een verklaring kan toetsen",
                 "de overtuiging dat alleen het denken tot kennis kan leiden",
                 "de gewoonte om elke verklaring in een verhaal te gieten"],
         antwoord=[0, 1],
         uitleg="Natuurfilosofie redeneerde over de natuur; wetenschap voegt daar een methode en "
                "een proef aan toe waarmee anderen je uitspraak kunnen nagaan."),
    dict(type="meerkeuze",
         vraag="Welke rol speelt Aristoteles volgens de fiche in het ontstaan van de "
               "wetenschappelijke methode?",
         opties=["hij nam de natuur systematisch waar en bracht ze in soorten onder",
                 "hij verwierp de waarneming en vertrouwde alleen op het denken",
                 "hij vond het experiment uit zoals wij het vandaag kennen",
                 "hij bedacht het begrip falsificatie als maatstaf voor wetenschap"],
         antwoord=0,
         uitleg="Aristoteles kijkt naar de natuur en ordent wat hij ziet. Daarmee zet hij "
                "waarneming en indeling als werkwijze neer."),
    dict(type="meerkeuze",
         vraag="Welke rol speelt Francis Bacon volgens de fiche?",
         opties=["hij maakte van de proef en de geordende waarneming een echte methode",
                 "hij bewees dat kennis enkel uit het denken kan komen",
                 "hij toonde aan dat een theorie nooit weerlegd kan worden",
                 "hij schreef de eerste verhalen over de goden van de natuur"],
         antwoord=0,
         uitleg="Bacon legt het gewicht bij het stelselmatig verzamelen en bij de proef, en "
                "waarschuwt tegen het aannemen van wat men altijd al geloofd heeft."),
    dict(type="meerkeuze",
         vraag="Waarom is een vaste methode zo belangrijk voor een wetenschap?",
         opties=["omdat een ander je werk dan kan overdoen en kan nagaan",
                 "omdat een theorie daardoor niet meer tegengesproken kan worden",
                 "omdat je dan geen waarnemingen meer nodig hebt",
                 "omdat elke onderzoeker dan hetzelfde zal vinden, wat er ook gebeurt"],
         antwoord=0,
         uitleg="Een methode maakt je werk <em>navolgbaar</em>: iemand anders kan het overdoen. "
                "Zonder dat is het een mening."),
    dict(type="meerkeuze",
         vraag="Welke uitspraken over de overgang van natuurfilosofie naar wetenschap kloppen?",
         opties=["wetenschap werkt met een methode die anderen kunnen nagaan",
                 "de natuurfilosofie zocht de oorzaak al binnen de natuur zelf",
                 "de wetenschap heeft de filosofie overbodig gemaakt",
                 "de natuurfilosofie werkte al met gecontroleerde proeven"],
         antwoord=[0, 1],
         uitleg="De eerste twee. De filosofie is niet overbodig geworden: de vraag wanneer iets "
                "wetenschap is, is zelf een filosofische vraag."),
    dict(type="meerkeuze",
         vraag="Wat is het demarcatievraagstuk?",
         opties=["de vraag waar de grens ligt tussen wetenschap en wat dat niet is",
                 "de vraag of de natuurwetenschappen beter zijn dan de menswetenschappen",
                 "de vraag of een onderzoeker zijn eigen mening mag geven",
                 "de vraag of de wetenschap ooit af zal zijn"],
         antwoord=0,
         uitleg="Demarcatie betekent afbakening. Het vraagstuk zoekt een maatstaf om wetenschap "
                "van niet-wetenschap te onderscheiden."),
    dict(type="meerkeuze",
         vraag="Wat is verificatie?",
         opties=["een theorie bevestigd zien door waarnemingen die erbij passen",
                 "een theorie onderuithalen met één waarneming die er niet bij past",
                 "een theorie zo opschrijven dat ze niet te weerleggen valt",
                 "een theorie vergelijken met een oudere theorie over hetzelfde"],
         antwoord=0,
         uitleg="Verifiëren is waarmaken: je zoekt gevallen die je theorie bevestigen."),
    dict(type="meerkeuze",
         vraag="Wat is falsificatie?",
         opties=["een theorie weerleggen met een waarneming die er niet bij past",
                 "een theorie bevestigen met zoveel mogelijk voorbeelden",
                 "een theorie omschrijven zodat ze op meer gevallen past",
                 "een theorie opzij zetten omdat ze te oud is"],
         antwoord=0,
         uitleg="Falsifiëren is onderuithalen. Eén tegenvoorbeeld is genoeg om een algemene "
                "uitspraak te weerleggen."),
    dict(type="meerkeuze",
         vraag="Je hebt duizend witte zwanen gezien. Wat bewijst dat over de uitspraak dat alle "
               "zwanen wit zijn?",
         opties=["niets met zekerheid, want de volgende zwaan kan zwart zijn",
                 "dat de uitspraak nu bewezen is en niet meer kan sneuvelen",
                 "dat de uitspraak onmiddellijk weerlegd is door die duizend",
                 "dat de uitspraak geen wetenschappelijke uitspraak kan zijn"],
         antwoord=0,
         uitleg="Dit is het beroemde voorbeeld bij de falsificatie: geen enkel aantal bevestigingen "
                "maakt een algemene uitspraak zeker, en één zwarte zwaan haalt ze onderuit."),
    dict(type="meerkeuze",
         vraag="Waarom is bevestiging zoeken zwakker dan tegenspraak zoeken?",
         opties=["bevestiging vind je makkelijk, ook voor een theorie die niet klopt",
                 "bevestiging is verboden binnen de wetenschappelijke methode",
                 "bevestiging kan enkel in de menswetenschappen gevonden worden",
                 "bevestiging kost meer tijd dan het zoeken van een tegenvoorbeeld"],
         antwoord=0,
         uitleg="Wie zoekt, vindt: voor zowat elke theorie vind je wel passende gevallen. De "
                "echte toets is of je er ook naar hebt gezocht wat haar zou breken."),
    dict(type="meerkeuze",
         vraag="Een onderzoeker stelt zijn proef zo op dat ze zijn stelling onderuit kán halen. "
               "Wat doet hij?",
         opties=["hij stelt zijn theorie bloot aan falsificatie",
                 "hij verifieert zijn theorie zo sterk mogelijk",
                 "hij maakt zijn theorie onweerlegbaar",
                 "hij verlaat de wetenschappelijke methode"],
         antwoord=0,
         uitleg="Juist dat is wat een wetenschappelijke houding volgens Popper kenmerkt: je zoekt "
                "zelf naar wat je ongelijk zou geven."),
    dict(type="waarofniet",
         vraag="Volgens de fiche droegen Aristoteles, Francis Bacon en Karl Popper elk bij aan de "
               "ontwikkeling van de wetenschappelijke methode.",
         antwoord=True,
         uitleg="Waar. De fiche noemt die drie namen bij de wetenschappelijke methode."),
    dict(type="waarofniet",
         vraag="Demarcatie betekent het bevestigen van een theorie met zoveel mogelijk "
               "voorbeelden.",
         antwoord=False,
         uitleg="Niet waar. Demarcatie betekent afbakening: waar ligt de grens tussen wetenschap "
                "en wat dat niet is. Bevestigen met voorbeelden is verificatie."),
    dict(type="waarofniet",
         vraag="Eén tegenvoorbeeld kan een algemene uitspraak weerleggen.",
         antwoord=True,
         uitleg="Waar. Dat is de kracht van de falsificatie, en het verschil met verificatie: geen "
                "enkel aantal bevestigingen maakt een algemene uitspraak zeker."),
    dict(type="waarofniet",
         vraag="De natuurfilosofie werkte al met een vaste methode en met proeven.",
         antwoord=False,
         uitleg="Niet waar. Ze zocht de oorzaak wel al in de natuur zelf, maar de methode en de "
                "proef kwamen pas met de wetenschap."),
    dict(type="invultekst",
         vraag="Hoe heet het vraagstuk over de grens tussen wetenschap en niet-wetenschap? Het ...",
         antwoord=["demarcatievraagstuk", "demarcatieprobleem"],
         uitleg="Demarcatie betekent afbakening."),
    dict(type="invultekst",
         vraag="Hoe heet het bevestigen van een theorie met waarnemingen die erbij passen?",
         antwoord=["verificatie"],
         uitleg="Verifiëren is waarmaken; falsifiëren is onderuithalen."),
    dict(type="invultekst",
         vraag="Hoe heet het weerleggen van een theorie met een waarneming die er niet bij past?",
         antwoord=["falsificatie"],
         uitleg="Eén tegenvoorbeeld volstaat om een algemene uitspraak te falsifiëren."),
    dict(type="invultekst",
         vraag="Welke filosoof uit de oudheid nam volgens de fiche de natuur systematisch waar en "
               "bracht ze in soorten onder?",
         antwoord=["Aristoteles"],
         uitleg="De fiche noemt Aristoteles, Francis Bacon en Karl Popper bij de "
                "wetenschappelijke methode."),
]

DEEL2 = [
    dict(type="meerkeuze",
         vraag="Welk antwoord geeft Karl Popper op het demarcatievraagstuk?",
         opties=["een uitspraak is wetenschappelijk als ze weerlegd kan worden",
                 "een uitspraak is wetenschappelijk als ze bevestigd is door veel gevallen",
                 "een uitspraak is wetenschappelijk als een deskundige ze onderschrijft",
                 "een uitspraak is wetenschappelijk als ze nergens tegenspraak vindt"],
         antwoord=0,
         uitleg="Falsifieerbaarheid is bij Popper de maatstaf: een theorie die niets uitsluit, is "
                "geen wetenschap."),
    dict(type="meerkeuze",
         vraag="Wat is er mis met een theorie die alles kan verklaren?",
         opties=["ze sluit niets uit, en dus kan geen enkele waarneming haar weerleggen",
                 "ze is te moeilijk om door gewone mensen begrepen te worden",
                 "ze verklaart te veel om nuttig te kunnen zijn in de praktijk",
                 "ze is nooit door genoeg onderzoekers bevestigd geraakt"],
         antwoord=0,
         uitleg="Hoe meer een theorie verklaart, hoe minder ze zegt. Wat met elke uitkomst te "
                "rijmen valt, loopt geen enkel risico."),
    dict(type="meerkeuze",
         vraag="Wat is een pseudowetenschap?",
         opties=["iets wat zich als wetenschap voordoet zonder de methode te volgen",
                 "een wetenschap die nog niet genoeg onderzoek heeft gedaan",
                 "een wetenschap die haar theorie ooit heeft moeten bijstellen",
                 "een wetenschap die over de mens gaat in plaats van over de natuur"],
         antwoord=0,
         uitleg="Pseudo betekent vals of schijn. Een pseudowetenschap leent de taal van de "
                "wetenschap maar niet haar methode."),
    dict(type="meerkeuze",
         vraag="Welke kenmerken wijzen op een pseudowetenschap?",
         opties=["de uitspraken zijn zo vaag dat geen enkele uitkomst ze kan tegenspreken",
                 "tegenspraak wordt weggeredeneerd in plaats van onderzocht",
                 "de theorie is in de loop van de jaren bijgesteld na nieuw onderzoek",
                 "de uitspraken zijn met een meting te toetsen"],
         antwoord=[0, 1],
         uitleg="De eerste twee. Een theorie bijstellen na nieuw onderzoek is net wél "
                "wetenschappelijk, en toetsbare uitspraken ook."),
    dict(type="meerkeuze",
         vraag="Een voorspelling luidt: er komt binnenkort een belangrijke verandering in je "
               "leven. Waarom is dat volgens Popper niet wetenschappelijk?",
         opties=["ze sluit niets uit, dus geen enkele gebeurtenis kan haar weerleggen",
                 "ze gaat over de toekomst, en daarover kan je niets weten",
                 "ze is te kort om een echte theorie te kunnen zijn",
                 "ze is nog door niemand bevestigd"],
         antwoord=0,
         uitleg="Elke uitkomst past erbij. Een voorspelling die niet kan sneuvelen, zegt niets."),
    dict(type="meerkeuze",
         vraag="Een arts zegt: als dit middel werkt, zakt de koorts binnen drie dagen bij "
               "minstens zeven op de tien patiënten. Wat is daaraan wetenschappelijk?",
         opties=["de uitspraak sluit uitkomsten uit en kan dus weerlegd worden",
                 "de uitspraak is door een deskundige gedaan",
                 "de uitspraak gaat over iets wat je kan waarnemen",
                 "de uitspraak klinkt redelijk en voorzichtig"],
         antwoord=0,
         uitleg="Precies dit maakt het verschil: de uitspraak zegt op voorhand welke uitkomst haar "
                "ongelijk zou geven."),
    dict(type="meerkeuze",
         vraag="Betekent falsifieerbaar dat een theorie fout is?",
         opties=["nee, het betekent dat ze fout zou kúnnen blijken",
                 "ja, het betekent dat ze al weerlegd is",
                 "ja, het betekent dat ze binnenkort weerlegd zal worden",
                 "nee, het betekent dat ze voor altijd bewezen is"],
         antwoord=0,
         uitleg="Falsifieerbaar is een eigenschap van de <em>vorm</em> van de uitspraak: ze loopt "
                "een risico. Dat is een pluspunt, geen fout."),
    dict(type="meerkeuze",
         vraag="Wat doe je in stap 1 van het stappenplan om een filosofische tekst te analyseren?",
         opties=["de tekst in zijn geheel lezen en zicht krijgen op de structuur",
                 "elke onbekende uitdrukking opzoeken en moeilijke zinnen ontleden",
                 "bedenken welke kritiek je zelf op de auteur hebt",
                 "meteen een samenvatting van enkele zinnen schrijven"],
         antwoord=0,
         uitleg="Stap 1 is globaal en oriënterend lezen: de indeling, de signaalwoorden en de "
                "kernbegrippen, met in elke alinea een kernzin."),
    dict(type="meerkeuze",
         vraag="Wat doe je in stap 2 van dat stappenplan?",
         opties=["grondig herlezen, woorden opzoeken en verbanden aanduiden",
                 "de tekst snel doorbladeren om de structuur te zien",
                 "nadenken over wat je er zelf van vindt",
                 "de tekst vergelijken met een tekst van een andere auteur"],
         antwoord=0,
         uitleg="Stap 2 is grondig lezen. De maatstaf die de fiche geeft: je moet het daarna met "
                "eigen woorden aan een vriend kunnen uitleggen."),
    dict(type="meerkeuze",
         vraag="Welke vraag hoort bij stap 3, de reflectie?",
         opties=["welke tegenvoorbeelden kan ik vinden voor deze conclusie?",
                 "waar staan de alinea's en de signaalwoorden?",
                 "wat betekent dit onbekende woord precies?",
                 "hoeveel hoofdstukken heeft deze tekst?"],
         antwoord=0,
         uitleg="Bij de reflectie zoek je tegenvoorbeelden, formuleer je je kritiek en vraag je je "
                "af hoe de auteur daarop zou antwoorden."),
    dict(type="meerkeuze",
         vraag="Waarom is het volgens dat stappenplan nuttig om te bedenken hoe de auteur op jouw "
               "kritiek zou antwoorden?",
         opties=["omdat je zo nagaat of je kritiek wel standhoudt",
                 "omdat je de auteur daarmee kan overtuigen van je gelijk",
                 "omdat je anders de tekst niet mag samenvatten",
                 "omdat elke kritiek beantwoord moet zijn voor ze telt"],
         antwoord=0,
         uitleg="Je kritiek is pas sterk als ze het antwoord van de auteur overleeft. Daarom staat "
                "die vraag in het stappenplan."),
    dict(type="meerkeuze",
         vraag="Waarom hoort de vraag wanneer iets wetenschap is bij de filosofie en niet bij de "
               "wetenschap zelf?",
         opties=["omdat geen enkele meting die vraag kan beslechten",
                 "omdat wetenschappers zich nooit met die vraag bezighouden",
                 "omdat de wetenschap geen methode heeft om iets te onderzoeken",
                 "omdat filosofen beter kunnen meten dan wetenschappers"],
         antwoord=0,
         uitleg="Het is een vraag over de maatstaf zelf, en een maatstaf kan je niet met diezelfde "
                "maatstaf afmeten. Dat is wetenschapsfilosofie."),
    dict(type="waarofniet",
         vraag="Voor Popper is een theorie wetenschappelijk als ze weerlegd kan worden.",
         antwoord=True,
         uitleg="Waar. Falsifieerbaarheid is zijn antwoord op het demarcatievraagstuk."),
    dict(type="waarofniet",
         vraag="Een theorie die alles kan verklaren, staat juist heel sterk.",
         antwoord=False,
         uitleg="Niet waar. Ze sluit niets uit en loopt dus geen risico. Volgens Popper is dat "
                "precies de zwakte."),
    dict(type="waarofniet",
         vraag="Een theorie bijstellen na nieuw onderzoek is een teken van pseudowetenschap.",
         antwoord=False,
         uitleg="Niet waar. Dat is net wetenschappelijk. Pseudowetenschap redeneert de tegenspraak "
                "weg in plaats van haar theorie aan te passen."),
    dict(type="waarofniet",
         vraag="Het stappenplan voor een filosofische tekst telt drie stappen: oriënterend lezen, "
               "grondig lezen en reflectie.",
         antwoord=True,
         uitleg="Waar. Dat zijn de drie stappen van bijlage 2."),
    dict(type="invultekst",
         vraag="Welke filosoof koppelt de fiche aan de falsificatie?",
         antwoord=["Karl Popper", "Popper"],
         uitleg="Popper stelt falsifieerbaarheid voor als maatstaf voor wetenschap."),
    dict(type="invultekst",
         vraag="Hoe noem je iets dat zich als wetenschap voordoet zonder de methode te volgen? Een ...",
         antwoord=["pseudowetenschap"],
         uitleg="Pseudo betekent vals of schijn."),
    dict(type="invultekst",
         vraag="Hoeveel stappen telt het stappenplan om een filosofische tekst te analyseren?",
         antwoord=["drie", "3"],
         uitleg="Oriënterend lezen, grondig lezen en reflectie."),
    dict(type="invultekst",
         vraag="In welke stap van dat stappenplan zoek je tegenvoorbeelden en formuleer je je "
               "kritiek? In de ...",
         antwoord=["reflectie", "derde stap"],
         uitleg="Stap 3 is de reflectie."),
]
