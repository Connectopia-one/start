"""De Franstalige wereld: omgangsvormen en gewoontes — pittig (🚀 Boost doorstroom, Frans).

Eigen vragen strikt binnen fr_cultuur: waar Frans gesproken wordt, het Frans
van België, Zwitserland en Québec, Franse gewoontes (school, maaltijd, feestdag)
en beleefdheidsvormen. Met een zelfgetekende schoolladder."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, LICHTGROEN, GEEL, ORANJE, BLAUW

SL = Prent("schoolladder-frankrijk", "L'école en France", "vier treden met een leeftijd, letters A tot D")
TR = [("A", 100, 400, "6 – 11 ans", LICHTGROEN), ("B", 310, 310, "11 – 15 ans", GEEL), ("C", 520, 220, "15 – 18 ans", ORANJE), ("D", 730, 130, "à partir de 18 ans", "#9ec7e6")]
for t, x, y, lft, kl in TR:
    SL.rect(x, y, 200, 560 - y, kl, DONKER, 6, 3)
    SL.tekst(x + 100, y + 40, lft, 20, vet=True)
    SL.letter(x + 100, y + 85, t)
SL.lijn(60, 560, 960, 560, DONKER, 3)
U = "schoolladder-frankrijk.svg"
Z = {t: [Prent.zone(x, y, 200, 560 - y)] for t, x, y, _, _ in TR}

MAIL = ("Lees de mail van Lucas, een Belgische leerling, aan een gastgezin in Lyon.\n\n"
        "« Salut !\n"
        "Je m'appelle Lucas et je vais loger chez vous pendant quinze jours en juillet. J'arrive le 12 juillet en train ; le billet coûte septante-cinq euros, "
        "et je voudrais savoir si quelqu'un pourrait venir me chercher à la gare. Mon GSM : 0470 12 34 56.\n"
        "Bisous,\n"
        "Lucas »")

VRAGEN = [
    klik("Bekijk de schoolladder. Klik op het lycée.", U, Z["C"], "Het lycée volgt op het collège en eindigt met le bac."),
    klik("Klik op het collège.", U, Z["B"], "Na de école primaire ga je naar het collège."),
    klik("Klik op de trede waar je naartoe gaat nadat je le bac gehaald hebt.", U, Z["D"], "Met le bac op zak kan je naar de université."),
    casus(MAIL, [
        mk("Lucas schrijft aan een gastgezin dat hij niet kent. Wat past niet bij zo'n mail?",
           ["'Salut !' en 'Bisous'", "'je voudrais savoir'", "'pourrait venir me chercher'", "'je vais loger chez vous'"],
           0, "Salut en bisous horen bij vrienden. Beter: Madame, Monsieur en Cordialement of Bien à vous."),
        sorteer("Welke woorden zou iemand in Lyon niet zo gebruiken?", ["Belgisch", "gewoon Frans uit Frankrijk"],
                [("septante", "Belgisch"), ("GSM", "Belgisch"), ("quinze jours", "gewoon Frans uit Frankrijk"), ("la gare", "gewoon Frans uit Frankrijk")],
                "In Frankrijk zegt men soixante-dix en un portable."),
        inv("Hoe zegt men in Frankrijk 'septante-cinq'? Schrijf het voluit, met streepjes.", ["soixante-quinze"], "Soixante-quinze: zestig plus vijftien."),
        keuze("'Quinze jours' betekent [[*twee weken|vijftien weken|een maand]].", "Zo zegt men veertien dagen."),
        keuze("Met 'je voudrais' gebruikt Lucas de [[*conditionnel de politesse|impératif|passé composé]].", "Je voudrais klinkt beleefder dan je veux."),
    ]),
    sorteer("België of Frankrijk?", ["België", "Frankrijk"],
            [("le dîner = het middagmaal", "België"), ("le déjeuner = het middagmaal", "Frankrijk"), ("nonante", "België"), ("quatre-vingt-dix", "Frankrijk"), ("le souper = het avondmaal", "België"), ("un portable", "Frankrijk")],
            "In België schuiven de maaltijden een plaats op."),
    koppel("Koppel het woord uit Québec aan de betekenis.",
           [("un courriel", "een e-mail"), ("la fin de semaine", "het weekend"), ("magasiner", "gaan winkelen"), ("un cellulaire", "een gsm")],
           ["een fiets"],
           "Québec vervangt Engelse leenwoorden door Franse."),
    tabel("Is het Frans hier een officiële taal?",
          [("Zwitserland", J), ("Senegal", J), ("Portugal", F), ("Luxemburg", J), ("Brazilië", F)],
          "In Portugal en Brazilië spreekt men Portugees."),
    volgorde("Zet de gangen van een klassieke Franse maaltijd in de juiste volgorde.",
             ["l'apéritif", "l'entrée", "le plat", "le fromage", "le dessert"],
             "De kaas komt vóór het dessert."),
    sorteer("Wanneer zeg je het?", ["bij het begin", "bij het afscheid", "als excuus"],
            [("Enchanté", "bij het begin"), ("Bonjour", "bij het begin"), ("Bonne soirée", "bij het afscheid"), ("À bientôt", "bij het afscheid"), ("Excusez-moi", "als excuus"), ("Je suis désolé", "als excuus")],
            "Enchanté zeg je bij een eerste ontmoeting."),
    mk("Je gaat in Parijs een apotheek binnen. Wat zeg je eerst?",
       ["Bonjour", "Je veux de l'aspirine", "Salut, ça va ?", "Au revoir"],
       0, "Eerst groeten, dan vragen. Meteen bestellen komt onbeleefd over."),
    mk("Een leerkracht in Québec zegt na een week: 'On peut se tutoyer, si tu veux.' Wat bedoelt ze?",
       ["jullie mogen elkaar met tu aanspreken", "je moet haar voortaan met vous aanspreken", "ze wil dat je haar een kus geeft", "je moet een formele mail sturen"],
       0, "Tutoyer: tu zeggen. In Québec gebeurt dat sneller."),
    keuze("De nationale feestdag van Frankrijk is op [[*14 juli|21 juli|11 november]].", "21 juli is de Belgische feestdag."),
    inv("Hoe heet het diploma waarmee een leerling in Frankrijk het lycée afsluit? Kort woord.", ["bac", "le bac", "baccalauréat", "le baccalauréat"], "Le baccalauréat, kortweg le bac."),
    tabel("Klopt dit over omgangsvormen en gewoontes?",
          [("Maanden schrijf je in het Frans met een kleine letter.", J), ("'Le 1er mai' is de eerste mei.", J), ("Bon appétit zeg je na de maaltijd.", F), ("La rentrée is het begin van het schooljaar.", J)],
          "Bon appétit zeg je vóór je begint te eten."),
    mk("Wat antwoord je beleefd op 'Merci beaucoup, Madame' van een klant?",
       ["De rien", "Bisous", "Excusez-moi", "Enchanté"],
       0, "De rien of je vous en prie: graag gedaan."),
    keuze("'Huit jours' betekent [[*een week|acht weken|twee weken]].", "Zoals quinze jours twee weken is."),
    sleep("Een formele mail begin je met [[Madame, Monsieur]] en sluit je af met [[Cordialement]]. Aan een vriend schrijf je [[Salut]].",
          ["Bisous à vous", "Au secours"], "Pas je taal aan de ontvanger aan."),
    mk("In welk werelddeel liggen de meeste landen waar Frans een officiële taal is?",
       ["Afrika", "Europa", "Azië", "Zuid-Amerika"],
       0, "Senegal, Mali, Congo, Ivoorkust en nog vele andere."),
    inv("Hoe noem je iemand die Frans spreekt? Eén Frans woord.", ["francophone", "un francophone", "une francophone"], "Un francophone; samen vormen ze la Francophonie."),
    open_("Je logeert bij een Frans gastgezin. Schrijf in het Frans een beleefde vraag om je gsm te mogen opladen. Gebruik de conditionnel.",
          "Pourriez-vous me dire où je peux recharger mon portable, s'il vous plaît ?"),
    keuze("Een cégep in Québec is een school [[*tussen het secundair en de universiteit|voor kleuters|voor volwassenen die Frans leren]].", "Frankrijk en België hebben die tussenstap niet."),
    tabel("Klopt dit over omgangsvormen?",
          [("La bise is een begroeting met kussen op de wang.", J), ("Lichaamstaal hoort ook bij een cultuur.", J), ("Tegen een onbekende volwassene zeg je meteen tu.", F), ("In een Franse winkel geef je altijd een fooi.", F)],
          "Vouvoyer tot de ander voorstelt om te tutoyeren."),
    mk("Je eet in een Frans restaurant. Op de rekening staat 'service compris'. Wat betekent dat?",
       ["de bediening zit al in de prijs", "je moet nog tien procent fooi geven", "de bediening is vandaag gratis", "je moet aan de kassa betalen"],
       0, "Een fooi mag, maar moet niet."),
    keuze("Canada heeft als officiële talen [[*Engels en Frans|enkel Engels|Frans en Spaans]].", "In Québec is het Frans bovendien de enige officiële taal."),
    inv("Wat is de hoofdstad van Senegal?", ["Dakar"], "Dakar ligt in een Franstalig land in West-Afrika."),
    mk("Je schrijft een blogbericht over je stage voor leeftijdsgenoten. Wat past?",
       ["losse maar verzorgde taal zonder sms-taal", "de deftigste slotformule die je kent uit brieven", "enkel sms-taal en emoji's", "een aanhef met Madame, Monsieur"],
       0, "Losser dan een brief, maar nog altijd geschreven taal."),
]
