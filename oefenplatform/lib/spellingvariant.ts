import { schikOpties } from "@/lib/optievolgorde";

/**
 * Wisselende woorden bij een spellingvraag.
 *
 * Een testgezin vroeg op 29 september 2026 of een kind dat een hoofdstuk
 * opnieuw maakt andere woorden kan krijgen. Kim bakende dat een dag later af:
 * enkel bij spelling, met een stuk of vijf woorden in roulatie. Haar
 * redenering, letterlijk: "Voor alle normale vragen en oefeningen moet dit
 * helemaal niet. Want de leerstof is de leerstof. Maar bij spelling kan ik me
 * wel inbeelden dat meer wisselende woorden beter is."
 *
 * Dat klopt ook inhoudelijk. Bij spelling zit de leerstof in de régel, niet in
 * het woord: vijf woorden die onder dezelfde regel vallen, toetsen precies
 * hetzelfde. Bij een inhoudsvraag verandert een ander woord de vraag wél, en
 * daar komt dus geen variant.
 *
 * De woorden staan in de kolom `vragen.varianten` (zie
 * supabase/spellingvarianten.sql) en worden met de hand geschreven en
 * nagelezen, nooit door een taalmodel bedacht: de welkomstbrief aan de
 * testgezinnen belooft uitdrukkelijk geen AI in de oefeningen.
 *
 * Welke beurt een kind krijgt, volgt uit hoe vaak dat kind deze vraag al
 * beantwoordde. De eerste keer is dat de vraag zoals ze in de databank staat,
 * daarna gaat ze de lijst af en begint ze opnieuw. Dat is een roulatie en geen
 * loting: een kind dat de bladzijde herlaadt, ziet hetzelfde woord staan.
 */

/** Eén beurt: enkel de velden die anders zijn dan bij de vraag zelf. */
export type Variant = {
  vraag?: string | null;
  opties?: string[] | null;
  antwoord?: number | string | boolean | number[] | string[] | null;
  uitleg?: string | null;
};

/** De velden die een beurt kan overschrijven, na het schudden van de opties. */
export type GetoondeVariant = {
  vraag: string;
  opties: string[] | null;
  antwoord: number | string | boolean | number[] | string[];
  uitleg: string | null;
  optieVolgorde: number[] | null;
};

type Basisvraag = {
  id: string;
  type: string;
  vraag: string;
  opties: string[] | null;
  antwoord: number | string | boolean | number[] | string[];
  uitleg: string | null;
};

/** Leest de kolom uit de databank uit; alles wat er raar uitziet, valt weg. */
export function leesVarianten(ruw: unknown): Variant[] {
  if (!Array.isArray(ruw)) return [];
  return ruw.filter(
    (v): v is Variant =>
      typeof v === "object" && v !== null && !Array.isArray(v),
  );
}

/**
 * Zet de varianten van één vraag om naar wat de browser kan tonen: per beurt de
 * volledige vraag, met de opties al geschud.
 *
 * Het schudden gebeurt hier en niet in de browser, zodat het op dezelfde manier
 * gaat als bij een gewone vraag (zie lib/optievolgorde.ts) en het antwoord van
 * een kind opgeslagen blijft worden met het nummer uit de databank.
 */
export function bouwVarianten(
  vraag: Basisvraag,
  ruw: unknown,
): GetoondeVariant[] {
  return leesVarianten(ruw).map((variant, i) => {
    const samen = {
      id: vraag.id,
      type: vraag.type,
      vraag: variant.vraag ?? vraag.vraag,
      opties: variant.opties ?? vraag.opties,
      antwoord: variant.antwoord ?? vraag.antwoord,
      uitleg: variant.uitleg ?? vraag.uitleg,
    };
    // Beurt 1 is de vraag zelf, dus deze lijst begint bij beurt 2.
    const geschikt = schikOpties(samen, `${vraag.id}#${i + 1}`);
    return {
      vraag: geschikt.vraag,
      opties: geschikt.opties,
      antwoord: geschikt.antwoord,
      uitleg: geschikt.uitleg,
      optieVolgorde: geschikt.optieVolgorde,
    };
  });
}

/**
 * De vraag zoals ze bij één bewaarde beurt hoorde, met de opties in de volgorde
 * van de databank.
 *
 * Voor de schermen waar een ouder of Kim meekijkt. Daar staat het antwoord van
 * het kind opgeslagen met het optienummer uit de databank, dus daar mag niets
 * geschud worden: anders staat de vraag over 'man' er met het antwoord
 * 'kinderen' onder.
 */
export function variantVoorBeurt<T extends Basisvraag>(
  vraag: T,
  ruw: unknown,
  beurt: number | null | undefined,
): T {
  if (!beurt || beurt < 1) return vraag;
  const v = leesVarianten(ruw)[beurt - 1];
  if (!v) return vraag;
  return {
    ...vraag,
    vraag: v.vraag ?? vraag.vraag,
    opties: v.opties ?? vraag.opties,
    antwoord: v.antwoord ?? vraag.antwoord,
    uitleg: v.uitleg ?? vraag.uitleg,
  };
}

/**
 * Het nummer van de beurt die een kind nu krijgt: 0 is de vraag zelf, 1 de
 * eerste variant, enzovoort. `beurten` is hoe vaak dit kind deze vraag al
 * beantwoordde.
 */
export function beurtnummer(beurten: number, aantalVarianten: number): number {
  if (aantalVarianten < 1) return 0;
  const rond = aantalVarianten + 1;
  const n = Math.max(0, Math.floor(beurten));
  return n % rond;
}
