import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { NIVEAUS, vindNiveau } from "@/lib/niveaus";
import { extraSoort, sorteerExtraBundels, type ExtraBundel } from "@/lib/extraBundels";
import { verwijderExtraBundel } from "./actions";
import { NieuweExtraBundelForm, type VakKeuze } from "./NieuweExtraBundelForm";

/*
  Extra bundels per vak, los van de hoofdstukken (Kim, 10 november 2026):
  examens op papier, lesbundels over het hele vak, ... Zie
  supabase/extra-bundels.sql.
*/
export default async function BeheerExtraBundelsPage() {
  const session = await requireBeheerder();
  const supabase = await createClient();

  const { data: vakken } = await supabase
    .from("vakken")
    .select("id, naam, slug, hoofdstukken(niveau)")
    .order("volgorde", { ascending: true });

  const keuzes: VakKeuze[] = ((vakken ?? []) as {
    id: string;
    naam: string;
    hoofdstukken: { niveau: string }[];
  }[])
    .map((v) => {
      const aanwezig = new Set(v.hoofdstukken.map((h) => h.niveau));
      return {
        id: v.id,
        naam: v.naam,
        niveaus: NIVEAUS.filter((n) => aanwezig.has(n.slug)).map((n) => ({
          slug: n.slug,
          naam: `${n.emoji} ${n.naam}`,
        })),
      };
    })
    .filter((v) => v.niveaus.length);

  const { data, error } = await supabase
    .from("extra_bundels")
    .select("*")
    .order("created_at", { ascending: true });
  const rijen = sorteerExtraBundels((data ?? []) as ExtraBundel[]);

  const vakVan = new Map(
    ((vakken ?? []) as { id: string; naam: string; slug: string }[]).map((v) => [v.id, v]),
  );

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">Extra bundels per vak</h1>
        <p className="mt-2 text-sm text-ink-dim">
          Bundels die bij een heel vak horen en niet bij één hoofdstuk: een examen op papier,
          een lesbundel over het hele vak, … Ze staan op de vakpagina onder &ldquo;Extra
          bundels&rdquo;, voor iedereen met volledige toegang. Vink &ldquo;alleen voor mij en
          de begeleiders&rdquo; aan voor een verbetersleutel.
        </p>

        {error && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            De lijst kon niet geladen worden: {error.message}. Heb je{" "}
            <code>supabase/extra-bundels.sql</code> al één keer uitgevoerd?
          </p>
        )}

        <section className="mt-8">
          <h2 className="font-display text-lg font-semibold text-ink">Nieuwe bundel</h2>
          <NieuweExtraBundelForm vakken={keuzes} />
        </section>

        <section className="mt-10">
          <h2 className="font-display text-lg font-semibold text-ink">Wat er nu staat</h2>
          {!rijen.length && <p className="mt-3 text-sm text-ink-dim">Nog niets.</p>}
          <ul className="mt-3 space-y-2">
            {rijen.map((b) => {
              const vak = vakVan.get(b.vak_id);
              const niveau = vindNiveau(b.niveau);
              const soort = extraSoort(b.soort);
              return (
                <li
                  key={b.id}
                  className="flex items-start justify-between gap-3 rounded-lg border border-border bg-surface p-3"
                >
                  <div className="min-w-0">
                    <p className="text-xs uppercase tracking-wide text-ink-dim">
                      {vak?.naam} · {niveau ? `${niveau.emoji} ${niveau.naam}` : b.niveau}
                      {b.alleen_begeleiding && " · alleen begeleiding"}
                    </p>
                    <a
                      href={`/niveaus/${b.niveau}/${vak?.slug}/extra/${b.id}`}
                      target="_blank"
                      rel="noopener"
                      className="font-medium text-ink hover:text-forest"
                    >
                      <span aria-hidden>{b.alleen_begeleiding ? "🔑" : soort.icoon}</span> {b.titel}
                    </a>
                    {b.omschrijving && <p className="text-sm text-ink-dim">{b.omschrijving}</p>}
                  </div>
                  <form action={verwijderExtraBundel}>
                    <input type="hidden" name="id" value={b.id} />
                    <button className="text-sm text-danger hover:underline">Weghalen</button>
                  </form>
                </li>
              );
            })}
          </ul>
        </section>
      </main>
    </>
  );
}
