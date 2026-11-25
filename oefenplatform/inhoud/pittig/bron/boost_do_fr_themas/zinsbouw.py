"""Soorten zinnen, bijzinnen en si-zinnen — pittig (🚀 Boost doorstroom, Frans).

Eigen vragen strikt binnen fr_zinsbouw: soorten zinnen, de vraag, de
ontkenning, de uitroep, zinsdelen en woordvolgorde, neven- en onderschikking,
voegwoorden, betrekkelijke bijzinnen, si-zinnen en voorzetsels bij plaatsen
en vervoer. Met een zelfgetekende zin in blokjes."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS

ZB = Prent("zin-in-blokjes-frans", "Une phrase en morceaux", "een lange Franse zin in blokjes over drie regels")
RIJEN = [(140, ["Comme", "il", "pleuvait,", "nous", "sommes", "restés"]),
         (300, ["à la maison", "et", "ma sœur", "a", "lu", "un livre"]),
         (460, ["que", "mon oncle", "lui", "avait", "offert."])]
BLOK = {}
for y, woorden in RIJEN:
    x = 60
    for w in woorden:
        b = max(70, len(w) * 17 + 34)
        ZB.rect(x, y, b, 80, "#f7f4ea", DONKER, 10, 3)
        ZB.tekst(x + b / 2, y + 50, w, 26)
        BLOK[w] = (x, y, b)
        x += b + 18
U = "zin-in-blokjes-frans.svg"


def zb(w):
    x, y, b = BLOK[w]
    return Prent.zone(x, y, b, 80)


VRAGEN = [
    klik("Bekijk de zin. Klik op alle persoonsvormen.", U, [zb("pleuvait,"), zb("sommes"), zb("a"), zb("avait")],
         "Pleuvait, sommes, a en avait: vier persoonsvormen, dus vier delen in de zin."),
    klik("Klik op het nevenschikkende voegwoord.", U, [zb("et")], "Et verbindt twee zinnen die elk alleen kunnen staan."),
    klik("Klik op het voegwoord dat een reden geeft.", U, [zb("Comme")], "Comme vooraan in de zin: omdat."),
    klik("Klik op het betrekkelijk voornaamwoord.", U, [zb("que")], "Que: het boek dat mijn oom haar gegeven had."),
    sorteer("Welke soort zin?", ["vragend", "bevelend", "uitroepend", "ontkennend"],
            [("Viens-tu demain ?", "vragend"), ("Fermez la porte.", "bevelend"), ("Quel beau temps !", "uitroepend"), ("Il ne vient jamais.", "ontkennend"), ("Comme c'est drôle !", "uitroepend"), ("Où habites-tu ?", "vragend")],
            "Quel, comme en que leiden een uitroep in."),
    inv("Maak een vraag met omkering: il parle français. Twee woorden met streepjes.", ["Parle-t-il", "parle-t-il"], "Tussen twee klinkers komt een -t-."),
    tabel("Is de vraag juist gebouwd?",
          [("Est-ce que vous venez ?", J), ("Venez-vous ?", J), ("Est-ce que venez-vous ?", F), ("A-t-elle fini ?", J)],
          "Kies est-ce que of de omkering, niet allebei."),
    sorteer("Welke ontkenning?", ["ne … jamais", "ne … plus", "ne … rien", "ne … personne"],
            [("nooit", "ne … jamais"), ("niet meer", "ne … plus"), ("niets", "ne … rien"), ("niemand", "ne … personne")],
            "Ne … toujours bestaat niet als ontkenning."),
    keuze("Ik heb niets gezien: Je [[*n'ai rien vu|n'ai vu rien|ne rien ai vu]].", "Rien staat rond het hulpwerkwoord, zoals pas."),
    keuze("Ik zie niemand: Je ne vois [[*personne|pas personne|personne pas]].", "Personne vervangt pas."),
    keuze("[[*Quelle|Quel|Quelle une]] bonne idée !", "Idée is vrouwelijk; in een uitroep geen lidwoord."),
    tabel("Klopt dit over zinnen en zinsbouw?",
          [("In het Frans staat er een spatie voor een vraagteken.", J), ("Een samengestelde zin heeft maar één persoonsvorm.", F), ("Het werkwoord komt overeen met het onderwerp.", J), ("Je vois le is de juiste volgorde.", F)],
          "Je le vois: het voornaamwoord komt vooraan."),
    sorteer("Nevenschikkend of onderschikkend voegwoord?", ["nevenschikkend", "onderschikkend"],
            [("mais", "nevenschikkend"), ("parce que", "onderschikkend"), ("donc", "nevenschikkend"), ("quand", "onderschikkend"), ("car", "nevenschikkend"), ("bien que", "onderschikkend")],
            "Mais, ou, et, donc, or, ni, car."),
    sorteer("Wat geeft het voegwoord aan?", ["tijd", "reden", "doel"],
            [("dès que", "tijd"), ("pendant que", "tijd"), ("parce que", "reden"), ("comme (vooraan)", "reden"), ("pour que", "doel")],
            "Pour que vraagt bovendien de subjonctif."),
    keuze("Je travaille dur [[*pour|pour que]] réussir mon examen.", "Zelfde onderwerp: pour + infinitief."),
    keuze("Je travaille dur [[*pour que|pour]] mes parents soient fiers.", "Ander onderwerp: pour que + subjonctif."),
    sorteer("Welk soort si-zin?", ["echte mogelijkheid", "onwerkelijk"],
            [("S'il fait beau, j'irai à la mer.", "echte mogelijkheid"), ("Si j'étais riche, j'achèterais une maison.", "onwerkelijk"), ("Si tu viens, on regardera un film.", "echte mogelijkheid"), ("Si nous avions une voiture, nous partirions.", "onwerkelijk")],
            "Si + présent → futur; si + imparfait → conditionnel."),
    inv("Vul in: S'il (pleuvoir) demain, nous resterons à la maison. Eén werkwoordsvorm.", ["pleut"], "Si + présent, dan futur."),
    inv("Vul in: Si j'(avoir) le temps, je t'aiderais. Eén werkwoordsvorm.", ["avais"], "Si + imparfait, dan conditionnel."),
    mk("Welke si-zin is juist?",
       ["Si tu étudiais plus, tu réussirais.", "Si tu étudierais plus, tu réussirais.", "Si tu étudieras plus, tu réussiras.", "Si tu étudiais plus, tu réussiras."],
       0, "Na si nooit een futur of conditionnel; imparfait gaat samen met conditionnel."),
    sleep("Mijn reis: J'habite [[à]] Gand, en [[en]] Belgique. Cet été, je vais [[au]] Portugal, puis [[aux]] Pays-Bas.",
          ["dans", "du"], "À bij steden, en bij vrouwelijke landen, au bij mannelijke, aux bij een meervoud."),
    keuze("Il pleut, donc je reste à la maison. Dat is een [[*nevenschikking|onderschikking]].", "Allebei de delen kunnen alleen staan."),
    mk("Waarom helpt het om de persoonsvormen te tellen in een lange Franse zin?",
       ["zo zie je uit hoeveel delen de zin bestaat", "zo weet je hoeveel woorden er in de zin staan", "zo vind je meteen het onderwerp van de tekst", "zo weet je welke tijd de schrijver gebruikt"],
       0, "Elke persoonsvorm hoort bij een eigen deel."),
    keuze("Voilà le café [[*où|que|dont]] nous nous sommes rencontrés.", "Een plaats: où."),
    volgorde("Zet de woorden in de juiste volgorde voor: 'Ik heb het hem niet gegeven.'",
             ["Je", "ne", "le", "lui", "ai", "pas", "donné."],
             "Ne vooraan, dan de voornaamwoorden, dan het hulpwerkwoord, dan pas, dan het deelwoord."),
    open_("Schrijf in het Frans een si-zin over iets onwerkelijks: wat zou je doen als je een dag vrij had?",
          "Si j'avais un jour de congé, je dormirais longtemps et j'irais au cinéma avec mes amis."),
    keuze("Les élèves de ma classe [[*parlent|parle]] beaucoup.", "Het onderwerp is les élèves, niet ma classe."),
    inv("Vul in: Cet été, nous allons … Marseille. Eén woord.", ["à"], "Bij steden altijd à."),
    mk("'Comme il faisait froid, nous avons allumé le feu.' Wat betekent comme hier?",
       ["omdat", "zoals", "hoewel", "terwijl"],
       0, "Comme vooraan in de zin geeft een reden."),
    keuze("Je ne bois [[*plus de|plus du|pas plus de]] café le soir.", "Na een ontkenning wordt du gewoon de."),
]
