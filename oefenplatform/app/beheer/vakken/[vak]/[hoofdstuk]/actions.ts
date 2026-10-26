"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { volgendVolgnummer, vrijeVolgnummers } from "@/lib/volgnummer";
import { leesWoordenlijst } from "@/lib/woordenlijst";
import { maakKeuzelijst, maakTabelAntwoord, zetVormKlaar, type VraagType } from "@/lib/vraagvorm";
import { pakCasussenUit, vanFormulier } from "@/lib/examenvormen";

type NieuweVraag = {
  type: VraagType;
  vraag: string;
  opties?: string[] | null;
  antwoord: unknown;
  /** Een casus: de situatie boven de vraag. Zie lib/examenvormen.ts. */
  casus?: string | null;
  /** Enkel bij een tabel in een importbestand; zie lib/vraagvorm.ts. */
  rijen?: string[];
  kolommen?: string[];
  uitleg?: string | null;
  /** Optioneel: een volledige externe URL naar een afbeelding (bv. na bulk-import). */
  afbeelding_url?: string | null;
};

function terugPad(vakSlug: string, volgnummer: string) {
  return `/beheer/vakken/${vakSlug}/${volgnummer}`;
}

function leesOpties(type: NieuweVraag["type"], optiesRaw: string): string[] | null {
  // Bij een tabel staan hier de uitspraken, één per rij.
  if (type !== "meerkeuze" && type !== "tabel") return null;
  return optiesRaw.split("\n").map((r) => r.trim()).filter(Boolean);
}

/**
 * Leest het antwoordveld zoals een mens het intikt.
 *
 * Bij meerkeuze mag je meer dan één nummer invullen, gescheiden door een
 * komma: "0, 2" betekent dat het eerste én het derde antwoord juist zijn en
 * dat een kind ze allebei moet aanduiden. Bij een invulvraag mag je meer dan
 * één juist antwoord geven, gescheiden door een verticale streep:
 * "planteneters | herbivoren". Het eerste is wat het kind te zien krijgt, de
 * rest telt evengoed juist. Zie lib/antwoord.ts.
 *
 * Staat hier apart omdat zowel maakVraag als bewerkVraag ze nodig heeft: twee
 * kopieën zouden na de eerste aanpassing uit elkaar lopen.
 */
function leesAntwoord(
  type: NieuweVraag["type"],
  antwoordRaw: string
): number | string | boolean | number[] | string[] {
  if (type === "meerkeuze") {
    const nummers = antwoordRaw
      .split(",")
      .map((deel) => Number(deel.trim()))
      .filter((n) => Number.isInteger(n));
    if (!nummers.length) throw new Error("Vul bij meerkeuze een nummer in, of meerdere met een komma ertussen.");
    return nummers.length === 1 ? nummers[0] : nummers.sort((a, b) => a - b);
  }
  if (type === "waarofniet") {
    return antwoordRaw.toLowerCase() === "waar" || antwoordRaw.toLowerCase() === "true";
  }
  if (antwoordRaw.includes("|")) {
    const woorden = antwoordRaw.split("|").map((w) => w.trim()).filter(Boolean);
    return woorden.length > 1 ? woorden : woorden[0] || antwoordRaw;
  }
  return antwoordRaw;
}

/**
 * Vraag, opties en antwoord samen, zoals ze uit het formulier komen. Een tabel
 * en een keuzelijst hebben de drie velden samen nodig: het antwoord van een
 * tabel hoort bij haar rijen, en het antwoord van een keuzelijst staat met een
 * sterretje in de zin zelf. Zie lib/vraagvorm.ts.
 *
 * Een tabel: bij Opties de uitspraken, één per regel. Bij Antwoord per rij de
 * juiste kolom, met een komma ertussen: "juist, fout, juist". Andere kolommen
 * dan juist en fout zet je ervoor, met een dubbelpunt erachter:
 * "Ja | Nee | Soms: ja, soms, nee".
 */
