"""Tekstsoorten, tekstverbanden en verwijswoorden — pittig (🚀 Boost doorstroom, Frans).

Eigen Franse teksten en vragen strikt binnen fr_tekstsoorten: de zes
tekstsoorten, tekstverbanden, signaalwoorden en verwijswoorden (ils, y, en,
celui-ci, ce dernier). Met een zelfgetekende tekst in vijf zinnen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER

BL = Prent("tekst-vijf-zinnen", "Un texte sur le télétravail", "een tekst van vijf zinnen, elk met een letter A tot E")
BL.rect(80, 60, 840, 560, "#ffffff", DONKER, 10, 3)
ZINNEN = [("A", 150, "Depuis 2020, beaucoup d'employés travaillent à la maison."),
          ("B", 240, "D'abord, ils gagnent du temps : pas de trajets en voiture."),
          ("C", 330, "De plus, ils peuvent mieux organiser leur journée."),
          ("D", 420, "Pourtant, certains se sentent seuls loin de leurs collègues."),
          ("E", 510, "Les entreprises proposent donc deux jours au bureau par semaine.")]
for t, y, zin in ZINNEN:
    BL.letter(125, y - 7, t)
    BL.tekst(165, y, zin, 23, "start")
U = "tekst-vijf-zinnen.svg"
Z = {t: [Prent.zone(100, y - 40, 810, 60)] for t, y, _ in ZINNEN}

AVIS = ("Lees de tekst.\n\n"
        "« Le nouveau smartphone de cette marque coûte 900 euros. Son écran est grand et ses photos sont belles. "
        "Par contre, la batterie ne tient pas une journée entière. À mon avis, ce prix est beaucoup trop élevé pour un appareil "
        "qui doit être rechargé deux fois par jour. Je préfère garder mon ancien téléphone. »")

ALINEAS = ("Lees de tekst.\n\n"
           "(1) Dans notre ville, de plus en plus de jeunes vont à l'école à vélo.\n"
           "(2) C'est surtout parce que la ville a construit de nouvelles pistes cyclables l'année dernière.\n"
           "(3) Résultat : il y a beaucoup moins de voitures devant les écoles le matin.\n"
           "(4) En revanche, dans les villages autour, presque tous les élèves viennent encore en bus.")

VRAGEN = [
    klik("Bekijk de tekst. Klik op de zin die een tegenstelling aankondigt.", U, Z["D"], "Pourtant: nochtans. De zin gaat in tegen de voordelen ervoor."),
    klik("Klik op de zin die het gevolg van alles ervoor geeft.", U, Z["E"], "Donc: dus. De bedrijven trekken er een besluit uit."),
    klik("Klik op de zin die een toevoeging aan het vorige voordeel geeft.", U, Z["C"], "De plus: bovendien. Er komt nog een voordeel bij."),
    casus(AVIS, [
        keuze("Dit is een [[*opiniërende|prescriptieve|narratieve]] tekst.", "À mon avis: volgens mij. De schrijver geeft zijn mening."),
        mk("Welk woord kondigt het nadeel aan?",
           ["par contre", "à mon avis", "pour un appareil", "deux fois par jour"],
           0, "Par contre: daarentegen. Na de voordelen komt het nadeel."),
        tabel("Feit of mening?",
              [("Le téléphone coûte 900 euros.", "feit"), ("Ce prix est beaucoup trop élevé.", "mening"), ("Son écran est grand.", "feit"), ("Je préfère garder mon ancien téléphone.", "mening")],
              "Een mening kan je niet nakijken; een prijs wel.", ["feit", "mening"]),
        mk("Wat bedoelt de schrijver met 'qui doit être rechargé deux fois par jour'?",
           ["de batterij moet twee keer per dag opgeladen worden", "de gsm moet twee keer per dag een update krijgen", "je moet het toestel twee keer per jaar laten nakijken", "het scherm moet twee keer per dag gepoetst worden"],
           0, "Recharger: opnieuw opladen. Het herhaalt het nadeel van de batterij."),
    ]),
    casus(ALINEAS, [
        sorteer("Welk tekstverband legt elke zin met de zin ervoor?", ["oorzaak", "gevolg", "tegenstelling"],
                [("zin 2", "oorzaak"), ("zin 3", "gevolg"), ("zin 4", "tegenstelling")],
                "Parce que: oorzaak. Résultat: gevolg. En revanche: daarentegen."),
        keuze("In zin 2 verwijst 'C'est' naar [[*het feit dat jongeren met de fiets gaan|de nieuwe fietspaden|de stad]].", "C'est … parce que: dat komt doordat."),
        inv("Welk Frans woord in zin 4 betekent 'daarentegen'? Twee woorden.", ["en revanche"], "En revanche betekent hetzelfde als par contre."),
        mk("Wat is de hoofdgedachte van de tekst?",
           ["nieuwe fietspaden doen jongeren in de stad meer fietsen", "jongeren in de dorpen fietsen liever dan in de stad", "de bussen in de dorpen rijden 's morgens niet meer naar school", "de stad wil alle auto's weren uit het centrum"],
           0, "Zin 2 en 3 dragen die boodschap; zin 4 is enkel een tegenstelling."),
    ]),
    sorteer("Welke soort tekst?", ["informatief", "persuasief", "prescriptief", "narratief"],
            [("une notice de médicament", "prescriptief"), ("une publicité pour un parfum", "persuasief"), ("un article sur les volcans", "informatief"), ("un récit de voyage", "narratief"), ("le règlement de la piscine", "prescriptief"), ("une campagne contre le harcèlement", "persuasief")],
            "Een bijsluiter en een reglement zeggen wat je moet doen."),
    tabel("Klopt dit over tekstsoorten?",
          [("Een tekst kan feiten bevatten en toch opiniërend zijn.", J), ("Een strip is een literaire tekst.", J), ("Een interview is narratief.", F), ("De bedoeling van de schrijver bepaalt de tekstsoort.", J)],
          "Een interview is informatief."),
    koppel("Koppel het signaalwoord aan de betekenis.",
           [("cependant", "echter"), ("de plus", "bovendien"), ("c'est-à-dire", "dat wil zeggen"), ("enfin", "ten slotte")],
           ["omdat"],
           "Signaalwoorden tonen de draad van de tekst."),
    sorteer("Wat kondigt het woord aan?", ["oorzaak", "gevolg", "tegenstelling", "toevoeging"],
            [("parce que", "oorzaak"), ("car", "oorzaak"), ("donc", "gevolg"), ("alors", "gevolg"), ("par contre", "tegenstelling"), ("en outre", "toevoeging")],
            "Car en parce que wijzen achteruit, donc en alors vooruit."),
    mk("'Le directeur a parlé avec le journaliste. Ce dernier avait beaucoup de questions.' Wie had veel vragen?",
       ["de journalist", "de directeur", "de directeur en de journalist", "de leerlingen van de school"],
       0, "Ce dernier: de laatstgenoemde."),
    keuze("'Il y a deux films : Lupin et Astérix. Celui-ci est plus drôle.' Celui-ci is [[*Astérix|Lupin]].", "Celui-ci: het dichtstbij, dus het laatstgenoemde."),
    mk("'Tu connais Bruxelles ? — Oui, j'y vais souvent.' Waarvoor staat y?",
       ["Bruxelles", "de persoon die vraagt", "de trein naar Brussel", "het woord souvent"],
       0, "Y vervangt een plaats die al genoemd is."),
    mk("'Tu veux des cerises ? — Oui, j'en veux un kilo.' Waarvoor staat en?",
       ["des cerises", "un kilo", "de persoon die vraagt", "de markt"],
       0, "En vervangt een groep met de: des cerises."),
    keuze("'Ma sœur a une voiture. Elle est rouge.' Elle verwijst naar [[*de auto of de zus: je moet het uit de context halen|altijd de zus|altijd de auto]].", "Elle verwijst naar elk vrouwelijk woord. Hier is 'de auto' het meest logisch."),
    sleep("Vul de signaalwoorden in: [[D'abord]], on lit le titre. [[Ensuite]], on regarde les images. [[Enfin]], on lit le texte.",
          ["Pourtant", "Car"], "Eerst, daarna, ten slotte."),
    inv("Vul in: Le match est annulé … de la neige. Het is vervelend. Drie woorden.", ["à cause de", "a cause de"], "À cause de: door, met iets vervelends."),
    keuze("'[[*Grâce à|À cause de]] ton aide, j'ai réussi mon examen.'", "Hulp is iets goeds: dankzij."),
    mk("Je leest enkel de signaalwoorden van een moeilijke tekst. Waarom helpt dat?",
       ["je ziet de opbouw van de gedachtegang", "je kent dan alle woorden van de tekst", "je weet dan precies wie de schrijver is", "je hoeft de tekst dan niet meer te lezen"],
       0, "Ze tonen de structuur, nog voor je alles begrijpt."),
    tabel("Kondigt het woord een tegenstelling aan?",
          [("mais", J), ("pourtant", J), ("ainsi", F), ("également", F), ("cependant", J)],
          "Ainsi betekent zo of dus; également is ook."),
    open_("Schrijf in het Frans twee zinnen over het weer, met een tegenstelling ertussen. Gebruik 'mais' of 'pourtant'.",
          "Il fait beau aujourd'hui. Pourtant, il fait très froid."),
    mk("Waaraan herken je een prescriptieve tekst het snelst?",
       ["aan de bevelende werkwoordsvormen", "aan de vele meningen van de schrijver", "aan een verhaal in de verleden tijd", "aan de rijm op het einde van de regels"],
       0, "Coupez, mélangez, ne courez pas: je krijgt opdrachten."),
    inv("Een getuigenis, een reisverslag en een dagboekfragment: welke tekstsoort? Eén woord.", ["narratief", "narratieve", "verhalend"], "Iemand vertelt wat er gebeurd is."),
    keuze("Van wie is de tekst, waarom is hij geschreven en voor wie? Met die vragen gebruik je het [[*communicatiemodel|woordenboek|tekstverband]].", "Zender, bedoeling, ontvanger."),
    mk("'La salle est fermée le lundi. En outre, elle ferme à midi le samedi.' Wat doet 'en outre'?",
       ["het voegt nog een beperking toe", "het zet de twee zinnen tegenover elkaar", "het geeft de oorzaak van de sluiting", "het noemt een voorbeeld bij de eerste zin"],
       0, "En outre: bovendien."),
]
