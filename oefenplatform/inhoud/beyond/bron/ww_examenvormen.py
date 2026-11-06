"""
Natuurwetenschappen welzijnswetenschappen 🌍 Beyond in de vormen van het examen
van de Examencommissie.

Kim op 6 november 2026: "kan deze ook opgemaakt worden als geschiedenis in
spark? want dat is zoals het ook op het echte examen gaat zijn". Zelfde opzet
als inhoud/spark/bron/geschiedenis_examenvormen.py: elk hoofdstuk krijgt er
vragen bij in de vormen van het examen (tabel, keuzelijst, volgorde, koppelen,
slepen naar kolommen, woorden in een zin slepen, open antwoord, tekenen en een
casus). Klikvragen op een prent staan er (nog) niet bij: daarvoor zijn eerst
tekeningen nodig.

De vragen die er al staan, blijven staan. De import zoekt elk hoofdstuk op zijn
titel en zet deze vragen erbij; zet "Bestaande vragen vervangen" dus NIET aan.
De titels zijn die van het vak "Natuurwetenschappen welzijnswetenschappen" zoals
ze online staan, met "Welzijnswetenschappen:" vooraan.

Hoe elke vorm in een bestand staat: zie lib/examenvormen.ts en lib/vraagvorm.ts.

Draaien: python3 inhoud/beyond/bron/ww_examenvormen.py
"""

import json
import os

J, F = True, False
HIER = os.path.dirname(os.path.abspath(__file__))
UIT = os.path.join(HIER, "..", "natuurwetenschappen-welzijnswetenschappen-examenvormen.json")
WW = "Welzijnswetenschappen: "


def tabel(vraag, rijen, uitleg):
    return {"type": "tabel", "vraag": vraag, "rijen": [r for r, _ in rijen], "antwoord": [a for _, a in rijen], "uitleg": uitleg}


def keuze(vraag, uitleg):
    return {"type": "keuzelijst", "vraag": vraag, "uitleg": uitleg}


def volgorde(vraag, stappen, uitleg):
    return {"type": "volgorde", "vraag": vraag, "opties": stappen, "uitleg": uitleg}


def koppel(vraag, paren, extra, uitleg):
    return {"type": "koppelen", "vraag": vraag, "paren": paren, "extra": extra, "uitleg": uitleg}


def sorteer(vraag, kolommen, items, uitleg):
    return {"type": "sorteren", "vraag": vraag, "kolommen": kolommen, "items": items, "uitleg": uitleg}


def sleep(vraag, extra, uitleg):
    return {"type": "sleepzin", "vraag": vraag, "extra": extra, "uitleg": uitleg}


def open_(vraag, voorbeeld, uitleg=None):
    v = {"type": "open", "vraag": vraag, "antwoord": voorbeeld}
    if uitleg:
        v["uitleg"] = uitleg
    return v


def teken(vraag, voorbeeld, uitleg=None):
    v = {"type": "tekenen", "vraag": vraag, "antwoord": voorbeeld}
    if uitleg:
        v["uitleg"] = uitleg
    return v


def casus(tekst, vragen):
    return {"casus": tekst, "vragen": vragen}


H = {}

# =========================================================================== Enzymen
H["Enzymen — deel 1"] = [
    tabel(
        "Lees elke uitspraak over enzymen. Is ze juist of fout?",
        [
            ("Een enzym is een eiwit.", J),
            ("Een enzym wordt bij de reactie opgebruikt.", F),
            ("Een enzym verlaagt de activeringsenergie.", J),
            ("Een enzym zorgt ervoor dat er op het einde meer product ontstaat.", F),
        ],
        "Een enzym is een eiwit dat als biokatalysator werkt: het verlaagt de activeringsenergie en komt onveranderd uit de reactie. Het verandert de evenwichtsligging niet; het evenwicht wordt alleen sneller bereikt.",
    ),
    sleep(
        "De stof die een enzym omzet, heet het [[substraat]]. Die bindt op het [[actief centrum]]. Samen vormen ze even het [[enzym-substraatcomplex]].",
        ["inhibitor", "co-enzym", "product"],
        "Een inhibitor remt het enzym, een co-enzym is een helper die vaak van een vitamine afgeleid is, en het product komt pas vrij na de reactie.",
    ),
    koppel(
        "Welk substraat breekt elk enzym af?",
        [
            ["Lactase", "Lactose"],
            ["Maltase", "Maltose"],
            ["Lipase", "Vetten of lipiden"],
            ["Pepsine", "Eiwitten"],
        ],
        ["Zetmeel"],
        "De naam op -ase wijst vaak naar het substraat. Pepsine is een oudere naam, maar breekt eiwitten af. Zetmeel wordt door amylase afgebroken.",
    ),
    volgorde(
        "Zet de stappen van een enzymreactie in de juiste volgorde.",
        [
            "Het substraat botst op het enzym",
            "Het substraat past in het actief centrum",
            "Het enzym-substraatcomplex ontstaat",
            "Het substraat wordt omgezet",
            "De producten komen vrij en het enzym is weer vrij",
        ],
        "Het substraat moet eerst het enzym raken en in het actief centrum passen. Dan vormen ze even het enzym-substraatcomplex, wordt het substraat omgezet en komen de producten vrij. Het enzym kan meteen opnieuw.",
    ),
    open_(
        "Leg met het sleutel-slotprincipe uit waarom lactase geen zetmeel kan afbreken.",
        "Het actief centrum van lactase is het slot en past enkel bij de vorm van lactose, de sleutel. Zetmeel heeft een andere vorm en past niet in dat actief centrum, dus het wordt niet omgezet. Dat heet substraatspecificiteit.",
    ),
]

