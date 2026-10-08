# -*- coding: utf-8 -*-
"""De leerbundels en oefenbundels voor Engels op 🌍 Beyond-niveau.

Gebaseerd op de fiches Engels 1 en Engels 2 van de derde graad
doorstroomfinaliteit domeingebonden, geldig vanaf 1 januari 2027. Die gelden
voor bedrijfswetenschappen en welzijnswetenschappen. Engels 1 weegt lezen en
luisteren elk de helft; Engels 2 is het productieve examen: schrijven,
schriftelijke interactie en een gesprek. Het ERK-niveau is B1.

Deze bundels dekken wat een platform met tekstvragen kán dragen: lezen, de
tekstsoorten, de woordvelden en de grammaticalijst. Luisteren, spreken en het
gesprek staan er niet in, en daarom staat in elke bundel achteraan hetzelfde
kader dat de leerling daar zelf naar stuurt.

De lijst van deze fiche gaat verder dan die van 🚀 Boost: de gerund, de
frequente semi-auxiliaries, de trappen van vergelijking bij de bijwoorden, de
indirect speech en de active en passive voice horen erbij. De voorbeelden
hieronder zijn andere dan die van Boost.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen, dus Kim laadt dezelfde bundel twee keer op.

De bundelsleutels eindigen op "-beyond", de naam van de categorie. Dat
achtervoegsel is nodig omdat de themanamen van Beyond botsen met die van
Boost en Spark.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Engels"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
NA = "-beyond"
tabel = bundel.tabel

BUNDELS = {}


def spreken(opdracht):
    """Het vaste slotkader over wat je niet achter een scherm leert."""
    return dict(kop="Oefen dit ook buiten het scherm", blokken=[
        ("p", "Op dit platform oefen je lezen, woordenschat en grammatica. Maar <strong>luisteren</strong> "
              "is de helft van het examen Engels 1, en Engels 2 bestaat uit <strong>schrijven</strong>, "
              "<strong>schriftelijke interactie</strong> en <strong>een gesprek</strong>. Luisteren en "
              "spreken leer je niet achter een scherm. Je leert ze door te luisteren naar mensen die echt "
              "Engels spreken, en door zelf je mond open te doen, ook als het hakkelt."),
        ("kader", "<strong>Deze week:</strong> " + opdracht + " Doe het één keer, en let daarna op wat je "
                  "miste of niet gezegd kreeg. Dat is precies je volgende oefening."),
    ])


def zet(sleutel, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BEYOND)
    BUNDELS[sleutel + NA] = b


# ───────────────────────── 1. Een Engelse tekst analyseren
zet("een-engelse-tekst-analyseren",
    titel="Een Engelse tekst analyseren",
    onder="Onderwerp, hoofdgedachte en hoofdpunten, verwijswoorden en signaalwoorden, en wat modale hulpwerkwoorden met de betekenis doen.",
    secties=[
        dict(kop="Onderwerp, hoofdgedachte en hoofdpunten", blokken=[
            ("p", "Drie woorden die op elkaar lijken en die je uit elkaar moet houden. "
                  "<strong>De hoofdgedachte van een tekst is niet hetzelfde als het onderwerp.</strong>"),
            ("p", tabel(["", "hoe lang", "voorbeeld"],
                        [["onderwerp", "enkele woorden", "uitleenfietsen in Leeds"],
                         ["hoofdgedachte", "een hele zin", "Te weinig slaap is slecht voor het hart."],
                         ["hoofdpunten", "de zinnen eronder", "de elementen die de hoofdgedachte dragen"]])),
            ("p", "Lees: <em>Since January, the city of Leeds has lent electric bikes to residents without "
                  "a car. A thousand people have already applied.</em> Het onderwerp zeg je in enkele "
                  "woorden: <strong>uitleenfietsen in Leeds</strong>."),
            ("p", "Lees: <em>Sleeping less than six hours a night raises the risk of heart disease. "
                  "Researchers therefore advise going to bed earlier.</em> De hoofdgedachte is een hele "
                  "zin: <strong>te weinig slaap is slecht voor het hart</strong>."),
            ("p", "Lees: <em>This novel tells the story of a Welsh family during the war. The author drew "
                  "on her grandmother's diary.</em> De hoofdpunten zijn de drie dingen die de tekst "
                  "daarover kwijt wil: <strong>het boek gaat over een Welsh gezin</strong>, <strong>het "
                  "verhaal speelt tijdens de oorlog</strong> en <strong>de schrijfster gebruikte een "
                  "dagboek</strong>."),
            ("kader", "<strong>Bij een leesvraag mag je het antwoord niet halen uit wat je zelf al over "
                      "het onderwerp weet, zeker niet als het de tekst tegenspreekt.</strong> Het antwoord "
                      "staat in de tekst, ook als je het beter denkt te weten. En <strong>de titel, de "
                      "tussentitels en de foto bij een tekst mag je niet overslaan</strong>: ze horen er "
                      "wel degelijk bij en geven vaak de hoofdgedachte weg."),
        ]),
        dict(kop="Gericht zoeken", blokken=[
            ("p", "Soms hoef je de tekst niet te begrijpen, enkel één gegeven te vinden."),
            ("p", tabel(["de zin", "de vraag", "het antwoord"],
                        [["The museum is closed on Mondays.", "op welke dag gesloten?", "Monday"],
                         ["Your parcel will arrive between 2 and 4 p.m.", "ten vroegste?", "2"],
                         ["Admission is free for under-12s.", "tot welke leeftijd gratis?", "12"],
                         ["There are only two seats left.", "hoeveel plaatsen vrij?", "nog maar twee"]])),
            ("p", "Lees: <em>The 7.12 train has been cancelled. Passengers should take the replacement bus "
                  "outside the station.</em> Drie dingen staan er: <strong>de trein rijdt niet</strong>, "
                  "<strong>er staat een vervangbus klaar</strong> en <strong>de bus staat buiten het "
                  "station</strong>."),
            ("p", "Lees: <em>Year 13 students sit their A-levels in June.</em> Dat gaat over "
                  "<strong>leerlingen van het laatste jaar</strong>: in Engeland loopt de school tot Year "
                  "13, en de A-levels zijn de eindexamens."),
            ("p", "Lees: <em>This guide is aimed at parents of gifted children.</em> De gids is bedoeld "
                  "<strong>voor ouders van hoogbegaafde kinderen</strong>."),
            ("p", "Lees: <em>Warning: this product may contain traces of nuts.</em> Dat is vooral "
                  "belangrijk <strong>voor wie allergisch is aan noten</strong>."),
        ]),
        dict(kop="Tussen de regels lezen", blokken=[
            ("p", "Een paar zinnen waar het antwoord net niet letterlijk in staat."),
            ("p", tabel(["de zin", "wat ze zegt"],
                        [["It was not necessary to cancel the concert.", "het concert ging door"],
                         ["The library will be open on Sunday, exceptionally.", "bij uitzondering"],
                         ["Owing to a lack of volunteers, the fair will not take place.",
                          "er zijn te weinig vrijwilligers"],
                         ["The film, though praised by critics, drew few viewers.",
                          "lof, maar weinig volk"],
                         ["The works will last until the end of the month, unless it rains.",
                          "bij regen kan het langer duren"]])),
            ("p", "Let op <em>not necessary</em>: dat zegt dat het niet nódig was, dus is het niet "
                  "gebeurd. En <em>unless</em> betekent tenzij: <strong>als het regent</strong> kunnen de "
                  "werken langer duren."),
            ("p", "Lees: <em>According to the author, social media are not to blame for everything.</em> "
                  "Het standpunt is: <strong>sociale media krijgen te veel de schuld</strong>."),
            ("p", "Lees: <em>I am writing to report an error on my bill.</em> De schrijver wil <strong>een "
                  "fout melden</strong>. Dat is de vaste openingszin van een klachtenmail."),
        ]),
        dict(kop="Verwijswoorden", blokken=[
            ("p", "Verwijswoorden dragen de samenhang tussen de zinnen. De fiche noemt drie groepen: "
                  "<strong>he, she, it, they</strong>, <strong>this, that, these, those</strong> en "
                  "<strong>the former, the latter</strong>."),
            ("p", "<strong>In <em>the former</em> verwijst <em>former</em> naar het eerste van twee "
                  "genoemde dingen</strong>, en <em>the latter</em> naar het tweede."),
            ("p", tabel(["de zinnen", "het verwijswoord", "waarnaar"],
                        [["Sarah called her brother. He did not pick up.", "he", "naar de broer van Sarah"],
                         ["The council approved the plan. It will cost two million pounds.", "it",
                          "naar het plan"],
                         ["The students handed in their essays. They were late.", "they",
                          "students, het meest logisch"],
                         ["What I remember most is her courage.", "what",
                          "naar de moed verder in de zin"]])),
            ("p", "Bij <em>They were late</em> kan <em>they</em> grammaticaal naar allebei verwijzen, maar "
                  "<strong>students</strong> is het logische: opstellen komen niet te laat uit zichzelf."),
        ]),
        dict(kop="Modale hulpwerkwoorden", blokken=[
            ("p", "De fiche noemt <strong>can en may</strong>, <strong>should en could</strong>, en "
                  "<strong>must</strong>. Ze veranderen de betekenis van een zin volledig, en daarom staan "
                  "ze bij het lezen en niet bij de grammatica alleen."),
            ("p", tabel(["zin", "wat het hulpwerkwoord zegt"],
                        [["You must hand in your essay on Friday.", "het is verplicht"],
                         ["You should hand in your essay on Friday.", "het is een advies"],
                         ["The results may be wrong.", "het kán, het is niet zeker"],
                         ["She can't have known about it.", "ze kan het niet geweten hebben"]])),
            ("p", "Het modale hulpwerkwoord voor een verplichting is <strong>must</strong>, vier letters. "
                  "En let op <em>may</em>: <strong>The results may be wrong</strong> zegt <strong>niet dat "
                  "de resultaten zeker verkeerd zijn</strong>, enkel dat het kan."),
        ]),
        dict(kop="Signaalwoorden", blokken=[
            ("p", "Signaalwoorden zeggen welk verband er tussen twee zinnen ligt. Wie ze herkent, leest "
                  "een moeilijke tekst twee keer zo snel."),
            ("p", tabel(["signaalwoord", "verband"],
                        [["however", "een tegenstelling"],
                         ["whereas", "een tegenstelling"],
                         ["although", "een toegeving"],
                         ["therefore, as a result, consequently", "een gevolg"],
                         ["indeed", "een onderbouwing van wat er net stond"]])),
            ("p", "De woorden die een gevolg aankondigen zijn <strong>therefore</strong>, <strong>as a "
                  "result</strong> en <strong>consequently</strong>. Het woord van negen letters dat daarom "
                  "betekent, is <strong>therefore</strong>."),
            ("p", "<strong>Although kondigt een toegeving aan</strong>: de schrijver geeft iets toe en zegt "
                  "er daarna iets tegenin. Lees: <em>Whereas the north is suffering drought, the south is "
                  "flooded.</em> <em>Whereas</em> legt hier <strong>een tegenstelling</strong>."),
            ("p", "Lees: <em>Young people read less than before. Indeed, a survey shows that…</em> De "
                  "tweede zin <strong>onderbouwt de eerste</strong>."),
        ]),
        dict(kop="Een onbekend woord uit elkaar halen", blokken=[
            ("p", "Lees: <em>This book is unreadable.</em> Je hoeft dat woord niet te kennen: je leidt het "
                  "af <strong>uit <em>read</em> plus <em>un-</em> en <em>-able</em></strong>. Un- maakt het "
                  "tegendeel, -able betekent dat het kan, dus: niet te lezen."),
            ("p", tabel(["deel", "wat het doet", "voorbeeld"],
                        [["un-, in-, dis-", "maakt het tegendeel", "unfair, incorrect, dislike"],
                         ["-able, -ible", "het kan gedaan worden", "readable, visible"],
                         ["-less", "zonder", "homeless, careless"],
                         ["-ful", "vol van", "careful, useful"],
                         ["-ness, -ity", "maakt er een zelfstandig naamwoord van", "kindness, ability"]])),
        ]),
        spreken("luister vijftien minuten naar een Engelstalige podcast over iets wat je toch al "
                "interesseert, en vertel daarna aan iemand in het Engels waar hij over ging."),
    ])


# ───────────────────────── 2. Tekstsoorten en de bedoeling van een tekst
zet("tekstsoorten-en-de-bedoeling-van-een-tekst",
    titel="Tekstsoorten en de bedoeling van een tekst",
    onder="De vijf tekstsoorten, feit tegenover mening, en hoe je doel, publiek en toon van een tekst herkent.",
    secties=[
        dict(kop="De tekstsoorten", blokken=[
            ("p", tabel(["soort", "wat hij doet", "voorbeeld"],
                        [["informatief", "iets te weten geven", "een encyclopedie, een nieuwsbericht"],
                         ["prescriptief", "zeggen wat je moet doen", "een recept, een handleiding"],
                         ["argumentatief", "je van iets overtuigen", "een opiniestuk, een reclametekst"],
                         ["narratief", "een verhaal vertellen", "een reisverslag, een roman"],
                         ["artistiek-literair", "iets moois maken met taal", "een gedicht, een roman"]])),
            ("p", "Een tekst die je van iets wil overtuigen, is <strong>argumentatief</strong>. "
                  "<strong>Eén tekst kan meer dan één soort tegelijk zijn</strong>: een reisverslag is "
                  "narratief en informatief, een roman is narratief en artistiek-literair."),
            ("p", tabel(["de tekst", "de soort"],
                        [["Mix the flour and the butter. Then add the eggs.", "prescriptief"],
                         ["The United Kingdom consists of four countries.", "informatief"],
                         ["It was the best of times, it was the worst of times.", "artistiek-literair"],
                         ["Last summer we drove to Cornwall. On the second day the car broke down.",
                          "narratief"],
                         ["Three reasons why we should ban cars from the city centre.", "argumentatief"]])),
            ("p", "<strong>Prescriptief</strong> zijn <strong>een gebruiksaanwijzing</strong>, <strong>een "
                  "recept uit een kookboek</strong> en <strong>de spelregels van een spel</strong>. "
                  "<em>Keep out of reach of children</em> staat <strong>op een verpakking</strong>."),
            ("p", "Een <strong>narratieve</strong> tekst verraadt zich door <strong>een verloop in de "
                  "tijd</strong>, <strong>personages die iets doen</strong> en <strong>veel verleden "
                  "tijden</strong>. Lees: <em>Once upon a time, in a village near the sea…</em> Daarna "
                  "verwacht je <strong>een verhaal</strong>."),
            ("p", "Twee valstrikken. <strong>Een reclametekst is niet zuiver informatief</strong>, al geeft "
                  "hij je gegevens: hij wil je iets doen kopen, dus hij is argumentatief. En <strong>een "
                  "gedicht hoort niet bij de informatieve teksten</strong>: het is artistiek-literair, ook "
                  "al steek je er iets van op."),
        ]),
        dict(kop="De opmaak verraadt de soort", blokken=[
            ("p", "<strong>Bij de soort van een tekst helpt het om naar de opmaak te kijken: kolommen, een "
                  "kader, een nummering.</strong> Je ziet vaak al wat voor tekst het is voor je één woord "
                  "gelezen hebt."),
            ("p", tabel(["wat je ziet", "wat het is"],
                        [["Tickets: £12. Doors open at 7 p.m.", "praktische info bij een concert"],
                         ["Minutes of the meeting of 4 March. Present: six members.",
                          "een verslag van een vergadering"],
                         ["Dear Sir or Madam … I look forward to hearing from you", "een formele brief"]])),
            ("p", "Van een brief maken deze stukken een <strong>formele</strong> brief: <strong>Dear Sir "
                  "or Madam</strong>, <strong>with regard to</strong> en <strong>I look forward to hearing "
                  "from you</strong>."),
            ("p", "In een krantenkop valt het werkwoord weg: <em>Man <strong>is</strong> injured in "
                  "fire</em> wordt gewoon <em>Man injured in fire</em>. De korte samenvatting bovenaan een "
                  "artikel heet de <strong>lead</strong>, vier letters, hetzelfde woord als lood."),
        ]),
        dict(kop="Feit of mening", blokken=[
            ("p", tabel(["zin", "feit of mening"],
                        [["Water boils at 100 degrees Celsius.", "een feit"],
                         ["Tea tastes better than coffee.", "een mening"],
                         ["This is the finest novel of the year.", "een mening"],
                         ["Everyone should learn a second language.", "een mening"],
                         ["The film was far too long.", "een mening"]])),
            ("p", "Een feit kan je nagaan, een mening niet. Let op woorden als <em>finest</em>, "
                  "<em>should</em> en <em>far too</em>: die dragen een oordeel."),
            ("p", "<strong>Een tekst die vol cijfers staat, geeft daarmee niet automatisch de "
                  "waarheid.</strong> Cijfers kunnen geselecteerd, verouderd of uit hun verband getrokken "
                  "zijn. Kijk wie ze geeft en waar ze vandaan komen."),
            ("p", "Lees: <em>In my view, homework does more harm than good.</em> <em>In my view</em> "
                  "kondigt <strong>een mening van de schrijver</strong> aan."),
            ("p", "Lees: <em>Not everyone agrees with this view.</em> Die zegt dat <strong>sommigen het er "
                  "niet mee eens zijn</strong>."),
        ]),
        dict(kop="Doel, publiek en toon", blokken=[
            ("p", "Drie Engelse woorden die je moet kennen: <strong>purpose</strong> (zeven letters) is het "
                  "<strong>doel</strong>, <strong>audience</strong> (acht letters) is het "
                  "<strong>publiek</strong>, en <strong>tone</strong> (vier letters) is de "
                  "<strong>toon</strong>."),
            ("p", "Een tekst kan als doel hebben: <strong>informeren</strong>, <strong>overtuigen</strong> "
                  "of <strong>aanzetten tot iets</strong>."),
            ("p", "Lees: <em>Students must register before 1 October.</em> Dat is bedoeld <strong>voor "
                  "studenten</strong>. En <strong>een tekst voor jonge kinderen gebruikt kortere zinnen en "
                  "gewonere woorden dan een tekst voor volwassenen</strong>."),
            ("p", "<strong>De toon van een tekst kan je horen aan de woordkeuze.</strong>"),
            ("p", tabel(["zin", "toon"],
                        [["Hey, fancy a coffee later?", "informeel"],
                         ["We regret to inform you that your application was unsuccessful.",
                          "formeel, en: je bent niet gekozen"],
                         ["Shocking! The council has wasted millions.", "verontwaardigd"]])),
        ]),
        dict(kop="Voorzichtig en retorisch", blokken=[
            ("p", "Woorden die een bewering voorzichtiger maken: <strong>may</strong>, "
                  "<strong>possibly</strong> en <strong>it seems</strong>. Een schrijver die ze gebruikt, "
                  "laat zich een uitweg."),
            ("p", "<strong>Bij <em>It is said that…</em> weet je juist níét wie het zegt.</strong> Die "
                  "constructie verbergt de bron, en dat is op zich al een reden om voorzichtig te zijn."),
            ("p", "Lees: <em>Some claim that screens harm children. However, the evidence is thin.</em> De "
                  "schrijver <strong>nuanceert wat anderen zeggen</strong>."),
            ("p", "Lees: <em>Do you really think that is fair?</em> Die vraag is <strong>retorisch: ze wil "
                  "geen antwoord</strong>, ze wil je overtuigen."),
            ("p", "Lees: <em>Readers are advised to check the small print.</em> Die zin <strong>geeft de "
                  "lezer een raad</strong>."),
        ]),
        spreken("lees één Engelstalig opiniestuk en zeg daarna in het Engels, hardop, in drie zinnen "
                "wat de schrijver vindt en of je het ermee eens bent."),
    ])


# ───────────────────────── 3. Woordvelden: wonen, eten en vrije tijd
zet("woordvelden-wonen-eten-en-vrije-tijd",
    titel="Woordvelden: wonen, eten en vrije tijd",
    onder="Huren en samenwonen, het huishouden, een restaurant in Engeland, en de taal van sport en vrije tijd.",
    secties=[
        dict(kop="Huren en wonen", blokken=[
            ("p", tabel(["Engels", "Nederlands"],
                        [["a landlord", "de eigenaar van een huurwoning, een man"],
                         ["a tenant", "iemand die een woning huurt"],
                         ["a lodger", "iemand die bij iemand een kamer huurt"],
                         ["a flatmate", "iemand met wie je samenwoont"],
                         ["a neighbour", "een buur"]])),
            ("p", "Let op het verschil tussen <strong>a tenant</strong> en <strong>a lodger</strong>: een "
                  "tenant huurt een hele woning, een lodger huurt een kamer in het huis van iemand anders, "
                  "die er zelf ook woont."),
            ("p", "Wat een woning je kost: <strong>the rent</strong>, <strong>the bills</strong> en "
                  "<strong>the deposit</strong>. <em>The rent is due on the first of the month</em> "
                  "betekent <strong>de huur moet de eerste betaald zijn</strong>. <em>The flat is fully "
                  "furnished</em> betekent <strong>het appartement is volledig gemeubeld</strong>."),
            ("p", "Soorten woningen: <strong>a ground floor</strong>, <strong>a semi-detached house</strong> "
                  "en <strong>a terraced house</strong>. Een <strong>semi-detached house</strong> is "
                  "<strong>een halfopen bebouwing</strong>: twee huizen aan elkaar. Een terraced house is "
                  "een rijwoning."),
            ("kader", "<strong>In het Brits Engels is <em>the first floor</em> niet de gelijkvloerse "
                      "verdieping.</strong> De gelijkvloers is <em>the ground floor</em>, en <em>the first "
                      "floor</em> is de verdieping daarboven, bij ons de eerste. Een Amerikaan telt wél "
                      "zoals een lift bij ons: first floor is daar de begane grond."),
            ("p", "<em>To move house</em> betekent <strong>van woning veranderen</strong>, en <em>we live "
                  "within walking distance of the station</em> betekent <strong>het station is te voet "
                  "bereikbaar</strong>."),
            ("p", "<strong><em>A cosy room</em> is geen kleine kamer met weinig licht</strong>, maar een "
                  "gezellige, behaaglijke kamer. Het is een lofbetuiging, geen klacht."),
        ]),
        dict(kop="Het huishouden", blokken=[
            ("p", "Een <strong>chore</strong> is <strong>een klusje in het huishouden</strong>. De ruimte "
                  "waar je kookt, is de <strong>kitchen</strong>."),
            ("p", tabel(["Engels", "wat je doet"],
                        [["to do the washing-up", "de vaat doen"],
                         ["to load the dishwasher", "de vaatwasser vullen"],
                         ["to do the hoovering", "stofzuigen"],
                         ["to do the laundry", "de was doen"]])),
            ("p", "<em>Hoover</em> is in Groot-Brittannië een merknaam die het gewone woord geworden is, "
                  "zoals wij frigo zeggen."),
        ]),
        dict(kop="Samenleven met anderen", blokken=[
            ("p", tabel(["uitdrukking", "betekenis"],
                        [["to get on well with someone", "goed opschieten met iemand"],
                         ["to fall out with someone", "ruzie krijgen met iemand"],
                         ["to keep in touch", "contact houden"]])),
        ]),
        dict(kop="Eten en een restaurant", blokken=[
            ("p", "Een <strong>meal</strong> is een maaltijd; een <strong>dish</strong> is een gerecht, en "
                  "ook het bord waar het op ligt. Een <strong>starter</strong> is <strong>een "
                  "voorgerecht</strong>, en een <strong>takeaway</strong> is <strong>eten dat je "
                  "meeneemt</strong>."),
            ("p", tabel(["Engels", "Nederlands"],
                        [["the steak is well done", "goed doorbakken"],
                         ["chips", "frieten, in het Brits Engels"],
                         ["crisps", "chips uit een zakje, in het Brits Engels"],
                         ["I am allergic to nuts", "ik ben allergisch aan noten"],
                         ["to have a sweet tooth", "graag zoet eten"]])),
            ("p", "<strong><em>Chips</em> betekent in het Brits Engels inderdaad frieten.</strong> Vraag je "
                  "in Londen om chips, dan krijg je een bord frieten; wil je het zakje, vraag dan "
                  "<em>crisps</em>."),
            ("p", "Onder de dranken staan <strong>still water</strong>, <strong>sparkling water</strong> en "
                  "<strong>squash</strong>. Still is plat, sparkling is bruisend, en squash is een siroop "
                  "die je met water aanlengt."),
            ("p", "Zinnen die je in een restaurant gebruikt: <strong>Could we have the bill, "
                  "please?</strong>, <strong>I would like to book a table.</strong> en <strong>Is service "
                  "included?</strong>"),
        ]),
        dict(kop="Sport en vrije tijd", blokken=[
            ("p", tabel(["Engels", "Nederlands"],
                        [["a draw", "een gelijkspel"],
                         ["they beat us two nil", "ze wonnen met twee nul"],
                         ["a team of a side", "een ploeg"],
                         ["a referee", "de scheidsrechter"],
                         ["a fan", "een supporter"],
                         ["the match was called off", "de wedstrijd ging niet door"]])),
            ("p", "<em>Nil</em> is nul in een uitslag; <em>zero</em> gebruik je daar niet. En let op "
                  "<em>to beat</em>: <em>they beat us</em> betekent dat zíj wonnen."),
            ("p", "<strong><em>To practise a sport</em> betekent niet dat je ermee gestopt bent</strong>, "
                  "integendeel: het betekent dat je die sport beoefent. Een hobby <em>you take up</em> is "
                  "<strong>een hobby waarmee je begint</strong>."),
            ("p", "Werkwoorden die bij vrije tijd horen: <strong>to hang out with friends</strong>, "
                  "<strong>to go for a walk</strong> en <strong>to work out at the gym</strong>."),
            ("p", "<strong>Een <em>fortnight</em> zijn geen vier weken maar twee</strong>: het woord komt "
                  "van <em>fourteen nights</em>, veertien nachten."),
        ]),
        spreken("bestel in gedachten een maaltijd in het Engels, van het reserveren tot de rekening, en "
                "zeg elke zin hardop."),
    ])


# ───────────────────────── 4. Woordvelden: gezondheid, natuur en duurzaamheid
zet("woordvelden-gezondheid-natuur-en-duurzaamheid",
    titel="Woordvelden: gezondheid, natuur en duurzaamheid",
    onder="Naar de dokter in Groot-Brittannië, geestelijke gezondheid, en de taal van natuur, klimaat en duurzaamheid.",
    secties=[
        dict(kop="Naar de dokter", blokken=[
            ("p", "Een <strong>GP</strong> is in Groot-Brittannië <strong>een huisarts</strong>, kort voor "
                  "<em>general practitioner</em>. <strong>The NHS</strong> is <strong>de Britse "
                  "gezondheidszorg</strong>, de National Health Service."),
            ("p", tabel(["Engels", "Nederlands"],
                        [["a check-up", "een nazicht"],
                         ["a referral", "een doorverwijzing naar een specialist"],
                         ["a repeat prescription", "een herhaalvoorschrift"],
                         ["a prescription", "het papier waarmee je medicijnen gaat halen"],
                         ["a treatment", "een behandeling"],
                         ["a side effect", "een bijwerking"]])),
            ("p", "Klachten waarmee je naar de dokter gaat: <strong>a sore throat</strong>, <strong>a "
                  "rash</strong> en <strong>shortness of breath</strong>. Een <strong>ache</strong> is een "
                  "doffe pijn die blijft duren, zoals in <em>headache</em> of <em>toothache</em>."),
            ("p", tabel(["zin", "betekenis"],
                        [["I am coming down with a cold.", "ik word verkouden"],
                         ["She is on medication.", "ze neemt medicijnen"],
                         ["To feel under the weather.", "zich niet goed voelen"],
                         ["He made a full recovery.", "hij is volledig genezen"],
                         ["To put on weight.", "bijkomen in gewicht"]])),
            ("kader", "<strong>In het Brits Engels zeg je <em>she is in hospital</em>, zonder het "
                      "lidwoord.</strong> Een Amerikaan zegt wel <em>in the hospital</em>. Hetzelfde geldt "
                      "voor <em>at school</em> en <em>at university</em>: zonder lidwoord als je er als "
                      "patiënt of leerling bent, met lidwoord als je er gewoon staat."),
        ]),
        dict(kop="Geestelijke gezondheid", blokken=[
            ("p", "Woorden die bij de geestelijke gezondheid horen: <strong>anxiety</strong>, "
                  "<strong>burnout</strong> en <strong>coping strategies</strong>."),
            ("p", "<strong><em>Mental health</em> betekent niet dat iemand een psychische ziekte "
                  "heeft.</strong> Het is gewoon de geestelijke gezondheid, zoals <em>physical health</em> "
                  "de lichamelijke is. Iedereen heeft mental health; de vraag is enkel hoe het ermee gaat."),
            ("p", "<em>To be under a lot of stress</em> betekent <strong>veel stress hebben</strong>. Een "
                  "<strong>carer</strong> is <strong>iemand die voor een ander zorgt</strong>, vaak "
                  "onbetaald, voor een ouder of een kind. <strong>Sleep</strong> is slaap, en <em>a "
                  "balanced diet</em> is <strong>een evenwichtige voeding</strong>."),
        ]),
        dict(kop="Natuur en dieren", blokken=[
            ("p", tabel(["Engels", "Nederlands"],
                        [["a species", "een soort"],
                         ["endangered", "bedreigd"],
                         ["a habitat", "het leefgebied van een dier of plant"],
                         ["wildlife", "de dieren in de vrije natuur"],
                         ["a cub", "een jong van een roofdier"],
                         ["crops", "gewassen op het land"]])),
            ("p", "<strong><em>Wildlife</em> betekent niet de dieren in een dierentuin</strong>, maar juist "
                  "de dieren die in het wild leven. En <strong>a hedgehog is geen vogel die in een heg "
                  "nestelt</strong>, al zou je dat aan het woord denken: het is een egel."),
        ]),
        dict(kop="Klimaat en natuurrampen", blokken=[
            ("p", "Natuurrampen: <strong>a flood</strong>, <strong>a drought</strong> en <strong>a "
                  "wildfire</strong>. Een <strong>drought</strong> is <strong>een droogte</strong>, en "
                  "<strong>a heatwave is een periode van ongewoon warm weer</strong>."),
            ("p", "<strong>Global warming</strong> is <strong>de opwarming van de aarde</strong>; "
                  "<strong>pollution</strong> is vervuiling; <strong>fossil fuels</strong> zijn "
                  "<strong>fossiele brandstoffen</strong>."),
        ]),
        dict(kop="Duurzaamheid", blokken=[
            ("p", "Woorden die bij duurzaamheid horen: <strong>renewable energy</strong>, <strong>carbon "
                  "footprint</strong> en <strong>waste separation</strong>."),
            ("p", tabel(["Engels", "Nederlands"],
                        [["renewable", "hernieuwbaar"],
                         ["single-use plastic", "plastic voor eenmalig gebruik"],
                         ["waste, rubbish, litter", "afval"],
                         ["to recycle", "afval opnieuw gebruiken als grondstof"],
                         ["to conserve water", "spaarzaam zijn met water"],
                         ["to go green", "milieuvriendelijker werken"]])),
            ("p", "De bronnen die <strong>renewable</strong> zijn: <strong>wind power</strong>, "
                  "<strong>solar power</strong> en <strong>hydropower</strong>. Let op het verschil tussen "
                  "<em>waste</em> (afval in het algemeen), <em>rubbish</em> (huisvuil) en <em>litter</em> "
                  "(zwerfvuil op straat)."),
        ]),
        spreken("kijk een Engelstalig nieuwsitem over het klimaat zonder ondertitels, en vat het daarna "
                "in het Engels samen in vijf zinnen."),
    ])
