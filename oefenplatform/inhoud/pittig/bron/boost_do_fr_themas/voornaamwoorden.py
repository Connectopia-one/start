"""Voornaamwoorden: COD, COI, y en en — pittig (🚀 Boost doorstroom, Frans).

Eigen vragen strikt binnen fr_voornaamwoorden: persoonlijk (sujet, COD, COI,
tonique, y, en) en hun plaats, wederkerend, betrekkelijk (qui, que, dont, où,
ce qui, ce que), bezittelijk, aanwijzend, vragend en onbepaald. Met een
zelfgetekend rijtje korte gesprekjes."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER

GS = Prent("vijf-gesprekjes", "Cinq petits dialogues", "vijf korte gesprekjes van twee zinnen, letters A tot E")
GS.rect(40, 55, 920, 570, "#ffffff", DONKER, 10, 3)
RG = [("A", 130, "— Tu as vu mes clés ?", "— Oui, je les ai mises sur la table."),
      ("B", 235, "— Tu vas à la piscine demain ?", "— Oui, j'y vais avec Léa."),
      ("C", 340, "— Tu veux du gâteau ?", "— Non merci, j'en ai déjà mangé."),
      ("D", 445, "— Tu as écrit à tes grands-parents ?", "— Oui, je leur ai écrit une carte."),
      ("E", 550, "— Tu viens avec Hugo ?", "— Non, je viens sans lui.")]
for t, y, v, a in RG:
    GS.letter(85, y + 8, t)
    GS.tekst(125, y, v, 22, "start")
    GS.tekst(125, y + 34, a, 22, "start")
U = "vijf-gesprekjes.svg"
Z = {t: [Prent.zone(55, y - 35, 890, 90)] for t, y, _, _ in RG}

BRIEF = ("Lees het bericht.\n\n"
         "« Salut Inès ! Tu te souviens de Malik, le garçon dont je t'ai parlé ? Je l'ai revu hier à la gare. "
         "Il m'a dit qu'il habite maintenant à Namur, la ville où sa mère est née. Je lui ai donné ton numéro : "
         "il veut te poser une question sur le stage que tu as fait l'été dernier. Ce qui m'a surpris, c'est qu'il se souvenait de toi ! »")

VRAGEN = [
    klik("Bekijk de gesprekjes. Klik op het gesprekje waarin het voornaamwoord een plaats vervangt.", U, Z["B"], "J'y vais: y vervangt à la piscine."),
    klik("Klik op het gesprekje waarin het voornaamwoord een hoeveelheid van iets vervangt.", U, Z["C"], "J'en ai mangé: en vervangt du gâteau."),
    klik("Klik op het gesprekje met een meewerkend voorwerp (COI) voor meerdere personen.", U, Z["D"], "Écrire à: leur, voor de grootouders."),
    klik("Klik op het gesprekje met een tonische vorm na een voorzetsel.", U, Z["E"], "Sans lui: na een voorzetsel de tonische vorm."),
    casus(BRIEF, [
        keuze("'Je l'ai revu' — l' verwijst naar [[*Malik|Inès|de gare]].", "L' is COD en slaat terug op Malik."),
        keuze("'Je lui ai donné ton numéro' — lui verwijst naar [[*Malik|Inès|de moeder van Malik]].", "Lui is COI: aan Malik."),
        sorteer("Welk betrekkelijk voornaamwoord, en waarom?", ["dont (parler de)", "où (plaats)", "que (lijdend voorwerp)"],
                [("le garçon … je t'ai parlé", "dont (parler de)"), ("la ville … sa mère est née", "où (plaats)"), ("le stage … tu as fait", "que (lijdend voorwerp)")],
                "Parler de geeft dont; où voor een plaats; que als het lijdend voorwerp is."),
        mk("Waarnaar verwijst 'Ce qui m'a surpris'?",
           ["naar het feit dat Malik zich Inès herinnerde", "naar de stad waar de moeder van Malik geboren is", "naar het telefoonnummer van Inès", "naar het station waar ze Malik zag"],
           0, "Ce qui slaat op een heel idee: c'est qu'il se souvenait de toi."),
    ]),
    sorteer("COD of COI? Welk voornaamwoord vervangt het?", ["le / la / les", "lui / leur"],
            [("Je vois Pierre.", "le / la / les"), ("Je parle à Pierre.", "lui / leur"), ("J'attends mes amis.", "le / la / les"), ("Je réponds à mes amis.", "lui / leur"), ("Je téléphone à ma sœur.", "lui / leur"), ("J'aide ma sœur.", "le / la / les")],
            "Een à voor de persoon verraadt het COI."),
    inv("Vervang: Je donne le cadeau à Léa. → Je … … donne. Twee woorden.", ["le lui"], "Le komt vóór lui."),
    tabel("Staan de voornaamwoorden in de juiste volgorde?",
          [("Il me le prête.", J), ("Je lui le donne.", F), ("Elle nous en parle.", J), ("Je vais y aller.", J), ("Il en y a.", F)],
          "Me, te, se, nous, vous; dan le, la, les; dan lui, leur; dan y; dan en. Il y en a."),
    keuze("Geef het mij! [[*Donne-le-moi|Donne-moi-le|Me le donne]] !", "Bij een bevestigend bevel achter het werkwoord, en me wordt moi."),
    keuze("Geef het mij niet! [[*Ne me le donne pas|Ne donne-le-moi pas|Ne le me donne pas]] !", "In de ontkenning staat alles weer vooraan."),
    sleep("Vul de tonische vormen in: Chez [[moi]], on mange tôt. [[Toi]], tu manges tard. Je pars avec [[eux]].",
          ["je", "ils"], "Na een voorzetsel of om te benadrukken: moi, toi, lui, elle, nous, vous, eux, elles."),
    keuze("On [[*va|allons]] au cinéma ce soir ?", "On wordt als enkelvoud vervoegd."),
    sorteer("Qui of que?", ["qui", "que"],
            [("La fille … chante est ma sœur.", "qui"), ("Le film … nous regardons est long.", "que"), ("Le bus … arrive est le 12.", "qui"), ("La robe … elle porte est rouge.", "que")],
            "Na qui volgt een werkwoord, na que een onderwerp."),
    inv("Vul in: Je me souviens du jour … nous nous sommes rencontrés. Eén woord.", ["où"], "Où ook voor een tijdstip."),
    mk("Welke zin met dont is juist?",
       ["C'est l'outil dont j'ai besoin.", "C'est la maison dont j'habite depuis longtemps.", "C'est le film dont je regarde ce soir.", "C'est l'ami dont je vois souvent en ville."],
       0, "Avoir besoin de: dont. Habiter, regarder en voir hebben geen de."),
    sorteer("Welk bezittelijk voornaamwoord?", ["le mien", "la mienne", "les miens", "les miennes"],
            [("ton vélo ? c'est …", "le mien"), ("ta maison ? c'est …", "la mienne"), ("tes livres ? ce sont …", "les miens"), ("tes clés ? ce sont …", "les miennes")],
            "Het ding beslist, niet de eigenaar."),
    keuze("'Quelle robe préfères-tu ? — [[*Celle|Celui|Cette]] de gauche.'", "Robe is vrouwelijk: celle."),
    inv("Vul in: Il n'y a … dans le frigo, er is niets in de koelkast.", ["rien"], "Rien vervangt pas: il n'y a rien."),
    keuze("J'hésite entre ces deux pulls. [[*Lequel|Laquelle|Lesquels]] préfères-tu ?", "Pull is mannelijk enkelvoud."),
    mk("'Mes cousins se téléphonent chaque semaine.' Wat betekent se hier?",
       ["ze bellen elkaar", "ze bellen zichzelf", "ze bellen hun ouders", "ze bellen nooit"],
       0, "Een wederkerend werkwoord kan wederkerig zijn: elkaar."),
    tabel("Klopt dit over voornaamwoorden?",
          [("Qui wordt nooit qu' voor een klinker.", J), ("Y kan ook een persoon vervangen.", F), ("Bij en blijft een getal staan: j'en ai deux.", J), ("Leur als voornaamwoord krijgt een s.", F)],
          "Voor personen gebruik je à lui, à elle; leur krijgt als voornaamwoord nooit een s."),
    mk("'Les profs ont parlé aux élèves. Ils leur ont expliqué le projet.' Wie legde uit?",
       ["de leerkrachten", "de leerlingen uit de klas", "de directie van de school", "de ouders van de leerlingen"],
       0, "Ils is onderwerp en slaat op les profs; leur op les élèves."),
    open_("Antwoord in het Frans met een voornaamwoord: 'Tu as parlé à ta prof de ton projet ?' Gebruik lui en en.",
          "Oui, je lui en ai parlé hier."),
    keuze("In een verzorgde geschreven tekst schrijf je eerder [[*cela|ça]].", "Ça is ongedwongen spreektaal."),
    inv("Vervang: Je pense à mon examen. → J'… pense. Eén letter.", ["y"], "Y vervangt een groep met à die geen persoon is."),
    mk("Vervang 'de Paris' in: Je viens de Paris.",
       ["J'en viens.", "J'y viens.", "Je le viens.", "Je lui viens."],
       0, "En vervangt een groep met de."),
    keuze("Il y a [[*quelqu'un|personne|rien]] à la porte : j'entends sonner.", "Quelqu'un: iemand."),
]
