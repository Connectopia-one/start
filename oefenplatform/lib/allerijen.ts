/**
 * Alle rijen van één vraag aan de databank, ook al zijn het er meer dan de
 * databank in één keer teruggeeft.
 *
 * Supabase geeft op een gewone select hoogstens een vast aantal rijen terug
 * (standaard duizend). Dat is een beveiliging tegen een vraag die per ongeluk
 * een hele tabel ophaalt, en ze komt zonder enige foutmelding: je krijgt het
 * eerste blok rijen, en de rest bestaat voor die pagina niet meer.
 *
 * Daar liep het op 14 oktober 2026 op mis bij de vinkjes van het
 * oefenplatform. In "voortgang" staat één rij per beantwoorde vraag, en wie
 * een hoofdstuk nog eens maakt, zet er twintig rijen bij. Een kind dat de
 * eerste zestien hoofdstukken van Nederlands een paar keer deed, zat zo over
 * die duizend rijen, en bij de hoofdstukken daarna bleef het vinkje weg.
 * Precies wat een ouder meldde: "bij de oefenreeksen vanaf de reeks
 * Woordsoorten deel 1 wordt er niet meer afgecheckt dat je ze gemaakt hebt".
 *
 * Deze functie vraagt de rijen daarom blok per blok op, met `range`, tot er
 * een leeg blok terugkomt. Ze stopt nooit bij een half blok: staat de grens
 * van de databank lager dan de blokgrootte hier, dan is élk blok half en zou
 * ze na het eerste al stoppen. Een leeg blok is dus het enige einde, en een
 * teller houdt het geheel binnen de perken.
 *
 * `bouw` krijgt de grenzen van het blok en geeft de query terug. Zet daar zelf
 * een vaste `order` op, anders kan dezelfde rij in twee blokken opduiken.
 */
export async function alleRijen<T>(
  bouw: (
    van: number,
    tot: number,
  ) => PromiseLike<{ data: T[] | null; error: unknown }>,
  blokgrootte = 1000,
): Promise<T[]> {
  const alles: T[] = [];
  // Honderd blokken van duizend: meer dan een kind ooit zal oefenen, en het
  // houdt een verkeerd gesorteerde vraag ervan om eindeloos door te gaan.
  for (let blok = 0; blok < 100; blok++) {
    const { data, error } = await bouw(
      alles.length,
      alles.length + blokgrootte - 1,
    );
    if (error || !data || data.length === 0) break;
    alles.push(...data);
  }
  return alles;
}
