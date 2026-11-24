"""Pittige hoofdstukken bij geschiedenis 🌍 Beyond dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen in de vormen van het examen van
de Examencommissie. Kim op 24 november 2026: er is vraag naar geschiedenis,
dus ook de dubbele finaliteit krijgt pittige hoofdstukken. Geen extra
leerstof: alles staat in de leerbundels van geschiedenis Beyond dubbele
finaliteit (leerbundels/bron/maak_geschiedenis_beyond_df.py). Waar een thema
overeenkomt met Beyond doorstroom, hergebruiken we vragen uit
beyond_geschiedenis_themas/ en de prenten in /examenvormen/geschiedenis-beyond.
"""
import importlib
import importlib.util

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Geschiedenis"
BESTAND = "beyond-df-geschiedenis-pittig.json"
AANTAL = 30

THEMAS = [
    ("referentiekader", "Het historisch referentiekader: tijd, ruimte en domeinen"),
    ("vergelijken", "Kenmerken van samenlevingen vergelijken"),
    ("wenen", "Restauratie en revolutie: het Congres van Wenen"),
    ("liberalisme", "Liberalisme en nationalisme"),
    ("belgie", "Het ontstaan van België"),
    ("industrie", "De eerste en de tweede industriële revolutie"),
    ("ongelijkheden", "Ongelijkheden: klassenmaatschappij en sociale strijd"),
    ("marxisme", "Marxisme, sociaaldemocratie, christendemocratie en migratie"),
    ("imperialisme", "Modern imperialisme en de wedloop om Afrika"),
    ("congo", "Congo: van Congo-Vrijstaat tot Belgisch Congo"),
    ("wo1", "De Eerste Wereldoorlog en de Vrede van Versailles"),
    ("interbellum", "Het interbellum: de opkomst van het totalitarisme"),
    ("wo2", "De Tweede Wereldoorlog en de Holocaust"),
    ("china", "China: van keizerrijk tot wereldmacht"),
    ("wereldorde", "Een nieuwe wereldorde: de Verenigde Naties en de Koude Oorlog"),
    ("europa", "De Europese eenmaking"),
    ("dekolonisatie", "De dekolonisatie van Congo"),
    ("belgie_na_1945", "België na 1945: breuklijnen, federale staat en emancipatie"),
    ("kunst", "Kunst en cultuur: een kunstwerk analyseren"),
    ("bronnen", "Redeneren met bronnen: bruikbaarheid en betrouwbaarheid"),
    ("beeldvorming", "Beeldvorming, standplaatsgebondenheid en betekenisgeving"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__}.beyond_df_geschiedenis_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if importlib.util.find_spec(f"{__package__}.beyond_df_geschiedenis_themas.{naam}")
]
