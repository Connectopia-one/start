"""micro — pittig (🚀 Boost dubbele finaliteit, natuurwetenschappen).

Hergebruikt de pittige vragen van natuurwetenschappen 🚀 Boost doorstroom (met
hun prenten), zonder wat de fiche van de dubbele finaliteit niet vraagt."""
from ..boost_do_nw_themas import micro as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [0, 3] + list(range(10, 22)) + [23, 24, 25, 26, 27])
VRAGEN += [
    sorteer("Welke vorm heeft deze bacterie?", ["bolvormig", "staafvormig", "spiraalvormig"],
            [("een kok", "bolvormig"), ("een bacil", "staafvormig"), ("een spiril", "spiraalvormig"), ("streptokokken in een ketting", "bolvormig")],
            "Kokken zijn bolvormig, bacillen staafvormig en spirillen spiraalvormig."),
    tabel("Welke onderdelen vind je terug bij een bacterie?",
          [("een celwand", J), ("een celmembraan", J), ("een kern met een kernmembraan", F), ("erfelijk materiaal los in het cytoplasma", J)],
          "Een bacterie heeft geen echte kern: haar erfelijk materiaal ligt vrij in het cytoplasma."),
    casus("Onder de microscoop zie je drie organismen. Organisme 1 is eencellig, heeft geen kern en deelt door celsplitsing. Organisme 2 is eencellig, heeft een kern en vormt uitstulpingen. Organisme 3 bestaat uit lange draden met sporenhoofdjes.", [
        tabel("Wat is elk organisme?",
              [("organisme 1", "bacterie"), ("organisme 2", "gist"), ("organisme 3", "schimmel")],
              "Celsplitsing zonder kern: bacterie; knopvorming: gist; draden: schimmel.",
              ["bacterie", "gist", "schimmel"]),
        inv("Hoe noem je de manier waarop organisme 2 zich vermeerdert?", ["knopvorming", "knopvorming of sprossing", "sprossing"],
            "Een gistcel vormt een kleine uitstulping die loskomt."),
    ]),
    tabel("Klopt dit over virussen?",
          [("Een virus bestaat uit erfelijk materiaal in een eiwitmantel.", J), ("Een virus kan zich enkel in een gastheercel vermeerderen.", J), ("Een bacteriofaag is een virus dat bacteriën aanvalt.", J), ("Een virus heeft een celwand.", F)],
          "Een virus is geen cel; het heeft een gastheer nodig."),
    koppel("Langs welke weg dringt dit micro-organisme binnen?",
           [("griepvirus", "via de luchtwegen"), ("salmonellabacterie in rauw ei", "via het spijsverteringskanaal"), ("tetanusbacterie", "via een wonde"), ("voetschimmel", "via de huid")],
           ["via het haar"], "Micro-organismen komen via de huid, de luchtwegen, het spijsverteringskanaal of een wonde binnen."),
    keuze("Een organisme dat zonder zuurstof kan leven, leeft [[*anaëroob|aëroob|autotroof]].",
          "An- betekent zonder; gisten kunnen anaëroob suiker omzetten."),
    mk("Waarom zijn handen wassen en niezen in je elleboog zo doeltreffend?",
       ["Ze breken de weg van de ziekteverwekker.", "Ze doden alle virussen in je hele lichaam.", "Ze maken je immuunsysteem meteen sterker.", "Ze werken in je lichaam net zoals een vaccin."], 0,
       "Wie de overdracht breekt, voorkomt besmetting."),
    tabel("Welke groeivoorwaarden heeft een bacterie nodig om snel te vermeerderen?",
          [("voedsel", J), ("vocht", J), ("een geschikte temperatuur", J), ("felle uv-straling", F)],
          "Bewaringstechnieken nemen net een van die voorwaarden weg."),
]
