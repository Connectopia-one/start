# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij natuurwetenschappen, richting welzijnswetenschappen (🌍 Beyond).

Hoort bij maak_natuurwetenschappen_welzijn.py: één oefenbundel per thema van
het extra blok "Stofwisselingsfysiologie en secretie". Deel 1 en deel 2 van
een thema krijgen dezelfde pdf.

Net als bij de gewone natuurwetenschappen zijn de oefeningen met opzet ándere
opgaven dan die op het scherm: tabellen aanvullen, volgordes uitschrijven,
gevallen uitleggen. Wie hier iets bijschrijft, legt het eerst naast
../../beyond/bron/ww_*.py en naast de leerbundel van hetzelfde thema.

De sleutels eindigen op "-beyond-doorstroom", zodat /beheer/leerstof enkel bij
die categorie zoekt.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Natuurwetenschappen welzijnswetenschappen"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"

W = "120px"
WM = "185px"
WL = "250px"
ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een uitleg: schrijf niet alleen wát er gebeurt, maar ook waaróm, met de juiste begrippen.",
    "Bij een volgorde: schrijf elke stap op, ook de stappen die vanzelfsprekend lijken.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================ 1. Enzymen
OEFENBUNDELS["oefenbundel-enzymen-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Welzijnswetenschappen: Enzymen", onder=ONDER, hoe=HOE,
    reeksen=[
        dict(kop="Begrippen", opdracht="Schrijf het juiste begrip.", oefeningen=[
            ("rij", [("de stof die een enzym omzet", "substraat"),
                     ("de plaats op het enzym waar het substraat bindt", "actief centrum"),
                     ("de energie om een reactie te starten", "activeringsenergie")], None, WM),
            ("rij", [("het enzym verliest blijvend zijn vorm", "denaturatie"),
                     ("een stof die de werking van een enzym remt", "inhibitor"),
                     ("een metaalion dat een enzym helpt", "cofactor")], None, WM),
        ]),
        dict(kop="Welk enzym, welk substraat?", opdracht="Vul de tabel aan.", oefeningen=[
            ("tabel", ["Enzym", "Breekt af", "Waar het werkt"],
             [["lactase", None, None], ["pepsine", None, None], ["speekselamylase", None, None],
              ["lipase", None, None]],
             "Lactase: lactose of melksuiker, in de dunne darm. Pepsine: eiwitten, in de maag. "
             "Speekselamylase: zetmeel, in de mond. Lipase: vetten of lipiden, in de dunne darm "
             "(uit de alvleesklier).", W),
        ]),
        dict(kop="Waar of niet waar?", opdracht="Kruis aan.", oefeningen=[
            ("waar", "Na de reactie is een enzym opgebruikt en moet het lichaam een nieuw maken.", False),
            ("waar", "Een enzym verlaagt de activeringsenergie van een reactie.", True),
            ("waar", "Een enzym dat bij 90 °C gedenatureerd is, gaat weer werken als je het afkoelt.", False),
            ("waar", "Bij een lage temperatuur werkt een enzym traag omdat de moleculen trager bewegen.", True),
        ]),
        dict(kop="Grafieken lezen", opdracht="Leg in volledige zinnen uit.", oefeningen=[
            ("open", "Je meet de reactiesnelheid van een menselijk enzym bij 10, 20, 30, 37, 45 en 60 °C. "
                     "Beschrijf de vorm van de grafiek en verklaar het verloop links en rechts van de top.",
             "De snelheid stijgt geleidelijk tot rond 37 °C, het temperatuursoptimum, en valt daarna snel. "
             "Links bewegen de moleculen trager en botsen enzym en substraat minder vaak. Rechts "
             "denatureert het enzym: het actief centrum verliest zijn vorm.", 4),
            ("open", "Je voegt steeds meer substraat toe bij dezelfde hoeveelheid enzym. Eerst stijgt de "
                     "snelheid, daarna blijft ze gelijk. Waarom?",
             "Eerst zijn er vrije actieve centra, dus meer substraat geeft meer botsingen. Op het einde zijn "
             "alle actieve centra bezet: de verzadiging. Het enzym werkt dan aan zijn maximumsnelheid.", 3),
        ]),
        dict(kop="Een proef ontwerpen", opdracht="Lees en antwoord.", oefeningen=[
            ("open", "Je wil aantonen dat pepsine in een zure omgeving het best werkt. Welke drie buizen "
                     "zet je klaar, en wat houd je in alle buizen gelijk?",
             "Bijvoorbeeld een buis met pH 2, een met pH 7 en een met pH 9, elk met dezelfde hoeveelheid "
             "pepsine en eiwit (bv. eiwit van een gekookt ei). Gelijk houden: temperatuur (37 °C), "
             "hoeveelheden en tijd. Alleen de pH verschilt.", 4),
            ("kies", "Speekselamylase komt met het voedsel in de maag. Wat gebeurt er?",
             ["het werkt sneller door het zuur", "het stopt grotendeels", "het wordt pepsine"], 1),
        ]),
    ],
)

