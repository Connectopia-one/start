"""Schrijven, schriftelijke interactie en leesbeleving — pittig (🚀 Boost doorstroom, Frans).

Eigen vragen strikt binnen fr_schrijven: taalhandelingen (informatie vragen,
mening, vertellen, uitleggen, overtuigen, sociale contacten), de bouw en de
toon van een mail, nalezen en leesbeleving. Met een zelfgetekende mail."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS

ML = Prent("mail-camping", "Une mail à un camping", "een mail met vijf delen, letters A tot E")
ML.rect(80, 55, 840, 570, "#ffffff", DONKER, 10, 3)
ML.rect(80, 55, 840, 50, GRIJS, DONKER, 10, 3)
ML.tekst(110, 88, "À : info@camping-des-pins.fr      Objet : réservation", 18, "start")
DL = [("A", 160, ["Madame, Monsieur,"]),
      ("B", 225, ["Je vous écris au sujet de votre annonce pour des emplacements en août."]),
      ("C", 300, ["Nous sommes quatre personnes avec une tente et nous voudrions", "rester du 3 au 10 août."]),
      ("D", 395, ["Pourriez-vous me dire s'il reste de la place et quel est le prix ?", "Est-ce que les chiens sont acceptés ?"]),
      ("E", 500, ["Bisous et à plus,", "Emma Peeters"])]
for t, y, regels in DL:
    ML.letter(125, y - 7, t)
    for i, r in enumerate(regels):
        ML.tekst(165, y + i * 32, r, 21, "start")
U = "mail-camping.svg"
Z = {t: [Prent.zone(100, y - 38, 810, 30 + 32 * len(r) + 10)] for t, y, r in DL}

ANTWOORD = ("Lees het antwoord van de camping.\n\n"
            "« Madame,\n"
            "Nous vous remercions de votre message. Il nous reste un emplacement pour une tente du 3 au 10 août. "
            "Le prix est de 25 euros par nuit pour quatre personnes. Malheureusement, les chiens ne sont pas acceptés. "
            "Si vous souhaitez réserver, merci de nous répondre avant le 15 juin.\n"
            "Cordialement,\n"
            "Camping des Pins »")

VRAGEN = [
    klik("Bekijk de mail van Emma. Klik op het deel dat niet past bij een formele mail.", U, Z["E"], "Bisous et à plus hoort bij vrienden. Beter: Cordialement."),
    klik("Klik op de zin die zegt waarom Emma schrijft.", U, Z["B"], "Je vous écris au sujet de: ik schrijf u in verband met."),
    klik("Klik op het deel waarin Emma informatie vraagt.", U, Z["D"], "Pourriez-vous me dire: zou u mij kunnen zeggen."),
    casus(ANTWOORD, [
        tabel("Klopt dit volgens het antwoord?",
              [("Er is nog plaats voor de hele week.", J), ("Een nacht kost 25 euro per persoon.", F), ("De hond mag mee.", F), ("Emma moet vóór 15 juni antwoorden.", J)],
              "Par nuit pour quatre personnes: per nacht voor vier personen. Les chiens ne sont pas acceptés."),
        inv("Hoeveel kosten zeven nachten samen? Schrijf het getal in euro.", ["175", "175 euro", "175 euros"], "7 × 25 = 175."),
        keuze("'Malheureusement' kondigt [[*slecht nieuws|een voorbeeld|een uitnodiging]] aan.", "Malheureusement: helaas."),
        mk("Emma wil boeken zonder hond. Welke zin past in haar antwoord?",
           ["Je voudrais réserver l'emplacement du 3 au 10 août.", "Salut, c'est cool, on arrive avec le chien demain !", "Je ne veux pas votre emplacement en août.", "Pourquoi les chiens ne sont-ils pas acceptés chez vous ?"],
           0, "Beleefd, met de conditionnel, en ze gaat in op het aanbod."),
        mk("Waarom is dit schriftelijke interactie?",
           ["je reageert op een bericht van iemand anders", "je schrijft een gedicht over je vakantie aan zee", "je vertelt een verhaal zonder dat iemand het leest", "je leest de mail van de camping enkel na"],
           0, "Interactie is ingaan op wat de ander schrijft."),
    ]),
    sorteer("Welke taalhandeling?", ["informatie vragen", "mening geven", "vertellen", "overtuigen"],
            [("Je voudrais savoir à quelle heure le musée ouvre.", "informatie vragen"), ("À mon avis, ce film est trop long.", "mening geven"), ("Hier, nous sommes allés à la mer et il a plu.", "vertellen"), ("Venez chez nous : c'est moins cher et plus rapide !", "overtuigen")],
            "Wat wil je met je zin bereiken?"),
    volgorde("Zet de delen van een verzorgde Franse mail in de juiste volgorde.",
             ["Madame, Monsieur,", "Je vous écris au sujet de …", "de inhoud van je vraag", "Je vous remercie d'avance.", "Cordialement,"],
             "Aanhef, reden, inhoud, bedanking, slot."),
    sorteer("Formeel of informeel?", ["formeel", "informeel"],
            [("Bien à vous", "formeel"), ("Coucou !", "informeel"), ("Je me permets de vous contacter", "formeel"), ("Ça te dit ?", "informeel"), ("Veuillez agréer mes salutations distinguées", "formeel"), ("Bisous", "informeel")],
            "Pas je taal aan de ontvanger aan."),
    keuze("Na 'je pense que' in een bevestigende zin komt de [[*indicatif|subjonctif]]: je pense qu'il a raison.", "Pas in de ontkenning komt de subjonctif."),
    mk("Je vertelt over een ongeval. Welke zin gebruikt de tijden goed?",
       ["Il pleuvait quand la voiture a glissé.", "Il a plu quand la voiture glissait.", "Il pleut quand la voiture a glissé.", "Il pleuvra demain quand la voiture glissait."],
       0, "Imparfait voor het decor, passé composé voor de gebeurtenis."),
    inv("Vul in: je vous … de votre réponse rapide. Het werkwoord betekent 'bedanken'.", ["remercie"], "Remercier quelqu'un de quelque chose."),
    tabel("Is dit een goede strategie bij schrijven?",
          [("vooraf een schrijfplan met kernwoorden maken", J), ("een onbekend woord omschrijven met woorden die je kent", J), ("een Nederlands woord invullen als je het Franse niet kent", F), ("halfweg overschakelen van vous naar tu", F)],
          "Omschrijven is een vaardigheid, geen nederlaag."),
    mk("Je kent het woord 'un tire-bouchon' niet. Hoe omschrijf je het?",
       ["un objet pour ouvrir une bouteille de vin", "un objet pour fermer une porte de la maison à clé", "une chose dans la cuisine", "une kurkentrekker en néerlandais"],
       0, "Beschrijf waarvoor het dient."),
    keuze("'Je vous prie d'agréer mes salutations distinguées' staat [[*onderaan|bovenaan]] een formele brief.", "Het is de deftige slotformule."),
    sorteer("Leesbeleving of feit over het boek?", ["leesbeleving", "feit"],
            [("Ce personnage me ressemble.", "leesbeleving"), ("Le livre a 200 pages.", "feit"), ("La fin m'a beaucoup touché.", "leesbeleving"), ("L'auteur est né à Liège.", "feit")],
            "Leesbeleving zegt wat de tekst met jou doet."),
    sleep("Ik vind het verhaal mooi: « J'ai [[beaucoup]] aimé cette histoire, [[parce que]] la fin m'a [[surpris]]. »",
          ["malgré", "jamais"], "Je geeft je gevoel en een reden."),
    mk("Iemand schrijft: 'Excusez-moi pour le retard de ma réponse.' Wat antwoord je gepast?",
       ["Ce n'est pas grave, ne vous inquiétez pas.", "C'est votre faute, vous êtes toujours en retard.", "Bisous, à plus.", "Je ne vous connais pas."],
       0, "Reageren op een verontschuldiging: ce n'est pas grave."),
    keuze("Een spellingcontrole vindt [[*niet|wel]] dat je 'mer' schreef waar je 'mère' bedoelde.", "Mer bestaat ook: de controle zwijgt."),
    tabel("Klopt dit over een schrijfopdracht?",
          [("Je beantwoordt alle vragen uit de mail van de ander.", J), ("Enkel de grammatica telt.", F), ("Je leest je tekst na voor je hem indient.", J), ("Bij een leeftijdsgenoot mag je sms-taal gebruiken.", F)],
          "Een losse toon mag, sms-taal niet."),
    mk("Je wil de directie overtuigen om een schoolreis naar Parijs te organiseren. Wat werkt het best?",
       ["tonen wat de school en de leerlingen eraan hebben", "alleen zeggen dat jij zelf heel graag naar Parijs wil", "vragen hoeveel de reis kost en verder niets zeggen", "dreigen dat je anders niet meer naar de les komt"],
       0, "Overtuigen: denk vanuit de ander."),
    inv("Vul het werkwoord in dat 'uitnodigen' betekent: nous voulons vous … à notre fête.", ["inviter"], "Inviter, une invitation."),
    open_("Schrijf in het Frans twee zinnen aan een Franse vriend: bedank hem voor zijn cadeau en zeg waarom je het leuk vindt.",
          "Merci beaucoup pour ton cadeau ! J'adore ce livre parce que j'aime les histoires de détectives."),
    mk("Je nodigt de buren die je nauwelijks kent uit op een feest. Welke zin past?",
       ["Nous serions ravis de vous voir à notre fête samedi.", "Salut les voisins, venez samedi soir, ce sera trop cool !", "Vous venez à la fête samedi ou pas ? Dites-le vite.", "Tu viens à notre fête samedi avec tes enfants ?"],
       0, "De conditionnel en vous maken de uitnodiging beleefd."),
    keuze("Je wil iemand aan het eind van een vraag bedanken. Je schrijft: Je vous remercie [[*d'avance|à plus|bisous]].", "Je vous remercie d'avance: alvast bedankt."),
    tabel("Leidt dit je eigen mening in?",
          [("à mon avis", J), ("je trouve que", J), ("il paraît que", F), ("on dit que", F)],
          "Il paraît que en on dit que is horen zeggen."),
    inv("Vul in: je voudrais des … sur vos cours de natation. Het woord betekent 'inlichtingen'.", ["renseignements", "informations"], "Un renseignement: een inlichting."),
    sleep("Mijn argumenten op een rij: [[D'abord]], c'est bon pour la santé. [[De plus]], ce n'est pas cher. [[Enfin]], c'est amusant.",
          ["Malheureusement", "Pourtant"], "Zo zet je argumenten op een rij."),
]