function leesVelden(type: NieuweVraag["type"], vraagRaw: string, optiesRaw: string, antwoordRaw: string) {
  // Volgorde, koppelen, sorteren, slepen, klikken, open en tekenen: zie
  // vanFormulier in lib/examenvormen.ts voor wat er in welk veld staat.
  const nieuw = vanFormulier(type, vraagRaw, optiesRaw, antwoordRaw);
  if (nieuw) {
    return {
      vraag: String(nieuw.vraag),
      opties: (nieuw.opties ?? null) as string[] | null,
      antwoord: nieuw.antwoord,
    };
  }
  if (type === "keuzelijst") {
    const { vraag, antwoord } = maakKeuzelijst(vraagRaw, antwoordRaw ? antwoordRaw.split(",").map((a) => a.trim()) : []);
    return { vraag, opties: null, antwoord };
  }
  if (!antwoordRaw) throw new Error("Vul minstens de vraag en het antwoord in.");
  if (type === "tabel") {
    const rijen = leesOpties(type, optiesRaw) ?? [];
    const dubbelpunt = antwoordRaw.indexOf(":");
    const kolommen = dubbelpunt >= 0 ? antwoordRaw.slice(0, dubbelpunt).split("|").map((k) => k.trim()) : null;
    const perRij = (dubbelpunt >= 0 ? antwoordRaw.slice(dubbelpunt + 1) : antwoordRaw).split(",").map((a) => a.trim());
    return { vraag: vraagRaw, opties: rijen, antwoord: maakTabelAntwoord(rijen, kolommen, perRij) };
  }
  return { vraag: vraagRaw, opties: leesOpties(type, optiesRaw), antwoord: leesAntwoord(type, antwoordRaw) };
}

/** Wat het formulier terugkrijgt: niets als het gelukt is, anders de reden. */
type Uitkomst = { fout: string } | undefined;

/**
 * Wordt rechtstreeks aangeroepen vanuit NieuwVraagForm (een client component),
 * niet als een `<form action>` — gooit daarom een gewone Error in plaats van
 * te redirecten, zodat het formulier zelf de foutmelding kan tonen (dezelfde
 * aanpak als registreerLeerstof hieronder).
 */
export async function maakVraag(formData: FormData): Promise<Uitkomst> {
  /* Een fout die hier gegooid wordt, verbergt Next in productie achter
     "Minified React error #441". Daarom gaat de reden als antwoord terug. */
  try {
    await maakVraagOf(formData);
  } catch (e) {
    return { fout: e instanceof Error ? e.message : "Er ging iets mis." };
  }
}

