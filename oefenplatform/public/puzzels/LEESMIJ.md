# De prenten voor de puzzel

Eén prent per hoofdstuk, voor de legpuzzel op de eindhalte van de tocht
(`/vakken/<vak>/<nummer>/leerbundel`). Kim maakt ze met ChatGPT.

**Waarom prenten en niet de tekeningen uit de leerbundel.** Die tekeningen zijn
schema's: een rooster, een tijdbalk, een stroomkring. Een stukje van een rooster
ziet er precies hetzelfde uit als het stukje ernaast, dus dan valt er niets te
puzzelen. Met een echte prent wel.

## Hoe een prent bij zijn hoofdstuk komt

Aan de bestandsnaam. `public/puzzels/<vak>/<hoofdstuk>.webp`, allebei
vereenvoudigd zoals `lib/slug.ts` het doet. Er is geen kolom in de databank en
geen SQL voor nodig.

Anders dan bij de leerbundels telt " — pittig" hier **wel** mee: een pittig
hoofdstuk heeft zijn eigen prent.

## Een nieuwe reeks klaarzetten

Krijg je losse prenten, noem ze dan naar het hoofdstuk en zet ze klaar:

    python3 inhoud/puzzels/bron/maak_puzzelfotos.py <vak> <map met prenten>

Krijg je één beeld met alle hoofdstukken erop naast elkaar (ChatGPT maakt dat
graag), snij het dan eerst:

    python3 inhoud/puzzels/bron/snij_blad.py <blad.png> <map>

Dat levert `01.png`, `02.png` … in leesvolgorde. Hernoem ze naar de titels en
laat er daarna `maak_puzzelfotos.py` over gaan. Dat script verkleint tot
hoogstens 900 px breed, bewaart als webp en schrijft `inhoud/puzzelfotos.ts`
opnieuw. Draai het ook los (zonder argumenten) als je zelf een bestand
toevoegde of weghaalde.

## Waar op te letten

- **Een uitgesneden vakje is klein** (rond de 300 px). Dat werkt, maar een losse
  prent van 1024 px ziet er merkbaar scherper uit. Een prent die telt, maak je
  dus beter apart.
- **Reken na wat erop staat.** Een beeldmaker zet zonder moeite een pizza in zes
  stukken met "1/2" erbij. In het hoofdstuk breuken merkt een kind dat meteen.
- Een prent die veel breder is dan hoog (meer dan 2,6 keer) wordt overgeslagen:
  het bord wordt dan een strookje met flinterdunne stukjes.
