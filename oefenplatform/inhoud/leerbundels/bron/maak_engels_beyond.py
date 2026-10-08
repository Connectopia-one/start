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


# ───────────────────────── 5. Woordvelden: school, werk, geld en verkeer
zet("woordvelden-school-werk-geld-en-verkeer",
    titel="Woordvelden: school, werk, geld en verkeer",
    onder="De Britse school en universiteit, solliciteren en werken, winkelen en bankieren, en de taal van het verkeer.",
    secties=[
        dict(kop="School", blokken=[
            ("p", tabel(["Engels", "Nederlands"],
                        [["a head teacher", "de directeur"],
                         ["a term", "een trimester"],
                         ["a pupil", "een leerling"],
                         ["a subject", "een vak"],
                         ["homework", "huiswerk, altijd enkelvoud"],
                         ["a degree", "een diploma van de universiteit"]])),
            ("p", "<strong>Homework</strong> bestaat enkel in het enkelvoud: je zegt nooit <em>homeworks</em>, "
                  "wel <em>a piece of homework</em>."),
            ("kader", "<strong>Een <em>public school</em> is in Groot-Brittannië geen gratis school van de "
                      "overheid.</strong> Het is juist een dure privéschool, zoals Eton en Harrow. De "
                      "gratis school van de overheid heet <em>a state school</em>. Dat is een van de "
                      "beruchtste valstrikken van het Brits Engels."),
            ("p", "<strong><em>A pupil</em> en <em>a student</em> zijn in het Brits Engels niet volledig "
                  "verwisselbaar.</strong> Een <em>pupil</em> zit op school, een <em>student</em> aan de "
                  "universiteit of hogeschool. In het Amerikaans Engels zegt men voor allebei "
                  "<em>student</em>."),
            ("p", tabel(["zin", "betekenis"],
                        [["to sit an exam", "een examen afleggen"],
                         ["I failed the test.", "ik ben niet geslaagd"],
                         ["to hand in an essay", "een taak inleveren"],
                         ["a deadline", "de uiterste datum"],
                         ["he is on a tight schedule", "hij heeft een vol programma"]])),
            ("p", "Aan een Engelse universiteit bestaan drie lesvormen: <strong>a lecture</strong> (een "
                  "hoorcollege), <strong>a seminar</strong> (een werkcollege in groep) en <strong>a "
                  "tutorial</strong> (met één of twee studenten bij een docent)."),
        ]),
        dict(kop="Werk zoeken en werken", blokken=[
            ("p", "Bij het zoeken van werk horen <strong>a job interview</strong>, <strong>a CV</strong> en "
                  "<strong>a cover letter</strong>. <strong><em>To apply for a job</em> betekent naar een "
                  "job solliciteren</strong>, en <strong>a reference</strong> is <strong>een aanbeveling "
                  "van een vorige baas</strong>."),
            ("p", tabel(["Engels", "Nederlands"],
                        [["a trainee", "een stagiair"],
                         ["a colleague", "iemand met wie je samenwerkt"],
                         ["a salary, a wage, pay", "loon"],
                         ["to work shifts", "in ploegen werken"],
                         ["she was made redundant", "ze werd ontslagen om economische redenen"]])),
            ("p", "<em>Made redundant</em> is geen ontslag om een fout: het bedrijf had de functie niet "
                  "meer nodig. Het Engels maakt dat onderscheid scherper dan wij."),
        ]),
        dict(kop="Winkelen en betalen", blokken=[
            ("p", tabel(["Engels", "Nederlands"],
                        [["a receipt", "een kasticket"],
                         ["a till", "de kassa"],
                         ["change", "wisselgeld"],
                         ["a refund", "geld dat je terugkrijgt"],
                         ["a discount of a reduction", "korting"],
                         ["a bargain", "een koopje"],
                         ["VAT", "de belasting op de toegevoegde waarde, onze btw"]])),
            ("p", "<em>The goods are out of stock</em> betekent <strong>de artikelen zijn niet "
                  "voorradig</strong>, en <em>prices have gone up</em> betekent <strong>de prijzen zijn "
                  "gestegen</strong>."),
        ]),
        dict(kop="Geld, sparen en lenen", blokken=[
            ("p", "Woorden over sparen en lenen: <strong>savings</strong>, <strong>interest</strong> en "
                  "<strong>debt</strong>. Een <strong>loan</strong> is het geld dat je van de bank krijgt "
                  "en terugbetaalt."),
            ("p", "<em>I am broke</em> betekent <strong>ik heb geen geld meer</strong>: blut, niet gebroken."),
            ("p", "<strong><em>To afford something</em> betekent niet dat je iets niet nodig hebt</strong>, "
                  "maar dat je het je kan veroorloven. <em>I can't afford it</em> is: ik heb er het geld "
                  "niet voor."),
        ]),
        dict(kop="Verkeer en reizen", blokken=[
            ("p", tabel(["Engels", "Nederlands"],
                        [["a commuter", "een pendelaar"],
                         ["a delay", "een vertraging"],
                         ["a single ticket", "een enkele rit"],
                         ["a return ticket", "een heen- en terugrit"],
                         ["a fare", "de prijs van een rit"],
                         ["a roundabout", "een rotonde"]])),
            ("p", "In het verkeer hoor je <strong>a traffic jam</strong>, <strong>a pedestrian "
                  "crossing</strong> en <strong>a speed limit</strong>."),
            ("p", "<strong><em>A pavement</em> is in het Brits Engels niet het wegdek voor de auto's</strong>, "
                  "maar de stoep. Een Amerikaan zegt daarvoor <em>sidewalk</em>, en noemt met "
                  "<em>pavement</em> juist wél het asfalt. Dat is een valstrik die in allebei de richtingen "
                  "werkt."),
            ("p", "<em>Mind the gap</em> in de Londense metro betekent <strong>let op de ruimte tussen "
                  "perron en trein</strong>. <em>The flight has been delayed by two hours</em> betekent "
                  "<strong>de vlucht is twee uur later</strong>."),
        ]),
        spreken("speel een sollicitatiegesprek in het Engels: iemand stelt je vijf vragen over je school "
                "en je vakantiewerk, en jij antwoordt in volle zinnen."),
    ])


# ───────────────────────── 6. Woordvelden: kunst, literatuur, politiek en reizen
zet("woordvelden-kunst-literatuur-politiek-en-reizen",
    titel="Woordvelden: kunst, literatuur, politiek en reizen",
    onder="Over een boek praten, het museum, het Britse politieke bestel, de samenleving en op reis gaan.",
    secties=[
        dict(kop="Een boek en een verhaal", blokken=[
            ("p", tabel(["Engels", "Nederlands"],
                        [["a novel", "een roman"],
                         ["a poem", "een gedicht"],
                         ["a sonnet", "een gedicht van veertien regels"],
                         ["a protagonist", "de hoofdpersoon van een verhaal"],
                         ["a narrator", "de verteller"],
                         ["the plot", "de opeenvolging van wat er gebeurt"],
                         ["the setting", "waar en wanneer het verhaal speelt"],
                         ["a quotation", "een citaat"]])),
            ("p", "Let op het verschil tussen <strong>the protagonist</strong> en <strong>the "
                  "narrator</strong>: de hoofdpersoon is wie het verhaal overkomt, de verteller is wie het "
                  "vertelt, en dat hoeft niet dezelfde te zijn."),
            ("p", "De delen van een boek: <strong>a chapter</strong>, <strong>a preface</strong> en "
                  "<strong>an epilogue</strong>. Shakespeare schreef <strong>plays</strong>, "
                  "<strong>sonnets</strong> en <strong>poems</strong>."),
            ("p", "<em>The book is set in Victorian London</em> betekent <strong>het boek speelt in "
                  "Victoriaans Londen</strong>; <em>the novel was adapted for the screen</em> betekent "
                  "<strong>het boek werd verfilmd</strong>."),
            ("kader", "<strong>Het woord <em>work</em> is in het Engels niet altijd ontelbaar.</strong> Als "
                      "het arbeid betekent wel: <em>I have a lot of work</em>. Maar als het over de werken "
                      "van een schrijver of een kunstenaar gaat, is het telbaar: <em>the complete works of "
                      "Shakespeare</em>, <em>an early work</em>."),
        ]),
        dict(kop="Kunst en erfgoed", blokken=[
            ("p", "In een museum hoor je <strong>an exhibition</strong>, <strong>a guided tour</strong> en "
                  "<strong>an audio guide</strong>. <strong>Heritage</strong> is <strong>erfgoed</strong>, "
                  "<strong>a century</strong> is een eeuw, en <strong>the Middle Ages</strong> zijn "
                  "<strong>de middeleeuwen</strong>, altijd in het meervoud."),
            ("p", "<strong>A review is een stuk waarin iemand een boek of film beoordeelt.</strong> Een "
                  "<em>award-winning film</em> is <strong>een bekroonde film</strong>."),
            ("p", "<strong><em>A library</em> is in het Engels geen boekwinkel</strong>, maar een "
                  "bibliotheek. De boekwinkel is <em>a bookshop</em> of <em>a bookstore</em>. Dit is een "
                  "van de bekendste valse vrienden tussen het Nederlands en het Engels."),
        ]),
        dict(kop="Politiek in Groot-Brittannië", blokken=[
            ("p", tabel(["Engels", "Nederlands"],
                        [["the Prime Minister", "de eerste minister"],
                         ["an MP", "een parlementslid, Member of Parliament"],
                         ["an election", "een verkiezing"],
                         ["a ballot", "een stembiljet of stemronde"],
                         ["a turnout", "de opkomst"],
                         ["a candidate", "een kandidaat"],
                         ["a bill", "een wetsontwerp"]])),
            ("p", "<strong>Het Britse parlement bestaat uit het House of Commons en het House of "
                  "Lords.</strong> De Commons zijn verkozen, de Lords niet."),
            ("p", "Let op <strong>a bill</strong>: in het parlement is dat een wetsontwerp, in een "
                  "restaurant de rekening. Eén woord, twee werelden."),
        ]),
        dict(kop="De samenleving", blokken=[
            ("p", "Woorden over de samenleving: <strong>equality</strong>, <strong>discrimination</strong> "
                  "en <strong>integration</strong>. <strong>Poverty</strong> is armoede, <strong>a "
                  "charity</strong> is <strong>een goed doel</strong>, en <em>to raise awareness</em> "
                  "betekent <strong>mensen bewust maken</strong>."),
            ("p", "<em>To go on strike</em> betekent <strong>gaan staken</strong>."),
            ("p", "<strong><em>A refugee</em> is niet iemand die zijn land uit vrije keuze verlaten heeft "
                  "om te reizen.</strong> Een vluchteling vertrekt omdat hij moet: oorlog, vervolging, "
                  "geweld. Wie uit vrije keuze vertrekt, is <em>a migrant</em> of <em>a traveller</em>, en "
                  "dat verschil heeft in het Engels ook een juridische betekenis."),
        ]),
        dict(kop="Reizen", blokken=[
            ("p", "<em>To go abroad</em> betekent <strong>naar het buitenland gaan</strong>. Een "
                  "<strong>border</strong> of <strong>frontier</strong> is de grens tussen twee landen."),
            ("p", tabel(["Engels", "Nederlands"],
                        [["to book a room", "een kamer reserveren"],
                         ["the hotel is fully booked", "het hotel is volzet"],
                         ["a sightseeing tour", "een stadsbezoek"],
                         ["a bank holiday", "een wettelijke feestdag"]])),
            ("kader", "<strong><em>Great Britain</em> en <em>the United Kingdom</em> betekenen niet "
                      "hetzelfde.</strong> Great Britain is het eiland met <strong>England</strong>, "
                      "<strong>Scotland</strong> en <strong>Wales</strong>. Het United Kingdom is dat plus "
                      "Noord-Ierland. En <em>the British Isles</em> is nog ruimer: daar hoort ook Ierland "
                      "bij, dat een eigen land is."),
        ]),
        spreken("vertel in het Engels over een boek of een film die je echt goed vond, in vijf zinnen: "
                "waar het over gaat, wie de hoofdpersoon is en waarom het je bijbleef."),
    ])


