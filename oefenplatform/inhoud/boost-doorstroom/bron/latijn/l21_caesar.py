# -*- coding: utf-8 -*-
from _basis import *

TITEL = "Lectuur: de jonge Caesar en de weg naar Gallië"
BRON = ("Een eigen tekst van Connectopia over het thema van de lectuuropdracht (Caesars jeugd en loopbaan). Gebaseerd op: Suetonius, Divus Iulius 1-24; Plutarchus, Caesar 1-14; Caesar, De bello Gallico I, 1-2. "
        "Wil je meer lezen, dan is de biografie Caesar van Adrian Goldsworthy uit de leeslijst van de Examencommissie een goede volgende stap.")
INLEIDING = "Deze tekst is geen Latijn. Hij helpt je bij de lectuuropdracht over Caesar. Lees hem rustig en beantwoord dan de vragen."
ALINEAS = [
    "Een jongen uit een oude familie",
    "Gaius Julius Caesar werd geboren in 100 voor Christus in Rome. Zijn familie, de Iulii, was heel oud en beweerde zelfs af te stammen van de godin Venus, via Aeneas en diens zoon Iulus. Rijk waren ze niet meer, en machtig evenmin. Wie in Rome iets wilde bereiken, moest een politieke loopbaan uitbouwen: de cursus honorum, de ladder van ambten, van quaestor tot consul.",
    "Toen Caesar jong was, woedde er een burgeroorlog. De dictator Sulla liet tegenstanders vermoorden. Caesar was getrouwd met de dochter van een van Sulla's vijanden en weigerde te scheiden. Hij moest onderduiken en kreeg pas genade na tussenkomst van invloedrijke familieleden. Volgens Suetonius zei Sulla toen dat er in die jongen vele Mariussen schuilden: hij zag gevaar in hem.",
    "Ontvoerd door piraten",
    "Op weg naar het eiland Rhodos, waar hij redenaarskunst wilde studeren, werd Caesar door piraten gevangengenomen. Ze vroegen een losgeld van twintig talenten. Caesar lachte en zei dat hij er minstens vijftig waard was. Tijdens zijn gevangenschap gedroeg hij zich alsof hij de baas was: hij las hun zijn gedichten voor en dreigde dat hij hen zou laten kruisigen. Toen het losgeld betaald was, verzamelde hij schepen, ving de piraten en liet hen inderdaad terechtstellen. Het verhaal toont wat hij later altijd zou laten zien: zelfvertrouwen, durf en snelheid.",
    "Schulden, populariteit en een verbond",
    "Caesar klom de ladder van ambten op. Als aedilis organiseerde hij prachtige spelen, waarvoor hij enorme schulden maakte. Zo won hij de gunst van het volk. In 60 voor Christus sloot hij een geheim verbond met twee machtige mannen: de veldheer Pompeius en de schatrijke Crassus. Dat verbond heet het eerste triumviraat. Dankzij hun steun werd Caesar consul in 59 voor Christus.",
    "Proconsul in Gallië",
    "Na zijn consulaat kreeg Caesar het bestuur over provincies in Gallië, eerst voor vijf jaar, later verlengd. Voor hem was dat een kans: met een oorlog kon hij roem, buit en een trouw leger verwerven, en zijn schulden afbetalen. In 58 voor Christus trokken de Helvetii door Gallië. Caesar greep in, en dat werd het begin van een oorlog die acht jaar zou duren. Hij beschreef die zelf in De bello Gallico, in de derde persoon, in een heldere en schijnbaar zakelijke stijl. Maar elk woord was ook bedoeld voor de lezers in Rome: zo bleef hij in de belangstelling, ook ver weg van de stad.",
]
WOORDEN = Wl(
    ("cursus honorum", "de vaste reeks politieke ambten in Rome"),
    ("talenten", "het talent was een grote hoeveelheid zilver, een enorme som geld"),
    ("aedilis", "een ambtenaar die onder meer de openbare spelen regelde"),
    ("triumviraat", "een verbond van drie mannen (tres viri)"),
    ("Proconsul", "een gewezen consul die een provincie bestuurt"),
)
VRAGEN = [
    mk("Van welke godin zou de familie van Caesar afstammen?",
       ["Venus", "Minerva", "Iuno", "Diana"], 0,
       "Via Aeneas, de zoon van Venus, en diens zoon Iulus. Daarom heette de familie de Iulii."),
    mk("Waarom moest de jonge Caesar onderduiken?",
       ["hij weigerde te scheiden", "hij had een senator gedood", "hij was gevlucht uit het leger", "hij had schulden bij Sulla"], 0,
       "Zijn vrouw was de dochter van een vijand van Sulla. Caesar weigerde van haar te scheiden en moest vluchten."),
    tabel("Klopt dit over het piratenverhaal?",
          [("Caesar vond het losgeld te laag.", J),
           ("Hij liet de piraten later terechtstellen.", J),
           ("Caesar ontsnapte door de piraten om te kopen.", F),
           ("De piraten lieten hem gratis gaan.", F)],
          "Caesar zei dat hij minstens vijftig talenten waard was. Na zijn vrijlating ving hij de piraten en liet hen kruisigen, zoals hij had gedreigd."),
    mk("Hoe won Caesar als aedilis de gunst van het volk?",
       ["met prachtige spelen", "met lagere belastingen", "met nieuwe wetten", "met een overwinning"], 0,
       "Hij organiseerde dure spelen en maakte daar grote schulden voor. Populariteit was in Rome belangrijk om verkozen te worden."),
    koppel("Koppel de persoon aan de omschrijving.",
           [["Sulla", "dictator die tegenstanders liet vermoorden"],
            ["Pompeius", "veldheer in het eerste triumviraat"],
            ["Crassus", "schatrijke man in het eerste triumviraat"],
            ["Iulus", "zoon van Aeneas, stamvader van de Iulii"]],
           ["koning van de Eburonen"],
           "Het eerste triumviraat (60 voor Christus) was een verbond van Caesar, Pompeius en Crassus. Ambiorix was de koning van de Eburonen."),
    mk("In welk jaar was Caesar consul?",
       ["59 voor Christus", "100 voor Christus", "44 voor Christus", "58 na Christus"], 0,
       "Caesar was consul in 59 voor Christus. In 100 voor Christus werd hij geboren. In 58 begon de Gallische Oorlog."),
    tabel("Waarom was de oorlog in Gallië een kans voor Caesar?",
          [("Hij kon roem winnen.", J),
           ("Hij kon met de buit zijn schulden betalen.", J),
           ("Hij kon zo consul worden.", F),
           ("Hij wilde de Galliërs leren lezen.", F)],
          "Caesar was al consul geweest. De oorlog bracht roem, buit en een leger dat trouw was aan hem persoonlijk."),
    mk("Welk volk zorgde in 58 voor Christus voor het begin van de oorlog?",
       ["de Helvetii", "de Belgae", "de Germanen", "de Britten"], 0,
       "De Helvetii wilden door Gallië trekken. Caesar greep in, en dat was het begin van de Gallische Oorlog."),
    keuze("Caesar schrijft De bello Gallico in de [[*derde persoon|eerste persoon|tweede persoon]]. Zo lijkt zijn verslag [[*objectief|grappig|poëtisch]], terwijl het ook reclame is voor hemzelf.",
          "Door over zichzelf te schrijven als Caesar, en niet als ik, klinkt het verslag als een neutraal verslag. Toch kiest hij zelf wat hij vertelt."),
    open_("Welke eigenschappen van Caesar zie je in het piratenverhaal, en waar komen ze later terug in zijn loopbaan?",
          "Zelfvertrouwen, durf en snelheid. Hij vindt zichzelf meer waard dan het losgeld en doet wat hij belooft. Later toont hij dezelfde durf als hij schulden maakt voor spelen, een verbond sluit met Pompeius en Crassus en een oorlog in Gallië begint om roem te winnen.",
          "Noem minstens twee eigenschappen en een voorbeeld uit zijn latere loopbaan."),
]