H["Enzymen — deel 2"] = [
    keuze(
        "Bij een lage temperatuur werkt een enzym [[*trager|sneller|helemaal niet meer]], omdat de moleculen [[*trager bewegen|gedenatureerd zijn|uit elkaar vallen]].",
        "Bij kou bewegen enzym en substraat trager en botsen ze minder vaak. Het enzym is niet kapot: warm je het op, dan werkt het weer.",
    ),
    sorteer(
        "Wat gebeurt er met een menselijk enzym bij elke temperatuur?",
        ["Werkt traag maar is niet kapot", "Werkt het snelst", "Is gedenatureerd"],
        [
            ["4 °C in de koelkast", "Werkt traag maar is niet kapot"],
            ["37 °C", "Werkt het snelst"],
            ["90 °C", "Is gedenatureerd"],
            ["15 °C", "Werkt traag maar is niet kapot"],
            ["70 °C", "Is gedenatureerd"],
        ],
        "Het temperatuursoptimum van menselijke enzymen ligt rond 37 °C. Kou vertraagt, maar hitte denatureert blijvend.",
    ),
    koppel(
        "Bij welke pH werkt elk enzym het best?",
        [
            ["Pepsine in de maag", "Rond pH 2"],
            ["Speekselamylase in de mond", "Rond pH 7"],
            ["Trypsine in de twaalfvingerige darm", "Rond pH 8"],
        ],
        ["Rond pH 12"],
        "Elk enzym heeft een eigen pH-optimum: pepsine in de zure maag, speekselamylase neutraal, trypsine licht basisch.",
    ),
    tabel(
        "Een enzym werkt bij zijn optimum. Wat doet de reactiesnelheid stijgen?",
        [
            ("Meer enzym toevoegen, met substraat genoeg", J),
            ("Meer substraat toevoegen als alle actieve centra al bezet zijn", F),
            ("Een inhibitor toevoegen", F),
            ("Meer substraat toevoegen als er nog veel vrije actieve centra zijn", J),
        ],
        "Meer enzym geeft meer actieve centra. Meer substraat helpt enkel zolang er vrije actieve centra zijn; bij verzadiging niet meer. Een inhibitor remt.",
    ),
    casus(
        "Sara doet een proef met amylase en zetmeel. Ze zet drie buizen klaar: één bij 0 °C, één bij 37 °C en één bij 90 °C. Na tien minuten test ze met jood of er nog zetmeel is.",
        [
            keuze(
                "Het zetmeel is het snelst verdwenen in de buis bij [[*37 °C|0 °C|90 °C]].",
                "Bij 37 °C werkt amylase het snelst: dat is het temperatuursoptimum.",
            ),
            tabel(
                "Daarna zet Sara alle buizen tien minuten op 37 °C. Wat klopt?",
                [
                    ("In de buis die eerst op 0 °C stond, gaat het enzym alsnog werken.", J),
                    ("In de buis die eerst op 90 °C stond, gaat het enzym alsnog werken.", F),
                ],
                "Kou vertraagt een enzym alleen. Hitte denatureert het blijvend: het actief centrum krijgt zijn vorm niet terug.",
            ),
            open_(
                "Welke dingen moet Sara in de drie buizen gelijk houden, zodat de proef eerlijk is?",
                "Dezelfde hoeveelheid amylase, dezelfde hoeveelheid zetmeel, dezelfde pH en dezelfde tijd. Alleen de temperatuur mag verschillen.",
            ),
        ],
    ),
    teken(
        "Teken de grafiek van de reactiesnelheid van een menselijk enzym tegen de temperatuur, van 0 tot 60 °C. Duid het temperatuursoptimum aan.",
        "Op de x-as de temperatuur, op de y-as de reactiesnelheid. De lijn stijgt geleidelijk tot een top rond 37 °C, het temperatuursoptimum, en valt daarna snel naar nul.",
    ),
]

# =========================================================================== Spijsvertering
H["Het spijsverteringsstelsel — deel 1"] = [
    volgorde(
        "Zet de delen van het spijsverteringskanaal in de volgorde waarin het voedsel ze passeert.",
        ["Mondholte", "Keelholte", "Slokdarm", "Maag", "Twaalfvingerige darm", "Nuchtere darm", "Kronkeldarm", "Karteldarm", "Endeldarm"],
        "Mond, keel, slokdarm, maag, dan de drie delen van de dunne darm (twaalfvingerige, nuchtere en kronkeldarm), daarna de karteldarm van de dikke darm en de endeldarm.",
    ),
    volgorde(
        "Zet de lagen van de wand van het spijsverteringskanaal in volgorde, van binnen naar buiten.",
        ["Slijmvlieslaag", "Bindweefsellaag", "Spierlaag", "Steunweefsel aan de buitenkant"],
        "Het slijmvlies of de mucosa ligt tegen de voedselbrij. Daarna komen bindweefsel, de spierlaag en tot slot weer bindweefsel.",
    ),
    sorteer(
        "Hoort elk deel bij de dunne darm of bij de dikke darm?",
        ["Dunne darm", "Dikke darm"],
        [
            ["Twaalfvingerige darm", "Dunne darm"],
            ["Blinde darm", "Dikke darm"],
            ["Nuchtere darm", "Dunne darm"],
            ["Karteldarm", "Dikke darm"],
            ["Kronkeldarm", "Dunne darm"],
            ["Endeldarm", "Dikke darm"],
        ],
        "De dunne darm: twaalfvingerige, nuchtere en kronkeldarm. De dikke darm: blinde darm met wormvormig aanhangsel, karteldarm en endeldarm.",
    ),
    koppel(
        "Welk orgaan doet wat?",
        [
            ["Lever", "Maakt gal"],
            ["Galblaas", "Slaat gal op"],
            ["Alvleesklier", "Geeft NaHCO₃ en enzymen af aan de darm"],
            ["Maag", "Maakt zoutzuur"],
        ],
        ["Neemt het meeste water op"],
        "Het meeste water wordt in de dunne darm opgenomen, en dat is geen klier.",
    ),
    keuze(
        "De maagportier ligt tussen de [[*maag en de twaalfvingerige darm|slokdarm en de maag|dunne en de dikke darm]]. Bij het slikken sluit het [[*strottenklepje|huigje|maagportier]] de luchtpijp af.",
        "De maagportier is de kringspier aan de uitgang van de maag. Het strottenklepje voorkomt dat voedsel in de luchtpijp komt.",
    ),
    open_(
        "Waarom wordt pepsine eerst aangemaakt als het inactieve pepsinogeen?",
        "Pepsine breekt eiwitten af. Was het meteen actief, dan zou het de cellen die het maken zelf verteren. Pas in de maagholte zet het zoutzuur pepsinogeen om in pepsine.",
    ),
]