async function maakVraagOf(formData: FormData) {
  await requireBeheerder();
  const hoofdstukId = String(formData.get("hoofdstuk_id") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");
  const type = String(formData.get("type") || "meerkeuze") as NieuweVraag["type"];
  const vraagRaw = String(formData.get("vraag") || "").trim();
  const optiesRaw = String(formData.get("opties") || "").trim();
  const antwoordRaw = String(formData.get("antwoord") || "").trim();
  const uitleg = String(formData.get("uitleg") || "").trim() || null;
  const casus = String(formData.get("casus") || "").trim() || null;
  const afbeeldingPad = String(formData.get("afbeelding_pad") || "").trim() || null;

  if (!vraagRaw) throw new Error("Vul minstens de vraag en het antwoord in.");

  const { vraag, opties, antwoord } = leesVelden(type, vraagRaw, optiesRaw, antwoordRaw);

  const admin = createAdminClient();

  const { error } = await admin.from("vragen").insert({
    hoofdstuk_id: hoofdstukId,
    volgnummer: await volgendVolgnummer(admin, "vragen", "hoofdstuk_id", hoofdstukId),
    type,
    vraag,
    opties,
    antwoord,
    uitleg,
    afbeelding_pad: afbeeldingPad,
    // Zo gaat een vraag zonder casus ook in als supabase/examenvormen.sql nog
    // niet gedraaid is.
    ...(casus ? { casus } : {}),
  });

  if (error) throw new Error("Vraag toevoegen is niet gelukt: " + error.message);

  revalidatePath(terugPad(vakSlug, volgnummer));
}

/**
 * Past een vraag aan die er al staat.
 *
 * Waarom dit bestaat: als er een melding binnenkomt dat een vraag onduidelijk
 * is, was het vroeger verwijderen en opnieuw intikken, of het hele
 * vragenbestand opnieuw importeren. Verwijderen kost het volgnummer en het
 * werk dat de kinderen op die vraag gemaakt hebben; een import van honderd
 * vragen om één zin te herschrijven is niet in verhouding.
 *
 * De afbeelding blijft staan zoals ze is: die verandert via toevoegen of
 * verwijderen, niet hier.
 *
 * Wordt net als maakVraag rechtstreeks aangeroepen vanuit een client
 * component, dus met een gewone Error in plaats van een redirect.
 */
export async function bewerkVraag(formData: FormData): Promise<Uitkomst> {
  try {
    await bewerkVraagOf(formData);
  } catch (e) {
    return { fout: e instanceof Error ? e.message : "Er ging iets mis." };
  }
}

async function bewerkVraagOf(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");
  const type = String(formData.get("type") || "meerkeuze") as NieuweVraag["type"];
  const vraagRaw = String(formData.get("vraag") || "").trim();
  const optiesRaw = String(formData.get("opties") || "").trim();
  const antwoordRaw = String(formData.get("antwoord") || "").trim();
  const uitleg = String(formData.get("uitleg") || "").trim() || null;
  const casus = String(formData.get("casus") || "").trim() || null;
  // Het veld staat er pas als de kolom bestaat, zie de pagina.
  const metCasus = formData.has("casus");

  if (!id) throw new Error("Welke vraag het is, is onderweg verloren gegaan. Herlaad de pagina.");
  if (!vraagRaw) throw new Error("Vul minstens de vraag en het antwoord in.");

  const { vraag, opties, antwoord } = leesVelden(type, vraagRaw, optiesRaw, antwoordRaw);

  const admin = createAdminClient();
  const { error } = await admin
    .from("vragen")
    .update({ type, vraag, opties, antwoord, uitleg, ...(metCasus ? { casus } : {}) })
    .eq("id", id);

  if (error) throw new Error("Aanpassen is niet gelukt: " + error.message);

  revalidatePath(terugPad(vakSlug, volgnummer));
}

/**
 * Haalt de vragen uit wat er geplakt is.
 *
 * Dit veld verwacht een kale lijst van vragen, want je zit al in één hoofdstuk.
 * Maar de bestanden in `inhoud/start` zijn gemaakt voor het andere invoerveld,
 * dat op de vakkenpagina staat: daar zit de lijst in `{"hoofdstukken": [...]}`.
 * Die twee door elkaar halen is zo gebeurd, dus we nemen zo'n bestand hier ook
 * gewoon aan. Staat er meer dan één hoofdstuk in, dan is het echt voor het
 * andere veld bedoeld en zeggen we dat.
 */
function haalVragenEruit(gelezen: unknown): NieuweVraag[] {
  if (Array.isArray(gelezen)) return gelezen as NieuweVraag[];

  const hoofdstukken = (gelezen as { hoofdstukken?: unknown })?.hoofdstukken;
  if (Array.isArray(hoofdstukken)) {
    if (hoofdstukken.length === 1) {
      const vragen = (hoofdstukken[0] as { vragen?: unknown })?.vragen;
      if (Array.isArray(vragen)) return vragen as NieuweVraag[];
    }
    throw new Error(
      "dit bestand bevat meerdere hoofdstukken. Gebruik het invoerveld op de vakkenpagina," +
        " onder \"Bulk-import: meerdere hoofdstukken tegelijk\"."
    );
  }

  throw new Error("Verwacht een JSON-array van vragen.");
}

export async function bulkImportVragen(formData: FormData) {
  await requireBeheerder();
  const hoofdstukId = String(formData.get("hoofdstuk_id") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");
  const json = String(formData.get("json") || "").trim();

  let vragen: NieuweVraag[];
  try {
    const gelezen = JSON.parse(json);
    vragen = haalVragenEruit(gelezen);
  } catch (e) {
    redirect(
      terugPad(vakSlug, volgnummer) +
        "?fout=" +
        encodeURIComponent("Ongeldige JSON: " + (e instanceof Error ? e.message : "onbekende fout"))
    );
  }

  // Een tabel of een keuzelijst die niet klopt, houdt het hele bestand tegen,
  // vóór er iets bewaard is. Zo staat er nooit een half hoofdstuk.
  try {
    vragen = (pakCasussenUit(vragen!) as NieuweVraag[]).map((v, i) => zetVormKlaar(v, `Vraag ${i + 1}`));
  } catch (e) {
    redirect(
      terugPad(vakSlug, volgnummer) +
        "?fout=" +
        encodeURIComponent("Bulk-import mislukt: " + (e instanceof Error ? e.message : "onbekende fout"))
    );
  }

  const admin = createAdminClient();
  const neemVolgnummer = await vrijeVolgnummers(admin, "vragen", "hoofdstuk_id", hoofdstukId);

  const rijen = vragen!.map((v) => ({
    hoofdstuk_id: hoofdstukId,
    volgnummer: neemVolgnummer(),
    type: v.type,
    vraag: v.vraag,
    opties: v.opties ?? null,
    antwoord: v.antwoord,
    uitleg: v.uitleg ?? null,
    afbeelding_pad: v.afbeelding_url ?? null,
    ...(v.casus ? { casus: v.casus } : {}),
  }));

  const { error } = await admin.from("vragen").insert(rijen);
  if (error) {
    redirect(terugPad(vakSlug, volgnummer) + "?fout=" + encodeURIComponent("Bulk-import mislukt: " + error.message));
  }

  revalidatePath(terugPad(vakSlug, volgnummer));
  redirect(terugPad(vakSlug, volgnummer));
}

export async function verwijderVraag(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");

  const admin = createAdminClient();
  const { data: vraag } = await admin.from("vragen").select("afbeelding_pad").eq("id", id).maybeSingle();
  // Enkel opruimen in onze eigen bucket — een externe URL (bulk-import) is niet
  // iets dat wij bewaren en dus niet iets dat wij kunnen/mogen verwijderen.
  if (vraag?.afbeelding_pad && !vraag.afbeelding_pad.startsWith("http")) {
    await admin.storage.from("vraagafbeeldingen").remove([vraag.afbeelding_pad]);
  }
  await admin.from("vragen").delete().eq("id", id);

  revalidatePath(terugPad(vakSlug, volgnummer));
  redirect(terugPad(vakSlug, volgnummer));
}

/**
 * Geeft een tijdelijke, rechtstreekse upload-link naar Supabase Storage terug
 * voor een afbeelding bij een vraag (zelfde patroon als leerstof-uploads).
 */
export async function maakVraagAfbeeldingUploadUrl(hoofdstukId: string, bestandsnaam: string) {
  await requireBeheerder();
  const admin = createAdminClient();
  const path = `${hoofdstukId}/${Date.now()}-${bestandsnaam}`;

  const { data, error } = await admin.storage.from("vraagafbeeldingen").createSignedUploadUrl(path);
  if (error || !data) {
    throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  }
  return { path: data.path, token: data.token };
}

/**
 * Geeft een tijdelijke, rechtstreekse upload-link naar Supabase Storage terug.
 * Het bestand zelf gaat zo NIET door de server action heen — dat omzeilt de
 * limiet van ~4,5MB die Vercel op reguliere server-verzoeken zet.
 */
export async function maakLeerstofUploadUrl(hoofdstukId: string, bestandsnaam: string) {
  await requireBeheerder();
  const admin = createAdminClient();
  const path = `${hoofdstukId}/${Date.now()}-${bestandsnaam}`;

  const { data, error } = await admin.storage.from("leerstof").createSignedUploadUrl(path);
  if (error || !data) {
    throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  }
  return { path: data.path, token: data.token };
}

export async function registreerLeerstof(input: {
  hoofdstukId: string;
  vakSlug: string;
  volgnummer: string;
  titel: string;
  bestandspad: string;
}) {
  await requireBeheerder();
  const admin = createAdminClient();

  const { error } = await admin.from("leerstof").insert({
    hoofdstuk_id: input.hoofdstukId,
    titel: input.titel,
    bestandspad: input.bestandspad,
  });

  if (error) throw new Error(error.message);
  revalidatePath(terugPad(input.vakSlug, input.volgnummer));
}

export async function verwijderLeerstof(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const bestandspad = String(formData.get("bestandspad") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");

  const admin = createAdminClient();
  if (bestandspad) await admin.storage.from("leerstof").remove([bestandspad]);
  await admin.from("leerstof").delete().eq("id", id);

  revalidatePath(terugPad(vakSlug, volgnummer));
  redirect(terugPad(vakSlug, volgnummer));
}

/* ------------------------------------------------------------------ leerbundel
   Een leerbundel is de theorie in het platform zelf, opgebouwd uit blokjes:
   een tussentitel, een stuk tekst, een weetje in een kadertje, of een
   afbeelding met een onderschrift. Zo kan je uitleg afwisselen met beeld.
   De blokjes staan in de volgorde van hun volgnummer; met verplaatsLeerbundelBlok
   wissel je een blokje van plaats met zijn buur. */

export type LeerbundelSoort = "titel" | "tekst" | "weetje" | "afbeelding";

/** Zie maakLeerstofUploadUrl: het bestand gaat rechtstreeks naar Supabase. */
export async function maakLeerbundelUploadUrl(hoofdstukId: string, bestandsnaam: string) {
  await requireBeheerder();
  const admin = createAdminClient();
  const path = `${hoofdstukId}/${Date.now()}-${bestandsnaam}`;

  const { data, error } = await admin.storage.from("leerbundel").createSignedUploadUrl(path);
  if (error || !data) {
    throw new Error(error?.message || "Kon geen upload-link aanmaken.");
  }
  return { path: data.path, token: data.token };
}

export async function voegLeerbundelBlokToe(input: {
  hoofdstukId: string;
  vakSlug: string;
  volgnummer: string;
  soort: LeerbundelSoort;
  tekst: string | null;
  afbeeldingPad: string | null;
}) {
  await requireBeheerder();

  const tekst = input.tekst?.trim() || null;
  if (input.soort === "afbeelding") {
    if (!input.afbeeldingPad) throw new Error("Kies eerst een afbeelding.");
  } else if (!tekst) {
    throw new Error("Vul de tekst in.");
  }

  const admin = createAdminClient();
  const { data: laatste } = await admin
    .from("leerbundel")
    .select("volgnummer")
    .eq("hoofdstuk_id", input.hoofdstukId)
    .order("volgnummer", { ascending: false })
    .limit(1);

  const { error } = await admin.from("leerbundel").insert({
    hoofdstuk_id: input.hoofdstukId,
    volgnummer: (laatste?.[0]?.volgnummer ?? 0) + 1,
    soort: input.soort,
    tekst,
    afbeelding_pad: input.afbeeldingPad,
  });
  if (error) throw new Error("Toevoegen is niet gelukt: " + error.message);

  revalidatePath(terugPad(input.vakSlug, input.volgnummer));
}

export async function verwijderLeerbundelBlok(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");

  const admin = createAdminClient();
  const { data: blok } = await admin
    .from("leerbundel")
    .select("afbeelding_pad")
    .eq("id", id)
    .maybeSingle();
  if (blok?.afbeelding_pad) {
    await admin.storage.from("leerbundel").remove([blok.afbeelding_pad]);
  }
  await admin.from("leerbundel").delete().eq("id", id);

  revalidatePath(terugPad(vakSlug, volgnummer));
  redirect(terugPad(vakSlug, volgnummer));
}

/** Wisselt het blokje van plaats met het blokje erboven of eronder. */
export async function verplaatsLeerbundelBlok(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("id") || "");
  const richting = String(formData.get("richting") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");
  const terug = terugPad(vakSlug, volgnummer);

  const admin = createAdminClient();
  const { data: blok } = await admin
    .from("leerbundel")
    .select("id, hoofdstuk_id, volgnummer")
    .eq("id", id)
    .maybeSingle();
  if (!blok) redirect(terug);

  const omhoog = richting === "omhoog";
  const { data: buur } = await admin
    .from("leerbundel")
    .select("id, volgnummer")
    .eq("hoofdstuk_id", blok!.hoofdstuk_id)
    [omhoog ? "lt" : "gt"]("volgnummer", blok!.volgnummer)
    .order("volgnummer", { ascending: !omhoog })
    .limit(1);

  const ander = buur?.[0];
  if (ander) {
    // Even naar een vrij nummer parkeren, anders botsen de twee nummers.
    await admin.from("leerbundel").update({ volgnummer: -1 }).eq("id", blok!.id);
    await admin.from("leerbundel").update({ volgnummer: blok!.volgnummer }).eq("id", ander.id);
    await admin.from("leerbundel").update({ volgnummer: ander.volgnummer }).eq("id", blok!.id);
  }

  revalidatePath(terug);
  redirect(terug);
}

/* ------------------------------------------------------------------ leestekst
   Begrijpend lezen: een tekst die boven de vragen blijft staan, met een
   verklarende woordenlijst. De woordenlijst wordt hier ingetypt als één woord
   per regel, "woord = uitleg", want dat leest een mens vlotter dan JSON. */

export async function bewaarLeestekst(formData: FormData) {
  await requireBeheerder();
  const id = String(formData.get("hoofdstuk_id") || "");
  const vakSlug = String(formData.get("vak_slug") || "");
  const volgnummer = String(formData.get("volgnummer") || "");
  const tekst = String(formData.get("leestekst") || "").trim();
  const lijst = leesWoordenlijst(String(formData.get("woordenlijst") || ""));

  const admin = createAdminClient();
  const { error } = await admin
    .from("hoofdstukken")
    .update({
      leestekst: tekst || null,
      woordenlijst: lijst.length ? lijst : null,
    })
    .eq("id", id);
  if (error) {
    redirect(
      `${terugPad(vakSlug, volgnummer)}?fout=` +
        encodeURIComponent(`De leestekst bewaren lukte niet: ${error.message}`)
    );
  }
  revalidatePath(terugPad(vakSlug, volgnummer));
  redirect(terugPad(vakSlug, volgnummer));
}
