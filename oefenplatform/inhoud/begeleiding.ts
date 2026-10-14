/*
  De opvolgfiches van de plusklas — /begeleiding

  Hieronder staan enkel de vaste teksten van die schermen. De fiches zelf
  (kinderen, opmerkingen, documenten) staan in de databank, niet in dit
  bestand. Je mag deze teksten gerust aanpassen.

  Wie deze schermen ziet: jij als beheerder, en accounts waarvan je de rol op
  "begeleider" zet via /beheer/begeleiders. Ouders en kinderen zien er niets
  van, ook niet hun eigen fiche.
*/

export const begeleidingTekst = {
  label: "Begeleiding",
  titel: "Opvolging plusklas",
  intro:
    "Hier volg je de kinderen van de plusklas apart op: hoe ver ze staan, wat jullie opvalt, en het werk dat ze thuis maakten. Alleen jij en de begeleiders zien dit scherm.",
  leegTekst:
    "Nog geen kinderen van de plusklas. Een kind verschijnt hier zodra het gezin met een plusklascode geregistreerd is en een kind toegevoegd heeft.",

  /*
    Het overzicht met de groepen. Elke actieve code krijgt een eigen scherm,
    zodat de plusklas van Hasselt niet door de testgezinnen loopt. Een gezin
    hoort bij de code waarmee het registreerde; zie supabase/groepen.sql.
  */
  groepen: {
    titel: "Opvolging",
    intro:
      "Elke code is een eigen groep. Klik bovenaan op een groep en je ziet alleen de kinderen die met die code registreerden.",
    leeg: "Er zijn nog geen codes. Maak er een aan bij Beheer, Plusklas-codes, en deel ze met de gezinnen.",
    filterLabel: "Kies een groep",
    zonderGroepTitel: "Nog geen groep",
    zonderGroepUitleg:
      "Deze gezinnen registreerden voor de groepen bestonden, dus weten we niet met welke code. Open de fiche van een kind en kies daar de juiste groep.",
    terug: "Terug naar de opvolging",
    groepLeeg: "Nog geen kinderen in deze groep.",
    inactief: "Niet meer actief",
    /*
      Welke soort opvolging deze groep krijgt. Kim op 14 oktober 2026: enkel de
      kindjes van de plusklas van Hasselt volgt ze in detail op; van de andere
      groepen wil ze de voortgang in een tabel zien, zonder zware opvolging.
      Het vinkje per code staat bij Beheer, Plusklas-codes.
    */
    volleOpvolging: "Volle opvolging",
    volleOpvolgingUitleg:
      "Van deze groep houd je alles bij: per kind een fiche met de voortgang per hoofdstuk, de opgeloste testen, jullie opmerkingen en het werk van thuis.",
    enkelTabel: "Enkel de voortgang",
    enkelTabelUitleg:
      "Van deze groep houd je enkel de voortgang bij, in de tabel hieronder. Geen fiche, geen opmerkingen en geen werk van thuis. Wil je een groep toch in detail opvolgen, zet dan het vinkje bij Beheer, Plusklas-codes.",
    laatstKop: "Laatst geoefend",
    nooit: "nog niet gestart",
  },

  /* Het keuzelijstje op de fiche waarmee je een gezin naar een groep zet. */
  groepKiezen: {
    kop: "Groep",
    uitleg:
      "Bij welke groep hoort dit gezin? Verandert dit, dan schuiven alle kinderen van het gezin mee.",
    geen: "Nog geen groep",
    bewaren: "Bewaren",
    alleenBeheerder:
      "Alleen de beheerder kan een gezin naar een andere groep zetten.",
  },

  /* Het scherm van één kind. */
  fiche: {
    /* Staat deze groep op "enkel de voortgang", dan blijft de fiche bij de
       tabel: geen opgeloste testen, geen opmerkingen, geen werk van thuis. */
    examensKop: "Afgelegde examens",
    examensUitleg:
      "De examens over een heel vak. Die staan los van de voortgang hierboven: een examen kleurt geen vinkjes in. Drie keer feilloos geeft de examenster van dat vak.",
    lichtKop: "Enkel de voortgang",
    lichtUitleg:
      "Dit gezin hoort bij een groep die je niet in detail opvolgt, dus hieronder staat enkel wat het kind al maakte. Wil je er opmerkingen, werk van thuis en de opgeloste testen bij, zet dan het vinkje Volle opvolging bij Beheer, Plusklas-codes, of zet dit gezin hierboven bij de plusklasgroep.",
    notitiesKop: "Opmerkingen",
    notitiesUitleg:
      "Wat jullie opvalt tijdens een sessie, een afspraak die je maakte, of wat je op een oudercontact wil zeggen. Ouders lezen dit niet mee.",
    notitiesLeeg: "Nog geen opmerkingen genoteerd.",
    documentenKop: "Werk van thuis",
    documentenUitleg:
      "Pdf's van oefeningen of opdrachten die het kind thuis maakte, om er later bij te nemen.",
    documentenLeeg: "Nog geen documenten opgeladen.",
    voortgangKop: "Voortgang op het platform",
    testenLink: "Opgeloste testen bekijken",
    voortgangLeeg: "Dit kind heeft nog geen vragen beantwoord op het platform.",
    stickersKop: "Verdiende stickers",
    afdrukTekst: "Deze fiche afdrukken",
  },

  /*
    De soorten opmerking. De sleutel moet overeenkomen met wat de databank
    toelaat (zie supabase/plusklasfiche.sql), dus voeg er niet zomaar een toe.
  */
  soorten: [
    { waarde: "opmerking", label: "Opmerking" },
    { waarde: "afspraak", label: "Afspraak" },
    { waarde: "oudercontact", label: "Voor het oudercontact" },
  ] as const,
};

export type NotitieSoort = (typeof begeleidingTekst.soorten)[number]["waarde"];