# ───────────────────────── 7. Woordvelden: wetenschap, techniek en taal
zet("woordvelden-wetenschap-techniek-en-taal",
    titel="Woordvelden: wetenschap, techniek en taal",
    onder="Onderzoek en resultaten, computers en internetgevaren, en hoe je een onbekend Engels woord uit elkaar haalt.",
    secties=[
        dict(kop="Onderzoek", blokken=[
            ("p", tabel(["Engels", "Nederlands"],
                        [["research", "onderzoek"],
                         ["a survey", "een enquête"],
                         ["an experiment of a trial", "een proef"],
                         ["evidence", "bewijsmateriaal"],
                         ["a sample", "een steekproef of een staal"],
                         ["a hypothesis", "een hypothese"],
                         ["the findings of a study", "de resultaten"]])),
            ("p", "<strong><em>Evidence</em> is in het Engels ontelbaar: je zegt <em>a piece of "
                  "evidence</em>, niet <em>an evidence</em>.</strong> Hetzelfde geldt voor "
                  "<em>research</em>, <em>information</em> en <em>advice</em>."),
            ("p", "<strong><em>Data</em> wordt in wetenschappelijk Engels vaak als meervoud behandeld: "
                  "<em>the data show…</em></strong> Het enkelvoud is <em>datum</em>, al hoor je in "
                  "gewone taal ook <em>the data shows</em>."),
            ("p", "<em>To run a test</em> betekent <strong>een test uitvoeren</strong>, en <strong>a "
                  "breakthrough</strong> is <strong>een doorbraak</strong>."),
        ]),
        dict(kop="Techniek en computers", blokken=[
            ("p", "Een <strong>device</strong> is een toestel; een <strong>invention</strong> is een "
                  "uitvinding. Bij een computer horen <strong>a keyboard</strong>, <strong>a screen</strong> "
                  "en <strong>a hard drive</strong>. <strong>Software</strong> is de programmatuur, het "
                  "tegengestelde van hardware."),
            ("p", tabel(["Engels", "Nederlands"],
                        [["a password", "een wachtwoord"],
                         ["a backup", "een veiligheidskopie"],
                         ["the system crashed", "het systeem viel uit"],
                         ["artificial intelligence", "kunstmatige intelligentie"]])),
            ("p", "<strong><em>To download</em> betekent niet een bestand naar de server sturen</strong>, "
                  "maar het juist ophalen, naar beneden, naar jouw toestel. Omhoog sturen is <em>to "
                  "upload</em>."),
            ("p", "Gevaren op het internet: <strong>phishing</strong>, <strong>a scam</strong> en "
                  "<strong>malware</strong>."),
            ("p", "<strong><em>A chemist</em> is in Groot-Brittannië niet altijd iemand die scheikunde "
                  "studeerde.</strong> <em>Go to the chemist's</em> betekent naar de apotheek gaan, en de "
                  "apotheker zelf heet ook <em>a chemist</em>."),
        ]),
        dict(kop="Een woord uit elkaar halen", blokken=[
            ("p", "Een <strong>prefix</strong> is <strong>een voorvoegsel</strong>, een suffix een "
                  "achtervoegsel. Wie de vaste stukjes kent, raadt de helft van de onbekende woorden."),
            ("p", tabel(["deel", "wat het doet", "voorbeeld"],
                        [["un-", "maakt het woord ontkennend", "unhappy"],
                         ["-er", "de persoon die het doet", "teacher, van to teach"],
                         ["-less", "zonder", "careless"],
                         ["-ness", "maakt er een naamwoord van", "happiness"],
                         ["-able", "het kan gedaan worden", "readable"]])),
            ("p", "Het achtervoegsel dat van <em>to teach</em> de persoon maakt, is <strong>-er</strong>: "
                  "<em>teacher</em>. <strong>Het achtervoegsel <em>-less</em> maakt een woord ontkennend: "
                  "<em>careless</em> is zonder zorg.</strong>"),
            ("p", "<em>Unemployment</em> lees je in drie delen: <em>un-</em> (niet) plus <em>employ</em> "
                  "(tewerkstellen) plus <em>-ment</em> (een toestand). Samen: <strong>werkloosheid</strong>."),
            ("p", "Een <strong>context clue</strong> is <strong>een aanwijzing in de zin eromheen</strong>. "
                  "Lees: <em>to raise cattle</em>. Je weet dat <em>to raise</em> opheffen betekent, maar "
                  "met <em>cattle</em> ernaast wordt het <strong>vee houden</strong>. Het woord eromheen "
                  "beslist."),
        ]),
        dict(kop="Valse vrienden en vaste uitdrukkingen", blokken=[
            ("p", "Een <strong>false friend</strong> is <strong>een woord dat bedriegt met zijn "
                  "vorm</strong>: het lijkt op een Nederlands woord en betekent iets anders."),
            ("p", tabel(["Engels", "lijkt op", "betekent echt"],
                        [["actually", "actueel", "eigenlijk, in werkelijkheid"],
                         ["eventually", "eventueel", "uiteindelijk"],
                         ["library", "librairie, boekwinkel", "bibliotheek"]])),
            ("p", "Het woord dat <strong>uiteindelijk</strong> betekent en vaak met eventueel verward "
                  "wordt, is <strong>eventually</strong>. Eventueel is in het Engels <em>possibly</em> of "
                  "<em>if necessary</em>."),
            ("p", "Een <strong>idiom</strong> is <strong>een vaste uitdrukking</strong>, waarvan de "
                  "betekenis niet uit de losse woorden volgt. Een <strong>loanword</strong> is <strong>een "
                  "woord uit een andere taal</strong>, zoals <em>rucksack</em> of <em>café</em>."),
            ("p", "<strong>Een <em>synonym</em> is geen woord met de tegengestelde betekenis</strong>, maar "
                  "juist met dezelfde of een bijna gelijke betekenis. Het tegengestelde is een "
                  "<em>antonym</em>."),
        ]),
        dict(kop="Spelling en uitspraak", blokken=[
            ("p", "Het verschil tussen <em>its</em> en <em>it's</em>: <strong>its is bezittelijk, it's is "
                  "it is</strong>. De apostrof staat voor de weggelaten letter, niet voor het bezit. Dat is "
                  "omgekeerd aan wat je zou verwachten, en daarom gaat het zo vaak mis."),
            ("p", "<strong>Brits en Amerikaans Engels spellen sommige woorden anders: colour en "
                  "color.</strong> Ook <em>centre</em> en <em>center</em>, <em>travelled</em> en "
                  "<em>traveled</em>, <em>realise</em> en <em>realize</em>. Kies één van de twee en blijf "
                  "er in een tekst bij."),
            ("p", "<strong>In <em>know</em> en <em>write</em> spreek je niet elke letter uit.</strong> De k "
                  "en de w zijn stom: die stonden er vroeger wel, en de spelling is blijven staan terwijl "
                  "de uitspraak veranderde."),
            ("p", "Een <strong>sound</strong> is de klank waarmee je een woord uitspreekt. Manieren van "
                  "spreken: <strong>formal</strong>, <strong>informal</strong> en <strong>slang</strong>."),
            ("p", "<em>The word is spelt with a double l</em> betekent <strong>het woord heeft twee "
                  "l'en</strong>."),
        ]),
        spreken("luister naar een Engelstalige wetenschapspodcast en schrijf vijf nieuwe woorden op; "
                "gebruik ze daarna alle vijf hardop in een eigen zin."),
    ])


