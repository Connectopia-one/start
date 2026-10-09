/*
  In de kijker: filmpjes, artikels en berichten die we delen.

  Kim op 9 oktober 2026: "hiermee delen we allemaal leuke filmpjes en artikels
  die te maken hebben met HB UHB ass of adhd of combo en iedereen kan hier
  zijn leuk ding delen". Het gaat dus niet over berichten over ons.

  Twee wegen leiden naar deze pagina, en je kiest zelf welke je gebruikt.

  1. VIA HET OUDERPORTAAL (de gewone manier)
     Ga naar Beheer, In de kijker. Daar zet je een bericht erbij, laad je er
     een beeld bij op en keur je een bericht goed dat iemand anders instuurde.
     Daar moet niemand code voor aanraken.

  2. VIA DIT BESTAND (als je toch liever hier werkt)
     Zet onderaan in de lijst "vastePosts" een blokje bij. Die berichten
     staan altijd vooraan op de pagina, boven de berichten uit de databank.

       {
         tekst: "Wat er in het bericht staat.",
         van: "Connectopia",                     wie het postte
         kanaal: "facebook",                     facebook | instagram |
                                                 linkedin | tiktok |
                                                 youtube | anders
         link: "https://www.facebook.com/...",   het echte bericht
         titel: "Kamp in de herfstvakantie",     optionele kop
         datum: "2026-10-01",                    optioneel, jaar-maand-dag
         eigen: true,                            een bericht van onszelf
         beeld: {
           bestand: "kamp-herfst.jpg",           in  public/in-de-kijker/
           beschrijving: "Twee kinderen bouwen een robot",
         },
       }

  Een beeld bij een bericht uit dit bestand zet je in  public/in-de-kijker/
  en hier vul je alleen de bestandsnaam in.

  WAAROM WE GEEN ECHTE FACEBOOK- EN INSTAGRAMVENSTERS GEBRUIKEN
  Die plaatsen cookies bij elke bezoeker, ook bij wie niets aanklikt, en dan
  moet er een cookiebanner op de site. Daarom maken we van elk bericht een
  eigen kaartje in onze stijl, met een knop naar het echte bericht. Niemand
  wordt gevolgd, en de pagina blijft even snel als de rest van de site.
*/

export type Kanaal =
  | "facebook"
  | "instagram"
  | "linkedin"
  | "tiktok"
  | "youtube"
  | "anders";

export type Post = {
  tekst: string;
  van: string;
  kanaal: Kanaal;
  link: string;
  titel?: string;
  datum?: string;
  eigen?: boolean;
  beeld?: { bestand: string; beschrijving: string };
};

/*
  Hoe een kanaal op het kaartje heet. Een kanaal dat hier niet in staat,
  valt terug op "Online".
*/
export const kanalen: Record<Kanaal, string> = {
  facebook: "Facebook",
  instagram: "Instagram",
  linkedin: "LinkedIn",
  tiktok: "TikTok",
  youtube: "YouTube",
  anders: "Online",
};

export const inkijker = {
  label: "In de kijker",
  titel: "Filmpjes en artikels die we delen",
  handgeschreven: "Jij mag er ook een bijzetten!",
  tekst:
    "Een filmpje dat het eindelijk eens goed uitlegt, een artikel dat je wil doorsturen, een podcast die deugd doet: alles over hoogbegaafdheid, uitzonderlijke hoogbegaafdheid, autisme, ADHD of een combinatie daarvan komt hier samen. Iedereen mag er een bijzetten.",

  /* De zin op de pagina zolang er nog geen enkel bericht op staat. */
  leegTekst:
    "Hier komen binnenkort de eerste filmpjes en artikels. Kwam jij iets tegen dat anderen moeten zien? Stuur het gerust in.",

  /* De knop op elk kaartje. */
  bekijkKnop: "Bekijken",

  spelregels: {
    titel: "Hoe deze pagina werkt",
    punten: [
      "Elk kaartje brengt je naar het filmpje, het artikel of het bericht zelf. We nemen niets over, we verwijzen ernaar.",
      "Het gaat over hoogbegaafdheid, autisme, ADHD of een combinatie daarvan, en het brengt iets bij of het doet gewoon deugd.",
      "Wat wij zelf delen staat er meteen op. Wat jij instuurt, komt erop nadat we het bekeken hebben.",
      "Geen reclame, en geen kritiek op scholen, organisaties of personen. Dat is dezelfde afspraak als op het prikbord.",
      "Geen namen of foto's van kinderen zonder de toestemming van hun ouders, ook niet als ze in het oorspronkelijke bericht staan.",
    ],
  },

  formulier: {
    titel: "Stuur jouw vondst in",
    tekst:
      "Kwam je een filmpje, een artikel of een bericht tegen dat anderen moeten zien? Stuur de link hier in, dan zetten we het erbij. We bekijken het eerst, dus het staat er niet meteen op.",
    linkLabel: "De link naar het filmpje of artikel",
    linkUitleg:
      "Het volledige adres van het bericht, dus beginnend met https://.",
    tekstLabel: "Waar gaat het over?",
    tekstUitleg:
      "Een paar zinnen volstaan, dat komt op het kaartje te staan. Schrijf er gerust bij waarom het jou raakte.",
    vanLabel: "Van wie is het?",
    vanUitleg:
      "Wie het maakte of waar het staat, zoals het op het kaartje mag komen: een naam, een krant, een kanaal.",
    kanaalLabel: "Waar staat het?",
    naamLabel: "Jouw volledige naam",
    naamUitleg: "Voor ons, zodat we weten met wie we te doen hebben.",
    mailLabel: "Jouw e-mailadres",
    mailUitleg: "Ook voor ons. We gebruiken het alleen om je iets te vragen.",
    privacy:
      "Je volledige naam en je e-mailadres komen niet op de website. Ze blijven bij ons, zodat we je kunnen bereiken als er iets niet klopt.",
    knopTekst: "Insturen",
    /* Wat er bovenaan staat nadat iemand op Insturen klikte. */
    gelukt:
      "Bedankt! We bekijken het en zetten het erbij, meestal binnen een paar dagen.",
    mislukt:
      "Dat is niet gelukt. Probeer het later nog eens, of mail het ons gewoon.",
    foutLink:
      "Die link lijkt niet te kloppen. Hij moet met https:// beginnen en naar het filmpje of het artikel zelf verwijzen.",
    foutTekst: "Schrijf even in een paar woorden waar het over gaat.",
    foutNaam: "Vul je naam in, zowel die op het kaartje als je volledige naam.",
    foutMail: "Vul een e-mailadres in waarop we je kunnen bereiken.",
    /* Zolang de databank nog niet klaarstaat, staat dit er in de plaats. */
    nogNiet:
      "Insturen kan hier nog niet. Mail je link gerust naar ons, dan zetten we hem erbij.",
  },

  /*
    De berichten die je hier zelf bijzet. Ze staan vooraan op de pagina,
    boven wat uit de databank komt. Laat je deze lijst leeg, dan staan er
    alleen de berichten uit het ouderportaal.
  */
  vastePosts: [] as Post[],
};
