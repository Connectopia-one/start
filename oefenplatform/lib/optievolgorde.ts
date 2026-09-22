/**
 * Zet de opties van een meerkeuzevraag in een vaste, eerlijk verdeelde volgorde.
 *
 * Waarom dit bestaat: wie vragen schrijft zet het juiste antwoord bijna vanzelf
 * vooraan, en merkt dat bij nalezen niet. In de bestanden van het platform stond
 * het juiste antwoord bij sommige vakken op meer dan negen van de tien vragen op
 * de eerste plaats. Een kind dat altijd het bovenste aanklikt haalt dan een hoge
 * score zonder iets te kennen, en leert op de verkeerde dingen te letten.
 *
 * Het rechtzetten gebeurt hier, bij het tonen, en niet in de vragen zelf. Zo
 * hoeft er niets opnieuw geïmporteerd te worden — wat de kinderen al
 * beantwoordden blijft gewoon staan — en geldt het meteen voor alle vragen die
 * er later bij komen.
 *
 * De volgorde volgt uit het id van de vraag, dus ze ligt vast: een kind dat de
 * pagina herlaadt of later terugkomt, ziet dezelfde volgorde, en een ouder die
 * meekijkt ziet hetzelfde als zijn kind.
 */

/** Een klein, voorspelbaar willekeurig getal uit een tekst (FNV-1a). */
function zaad(tekst: string): number {
  let h = 0x811c9dc5;
  for (let i = 0; i < tekst.length; i++) {
    h ^= tekst.charCodeAt(i);
    h = Math.imul(h, 0x01000193);
  }
  return h >>> 0;
}

/** Losse getallen uit dat zaad, zodat de volgorde elke keer dezelfde is. */
function teller(begin: number): () => number {
  let t = begin;
  return () => {
    t = (t + 0x6d2b79f5) >>> 0;
    let x = Math.imul(t ^ (t >>> 15), 1 | t);
    x = (x + Math.imul(x ^ (x >>> 7), 61 | x)) ^ x;
    return ((x ^ (x >>> 14)) >>> 0) / 4294967296;
  };
}

export type SchikbareVraag = {
  id: string;
  type: string;
  opties: string[] | null;
  antwoord: number | string | boolean;
};

/**
 * Geeft de vraag terug met geschudde opties, het antwoordnummer dat bij die
 * nieuwe volgorde hoort, en `optieVolgorde`: per getoonde plaats het nummer dat
 * de optie in de databank heeft. Dat laatste is nodig om het antwoord van een
 * kind op te slaan zoals het altijd al opgeslagen werd, zodat de pagina waar
 * ouders meekijken blijft kloppen.
 *
 * Vragen die geen meerkeuze zijn, of waar iets niet klopt aan de opties, komen
 * ongewijzigd terug met `optieVolgorde: null`.
 */
export function schikOpties<T extends SchikbareVraag>(
  vraag: T
): T & { optieVolgorde: number[] | null } {
  const opties = vraag.opties;
  if (
    vraag.type !== "meerkeuze" ||
    !Array.isArray(opties) ||
    opties.length < 2 ||
    typeof vraag.antwoord !== "number" ||
    !Number.isInteger(vraag.antwoord) ||
    vraag.antwoord < 0 ||
    vraag.antwoord >= opties.length
  ) {
    return { ...vraag, optieVolgorde: null };
  }

  const volgend = teller(zaad(vraag.id));
  const volgorde = opties.map((_, i) => i);
  for (let i = volgorde.length - 1; i > 0; i--) {
    const j = Math.floor(volgend() * (i + 1));
    [volgorde[i], volgorde[j]] = [volgorde[j], volgorde[i]];
  }

  return {
    ...vraag,
    opties: volgorde.map((i) => opties[i]),
    antwoord: volgorde.indexOf(vraag.antwoord),
    optieVolgorde: volgorde,
  };
}