# ───────────────────────── 8. Naamwoorden, lidwoorden en hoeveelheden
zet("naamwoorden-lidwoorden-en-hoeveelheden",
    titel="Naamwoorden, lidwoorden en hoeveelheden",
    onder="Onregelmatige meervouden, telbaar en ontelbaar, de bezitsvorm, a of an of niets, en de getallen.",
    secties=[
        dict(kop="Het meervoud", blokken=[
            ("p", "De gewone regel is een <em>-s</em>, maar een handvol woorden doet het anders. Die moet "
                  "je kennen."),
            ("p", tabel(["enkelvoud", "meervoud"],
                        [["child", "children"],
                         ["woman", "women"],
                         ["foot", "feet"],
                         ["tooth", "teeth"],
                         ["mouse", "mice"],
                         ["person", "people"],
                         ["analysis", "analyses"],
                         ["sheep", "sheep"]])),
            ("p", "<strong>Het woord <em>sheep</em> krijgt in het meervoud geen s</strong>: <em>two "
                  "sheep</em>. Hetzelfde geldt voor <em>fish</em> en <em>deer</em>. En <strong>het meervoud "
                  "van <em>potato</em> is niet <em>potatos</em> maar <em>potatoes</em></strong>: woorden op "
                  "een medeklinker plus <em>-o</em> krijgen <em>-es</em>, net als <em>tomatoes</em> en "
                  "<em>heroes</em>."),
            ("p", "Woorden op <em>-f</em> of <em>-fe</em> maken daar vaak <em>-ves</em> van: <em>one knife, "
                  "two <strong>knives</strong></em>, ook <em>life — lives</em> en <em>wolf — wolves</em>."),
            ("p", "Sommige woorden staan altijd in het meervoud: <strong>scissors</strong>, "
                  "<strong>trousers</strong> en <strong>glasses</strong>. Wil je ze tellen, dan zeg je "
                  "<em>I bought two <strong>pairs</strong> of trousers</em>."),
        ]),
        dict(kop="Telbaar en ontelbaar", blokken=[
            ("p", "<strong><em>Information</em> is in het Engels ontelbaar: je zegt nooit "
                  "<em>informations</em>.</strong> Hetzelfde geldt voor <em>advice</em>, <em>news</em>, "
                  "<em>furniture</em>, <em>luggage</em> en <em>research</em>. Wil je er één van, dan zet je "
                  "er een maatwoord voor: <em>He gave me a good <strong>piece of advice</strong></em>."),
            ("p", "Een ontelbaar woord krijgt een werkwoord in het enkelvoud, ook als het op een s "
                  "eindigt."),
            ("p", tabel(["zin", "waarom"],
                        [["The news <strong>is</strong> good.", "news is ontelbaar, ondanks de s"],
                         ["My hair <strong>is</strong> too long.", "hair is in het Engels ontelbaar"],
                         ["The police <strong>have</strong> already arrived.",
                          "police is altijd meervoud, ook zonder s"]])),
        ]),
        dict(kop="De bezitsvorm", blokken=[
            ("p", "<em>The car of my brother</em> wordt <em>my <strong>brother's</strong> car</em>. Bij "
                  "mensen en dieren gebruik je die vorm met apostrof."),
            ("p", tabel(["vorm", "wanneer"],
                        [["the boy's bike", "één jongen"],
                         ["the boys' bikes", "meer jongens: de apostrof na de s"],
                         ["the children's room", "een onregelmatig meervoud zonder s: 's"]])),
            ("p", "<strong>Bij een meervoud dat al op een s eindigt, zet je de apostrof na die s: <em>the "
                  "teachers' room</em>.</strong>"),
            ("p", "Voor een ding gebruik je liever <em>of</em>: het dak van het huis is <strong>the roof of "
                  "the house</strong>, niet <em>the house's roof</em>."),
            ("p", "Een maat voor een zelfstandig naamwoord blijft enkelvoud en krijgt een streepje: "
                  "<em>a ten-minute walk</em> is <strong>een wandeling van tien minuten</strong>. Let op: "
                  "geen s aan <em>minute</em>."),
        ]),
        dict(kop="A, an, the of niets", blokken=[
            ("p", "<em>A</em> of <em>an</em> hangt af van de <strong>klank</strong>, niet van de letter."),
            ("p", tabel(["zin", "waarom"],
                        [["She is <strong>an</strong> engineer.", "een klinkerklank"],
                         ["She has <strong>an</strong> interesting job.", "een klinkerklank"],
                         ["I have been waiting for <strong>half</strong> an hour.",
                          "de h van hour is stom, dus an"],
                         ["<strong>A</strong> university.", "klinkt als joe-niversity, dus a"]])),
            ("p", "<strong>Voor <em>a university</em> staat <em>a</em> en niet <em>an</em>, hoewel het met "
                  "een u begint.</strong> Je hoort een j-klank, en dat is een medeklinker."),
            ("p", "<em>The</em> staat bij muziekinstrumenten: <em>He plays <strong>the</strong> "
                  "piano</em>. Maar in veel vaste uitdrukkingen staat juist niets."),
            ("p", tabel(["zonder lidwoord", "waarom"],
                        [["I like music.", "een algemeen begrip"],
                         ["She is at school.", "als leerling, niet als bezoeker"],
                         ["We had lunch at one.", "maaltijden staan zonder lidwoord"],
                         ["I go to school by bus.", "vervoermiddelen na by"]])),
            ("p", "<strong>Je zegt niet <em>the France</em> om over het land te spreken.</strong> Landen "
                  "staan zonder lidwoord, op een paar meervouden en samenstellingen na: <em>the "
                  "Netherlands</em>, <em>the United Kingdom</em>, <em>the United States</em>."),
        ]),
        dict(kop="Hoeveelheden", blokken=[
            ("p", tabel(["telbaar", "ontelbaar"],
                        [["many — too many cars", "much — how much money"],
                         ["few — few friends", "little — very little time"],
                         ["several", "a great deal of"],
                         ["a few", "a little"]])),
            ("p", "Bij een telbaar naamwoord horen <strong>many</strong>, <strong>few</strong> en "
                  "<strong>several</strong>. <em>How <strong>much</strong> money do you need?</em>, maar "
                  "<em>There are too <strong>many</strong> cars in the city.</em> En <em>I have very "
                  "<strong>little</strong> time left</em>, want tijd telt niet."),
            ("kader", "<strong>Er is wel degelijk een verschil tussen <em>few friends</em> en <em>a few "
                      "friends</em>.</strong> <em>Few friends</em> is somber: bijna geen. <em>A few "
                      "friends</em> is neutraal: enkele. Hetzelfde geldt voor <em>little</em> en <em>a "
                      "little</em>. Eén lidwoord keert de toon van de zin om."),
            ("p", "<em>Some</em> staat in bevestigende zinnen, <em>any</em> in vragen en ontkenningen: "
                  "<em>Is there <strong>any</strong> milk left?</em>"),
            ("p", "Uitdrukkingen die zeggen dat er veel van iets is: <strong>a lot of</strong>, "
                  "<strong>plenty of</strong> en <strong>a great deal of</strong>."),
        ]),
        dict(kop="Getallen en datums", blokken=[
            ("p", "<strong>Hundred, thousand en million blijven enkelvoud na een getal: <em>two hundred "
                  "people</em>.</strong> Pas zonder getal krijgen ze een s: <em>hundreds of people</em>."),
            ("p", "Je leest <em>1,500</em> als <strong>one thousand five hundred</strong>. Let op de "
                  "komma: in het Engels scheidt die de duizendtallen, waar wij een punt zetten."),
            ("p", tabel(["getal", "rangtelwoord"],
                        [["three", "third — the third person in the queue"],
                         ["twelve", "twelfth"],
                         ["twenty", "twentieth"]])),
            ("p", "De datum 3 mei zeg je in Brits Engels als <strong>the third of May</strong>. Een "
                  "Amerikaan zegt <em>May third</em>, en schrijft de datum ook in de andere volgorde."),
        ]),
        spreken("beschrijf in het Engels wat er op je bureau ligt, en let daarbij op elk lidwoord en elk "
                "meervoud dat je gebruikt."),
    ])