H["Het spijsverteringsstelsel — deel 2"] = [
    tabel(
        "Lees elke uitspraak. Is ze juist of fout?",
        [
            ("Gal bevat enzymen die vetten afbreken.", F),
            ("Galzouten verdelen grote vetdruppels in kleine druppeltjes.", J),
            ("Glycerol en vetzuren gaan via het lymfevat naar het bloed.", J),
            ("Glucose gaat via de leverpoortader naar de lever.", J),
            ("De dikke darm neemt het meeste water op.", F),
        ],
        "Gal emulgeert vetten maar bevat geen enzymen. Vetten gaan als lipoproteïnen naar de lymfe, glucose en aminozuren via de leverpoortader naar de lever. Het meeste water wordt al in de dunne darm opgenomen.",
    ),
    koppel(
        "Wat is het eindproduct van de vertering van elke voedingsstof?",
        [
            ["Zetmeel", "Glucose"],
            ["Eiwitten", "Aminozuren"],
            ["Vetten", "Glycerol en vetzuren"],
            ["Sacharose", "Glucose en fructose"],
        ],
        ["Glucose en galactose"],
        "Glucose en galactose komen uit lactose, de melksuiker, niet uit een van de stoffen links.",
    ),
    sorteer(
        "Is elke vorm van transport passief of actief?",
        ["Passief, geen ATP", "Actief, met ATP"],
        [
            ["Diffusie", "Passief, geen ATP"],
            ["Osmose", "Passief, geen ATP"],
            ["Gefaciliteerde diffusie", "Passief, geen ATP"],
            ["Een pomp die een stof tegen het concentratieverschil in brengt", "Actief, met ATP"],
            ["Blaasjestransport", "Actief, met ATP"],
        ],
        "Wat met het concentratieverschil mee gaat, is passief, ook via een transporteiwit. Tegen het concentratieverschil in kost energie uit ATP.",
    ),
    sleep(
        "De dunne darm heeft plooien, [[darmvlokken]] en [[microvilli]]. Die vergroten het [[oppervlak]] voor de opname van voedingsstoffen.",
        ["kraakbeenringen", "volume", "trilharen"],
        "Kraakbeenringen en trilharen horen bij de luchtpijp. Het gaat om een groter oppervlak, niet om een groter volume.",
    ),
    casus(
        "Lotte (16) heeft al maanden buikpijn, diarree en ze vermagert, hoewel ze goed eet. Een onderzoek toont dat haar darmvlokken beschadigd zijn. De arts denkt aan coeliakie.",
        [
            keuze(
                "Coeliakie is een [[*auto-immuunziekte|bacteriële infectie|voedselvergiftiging]] waarbij [[*gluten|lactose|vetten]] de darmvlokken beschadigen.",
                "Bij coeliakie reageert het afweersysteem op gluten en beschadigt het zo de eigen darmvlokken.",
            ),
            open_(
                "Leg uit waarom Lotte vermagert, ook al eet ze genoeg.",
                "De darmvlokken vergroten het opnameoppervlak. Zijn ze beschadigd, dan is dat oppervlak veel kleiner en neemt ze minder voedingsstoffen op.",
            ),
            keuze(
                "De behandeling is [[*strikt glutenvrij eten|antibiotica nemen|lactosevrij eten]].",
                "Zonder gluten herstellen de darmvlokken. Antibiotica helpen bij een bacterie zoals Helicobacter pylori, niet bij coeliakie.",
            ),
        ],
    ),
]

# =========================================================================== Uitscheiding
H["Het uitscheidingsstelsel — deel 1"] = [
    volgorde(
        "Zet de weg van de urine in de juiste volgorde.",
        ["Nier", "Urineleider", "Urineblaas", "Urinebuis"],
        "De nier maakt urine, de urineleider brengt ze naar de blaas, en via de urinebuis gaat ze naar buiten.",
    ),
    volgorde(
        "Zet de delen van een nefron in de volgorde waarin het filtraat erdoor stroomt.",
        ["Kapsel van Bowman", "Eerste kronkelbuisje", "Lus van Henle", "Tweede kronkelbuisje", "Verzamelbuis"],
        "Het filtraat ontstaat in het kapsel van Bowman en gaat dan door het eerste kronkelbuisje, de lus van Henle en het tweede kronkelbuisje naar de verzamelbuis.",
    ),
    sorteer(
        "Ligt elk deel in de nierschors of in het niermerg?",
        ["Nierschors", "Niermerg"],
        [
            ["Glomerulus", "Nierschors"],
            ["Kapsel van Bowman", "Nierschors"],
            ["Nierpiramides", "Niermerg"],
            ["Eerste kronkelbuisje", "Nierschors"],
            ["Diepste deel van de lus van Henle", "Niermerg"],
        ],
        "De nierlichaampjes en de kronkelbuisjes liggen in de schors. De lus van Henle duikt diep het merg in, waar ook de nierpiramides liggen.",
    ),
    koppel(
        "Welke stap in de nier is het?",
        [
            ["Water en kleine stoffen worden uit de glomerulus in het kapsel geperst", "Filtratie"],
            ["Glucose gaat uit het nierbuisje terug naar het bloed", "Resorptie"],
            ["Extra stoffen worden actief uit het bloed in het buisje gebracht", "Secretie"],
        ],
        ["Osmoregulatie"],
        "Osmoregulatie is het geheel van het water- en zoutevenwicht, geen stap van het nefron.",
    ),
    tabel(
        "Zit dit normaal in de urine van een gezond iemand?",
        [
            ("Ureum", J),
            ("Glucose", F),
            ("Water", J),
            ("Albumine", F),
            ("Rode bloedcellen", F),
            ("Zouten", J),
        ],
        "Urine bevat water, ureum, urinezuur en zouten. Alle glucose wordt teruggeresorbeerd, en rode bloedcellen en grote eiwitten zijn te groot voor de nierfilter.",
    ),
    open_(
        "Bij een urinetest vindt men veel eiwit in de urine. Wat is er waarschijnlijk mis, en waarom?",
        "De nierfilter in de glomerulus is waarschijnlijk beschadigd. Grote eiwitten zijn normaal te groot om erdoor te gaan; zitten ze in de urine, dan lekt de filter.",
    ),
]

