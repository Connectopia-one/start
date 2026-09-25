/*
  De drie kaarten "ontdek verder", onderaan de winactiepagina en op de
  bedanktpagina na een verstuurd formulier.

  Waarom: wie via een bericht op sociale media binnenkomt, landt rechtstreeks
  op één pagina en ziet de rest van de site nooit. Net na het inschrijven is
  het moment waarop iemand het meest geneigd is om nog verder te kijken.

  Aanpassen mag zonder code: de titels, de tekstjes en de knoppen staan hier.
*/

export const verder = {
  /* Onderaan de winactiepagina. */
  titel: "En wie zijn wij dan?",
  tekst:
    "Het oefenplatform is maar één stuk van wat we doen. Connectopia vzw begeleidt kinderen met een ontwikkelingsvoorsprong, ASS of ADHD, en de mensen rond hen.",

  /* Op de bedanktpagina, na een verstuurd formulier. */
  bedanktTitel: "Ondertussen",
  bedanktTekst:
    "Je hoeft zelf niets meer te doen. Als je zin hebt om verder te kijken:",

  kaarten: [
    {
      titel: "Ons aanbod",
      tekst:
        "De externe plusklas, de pluswerkingen in Hasselt en Genk, Young Engineers en een kamp in elke schoolvakantie.",
      link: "/aanbod",
      knop: "Bekijk het aanbod",
    },
    {
      titel: "Over Connectopia",
      tekst:
        "Waar we vandaan komen, waarom we dit doen en wie je tegenkomt als je langskomt.",
      link: "/over-ons",
      knop: "Leer ons kennen",
    },
    {
      titel: "Waar kan je terecht?",
      tekst:
        "Een gids met plekken en mensen die verder helpen bij een vermoeden of een diagnose.",
      link: "/waar-kan-je-terecht",
      knop: "Naar de gids",
    },
  ],
};
