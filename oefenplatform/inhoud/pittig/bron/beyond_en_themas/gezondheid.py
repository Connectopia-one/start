"""Woordvelden: gezondheid, natuur en duurzaamheid — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the text.\n\n"
    "Last week I felt a bit under the weather: a sore throat, a headache and no energy at all. "
    "After three days I booked an appointment with my GP. She gave me a check-up and said it was just a virus, "
    "so there was no need for antibiotics. She advised rest, plenty of water and a balanced diet. "
    "However, because the headache did not go away, she wrote a referral to a specialist, just to be safe. "
    "Two weeks later I had made a full recovery."
)

TEKST2 = (
    "Read the text.\n\n"
    "The hedgehog population in Britain has fallen by half since 2000. Hedgehogs lose their habitat when hedges are removed "
    "and gardens are covered with paving. Pesticides also kill the insects they feed on. "
    "Conservation groups now ask people to cut a small hole in their garden fence, so that hedgehogs can move from garden to garden. "
    "They also warn against litter: hedgehogs often get stuck in single-use plastic. "
    "Although the species is not yet endangered, experts fear it soon could be."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            mk(
                "Waarom kreeg de schrijver geen antibiotica?",
                ["Het was een virus", "Hij was allergisch voor antibiotica", "De apotheek was die dag gesloten", "Hij wou liever geen medicijnen"],
                0,
                "It was just a virus, so there was no need for antibiotics.",
            ),
            mk(
                "Waarom schreef de huisarts een verwijzing?",
                ["De hoofdpijn bleef", "De keelpijn werd veel erger", "Hij had uitslag op zijn armen", "Hij had nieuwe medicijnen nodig"],
                0,
                "Because the headache did not go away … a referral to a specialist.",
            ),
            tabel(
                "Raadde de huisarts dit aan?",
                [
                    ("rusten", J),
                    ("veel water drinken", J),
                    ("antibiotica nemen", F),
                    ("gezond en gevarieerd eten", J),
                ],
                "Rest, plenty of water and a balanced diet.",
            ),
            keuze(
                "Na twee weken was de schrijver [[*helemaal genezen|nog altijd ziek]].",
                "A full recovery is een volledig herstel.",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            mk(
                "Welke oorzaken van de achteruitgang noemt de tekst?",
                ["Minder leefgebied en voedsel", "Te veel egels in de Britse tuinen", "Te koude en lange winters", "Ziektes die van honden komen"],
                0,
                "Habitat loss en pesticides that kill the insects they feed on.",
            ),
            mk(
                "Waarom vragen natuurorganisaties om een gat in je omheining?",
                ["Zodat egels kunnen doorlopen", "Zodat je buren je tuin kunnen zien", "Zodat regenwater kan weglopen", "Zodat er meer insecten in je tuin komen"],
                0,
                "So that hedgehogs can move from garden to garden.",
            ),
            keuze(
                "Volgens de tekst is de egel [[*nog niet|al]] een bedreigde soort.",
                "Although the species is not yet endangered.",
            ),
            inv(
                "Met hoeveel is het aantal egels sinds 2000 gedaald? Antwoord als breuk of percentage.",
                ["de helft", "1/2", "50%", "50 %", "50", "half"],
                "Has fallen by half.",
            ),
        ],
    ),
    koppel(
        "Koppel elk Engels woord aan zijn vertaling.",
        [
            ("a side effect", "een bijwerking"),
            ("a prescription", "een voorschrift"),
            ("a carer", "een mantelzorger"),
            ("a rash", "uitslag op de huid"),
        ],
        ["een ziekenhuis"],
        "Hospital zou ziekenhuis zijn.",
    ),
    sorteer(
        "Hernieuwbaar of niet?",
        ["Hernieuwbaar", "Niet hernieuwbaar"],
        [
            ("solar power", "Hernieuwbaar"),
            ("coal", "Niet hernieuwbaar"),
            ("wind power", "Hernieuwbaar"),
            ("natural gas", "Niet hernieuwbaar"),
            ("hydropower", "Hernieuwbaar"),
        ],
        "Fossil fuels raken op; wind, zon en water niet.",
    ),
    tabel(
        "Klopt deze vertaling?",
        [
            ("a drought – een overstroming", F),
            ("wildlife – dieren en planten in het wild", J),
            ("crops – gewassen", J),
            ("a cub – een lammetje", F),
        ],
        "A drought is een droogte; a cub is het jong van een roofdier.",
    ),
    mk(
        "« I think I'm coming down with the flu. » Wat bedoelt de spreker?",
        ["Ze wordt ziek", "Ze is net genezen", "Ze gaat naar beneden", "Ze heeft een vaccin gekregen"],
        0,
        "To come down with: iets onder de leden krijgen.",
    ),
    mk(
        "« He has been on medication for his anxiety. » Wat betekent dat?",
        ["Hij neemt medicijnen", "Hij ligt in het ziekenhuis", "Hij werkt in een apotheek", "Hij is gestopt met medicijnen"],
        0,
        "To be on medication; anxiety is angst.",
    ),
    mk(
        "« Since the holidays I've put on three kilos. » Wat gebeurde er?",
        ["Bijgekomen", "Drie kilo vermagerd", "Drie kilo boodschappen gekocht", "Drie kilometer gelopen"],
        0,
        "To put on weight is bijkomen.",
    ),
    mk(
        "Welke zin is correct Brits Engels?",
        ["She is in hospital.", "She is in the hospital of the NHS.", "She is at hospital now.", "She is on the hospital."],
        0,
        "In het Brits Engels zonder lidwoord: in hospital.",
    ),
    mk(
        "« Our company has gone green. » Wat betekent dat?",
        ["Milieuvriendelijker", "Het logo is groen geschilderd", "Het bedrijf is failliet gegaan", "Het bedrijf verkoopt groenten"],
        0,
        "To go green: milieuvriendelijker werken.",
    ),
    mk(
        "Wat betekent « to reduce your carbon footprint »?",
        ["Minder CO₂ uitstoten", "Minder vaak wandelen in het bos", "Kleinere schoenen kopen", "Minder steenkool verkopen aan anderen"],
        0,
        "Carbon footprint is je CO₂-voetafdruk.",
    ),
    volgorde(
        "Zet de drie R's van duurzaamheid in de volgorde van hoe goed ze zijn, beste eerst.",
        ["reduce", "reuse", "recycle"],
        "Minder gebruiken is beter dan hergebruiken, en dat is beter dan recycleren.",
    ),
    keuze(
        "« I've been under a lot of stress lately. » De spreker heeft [[*veel|weinig]] stress.",
        "To be under stress is onder druk staan.",
    ),
    keuze(
        "« Mental health » betekent [[*geestelijke gezondheid|een psychische ziekte]].",
        "Mental illness zou een psychische ziekte zijn.",
    ),
    inv(
        "Vul aan met één Engels woord: « During the ___ the river burst its banks and many houses were flooded. »",
        ["flood"],
        "A flood is een overstroming.",
    ),
    inv(
        "Vul aan met één Engels woord: « Please don't drop ___ in the park; use the bins. »",
        ["litter", "rubbish", "waste"],
        "Litter is zwerfvuil.",
    ),
    mk(
        "« The doctor referred me to a specialist. » Wat deed de dokter?",
        ["Doorverwijzen", "Hij gaf me een voorschrift voor pillen", "Hij belde een ambulance voor me", "Hij gaf me een volledige controle"],
        0,
        "To refer: doorverwijzen. A referral is een verwijzing.",
    ),
    mk(
        "« My grandmother needs a carer three times a day. » Wat heeft ze nodig?",
        ["Iemand die voor haar zorgt", "Een auto om rond te rijden", "Een kaart om te betalen", "Een huisdier als gezelschap"],
        0,
        "A carer zorgt voor iemand.",
    ),
    tabel(
        "Is dit een klacht waarmee je naar de huisarts gaat?",
        [
            ("a sore throat", J),
            ("a heatwave", F),
            ("an earache", J),
            ("a habitat", F),
        ],
        "Ache is een aanhoudende pijn: earache, headache.",
    ),
    keuze(
        "« We should conserve water during the drought. » We moeten water [[*sparen|weggooien]].",
        "To conserve: sparen, behoeden.",
    ),
    inv(
        "Vul aan met één Engels woord: « Getting eight hours of ___ a night is good for your health. »",
        ["sleep"],
        "Sleep is ook het naamwoord.",
    ),
    mk(
        "« Coping strategies » helpen je om …",
        ["met moeilijkheden om te gaan", "sneller te kunnen lopen", "je huiswerk te kopiëren", "medicijnen te bestellen"],
        0,
        "To cope with: omgaan met.",
    ),
    sleep(
        "Een bedreigde soort is an [[endangered]] species. Een dier verliest zijn [[habitat]] als het bos verdwijnt. Steenkool en aardolie zijn [[fossil]] fuels.",
        ["renewable", "extinct"],
        "Extinct zou uitgestorven zijn.",
    ),
    open_(
        "Schrijf in het Engels twee tips om op school minder single-use plastic te gebruiken.",
        "Bring a reusable water bottle instead of buying plastic bottles. Use a lunchbox instead of wrapping your sandwiches in cling film.",
    ),
]