H["Het uitscheidingsstelsel — deel 2"] = [
    volgorde(
        "Je hebt veel gezweet en weinig gedronken. Zet de stappen van de osmoregulatie in volgorde.",
        [
            "Het bloed wordt te geconcentreerd",
            "Osmoreceptoren merken het op",
            "De hypothalamus stuurt een signaal",
            "De hypofyse geeft meer ADH af",
            "De verzamelbuis neemt meer water terug",
            "Je plast weinig en geconcentreerd",
        ],
        "Sensor: osmoreceptoren. Controlecentrum: hypothalamus. Via de hypofyse komt ADH in het bloed, en de nieren als effector houden water vast.",
    ),
    keuze(
        "ADH maakt de wand van de verzamelbuis [[*beter|minder]] doorlaatbaar voor water. Alcohol [[*remt|stimuleert]] de afgifte van ADH, waardoor je [[*meer|minder]] moet plassen.",
        "Meer ADH: meer water terug, weinig urine. Alcohol remt ADH: minder water terug, meer urine.",
    ),
    koppel(
        "Welke rol speelt elk deel in de osmoregulatie?",
        [
            ["Osmoreceptoren", "Sensor"],
            ["Hypothalamus", "Controlecentrum"],
            ["Nieren", "Effector"],
        ],
        ["Hormoon"],
        "Het hormoon is ADH; dat is de boodschapper, geen van de drie delen links.",
    ),
    tabel(
        "Wat helpt om nierstenen te voorkomen?",
        [
            ("Voldoende water drinken", J),
            ("Veel zout eten", F),
            ("Gezond en gevarieerd eten", J),
            ("Zo weinig mogelijk drinken", F),
        ],
        "Veel water en weinig zout houden de urine verdund, zodat stoffen minder snel neerslaan tot een steen.",
    ),
    casus(
        "Meneer Peeters heeft nierfalen. Drie keer per week gaat hij naar het ziekenhuis voor hemodialyse. In zijn arm heeft hij een shunt.",
        [
            keuze(
                "Bij nierfalen stapelt vooral [[*ureum|glucose|albumine]] zich op in het bloed.",
                "Ureum is de afvalstof uit de afbraak van aminozuren die gezonde nieren met de urine afvoeren.",
            ),
            open_(
                "Leg uit hoe hemodialyse het bloed van meneer Peeters zuivert.",
                "Het bloed stroomt door een kunstnier langs een semipermeabel membraan. Afvalstoffen zoals ureum gaan door het membraan naar een spoelvloeistof, en het gezuiverde bloed gaat terug naar het lichaam.",
            ),
            keuze(
                "Een shunt is een verbinding tussen [[*een slagader en een ader|twee aders|de nier en de blaas]], zodat men vlot veel bloed kan afnemen.",
                "Door de slagader op een ader aan te sluiten, wordt die ader dik en stevig genoeg om vaak aan te prikken.",
            ),
        ],
    ),
]

# =========================================================================== Bloed
H["Het bloed — deel 1"] = [
    koppel(
        "Welke taak heeft elk bestanddeel van het bloed?",
        [
            ["Rode bloedcellen", "Vervoeren zuurstof"],
            ["Witte bloedcellen", "Afweer tegen ziekteverwekkers"],
            ["Bloedplaatjes", "Helpen bij de bloedstolling"],
            ["Plasma", "Vervoert voedingsstoffen, hormonen en afvalstoffen"],
        ],
        ["Maken gal aan"],
        "Gal wordt in de lever gemaakt, niet in het bloed.",
    ),
    volgorde(
        "Bloed met een middel tegen stolling wordt gecentrifugeerd. Zet de lagen in volgorde, van onder naar boven.",
        ["Rode bloedcellen", "Witte bloedcellen en bloedplaatjes", "Plasma"],
        "De zware rode bloedcellen zakken naar onder, daarop een dun laagje witte bloedcellen en bloedplaatjes, en bovenaan het lichte plasma.",
    ),
    tabel(
        "Lees elke uitspraak over rode bloedcellen. Is ze juist of fout?",
        [
            ("Een rijpe rode bloedcel heeft geen kern.", J),
            ("Een rode bloedcel leeft ongeveer een jaar.", F),
            ("Hemoglobine bevat ijzer.", J),
            ("Eén hemoglobinemolecule bindt maximaal twee zuurstofmoleculen.", F),
        ],
        "Rode bloedcellen hebben geen kern en leven ongeveer 120 dagen. Hemoglobine heeft vier heemgroepen met ijzer en bindt dus vier zuurstofmoleculen.",
    ),
    sleep(
        "Het percentage van het bloedvolume dat uit rode bloedcellen bestaat, heet de [[hematocrietwaarde]]. Het hormoon [[EPO]] uit de [[nieren]] laat die stijgen.",
        ["insuline", "lever", "hemoglobinewaarde"],
        "EPO, erytropoëtine, komt uit de nieren en laat het rode beenmerg meer rode bloedcellen maken.",
    ),
    sorteer(
        "Is elke witte bloedcel een granulocyt of een agranulocyt?",
        ["Granulocyt", "Agranulocyt"],
        [
            ["Neutrofiel", "Granulocyt"],
            ["Monocyt", "Agranulocyt"],
            ["Eosinofiel", "Granulocyt"],
            ["B-lymfocyt", "Agranulocyt"],
            ["Basofiel", "Granulocyt"],
            ["T-lymfocyt", "Agranulocyt"],
        ],
        "Granulocyten hebben korrels: neutrofielen, eosinofielen en basofielen. Monocyten en lymfocyten zijn agranulocyten.",
    ),
    open_(
        "Een wielrenner gaat drie weken op hoogtestage. Leg uit wat er met zijn bloed gebeurt en waarom hem dat helpt.",
        "In de ijle lucht is er minder zuurstof. De nieren maken meer EPO, waardoor het beenmerg meer rode bloedcellen maakt. Zijn hematocriet stijgt en zijn bloed kan meer zuurstof vervoeren.",
    ),
]

