"""Présent, impératif en de wederkerende werkwoorden — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Vragen over de présent, de frequente onregelmatige werkwoorden, de impératif, de
wederkerende en onpersoonlijke werkwoorden uit Frans Beyond dubbele finaliteit
(zonder de werkwoorden die hier niet in de leerstof staan), aangevuld met eigen
vragen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import presens as _p

VRAGEN = [_p.VRAGEN[i] for i in (0, 1, 2, 3, 4, 6, 7, 11, 13, 15, 17, 18, 19, 23)] + [
    tabel("Welke vorm van avoir of être past?",
          [("Nous ___ belges.", "sommes"), ("Ils ___ deux chiens.", "ont"), ("Vous ___ fatigués ?", "êtes"), ("J'___ quinze ans.", "ai")],
          "Verwar ils ont en ils sont niet. Voor je leeftijd gebruik je avoir.",
          kolommen=["ai", "ont", "sommes", "êtes"]),
    keuze("« Je [[*vais|va]] à l'école à vélo, et mes amis [[*vont|allent]] à pied. »",
          "Aller: je vais, ils vont."),
    keuze("« Vous [[*faites|faisez]] du sport ? »",
          "Faire: vous faites."),
    keuze("« Nous [[*devons|doivons]] partir maintenant. »",
          "Devoir: nous devons, ils doivent."),
    keuze("« D'où [[*viens|vient]]-tu ? »",
          "Venir: tu viens."),
    tabel("Vervoeg je het zoals finir?",
          [("choisir", J), ("partir", F), ("dormir", F), ("finir", J)],
          "Partir, sortir en dormir doen het anders: nous partons."),
    keuze("Een recept zegt « [[*Ajoutez|Vous ajoutez|Ajouter]] le riz. »",
          "Een opdracht in de vous-vorm: de impératif."),
    keuze("Je zegt tegen een vriend: « [[*Regarde|Regardes]] ! »",
          "Bij een werkwoord op -er valt de s van de tu-vorm weg."),
    keuze("« J'aime [[*jouer|joue|joué]] au basket, et il faut [[*partir|part|parti]] maintenant. »",
          "Na aimer en il faut komt de infinitief."),
    tabel("Infinitief, persoonsvorm of voltooid deelwoord?",
          [("aller", "infinitief"), ("vous allez", "persoonsvorm"), ("je suis allé", "voltooid deelwoord"), ("tu vas", "persoonsvorm")],
          "Ze klinken bijna gelijk, maar hun rol is anders.",
          kolommen=["infinitief", "persoonsvorm", "voltooid deelwoord"]),
    keuze("« Il [[*fait|est]] beau aujourd'hui, mais il [[*pleut|pleuve]] demain. »",
          "Over het weer: il fait; pleuvoir: il pleut."),
    keuze("« [[*Allons|Allez|Va]]-y, les amis ! » betekent laten we gaan.",
          "De nous-vorm van de impératif."),
]
