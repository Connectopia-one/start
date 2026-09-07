import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";

export default async function BeheerPage() {
  const session = await requireBeheerder();
  const supabase = await createClient();

  const [{ count: vakkenCount }, { count: betaaldCount }, { count: plusklasCount }] = await Promise.all([
    supabase.from("vakken").select("id", { count: "exact", head: true }),
    supabase.from("betalingen").select("id", { count: "exact", head: true }).eq("status", "betaald"),
    supabase.from("profiles").select("id", { count: "exact", head: true }).eq("is_plusklas", true),
  ]);

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">Beheer</h1>
        <p className="mt-1 text-sm text-ink-dim">
          {vakkenCount ?? 0} vak{(vakkenCount ?? 0) === 1 ? "" : "ken"} &middot; {betaaldCount ?? 0}{" "}
          betaalde toegang{(betaaldCount ?? 0) === 1 ? "" : "en"} &middot; {plusklasCount ?? 0} plusklas-account
          {(plusklasCount ?? 0) === 1 ? "" : "s"}
        </p>

        <div className="mt-8 grid gap-8 sm:grid-cols-2">
          <section>
            <h2 className="font-display text-lg font-semibold text-ink">Vakken &amp; hoofdstukken</h2>
            <p className="mt-3 text-sm text-ink-dim">
              Vakken en hoofdstukken aanmaken, en instellen welk hoofdstuk gratis is.
            </p>
            <Link
              href="/beheer/vakken"
              className="mt-4 inline-block rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Vakken beheren &rarr;
            </Link>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">Plusklas-codes</h2>
            <p className="mt-3 text-sm text-ink-dim">
              Codes die je deelt met plusklas-gezinnen voor gratis volledige toegang bij
              registratie.
            </p>
            <Link
              href="/beheer/codes"
              className="mt-4 inline-block rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Codes beheren &rarr;
            </Link>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">Voortgang</h2>
            <p className="mt-3 text-sm text-ink-dim">
              Score en aantal beantwoorde vragen per kind, over alle vakken heen.
            </p>
            <Link
              href="/beheer/voortgang"
              className="mt-4 inline-block rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Voortgang bekijken &rarr;
            </Link>
          </section>
        </div>
      </main>
    </>
  );
}