# ============================================================ 2. Spijsvertering
OEFENBUNDELS["oefenbundel-het-spijsverteringsstelsel-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Welzijnswetenschappen: Het spijsverteringsstelsel", onder=ONDER, hoe=HOE,
    reeksen=[
        dict(kop="De weg van het voedsel", opdracht="Schrijf de delen in de juiste volgorde.", oefeningen=[
            ("open", "Zet in volgorde: dikke darm, slokdarm, mondholte, twaalfvingerige darm, maag, "
                     "keelholte, endeldarm, nuchtere darm, kronkeldarm.",
             "mondholte, keelholte, slokdarm, maag, twaalfvingerige darm, nuchtere darm, kronkeldarm, "
             "dikke darm, endeldarm", 2),
            ("open", "Noem de vier lagen van de wand van het spijsverteringskanaal, van binnen naar buiten.",
             "slijmvlies of mucosa, bindweefsel, spierlaag, bindweefsel of steunweefsel", 2),
        ]),
        dict(kop="Wie maakt wat?", opdracht="Schrijf het orgaan of de cellen.", oefeningen=[
            ("rij", [("maakt gal", "lever"), ("slaat gal op", "galblaas"),
                     ("maakt zoutzuur", "pariëtale cellen")], None, WM),
            ("rij", [("geeft NaHCO₃ af", "alvleesklier"), ("maakt lactase", "dunne darm"),
                     ("maakt vitamine K", "darmflora")], None, WM),
        ]),
        dict(kop="Vertering in een tabel", opdracht="Vul de tabel aan.", oefeningen=[
            ("tabel", ["Voedingsstof", "Enzym(en)", "Eindproduct"],
             [["zetmeel", None, None], ["eiwitten", None, None], ["vetten", None, None],
              ["sacharose", None, None]],
             "Zetmeel: amylase en maltase, glucose. Eiwitten: pepsine, trypsine en peptidasen, "
             "aminozuren. Vetten: lipase (na emulgeren door gal), glycerol en vetzuren. Sacharose: "
             "sacharase, glucose en fructose.", W),
        ]),
        dict(kop="Waar of niet waar?", opdracht="Kruis aan.", oefeningen=[
            ("waar", "Gal bevat enzymen die vetten afbreken.", False),
            ("waar", "Glycerol en vetzuren komen via het lymfevat in het bloed.", True),
            ("waar", "De maagportier ligt tussen de slokdarm en de maag.", False),
            ("waar", "Osmose is een passieve vorm van transport.", True),
        ]),
        dict(kop="Uitleggen", opdracht="Leg in volledige zinnen uit.", oefeningen=[
            ("open", "Waarom maakt de maag pepsine eerst aan als het inactieve pepsinogeen?",
             "Zo verteert het enzym de cellen die het maken niet zelf. Pas in de maagholte zet het zoutzuur "
             "pepsinogeen om in actief pepsine.", 3),
            ("open", "Iemand met coeliakie heeft beschadigde darmvlokken. Waarom kan die persoon gewicht "
                     "verliezen, ook al eet hij genoeg?",
             "Darmvlokken en microvilli vergroten het opnameoppervlak. Zijn ze beschadigd, dan is het "
             "oppervlak veel kleiner en worden minder voedingsstoffen opgenomen.", 3),
            ("open", "Een rode bloedcel komt in zuiver water terecht. Wat gebeurt er en waarom?",
             "Zuiver water is hypotoon. Water stroomt door osmose de cel in, zodat ze opzwelt en kan "
             "barsten.", 3),
        ]),
    ],
)

