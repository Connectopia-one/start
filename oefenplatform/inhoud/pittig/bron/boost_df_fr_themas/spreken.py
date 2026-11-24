"""Spreken, gesprekken, klank en spelling — pittig (🛠️ Boost dubbele finaliteit, Frans A2).

Eigen vragen over gesprekken voeren, de beoordelingsrijen bij spreken, en de
klanken, accenten en spelling van het Frans, plus enkele vragen uit Frans Beyond
dubbele finaliteit."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_df_fr_themas import schrijven as _s

VRAGEN = [_s.VRAGEN[i] for i in (6, 15, 16, 19, 20)] + [
    casus("Lis le petit dialogue.\n\n« Élève : Bonjour madame, excusez-moi, vous avez une minute ?\n"
          "Dame : Oui, bien sûr.\nÉlève : Je cherche la gare. C'est loin ?\n"
          "Dame : Non, c'est à dix minutes à pied. Vous prenez la deuxième rue à gauche.\n"
          "Élève : Pardon, vous pouvez répéter, s'il vous plaît ?\n"
          "Dame : La deuxième rue à gauche, puis tout droit.\nÉlève : Merci beaucoup, au revoir ! »", [
        keuze("De leerling begint het gesprek [[*beleefd met bonjour en excusez-moi|meteen met zijn vraag]].",
              "Eerst groeten, dan vragen."),
        keuze("Hij gebruikt de [[*vous-vorm|tu-vorm]], want hij kent de dame niet.",
              "Vous tegen een onbekende volwassene."),
        mk("Waarom zegt de leerling « vous pouvez répéter » ?",
           ["Hij heeft de weg niet goed begrepen.", "Hij wil dat de dame stiller spreekt.", "Hij wil het gesprek beleefd afsluiten.", "Hij weet de weg naar het station al."], 0,
           "Répéter: herhalen. Vragen om te herhalen mag altijd."),
        inv("Hoeveel minuten wandel je tot aan het station? Geef het getal.", ["10", "dix", "tien"],
            "C'est à dix minutes à pied."),
        keuze("Met « au revoir » [[*sluit hij het gesprek af|begint hij het gesprek]].",
              "Au revoir: tot ziens."),
    ]),
    tabel("Is dit een beoordelingsrij die enkel bij spreken en mondelinge interactie hoort?",
          [("lichaamstaal", J), ("spreektempo en vlotheid", J), ("uitspraak en intonatie", J), ("spelling en leestekengebruik", F)],
          "Spelling hoort bij schrijven."),
    keuze("Bij spreken worden onderbrekingen en valse starts [[*aanvaard|altijd afgestraft]].",
          "Je moet niet vloeiend klinken, je boodschap moet overkomen."),
    keuze("Bij uitspraak en intonatie [[*mag je een accent hebben, zolang de boodschap duidelijk blijft|moet je klinken als een moedertaalspreker]].",
          "Een accent mag."),
    tabel("Klinkt de ou als oe zoals in het Nederlandse boek?",
          [("rouge", J), ("jour", J), ("tout", J), ("moi", F)],
          "In moi klinkt oi als wa."),
    sorteer("Hoor je de laatste letter?", ["ja", "nee"],
            [("petit", "nee"), ("sac", "ja"), ("avec", "ja"), ("ils parlent (de -ent)", "nee")],
            "De slot-t van petit en de uitgang -ent hoor je niet."),
    tabel("Klinkt de c als een s of als een k?",
          [("cent", "s"), ("car", "k"), ("ciel", "s"), ("couleur", "k")],
          "Voor e en i klinkt c als s, voor a, o en u als k.",
          kolommen=["s", "k"]),
    keuze("In « garçon » zorgt de cédille dat de c klinkt als een [[*s|k]], ook al volgt er een o.",
          "Zonder cédille zou het een k-klank zijn."),
    tabel("Klopt dit over de Franse h?",
          [("Je hoort de h in heure niet.", J), ("Daarom schrijf je l'heure.", J), ("In hôtel spreek je de h luid uit.", F)],
          "De Franse h is stil."),
    keuze("« Il [[*a|à]] un vélo. » « Il va [[*à|a]] Bruxelles. »",
          "A is een vorm van avoir, à een voorzetsel."),
    keuze("« Tu habites [[*où|ou]] ? » « Thé [[*ou|où]] café ? »",
          "Où is waar, ou is of."),
    keuze("« Pose le sac [[*là|la]], sur [[*la|là]] table. »",
          "Là is daar; la is het lidwoord."),
    koppel("Welk accent hoort bij welk woord?",
           [("été", "accent aigu"), ("père", "accent grave"), ("français", "cédille"), ("où", "accent grave op de u")], ["geen accent"],
           "Het accent aigu helt naar rechts, het accent grave naar links."),
    keuze("De é in « été » klinkt [[*gesloten, zoals in beek|open, zoals in bed]].",
          "De è in père is open."),
    keuze("« J'ai [[*mangé|manger]] une pomme. » « Je vais [[*manger|mangé]] une pomme. »",
          "Na avoir komt het voltooid deelwoord, na aller de infinitief."),
    tabel("Schrijf je het lidwoord samengetrokken?",
          [("l'ami", J), ("l'école", J), ("l'heure", J), ("le garçon", F)],
          "Le en la worden l' voor een klinker of een stille h."),
    keuze("In het Frans valt de klemtoon meestal op [[*de laatste lettergreep|de eerste lettergreep]]: té-lé-PHONE.",
          "Anders dan in het Nederlands."),
    keuze("Zeg je « Tu viens ? » als vraag, dan laat je je stem op het einde [[*omhooggaan|dalen]].",
          "Intonatie maakt van een mededeling een vraag."),
    mk("Waarom vangt een spellingcontrole niet alle fouten op?",
       ["Ze ziet niet dat je ou schreef waar où moest.", "Ze werkt enkel in het Nederlands.", "Ze kent geen enkel Frans woord met een accent.", "Ze verbetert enkel de leestekens in een zin."], 0,
       "Ou en où zijn allebei echte woorden; de controle kent de bedoeling niet."),
    volgorde("Zet de stappen om een spreekopdracht voor te bereiden in een goede volgorde.",
             ["de opdracht goed lezen", "een spreekplan met kernwoorden maken", "luidop oefenen", "de opname maken en indienen"],
             "Plan, oefen, neem op."),
    inv("Hoe klinkt oi in « trois »? Schrijf de klank met twee letters.", ["wa"],
        "Moi, trois, voiture: oi klinkt als wa."),
]
