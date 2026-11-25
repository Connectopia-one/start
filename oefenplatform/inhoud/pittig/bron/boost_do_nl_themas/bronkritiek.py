"""Bronnen wegen: objectief, gekleurd of nep — pittig (🚀 Boost doorstroom, Nederlands).

Eigen teksten en vragen strikt binnen nl_bronkritiek, met een zelfgetekend
verdacht bericht op sociale media."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL

NB = Prent("verdacht-bericht", "Een bericht op sociale media", "een gedeeld bericht met een kop in hoofdletters, een foto, een korte tekst en een oproep om te delen, met letters A tot E")
NB.rect(200, 55, 600, 545, "white", DONKER, 22, 3)
NB.cirkel(250, 95, 26, "#ccc", DONKER, 2); NB.tekst(290, 90, "Iemand deelde dit", 22, "start", GRIJS); NB.tekst(290, 116, "Gedeeld bericht", 18, "start", GRIJS)
NB.tekst(500, 175, "SCHANDALIG!!! SCHOLEN", 30, "middle", ROOD, True); NB.tekst(500, 212, "VERBIEDEN BROODDOZEN", 30, "middle", ROOD, True)
NB.rect(240, 235, 520, 170, "#dde7ef", DONKER, 10, 2); NB.tekst(500, 328, "(foto van een lege refter)", 20, "middle", GRIJS)
NB.tekst(500, 440, "Vanaf volgende week moet elk kind", 22); NB.tekst(500, 468, "dure warme maaltijden kopen.", 22)
NB.tekst(500, 500, "De media zwijgen erover!", 22)
NB.rect(240, 525, 520, 50, "#ffe8e8", ROOD, 12, 2); NB.tekst(500, 558, "DEEL DIT VOOR HET VERWIJDERD WORDT!", 19, "middle", ROOD, True)
LET = {"A": (150, 100), "B": (150, 195), "C": (850, 320), "D": (150, 500), "E": (850, 550)}
for t, (x, y) in LET.items():
    NB.letter(x, y, t)
NB.lijn(172, 100, 222, 100, DONKER, 1); NB.lijn(172, 195, 260, 190, DONKER, 1); NB.lijn(828, 320, 762, 320, DONKER, 1); NB.lijn(172, 500, 300, 495, DONKER, 1); NB.lijn(828, 550, 762, 550, DONKER, 1)
U = "verdacht-bericht.svg"
Z = {t: Prent.rond(x, y, 32) for t, (x, y) in LET.items()}

VRAGEN = [
    klik("Bekijk het bericht. Klik op de letter bij het deel waaruit blijkt dat je de zender niet kent.", U, [Z["A"]],
         "Zonder zender kan je deskundigheid, bedoeling en belang niet wegen."),
    klik("Klik op de letter bij de kop met een waardewoord en uitroeptekens.", U, [Z["B"]],
         "Waardewoorden en uitroeptekens verraden een oordeel."),
    klik("Klik op de letter bij de oproep die het bericht snel wil laten verspreiden.", U, [Z["E"]],
         "Nepnieuws leunt op snelle verspreiding via sociale media."),
    casus("Hetzelfde bericht als op de prent: 'SCHANDALIG!!! Scholen verbieden brooddozen. Vanaf volgende week moet elk kind dure warme maaltijden kopen. De media zwijgen erover! Deel dit voor het verwijderd wordt!'", [
        tabel("Is dit een signaal dat het bericht nepnieuws kan zijn?",
              [("er staat geen auteur bij", J), ("er staat geen datum of bron bij", J), ("het circuleert enkel via sociale media", J), ("de kop is in hoofdletters", J), ("er staat een foto bij", F)],
              "Een foto bewijst niets: hij kan overal vandaan komen."),
        mk("Wat doe je best voor je dit bericht deelt?",
           ["nagaan of een betrouwbare bron het meldt", "het meteen delen, want het is erg dringend", "de foto groter maken om beter te kunnen kijken", "tellen hoeveel mensen het al deelden"],
           0, "Kijk of andere, betrouwbare bronnen het melden."),
    ]),
    tabel("Helpt deze vraag je de betrouwbaarheid van een tekst te beoordelen?",
          [("Wie is de zender?", J), ("Is de zender deskundig in dit onderwerp?", J), ("Hoeveel tussentitels heeft de tekst?", F), ("Is de informatie nog actueel?", J)],
          "Het aantal tussentitels zegt niets over betrouwbaarheid."),
    tabel("Klopt dit over betrouwbaarheid?",
          [("Een tekst van een deskundige is altijd objectief.", F), ("Zodra een tekst bronnen vermeldt, is hij betrouwbaar.", F), ("Veel spelfouten zijn een waarschuwingslicht.", J), ("Een deskundige kan ook een belang hebben.", J)],
          "Bronnen moet je ook zelf wegen."),
    mk("Een onderzoek over de gezondheid van energiedranken werd betaald door een fabrikant van energiedranken. Wat doe je?",
       ["extra kritisch lezen", "het onderzoek meteen weggooien", "het blindelings geloven", "enkel de titel lezen"],
       0, "De opdrachtgever kan belang hebben bij de uitkomst. Dat maakt het niet meteen waardeloos."),
    mk("Een artikel over de regels voor bromfietsen dateert van 2012. Waarom ben je voorzichtig?",
       ["de regels kunnen intussen veranderd zijn", "artikels uit 2012 zijn altijd nepnieuws", "er staan te weinig foto's bij", "het is te lang geleden geschreven om te lezen"],
       0, "Wetgeving verouderd snel."),
    mk("Waarom weegt een krantenartikel meestal zwaarder dan een doorgestuurd bericht in een groepschat?",
       ["het passeerde een redactie", "het is altijd langer", "het staat op papier", "kranten schrijven nooit fouten"],
       0, "Sommige kanalen hebben redactionele controle, andere niet."),
    sorteer("Hoe doet deze tekst zich voor?", ["publireportage", "satire", "nepnieuws"],
            [("een 'artikel' over een nieuwe gsm, betaald door het merk", "publireportage"), ("een grappig verzonnen nieuwsbericht op een bekende humorsite", "satire"), ("een verzonnen bericht zonder bron dat via sociale media rondgaat", "nepnieuws")],
            "Ze lenen allemaal de vorm van iets anders."),
    tabel("Klopt dit over satire en propaganda?",
          [("Satire wil je misleiden.", F), ("Propaganda toont met opzet maar één kant.", J), ("Satire wil iets aan de kaak stellen.", J)],
          "Het misverstand ontstaat als je satire los van zijn bron leest."),
    mk("Een influencer prijst een shampoo zonder te zeggen dat hij ervoor betaald wordt. Welk criterium kan je niet toepassen?",
       ["de bedoeling van de zender", "de actualiteit van de tekst", "de spelling van de tekst", "het aantal volgers van de zender"],
       0, "Je denkt een eerlijke mening te lezen terwijl het reclame is."),
    casus("Twee krantenkoppen over dezelfde betoging:\n\nKrant 1: 'Vijfduizend jongeren eisen betere fietspaden'\nKrant 2: 'Betoging legt spitsverkeer urenlang lam'", [
        tabel("Klopt dit over de twee krantenkoppen?",
              [("Allebei kunnen ze kloppen.", J), ("Eén van de twee kranten moet liegen.", F), ("Ze kiezen een andere invalshoek.", J)],
              "Framing werkt net omdat alles waar kan zijn."),
        inv("Hoe noem je het kiezen van een invalshoek die de lezer in een richting duwt? Eén woord.", ["framing"], "Framing."),
        keuze("Krant 2 zet vooral [[*de hinder|de eisen|het aantal jongeren]] in de kijker.", "Dezelfde feiten, een ander kader."),
    ]),
    koppel("Koppel het eufemisme aan wat er eigenlijk bedoeld wordt.",
           [("prijsaanpassing", "prijsverhoging"), ("herstructurering", "ontslagen"), ("heengaan", "sterven")],
           ["korting"],
           "Een eufemisme is een verzachtend woord voor iets onaangenaams."),
    sorteer("Welke gevoelswaarde heeft het woord?", ["positiever", "negatiever"],
            [("voordelig", "positiever"), ("goedkoop", "negatiever"), ("overheidsuitgaven", "positiever"), ("belastinggeld verkwisten", "negatiever")],
            "Die gevoelswaarde heet de connotatie."),
    tabel("Is dit een talig middel om subjectiviteit uit te drukken?",
          [("beeldspraak", J), ("overdrijving", J), ("modaliteit", J), ("de bladspiegel", F)],
          "De bladspiegel is vormgeving."),
    keuze("In 'Zwijg eens even!' maakt het woordje 'eens' het bevel [[*zachter|harder|langer]].", "Zulke woordjes heten modale partikels."),
    mk("'Een golf van klachten overspoelde de dienst.' Wat doet die beeldspraak?",
       ["ze laat de klachten voelen als een ramp", "ze geeft het precieze aantal klachten weer", "ze maakt de tekst een stuk objectiever", "ze noemt de bron van alle klachten"],
       0, "Beeldspraak brengt subjectiviteit binnen."),
    mk("Twee betrouwbare bronnen geven een ander cijfer over hetzelfde onderwerp. Wat doe je?",
       ["vergelijken hoe ze aan hun cijfers komen", "het hoogste cijfer kiezen", "allebei negeren", "het cijfer kiezen dat jou het best uitkomt"],
       0, "Vaak meten ze iets anders of over een andere periode."),
    keuze("Een recensie eindigt met: 'Een meesterwerk, als je van drie uur stilstaande beelden houdt.' De schrijver is [[*ironisch|objectief|deskundig]].", "Hij bedoelt het omgekeerde: een dubbele bodem."),
    tabel("Betrouwbaar, correct of bruikbaar?",
          [("de tekst geeft een antwoord op jouw vraag", "bruikbaar"), ("de feiten in de tekst kloppen", "correct"), ("de zender is deskundig en eerlijk over zijn belang", "betrouwbaar")],
          "Drie verschillende dingen.", ["betrouwbaar", "correct", "bruikbaar"]),
    mk("Een frisdrankmerk schrijft een lange tekst over 'bewust bewegen'. Waarop let je vooral?",
       ["wat er niet in staat over suiker", "hoe lang de tekst precies is", "of er mooie foto's bij de tekst staan", "of de tekst duidelijke tussentitels heeft"],
       0, "Wat de zender weglaat, verraadt zijn doel."),
    inv("Hoe noem je een verzachtend woord voor iets onaangenaams? Eén woord.", ["eufemisme", "een eufemisme"], "Een eufemisme, zoals heengaan voor sterven."),
    keuze("Een eenzijdige, meestal politieke tekst die met opzet één kant toont, heet [[*propaganda|satire|een recensie]].", "Propaganda wil beïnvloeden, niet informeren."),
    keuze("Een verborgen betekenis onder de letterlijke tekst noem je een [[*dubbele bodem|eufemisme|connotatie]].", "Wie hem mist, leest ironie letterlijk."),
    tabel("Kleurt dit woord een krantenkop?",
          [("eindelijk", J), ("zogenaamd", J), ("dinsdag", F), ("dramatisch", J)],
          "'Dinsdag' is een gegeven."),
    open_("Leg uit waarom framing geen liegen is, maar je toch kan sturen. Geef een voorbeeld.",
          "Bij framing kan alles wat er staat waar zijn. De schrijver kiest wel welke feiten hij belicht en met welke woorden. Een betoging kan 'duizenden op straat voor het klimaat' of 'verkeerschaos in het centrum' heten."),
]
