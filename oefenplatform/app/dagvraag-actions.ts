"use server";

import { createClient } from "@/lib/supabase/server";
import { getSessionProfile } from "@/lib/auth";
import { heeftVolledigeToegang } from "@/lib/toegang";
import { schikOpties, zaad } from "@/lib/optievolgorde";
import { vandaagSleutel } from "@/lib/dagvraag";
import { NIVEAUS } from "@/lib/niveaus";

export type Dagvraag = {
  id: string;
  type: "meerkeuze" | "waarofniet";
  vraag: string;
  opties: string[] | null;
  antwoord: number | string | boolean | number[] | string[];
  uitleg: string | null;
  afbeeldingUrl: string | null;
  /** Waar de vraag vandaan komt, zodat een moeilijke vraag nooit uit de lucht valt. */
  vak: string;
  vakSlug: string;
  hoofdstuk: string;
  hoofdstukNummer: number;
  niveau: string;
};

export type DagvraagAntwoord = {
  vraag: Dagvraag | null;
  /** De categorieën waarin deze bezoeker vandaag vragen mag zien. */
  niveaus: string[];
  /** Kijkt hier iemand mee die alleen de gratis hoofdstukken mag zien? */
  achterSlot: boolean;
};

/*
  Waarom alleen meerkeuze en waar/niet-waar: bij een invulvraag hangt "juist"
  af van een hele reeks afwegingen (accenten, enkelvoud en meervoud, getallen
  die anders geschreven staan) die in de Quiz zorgvuldig zijn uitgewerkt. Die
  hier overdoen zou betekenen dat dezelfde vraag op twee plekken anders
  beoordeeld kan worden, en dat is erger dan een iets kleinere voorraad.
*/
const SOORTEN = ["meerkeuze", "waarofniet"];

const VELDEN =
  "id, type, vraag, opties, antwoord, uitleg, afbeelding_pad, " +
  "hoofdstukken!inner(titel, volgnummer, niveau, gratis, vakken!inner(naam, slug))";

type RuweVraag = {
  id: string;
  type: string;
  vraag: string;
  opties: string[] | null;
  antwoord: number | string | boolean | number[] | string[];
  uitleg: string | null;
  afbeelding_pad: string | null;
  hoofdstukken: {
    titel: string;
    volgnummer: number;
    niveau: string;
    vakken: { naam: string; slug: string };
  };
};

/**
 * De vraag van vandaag uit de gevraagde categorie.
 *
 * De keuze ligt vast per dag en per categorie: hetzelfde kind ziet dezelfde
 * vraag als het de pagina herlaadt, en twee kinderen die samen oefenen zien
 * hetzelfde. Er wordt niets opgeslagen in de voortgang — dit is een extraatje,
 * geen les, en één losse vraag hoort geen vinkje op een heel hoofdstuk te
 * zetten. Zie ook het weekdoel in components/Dagvraag.tsx.
 */
export async function haalDagvraag(niveauSlug: string | null): Promise<DagvraagAntwoord> {
  const session = await getSessionProfile();
  const volledig = heeftVolledigeToegang(session?.profile ?? null);
  const supabase = await createClient();

  const niveaus = await beschikbareNiveaus(volledig);
  // Vraagt iemand een categorie die hij niet mag zien (of die leeg is), dan
  // vallen we terug op alles wat hij wél mag zien. Beter een andere vraag dan
  // een leeg kader.
  const niveau = niveauSlug && niveaus.includes(niveauSlug) ? niveauSlug : null;

  // Eerst tellen hoeveel vragen in aanmerking komen, dan er precies één
  // ophalen met de dag als plaatsnummer. Zo hoeft er nooit een lijst van
  // duizenden vragen over de lijn, en toch is de keuze voor iedereen dezelfde.
  let tellen = supabase
    .from("vragen")
    .select(VELDEN, { count: "exact", head: true })
    .in("type", SOORTEN);
  if (!volledig) tellen = tellen.eq("hoofdstukken.gratis", true);
  if (niveau) tellen = tellen.eq("hoofdstukken.niveau", niveau);
  const { count } = await tellen;
  if (!count) return { vraag: null, niveaus, achterSlot: !volledig };

  const plek = zaad(`${vandaagSleutel()}|${niveau ?? "alles"}`) % count;
  let halen = supabase.from("vragen").select(VELDEN).in("type", SOORTEN).order("id");
  if (!volledig) halen = halen.eq("hoofdstukken.gratis", true);
  if (niveau) halen = halen.eq("hoofdstukken.niveau", niveau);
  const { data } = await halen.range(plek, plek);

  const rij = ((data ?? [])[0] as unknown as RuweVraag) ?? null;
  if (!rij) return { vraag: null, niveaus, achterSlot: !volledig };

  // De opties krijgen hier hun volgorde, net als in een gewoon hoofdstuk, zodat
  // het juiste antwoord niet altijd op dezelfde plaats staat.
  const geschikt = schikOpties({
    id: rij.id,
    type: rij.type,
    opties: rij.opties,
    antwoord: rij.antwoord,
  });

  return {
    vraag: {
      id: rij.id,
      type: rij.type as "meerkeuze" | "waarofniet",
      vraag: rij.vraag,
      opties: geschikt.opties,
      antwoord: geschikt.antwoord,
      uitleg: rij.uitleg,
      afbeeldingUrl: await afbeelding(rij.afbeelding_pad),
      vak: rij.hoofdstukken.vakken.naam,
      vakSlug: rij.hoofdstukken.vakken.slug,
      hoofdstuk: rij.hoofdstukken.titel,
      hoofdstukNummer: rij.hoofdstukken.volgnummer,
      niveau: rij.hoofdstukken.niveau,
    },
    niveaus,
    achterSlot: !volledig,
  };
}

/** Een afbeelding bij de vraag: ofwel een volledige URL, ofwel iets uit de bucket. */
async function afbeelding(pad: string | null): Promise<string | null> {
  if (!pad) return null;
  if (pad.startsWith("http")) return pad;
  const supabase = await createClient();
  const { data } = await supabase.storage.from("vraagafbeeldingen").createSignedUrl(pad, 3600);
  return data?.signedUrl ?? null;
}

/** In welke categorieën deze bezoeker iets te zien krijgt, in de vaste volgorde. */
async function beschikbareNiveaus(volledig: boolean): Promise<string[]> {
  const supabase = await createClient();
  let zoek = supabase.from("hoofdstukken").select("niveau");
  if (!volledig) zoek = zoek.eq("gratis", true);
  const { data } = await zoek;

  const gevonden = new Set((data ?? []).map((h) => h.niveau as string));
  return NIVEAUS.filter((n) => gevonden.has(n.slug)).map((n) => n.slug);
}
