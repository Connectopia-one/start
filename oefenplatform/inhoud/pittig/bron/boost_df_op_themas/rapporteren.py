"""Rapporteren en respectvol omgaan — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_rapporteren: mondeling en schriftelijk, intern en extern
rapporteren, waarden en normen, en positief en opbouwend omgaan met anderen:
diversiteit, respect, gevoelige onderwerpen, emoties en privacy. Met een
zelfgetekend rapport."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, LICHTGROEN

RP = Prent("rapport-opvang", "Rapport van de naschoolse opvang", "een rapport met vijf lijnen, letters A tot E")
RP.rect(60, 60, 880, 540, "#ffffff", DONKER, 8, 3)
RP.rect(60, 60, 880, 50, LICHTGROEN, DONKER, 8, 3)
RP.tekst(90, 93, "Teamschrift, groep De Uilen", 19, "start")
LIJNEN = [("A", "Datum: woensdag 3 maart, 14.20 uur"),
          ("B", "Aanwezig: begeleider Sanne en Jamal (8)"),
          ("C", "Jamal valt van het klimrek en schaaft zijn linkerknie."),
          ("D", "Volgens mij krijgt hij thuis te weinig aandacht."),
          ("E", "Mama om 14.35 uur gebeld; ze haalt hem om 16 uur op.")]
Z = {}
for i, (t, zin) in enumerate(LIJNEN):
    y = 175 + i * 88
    RP.letter(110, y - 7, t)
    RP.tekst(150, y, zin, 21, "start")
    Z[t] = [Prent.zone(85, y - 42, 840, 70)]
U = "rapport-opvang.svg"

OPVANG = ("Lees de situatie.\n\n"
          "Je werkt in de naschoolse opvang. Mats (9) vertelt je in vertrouwen dat zijn ouders gaan scheiden. Hij is stil en wil niet mee voetballen. "
          "Een andere mama vraagt je aan de poort: 'Wat is er met Mats? Hij is zo stil.' 's Avonds overleg je met je verantwoordelijke.")

VRAGEN = [
    klik("Bekijk het rapport. Klik op de lijn die niet in een rapport hoort.", U, Z["D"], "Een rapport blijft bij de feiten; je eigen oordeel hoort er niet in."),
    klik("Klik op de lijn die toont wie erbij was.", U, Z["B"], "Wat, wanneer en wie: zo is het rapport controleerbaar."),
    sorteer("Interne of externe rapportering?", ["intern", "extern"],
            [("een overdracht aan de collega van de avondploeg", "intern"), ("een verslag voor de huisarts", "extern"), ("een notitie in het teamschrift", "intern"), ("een brief aan de ouders", "extern"), ("een melding aan het CLB", "extern"), ("een bespreking op de teamvergadering", "intern")],
            "Intern blijft binnen de werking; extern gaat naar buiten."),
    sorteer("Mondeling of schriftelijk rapporteren?", ["mondeling", "schriftelijk"],
            [("je vertelt op het teamoverleg wat er gebeurde", "mondeling"), ("je vult het digitale dossier aan", "schriftelijk"), ("je belt de mama even op", "mondeling"), ("je schrijft in het heen-en-weerschriftje", "schriftelijk")],
            "Schriftelijk blijft bestaan en kan je later nalezen."),
    tabel("Waarde of norm?",
          [("eerlijkheid", "waarde"), ("je mag niet liegen", "norm"), ("respect", "waarde"), ("je laat iemand uitspreken", "norm"), ("vrijheid", "waarde"), ("je klopt aan voor je binnengaat", "norm")],
          "Een waarde is wat je belangrijk vindt, een norm is hoe je dan handelt.", ["waarde", "norm"]),
    casus(OPVANG, [
        mk("Wat antwoord je de andere mama?",
           ["Dat kan ik niet met u bespreken, maar bedankt voor uw bezorgdheid.", "Zijn ouders gaan scheiden, dus wees maar wat lief voor hem.", "Ik weet het niet, vraag het maar aan de andere ouders aan de poort.", "Hij heeft het thuis moeilijk, maar zeg het aan niemand verder."],
           0, "Wat je over een kind weet, blijft bij wie het nodig heeft."),
        keuze("Wat je 's avonds aan je verantwoordelijke vertelt, is [[*interne|externe]] rapportering.", "Het blijft binnen de eigen werking."),
        keuze("Een scheiding thuis is een [[*gevoelig onderwerp|vooroordeel|norm]].", "Ziekte, geld, een scheiding of een overlijden vragen voorzichtigheid."),
        mk("Hoe reageer je het best op Mats?",
           ["'Ik zie dat je stil bent. Wil je praten of liever iets rustigs doen?'", "'Kom, niet zo flauw doen, iedereen gaat mee voetballen, ook jij vandaag.'", "'Scheidingen gebeuren heel vaak, dus daar moet je echt niet over piekeren.'", "'Ik ga dit aan de andere kinderen vertellen, dan begrijpen ze je beter.'"],
           0, "Je benoemt wat je ziet en laat hem zelf kiezen, zonder aan te dringen."),
        keuze("Dat je niets doorvertelt aan de andere mama, heeft te maken met [[*privacy en het beroepsgeheim|positieve feedback|een vooroordeel]].", "Je zwijgt over wat je door je werk te weten komt."),
    ]),
    tabel("Hoort dit bij een veilige sfeer in een groep?",
          [("fouten maken mag", J), ("enkel de beste kinderen mogen meedoen", F), ("de afspraken hangen zichtbaar aan de muur", J), ("wie iets fout zegt, wordt uitgelachen", F)],
          "Wie weet wat mag en niet uitgelachen wordt, voelt zich veilig."),
    mk("Waarom hoort je eigen oordeel niet in een rapport?",
       ["een rapport moet controleerbaar zijn voor anderen", "een oordeel is altijd fout", "rapporten mogen maximaal drie korte zinnen tellen, niet meer", "ouders lezen nooit een rapport"],
       0, "Feiten kan een ander nakijken, een oordeel niet."),
    keuze("Uit de waarde [[*respect|snelheid|winst]] volgt de norm dat je iemand laat uitspreken.", "Normen komen uit waarden."),
    keuze("Een begeleider denkt dat een jongen met een hoodie wel lastig zal zijn, nog voor hij hem kent. Dat is een [[*vooroordeel|norm|waarde]].", "Een oordeel zonder kennis."),
    mk("Een kind is boos en schopt tegen een stoel. Wat zeg je eerst?",
       ["'Ik zie dat je heel boos bent.'", "'Stop daarmee, of je moet in de hoek.'", "'Boos zijn mag hier nooit.'", "'Waarom doe je toch altijd zo raar?'"],
       0, "Een emotie benoemen geeft het kind het gevoel dat het gezien wordt."),
    inv("Hoe noem je rapportering naar iemand buiten de eigen werking, zoals een arts of het CLB? Eén woord.", ["extern", "externe rapportering", "externe"], "Externe rapportering."),
    tabel("Is dit opbouwend omgaan met een kind?",
          [("je start bij wat het kind al kan", J), ("je somt al zijn fouten op", F), ("je benoemt zijn sterktes", J), ("je beslist alles in zijn plaats", F)],
          "Opbouwend begint bij mogelijkheden en sterktes."),
    keuze("Een gezin viert andere feesten dan jij gewend bent. Openstaan voor diversiteit betekent dat [[*die verschillen er mogen zijn|zij zich moeten aanpassen|je het gesprek vermijdt]].", "Verschillen krijgen plaats."),
    mk("Met wie deel je dat een kind van de opvang diabetes heeft?",
       ["met de collega's die voor hem zorgen", "met alle ouders van de groep", "met niemand, ook niet met je collega's", "met de buren van het kind"],
       0, "Enkel met wie die informatie nodig heeft om goed te zorgen."),
    sleep("Wat iemand belangrijk vindt, noem je zijn [[waarden]]. De regels die daaruit volgen, noem je [[normen]]. Waarden verschillen door [[cultuur]] en opvoeding.",
          ["privacy", "feiten"],
          "Daarom verschillen waarden van gezin tot gezin."),
    keuze("Een schriftelijk rapport is belangrijk omdat het [[*blijft bestaan en na te lezen is|sneller is dan praten|geen datum nodig heeft]].", "Wat op papier staat, kan later opgevolgd worden."),
    tabel("Klopt dit over privacy?",
          [("Je praat thuis aan tafel over de kinderen van je stage, met hun naam.", F), ("Je deelt informatie enkel met wie ze nodig heeft.", J), ("Een foto van een kind van de opvang zet je zomaar op je sociale media.", F), ("Het beroepsgeheim geldt voor wat je door je werk te weten komt.", J)],
          "Gegevens blijven binnen."),
    keuze("'Ik zie dat je verdrietig bent' is een manier om de [[*emoties|normen|feiten]] van een kind te benoemen.", "Het kind voelt zich gezien."),
    mk("Welke zin toont respect voor een kind?",
       ["'Wat vind jij ervan? Jij mag mee kiezen.'", "'Ik heb al beslist, jij moet gewoon volgen.'", "'Wacht, ik praat nu met een volwassene, niet met jou.'", "'Doe maar wat je wil, het kan mij niet schelen.'"],
       0, "Zijn mening vragen en mee laten beslissen."),
    keuze("Een verslag dat je naar de logopedist van het kind stuurt, is [[*extern|intern]].", "Het gaat naar iemand buiten de eigen werking."),
    mk("Waarom zet je een datum en een uur in een rapport?",
       ["zodat anderen kunnen nagaan wanneer het gebeurde", "omdat het rapport dan mooier oogt", "omdat dat eigenlijk de enige regel is die er voor rapporten bestaat", "zodat niemand het rapport nog kan lezen"],
       0, "Zo is het rapport controleerbaar."),
    keuze("Een kind vertelt over de ziekte van zijn oma. Je [[*gaat er voorzichtig op in en dringt niet aan|verandert snel van onderwerp|vraagt meteen alle details]].", "Je neemt het ernstig, in je eigen woorden."),
    tabel("Speelt dit mee in de waarden van een gezin?",
          [("cultuur", J), ("geloof", J), ("de kleur van het huis", F), ("opvoeding", J)],
          "Ook ervaring speelt mee."),
    inv("Wat moet een rapport bevatten in plaats van meningen? Eén woord.", ["feiten", "de feiten"], "Feiten."),
    open_("Schrijf een korte, objectieve notitie voor het teamschrift: een kind van zes is vandaag tijdens de middag gevallen op de speelplaats.",
          "Dinsdag 12 mei, 12.40 uur. Aanwezig: begeleider Ann en Lou (6). Lou struikelt bij het lopen op de speelplaats en schaaft haar rechterhand. Wonde gereinigd. Papa om 12.55 uur gebeld."),
]
