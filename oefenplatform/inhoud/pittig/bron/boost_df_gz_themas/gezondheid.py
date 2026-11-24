"""Gezondheid in kaart: Gordon en het ICF — pittig (🛠️ Boost dubbele finaliteit, gezondheidszorg en welzijn).

Eigen vragen strikt binnen gz_gezondheid, met een zelfgetekend leeg ICF-schema."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL

IC = Prent("icf-leeg", "Het ICF-schema zonder woorden", "de gezondheidstoestand in drie vakken bovenaan, met twee vakken eronder, met letters A tot E")
VAK = "#eef4ff"
for x in (110, 390, 670):
    IC.rect(x, 90, 220, 110, VAK, DONKER, 14, 2)
IC.rect(110, 380, 360, 110, "#fff4dc", DONKER, 14, 2)
IC.rect(530, 380, 360, 110, "#fff4dc", DONKER, 14, 2)
IC.lijn(330, 145, 390, 145, DONKER, 3); IC.lijn(610, 145, 670, 145, DONKER, 3)
IC.lijn(290, 380, 220, 200, DONKER, 3); IC.lijn(290, 380, 500, 200, DONKER, 3); IC.lijn(290, 380, 780, 200, DONKER, 3)
IC.lijn(710, 380, 220, 200, DONKER, 3); IC.lijn(710, 380, 500, 200, DONKER, 3); IC.lijn(710, 380, 780, 200, DONKER, 3)
LET = {"A": (220, 145), "B": (500, 145), "C": (780, 145), "D": (290, 435), "E": (710, 435)}
for t, (x, y) in LET.items():
    IC.letter(x, y, t)
U = "icf-leeg.svg"
Z = {t: Prent.rond(x, y, 40) for t, (x, y) in LET.items()}

VRAGEN = [
    klik("In dit schema staan de drie delen van de gezondheidstoestand bovenaan in deze volgorde: lichaam, doen, samen. Klik op het vak waar je noteert dat Mila niet meer zelf kan koken.", U, [Z["B"]],
         "Koken is een activiteit: dat is doen."),
    klik("Dezelfde volgorde bovenaan: lichaam, doen, samen. Klik op het vak waar je noteert dat Mila niet meer naar de turnclub kan.", U, [Z["C"]],
         "Meedoen aan vrije tijd en de maatschappij is samen."),
    klik("Dezelfde volgorde bovenaan: lichaam, doen, samen. Klik op het vak waar je noteert dat Mila's heup slecht werkt.", U, [Z["A"]],
         "De werking van het lichaam staat bij lichaam."),
    klik("Onderaan staat links het ik en rechts de omgeving. Klik op het vak waar Mila's huis met veel trappen komt.", U, [Z["E"]],
         "De woning ligt buiten de persoon: een externe factor."),
    klik("Onderaan staat links het ik en rechts de omgeving. Klik op het vak waar je noteert dat Mila 78 jaar is.", U, [Z["D"]],
         "Leeftijd is een persoonlijke factor."),
    sorteer("Onder welk patroon van Gordon valt deze vaststelling bij Jan?", ["voeding en stofwisseling", "uitscheiding", "slaap en rust"],
            [("Jan drinkt weinig water", "voeding en stofwisseling"), ("Jan heeft last van verstopping", "uitscheiding"), ("Jan ligt elke nacht lang wakker", "slaap en rust"), ("Jan zweet erg veel", "uitscheiding"), ("Jan slaat vaak het ontbijt over", "voeding en stofwisseling")],
            "Zweten hoort ook bij uitscheiding."),
    sorteer("Onder welk patroon van Gordon valt deze vaststelling bij Lien?", ["zelfbeleving", "rol en relatie", "stressverwerking"],
            [("Lien vindt zichzelf niets waard", "zelfbeleving"), ("Lien voelt zich buitengesloten in haar klas", "rol en relatie"), ("Lien raakt in paniek voor elke toets", "stressverwerking"), ("Lien is de oudste thuis en zorgt voor haar zusjes", "rol en relatie")],
            "Rol en relatie gaat over je plaats in gezin, school of groep."),
    koppel("Koppel het patroon aan waarover het gaat.",
           [("waarneming en cognitie", "zien, horen en onthouden"), ("activiteiten", "bewegen, werken en vrije tijd"), ("gezondheidsbeleving en instandhouding", "hoe iemand zijn eigen gezondheid ziet"), ("waarden en levensopvatting", "wat iemand belangrijk vindt in het leven")],
           ["winst en verlies"],
           "Winst en verlies hoort bij een boekhouding."),
    tabel("Is dit een patroon van Gordon?",
          [("seksualiteit en voortplanting", J), ("winst en verlies", F), ("slaap en rust", J), ("lengte en gewicht", F)],
          "Gordon heeft elf patronen, van gezondheidsbeleving tot waarden en levensopvatting."),
    mk("Tom slaapt al weken slecht. Op welk patroon zie je dat waarschijnlijk ook een gevolg?",
       ["activiteiten", "seksualiteit en voortplanting", "waarden en levensopvatting", "voeding en stofwisseling enkel"],
       0, "Wie te weinig slaapt, beweegt en onderneemt minder: de patronen hangen samen."),
    mk("Een zorgkundige noteert bij een bewoner enkel dat zijn been pijn doet. Wat loopt er mis?",
       ["ze kijkt niet naar het geheel van zijn functioneren", "ze moest eerst zelf een medische diagnose stellen", "pijn hoort bij geen enkel patroon van Gordon thuis", "ze had het ICF en Gordon helemaal niet mogen gebruiken"],
       0, "Met een vast schema mis je de rest van het functioneren niet."),
    keuze("Wie stelt een medische diagnose? [[*een arts|de zorgkundige met Gordon|het ICF-schema]]",
          "Gordon en het ICF brengen het functioneren in kaart, de diagnose stelt een arts."),
    volgorde("Zet de stappen van een systematische aanpak in de juiste volgorde.",
             ["het probleem benoemen", "een oplossing zoeken", "de oplossing uitvoeren"],
             "Eerst vaststellen wat er precies aan de hand is."),
    tabel("Klopt dit over een systematische aanpak?",
          [("Je vergeet minder.", J), ("Je werkt sneller.", J), ("Je hoeft niet meer goed te kijken.", F), ("Je kan uitleggen hoe je werkte.", J)],
          "Een vaste werkwijze vervangt het kijken niet."),
    sorteer("Persoonlijke factor of externe factor?", ["persoonlijke factor", "externe factor"],
            [("het karakter", "persoonlijke factor"), ("de woonplaats", "externe factor"), ("de leeftijd", "persoonlijke factor"), ("een behulpzame buur", "externe factor"), ("de opleiding die iemand volgde", "persoonlijke factor"), ("de school", "externe factor")],
            "Persoonlijke factoren zitten bij het ik, externe factoren in de omgeving."),
    sorteer("Helpt of hindert deze omgeving?", ["helpt", "hindert"],
            [("een lift in het gebouw", "helpt"), ("veel lawaai in de klas", "hindert"), ("een trap aan de ingang", "hindert"), ("een buur die boodschappen doet", "helpt")],
            "De omgeving kan een drempel wegnemen of opwerpen."),
    koppel("Koppel het deel van de gezondheidstoestand aan zijn vraag.",
           [("lichaam", "hoe werkt het lichaam?"), ("doen", "wat doet iemand zelf?"), ("samen", "doet iemand mee?")],
           ["hoeveel verdient iemand?"],
           "Geld hoort niet bij de gezondheidstoestand."),
    mk("Waarom staan de pijlen in het ICF-schema in twee richtingen?",
       ["de delen beïnvloeden elkaar", "je mag het schema in twee richtingen lezen", "het lichaam bepaalt alles in de omgeving", "elk deel staat helemaal los van de rest"],
       0, "Gezondheidstoestand, ik en omgeving hangen samen."),
    mk("Ahmed zit in een rolstoel. In de nieuwe school is er een lift en kan hij overal binnen. Wat veranderde er volgens het ICF?",
       ["een externe factor die hem nu helpt", "een lichaamsfunctie die weer helemaal herstelde", "een persoonlijke factor van Ahmed zelf", "een patroon van Gordon dat helemaal wegviel"],
       0, "Aan het lichaam veranderde niets; de omgeving helpt nu."),
    tabel("Klopt dit over het ICF?",
          [("Het ICF kijkt ook naar wat wel lukt.", J), ("Het ICF heeft elf patronen.", F), ("Het ICF kijkt ook naar de omgeving.", J), ("Het ICF stelt een diagnose.", F)],
          "Gordon heeft de elf patronen; een diagnose stelt een arts."),
    sleep("Gordon werkt met [[elf]] patronen. Het ICF werkt met de [[gezondheidstoestand]], het [[ik]] en de [[omgeving]].",
          ["negen", "boekhouding"],
          "Beide schema's brengen het functioneren in kaart."),
    inv("Hoe noem je in het ICF wat iemand meemaakte, zoals zijn opleiding en gewoonten? Hoogstens twee woorden.",
        ["individuele achtergrond", "de individuele achtergrond", "achtergrond"],
        "De individuele achtergrond hoort bij het ik."),
    keuze("Zich wassen en koken horen in het ICF bij [[*doen|lichaam|samen]].",
          "Doen gaat over de activiteiten die iemand zelf uitvoert."),
    casus("Mevrouw Peeters (82) woont alleen. Ze ziet slecht, eet weinig omdat ze niet meer zelf boodschappen kan doen en mist haar vriendinnen van de kaartclub. Haar dochter komt elke week.", [
        sorteer("Onder welk patroon van Gordon noteer je dit?", ["waarneming en cognitie", "voeding en stofwisseling", "rol en relatie"],
                [("ze ziet slecht", "waarneming en cognitie"), ("ze eet weinig", "voeding en stofwisseling"), ("ze mist haar vriendinnen", "rol en relatie")],
                "Zien hoort bij waarneming en cognitie."),
        keuze("Dat ze niet meer naar de kaartclub kan, hoort in het ICF bij [[*samen|doen|lichaam]].", "Meedoen aan vrije tijd is samen."),
        keuze("De dochter die elke week komt, is in het ICF een [[*externe factor|persoonlijke factor|lichaamsfunctie]].", "Het gezin hoort bij de omgeving."),
        mk("Wat is een sterkte die je met het ICF in kaart brengt?",
           ["de wekelijkse hulp van haar dochter", "dat ze slecht ziet met haar beide ogen", "dat ze weinig eet zonder hulp", "dat ze de kaartclub moet missen"],
           0, "Het ICF kijkt ook naar wat wel lukt en welke steun er is."),
    ]),
    open_("Leg uit waarom je bij iemand met een beperking ook naar de omgeving kijkt. Gebruik een voorbeeld.",
          "De omgeving kan helpen of hinderen. Iemand in een rolstoel kan niet binnen in een gebouw met enkel een trap, maar wel als er een lift is. Aan het lichaam verandert niets, toch functioneert de persoon beter."),
    keuze("Een vriendin die Mila elke dag helpt, hoort in het ICF bij [[*de omgeving|het ik|het lichaam]].",
          "Alles buiten de persoon is omgeving."),
    inv("Hoe noem je het patroon van Gordon over hoe iemand zijn eigen gezondheid ziet en wat hij ervoor doet? Hoogstens vier woorden.",
        ["gezondheidsbeleving en instandhouding", "gezondheidsbeleving", "gezondheidsbeleving en -instandhouding"],
        "Gezondheidsbeleving en instandhouding."),
]