# ───────────────────────── 9. Voornaamwoorden en betrekkelijke bijzinnen
zet("voornaamwoorden-en-betrekkelijke-bijzinnen",
    titel="Voornaamwoorden en betrekkelijke bijzinnen",
    onder="Onderwerp en voorwerp, bezit, wederkerende en onbepaalde voornaamwoorden, en de betrekkelijke bijzin met en zonder komma's.",
    secties=[
        dict(kop="Onderwerp of voorwerp", blokken=[
            ("p", tabel(["onderwerp", "voorwerp"],
                        [["I", "me"], ["you", "you"], ["he", "him"], ["she", "her"],
                         ["it", "it"], ["we", "us"], ["they", "them"]])),
            ("p", "<em><strong>She</strong> gave the book to me</em>: vooraan staat de onderwerpsvorm. "
                  "<em>My parents sent <strong>us</strong> a card</em>: na het werkwoord de voorwerpsvorm."),
            ("p", "Na een voorzetsel staat altijd de voorwerpsvorm: <em>Between you and "
                  "<strong>me</strong>, I think he is wrong.</em> <em>Between you and I</em> hoor je vaak, "
                  "maar het is fout."),
            ("p", "<strong>In het Engels gebruik je <em>they</em> ook voor één persoon van wie je het "
                  "geslacht niet zegt.</strong> <em>Someone left their coat.</em> Dat is geen slordigheid: "
                  "het staat al eeuwen in het Engels en het is vandaag de gewone vorm."),
        ]),
        dict(kop="Bezit", blokken=[
            ("p", tabel(["voor een naamwoord", "alleenstaand"],
                        [["my", "mine"], ["your", "yours"], ["his", "his"], ["her", "hers"],
                         ["its", "—"], ["our", "ours"], ["their", "theirs"]])),
            ("p", "De alleenstaande vormen zijn <strong>mine</strong>, <strong>yours</strong> en "
                  "<strong>theirs</strong>: ze staan zonder naamwoord erachter. <em>This bike is not mine, "
                  "it is <strong>his</strong></em>, en <em>Is this bag <strong>yours</strong>?</em>"),
            ("p", "<strong>Je schrijft het bezittelijke <em>its</em> zonder apostrof.</strong> Geen enkele "
                  "alleenstaande bezitsvorm krijgt er een: niet <em>your's</em>, niet <em>her's</em>, niet "
                  "<em>their's</em>."),
            ("kader", "<strong><em>There</em>, <em>their</em> en <em>they're</em> betekenen niet hetzelfde.</strong> "
                      "<em>There</em> is daar, <em>their</em> is hun, <em>they're</em> is <em>they are</em>. "
                      "Ze klinken gelijk, en dat is precies waarom ze zo vaak door elkaar gaan."),
        ]),
        dict(kop="Wederkerende voornaamwoorden", blokken=[
            ("p", tabel(["persoon", "vorm"],
                        [["I", "myself"], ["you (één)", "yourself"], ["he", "himself"],
                         ["she", "herself"], ["we", "ourselves"], ["you (meer)", "yourselves"],
                         ["they", "themselves"]])),
            ("p", "<em>He hurt <strong>himself</strong> while cooking.</em> <em>We enjoyed "
                  "<strong>ourselves</strong> at the party.</em> <em>They built the house "
                  "<strong>themselves</strong>.</em>"),
            ("p", "<em>I did it myself</em> betekent <strong>ik deed het zelf</strong>, zonder hulp. "
                  "Dezelfde vorm dient dus voor twee dingen: de handeling keert terug op de persoon, of je "
                  "legt er nadruk mee."),
        ]),
        dict(kop="Onbepaalde voornaamwoorden", blokken=[
            ("p", "Onbepaalde voornaamwoorden zijn <strong>somebody</strong>, <strong>nothing</strong>, "
                  "<strong>everyone</strong>, en al hun broers en zussen op <em>-body</em>, <em>-one</em>, "
                  "<em>-thing</em> en <em>-where</em>."),
            ("p", "<strong>Ze krijgen altijd een werkwoord in het enkelvoud</strong>, ook al klinken ze "
                  "naar veel mensen: <strong>nobody</strong>, <strong>everything</strong> en "
                  "<strong>somebody</strong> doen dat allemaal. Dus <strong><em>everybody are here</em> is "
                  "fout</strong>: het is <em>everybody <strong>is</strong> here</em>."),
        ]),
        dict(kop="This, that, these, those", blokken=[
            ("p", "<strong>Het verschil tussen <em>this</em> en <em>that</em> is afstand: this is dichtbij, "
                  "that is verder weg.</strong> In het meervoud: <em>these</em> en <em>those</em>."),
            ("p", tabel(["", "dichtbij", "verder weg"],
                        [["enkelvoud", "this", "that"], ["meervoud", "these", "those"]])),
            ("p", "<em><strong>These</strong> books on the shelf are mine.</em> <em>I like this shirt, but "
                  "I prefer <strong>that</strong> one over there.</em>"),
            ("p", "In <em>The results arrived. They were better than expected</em> verwijst <em>they</em> "
                  "<strong>naar de resultaten</strong>."),
        ]),
        dict(kop="Vraagwoorden", blokken=[
            ("p", "De vraagwoorden die het Engels kent: <strong>whose</strong>, <strong>whom</strong> en "
                  "<strong>which</strong>, naast who, what, where, when, why en how."),
            ("p", tabel(["vraagwoord", "waarnaar het vraagt"],
                        [["Who is at the door?", "naar een persoon, als onderwerp"],
                         ["Whose coat is this?", "naar de bezitter"],
                         ["Which of these two do you prefer?", "naar een keuze uit een beperkt aantal"],
                         ["What did she ask?", "naar een zaak, uit een open veld"]])),
            ("p", "<strong><em>Who's</em> betekent <em>who is</em> of <em>who has</em>, en <em>whose</em> "
                  "betekent van wie.</strong> Weer dezelfde regel als bij <em>its</em>: de apostrof staat "
                  "voor een weggelaten letter, nooit voor bezit."),
            ("p", "<em>She asked me <strong>what</strong> I wanted.</em> In zo'n indirecte vraag blijft het "
                  "vraagwoord staan, maar de woordvolgorde wordt die van een gewone zin."),
        ]),
        dict(kop="De betrekkelijke bijzin", blokken=[
            ("p", tabel(["woord", "waarvoor"],
                        [["who", "voor personen: the man who lives next door"],
                         ["which", "voor zaken: the book which I bought"],
                         ["that", "voor allebei, in een beperkende bijzin"],
                         ["whose", "bezit: the woman whose son won the prize"],
                         ["whom", "voor personen, als voorwerp: the people whom I work with"]])),
            ("p", "<strong><em>Who</em> en <em>which</em> kunnen niet door elkaar gebruikt worden</strong>: "
                  "who is voor mensen, which voor dingen. <em>That</em> kan voor allebei."),
            ("p", "De fiche noemt ook <strong>when</strong>, <strong>where</strong> en <strong>why</strong>. "
                  "<strong>In <em>the day when we met</em> verwijst <em>when</em> naar een tijdstip.</strong> "
                  "<em>This is the town <strong>where</strong> I grew up</em>, en <em>The reason "
                  "<strong>why</strong> he left is unclear</em>."),
            ("p", "Deze drie zinnen zijn alle drie juist: <strong>The book that I read was good.</strong>, "
                  "<strong>The book which I read was good.</strong> en <strong>The book I read was "
                  "good.</strong> <strong>Het betrekkelijke woord mag weggelaten worden</strong> wanneer "
                  "het het voorwerp van de bijzin is, zoals in <em>The film I saw was long.</em> Is het "
                  "het onderwerp, dan moet het blijven staan: <em>The man <strong>who</strong> lives next "
                  "door</em> kan niet zonder."),
            ("p", "Ook juist gebouwd: <em>The man <strong>that</strong> I met was kind.</em>"),
        ]),
        dict(kop="Met of zonder komma's", blokken=[
            ("kader", "<strong>My brother, who lives in Spain, called</strong> tegenover <strong>My brother "
                      "who lives in Spain called</strong>. Met komma's heb ik <strong>één</strong> broer, "
                      "en dat hij in Spanje woont is extra informatie. Zonder komma's heb ik er "
                      "meerdere, en zeg ik welke van hen belde. Twee komma's veranderen hoeveel broers ik "
                      "heb."),
            ("p", "<strong>In een uitbreidende bijzin tussen komma's mag je <em>that</em> niet "
                  "gebruiken.</strong> Daar staat who of which: <em>My car, <strong>which</strong> is ten "
                  "years old, still runs.</em>"),
        ]),
        spreken("beschrijf in het Engels drie mensen uit je omgeving, elk in één zin met een "
                "betrekkelijke bijzin erin."),
    ])


