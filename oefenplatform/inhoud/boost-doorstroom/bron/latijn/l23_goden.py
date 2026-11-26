# -*- coding: utf-8 -*-
from _basis import *

TITEL = "Lectuur: leven met de goden, godsdienst en tolerantie in Rome"
BRON = ("Een eigen tekst van Connectopia over het thema van de lectuuropdracht (godsdienst en tolerantie in de Romeinse wereld). Gebaseerd op: Caesar, De bello Gallico VI, 17 (interpretatio Romana); Livius XXXIX, 8-19 (de Bacchanalia); "
        "Plinius, Epistulae X, 96-97; Tacitus, Annales XV, 44 (Nero en de christenen); het edict van Milaan (313). Wil je meer lezen, dan is Leven met de goden van Inger Kuin uit de vakfiche een goede volgende stap.")
INLEIDING = "Deze tekst is geen Latijn. Hij helpt je bij de lectuuropdracht over godsdienst en tolerantie. Lees hem rustig en beantwoord dan de vragen."
ALINEAS = [
    "Een godsdienst van doen, niet van geloven",
    "Voor een Romein ging godsdienst minder over wat je geloofde en meer over wat je deed. Je bracht offers, sprak de juiste gebeden uit en vierde de feesten op de juiste dag. Zo hield je de pax deorum in stand, de vrede met de goden. Ging het slecht, met een nederlaag of een epidemie, dan dacht men dat er iets misgelopen was in die verhouding, en zocht men naar de fout in de rituelen.",
    "Godsdienst was ook een zaak van de staat. Priesters waren vaak politici, en de belangrijkste priester, de pontifex maximus, was een publiek ambt. Caesar zelf werd in 63 voor Christus tot pontifex maximus verkozen. Thuis vereerde elke familie haar eigen huisgoden: de Lares en de Penates, die het huis en de voorraad beschermden.",
    "Ruimte voor andere goden",
    "De Romeinen waren in veel opzichten verdraagzaam. Veroverden ze een volk, dan namen ze vaak diens goden op. Ze gingen ervan uit dat andere volken dezelfde goden vereerden onder andere namen. Caesar doet dat ook: als hij de Gallische goden beschrijft, noemt hij ze Mercurius, Apollo en Mars. Dat heet de interpretatio Romana. Zo kwamen in de loop der eeuwen ook goden uit het oosten naar Rome, zoals de Egyptische Isis en de Perzische Mithras.",
    "Waar de verdraagzaamheid ophield",
    "Toch had die tolerantie grenzen. Wat de Romeinen wantrouwden, waren groepen die in het geheim samenkwamen en zich afzonderden van de gemeenschap. In 186 voor Christus liet de senaat de Bacchanalia, nachtelijke feesten voor de god Bacchus, hard aanpakken, omdat men er misdaden en een samenzwering achter vermoedde. Wat niet bij de oude gebruiken hoorde en volgens hen te ver ging, noemden ze superstitio, bijgeloof.",
    "Met de christenen lag het nog moeilijker. Zij weigerden te offeren aan de goden en aan de keizer. Voor de Romeinen was dat geen privézaak: wie de goden verwaarloosde, bracht de vrede met de goden en dus de hele staat in gevaar. Na de grote brand van Rome in 64 na Christus liet keizer Nero christenen terechtstellen als zondebok. Rond 112 vroeg Plinius aan keizer Trajanus hoe hij met hen moest omgaan. Vervolgingen kwamen en gingen, tot keizer Constantijn in 313 met het edict van Milaan alle godsdiensten, ook het christendom, vrij liet. Later, in 380, werd het christendom de staatsgodsdienst.",
]
WOORDEN = Wl(
    ("pax deorum", "de vrede met de goden, de goede verhouding tussen goden en mensen"),
    ("pontifex maximus", "de opperpriester van Rome"),
    ("Lares", "de beschermgoden van het huis en de familie"),
    ("Penates", "de goden van de voorraadkast en het gezin"),
    ("interpretatio Romana", "andere goden een Romeinse naam geven"),
    ("Bacchanalia", "geheime nachtelijke feesten voor Bacchus, de god van de wijn"),
    ("superstitio", "bijgeloof, overdreven of vreemde godsdienst"),
    ("edict van Milaan", "een besluit van 313 dat godsdienstvrijheid gaf"),
)
VRAGEN = [
    mk("Wat was voor een Romein het belangrijkste in de godsdienst?",
       ["de juiste rituelen uitvoeren", "een persoonlijk geloof hebben", "de heilige boeken lezen", "een priester worden"], 0,
       "Godsdienst draaide om doen: offers, gebeden en feesten op de juiste manier."),
    mk("Wat betekent pax deorum?",
       ["de vrede met de goden", "de oorlog tussen de goden", "de tempel van de vrede", "het feest van de goden"], 0,
       "Als de vrede met de goden goed zat, ging het goed met de staat. Ging het slecht, dan zocht men een fout in de rituelen."),
    keuze("De Lares en de Penates waren de goden van [[*het huis en de familie|de oorlog|de zee]]. De pontifex maximus was [[*de opperpriester van Rome|de leider van het leger|de koning van Rome]].",
          "Caesar werd in 63 voor Christus pontifex maximus. Godsdienst en politiek gingen in Rome hand in hand."),
    mk("Wat is de interpretatio Romana?",
       ["vreemde goden Romeins noemen", "de Romeinse goden afschaffen", "de Bijbel vertalen in het Latijn", "een tempel bouwen voor elke god"], 0,
       "Caesar noemt de Gallische goden Mercurius, Apollo en Mars. De Romeinen dachten dat andere volken dezelfde goden vereerden onder andere namen."),
    tabel("Welke goden kwamen van buitenaf naar Rome?",
          [("Isis uit Egypte", J),
           ("Mithras uit Perzië", J),
           ("Iuppiter uit Gallië", F),
           ("Mars uit Germanië", F)],
          "Iuppiter en Mars zijn oude Romeinse goden. Isis en Mithras kwamen uit het oosten."),
    mk("Waarom liet de senaat de Bacchanalia aanpakken?",
       ["men vreesde een samenzwering", "Bacchus was een vijandige god", "de feesten waren te duur", "de christenen vierden ze"], 0,
       "Geheime nachtelijke bijeenkomsten maakten de Romeinen wantrouwig. In 186 voor Christus greep de senaat hard in."),
    mk("Waarom was het weigeren van offers voor Romeinen zo erg?",
       ["het bracht de vrede met de goden in gevaar", "het kostte de staat veel geld", "het was een belediging voor de priesters", "het was verboden door de senaat"], 0,
       "Wie de goden verwaarloosde, bracht volgens de Romeinen de hele gemeenschap in gevaar. Godsdienst was een zaak van iedereen."),
    volgorde("Zet de gebeurtenissen in de juiste volgorde.",
             ["de senaat treedt op tegen de Bacchanalia",
              "Caesar wordt pontifex maximus",
              "Nero laat christenen terechtstellen na de brand van Rome",
              "Plinius schrijft aan Trajanus over de christenen",
              "het edict van Milaan geeft godsdienstvrijheid"],
             "186 voor Christus, 63 voor Christus, 64 na Christus, rond 112 na Christus, 313 na Christus."),
    tabel("Klopt dit over de tolerantie van de Romeinen?",
          [("Ze namen vaak de goden van veroverde volken op.", J),
           ("Geheime groepen maakten hen wantrouwig.", J),
           ("Ze lieten elke godsdienst altijd volledig vrij.", F),
           ("Het christendom werd al in de tijd van Caesar de staatsgodsdienst.", F)],
          "De tolerantie had grenzen. Het christendom werd pas in 380 na Christus de staatsgodsdienst."),
    open_("Waarom waren de Romeinen verdraagzaam tegenover de goden van Isis en Mithras, maar niet tegenover de christenen? Leg uit.",
          "Isis en Mithras konden naast de Romeinse goden vereerd worden: wie ze vereerde, bleef ook offeren aan de Romeinse goden en de keizer. De christenen weigerden dat, want zij geloofden in één God. Voor de Romeinen bracht dat de vrede met de goden en dus de staat in gevaar.",
          "Gebruik het idee van de pax deorum en het weigeren van offers."),
]
