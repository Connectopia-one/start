"""Biologische feedback en homeostase — pittig (🚀 Boost dubbele finaliteit, natuurwetenschappen).

Eigen vragen strikt binnen nwdf_feedback, met een zelfgetekend schema van een
feedbacksysteem om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, ORANJE, GROEN, ROOD, DONKER, GRIJS

FB = Prent("feedback-temperatuur", "Temperatuurregeling bij de mens", "schema met de huid, de hersenen, de zweetklieren en de bloedvaten, verbonden met pijlen en letters, en een terugkoppelpijl met een minteken")
blokken = {
    "A": (20, 270, "warmere omgeving", "#f6e3c9"),
    "B": (270, 270, "warmtereceptoren in de huid", "#e6eef6"),
    "C": (470, 140, "hersenen", "#efe3f2"),
    "D": (700, 270, "zweetklieren en bloedvaten", "#e3f0dc"),
    "E": (700, 450, "lichaamstemperatuur daalt", "#f2f2f2"),
}
for t, (x, y, txt, kl) in blokken.items():
    FB.rect(x, y, 190, 80, kl, DONKER, 12, 2)
    woorden = txt.split(" ")
    if len(txt) > 18:
        h = len(woorden) // 2
        FB.tekst(x + 95, y + 36, " ".join(woorden[:h]), 16)
        FB.tekst(x + 95, y + 58, " ".join(woorden[h:]), 16)
    else:
        FB.tekst(x + 95, y + 46, txt, 16)
    FB.letter(x + 190, y, t)
FB.pijl(212, 310, 268, 310, DONKER, 3)
FB.pijl(460, 300, 510, 222, BLAUW, 3)
FB.pijl(660, 220, 720, 270, ORANJE, 3)
FB.pijl(795, 350, 795, 450, DONKER, 3)
FB.pad("M 700 490 C 330 570 300 470 330 352", "none", ROOD, 3)
FB.tekst(400, 545, "−", 40, kleur=ROOD, vet=True)
U = "feedback-temperatuur.svg"
Z = {t: Prent.zone(x - 10, y - 20, 230, 110) for t, (x, y, txt, kl) in blokken.items()}
Z["min"] = Prent.zone(300, 480, 260, 90)

VRAGEN = [
    klik("Klik op de receptoren in dit feedbacksysteem.", U, [Z["B"]],
         "De warmtereceptoren in de huid vangen de prikkel op."),
    klik("Klik op het controlecentrum, dat de gemeten waarde vergelijkt met de normwaarde.", U, [Z["C"]],
         "De hersenen vergelijken en beslissen."),
    klik("Klik op de effectoren die de reactie uitvoeren.", U, [Z["D"]],
         "Zweetklieren en bloedvaten voeren de reactie uit."),
    klik("Klik op de pijl die toont dat het om negatieve feedback gaat.", U, [Z["min"]],
         "Het minteken: de reactie werkt de verandering tegen."),
    volgorde("Zet de stappen van een feedbacksysteem in de juiste volgorde.",
             ["prikkel", "receptor", "conductor", "controlecentrum", "effector", "reactie"],
             "De prikkel wordt opgevangen, doorgegeven, vergeleken en beantwoord."),
    casus("Na een stevige maaltijd stijgt het glucosegehalte in het bloed van Ella. Een paar uur later, na het sporten, daalt het onder de normwaarde.", [
        tabel("Welk hormoon werkt op welk moment?",
              [("na de maaltijd", "insuline"), ("na het sporten", "glucagon"), ("bij het ontbijt na een lange nacht zonder eten, vóór je eet", "glucagon")],
              "Insuline doet het gehalte dalen, glucagon doet het stijgen.", ["insuline", "glucagon"]),
        tabel("Wat doet de lever?",
              [("na de maaltijd slaat ze glucose op als glycogeen", J), ("na het sporten breekt ze glycogeen af tot glucose", J), ("ze maakt zelf insuline", F)],
              "De alvleesklier maakt de hormonen, de lever voert uit."),
        mk("Waarom is dit negatieve feedback?",
           ["Het gehalte keert terug.", "De reactie versterkt nog de stijging.", "Het gehalte blijft altijd stijgen.", "Er is geen normwaarde."], 0,
           "Het lichaam werkt de afwijking tegen."),
    ]),
    sorteer("Negatieve of positieve feedback?", ["negatief", "positief"],
            [("zweten als je het te warm hebt", "negatief"), ("stolling die nog meer stolling uitlokt", "positief"), ("insuline na een maaltijd", "negatief"), ("rillen als je het koud hebt", "negatief"), ("weeën die steeds sterker worden bij de geboorte", "positief")],
            "Negatief werkt tegen, positief versterkt."),
    tabel("Wat doet je lichaam als je het te koud hebt?",
          [("de bloedvaten in de huid vernauwen", J), ("je spieren rillen", J), ("je zweetklieren geven meer zweet af", F), ("je kippenvel komt op", J)],
          "Minder warmteverlies en meer warmteproductie."),
    koppel("Welke rol hoort bij welk onderdeel?",
           [("receptor", "vangt de prikkel op"), ("conductor", "geeft het signaal door"), ("controlecentrum", "vergelijkt met de normwaarde"), ("effector", "voert de reactie uit")],
           ["normwaarde"], "Elk onderdeel van het systeem heeft zijn taak."),
    tabel("Klopt dit over de signaaloverdracht?",
          [("Een zenuwsignaal gaat snel via zenuwbanen.", J), ("Een hormoon gaat trager via het bloed.", J), ("Een hormoon bereikt enkel het orgaan naast de klier.", F)],
          "Zenuwen werken snel en gericht, hormonen trager en verspreid."),
    casus("Bij Jonas met diabetes type 1 maakt de alvleesklier geen insuline meer.", [
        mk("Wat loopt er mis in het feedbacksysteem?",
           ["Het signaal valt weg.", "De lever maakt te veel insuline.", "De normwaarde verdwijnt.", "De receptoren worden blind."], 0,
           "Zonder insuline krijgt de lever het bericht om glucose op te slaan niet."),
        tabel("Klopt dit over Jonas?",
              [("Zijn glucosegehalte blijft na een maaltijd te hoog.", J), ("Hij kan insuline toegediend krijgen.", J), ("Hij heeft vooral te weinig glucagon.", F)],
              "Insuline vervangt het ontbrekende signaal."),
    ]),
    tabel("Klopt dit over homeostase?",
          [("Het lichaam houdt zijn inwendige milieu binnen nauwe grenzen.", J), ("Cellen werken enkel binnen een smalle temperatuurzone goed.", J), ("Een feedbacksysteem start pas als alles volledig ontregeld is.", F)],
          "Kleine afwijkingen worden meteen bijgestuurd."),
    sleep("Bij warmte [[verwijden]] de bloedvaten in de huid en geven de zweetklieren zweet af. Het zweet [[verdampt]] en neemt daarbij [[warmte]] op.",
          ["vernauwen", "condenseert"], "Zo koelt je lichaam af."),
    mk("Op een schema loopt een pijl met een minteken van een klier terug naar de hersenen. Wat betekent die?",
       ["Het hormoon remt de hersenen af.", "Het hormoon versterkt de hersenen.", "De klier stuurt geen signaal meer.", "De hersenen sturen de klier aan."], 0,
       "Een minteken toont afremmen."),
    tabel("Klopt dit over stress?",
          [("Je hartritme versnelt.", J), ("Je spieren krijgen meer zuurstof en glucose.", J), ("Je hartritme vertraagt om energie te sparen.", F)],
          "Stress maakt je lichaam klaar om te reageren."),
    keuze("Een plant die te veel water dreigt te verliezen, [[*sluit|opent|verwijdert]] haar huidmondjes.",
          "Ook planten houden hun waterhuishouding in evenwicht."),
    inv("De normwaarde van je lichaamstemperatuur is ongeveer 37 °C. Na het sporten meet je 38,5 °C. Hoeveel graden ligt dat boven de normwaarde?", ["1,5", "1.5", "1,5 °C"],
        "38,5 − 37 = 1,5 °C: je lichaam gaat zweten om af te koelen."),
    tabel("Is dit een effector?",
          [("de zweetklieren", J), ("de spiertjes in de wand van een bloedvat", J), ("de alvleesklier", J), ("de warmtereceptoren in de huid", F)],
          "Effectoren zijn spieren en klieren; receptoren vangen op."),
    mk("Waar zitten de receptoren die meten of je bloeddruk goed is?",
       ["in de wand van grote bloedvaten", "in de zweetklieren van de huid", "in de lever, naast de gal", "in de spieren van je benen en armen"], 0,
       "Ze geven de gemeten druk door aan de hersenen."),
    keuze("Een prikkel is elke verandering in het [[*inwendige of uitwendige|enkel uitwendige|enkel inwendige]] milieu.",
          "Ook een dalend glucosegehalte is een prikkel."),
    klik("Klik op de prikkel die het hele systeem in gang zet.", U, [Z["A"]],
         "Een warmere omgeving is de prikkel."),
    klik("Klik op het gevolg dat via de terugkoppeling weer bij de receptoren uitkomt.", U, [Z["E"]],
         "De dalende temperatuur wordt opnieuw gemeten: zo sluit de kring."),
    tabel("Welke organen spelen mee in de regeling van de glucosespiegel?",
          [("de alvleesklier", J), ("de lever", J), ("de zweetklieren", F), ("het bloed als transport", J)],
          "De alvleesklier maakt de hormonen, het bloed vervoert ze, de lever slaat op of geeft vrij."),
    inv("Je lichaam probeert een temperatuur van 37 °C aan te houden. Hoe noem je die waarde in een feedbacksysteem?", ["normwaarde", "de normwaarde"],
        "De normwaarde: het controlecentrum vergelijkt elke meting ermee."),
    sorteer("Doet dit het glucosegehalte in je bloed stijgen of dalen?", ["stijgen", "dalen"],
            [("een maaltijd met veel suiker", "stijgen"), ("insuline", "dalen"), ("glucagon", "stijgen"), ("een uur hard sporten", "dalen")],
            "Eten en glucagon verhogen, insuline en inspanning verlagen."),
    mk("Waarom heeft een organisme biologische feedback nodig?",
       ["zijn cellen werken binnen nauwe grenzen", "zo groeit het sneller dan andere organismen", "zo verbruikt het helemaal geen energie meer", "anders heeft het geen hormonen"], 0,
       "Temperatuur, water en glucose moeten binnen grenzen blijven."),
    tabel("Klopt dit over positieve feedback?",
          [("Het gevolg versterkt de oorzaak.", J), ("Ze komt voor bij bloedstolling.", J), ("Ze houdt je temperatuur constant.", F)],
          "Positieve feedback eindigt pas als de taak af is."),
]
