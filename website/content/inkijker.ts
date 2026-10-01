/*
  In de kijker: berichten van sociale media op de website.

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
  titel: "Wat er over ons rondgaat",
  handgeschreven: "Deel het gerust verder!",
  tekst:
    "Berichten van onze eigen pagina's en van mensen die over ons schreven, op één plek bij elkaar. Klik op een kaartje om het echte bericht te openen, en deel het daar verder als je wil.",

  /* De zin op de pagina zolang er nog geen enkel bericht op staat. */
  leegTekst:
    "Hier komen binnenkort de eerste berichten. Heb jij er een over ons gemaakt? Stuur hem gerust in.",

  /* De knop op elk kaartje. */
  bekijkKnop: "Open het bericht",

  spelregels: {
    titel: "Hoe deze pagina werkt",
    punten: [
      "Elk kaartje linkt naar het echte bericht. Daar kan je het liken, becommentariëren en verder delen.",
      "Berichten van onszelf staan er meteen op. Een bericht van iemand anders komt er pas op nadat wij het gelezen hebben.",
      "We zetten er alleen berichten op waarvan de maker het goed vindt. Vraag je om het weg te halen, dan is het diezelfde dag weg.",
      "Geen namen of foto's van kinderen zonder de toestemming van hun ouders, ook niet als ze in het oorspronkelijke bericht staan.",
    ],
  },

  formulier: {
    titel: "Stuur je bericht in",
    tekst:
      "Schreef je iets over ons op Facebook, Instagram of LinkedIn? Stuur het hier in, dan zetten we het erbij. We lezen het eerst, dus het staat er niet meteen op.",
    linkLabel: "De link naar je bericht",
    linkUitleg:
      "Het volledige adres van het bericht, dus beginnend met https://.",
    tekstLabel: "Waar gaat het over?",
    tekstUitleg: "Een paar zinnen volstaan. Dat komt op het kaartje te staan.",
    vanLabel: "Van wie is het bericht?",
    vanUitleg:
      "Zoals het op het kaartje mag staan: jouw voornaam, of de naam van je zaak of organisatie.",
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
      "Bedankt! We lezen je bericht na en zetten het erbij, meestal binnen een paar dagen.",
    mislukt:
      "Dat is niet gelukt. Probeer het later nog eens, of mail het ons gewoon.",
    foutLink:
      "Die link lijkt niet te kloppen. Hij moet met https:// beginnen en naar het bericht zelf verwijzen.",
    foutTekst: "Schrijf even in een paar woorden waar het bericht over gaat.",
    foutNaam: "Vul je naam in, zowel die op het kaartje als je volledige naam.",
    foutMail: "Vul een e-mailadres in waarop we je kunnen bereiken.",
    /* Zolang de databank nog niet klaarstaat, staat dit er in de plaats. */
    nogNiet:
      "Insturen kan hier nog niet. Mail je bericht gerust naar ons, dan zetten we het erbij.",
  },

  /*
    De berichten die je hier zelf bijzet. Ze staan vooraan op de pagina,
    boven wat uit de databank komt. Laat je deze lijst leeg, dan staan er
    alleen de berichten uit het ouderportaal.
  */
  vastePosts: [] as Post[],
};
