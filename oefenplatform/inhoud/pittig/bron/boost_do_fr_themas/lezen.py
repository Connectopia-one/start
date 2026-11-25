"""Een Franse tekst analyseren — pittig (🚀 Boost doorstroom, Frans, ERK B1).

Eigen Franse teksten en vragen strikt binnen fr_lezen: onderwerp,
hoofdgedachte, hoofdpunten, losse gegevens, en afleiden: bedoeling, toon,
verband tussen zinnen, twee teksten vergelijken. Met een zelfgetekende affiche."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ORANJE, GEEL, LICHTGROEN

AF = Prent("affiche-fete-du-quartier", "Une affiche dans la rue", "een affiche met vijf regels tekst, letters A tot E")
AF.rect(200, 60, 600, 560, "#fff8e1", DONKER, 12, 4)
AF.tekst(500, 130, "FÊTE DU QUARTIER", 40, vet=True)
AF.rect(240, 150, 520, 4, ORANJE, ORANJE, 0, 0)
REG = [("A", 210, "Samedi 14 juin, de 14 h à 22 h"), ("B", 280, "Place Saint-Paul (s'il pleut : salle des sports)"),
       ("C", 350, "Entrée gratuite – repas : 8 € (enfants : 4 €)"), ("D", 420, "Apportez un dessert à partager !"),
       ("E", 490, "Inscription obligatoire avant le 7 juin")]
for t, y, zin in REG:
    AF.letter(260, y - 7, t)
    AF.tekst(300, y, zin, 22, "start")
AF.tekst(500, 580, "Info : comite.stpaul@exemple.be", 18)
U = "affiche-fete-du-quartier.svg"
Z = {t: [Prent.zone(235, y - 35, 545, 50)] for t, y, _ in REG}

MAIRIE = ("Lees de tekst.\n\n"
          "« À partir du 1er mars, les voitures ne pourront plus entrer dans le centre de Liège le samedi. "
          "La ville veut rendre les rues plus calmes et plus sûres pour les piétons. Les commerçants ne sont pas tous d'accord : "
          "certains ont peur de perdre des clients. Pourtant, à Gand, où la même règle existe depuis dix ans, les magasins du centre "
          "vendent aujourd'hui plus qu'avant. Des bus gratuits rouleront toutes les dix minutes depuis les parkings à l'entrée de la ville. »")

LETTRE = ("Lees de mail.\n\n"
          "« Chère Madame Dubois,\n"
          "Je vous écris parce que mon fils Théo a oublié son sac de sport au vestiaire vendredi dernier. "
          "Il pense l'avoir laissé sous le banc, à côté de la porte. Dans ce sac, il y a ses chaussures neuves et sa gourde bleue. "
          "Pourriez-vous vérifier s'il est encore là ? Théo passera le chercher lundi après les cours, si cela vous convient. "
          "Merci beaucoup et bonne journée,\n"
          "Nadia Lambert »")

DEUX = ("Lees de twee korte teksten.\n\n"
        "Texte 1 : « Le nouveau parc de la ville est magnifique ! Des arbres partout, un étang avec des canards, et enfin un vrai terrain de basket. "
        "Allez-y ce week-end, vous ne le regretterez pas. »\n\n"
        "Texte 2 : « Le nouveau parc a coûté deux millions d'euros. Il fait quatre hectares et compte trois cents arbres. "
        "Il est ouvert tous les jours de 7 h à 21 h. »")

VRAGEN = [
    klik("Bekijk de affiche. Klik op de regel die zegt wat je zelf moet meebrengen.", U, Z["D"], "Apportez un dessert à partager: breng een dessert mee om te delen."),
    klik("Op dezelfde affiche: klik op de regel die zegt waar het feest is als het regent.", U, Z["B"], "S'il pleut: als het regent. Dan gaat het door in de sporthal."),
    klik("Klik op de regel die zegt wat je ten laatste op 7 juni moet doen.", U, Z["E"], "Inscription obligatoire avant le 7 juin: je moet je vóór 7 juni inschrijven."),
    casus(MAIRIE, [
        inv("Wat is het onderwerp van de tekst? Hoogstens vier woorden.", ["autovrij centrum", "een autovrij centrum", "autovrije zaterdag", "geen auto's in het centrum", "auto's uit het centrum", "autoverbod in het centrum", "autovrij stadscentrum"],
            "Les voitures ne pourront plus entrer dans le centre: auto's mogen het centrum niet meer in."),
        mk("Wat is de hoofdgedachte?",
           ["een autovrij centrum hoeft de winkels geen klanten te kosten", "de handelaars in Luik zijn het helemaal niet eens met de stad", "in Gent rijden er elke tien minuten gratis bussen rond", "vanaf 1 maart mag je in Luik nergens meer met de auto rijden"],
           0, "Het voorbeeld van Gent weerlegt de angst van de handelaars. Daar werkt de tekst naartoe."),
        keuze("Het woord 'Pourtant' leidt een [[*tegenstelling|reden|opsomming]] in.", "Pourtant is toch, nochtans: het gaat in tegen de angst van de handelaars."),
        tabel("Staat dit in de tekst?",
              [("De regel geldt enkel op zaterdag.", J), ("Alle handelaars zijn tegen.", F), ("In Gent bestaat dezelfde regel al tien jaar.", J), ("De bussen vanaf de parkings zijn betalend.", F)],
              "Pas tous d'accord: niet allemaal akkoord. Des bus gratuits: gratis bussen."),
        mk("Waarom vermeldt de schrijver de bussen helemaal op het einde?",
           ["om te tonen hoe je het centrum toch kan bereiken", "om de angst van de handelaars nog groter te maken", "om te bewijzen dat de regel in Gent mislukt is", "om de lezer aan te raden met de auto te komen"],
           0, "Het is een praktische oplossing voor wie niet meer met de auto binnen mag."),
        inv("Welk Frans woord in de tekst betekent 'voetgangers'?", ["piétons", "pietons", "les piétons"], "Un piéton is een voetganger."),
    ]),
    casus(LETTRE, [
        mk("Wat vraagt Nadia aan mevrouw Dubois?",
           ["te kijken of de sporttas nog in de kleedkamer ligt", "nieuwe sportschoenen voor haar zoon Théo te kopen", "Théo vrijdag na de les naar huis te laten gaan", "de blauwe drinkfles van Théo zo snel mogelijk op te sturen"],
           0, "Pourriez-vous vérifier s'il est encore là: zou u kunnen nakijken of hij er nog is?"),
        tabel("Klopt dit volgens de mail?",
              [("Théo vergat zijn tas op vrijdag.", J), ("De tas ligt volgens Théo bij de douches.", F), ("Théo wil de tas maandag na school komen halen.", J), ("In de tas zitten oude schoenen.", F)],
              "Sous le banc, à côté de la porte: onder de bank, naast de deur. Ses chaussures neuves: zijn nieuwe schoenen."),
        keuze("De zin 'si cela vous convient' betekent: [[*als het u past|als u het vindt|als u het wil kopen]].", "Convenir à quelqu'un: iemand passen."),
        mk("Waaraan zie je dat de mail beleefd en formeel is?",
           ["aan 'Chère Madame' en het gebruik van vous", "aan de vele uitroeptekens in elke zin", "aan het gebruik van tu tegen de juf van Théo", "aan de korte zinnen zonder werkwoord"],
           0, "Vous en een vaste aanhef en groet maken een mail formeel."),
    ]),
    casus(DEUX, [
        sorteer("Bij welke tekst hoort dit?", ["texte 1", "texte 2"],
                [("geeft een mening", "texte 1"), ("geeft enkel cijfers en feiten", "texte 2"), ("spreekt de lezer rechtstreeks aan", "texte 1"), ("vermeldt de openingsuren", "texte 2")],
                "Allez-y spreekt je aan; deux millions d'euros en de uren zijn feiten."),
        mk("Wat is de bedoeling van texte 1?",
           ["de lezer overtuigen om naar het park te gaan", "de lezer informeren over wat het park kostte", "de lezer waarschuwen voor de eenden in de vijver", "de lezer uitleggen hoe je een park aanlegt"],
           0, "Vous ne le regretterez pas: je zal er geen spijt van hebben."),
        keuze("De toon van texte 2 is [[*zakelijk|enthousiast|boos]].", "Geen enkel oordeel, enkel feiten."),
        inv("Hoeveel bomen telt het park? Schrijf het getal in cijfers.", ["300"], "Trois cents arbres: driehonderd bomen."),
    ]),
    tabel("Lees: 'Il fait beau, mais il fait froid.' Wat klopt?",
          [("Het is mooi weer.", J), ("Het is warm.", F), ("'Mais' zet twee dingen tegenover elkaar.", J)],
          "Il fait froid: het is koud."),
    mk("'Il n'a jamais pris l'avion.' Wat betekent dat?",
       ["hij heeft nog nooit het vliegtuig genomen", "hij neemt elke week het vliegtuig naar Parijs", "hij heeft het vliegtuig gisteren gemist", "hij wil nooit meer het vliegtuig nemen"],
       0, "Ne … jamais: nooit. Let goed op de ontkenning, ze draait de zin om."),
    keuze("'Il ne reste plus de pain.' Er is [[*geen brood meer|nog veel brood|nieuw brood]].", "Ne … plus: niet meer."),
    sleep("Lees: 'Elle est restée à la maison parce qu'elle était malade.' Ze bleef [[thuis]] omdat ze [[ziek]] was.",
          ["moe", "buiten"], "Parce que geeft de reden."),
    mk("'Le magasin ferme à 18 h, sauf le dimanche.' Wat leer je daaruit?",
       ["op zondag gelden andere uren", "de winkel is op zondag om 18 u dicht", "de winkel is elke dag open tot 18 u", "de winkel opent pas om 18 u"],
       0, "Sauf: behalve. Op zondag geldt de regel van 18 u niet."),
    keuze("'Une dizaine de personnes' is [[*ongeveer tien mensen|precies tien mensen|twintig mensen]].", "Zoals une centaine: een honderdtal."),
    open_("Lees: 'Je voulais acheter ce livre, mais il était trop cher. Alors je l'ai emprunté à la bibliothèque.' Leg in je eigen woorden uit wat er gebeurde en waarom.",
          "De persoon wilde het boek kopen, maar het was te duur. Daarom leende hij of zij het in de bibliotheek."),
    mk("'Encore un retard ! C'est la troisième fois cette semaine.' Welke toon heeft deze zin?",
       ["geërgerd", "blij", "zakelijk", "verdrietig"],
       0, "Encore en het uitroepteken: de schrijver is het beu."),
    inv("'Le train de 8 h 10 a vingt minutes de retard.' Hoe laat komt de trein ongeveer? Schrijf zo: 8.30", ["8.30", "8u30", "8 h 30", "8:30", "8h30"],
        "Vingt minutes de retard: twintig minuten vertraging."),
    volgorde("Zet de stappen van dit recept in de juiste volgorde.",
             ["D'abord, lave les fraises.", "Ensuite, coupe-les en deux.", "Puis, ajoute un peu de sucre.", "Enfin, mets-les au frigo."],
             "D'abord, ensuite, puis, enfin: eerst, daarna, dan, ten slotte."),
    keuze("'Grâce à la pluie, les plantes ont bien poussé.' 'Grâce à' geeft een [[*oorzaak met een goed gevolg|tegenstelling|voorwaarde]].", "Grâce à: dankzij."),
    tabel("Lees: 'Je n'ai pas encore fini mes devoirs, donc je ne peux pas sortir.' Klopt dit?",
          [("Het huiswerk is al klaar.", F), ("De schrijver mag nog niet weg.", J), ("'Donc' geeft een gevolg.", J)],
          "Pas encore: nog niet. Donc: dus."),
    koppel("Koppel het Franse woord aan de betekenis.",
           [("déçu", "teleurgesteld"), ("fier", "trots"), ("inquiet", "ongerust")],
           ["verliefd"],
           "Je hebt ze nodig om de toon van een tekst te herkennen."),
]
