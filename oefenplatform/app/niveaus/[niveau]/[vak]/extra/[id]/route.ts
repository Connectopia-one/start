import { getSessionProfile } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { magExtraBundel } from "@/lib/extraBundels";

/*
  Eén extra bundel openen (zie supabase/extra-bundels.sql). De opslagmap is
  niet publiek: hier kijken we eerst of je de bundel mag zien, en sturen we
  je dan door naar een link die één minuut werkt. Zo kan een verbetersleutel
  niet doorgegeven worden met een gewone link.
*/
export async function GET(
  _request: Request,
  { params }: { params: Promise<{ niveau: string; vak: string; id: string }> },
) {
  const { id } = await params;
  if (!/^[0-9a-f-]{36}$/i.test(id)) return new Response("Niet gevonden", { status: 404 });

  const session = await getSessionProfile();
  if (!session) return new Response("Log eerst in.", { status: 401 });

  const admin = createAdminClient();
  const { data: bundel } = await admin
    .from("extra_bundels")
    .select("id, bestandspad, alleen_begeleiding")
    .eq("id", id)
    .single();
  if (!bundel) return new Response("Niet gevonden", { status: 404 });

  if (!magExtraBundel(bundel, session.profile ?? null)) {
    return new Response("Deze bundel is niet voor dit account.", { status: 403 });
  }

  const { data } = await admin.storage
    .from("extrabundels")
    .createSignedUrl(bundel.bestandspad, 60);
  if (!data?.signedUrl) return new Response("Bestand niet gevonden", { status: 404 });

  return Response.redirect(data.signedUrl, 302);
}