# ============================================================ 3. Uitscheiding
OEFENBUNDELS["oefenbundel-het-uitscheidingsstelsel-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Welzijnswetenschappen: Het uitscheidingsstelsel", onder=ONDER, hoe=HOE,
    reeksen=[
        dict(kop="De weg van de urine", opdracht="Schrijf in de juiste volgorde.", oefeningen=[
            ("open", "Zet in volgorde: verzamelbuis, lus van Henle, kapsel van Bowman, tweede kronkelbuisje, "
                     "eerste kronkelbuisje, nierbekken, urineleider.",
             "kapsel van Bowman, eerste kronkelbuisje, lus van Henle, tweede kronkelbuisje, verzamelbuis, "
             "nierbekken, urineleider", 2),
            ("rij", [("van nier naar blaas", "urineleider"), ("van blaas naar buiten", "urinebuis"),
                     ("brengt bloed in de nier", "nierslagader")], None, WM),
        ]),
        dict(kop="Drie stappen in het nefron", opdracht="Vul de tabel aan.", oefeningen=[
            ("tabel", ["Stap", "Waar", "Wat gebeurt er"],
             [["filtratie", None, None], ["resorptie", None, None], ["secretie", None, None]],
             "Filtratie: van de glomerulus naar het kapsel van Bowman; water en kleine stoffen worden "
             "eruit geperst tot voorurine. Resorptie: in de kronkelbuisjes en de lus van Henle; nuttige "
             "stoffen zoals glucose gaan terug naar het bloed. Secretie: in de kronkelbuisjes; extra stoffen "
             "worden actief uit het bloed in het buisje gebracht.", WM),
        ]),
        dict(kop="Wat zit erin?", opdracht="Schrijf ja of nee: zit het normaal in de urine?", oefeningen=[
            ("rij", [("ureum", "ja"), ("glucose", "nee"), ("albumine", "nee")], None, W),
            ("rij", [("water", "ja"), ("rode bloedcellen", "nee"), ("zouten", "ja")], None, W),
        ]),
        dict(kop="Waar of niet waar?", opdracht="Kruis aan.", oefeningen=[
            ("waar", "ADH maakt de verzamelbuis beter doorlaatbaar voor water.", True),
            ("waar", "Alcohol stimuleert de afgifte van ADH.", False),
            ("waar", "De lus van Henle ligt volledig in de nierschors.", False),
            ("waar", "De externe kringspier van de blaas kan je bewust aansturen.", True),
        ]),
        dict(kop="Gevallen", opdracht="Leg in volledige zinnen uit.", oefeningen=[
            ("open", "Na een lange fietstocht op een warme dag heb je weinig gedronken. Je plast weinig en "
                     "donker. Beschrijf hoe je lichaam dat regelt: sensor, controlecentrum, hormoon en effector.",
             "Osmoreceptoren merken dat het bloed te geconcentreerd is. De hypothalamus laat de hypofyse meer "
             "ADH afgeven. In de nieren neemt de verzamelbuis meer water terug, zodat de urine weinig en "
             "geconcentreerd is. Daarnaast krijg je dorst.", 4),
            ("open", "Bij een urineonderzoek vindt men veel eiwit en wat bloed in de urine. Waar zit het "
                     "probleem waarschijnlijk, en waarom?",
             "In de nierfilter van de glomerulus. Rode bloedcellen en grote eiwitten zijn normaal te groot om "
             "erdoor te gaan; zitten ze in de urine, dan is de filter beschadigd.", 3),
            ("open", "Leg uit hoe hemodialyse het bloed zuivert en waarom de patiënt een shunt heeft.",
             "Het bloed stroomt door een kunstnier langs een semipermeabel membraan en geeft afvalstoffen "
             "zoals ureum af aan een spoelvloeistof. De shunt verbindt een slagader en een ader in de arm, "
             "zodat men vlot veel bloed kan afnemen.", 4),
        ]),
    ],
)

