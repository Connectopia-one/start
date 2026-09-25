import { NextResponse } from "next/server";
import { getSessionProfile } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { maakTestPdf, type PdfPoging, type PdfVraag } from "@/lib/testpdf";

/*
  Levert één opgeloste test als pdf, zodat een begeleider die kan downloaden
  en bewaren zoals een leerbundel.

  Het tekenen van de pdf gebeurt in lib/testpdf.ts. Hier halen we enkel de
  gegevens op, na dezelfde twee controles als overal bij de fiches: ben je
  beheerder of begeleider, en hoort dit kind bij een plusklasgezin.
*/

function veiligeBestandsnaam(tekst: string) {
  return (
    tekst
      .normalize("NFD")
      .replace(/[̀-ͯ]/g, "")
      .replace(/[^a-zA-Z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "")
      .toLowerCase() || "test"
  );
}

export async function GET(
  _verzoek: Request,
  { params }: { params: Promise<{ kindId: string; hoofdstukId: string }> },
) {
  const session = await getSessionProfile();
  const rol = session?.profile?.role;
  if (rol !== "beheerder" && rol !== "begeleider") {
    return new NextResponse("Geen toegang.", { status: 403 });
  }

  const { kindId, hoofdstukId } = await params;
  const supabase = await createClient();

  const { data: kind } = await supabase
    .from("kinderen")
    .select("id, naam, profiles(full_name, is_plusklas)")
    .eq("id", kindId)
    .single();

  const gezin = (
    kind as { profiles?: { full_name: string; is_plusklas: boolean } } | null
  )?.profiles;
  if (!kind || !gezin?.is_plusklas) {
    return new NextResponse("Niet gevonden.", { status: 404 });
  }

  const { data: hoofdstuk } = await supabase
    .from("hoofdstukken")
    .select("id, titel, leestekst, woordenlijst, vakken(naam)")
    .eq("id", hoofdstukId)
    .single<{
      id: string;
      titel: string;
      leestekst: string | null;
      woordenlijst: { woord: string; uitleg: string }[] | null;
      vakken: { naam: string };
    }>();
  if (!hoofdstuk) return new NextResponse("Niet gevonden.", { status: 404 });

  const { data: vragen } = await supabase
    .from("vragen")
    .select("id, type, vraag, opties, antwoord, uitleg")
    .eq("hoofdstuk_id", hoofdstukId)
    .order("volgnummer", { ascending: true });

  const ids = (vragen ?? []).map((v) => v.id);
  const { data: pogingen } = ids.length
    ? await supabase
        .from("voortgang")
        .select("vraag_id, correct, gegeven_antwoord, beantwoord_op")
        .eq("kind_id", kindId)
        .in("vraag_id", ids)
        .order("beantwoord_op", { ascending: false })
    : { data: [] };

  const bytes = await maakTestPdf({
    kindNaam: kind.naam,
    gezinNaam: gezin.full_name,
    vak: hoofdstuk.vakken.naam,
    hoofdstuk: hoofdstuk.titel,
    vragen: (vragen ?? []) as unknown as PdfVraag[],
    pogingen: (pogingen ?? []) as unknown as PdfPoging[],
    leestekst: hoofdstuk.leestekst,
    woordenlijst: hoofdstuk.woordenlijst,
  });

  const naam = `${veiligeBestandsnaam(kind.naam)}-${veiligeBestandsnaam(hoofdstuk.titel)}.pdf`;

  return new NextResponse(bytes as unknown as BodyInit, {
    headers: {
      "Content-Type": "application/pdf",
      "Content-Disposition": `attachment; filename="${naam}"`,
      "Cache-Control": "no-store",
    },
  });
}