H["Het bloed — deel 2"] = [
    volgorde(
        "Zet de laatste stappen van de bloedstolling in volgorde.",
        [
            "Bloedplaatjes kleven tegen de beschadigde wand",
            "De stollingscascade start",
            "Protrombine wordt trombine",
            "Trombine zet fibrinogeen om in fibrine",
            "Fibrinedraden vormen een stolsel",
        ],
        "De bloedplaatjes starten de stollingscascade. Op het einde zet trombine het opgeloste fibrinogeen om in onoplosbare fibrinedraden.",
    ),
    tabel(
        "Kan elke patiënt dit bloed veilig krijgen? Kijk enkel naar het AB0-systeem.",
        [
            ("Patiënt met bloedgroep AB krijgt bloed van groep A", J),
            ("Patiënt met bloedgroep O krijgt bloed van groep A", F),
            ("Patiënt met bloedgroep A krijgt bloed van groep O", J),
            ("Patiënt met bloedgroep B krijgt bloed van groep A", F),
        ],
        "AB heeft geen anti-A of anti-B en kan alles krijgen. O heeft anti-A en anti-B en kan enkel O krijgen. Bloed van groep O heeft geen A- of B-antigenen en past bij iedereen.",
    ),
    koppel(
        "Welke antilichamen zitten in het plasma bij elke bloedgroep?",
        [
            ["Bloedgroep A", "Anti-B"],
            ["Bloedgroep B", "Anti-A"],
            ["Bloedgroep AB", "Geen anti-A en geen anti-B"],
            ["Bloedgroep O", "Anti-A en anti-B"],
        ],
        ["Anti-D van nature"],
        "Anti-D is er nooit van nature: een resusnegatieve persoon maakt het pas na contact met resuspositief bloed.",
    ),
    koppel(
        "Welke witte bloedcel doet dit?",
        [
            ["Wordt een plasmacel die antilichamen maakt", "B-lymfocyt"],
            ["Doodt lichaamscellen die besmet zijn met een virus", "T-lymfocyt"],
            ["Wordt in het weefsel een macrofaag", "Monocyt"],
            ["Ruimt bij een ontsteking als eerste bacteriën op", "Neutrofiel"],
        ],
        ["Trombocyt"],
        "Een trombocyt is een bloedplaatje en helpt bij de stolling, niet bij de afweer.",
    ),
    casus(
        "Ella is resusnegatief. Ze is zwanger van haar eerste kind, en dat kind is resuspositief. Bij de bevalling komt wat bloed van de baby in haar bloed.",
        [
            keuze(
                "Na de bevalling kan Ella [[*anti-D|anti-A|anti-B]] maken.",
                "Haar afweer ziet het D-antigeen van de baby als vreemd en maakt er antilichamen tegen.",
            ),
            open_(
                "Waarom is dat vooral een risico bij een volgende zwangerschap van een resuspositief kind?",
                "Het anti-D van Ella kan door de placenta naar de volgende baby gaan en zijn rode bloedcellen doen klonteren en afbreken. Bij de eerste baby is er nog geen anti-D, want dat wordt pas na het contact gemaakt.",
            ),
        ],
    ),
    sleep(
        "Het samenklonteren van rode bloedcellen door antilichamen heet [[agglutinatie]]. Plasma zonder stollingsfactoren heet [[serum]].",
        ["fagocytose", "lymfe", "hemolyse"],
        "Fagocytose is het opslokken van een bacterie. Hemolyse is het kapotgaan van rode bloedcellen, wat na de agglutinatie volgt.",
    ),
]