# ============================================================ 4. Bloed
OEFENBUNDELS["oefenbundel-het-bloed-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Welzijnswetenschappen: Het bloed", onder=ONDER, hoe=HOE,
    reeksen=[
        dict(kop="Bloedcellen", opdracht="Vul de tabel aan.", oefeningen=[
            ("tabel", ["Bloedcel", "Andere naam", "Taak"],
             [["rode bloedcel", None, None], ["witte bloedcel", None, None], ["bloedplaatje", None, None]],
             "Rode bloedcel: erytrocyt, vervoert zuurstof met hemoglobine. Witte bloedcel: leukocyt, afweer "
             "tegen ziekteverwekkers. Bloedplaatje: trombocyt, helpt bij de bloedstolling.", WM),
        ]),
        dict(kop="Welke witte bloedcel?", opdracht="Schrijf de soort.", oefeningen=[
            ("rij", [("wordt een plasmacel en maakt antilichamen", "B-lymfocyt"),
                     ("doodt cellen die met een virus besmet zijn", "T-lymfocyt"),
                     ("wordt in het weefsel een macrofaag", "monocyt")], None, WM),
            ("rij", [("talrijkst, ruimt als eerste bacteriën op", "neutrofiel"),
                     ("actief tegen wormen en bij allergie", "eosinofiel"),
                     ("maakt histamine vrij", "basofiel")], None, WM),
        ]),
        dict(kop="Bloedgroepen", opdracht="Vul in.", oefeningen=[
            ("tabel", ["Bloedgroep", "Antigenen op de rode bloedcel", "Antilichamen in het plasma"],
             [["A", None, None], ["B", None, None], ["AB", None, None], ["O", None, None]],
             "A: A-antigenen, anti-B. B: B-antigenen, anti-A. AB: A en B, geen antilichamen. O: geen "
             "antigenen, anti-A en anti-B.", W),
            ("kies", "Wie is de universele donor van rode bloedcellen?",
             ["AB-positief", "O-negatief", "A-negatief"], 1),
            ("open", "Waarom mag iemand met bloedgroep A geen bloed van groep B krijgen?",
             "Het anti-B in het plasma van de ontvanger doet de rode bloedcellen van de donor klonteren "
             "(agglutinatie), waarna ze kapotgaan.", 3),
        ]),
        dict(kop="Waar of niet waar?", opdracht="Kruis aan.", oefeningen=[
            ("waar", "Serum is plasma zonder stollingsfactoren.", True),
            ("waar", "Een rijpe rode bloedcel heeft een grote celkern.", False),
            ("waar", "Het meeste CO₂ wordt vervoerd als waterstofcarbonaat in het plasma.", True),
            ("waar", "Anti-D zit van nature in het bloed van iedereen die resusnegatief is.", False),
        ]),
        dict(kop="Uitleggen", opdracht="Leg in volledige zinnen uit.", oefeningen=[
            ("open", "Een wielrenner gaat drie weken op hoogtestage. Wat gebeurt er met zijn hematocriet en "
                     "waarom?",
             "In de ijle lucht is er minder zuurstof. De nieren maken meer EPO, dat het rode beenmerg meer "
             "rode bloedcellen laat maken. De hematocriet stijgt.", 3),
            ("open", "Schrijf de laatste stappen van de bloedstolling uit, van protrombine tot stolsel.",
             "Protrombine wordt trombine. Trombine zet het opgeloste fibrinogeen om in onoplosbare "
             "fibrinedraden. Die vormen een net waarin bloedcellen blijven hangen: het stolsel.", 3),
        ]),
    ],
)

