"""Woordvelden: eten, kleding, wonen en winkelen — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Eigen vragen met de woorden uit het gewone hoofdstuk: een menu, boodschappen,
aan de kassa, kleren, kleuren en materialen, de woning en een gewone dag."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import dagelijks as _d

T1 = ("Lis le menu.\n\n"
      "« Café du Marché — Formule midi : 16 euros.\n"
      "Entrée : soupe à l'oignon ou œuf mayonnaise.\n"
      "Plat : poisson et riz, ou omelette aux champignons (végétarien).\n"
      "Dessert : tarte aux pommes ou fromage.\n"
      "Boisson non comprise. Café : 2 euros. Fermé le dimanche. »")

T2 = ("Lis le dialogue au magasin.\n\n"
      "« — Bonjour, je cherche une veste pour l'hiver.\n"
      "— Quelle taille ?\n— Du M, et en noir ou en gris, s'il vous plaît.\n"
      "— Voilà, elle est en laine. Elle coûte 59 euros.\n"
      "— C'est un peu cher… Vous l'avez aussi en coton ?\n"
      "— Oui, en bleu, à 39 euros.\n— Parfait, je la prends. Je paie par carte. »")

VRAGEN = [_d.VRAGEN[i] for i in (8, 11, 15, 16, 22)] + [
    casus(T1, [
        inv("Hoeveel euro betaal je voor de formule met een koffie erbij? Schrijf enkel het getal.", ["18"],
            "16 plus 2 euro: boisson non comprise, de drank zit er niet in."),
        tabel("Klopt dit volgens het menu?",
              [("Er is een vegetarisch hoofdgerecht.", J), ("Een drank zit in de prijs.", F), ("Als dessert kan je ook kaas kiezen.", J), ("Het café is op zondag open.", F)],
              "Non comprise: niet inbegrepen. Fermé le dimanche."),
        keuze("« le poisson » is [[*vis|kip|varkensvlees]].",
              "Le poulet is kip, le porc varkensvlees."),
        keuze("Een vegetariër kiest als hoofdgerecht de [[*omelet met champignons|vis met rijst]].",
              "Végétarien: zonder vlees of vis."),
    ]),
    casus(T2, [
        keuze("De klant zoekt een [[*vest|broek|hemd]] voor de winter.",
              "Une veste: een vest, jas."),
        tabel("Klopt dit volgens het gesprek?",
              [("De klant wil maat M.", J), ("De wollen vest kost 59 euro.", J), ("De klant koopt de vest in het zwart.", F), ("Ze betaalt met de kaart.", J)],
              "Ze neemt de katoenen vest in het blauw."),
        inv("Hoeveel euro bespaart de klant door de katoenen vest te nemen? Schrijf enkel het getal.", ["20"],
            "59 min 39 is 20 euro."),
        keuze("« en laine » en « en coton » noemen [[*het materiaal|de kleur|de maat]].",
              "La laine: wol; le coton: katoen."),
    ]),
    koppel("Koppel elk Frans woord aan zijn betekenis.",
           [("le poulet", "de kip"), ("le porc", "het varkensvlees"), ("le pain", "het brood"), ("le poisson", "de vis")], ["de kaas"],
           "Vier p-woorden die je niet mag verwarren; kaas is le fromage."),
    keuze("« un kilo [[*de|des]] pommes de terre » « beaucoup [[*de|du]] lait »",
          "Na een hoeveelheid komt de, zonder lidwoord."),
    tabel("Waar koop je het?",
          [("une baguette", "la boulangerie"), ("de la viande", "la boucherie"), ("un livre", "la librairie"), ("des croissants", "la boulangerie")],
          "Une librairie is een boekhandel, geen bibliotheek.",
          kolommen=["la boulangerie", "la boucherie", "la librairie"]),
    keuze("De verkoper vraagt « Vous payez par carte ou en [[*espèces|espèce]] ? ».",
          "Payer en espèces: cash betalen."),
    tabel("Biljet of muntstuk?",
          [("un billet de vingt euros", "biljet"), ("une pièce de deux euros", "muntstuk"), ("une pièce de cinquante cents", "muntstuk"), ("un billet de cinq euros", "biljet")],
          "Un billet is van papier, une pièce van metaal.",
          kolommen=["biljet", "muntstuk"]),
    mk("Aan de kassa vraagt de verkoper « Ce sera tout ? ». Wat antwoord je als je nog een zak wil?",
       ["Non, je voudrais aussi un sac.", "Oui, c'est tout, merci beaucoup.", "Je paie en espèces, s'il vous plaît.", "Voilà votre ticket, bonne journée."], 0,
       "Ce sera tout ? vraagt of dat alles is."),
    sorteer("Kleur of vorm?", ["kleur", "vorm"],
            [("gris", "kleur"), ("carré", "vorm"), ("jaune", "kleur"), ("rond", "vorm"), ("blanc", "kleur")],
            "Carré en rond zijn vormen."),
    keuze("« une chemise [[*blanche|blanc]] » « un pantalon [[*noir|noire]] »",
          "Blanc wordt blanche in het vrouwelijk."),
    tabel("Is dit een kledingstuk?",
          [("une jupe", J), ("un bonnet", J), ("une assiette", F), ("un pantalon", J)],
          "Une assiette is een bord."),
    tabel("In welke kamer vind je het meestal?",
          [("un lit", "la chambre"), ("un frigo", "la cuisine"), ("une douche", "la salle de bains"), ("une armoire", "la chambre")],
          "Chambre, cuisine, salle de bains.",
          kolommen=["la cuisine", "la chambre", "la salle de bains"]),
    volgorde("Zet de ochtend in de juiste volgorde.",
             ["je me lève", "je me douche", "je prends mon petit-déjeuner", "je pars à l'école"],
             "Opstaan, douchen, ontbijten, vertrekken."),
    koppel("Koppel elke Franse uitdrukking aan haar betekenis.",
           [("mettre la table", "de tafel dekken"), ("faire la vaisselle", "de vaat doen"), ("ranger sa chambre", "zijn kamer opruimen"), ("faire les courses", "boodschappen doen")], ["zich scheren"],
           "Zich scheren is se raser."),
    tabel("Is dit een persoonlijk voorwerp dat je meeneemt als je vertrekt?",
          [("les clés", J), ("le portefeuille", J), ("le parapluie", J), ("le lave-linge", F)],
          "Een wasmachine neem je niet mee."),
    keuze("« Se doucher » is zich [[*douchen|scheren|aankleden]].",
          "Zich scheren is se raser."),
    inv("Hoe zeg je fles in het Frans? Eén woord, zonder lidwoord.", ["bouteille"],
        "Une bouteille de lait: een fles melk."),
    keuze("« Ça coûte [[*combien|comment]] ? »",
          "Combien: hoeveel."),
    tabel("Klopt dit over een woning?",
          [("Un loyer is de huurprijs.", J), ("Une cave is een kelder.", J), ("Un balcon is een bad.", F)],
          "Un balcon is een balkon; een bad is une baignoire."),
]