# =========================================================================== Hart en bloedsomloop
H["Het hart en de bloedsomloop — deel 1"] = [
    volgorde(
        "Volg het bloed door de rechterhelft van het hart. Zet in de juiste volgorde.",
        ["Holle aders", "Rechterboezem", "Tricuspidalisklep", "Rechterkamer", "Pulmonalisklep", "Longslagader"],
        "Zuurstofarm bloed komt via de holle aders in de rechterboezem en gaat door de tricuspidalisklep naar de rechterkamer, en dan door de pulmonalisklep de longslagader in.",
    ),
    volgorde(
        "Volg het bloed door de linkerhelft van het hart. Zet in de juiste volgorde.",
        ["Longaders", "Linkerboezem", "Mitralisklep", "Linkerkamer", "Aortaklep", "Aorta"],
        "Zuurstofrijk bloed komt via de longaders in de linkerboezem en gaat door de mitralisklep naar de linkerkamer, dan door de aortaklep de aorta in.",
    ),
    sorteer(
        "Vervoert elk bloedvat zuurstofrijk of zuurstofarm bloed?",
        ["Zuurstofrijk", "Zuurstofarm"],
        [
            ["Aorta", "Zuurstofrijk"],
            ["Longslagader", "Zuurstofarm"],
            ["Longaders", "Zuurstofrijk"],
            ["Bovenste holle ader", "Zuurstofarm"],
            ["Kransslagader", "Zuurstofrijk"],
        ],
        "Let op: de longslagader is een slagader met zuurstofarm bloed, en de longaders zijn aders met zuurstofrijk bloed.",
    ),
    tabel(
        "Lees elke uitspraak over het hart. Is ze juist of fout?",
        [
            ("De linkerkamer heeft de dikste spierwand.", J),
            ("Het hart heeft drie holtes.", F),
            ("De hartspier krijgt zijn bloed via de kransslagaders.", J),
            ("De mitralisklep ligt tussen de rechterboezem en de rechterkamer.", F),
        ],
        "De linkerkamer pompt het bloed door de hele grote bloedsomloop. Het hart heeft vier holtes. De mitralisklep ligt links; rechts ligt de tricuspidalisklep.",
    ),
    volgorde(
        "Zet de hartwand in volgorde, van binnen naar buiten.",
        ["Endocard", "Myocard", "Epicard", "Hartzakje"],
        "Het endocard bekleedt de binnenkant, het myocard is de dikke spierlaag, het epicard ligt erop, en rond het hart zit het hartzakje of pericard.",
    ),
    teken(
        "Teken een schema van het hart met de vier holtes. Duid de vier kleppen aan en zet pijlen voor de richting van het bloed.",
        "Vier vakjes: boven de twee boezems, onder de twee kamers, met het tussenschot in het midden. Rechts (op de tekening links) de tricuspidalisklep tussen boezem en kamer en de pulmonalisklep naar de longslagader. Links de mitralisklep tussen boezem en kamer en de aortaklep naar de aorta. Pijlen van boezem naar kamer en van kamer naar de slagader.",
    ),
]

H["Het hart en de bloedsomloop — deel 2"] = [
    volgorde(
        "Zet de prikkelgeleiding van het hart in volgorde.",
        ["Sinusknoop", "AV-knoop", "Bundel van His", "Bundeltakken", "Purkinjevezels"],
        "De prikkel ontstaat in de sinusknoop, wordt in de AV-knoop even opgehouden en gaat dan via de bundel van His en de bundeltakken naar de purkinjevezels in de kamerwand.",
    ),
    koppel(
        "Waarbij hoort elk deel van het ECG?",
        [
            ["P-top", "Prikkeling van de boezems"],
            ["QRS-complex", "Prikkeling van de kamers"],
            ["T-top", "Herstel van de kamers"],
        ],
        ["Sluiten van de aortaklep"],
        "Een ECG meet elektrische activiteit, geen kleppen.",
    ),
    keuze(
        "Tijdens de kamersystole trekken de kamers [[*samen|niet samen]], zijn de atrioventriculaire kleppen [[*dicht|open]] en staan de aortaklep en de pulmonalisklep [[*open|dicht]].",
        "De kamers persen het bloed de slagaders in. De kleppen naar de boezems sluiten, zodat het bloed niet terugstroomt.",
    ),
    sorteer(
        "Past elk kenmerk bij een slagader of bij een ader?",
        ["Slagader", "Ader"],
        [
            ["Dikke, gespierde wand", "Slagader"],
            ["Heeft kleppen", "Ader"],
            ["Hoge druk", "Slagader"],
            ["Lage druk", "Ader"],
            ["Vervoert bloed van het hart weg", "Slagader"],
        ],
        "Slagaders krijgen het bloed met hoge druk uit het hart en hebben een stevige wand. Aders brengen het bloed terug, met lage druk, en hebben kleppen.",
    ),
    tabel(
        "Wat helpt het bloed in de aders van je benen terug naar het hart?",
        [
            ("De veneuze kleppen", J),
            ("Het samentrekken van de beenspieren", J),
            ("De zwaartekracht", F),
            ("De zuigwerking bij het inademen", J),
        ],
        "De zwaartekracht werkt net tegen. Kleppen, spieren en de zuigwerking van de ademhaling zorgen voor de veneuze terugstroom.",
    ),
    casus(
        "Jan (58) rookt al jaren. Op een ochtend krijgt hij een drukkende pijn op de borst die uitstraalt naar zijn linkerarm. In het ziekenhuis stellen ze een hartinfarct vast.",
        [
            keuze(
                "Een hartinfarct ontstaat meestal doordat [[*een kransslagader verstopt raakt|de aortaklep lekt|de sinusknoop stopt]].",
                "De kransslagaders brengen zuurstofrijk bloed naar de hartspier zelf.",
            ),
            open_(
                "Leg uit waarom er bij een infarct een stuk hartspier afsterft.",
                "Achter de verstopping krijgt de hartspier geen zuurstofrijk bloed meer. Zonder zuurstof kunnen de spiercellen geen energie maken en sterven ze af.",
            ),
        ],
    ),
    open_(
        "Leg uit wat een poortader is en geef het voorbeeld van de leverpoortader.",
        "Een poortader is een ader tussen twee haarvatennetwerken. De leverpoortader brengt bloed van de haarvaten van de darm naar die van de lever, zodat de lever de opgenomen voedingsstoffen eerst verwerkt en het bloed ontgift.",
    ),
]