# ============================================================ 5. Hart en bloedsomloop
OEFENBUNDELS["oefenbundel-het-hart-en-de-bloedsomloop-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Welzijnswetenschappen: Het hart en de bloedsomloop", onder=ONDER, hoe=HOE,
    reeksen=[
        dict(kop="De weg van het bloed", opdracht="Schrijf in de juiste volgorde.", oefeningen=[
            ("open", "Volg een rode bloedcel van de onderste holle ader tot in de aorta. Noem alle holtes, "
                     "kleppen en bloedvaten.",
             "onderste holle ader, rechterboezem, tricuspidalisklep, rechterkamer, pulmonalisklep, "
             "longslagader, longen, longaders, linkerboezem, mitralisklep, linkerkamer, aortaklep, aorta", 3),
            ("open", "Zet de prikkelgeleiding in volgorde: bundeltakken, AV-knoop, purkinjevezels, "
                     "sinusknoop, bundel van His.",
             "sinusknoop, AV-knoop, bundel van His, bundeltakken, purkinjevezels", 2),
        ]),
        dict(kop="Bloedvaten", opdracht="Schrijf zuurstofrijk of zuurstofarm.", oefeningen=[
            ("rij", [("aorta", "zuurstofrijk"), ("longslagader", "zuurstofarm"),
                     ("longaders", "zuurstofrijk")], None, W),
            ("rij", [("bovenste holle ader", "zuurstofarm"), ("kransslagader", "zuurstofrijk"),
                     ("leverpoortader", "zuurstofarm")], None, W),
        ]),
        dict(kop="Slagader of ader?", opdracht="Vul de tabel aan.", oefeningen=[
            ("tabel", ["Kenmerk", "Slagader", "Ader"],
             [["dikte van de wand", None, None], ["kleppen", None, None], ["bloeddruk", None, None]],
             "Slagader: dikke, gespierde wand, geen kleppen, hoge druk. Ader: dunnere wand, wel kleppen, "
             "lage druk.", W),
        ]),
        dict(kop="Waar of niet waar?", opdracht="Kruis aan.", oefeningen=[
            ("waar", "De rechterkamer heeft de dikste spierwand.", False),
            ("waar", "Het QRS-complex hoort bij de prikkeling van de kamers.", True),
            ("waar", "Tijdens de kamersystole zijn de atrioventriculaire kleppen open.", False),
            ("waar", "Een poortader ligt tussen twee haarvatennetwerken.", True),
        ]),
        dict(kop="Uitleggen", opdracht="Leg in volledige zinnen uit.", oefeningen=[
            ("open", "Waarom houdt de AV-knoop de prikkel even tegen?",
             "Zo lopen de boezems eerst leeg in de kamers voor de kamers samentrekken.", 2),
            ("open", "Noem drie dingen die het bloed in de aders van je benen terug naar het hart helpen.",
             "de veneuze kleppen, het samentrekken van de beenspieren rond de aders, de zuigwerking bij "
             "het inademen", 3),
            ("open", "Iemand krijgt een hartinfarct. Wat is meestal de oorzaak en waarom sterft er dan "
                     "hartspierweefsel af?",
             "Een kransslagader raakt verstopt. Het deel van de hartspier daarachter krijgt geen zuurstof en "
             "voedingsstoffen meer en sterft af.", 3),
        ]),
    ],
)

# ============================================================ 6. Bloeddruk en lymfe
OEFENBUNDELS["oefenbundel-de-bloeddruk-en-het-lymfestelsel-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Welzijnswetenschappen: De bloeddruk en het lymfestelsel", onder=ONDER, hoe=HOE,
    reeksen=[
        dict(kop="Bloeddruk lezen", opdracht="Antwoord kort.", oefeningen=[
            ("kort", "Een meting geeft 135/85 mmHg. Wat is de bovendruk?", "135 mmHg", "90px"),
            ("kort", "Vanaf welke waarde spreekt men van hypertensie?", "140/90 mmHg", "90px"),
            ("kies", "Waar is de bloeddruk het laagst?", ["in de aorta", "in de haarvaten", "in de holle aders"], 2),
        ]),
        dict(kop="De regeling", opdracht="Schrijf het juiste begrip.", oefeningen=[
            ("rij", [("meten de bloeddruk in aorta en halsslagader", "baroreceptoren"),
                     ("het controlecentrum in het verlengde merg", "cardiovasculair centrum"),
                     ("het vernauwen van een bloedvat", "vasoconstrictie")], None, WM),
            ("open", "Zet het renine-angiotensinesysteem in volgorde, van een te lage bloeddruk tot het effect.",
             "Te lage bloeddruk: de nieren maken renine. Renine zet angiotensinogeen om in angiotensine I. "
             "ACE zet dat om in angiotensine II. Dat vernauwt de bloedvaten en maakt aldosteron vrij, zodat "
             "de nieren meer zout en water terugnemen. De bloeddruk stijgt.", 4),
        ]),
        dict(kop="Waar of niet waar?", opdracht="Kruis aan.", oefeningen=[
            ("waar", "Het parasympatisch zenuwstelsel versnelt de hartslag tijdens het sporten.", False),
            ("waar", "Een negatief feedbacksysteem werkt een verandering tegen.", True),
            ("waar", "Het lymfestelsel heeft een eigen pomp, net als de bloedsomloop.", False),
            ("waar", "In de thymus rijpen de T-lymfocyten.", True),
        ]),
        dict(kop="Weefselvocht en lymfe", opdracht="Leg in volledige zinnen uit.", oefeningen=[
            ("open", "Leg uit hoe weefselvocht ontstaat aan het begin van een haarvat en hoe een deel "
                     "terugkomt aan het einde.",
             "Aan het begin perst de bloeddruk plasma uit het haarvat. Aan het einde is de bloeddruk gezakt "
             "en trekken de plasma-eiwitten water terug in het haarvat (osmotische druk). Het overschot "
             "gaat naar de lymfecapillairen.", 4),
            ("open", "Na een borstkankeroperatie werden lymfeklieren in de oksel weggenomen. De arm zwelt op. "
                     "Hoe heet dat en hoe kan men het behandelen?",
             "Lymfoedeem: de lymfe wordt niet goed afgevoerd. Behandeling met lymfedrainage, steunkousen of "
             "een drukverband, en blijven bewegen.", 3),
            ("tabel", ["Orgaan", "Wat het doet voor de afweer of het bloed"],
             [["milt", None], ["lymfeklier", None], ["thymus", None]],
             "Milt: ruimt versleten rode bloedcellen op, controleert het bloed op ziekteverwekkers, slaat "
             "bloed op. Lymfeklier: filtert de lymfe, lymfocyten ruimen ziektekiemen op. Thymus: laat de "
             "T-lymfocyten rijpen (thymosine).", WL),
        ]),
    ],
)