# ───────────────────────── 10. Bijvoeglijke naamwoorden, bijwoorden en voorzetsels
zet("bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels",
    titel="Bijvoeglijke naamwoorden, bijwoorden en voorzetsels",
    onder="De trappen van vergelijking, het verschil tussen een bijvoeglijk naamwoord en een bijwoord, en de voorzetsels die je uit het hoofd moet kennen.",
    secties=[
        dict(kop="Het bijvoeglijk naamwoord", blokken=[
            ("p", "Het bijvoeglijk naamwoord staat <strong>vóór</strong> het naamwoord: <em>She has a "
                  "<strong>red</strong> car.</em> Na <em>to be</em> staat het ook, en dan nog altijd als "
                  "bijvoeglijk naamwoord, niet als bijwoord: <em>The soup is <strong>cold</strong>.</em>"),
            ("p", "<strong>Een bijvoeglijk naamwoord krijgt in het Engels nooit een s in het "
                  "meervoud.</strong> Het is <em>two red cars</em>, niet <em>two reds cars</em>."),
            ("p", "Staan er twee bijvoeglijke naamwoorden, dan ligt hun volgorde vast: eerst de grootte, "
                  "dan de kleur. <em>I have two <strong>small black</strong> dogs.</em>"),
            ("kader", "<strong>Het verschil tussen <em>interested</em> en <em>interesting</em>: "
                      "interested is een gevoel, interesting een eigenschap.</strong> Jij bent "
                      "<em>interested</em>, het boek is <em>interesting</em>. <em>I am "
                      "<strong>interested</strong> in history.</em> Zeg je <em>I am interesting</em>, dan "
                      "zeg je dat jij boeiend bent om te zien. Hetzelfde paar bij bored en boring, tired "
                      "en tiring, excited en exciting."),
            ("p", "<em>A far-fetched story</em> is <strong>een ongeloofwaardig verhaal</strong>: letterlijk "
                  "van ver gehaald."),
        ]),
        dict(kop="De trappen van vergelijking", blokken=[
            ("p", "Korte woorden krijgen <em>-er</em> en <em>-est</em>, lange woorden <em>more</em> en "
                  "<em>most</em>."),
            ("p", tabel(["", "vergrotend", "overtreffend"],
                        [["big", "bigger", "the biggest"],
                         ["happy", "happier", "the happiest"],
                         ["easy", "easier", "the easiest"],
                         ["large", "larger", "the largest"],
                         ["careful", "more careful", "the most careful"],
                         ["useful", "more useful", "the most useful"],
                         ["interesting", "more interesting", "the most interesting"]])),
            ("p", "<strong>Bij een woord van één lettergreep op een klinker plus een consonant verdubbelt "
                  "die consonant: <em>big</em> wordt <em>bigger</em>.</strong> Een <em>-y</em> na een "
                  "medeklinker wordt <em>-i</em>: happy — happier."),
            ("p", "<em>This book is <strong>more interesting</strong> than the other one.</em> <em>She is "
                  "<strong>taller than</strong> her sister.</em> <em>This is by far the "
                  "<strong>longest</strong> day of the year.</em>"),
            ("p", "De onregelmatige rijtjes moet je kennen: <strong>good, better, best</strong>, "
                  "<strong>bad, worse, worst</strong> en <strong>far, further, furthest</strong>. "
                  "<strong>De vergrotende trap van <em>good</em> is <em>better</em>, en de overtreffende "
                  "trap is <em>best</em>.</strong> <em>This is the <strong>best</strong> film I have ever "
                  "seen.</em>"),
            ("p", "<strong><em>Elder</em> kan je niet zoals <em>older</em> met <em>than</em> "
                  "gebruiken.</strong> <em>He is elder than me</em> is fout; het is <em>older than "
                  "me</em>. <em>Elder</em> staat enkel voor een naamwoord: <em>my elder brother</em>."),
            ("p", "Gelijkheid zeg je met <strong>as … as</strong>: <em>He is not as fast "
                  "<strong>as</strong> his brother.</em> <em>Her work is as good <strong>as</strong> "
                  "mine.</em>"),
            ("p", "<em>The more you practise, the better you get</em> betekent <strong>hoe meer je oefent, "
                  "hoe beter je wordt</strong>. Twee keer <em>the</em> plus een vergrotende trap, net als "
                  "ons hoe … hoe."),
        ]),
        dict(kop="Het bijwoord", blokken=[
            ("p", "Een bijwoord zegt iets over het werkwoord, en krijgt meestal <em>-ly</em>: <em>She sings "
                  "<strong>beautifully</strong>.</em> Juist gevormd zijn <strong>slowly</strong>, "
                  "<strong>happily</strong> en <strong>carefully</strong>. <strong>Het bijwoord van "
                  "<em>easy</em> is <em>easily</em></strong>: de y wordt een i."),
            ("p", "Twee onregelmatigheden. Het bijwoord van <em>good</em> is <strong>well</strong>: <em>He "
                  "plays the piano <strong>well</strong>.</em> En een paar woorden zijn tegelijk "
                  "bijvoeglijk naamwoord en bijwoord, zonder <em>-ly</em>: <strong>fast</strong>, "
                  "<strong>hard</strong> en <strong>late</strong>."),
            ("kader", "<strong><em>Hard</em> en <em>hardly</em> betekenen niet hetzelfde.</strong> "
                      "<em>Hard</em> is hard of ijverig, <em>hardly</em> is nauwelijks. <em>I "
                      "<strong>hardly</strong> know her</em> betekent <strong>ik ken haar amper</strong>, "
                      "en niet dat je haar moeizaam kent. Ook <em>late</em> en <em>lately</em> (de laatste "
                      "tijd) zijn zo'n paar."),
            ("p", "Een bijwoord in de vergrotende trap volgt dezelfde regel: <em>He drives <strong>more "
                  "carefully</strong> than I do.</em>"),
            ("p", "<strong>Een bijwoord van frequentie zoals <em>always</em> staat voor het werkwoord, "
                  "maar na <em>to be</em>.</strong> <em>He <strong>always</strong> arrives late</em>, maar "
                  "<em>He is <strong>always</strong> late</em>."),
            ("p", "Een bijwoord dat over de hele zin gaat, staat vooraan met een komma: "
                  "<em><strong>Luckily</strong>, nobody got hurt.</em>"),
        ]),
        dict(kop="Voorzetsels", blokken=[
            ("p", "Voorzetsels volgen geen regel: je leert ze per uitdrukking."),
            ("p", tabel(["vast voorzetsel", "voorbeeld"],
                        [["good at", "I am good at maths."],
                         ["married to", "She is married to a teacher."],
                         ["to wait for", "I am waiting for the bus."],
                         ["to depend on", "I depend on my parents."],
                         ["to arrive in of at", "to arrive in London, to arrive at the station"]])),
            ("p", "<strong>Je zegt niet <em>to arrive to London</em>.</strong> Bij een stad of een land is "
                  "het <em>to arrive <strong>in</strong></em>, bij een gebouw of een halte <em>to arrive "
                  "<strong>at</strong></em>."),
            ("p", tabel(["tijd", "voorzetsel"],
                        [["on Monday, on 3 May", "on: bij een dag of een datum"],
                         ["in May, in 2019, in the morning", "in: bij een maand, een jaar, een dagdeel"],
                         ["at six, at night", "at: bij een uur"],
                         ["since 2019", "since: vanaf een beginpunt"],
                         ["for two hours", "for: bij een tijdsduur"]])),
            ("p", "<em>The meeting is <strong>on</strong> Monday.</em> <em>He has been living here "
                  "<strong>since</strong> 2019.</em> <strong>Je zegt <em>at the weekend</em> in Brits "
                  "Engels en <em>on the weekend</em> in Amerikaans Engels.</strong>"),
            ("p", "Voorzetsels die zeggen waar iets ligt: <strong>under</strong>, <strong>next to</strong> "
                  "en <strong>between</strong>. En let op de hoek: <em>The shop is "
                  "<strong>on</strong> the corner.</em>"),
        ]),
        spreken("vergelijk hardop in het Engels drie dingen in je kamer, met telkens een andere trap van "
                "vergelijking, en let op elk voorzetsel dat je gebruikt."),
    ])