# =========================================================================== Bloeddruk en lymfe
H["De bloeddruk en het lymfestelsel — deel 1"] = [
    tabel(
        "Lees elke uitspraak over de bloeddruk. Is ze juist of fout?",
        [
            ("Ongeveer 120/80 mmHg is normaal bij een gezonde volwassene in rust.", J),
            ("Vanaf 120/80 mmHg spreekt men van hypertensie.", F),
            ("De bloeddruk is het hoogst in de aorta.", J),
            ("De bloeddruk is hoger in de aders dan in de slagaders.", F),
        ],
        "Hypertensie begint vanaf 140/90 mmHg. De druk is het hoogst in de aorta en daalt tot in de aders.",
    ),
    volgorde(
        "Zet het renine-angiotensinesysteem in de juiste volgorde.",
        [
            "De bloeddruk is te laag",
            "De nieren maken renine",
            "Angiotensinogeen wordt angiotensine I",
            "ACE zet het om in angiotensine II",
            "Vasoconstrictie en aldosteron",
            "De bloeddruk stijgt",
        ],
        "Renine zet angiotensinogeen om in angiotensine I, ACE maakt er angiotensine II van. Dat vernauwt de bloedvaten en maakt aldosteron vrij, zodat de nieren meer zout en water terugnemen.",
    ),
    sorteer(
        "Doet elke verandering de bloeddruk stijgen of dalen?",
        ["Stijgen", "Dalen"],
        [
            ["Vasoconstrictie", "Stijgen"],
            ["Vasodilatatie", "Dalen"],
            ["Meer aldosteron", "Stijgen"],
            ["Het hart klopt trager", "Dalen"],
            ["Het orthosympatisch zenuwstelsel wordt actief", "Stijgen"],
        ],
        "Nauwere vaten, meer bloedvolume en een sneller hart doen de druk stijgen. Wijdere vaten en een trager hart doen ze dalen.",
    ),
    koppel(
        "Welke rol speelt elk deel bij de regeling van de bloeddruk?",
        [
            ["Baroreceptoren", "Meten de druk in de aorta en de halsslagaders"],
            ["Cardiovasculair centrum", "Stuurt bij vanuit het verlengde merg"],
            ["Aldosteron", "Laat de nieren meer zout en water terugnemen"],
        ],
        ["Maakt de verzamelbuis doorlaatbaar voor water"],
        "Dat laatste doet ADH, niet aldosteron.",
    ),
    keuze(
        "De bloeddruk wordt geregeld door een [[*negatief|positief]] feedbacksysteem: het [[*werkt de verandering tegen|versterkt de verandering]].",
        "Is de druk te hoog, dan zorgt het systeem dat ze daalt, en omgekeerd.",
    ),
    open_(
        "Geef drie dingen die iemand kan doen om een te hoge bloeddruk te voorkomen.",
        "Minder zout eten, regelmatig bewegen en niet roken. Ook een gezond gewicht en weinig alcohol helpen.",
    ),
]

H["De bloeddruk en het lymfestelsel — deel 2"] = [
    sleep(
        "Aan het begin van een haarvat perst de [[bloeddruk]] plasma naar buiten. Aan het einde trekken de [[plasma-eiwitten]] water terug. Het overschot gaat naar de [[lymfecapillairen]].",
        ["kransslagaders", "bloedplaatjes", "nierbuisjes"],
        "Zo ontstaat weefselvocht, en wat niet terugkeert naar het haarvat, wordt lymfe.",
    ),
    koppel(
        "Wat doet elk lymfeorgaan?",
        [
            ["Milt", "Ruimt versleten rode bloedcellen op"],
            ["Thymus", "Laat T-lymfocyten rijpen"],
            ["Lymfeklier", "Filtert de lymfe"],
        ],
        ["Maakt insuline"],
        "Insuline komt uit de alvleesklier, en die hoort niet bij het lymfestelsel.",
    ),
    tabel(
        "Lees elke uitspraak over het lymfestelsel. Is ze juist of fout?",
        [
            ("Lymfevaten hebben kleppen.", J),
            ("Het lymfestelsel heeft een eigen pomp.", F),
            ("Werkende spieren duwen de lymfe vooruit.", J),
            ("De schildklier hoort bij het lymfestelsel.", F),
        ],
        "Lymfe wordt voortgeduwd door werkende spieren, en de kleppen houden de richting. Een eigen pomp is er niet. De schildklier is een hormoonklier.",
    ),
    sorteer(
        "Wat zit er in weefselvocht, vergeleken met plasma?",
        ["Evenveel als in plasma", "Veel minder dan in plasma"],
        [
            ["Water", "Evenveel als in plasma"],
            ["Zouten", "Evenveel als in plasma"],
            ["Grote eiwitten", "Veel minder dan in plasma"],
            ["Glucose", "Evenveel als in plasma"],
        ],
        "Kleine stoffen gaan vlot door de wand van het haarvat. Grote eiwitten blijven grotendeels in het bloed.",
    ),
    casus(
        "Mevrouw Claes werd geopereerd aan borstkanker. Daarbij werden ook de lymfeklieren in haar oksel weggenomen. Enkele maanden later is haar arm dik en gezwollen.",
        [
            keuze(
                "Deze zwelling heet [[*lymfoedeem|hongeroedeem|hypertensie]].",
                "Zonder lymfeklieren wordt de lymfe uit de arm niet goed afgevoerd.",
            ),
            open_(
                "Leg uit waarom de arm opzwelt.",
                "Het weefselvocht dat niet terug in de haarvaten gaat, moet via de lymfevaten afgevoerd worden. Zonder de lymfeklieren in de oksel lukt dat niet goed, zodat er vocht in de arm blijft staan.",
            ),
            tabel(
                "Wat helpt mevrouw Claes?",
                [
                    ("Lymfedrainage", J),
                    ("De arm zo weinig mogelijk bewegen", F),
                    ("Een steunkous of drukverband", J),
                ],
                "Lymfedrainage en druk helpen de lymfe weg. Bewegen helpt ook, want werkende spieren duwen de lymfe vooruit.",
            ),
        ],
    ),
]

