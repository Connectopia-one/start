import { getSessionProfile } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { isBegeleiding, magExtraBundel } from "@/lib/extraBundels";
import { haalPinHash, isOntgrendeld } from "@/lib/ouderpin";

/*
  Eén extra bundel openen (zie supabase/extra-bundels.sql). De opslagmap is
  niet publiek: hier kijken we eerst of je de bundel mag zien, en sturen we
  je dan door naar een link die één minuut werkt.

  Een verbetersleutel staat voor ouders achter de ouderpincode (Kim,
  10 november 2026): kinderen oefenen vaak op het account van de ouder.
  - geen pincode op het account: eerst er een instellen in Mijn account;
  - wel een pincode, maar niet net ingegeven: eerst de pincode, daarna komt
    de ouder vanzelf hier terug en gaat het bestand open.
  Beheerder en begeleiders hebben geen pincode nodig.
*/
export async function GET(
  request: Request,
  { params }: { params: Promise<{ niveau: string; vak: string; id: string }> },
) {
  const { niveau, vak, id } = await params;
  if (!/^[0-9a-f-]{36}$/i.test(id)) return new Response("Niet gevonden", { status: 404 });

  const hier = `/niveaus/${niveau}/${vak}/extra/${id}`;
  const naar = (pad: string) => Response.redirect(new URL(pad, request.url), 303);

  const session = await getSessionProfile();
  if (!session) return naar(`/login?volgende=${encodeURIComponent(hier)}`);
  const profile = session.profile ?? null;
  if (!magExtraBundel(profile)) {
    return new Response("Deze bundel is er voor wie volledige toegang heeft.", { status: 403 });
  }

  const admin = createAdminClient();
  const { data: bundel } = await admin
    .from("extra_bundels")
    .select("id, bestandspad, verbetersleutel")
    .eq("id", id)
    .single();
  if (!bundel) return new Response("Niet gevonden", { status: 404 });

  if (bundel.verbetersleutel && !isBegeleiding(profile)) {
    const hash = await haalPinHash(session.userId);
    if (!hash) {
      const uitleg =
        "Verbetersleutels openen met de ouderpincode, zodat je kind de oplossingen niet kan zien. Kies hieronder eerst een pincode en klik daarna opnieuw op de verbetersleutel.";
      return naar(`/account?fout=${encodeURIComponent(uitleg)}#pincode`);
    }
    if (!(await isOntgrendeld(session.userId, hash))) {
      return naar(`/account/pincode?terug=${encodeURIComponent(hier)}`);
    }
  }

  const { data } = await admin.storage
    .from("extrabundels")
    .createSignedUrl(bundel.bestandspad, 60);
  if (!data?.signedUrl) return new Response("Bestand niet gevonden", { status: 404 });

  return Response.redirect(data.signedUrl, 302);
}