# ───────────────────────── 11. De tegenwoordige tijden en de present perfect
zet("de-tegenwoordige-tijden-en-de-present-perfect",
    titel="De tegenwoordige tijden en de present perfect",
    onder="Present simple tegenover continuous, de hulpwerkwoorden do en does, en wanneer je de present perfect gebruikt in plaats van de past simple.",
    secties=[
        dict(kop="Present simple", blokken=[
            ("p", "De present simple gebruik je voor gewoontes, feiten en dienstregelingen. De derde "
                  "persoon enkelvoud krijgt een <em>-s</em>."),
            ("p", tabel(["zin", "waarom simple"],
                        [["She goes to school every day.", "een gewoonte"],
                         ["He works in a bank.", "een blijvende toestand"],
                         ["Water boils at 100 degrees.", "een feit"],
                         ["The train leaves at six tomorrow.", "een dienstregeling"],
                         ["He always arrives late.", "een gewoonte"]])),
            ("p", "Woorden die bij de present simple horen: <strong>every day</strong>, "
                  "<strong>usually</strong> en <strong>on Mondays</strong>."),
            ("p", "<strong>Een werkwoord op een <em>-y</em> na een consonant krijgt <em>-ies</em> in de "
                  "derde persoon: <em>he studies</em>.</strong> Juist zijn dus <em>He always arrives "
                  "late.</em>, <em>She studies French.</em> en <em>They don't live here.</em>"),
        ]),
        dict(kop="Present continuous", blokken=[
            ("p", "De present continuous is <em>to be</em> plus <em>-ing</em>, en zegt dat iets nú bezig "
                  "is. <em>Look, it <strong>is raining</strong>.</em> <em>I <strong>am looking</strong> "
                  "for my keys at the moment.</em> <em>They <strong>are preparing</strong> dinner right "
                  "now.</em>"),
            ("p", "In de continuous staan ook <em>I am reading a novel.</em>, <em>She is working late.</em> "
                  "en <em>They are waiting outside.</em>"),
            ("p", "<strong>Werkwoorden als <em>to know</em>, <em>to want</em> en <em>to understand</em> "
                  "staan normaal niet in de continuous vorm.</strong> Dat zijn toestanden, geen "
                  "handelingen: je zegt <em>I know</em>, nooit <em>I am knowing</em>."),
            ("p", "<strong>In <em>I am seeing the doctor tomorrow</em> gaat het niet over iets dat nu "
                  "gebeurt.</strong> De continuous dient ook voor een <strong>afspraak in de "
                  "toekomst</strong> die al vastligt. Dat is een van de weinige plaatsen waar een "
                  "tegenwoordige tijd over morgen gaat."),
        ]),
        dict(kop="Do en does", blokken=[
            ("p", "In een vraag en een ontkenning komt <em>do</em> of <em>does</em> erbij, en het hoofdwerkwoord "
                  "verliest dan zijn <em>-s</em>."),
            ("p", tabel(["", "vraag", "ontkenning"],
                        [["I, you, we, they", "Do you speak French?", "They don't live here."],
                         ["he, she, it", "Does he speak French?", "He does not like coffee."]])),
            ("p", "Daarnaast dient <em>do</em> voor nadruk. In <em>I <strong>do</strong> like your new "
                  "coat</em> <strong>legt het nadruk op <em>like</em></strong>. Zo ook: <em>She "
                  "<strong>does</strong> know the answer</em>, ze weet het wél."),
        ]),
        dict(kop="There is en there are", blokken=[
            ("p", "<strong>Je zegt <em>there is</em> bij een enkelvoud en <em>there are</em> bij een "
                  "meervoud</strong>, niet omgekeerd."),
            ("p", tabel(["zin", "waarom"],
                        [["Is there any milk in the fridge?", "milk is ontelbaar, dus enkelvoud"],
                         ["There are too many cars.", "cars is meervoud"],
                         ["Were there many people at the meeting?",
                          "in de verleden tijd, bij een meervoud"]])),
        ]),
        dict(kop="De present perfect", blokken=[
            ("p", "De present perfect is <em>have</em> of <em>has</em> plus het voltooid deelwoord. Hij "
                  "legt een brug tussen vroeger en nu: wat er gebeurd is, telt nog altijd."),
            ("p", tabel(["zin", "waarom perfect"],
                        [["I have finished my homework.", "het gevolg telt nu"],
                         ["She has lived in London since 2020.", "en woont er nog"],
                         ["Have you ever been to Ireland?", "ooit, geen tijdstip genoemd"],
                         ["He has had three cups of coffee today.", "vandaag is nog niet voorbij"],
                         ["This is the first time I have been here.", "vaste uitdrukking"]])),
            ("p", "Voltooide deelwoorden die je moet kennen: <strong>written</strong>, "
                  "<strong>taken</strong>, <strong>bought</strong>, en ook <em>I have <strong>seen</strong> "
                  "that film twice</em>, <em>Have you <strong>eaten</strong> your dinner yet?</em>, <em>He "
                  "has <strong>worked</strong> in this school for ten years.</em>"),
            ("p", "Woorden die bij de present perfect passen: <strong>already</strong>, <strong>just</strong> "
                  "en <strong>yet</strong>. <strong>Tussen <em>have</em> en het deelwoord staan "
                  "<em>just</em>, <em>already</em> en <em>never</em></strong>; <em>yet</em> staat achteraan."),
            ("p", "<em>I have lost my keys</em> betekent <strong>ik heb ze nu nog niet terug</strong>. Zou "
                  "je ze intussen gevonden hebben, dan zeg je <em>I lost my keys</em>."),
            ("kader", "<strong>Bij een bepaald tijdstip in het verleden gebruik je de past simple, niet de "
                      "present perfect.</strong> Daarom is <em>I have finished my work yesterday</em> "
                      "fout: met <em>yesterday</em> hoort <em>I finished my work yesterday</em>. Dit is de "
                      "fout die Nederlandstaligen het vaakst maken, want bij ons kan het wel."),
            ("p", "<em>I <strong>haven't seen</strong> him since Monday.</em> <strong><em>Since</em> "
                  "gebruik je bij een beginpunt en <em>for</em> bij een tijdsduur</strong>: since Monday, "
                  "for two hours."),
            ("p", "<strong><em>He has gone to Paris</em> betekent niet dat hij er geweest is en alweer "
                  "terug.</strong> Hij is er nog. Wie terug is, zegt <em>He has <strong>been</strong> to "
                  "Paris</em>."),
        ]),
        dict(kop="De present perfect continuous", blokken=[
            ("p", "<em>Have been</em> plus <em>-ing</em> zegt dat iets al een tijd bezig is en nog altijd "
                  "duurt: <em>They <strong>have been waiting</strong> for two hours and are still "
                  "waiting.</em> <em>How long <strong>have</strong> you been learning English?</em>"),
            ("p", "<strong>Het verschil tussen <em>I have read the book</em> en <em>I have been reading the "
                  "book</em>: het eerste is af, het tweede nog niet.</strong> De gewone perfect kijkt naar "
                  "het resultaat, de continuous naar de bezigheid."),
        ]),
        spreken("vertel in het Engels wat je deze week al gedaan hebt en wat je nu aan het doen bent, en "
                "let erop welke tijd je waar nodig hebt."),
    ])


# ───────────────────────── 12. De verleden tijden
zet("de-verleden-tijden",
    titel="De verleden tijden",
    onder="Past simple, past continuous en past perfect: welke vorm hoort bij welk moment, en de onregelmatige werkwoorden.",
    secties=[
        dict(kop="De past simple", blokken=[
            ("p", "<strong>Een regelmatig werkwoord krijgt in de past simple <em>-ed</em>, bij elke "
                  "persoon dezelfde vorm.</strong> <em>They <strong>stayed</strong> at home all day.</em> "
                  "<em>The film <strong>lasted</strong> two hours.</em>"),
            ("p", "<strong>Bij een werkwoord op één klinker plus één consonant verdubbelt die consonant "
                  "voor <em>-ed</em>: <em>stop</em> wordt <em>stopped</em>.</strong>"),
            ("p", "De onregelmatige werkwoorden moet je gewoon kennen. Deze rijtjes van drie zijn juist: "
                  "<strong>see, saw, seen</strong>, <strong>speak, spoke, spoken</strong> en <strong>take, "
                  "took, taken</strong>."),
            ("p", tabel(["infinitief", "past simple", "voorbeeld"],
                        [["to go", "went", "We went to Spain last summer."],
                         ["to break", "broke", "He broke the window yesterday."],
                         ["to write", "wrote", "She wrote me a letter."],
                         ["to ride", "rode", "He rode his bike to school every day."],
                         ["to lose", "lost", "I lost my keys this morning."],
                         ["to have", "had", "We had a lot of fun at the fair."],
                         ["to buy, to catch, to teach", "bought, caught, taught", "alle drie op -ught"]])),
            ("p", "<strong>De verleden tijd van <em>to read</em> schrijf je niet <em>readed</em>.</strong> "
                  "Je schrijft <em>read</em>, net als de infinitief, maar je spreekt het uit als "
                  "<em>red</em>."),
            ("p", "Woorden die bij de past simple passen: <strong>yesterday</strong>, <strong>last "
                  "week</strong> en <strong>in 1995</strong>. Zodra er een bepaald moment in de zin staat, "
                  "is het de past simple."),
        ]),
        dict(kop="Vragen, ontkenningen en was of were", blokken=[
            ("p", "In een vraag en een ontkenning komt <em>did</em> erbij, en het hoofdwerkwoord gaat terug "
                  "naar de infinitief: <em><strong>Did</strong> you see the film last night?</em> en "
                  "<em>She <strong>did</strong> not come to the party.</em>"),
            ("p", "<strong>Je zegt niet <em>I didn't went to the party</em>.</strong> Het is <em>I "
                  "<strong>didn't go</strong></em>: <em>did</em> draagt de verleden tijd al, dus het "
                  "werkwoord hoeft hem niet nog eens."),
            ("p", "<em>To be</em> doet het alleen, zonder <em>did</em>: <em>She <strong>was</strong> born "
                  "in Hasselt.</em> <em>They <strong>were</strong> in the garden yesterday.</em>"),
            ("p", "<em>Used to</em> zegt dat iets vroeger zo was en nu niet meer: <em>He used "
                  "<strong>to live</strong> in Brussels.</em> Altijd met <em>to</em> en de infinitief."),
        ]),
        dict(kop="De past continuous", blokken=[
            ("p", "<em>Was</em> of <em>were</em> plus <em>-ing</em>: iets was bezig toen er iets anders "
                  "gebeurde."),
            ("p", "Je gebruikt de past continuous <strong>voor iets dat bezig was</strong>, <strong>voor "
                  "het decor van een verhaal</strong> en <strong>voor twee dingen die samen liepen</strong>."),
            ("p", tabel(["zin", "wat ze zegt"],
                        [["I was watching TV when the phone rang.", "het kijken was al bezig"],
                         ["While we were walking, it started to rain.", "het decor van wat volgt"],
                         ["She was sleeping when I came in.", "ze sliep al"],
                         ["What were you doing at eight o'clock?", "op dat ogenblik bezig"]])),
            ("p", "In de past continuous staan ook <em>They were waiting outside.</em>, <em>He was reading "
                  "a book.</em> en <em>We were having dinner.</em>"),
            ("kader", "<strong>Het verschil tussen <em>when I arrived, she cooked</em> en <em>when I "
                      "arrived, she was cooking</em>: in het tweede was ze al bezig.</strong> In het "
                      "eerste begon ze pas te koken toen jij binnenkwam. Eén <em>-ing</em> verandert de "
                      "hele volgorde van de gebeurtenissen."),
            ("p", "<strong><em>He was always losing his keys</em> klinkt in het Engels niet "
                  "neutraal.</strong> De continuous met <em>always</em> draagt ergernis of verwondering: "
                  "hij verloor ze alweer, altijd opnieuw."),
        ]),
        dict(kop="De past perfect", blokken=[
            ("p", "<strong>De past perfect gebruik je voor wat nog vroeger gebeurde dan iets anders in het "
                  "verleden.</strong> Hij is <em>had</em> plus het voltooid deelwoord, bij elke persoon "
                  "hetzelfde."),
            ("p", tabel(["zin", "welke stap eerst"],
                        [["When I arrived, the film had already started.", "de film startte eerst"],
                         ["She had finished her work before he called.", "het werk was eerst af"],
                         ["He said he had read the book already.", "het lezen kwam eerst"],
                         ["By the time we got there, everyone had gone home.", "weggaan kwam eerst"],
                         ["I didn't know she had been ill.", "het ziek zijn kwam eerst"]])),
            ("p", "In de past perfect staan ook <em>She had left before noon.</em>, <em>They had eaten "
                  "already.</em> en <em>I had never been there.</em> En: <em>They had never "
                  "<strong>seen</strong> such a storm.</em> <em>I <strong>had</strong> just left when you "
                  "called.</em>"),
            ("p", "<strong>Je mag de past perfect niet gebruiken zonder dat er een tweede gebeurtenis in "
                  "het verleden is.</strong> Hij bestaat alleen om twee momenten uit elkaar te houden; "
                  "staat er maar één, dan is het de past simple."),
            ("p", "<strong>In het Engels staat de past perfect in de bijzin van een onvervulde voorwaarde: "
                  "<em>if I had known</em>.</strong> Dat is de derde conditional: <em>If I had known, I "
                  "would have told you.</em>"),
            ("p", "Er bestaat ook een past perfect continuous: <em>They <strong>had been waiting</strong> "
                  "for an hour when the bus finally came.</em>"),
        ]),
        spreken("vertel in het Engels een klein voorval uit je eigen leven, en gebruik daarin bewust alle "
                "drie de verleden tijden."),
    ])