# =========================================================================== Ademhaling
H["Het ademhalingsstelsel — deel 1"] = [
    volgorde(
        "Zet de weg van de ingeademde lucht in de juiste volgorde.",
        ["Neusholte", "Keelholte", "Strottenhoofd", "Luchtpijp", "Bronchiën", "Bronchiolen", "Longblaasjes"],
        "Van de neus over de keel en het strottenhoofd naar de luchtpijp, die zich splitst in bronchiën en bronchiolen tot in de longblaasjes.",
    ),
    koppel(
        "Welke taak heeft elk deel?",
        [
            ["Kraakbeenringen", "Houden de luchtpijp open"],
            ["Strottenklepje", "Sluit het strottenhoofd af bij het slikken"],
            ["Trilhaarepitheel", "Voert slijm met stof naar de keel"],
            ["Longblaasjes", "Plaats van de gaswisseling"],
        ],
        ["Maakt de stem"],
        "De stem ontstaat in de stembanden, in het strottenhoofd; dat staat niet links.",
    ),
    tabel(
        "Lees elke uitspraak. Is ze juist of fout?",
        [
            ("De rechterlong heeft drie longkwabben.", J),
            ("De linkerlong heeft drie longkwabben.", F),
            ("De gaswisseling gebeurt in de longblaasjes.", J),
            ("De longen zetten uit door hun eigen spieren.", F),
        ],
        "Rechts drie kwabben, links twee, want daar ligt het hart. De longen hebben geen eigen spieren; ze volgen de borstkas.",
    ),
    volgorde(
        "Zet de stappen van een inademing in de juiste volgorde.",
        [
            "Het middenrif en de tussenribspieren trekken samen",
            "De borstholte wordt groter",
            "De druk in de longen daalt",
            "Lucht stroomt naar binnen",
        ],
        "Door de grotere borstholte daalt de druk in de longen onder de luchtdruk buiten, en dan stroomt er lucht in.",
    ),
    sorteer(
        "Hoort elk kenmerk bij de middenrifademhaling of bij de ribademhaling?",
        ["Middenrifademhaling", "Ribademhaling"],
        [
            ["Het middenrif wordt platter", "Middenrifademhaling"],
            ["De tussenribspieren heffen de ribben op", "Ribademhaling"],
            ["Wordt ook buikademhaling genoemd", "Middenrifademhaling"],
            ["Wordt ook borstademhaling genoemd", "Ribademhaling"],
        ],
        "Bij de middenrifademhaling bolt de buik wat naar buiten. Bij de ribademhaling gaat de borstkas omhoog en naar voor.",
    ),
    open_(
        "Geef drie kenmerken van de longblaasjes die gaswisseling makkelijk maken.",
        "Ze hebben samen een enorm groot oppervlak, hun wand is erg dun en ze zijn omringd door een dicht net van haarvaten.",
    ),
]

H["Het ademhalingsstelsel — deel 2"] = [
    keuze(
        "In de longblaasjes is de partiële druk van O₂ [[*hoger|lager]] dan in het bloed. Zuurstof gaat er door [[*diffusie|actief transport|osmose]] naar het bloed.",
        "Gassen gaan passief van hoge naar lage partiële druk.",
    ),
    tabel(
        "Wanneer laat hemoglobine zuurstof makkelijker los?",
        [
            ("Bij een hogere temperatuur", J),
            ("Bij een hogere CO₂-concentratie", J),
            ("Bij een hogere pH, dus minder zuur", F),
            ("In de longblaasjes", F),
        ],
        "In werkende spieren is het warm, zuur en is er veel CO₂: daar laat hemoglobine zuurstof los. In de longen bindt ze juist zuurstof.",
    ),
    koppel(
        "Welke waarde uit het spirogram is het?",
        [
            ["De lucht bij een gewone, rustige ademhaling", "Ademvolume"],
            ["De lucht die je na een gewone inademing nog extra kan inademen", "Complementair volume"],
            ["De lucht die na een maximale uitademing in de longen blijft", "Restvolume"],
            ["De grootste hoeveelheid lucht die je na een maximale inademing kan uitademen", "Vitale capaciteit"],
        ],
        ["Hematocriet"],
        "De hematocriet hoort bij het bloed, niet bij het spirogram.",
    ),
    keuze(
        "De totale longcapaciteit is de vitale capaciteit [[*plus|min]] het [[*restvolume|ademvolume|complementair volume]].",
        "Het restvolume kan je niet uitademen, maar het zit wel in de longen.",
    ),
    open_(
        "Iemand heeft een ademvolume van 0,5 L, een complementair volume van 3,0 L en een uitademingsreservevolume van 1,2 L. Bereken de vitale capaciteit en schrijf je berekening op.",
        "Vitale capaciteit = ademvolume + complementair volume + uitademingsreservevolume = 0,5 L + 3,0 L + 1,2 L = 4,7 L.",
    ),
    casus(
        "Noor (15) heeft astma. Tijdens de sportles krijgt ze het benauwd. Ze hoest, haar ademhaling piept en ze krijgt moeilijk lucht. Ze neemt haar puffer.",
        [
            keuze(
                "Bij een astma-aanval [[*vernauwen en zwellen de bronchiolen|scheuren de longblaasjes|stopt het middenrif]].",
                "Door de nauwere en gezwollen bronchiolen gaat er moeilijk lucht in en uit.",
            ),
            open_(
                "Wat doet haar puffer?",
                "De puffer verwijdt de bronchiolen, zodat er weer meer lucht door kan en ademen makkelijker gaat.",
            ),
            tabel(
                "Lees elke uitspraak. Is ze juist of fout?",
                [
                    ("Astma is besmettelijk.", F),
                    ("Mucoviscidose is een erfelijke ziekte met taai slijm.", J),
                    ("Bij hyperventilatie adem je te veel CO₂ uit.", J),
                ],
                "Astma en mucoviscidose zijn niet besmettelijk. Bij hyperventilatie adem je te snel en te diep, zodat je te veel CO₂ uitademt.",
            ),
        ],
    ),
]


def tel(vragen):
    """Telt de vragen, ook die in een casus."""
    n = 0
    for v in vragen:
        n += len(v["vragen"]) if "casus" in v else 1
    return n


def main():
    hoofdstukken = [{"titel": WW + t, "niveau": "beyond-doorstroom", "vragen": v} for t, v in H.items()]
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump({"hoofdstukken": hoofdstukken}, f, ensure_ascii=False, indent=2)
        f.write("\n")
    for t, v in H.items():
        print(f"  {t}: {tel(v)}")
    totaal = sum(tel(v) for v in H.values())
    print(f"{len(hoofdstukken)} hoofdstukken, {totaal} vragen -> {os.path.normpath(UIT)}")


if __name__ == "__main__":
    main()
