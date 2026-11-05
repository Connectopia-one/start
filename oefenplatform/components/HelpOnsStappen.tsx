import Link from "next/link";
import { createClient } from "@/lib/supabase/server";

/*
  De twee stappen van "Help ons beter worden": de enquête en een review.

  Staat bovenaan /enquete en /reviews, zodat een gezin altijd ziet wat al
  binnen is en wat nog moet. Kim keurt daarna zelf goed (Beheer → Enquêtes en
  reviews); pas dan verschijnt hier dat de beloning klaarstaat.

  Zolang supabase/enquete-en-reviews.sql niet gedraaid is, bestaan de tabellen
  nog niet. Dan tekent dit blokje niets, in plaats van de pagina te breken.
*/
export async function HelpOnsStappen({ userId }: { userId: string }) {
  const supabase = await createClient();
  const [enquete, review, beloning] = await Promise.all([
    supabase.from("enquetes").select("id").eq("profile_id", userId).maybeSingle(),
    supabase.from("reviews").select("id, goedgekeurd").eq("profile_id", userId).maybeSingle(),
    supabase.from("beloningen").select("soort").eq("profile_id", userId).maybeSingle(),
  ]);
  if (enquete.error || review.error) return null;

  const enqueteKlaar = Boolean(enquete.data);
  const reviewKlaar = Boolean(review.data);

  return (
    <div className="mt-6 max-w-2xl rounded-xl border border-border bg-surface px-5 py-4 text-sm">
      <p className="font-semibold text-ink">Help ons het platform beter maken</p>
      <ul className="mt-2 space-y-1 text-ink">
        <li>
          {enqueteKlaar ? "✅" : "⬜"}{" "}
          <Link href="/enquete" className="underline underline-offset-2">
            De enquête
          </Link>{" "}
          <span className="text-ink-dim">(alleen wij lezen je antwoorden)</span>
        </li>
        <li>
          {reviewKlaar ? "✅" : "⬜"}{" "}
          <Link href="/reviews#schrijf" className="underline underline-offset-2">
            Een eerlijke review
          </Link>{" "}
          <span className="text-ink-dim">(komt op het reviewbord als wij hem ophangen)</span>
        </li>
      </ul>
      {beloning.data ? (
        <p className="mt-3 rounded-md bg-forest/10 px-3 py-2 text-forest-dark">
          {beloning.data.soort === "vaste_prijs"
            ? "Dank je wel! We hebben alles gelezen. Jouw prijs blijft 20 euro per schooljaar, ook als de prijs later stijgt."
            : "Dank je wel! We hebben alles gelezen. Je hebt gratis toegang tot en met 31 augustus 2027."}
        </p>
      ) : enqueteKlaar && reviewKlaar ? (
        <p className="mt-3 text-ink-dim">
          Allebei binnen, dank je wel! Kim leest alles zelf na. Zodra dat gebeurd is, zie je hier
          wat je als bedankje krijgt.
        </p>
      ) : null}
    </div>
  );
}