# ───────────────────────── 13. De toekomst, de modale hulpwerkwoorden en de gerund
zet("de-toekomst-de-modale-hulpwerkwoorden-en-de-gerund",
    titel="De toekomst, de modale hulpwerkwoorden en de gerund",
    onder="Will tegenover going to, wat elk modaal hulpwerkwoord zegt, de semi-auxiliaries, en wanneer er -ing en wanneer to komt.",
    secties=[
        dict(kop="Over de toekomst spreken", blokken=[
            ("p", "De fiche noemt drie manieren: de <strong>will future</strong>, de <strong>going to "
                  "future</strong> en de <strong>present simple</strong>."),
            ("p", tabel(["vorm", "wanneer", "voorbeeld"],
                        [["will", "een beslissing op het moment zelf, een voorspelling",
                          "The phone is ringing. I will answer it."],
                         ["going to", "een plan dat er al is, of een zichtbaar teken",
                          "Look at those clouds, it is going to rain."],
                         ["present continuous", "een vaste afspraak", "I am seeing the doctor tomorrow."],
                         ["present simple", "een uurrooster", "The train leaves at six."]])),
            ("p", "<em>We <strong>are</strong> going to move house next month.</em> Het hulpwerkwoord is "
                  "hier <em>are</em>: <em>going to</em> is een vorm van <em>to be</em>."),
            ("p", "<strong>Bij een vast uurrooster staat de present simple, ook voor iets dat nog moet "
                  "komen: <em>the train leaves at six</em>.</strong>"),
            ("p", "<em>They will have arrived by now</em> betekent <strong>ze zijn nu wel "
                  "aangekomen</strong>: een <em>will</em> die niets over de toekomst zegt maar een "
                  "vermoeden over het heden uitdrukt."),
        ]),
        dict(kop="De modale hulpwerkwoorden", blokken=[
            ("p", "Modale hulpwerkwoorden zijn onder meer <strong>can</strong>, <strong>may</strong> en "
                  "<strong>should</strong>. Ze volgen twee vaste regels: <strong>na een modaal "
                  "hulpwerkwoord staat het werkwoord zonder <em>to</em>: <em>I can swim</em></strong>, en "
                  "<strong>een modaal hulpwerkwoord krijgt geen s in de derde persoon</strong>: het is "
                  "<em>she can swim</em>, nooit <em>she cans swim</em>."),
            ("p", tabel(["zin", "wat ze zegt"],
                        [["You must wear a helmet.", "het is verplicht"],
                         ["You must not smoke here.", "het is verboden"],
                         ["You don't have to come.", "je hoeft niet te komen"],
                         ["You should see a doctor.", "het is een raad"],
                         ["She might come.", "ze komt misschien"],
                         ["He can't be at home.", "het kan niet dat hij thuis is"],
                         ["You could have told me.", "je had het mij kunnen zeggen"]])),
            ("kader", "<strong>Let op het verschil tussen <em>must not</em> en <em>don't have to</em>.</strong> "
                      "<em>You must not smoke here</em> is een verbod. <em>You don't have to come</em> is "
                      "juist het omgekeerde van een verplichting: het mág, maar het hoeft niet. Twee "
                      "ontkenningen die er hetzelfde uitzien en tegenovergesteld werken."),
            ("p", "<em>I would rather stay home</em> betekent <strong>ik blijf liever thuis</strong>, en "
                  "<em>he had better leave now</em> betekent <strong>hij kan beter nu vertrekken</strong>."),
            ("p", "Hoffelijke verzoeken: <strong>Would you mind closing the door?</strong>, <strong>Could "
                  "you close the door, please?</strong> en <strong>May I ask you to close the "
                  "door?</strong> Om toelating vraag je met <em><strong>May</strong> I open the "
                  "window?</em>, of met <em>Can</em> of <em>Could</em>."),
            ("p", "<strong><em>Shall</em> gebruik je in Brits Engels niet vooral in een mededeling met "
                  "<em>he</em> of <em>she</em>.</strong> Het staat bij <em>I</em> en <em>we</em>, en bijna "
                  "altijd in een vraag: <em>Shall we go?</em>, <em>Shall I help you?</em>"),
        ]),
        dict(kop="De semi-auxiliaries", blokken=[
            ("p", "Modale hulpwerkwoorden hebben geen verleden tijd en geen infinitief. Daarvoor bestaan de "
                  "<strong>semi-auxiliaries</strong>: <strong>to be able to</strong>, <strong>to have "
                  "to</strong> en <strong>to be allowed to</strong>."),
            ("p", tabel(["modaal", "semi-auxiliary", "verleden tijd"],
                        [["can", "to be able to", "I was able to finish it."],
                         ["must", "to have to", "Yesterday I had to work late."],
                         ["may", "to be allowed to", "We were allowed to leave early."]])),
            ("p", "<em>I am <strong>able</strong> to finish this today.</em> <em>We are not allowed "
                  "<strong>to use</strong> our phones.</em> En de verleden vorm van <em>have to</em> is "
                  "gewoon <em><strong>had</strong> to</em>."),
        ]),
        dict(kop="De imperatief", blokken=[
            ("p", "<strong>In de imperatief staat het werkwoord zonder <em>to</em> en zonder "
                  "onderwerp.</strong> <em><strong>Close</strong> the door, please.</em> Verbieden doe je "
                  "met <em>Don't</em>: <em>Don't close the door.</em>"),
        ]),
        dict(kop="Gerund of infinitief", blokken=[
            ("p", "Een <strong>gerund</strong> is de <em>-ing</em>-vorm die zich als een naamwoord "
                  "gedraagt. <strong>Hij kan wel degelijk het onderwerp van een zin zijn</strong>: "
                  "<em><strong>Swimming</strong> is good for your health.</em>"),
            ("p", tabel(["na", "welke vorm", "voorbeeld"],
                        [["to enjoy, to avoid, to mind, to finish", "een gerund", "I enjoy reading."],
                         ["to decide, to want, to hope", "to plus infinitief",
                          "She decided to take the job."],
                         ["elk voorzetsel", "een gerund", "He is good at cooking."],
                         ["to let, to make", "de infinitief zonder to", "They let him leave early."]])),
            ("p", "Na de werkwoorden <strong>to avoid</strong>, <strong>to mind</strong> en <strong>to "
                  "finish</strong> staat dus een gerund."),
            ("p", "<strong>Na een voorzetsel staat in het Engels altijd een gerund: <em>before "
                  "leaving</em>, <em>instead of waiting</em>.</strong> Dat geldt ook voor "
                  "<strong>without</strong>, <strong>before</strong> en <strong>for</strong>: <em>Thank "
                  "you for <strong>helping</strong> me.</em> <em>He went out without "
                  "<strong>saying</strong> goodbye.</em>"),
            ("p", "<strong>Na <em>to make</em> staat de infinitief zonder <em>to</em>.</strong> <em>She "
                  "made me <strong>wait</strong></em>, niet <em>she made me to wait</em>. Hetzelfde na "
                  "<em>to let</em>."),
            ("kader", "<strong>Het verschil tussen <em>I stopped smoking</em> en <em>I stopped to "
                      "smoke</em>: het eerste is gestopt met roken.</strong> Het tweede is juist blijven "
                      "staan om een sigaret op te steken. Bij een handvol werkwoorden, zoals <em>stop</em>, "
                      "<em>remember</em> en <em>forget</em>, verandert de betekenis volledig met de vorm."),
        ]),
        spreken("maak in het Engels drie hoffelijke verzoeken en drie plannen voor volgende week, en zeg "
                "ze hardop tot ze vlot klinken."),
    ])


