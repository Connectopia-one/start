# -*- coding: utf-8 -*-
"""Ready geschiedenis en maatschappij: Samenleven (regels en afspraken, rechten van het
kind, de gemeente en de burgemeester, België met koning en regering, feesten en
gewoonten, respect voor elkaar). Doelen einde 4de leerjaar."""
from vr import mk, inv, wn

TITEL = "Samenleven"
UITLEG_1 = "Regels, afspraken en kinderrechten."
UITLEG_2 = "Gemeente, België en feesten."

DEEL_1 = [
    mk("Waarom zijn er regels in de klas?", ["zodat iedereen veilig kan leren", "om de juf en de meester te plagen", "omdat het moet van de buren", "om de lessen saai te maken"], 0, "Afspraken zorgen ervoor dat iedereen zich goed voelt."),
    wn("Kinderen hebben rechten.", True, "In het Kinderrechtenverdrag staan de rechten van alle kinderen."),
    mk("Welk recht hebben alle kinderen?", ["het recht om te leren", "het recht om nooit te slapen", "het recht om alles te kopen wat je wil", "het recht om auto te rijden"], 0, "Elk kind heeft recht op onderwijs."),
    inv("Kinderen hebben ook het recht om te ___. (s...)", ["spelen"], "Spelen en rusten is een kinderrecht."),
    wn("Een kind mag gepest worden als het anders is.", False, "Elk kind heeft recht op bescherming. Pesten is nooit oké."),
    mk("Wat doe je als je ziet dat iemand gepest wordt?", ["Je zegt het aan een volwassene.", "Je lacht mee.", "Je kijkt snel de andere kant op.", "Je doet mee."], 0, "Hulp halen is moedig en juist."),
    wn("Regels in het verkeer zorgen voor veiligheid.", True, "Door rood licht stoppen en voorrang geven voorkomt ongelukken."),
    mk("Wat betekent respect hebben voor iemand?", ["Je bent vriendelijk en eerlijk.", "Je doet alsof die persoon er niet is.", "Je lacht hem uit.", "Je neemt zijn spullen."], 0, "Respect is iemand behandelen zoals je zelf behandeld wil worden."),
    inv("Een afspraak die voor iedereen in een land geldt, heet een ___. (w...)", ["wet"], "Wetten worden gemaakt door het parlement."),
    wn("Alle kinderen in de wereld zijn even belangrijk.", True, "Elk kind heeft dezelfde rechten, waar het ook woont."),
    mk("Wat is een klasraad?", ["een overleg in de klas", "een groep leraren die toetsen maakt", "een feestje op school", "een soort tafel"], 0, "In de klasraad bespreek je samen wat goed gaat en wat beter kan."),
    wn("Als je het niet eens bent, mag je slaan.", False, "Praat erover, zoek samen een oplossing of vraag hulp."),
    mk("Wat doe je als je een fout gemaakt hebt tegenover iemand?", ["Je zegt sorry.", "Je doet alsof er niets gebeurd is.", "Je geeft de schuld aan een ander.", "Je loopt weg."], 0, "Sorry zeggen en het goedmaken is belangrijk."),
    inv("Vrijheid van ___ betekent dat iedereen zijn mening mag zeggen. (m...)", ["meningsuiting"], "Vrijheid van meningsuiting is een belangrijk recht, als je anderen respecteert."),
    wn("Kinderen hebben het recht om gehoord te worden over dingen die over hen gaan.", True, "Ook kinderen mogen hun mening geven."),
    mk("Welke afspraak hoort NIET in een klas?", ["Wie het eerst roept, mag alles beslissen.", "We luisteren naar elkaar.", "We ruimen samen op.", "We helpen elkaar."], 0, "Samen beslissen en naar elkaar luisteren is eerlijker."),
    wn("Thuis zijn er nooit afspraken.", False, "Ook thuis zijn er afspraken, bijvoorbeeld over bedtijd."),
    mk("Wat is Kinderrechtendag?", ["20 november", "de verjaardag van de koning", "de eerste schooldag", "Nieuwjaar"], 0, "Op 20 november 1989 werd het Kinderrechtenverdrag goedgekeurd."),
    wn("Regels kunnen nooit veranderen.", False, "Als een regel niet meer goed werkt, kan je hem samen aanpassen."),
    wn("Iedereen is anders, en dat is oké.", True, "Verschillen maken een groep net rijker."),
]

