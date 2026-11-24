"""Persoonlijkheid: trekken, de big five en HEXACO — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen). Eigen vragen en een eigen
persoonlijkheidsprofiel, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Profiel van Lies op de Big Five ---------------------------------------------------------
PR = Prent("big-five-profiel", "Het profiel van Lies op de Big Five", "een liggend staafdiagram met vijf factoren en een score van laag tot hoog: openheid voor ervaringen hoog, zorgvuldigheid laag, extraversie hoog, vriendelijkheid middelmatig, neuroticisme laag")
FACT = [("openheid voor ervaringen", 0.9), ("zorgvuldigheid", 0.2), ("extraversie", 0.85),
        ("vriendelijkheid", 0.5), ("neuroticisme", 0.15)]
X0, X1 = 420, 900
PR.tekst(X0, 90, "laag", 18, "start", GRIJS)
PR.tekst(X1, 90, "hoog", 18, "end", GRIJS)
for i, (naam, w) in enumerate(FACT):
    y = 120 + i * 95
    PR.tekst(X0 - 20, y + 42, naam, 21, "end")
    PR.rect(X0, y + 10, X1 - X0, 50, "#f4f4f2", GRIJS, 6, 1)
    PR.rect(X0, y + 10, (X1 - X0) * w, 50, "#c4d5b5", DONKER, 6, 2)


def balk(i):
    return [Prent.zone(60, 120 + i * 95, X1 - 60, 70)]


VRAGEN = [
    klik("Klik op de factor die in HEXACO emotionaliteit heet.", PR.bestand, balk(4),
         "HEXACO gebruikt emotionaliteit waar de Big Five over neuroticisme spreekt."),
    klik("Klik op de factor die over orde, planning en doorzetten gaat.", PR.bestand, balk(1),
         "Zorgvuldigheid, in het Engels conscientiousness."),
    met_prent(PR.bestand, tabel("Wat past bij Lies volgens haar profiel?", [
        ("Ze zoekt graag nieuwe dingen en ideeën op.", J),
        ("Ze plant haar werk altijd netjes en ruim op tijd.", F),
        ("Ze is snel gespannen en bezorgd.", F),
        ("Ze zoekt graag gezelschap en prikkels.", J),
    ], "Hoog op openheid en extraversie, laag op zorgvuldigheid en neuroticisme.")),
    met_prent(PR.bestand, keuze("Op de as van neuroticisme ligt Lies dicht bij de pool [[*emotionele stabiliteit|neuroticisme]].",
              "Een lage score op neuroticisme betekent emotioneel stabiel.")),
    met_prent(PR.bestand, mk("Welke factor ontbreekt in dit profiel om er een HEXACO-profiel van te maken?",
              ["integriteit", "vriendelijkheid", "extraversie", "openheid"], 0,
              "HEXACO heeft zes factoren: de integriteit komt erbij.")),
    met_prent(PR.bestand, keuze("Dat Lies laag scoort op zorgvuldigheid betekent dat die factor bij haar [[*wel bestaat, maar laag is|niet bestaat|ziek is]].",
              "Een lage score is ook een score.")),
    tabel("Cardinale, centrale of secundaire trek?", [
        ("Een man is in alles wat hij doet bezig met gerechtigheid; het kleurt zijn hele leven.", "cardinaal"),
        ("Een vriendin is doorgaans grappig, eerlijk en behulpzaam.", "centraal"),
        ("Een rustige jongen wordt ongeduldig, maar enkel als hij in de file staat.", "secundair"),
    ], "Allport: overheersend, typerend in veel situaties, of enkel in bepaalde situaties.",
       kolommen=["cardinaal", "centraal", "secundair"]),
    keuze("Allport vond een cardinale trek [[*zeldzaam|heel gewoon|bij iedereen aanwezig]].",
          "De meeste mensen beschrijf je met centrale trekken."),
    inv("Hoe heet de grondlegger van de trektheoretische benadering? Familienaam.", ["Allport", "Gordon Allport"],
        "Gordon Allport."),
    koppel("Koppel elke letter van het PEN-model aan de as.", [
        ["P", "psychoticisme"],
        ["E", "extraversie"],
        ["N", "neuroticisme"],
    ], ["integriteit", "openheid"], "Drie assen van Eysenck."),
    tabel("Hoeveel factoren of assen heeft dit model?", [
        ("PEN-model", "3"),
        ("Big Five", "5"),
        ("HEXACO", "6"),
    ], "Eysenck drie, Costa en McCrae vijf, Lee en Ashton zes.", kolommen=["3", "5", "6"]),
    koppel("Koppel elk model aan de onderzoekers.", [
        ["PEN-model", "Eysenck"],
        ["Big Five", "Costa en McCrae"],
        ["HEXACO", "Lee en Ashton"],
        ["cardinale, centrale en secundaire trekken", "Allport"],
    ], ["Darley en Latané"], "Elk model hoort bij zijn makers."),
    casus(
        "Een bedrijf zoekt een boekhouder. De directeur wil vooral weten of de kandidaat ordelijk werkt, "
        "eerlijk omgaat met het geld van de zaak en niet in paniek slaat bij een drukke afsluiting.",
        [
            tabel("Welke factor meet wat de directeur wil weten?", [
                ("ordelijk werken", "zorgvuldigheid"),
                ("eerlijk omgaan met geld", "integriteit"),
                ("niet in paniek slaan", "emotionele stabiliteit"),
            ], "Drie verschillende factoren.", kolommen=["zorgvuldigheid", "integriteit", "emotionele stabiliteit"]),
            keuze("Omdat hij integriteit wil meten, gebruikt hij best het [[*HEXACO-model|Big Five-model|PEN-model]].",
                  "Enkel HEXACO heeft een eigen factor voor integriteit."),
            mk("Wat is een bezwaar als de directeur enkel naar de scores kijkt?",
               ["scores beschrijven, maar verklaren weinig",
                "scores bestaan enkel voor kinderen",
                "een lage score betekent dat iemand ziek is",
                "de factoren veranderen elke dag"], 0,
               "Een score zegt hoe iemand is, niet waarom."),
        ],
    ),
    sorteer("Komt deze factor in de Big Five én in HEXACO voor, of enkel in HEXACO?", ["In beide", "Enkel in HEXACO"], [
        ["extraversie", "In beide"],
        ["integriteit", "Enkel in HEXACO"],
        ["zorgvuldigheid", "In beide"],
        ["openheid voor ervaringen", "In beide"],
        ["vriendelijkheid", "In beide"],
    ], "Vier factoren zijn gelijk, één krijgt een andere naam en integriteit komt erbij."),
    tabel("Welke factor van de Big Five is het?", [
        ("Ze leest graag over verre culturen en probeert elk nieuw gerecht.", "openheid"),
        ("Hij helpt graag en gaat makkelijk mee met anderen.", "vriendelijkheid"),
        ("Ze is elke dag op tijd en houdt een strakke planning bij.", "zorgvuldigheid"),
    ], "Nieuwsgierigheid, meegaandheid, orde.", kolommen=["openheid", "vriendelijkheid", "zorgvuldigheid"]),
    mk("Een psycholoog zegt: 'Je bent niet introvert of extravert, je zit ergens op de lijn.' Waarom denkt een trektheorie zo?",
       ["de meeste mensen liggen ertussenin",
        "hokjes zijn moeilijker te tekenen",
        "een as heeft altijd precies vijf punten",
        "iedereen is volledig introvert of extravert"], 0,
       "Niemand is volledig introvert of volledig extravert."),
    tabel("Klopt dit?", [
        ("HEXACO verwerpt de Big Five volledig.", F),
        ("Een hoge score op neuroticisme betekent een ziekte.", F),
        ("Allport begon het denken in trekken, de Big Five verfijnde dat.", J),
        ("Het PEN-model heeft minder assen dan de Big Five.", J),
    ], "HEXACO bouwt verder op de Big Five; de assen beschrijven gewone verschillen."),
    sleep("De factor zorgvuldigheid heet in het Engels [[conscientiousness]]. De extra factor van HEXACO heet in het Engels [[honesty-humility]].",
          ["agreeableness", "openness"], "Twee Engelse namen uit de modellen."),
    keuze("Cross-cultureel onderzoek gaat na of de vijf factoren [[*overal terugkomen|enkel in Europa bestaan|elk jaar veranderen]].",
          "Als ze in veel culturen terugkomen, is het model sterker."),
    inv("Hoeveel factoren heeft HEXACO? Schrijf het getal.", ["6", "zes"],
        "De naam verwijst naar de zes beginletters."),
    klik("Klik op de factor waarop Lies het hoogst scoort.", PR.bestand, balk(0),
         "Openheid voor ervaringen is de langste balk."),
    keuze("Een hoog neuroticisme betekent sneller [[*gespannen en bezorgd|nieuwsgierig en open|ordelijk en plichtsbewust]] zijn.",
          "Neuroticisme meet hoe gevoelig iemand is voor stress en zorgen."),
    tabel("Welke soort trek bij Allport?", [
        ("komt enkel in bepaalde omstandigheden boven", "secundair"),
        ("vijf tot tien eigenschappen die iemand typeren", "centraal"),
        ("overheerst alles in iemands leven", "cardinaal"),
    ], "Drie soorten trekken.", kolommen=["cardinaal", "centraal", "secundair"]),
    inv("Welke factor meet hoe oprecht en bescheiden iemand is?", ["integriteit", "de integriteit"],
        "Integriteit, de extra factor van HEXACO."),
    mk("Wat wil een trektheorie in de eerste plaats doen?",
       ["vaste eigenschappen beschrijven",
        "het onbewuste blootleggen met dromen",
        "beloning en straf van gedrag meten",
        "de fasen van een groep voorspellen"], 0,
       "Een trektheorie beschrijft eerst."),
    keuze("Wie hoog scoort op extraversie, zoekt [[*veel|weinig]] gezelschap en prikkels.",
          "Extraversie staat tegenover introversie."),
    keuze("Lee en Ashton horen bij [[*HEXACO|de Big Five|het PEN-model]].",
          "Costa en McCrae horen bij de Big Five."),
    open_("Vergelijk de Big Five met HEXACO: wat is gelijk en wat verschilt?",
          "Vier factoren zijn gelijk: extraversie, vriendelijkheid, zorgvuldigheid en openheid voor ervaringen. Neuroticisme heet in HEXACO emotionaliteit. HEXACO heeft er een zesde factor bij: integriteit (honesty-humility). De Big Five is van Costa en McCrae, HEXACO van Lee en Ashton."),
]