# ============================================================ 7. Ademhaling
OEFENBUNDELS["oefenbundel-het-ademhalingsstelsel-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Welzijnswetenschappen: Het ademhalingsstelsel", onder=ONDER, hoe=HOE,
    reeksen=[
        dict(kop="De luchtwegen", opdracht="Schrijf in de juiste volgorde of het juiste begrip.", oefeningen=[
            ("open", "Zet in volgorde: bronchiolen, luchtpijp, neusholte, longblaasjes, strottenhoofd, "
                     "keelholte, bronchiën.",
             "neusholte, keelholte, strottenhoofd, luchtpijp, bronchiën, bronchiolen, longblaasjes", 2),
            ("rij", [("houden de luchtpijp open", "kraakbeenringen"),
                     ("sluit het strottenhoofd af bij slikken", "strottenklepje"),
                     ("voeren slijm met stof naar de keel", "trilharen")], None, WM),
        ]),
        dict(kop="Inademen en uitademen", opdracht="Vul de tabel aan.", oefeningen=[
            ("tabel", ["", "Inademing", "Rustige uitademing"],
             [["middenrif", None, None], ["borstholte", None, None], ["druk in de longen", None, None]],
             "Inademing: middenrif trekt samen en wordt platter, borstholte wordt groter, druk daalt. "
             "Rustige uitademing: middenrif ontspant en welft op, borstholte wordt kleiner, druk stijgt.", WM),
        ]),
        dict(kop="Het spirogram", opdracht="Reken.", oefeningen=[
            ("kort", "Ademvolume 0,5 L, complementair volume 3,0 L, uitademingsreservevolume 1,2 L. Hoe groot "
                     "is de vitale capaciteit?", "4,7 L", "90px"),
            ("kort", "Het restvolume is 1,3 L. Hoe groot is de totale longcapaciteit?", "6,0 L", "90px"),
            ("open", "Waarom kan je het restvolume niet met een gewone spirometer meten?",
             "Het restvolume blijft na een maximale uitademing in de longen en komt er dus nooit uit; de "
             "spirometer meet enkel lucht die in- of uitgeademd wordt.", 2),
        ]),
        dict(kop="Waar of niet waar?", opdracht="Kruis aan.", oefeningen=[
            ("waar", "De linkerlong heeft drie longkwabben.", False),
            ("waar", "In de longblaasjes is de partiële druk van O₂ hoger dan in het bloed van de haarvaten.", True),
            ("waar", "De longen zetten uit dankzij hun eigen spieren.", False),
            ("waar", "Bij hyperventilatie adem je te veel CO₂ uit.", True),
        ]),
        dict(kop="Uitleggen", opdracht="Leg in volledige zinnen uit.", oefeningen=[
            ("open", "Noem drie kenmerken van de longblaasjes die gaswisseling makkelijk maken.",
             "Ze hebben samen een enorm groot oppervlak, hun wand is erg dun en ze zijn omringd door een dicht "
             "net van haarvaten.", 3),
            ("open", "In een werkende spier is het warm, zuur en is er veel CO₂. Wat betekent dat voor de "
                     "hemoglobine, en waarom is dat handig?",
             "De zuurstofaffiniteit daalt: hemoglobine laat er makkelijker zuurstof los. Zo krijgt de "
             "werkende spier precies daar meer zuurstof waar ze die nodig heeft.", 3),
            ("open", "Waarom krijgen rokers vaak een rokershoest?",
             "Rook beschadigt de trilharen, zodat het slijm niet meer goed afgevoerd wordt. Het lichaam "
             "probeert het dan weg te hoesten.", 2),
        ]),
    ],
)