DEEL_2 = [
    mk("Wie is de baas van een gemeente?", ["de burgemeester", "de koning", "de directeur van de school", "de bakker"], 0, "De burgemeester leidt de gemeente samen met de schepenen."),
    mk("Waar werkt de burgemeester?", ["in het gemeentehuis", "in het ziekenhuis", "in de bakkerij om de hoek", "op school"], 0, "In het gemeentehuis of stadhuis regelt men zaken van de gemeente."),
    wn("België heeft een koning.", True, "België is een koninkrijk. Koning Filip is het staatshoofd."),
    inv("Hoe heet de koning van België? Koning ___.", ["Filip", "Philippe"], "Koning Filip is koning sinds 2013."),
    mk("Wie maakt de wetten in België?", ["het parlement", "de burgemeester alleen", "de kinderen van het 4de leerjaar", "de politie"], 0, "Het parlement stemt over de wetten."),
    mk("Wanneer is de nationale feestdag van België?", ["21 juli", "1 januari", "25 december", "11 november"], 0, "Op 21 juli 1831 legde de eerste koning, Leopold I, de eed af."),
    wn("De Belgische vlag is zwart, geel en rood.", True, "Drie verticale banen: zwart, geel en rood."),
    mk("Welk feest vieren veel kinderen in België op 6 december?", ["Sinterklaas", "Pasen", "Halloween", "Kerstmis"], 0, "Op 6 december brengt Sinterklaas cadeautjes."),
    inv("Op 25 december vieren veel mensen ___.", ["Kerstmis", "kerst", "Kerst"], "Kerstmis viert men op 25 december."),
    wn("Iedereen in België viert precies dezelfde feesten.", False, "Mensen hebben verschillende godsdiensten en gewoonten, zoals het Suikerfeest of Chanoeka."),
    mk("Welk feest sluit de vastenmaand ramadan af?", ["het Suikerfeest", "Pasen", "Carnaval", "Kerstmis"], 0, "Moslims vieren het Suikerfeest na de ramadan."),
    mk("Wat doet de politie?", ["zorgen voor veiligheid", "brood bakken", "huizen bouwen", "lesgeven in de lagere school"], 0, "De politie helpt mensen en zorgt dat iedereen zich aan de regels houdt."),
    wn("De brandweer komt enkel bij brand.", False, "De brandweer helpt ook bij ongevallen, overstromingen en als iemand vastzit."),
    inv("Het noodnummer voor brandweer en ziekenwagen in België is ___.", "112", "Bel 112 bij een noodgeval.", 112),
    mk("Wat betekent stemmen bij verkiezingen?", ["kiezen wie bestuurt", "zingen in een koor", "een nieuw liedje leren", "een spel spelen"], 0, "Volwassenen kiezen wie hen vertegenwoordigt."),
    wn("Op 11 november herdenken we het einde van de Eerste Wereldoorlog.", True, "Op 11 november 1918 eindigde de Eerste Wereldoorlog."),
    mk("Wat is een gewoonte?", ["iets wat je telkens weer doet", "iets wat je maar één keer in je leven doet", "een soort kleding", "een wet"], 0, "Bijvoorbeeld: elke zondag bij oma gaan eten."),
    wn("Carnaval is een feest met verkleden en optochten.", True, "In Aalst en Binche zijn er bekende carnavalsstoeten."),
    mk("Waarom betalen volwassenen belastingen?", ["Voor wegen, scholen en ziekenhuizen.", "Om de koning en de koningin rijk te maken.", "Omdat het een spel is.", "Om snoep te kopen."], 0, "Met belastingen betaalt men dingen die we samen gebruiken."),
    wn("Kinderen van 9 jaar mogen stemmen bij de verkiezingen voor de gemeente.", False, "Bij de gemeenteraadsverkiezingen stemmen volwassenen vanaf 18 jaar."),
]


# Prentvragen (vraag 21 tot 24), Kim 26/11.
from vr import mk, inv, wn
import prent as P
PRENT_1 = [
    mk("Wat betekent dit verkeersbord?", ["Verboden voor fietsers", "Hier is een fietspad", "Hier kan je je fiets zetten", "Fietsen te koop"], 0, "Een rond bord met een rode rand is een verbod. De fiets erin: geen fietsers.", prent=P.p_verkeersbord("samenleven-geen-fietsers", "geen-fietsers")),
    mk("Wat zie je op de prent?", ["een zebrapad", "een fietspad", "een parking", "een speelplaats"], 0, "Witte strepen op de weg: een zebrapad. Daar steek je over.", prent=P.p_verkeersbord("samenleven-zebrapad", "zebrapad")),
    wn("Bij dit bord mag je doorrijden zonder te stoppen.", False, "Bij een stopbord moet je helemaal stoppen en kijken.", prent=P.p_verkeersbord("samenleven-stop", "stop")),
    inv("Elk kind heeft recht op een veilige t... om te wonen.", ["thuis"], "Elk kind heeft recht op een thuis. Dat staat in de kinderrechten.", prent=P.p_voorwerp("samenleven-huis", "huis")),
]
PRENT_2 = [
    mk("Bij welk feest hoort deze boom?", ["Kerstmis", "Pasen", "Carnaval", "Sinterklaas"], 0, "Met Kerstmis versieren veel mensen een kerstboom.", prent=P.p_ding("samenleven-kerstboom", "kerstboom")),
    inv("Bij welk feest zoeken kinderen naar deze eieren?", ["Pasen", "pasen"], "Met Pasen zoeken kinderen paaseieren.", prent=P.p_ding("samenleven-paaseieren", "paaseieren")),
    wn("Dit is de vlag van Nederland.", False, "Zwart, geel en rood, rechtop: dit is de vlag van België.", prent=P.p_vlag("samenleven-vlag-be", ["#222", "#f5c400", "#d0453a"])),
    mk("Waar vraag je een identiteitskaart aan?", ["in het gemeentehuis", "in de bakkerij", "in de sporthal", "in het zwembad"], 0, "Voor een identiteitskaart ga je naar het gemeentehuis.", prent=P.p_ding("samenleven-gemeentehuis", "gemeentehuis")),
]
