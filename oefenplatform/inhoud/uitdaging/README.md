# Uitdaging: één verdiepingshoofdstuk per vak

Voor de kinderen die de gewone hoofdstukken vlot afwerken staat er per vak één
extra hoofdstuk klaar: **Uitdaging — alles door elkaar**, twintig moeilijkere
vragen die de hoofdstukken van dat vak door elkaar halen.

Het zijn er elf: zes voor 🌱 Start (wiskunde, Nederlands, geschiedenis,
aardrijkskunde, Engels, wetenschap en techniek) en vijf voor ✨ Spark (wiskunde,
Nederlands, geschiedenis, natuurwetenschappen, Frans). Samen 220 vragen.

## Wat maakt een vraag hier moeilijker?

Geen nieuwe leerstof. Alles staat op wat in de gewone hoofdstukken van dat vak
al aan bod komt, zodat de leerbundels blijven kloppen. Moeilijker wordt het door
de manier van vragen:

- **twee stappen** in plaats van één (eerst 25 % korting, dan nog eens 10 %);
- **omgekeerd denken** (je kent het gemiddelde en zoekt het ontbrekende cijfer);
- **twee hoofdstukken verbinden** (de heirbanen en het internet, de maan en het
  aantal maanden in een jaar);
- **een besluit trekken** uit wat er staat (welk kengetal geeft het eerlijkste
  beeld, wat mag je uit één Romeinse munt afleiden);
- **een veelgemaakte fout** die er juist uitziet (eerst +10 % en dan −10 % is
  niet hetzelfde als nul).

## Importeren

Elk bestand bevat **één** hoofdstuk en gaat via **Beheer → Vakken → het vak →
vragen importeren**, met het vinkje **"Bestaande vragen vervangen" aan**. Dat is
veilig: het bestand raakt alleen dit ene nieuwe hoofdstuk aan, en importeer je
per ongeluk een tweede keer, dan staat er nóg altijd twintig vragen in plaats
van veertig. De voortgang van de andere hoofdstukken blijft dus onaangeroerd.

| Bestand | Vak | Niveau |
|---------|-----|--------|
| `start-wiskunde-uitdaging.json` | Wiskunde | 🌱 Start |
| `start-nederlands-uitdaging.json` | Nederlands | 🌱 Start |
| `start-geschiedenis-uitdaging.json` | Geschiedenis | 🌱 Start |
| `start-aardrijkskunde-uitdaging.json` | Aardrijkskunde | 🌱 Start |
| `start-engels-uitdaging.json` | Engels | 🌱 Start |
| `start-wetenschap-en-techniek-uitdaging.json` | Wetenschap en techniek | 🌱 Start |
| `spark-wiskunde-uitdaging.json` | Wiskunde | ✨ Spark |
| `spark-nederlands-uitdaging.json` | Nederlands | ✨ Spark |
| `spark-geschiedenis-uitdaging.json` | Geschiedenis | ✨ Spark |
| `spark-natuurwetenschappen-uitdaging.json` | Natuurwetenschappen | ✨ Spark |
| `spark-frans-uitdaging.json` | Frans | ✨ Spark |

Er is **geen SQL** voor nodig. In het oefenplatform staat het vakje achteraan in
de rij hoofdstukken van dat vak, met een oranje randje en het label "Extra
uitdaging" (`components/HoofdstukTegels.tsx` herkent elke titel die met
"Uitdaging" begint).

## Bijwerken

De vragen staan in `bron/<niveau>_<vak>.py`. Draai daarna:

    python3 inhoud/uitdaging/bron/bouw_uitdaging.py            # alles
    python3 inhoud/uitdaging/bron/bouw_uitdaging.py spark_frans  # één vak

Het script schrijft pas een bestand als alles klopt. Het kijkt na of er twintig
vragen zijn, of elke vraag uitleg heeft, of een antwoord binnen de opties valt,
of er geen vraag dubbel staat, en of er niet te raden valt (hoogstens vier op de
tien meerkeuzevragen met de langste optie als antwoord, en tussen 35 en 65
procent van de waar-of-niet-vragen op waar — dezelfde grenzen als
`inhoud/controleer_patronen.py`). Bij een rekenvraag mag je een veld `reken`
meegeven met de berekening; het script rekent die zelf uit en vergelijkt ze met
het antwoord dat in de vraag staat.

Bij wiskunde weigert het script meerkeuzevragen met meerdere juiste antwoorden;
bij de andere vakken van ✨ Spark mogen die wel.