# ───────────────────────── 14. Zinsbouw, indirecte rede en de passieve vorm
zet("zinsbouw-indirecte-rede-en-de-passieve-vorm",
    titel="Zinsbouw, indirecte rede en de passieve vorm",
    onder="De delen van een zin, de voegwoorden, de voorwaardelijke zinnen, iemands woorden weergeven en de passieve vorm.",
    secties=[
        dict(kop="De delen van een zin", blokken=[
            ("p", "Het <strong>subject</strong> is het deel van de zin dat zegt wie de handeling doet. In "
                  "<em>The old man next door walks every morning</em> is dat <strong>the old man next "
                  "door</strong>: het hele stuk, niet alleen <em>man</em>."),
            ("p", "In <em>She gave her brother a book</em> is <strong>a book</strong> het lijdend voorwerp: "
                  "dat is wat gegeven wordt. <em>Her brother</em> is het meewerkend voorwerp."),
            ("p", "In <em>They left the house early in the morning</em> is <strong>early in the "
                  "morning</strong> de bepaling van tijd."),
            ("p", "Er zijn verschillende soorten zinnen: <strong>een mededelende zin</strong>, <strong>een "
                  "vragende zin</strong> en <strong>een bevelende zin</strong>. <strong>Een uitroepende "
                  "zin begint in het Engels niet altijd met een werkwoord</strong>: hij begint vaak met "
                  "<em>What</em> of <em>How</em>, zoals in <em>What a day!</em>"),
            ("p", "<strong>Een samengestelde zin heeft meer dan één werkwoordelijk gezegde.</strong>"),
        ]),
        dict(kop="De woordorde", blokken=[
            ("p", "<strong>In het Engels staat het werkwoord in een gewone mededelende zin meteen na het "
                  "onderwerp.</strong> Anders dan bij ons schuift het nooit naar achteren."),
            ("p", "Een bijwoord van frequentie komt tussen het onderwerp en het werkwoord. Juist zijn: "
                  "<strong>I often go to the library.</strong>, <strong>She always arrives early.</strong> "
                  "en <strong>We usually eat at seven.</strong>"),
        ]),
        dict(kop="Het werkwoord bij het onderwerp", blokken=[
            ("p", tabel(["zin", "waarom"],
                        [["My brother and I are going to the cinema.", "twee personen, dus meervoud"],
                         ["Each of the students has a book.", "each is enkelvoud"],
                         ["Everyone in the class is ready.", "everyone is enkelvoud"],
                         ["The number of visitors has risen.", "the number is het onderwerp, enkelvoud"]])),
            ("p", "Laat je niet misleiden door wat er tussen het onderwerp en het werkwoord staat: in "
                  "<em>Each of the students</em> is <em>each</em> het onderwerp, niet <em>students</em>."),
        ]),
        dict(kop="Voegwoorden", blokken=[
            ("p", "De <strong>nevenschikkende</strong> voegwoorden zijn <strong>and</strong>, "
                  "<strong>but</strong> en <strong>or</strong>: ze zetten twee gelijkwaardige zinnen naast "
                  "elkaar."),
            ("p", tabel(["voegwoord", "verband", "voorbeeld"],
                        [["because", "een reden", "He stayed home because he was ill."],
                         ["although", "een toegeving", "Although it was raining, we went out."],
                         ["until", "tot wanneer", "I will wait until you arrive."],
                         ["unless", "tenzij", "We can go unless you prefer to stay."]])),
            ("p", "<strong><em>However</em> is geen voegwoord dat twee zinnen verbindt zoals "
                  "<em>and</em>.</strong> Het is een bijwoord: je zet er een punt of een kommapunt voor. "
                  "<em>It was raining. However, we went out.</em> Schrijf je <em>It was raining, however "
                  "we went out</em>, dan plak je twee zinnen aan elkaar."),
        ]),
        dict(kop="De voorwaardelijke zinnen", blokken=[
            ("p", tabel(["", "na if", "in de hoofdzin", "wanneer"],
                        [["zero conditional", "present simple", "present simple", "altijd waar"],
                         ["first conditional", "present simple", "will plus infinitief", "goed mogelijk"],
                         ["second conditional", "past simple", "would plus infinitief", "onwaarschijnlijk"],
                         ["third conditional", "past perfect", "would have plus deelwoord",
                          "niet meer te veranderen"]])),
            ("p", "<em>If you heat water, it <strong>boils</strong>.</em> <em>If it rains tomorrow, we "
                  "<strong>will stay</strong> at home.</em> <em>If you <strong>ask</strong> me, I will "
                  "help you.</em>"),
            ("p", "<strong>Na <em>if</em> staat in de eerste conditional geen <em>will</em>.</strong> Het "
                  "is <em>if it rains</em>, nooit <em>if it will rain</em>. Juist gebouwd zijn: <em>If it "
                  "snows, school closes.</em>, <em>If it snows, school will close.</em> en <em>School will "
                  "close if it snows.</em>"),
            ("p", "<strong>Het verschil tussen de zero en de first conditional: de zero is altijd waar, de "
                  "first is mogelijk.</strong> De zero beschrijft een natuurwet of een vaste regel, de "
                  "first één keer, morgen misschien."),
        ]),
        dict(kop="De indirecte rede", blokken=[
            ("p", "Bij de indirecte rede geef je iemands woorden weer zonder ze te citeren. Drie dingen "
                  "veranderen: <strong>de tijd schuift een stap terug</strong>, <strong>de voornaamwoorden "
                  "veranderen</strong> en <strong>de aanhalingstekens verdwijnen</strong>."),
            ("p", tabel(["directe rede", "indirecte rede"],
                        [["\"I am tired.\"", "He said he was tired."],
                         ["\"I will come tomorrow.\"", "She said she would come tomorrow."],
                         ["\"Close the door.\"", "He told me to close the door."],
                         ["\"Where is she?\"", "He asked where she was."]])),
            ("p", "<strong>In de indirecte rede houdt een vraag zijn omgekeerde woordorde niet.</strong> "
                  "<em>He asked where was she</em> is fout; het is <em>He asked where she "
                  "<strong>was</strong></em>. Het wordt weer een gewone zin."),
            ("p", "Een bevel wordt <em>to</em> plus de infinitief: <em>He told me <strong>to close</strong> "
                  "the door.</em>"),
        ]),
        dict(kop="De passieve vorm", blokken=[
            ("p", "De passieve vorm is <em>to be</em> plus het voltooid deelwoord. Het lijdend voorwerp "
                  "komt vooraan te staan."),
            ("p", tabel(["actief", "passief"],
                        [["They built the bridge in 1950.", "The bridge was built in 1950."],
                         ["Someone sent the letter yesterday.", "The letter was sent yesterday."],
                         ["They are repairing the road.", "The road is being repaired at the moment."]])),
            ("p", "<em>This house <strong>was</strong> built in 1930.</em> In de passieve vorm staan ook "
                  "<em>The results were published.</em>, <em>The car is being repaired.</em> en <em>The "
                  "letter has been sent.</em>"),
            ("p", "<strong>Niet elke zin met <em>to be</em> erin is een passieve zin.</strong> <em>She is "
                  "tired</em> is gewoon een mededeling; pas met een voltooid deelwoord erachter wordt het "
                  "passief."),
            ("p", "<strong>In een passieve zin hoef je de dader niet te noemen.</strong> Dat is precies "
                  "waarom <strong>krantenkoppen vaak in de passieve vorm staan: de nadruk valt op het "
                  "lijdend voorwerp</strong>. <em>Three arrested after fire</em> zegt wat er gebeurd is, "
                  "en laat open wie het deed."),
            ("p", "<em>He is said to be ill</em> betekent <strong>men zegt dat hij ziek is</strong>. Weer "
                  "een passieve vorm die de bron wegmoffelt, en weer een reden om te vragen wie dat dan "
                  "zegt."),
        ]),
        spreken("neem een kort Engels nieuwsbericht, zet drie zinnen ervan hardop om in de indirecte "
                "rede, en zeg daarna wat erin passief staat en waarom."),
    ])
