import { PDFDocument } from "pdf-lib";
import { getSessionProfile } from "@/lib/auth";
import { heeftVolledigeToegang } from "@/lib/toegang";
import { createClient } from "@/lib/supabase/server";
import { vindNiveau } from "@/lib/niveaus";
import { sorteerHoofdstukken } from "@/lib/hoofdstukvolgorde";

/*
  De hele cursus van één vak in één categorie, als één pdf.

  Lotte, enquête november 2026: "zou ik van elk vak ook een volledige cursus
  van het vak erop zetten". Kim: "de volledige cursussen zijn eigenlijk de
  lesbundels gebundeld, die staan er al." Dus plakken we hier de leerbundels
  van alle hoofdstukken aan elkaar, in de volgorde van de hoofdstukken.

  - Enkel leerbundels, geen oefenbundels.
  - Deel 1 en deel 2 van een thema delen dezelfde bundel: die komt er één keer in.
  - Enkel voor wie volledige toegang heeft, net als de losse bundels.
*/
export const maxDuration = 60;

const isOefenbundel = (titel: string) =>
  titel.trim().toLowerCase().startsWith("oefenbundel");

function themaVan(titel: string) {
  return (/^(.+?) — deel [12]$/.exec(titel.trim())?.[1] ?? titel).trim();
}

export async function GET(
  _request: Request,
  { params }: { params: Promise<{ niveau: string; vak: string }> },
) {
  const { niveau: niveauSlug, vak: vakSlug } = await params;
  const niveau = vindNiveau(niveauSlug);
  if (!niveau) return new Response("Niet gevonden", { status: 404 });

  const session = await getSessionProfile();
  if (!session || !heeftVolledigeToegang(session.profile ?? null)) {
    return new Response("Enkel met volledige toegang.", { status: 403 });
  }

  const supabase = await createClient();
  const { data: vak } = await supabase
    .from("vakken")
    .select("id, naam, slug, hoofdstukken(id, titel, volgnummer, gratis, niveau)")
    .eq("slug", vakSlug)
    .single();
  if (!vak) return new Response("Niet gevonden", { status: 404 });

  const hoofdstukken = sorteerHoofdstukken(
    (
      vak.hoofdstukken as {
        id: string;
        titel: string;
        volgnummer: number;
        gratis: boolean;
        niveau: string;
      }[]
    ).filter((h) => h.niveau === niveau.slug),
  );
  if (!hoofdstukken.length) return new Response("Niet gevonden", { status: 404 });

  const { data: rijen } = await supabase
    .from("leerstof")
    .select("hoofdstuk_id, titel, bestandspad, created_at")
    .in(
      "hoofdstuk_id",
      hoofdstukken.map((h) => h.id),
    )
    .order("created_at", { ascending: true });

  // Per hoofdstuk, in de volgorde van de hoofdstukken, en elk thema één keer.
  const gehad = new Set<string>();
  const paden: string[] = [];
  for (const h of hoofdstukken) {
    const thema = themaVan(h.titel);
    for (const r of rijen ?? []) {
      if (r.hoofdstuk_id !== h.id || isOefenbundel(r.titel)) continue;
      const sleutel = `${thema}|${r.titel.trim().toLowerCase()}`;
      if (gehad.has(sleutel)) continue;
      gehad.add(sleutel);
      paden.push(r.bestandspad);
    }
  }
  if (!paden.length) {
    return new Response("Voor dit vak staan er nog geen leerbundels klaar.", {
      status: 404,
    });
  }

  const cursus = await PDFDocument.create();
  cursus.setTitle(`${vak.naam} – ${niveau.naam} – Connectopia`);
  for (const pad of paden) {
    const { data: blob } = await supabase.storage.from("leerstof").download(pad);
    if (!blob) continue;
    try {
      const bron = await PDFDocument.load(await blob.arrayBuffer());
      const paginas = await cursus.copyPages(bron, bron.getPageIndices());
      for (const p of paginas) cursus.addPage(p);
    } catch {
      // Eén kapotte pdf mag de hele cursus niet tegenhouden.
    }
  }
  if (!cursus.getPageCount()) {
    return new Response("De leerbundels konden niet geladen worden.", {
      status: 500,
    });
  }

  const bytes = await cursus.save();
  const naam = `cursus-${vak.slug}-${niveau.slug}.pdf`;
  return new Response(Buffer.from(bytes), {
    headers: {
      "Content-Type": "application/pdf",
      "Content-Disposition": `attachment; filename="${naam}"`,
      "Cache-Control": "private, no-store",
    },
  });
}
