# -*- coding: utf-8 -*-
from _basis import *

TITEL = "Lectuur: wonen en werken in Pompeii"
BRON = ("Een eigen tekst van Connectopia over het thema van de lectuuropdracht (huis en haard, en de economie van Pompeii). Gebaseerd op: Plinius, Epistulae VI, 16 en 20; Vitruvius, De architectura VI; Plinius de Oudere, Naturalis Historia XXXI, 93-95 (garum); "
        "en de opgravingen in Pompeii, zoals het huis van de bankier Lucius Caecilius Iucundus en de bakkerij van Modestus. Wil je meer lezen, dan is Pompeii van Mary Beard uit de leeslijst van de Examencommissie een goede volgende stap.")
INLEIDING = "Deze tekst is geen Latijn. Hij helpt je bij de lectuuropdracht over Pompeii. Lees hem rustig en beantwoord dan de vragen."
ALINEAS = [
    "Een stad die stilstond",
    "Toen de Vesuvius in 79 na Christus uitbarstte, verdween Pompeii onder een dikke laag as en puimsteen. Daardoor bleef de stad bewaard zoals ze op die dag was: met huizen, winkels, schilderingen en zelfs opschriften op de muren. Pas vanaf 1748 begon men de stad op te graven. Vandaag is ze een uniek venster op het dagelijkse leven van een Romeinse stad, al moet je oppassen: Pompeii was op dat moment al aan het herstellen van een zware aardbeving in 62 na Christus.",
    "Het huis: domus en insula",
    "Rijke families woonden in een domus. Langs de straat zag je weinig: een deur, en soms winkeltjes in de voorgevel die verhuurd werden. Binnen kwam je in het atrium, een hal met een opening in het dak. Daaronder stond een bekken, het impluvium, dat regenwater opving. Rond het atrium lagen kamers, en in het tablinum ontving de heer des huizes zijn cliënten. Verder naar achteren lag een tuin met zuilengang, het peristylium. Gewone mensen woonden in kleinere huizen of in appartementen boven winkels. In grote steden zoals Rome heetten zulke huurkazernes insulae.",
    "Het huis was niet alleen privé. 's Ochtends kwamen cliënten hun patronus begroeten, en er werden zaken gedaan. In het atrium stonden ook het altaartje voor de huisgoden, het lararium, en de kast met de wasmaskers van de voorouders. Het huis toonde wie je was.",
    "Bakkers, bankiers en vissaus",
    "Pompeii was een drukke handelsstad. Er waren tientallen bakkerijen met grote molens van lavasteen, die door ezels werden rondgedraaid. In de bakkerij van Modestus vond men zelfs verkoolde broden terug. De bankier Lucius Caecilius Iucundus bewaarde zijn rekeningen op wastafeltjes, die bij de opgravingen ontdekt werden: zo weten we hoe hij geld leende en veilingen regelde. Een beroemd product van de stad was garum, een sterke saus van gegiste vis. Eén producent, Aulus Umbricius Scaurus, liet zelfs mozaïeken met zijn garumpotten in zijn huis aanbrengen. Op de muren lees je verkiezingsaffiches, reclame en graffiti: Pompeii was een stad vol mensen die werkten, kochten, stemden en roddelden.",
]
WOORDEN = Wl(
    ("domus", "het huis van een rijke familie"),
    ("atrium", "de centrale hal van een Romeins huis"),
    ("impluvium", "het bekken dat regenwater opvangt in het atrium"),
    ("tablinum", "de ontvangstkamer van de heer des huizes"),
    ("peristylium", "een tuin met een zuilengang rondom"),
    ("insulae", "huurkazernes met appartementen"),
    ("patronus", "een machtige beschermheer"),
    ("lararium", "het huisaltaar voor de Lares"),
    ("garum", "een sterke saus van gegiste vis"),
)
VRAGEN = [
    mk("Waarom bleef Pompeii zo goed bewaard?",
       ["het lag onder een dikke laag as", "het werd nooit door mensen verlaten", "het lag op een berg", "het werd elk jaar hersteld"], 0,
       "De as en de puimsteen van de Vesuvius bedekten de stad in 79 na Christus. Pas vanaf 1748 werd ze opgegraven."),
    mk("Waarom moet je volgens de tekst oppassen als je Pompeii als voorbeeld gebruikt?",
       ["de stad was nog in herstelling", "de stad was helemaal niet Romeins", "er woonden enkel rijke mensen", "alles werd later nagebouwd"], 0,
       "In 62 na Christus was er een zware aardbeving. In 79 waren veel gebouwen nog in herstelling. Pompeii is dus een momentopname van een stad in verandering."),
    koppel("Koppel het deel van een domus aan de beschrijving.",
           [["atrium", "de centrale hal met een opening in het dak"],
            ["impluvium", "het bekken voor regenwater"],
            ["tablinum", "de ontvangstkamer van de heer des huizes"],
            ["peristylium", "de tuin met zuilengang"]],
           ["de keuken op het dak"],
           "Een Romeins huis was naar binnen gekeerd. Van de straat zag je weinig, binnen was het ruim en licht."),
    tabel("Klopt dit over een Romeinse domus?",
          [("Er waren soms winkeltjes in de voorgevel.", J),
           ("Cliënten kwamen 's ochtends hun patronus begroeten.", J),
           ("Het huis had grote ramen naar de straat.", F),
           ("Het huis was helemaal privé, niemand kwam binnen.", F)],
          "Het huis was ook een plaats om zaken te doen en je status te tonen. Ramen naar de straat waren klein of er waren er geen."),
    mk("Wat stond er in het lararium?",
       ["een altaartje voor de huisgoden", "de geldkist van de familie", "het bed van de heer des huizes", "de molen van de bakker"], 0,
       "Het lararium was het huisaltaar voor de Lares, de beschermgoden van het huis. Vergelijk met de godsdienst van doen."),
    mk("Hoe werden de molens in de bakkerijen rondgedraaid?",
       ["door ezels", "door water", "door de wind", "door stoom"], 0,
       "Grote molens van lavasteen werden door ezels of slaven rondgedraaid. In de bakkerij van Modestus vond men verkoolde broden."),
    mk("Hoe weten we hoe de bankier Iucundus werkte?",
       ["zijn wastafeltjes werden gevonden", "hij schreef een boek over zijn bank", "Plinius beschreef hem in een brief", "zijn standbeeld vertelt het"], 0,
       "Bij de opgravingen vond men de wastafeltjes van Lucius Caecilius Iucundus met zijn rekeningen en ontvangstbewijzen."),
    keuze("Garum is een saus van [[*gegiste vis|olijven|honing]]. De producent Umbricius Scaurus liet zijn garumpotten afbeelden in [[*mozaïeken|beelden|munten]].",
          "Garum was overal in het Romeinse rijk geliefd. Pompeii was er bekend om."),
    tabel("Wat lees je op de muren van Pompeii?",
          [("verkiezingsaffiches", J),
           ("reclame en graffiti", J),
           ("hele boeken van Vergilius", F),
           ("krantenberichten over de uitbarsting", F)],
          "De muren van Pompeii zitten vol opschriften: verkiezingsoproepen, reclame, liefdesboodschappen en scheldwoorden. Kranten bestonden niet."),
    open_("Welke bronnen gebruiken historici om het dagelijkse leven in Pompeii te kennen? Noem er drie uit de tekst en leg uit wat elk ons leert.",
          "De huizen zelf tonen hoe mensen woonden (atrium, peristylium). De wastafeltjes van Iucundus tonen hoe een bankier werkte. De bakkerijen met molens en broden tonen het werk van bakkers. De mozaïeken van Scaurus en de opschriften op de muren tonen handel, reclame en politiek. De brieven van Plinius vertellen over de uitbarsting.",
          "Noem drie verschillende soorten bronnen, bijvoorbeeld gebouwen, wastafeltjes, opschriften of de brieven van Plinius."),
]
