"""Tekstsoorten, tekstverbanden en leesstrategieën — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Vragen over de zes tekstsoorten uit Frans Beyond dubbele finaliteit, aangevuld met
eigen vragen over signaalwoorden, verwijswoorden en leesstrategieën."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import tekstsoorten as _t

T1 = ("Lis le texte.\n\n"
      "« Mes grands-parents habitent à la campagne. Ils ont des poules et un grand potager. "
      "Chaque dimanche, nous y allons en voiture. Ma grand-mère nous donne toujours des œufs. "
      "Nous les mangeons le lundi matin. Mon frère n'aime pas la campagne, par contre moi, je l'adore, "
      "parce que c'est calme. »")

VRAGEN = [_t.VRAGEN[i] for i in (0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 16, 17, 18, 21, 24, 25)] + [
    casus(T1, [
        keuze("« Ils » in de tweede zin verwijst naar [[*de grootouders|de kippen|de ouders van de schrijver]].",
              "Ils vervangt mes grands-parents uit de zin ervoor."),
        keuze("« y » in « nous y allons » verwijst naar [[*het platteland bij de grootouders|de auto|de zondag]].",
              "Y vervangt een plaats."),
        keuze("« les » in « nous les mangeons » verwijst naar [[*de eieren|de kippen|de grootouders]].",
              "Je eet de eieren die de grootmoeder geeft."),
        keuze("« par contre » zet [[*de broer en de schrijver tegenover elkaar|twee dagen van de week op een rij]].",
              "Hij houdt niet van het platteland, de schrijver wel."),
        inv("Welke twee woorden in de laatste zin geven een reden? Schrijf ze.", ["parce que"],
            "Parce que c'est calme: omdat het rustig is."),
    ]),
    koppel("Koppel elk Frans signaalwoord aan zijn betekenis.",
           [("d'abord", "eerst"), ("ensuite", "daarna"), ("enfin", "tot slot"), ("donc", "dus")], ["omdat"],
           "Deze woorden zetten de stappen of de gedachten op een rij."),
    tabel("Wat kondigt het signaalwoord aan?",
          [("cependant", "tegenstelling"), ("car", "reden"), ("par contre", "tegenstelling"), ("parce que", "reden")],
          "Cependant en par contre zetten iets tegenover elkaar; car en parce que geven een reden.",
          kolommen=["reden", "tegenstelling"]),
    mk("Lees: « Le parc est fermé, car il y a eu une tempête. » Wat betekent car hier?",
       ["want", "maar", "dus", "eerst"], 0,
       "Car geeft de reden: er was een storm."),
    volgorde("Je krijgt een Franse tekst op het examen. Zet deze leesstappen in een goede volgorde.",
             ["naar de titel en de foto kijken", "de tekst één keer helemaal lezen", "de vraag lezen en het stuk zoeken dat erbij hoort", "enkel de woorden opzoeken die je echt nodig hebt"],
             "Eerst het geheel, dan de details."),
    tabel("Is dit een goede strategie om een onbekend woord te begrijpen?",
          [("kijken of het lijkt op een Nederlands of Engels woord", J), ("de rest van de zin gebruiken", J), ("letten op een voorvoegsel zoals im-", J), ("de hele tekst overslaan", F)],
          "Context, andere talen en woordvorming helpen je raden."),
]
