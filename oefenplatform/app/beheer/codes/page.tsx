import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import { maakCode, wisselActief, verwijderCode, zetGroepToegangUit } from "./actions";

export default async function BeheerCodesPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; melding?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout, melding } = await searchParams;
  const supabase = await createClient();

  const { data: codes } = await supabase
    .from("plusklas_codes")
    .select("code, label, actief, created_at")
    .order("created_at", { ascending: false });

  /* Hoeveel accounts met deze code nu nog gratis toegang hebben. Met de
     service-sleutel, zodat ook accounts zonder kind meetellen. */
  const { data: metToegang } = await createAdminClient()
    .from("profiles")
    .select("plusklas_code")
    .eq("is_plusklas", true)
    .not("plusklas_code", "is", null);

  const aantalPerCode = new Map<string, number>();
  for (const rij of metToegang ?? []) {
    const code = rij.plusklas_code as string;
    aantalPerCode.set(code, (aantalPerCode.get(code) ?? 0) + 1);
  }

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">Plusklas-codes</h1>
        <p className="mt-2 text-sm text-ink-dim">
          Deel een actieve code met plusklas-gezinnen. Wie zich registreert met deze code krijgt
          automatisch gratis volledige toegang. Een code inactief zetten houdt enkel nieuwe mensen
          tegen: wie ze al gebruikte, houdt zijn toegang tot je ze hieronder uitzet.
        </p>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}
        {melding && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">{melding}</p>
        )}

        <ul className="mt-6 space-y-2">
          {(codes ?? []).map((c) => {
            const aantal = aantalPerCode.get(c.code) ?? 0;
            return (
            <li
              key={c.code}
              className="rounded-lg border border-border bg-surface p-3 text-sm"
            >
              <div className="flex items-center justify-between gap-3">
              <div>
                <p className="font-mono font-medium text-ink">{c.code}</p>
                {c.label && <p className="text-xs text-ink-dim">{c.label}</p>}
              </div>
              <div className="flex items-center gap-3">
                <form action={wisselActief}>
                  <input type="hidden" name="code" value={c.code} />
                  <input type="hidden" name="actief" value={String(c.actief)} />
                  <button
                    type="submit"
                    className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${
                      c.actief ? "bg-forest/10 text-forest-dark" : "bg-ink-dim/10 text-ink-dim"
                    }`}
                  >
                    {c.actief ? "Actief" : "Inactief"}
                  </button>
                </form>
                <form action={verwijderCode}>
                  <input type="hidden" name="code" value={c.code} />
                  <button type="submit" className="text-xs text-danger hover:underline">
                    Verwijderen
                  </button>
                </form>
              </div>
              </div>

              {/* Einde van een testperiode: alle gezinnen van deze code in één
                  keer terug op de gratis hoofdstukken. */}
              <div className="mt-2 flex flex-wrap items-center justify-between gap-2 border-t border-border pt-2">
                <span className="text-xs text-ink-dim">
                  {aantal === 0
                    ? "Niemand met deze code heeft nu gratis toegang."
                    : `${aantal} ${aantal === 1 ? "account heeft" : "accounts hebben"} gratis toegang via deze code.`}
                </span>
                {aantal > 0 && (
                  <form action={zetGroepToegangUit}>
                    <input type="hidden" name="code" value={c.code} />
                    <button
                      type="submit"
                      className="rounded-full border border-border px-3 py-1 text-xs font-medium text-ink hover:border-danger hover:text-danger"
                    >
                      Toegang van deze {aantal} uitzetten
                    </button>
                  </form>
                )}
              </div>
            </li>
            );
          })}
          {!codes?.length && <li className="text-sm text-ink-dim">Nog geen codes aangemaakt.</li>}
        </ul>

        <form action={maakCode} className="mt-6 space-y-3 rounded-xl border border-border bg-surface p-5">
          <div className="space-y-1.5">
            <label className="text-sm font-medium text-ink">Code</label>
            <input
              name="code"
              required
              placeholder="bv. PLUSKLAS2026"
              className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm font-mono outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
          </div>
          <div className="space-y-1.5">
            <label className="text-sm font-medium text-ink">
              Label <span className="font-normal text-ink-dim">(optioneel, enkel voor jezelf)</span>
            </label>
            <input
              name="label"
              placeholder="bv. Plusklas Hasselt 2026-2027"
              className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
          </div>
          <button
            type="submit"
            className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
          >
            Code toevoegen
          </button>
        </form>
      </main>
    </>
  );
}
