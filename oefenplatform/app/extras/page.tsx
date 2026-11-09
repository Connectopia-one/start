import Link from "next/link";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { extrasTekst, soorten, spelKaarten } from "@/inhoud/extras";
import { haalMateriaal } from "@/lib/extrasMateriaal";

export const metadata = {
  title: "Leuke extra's — Oefenplatform Connectopia",
  description:
    "Educatieve spellen, leuke links, afdrukbare documenten en filmpjes naast de leerstof, per schoolniveau. Gratis en zonder account.",
};

/*
  Vier grote knoppen, elk naar een eigen pagina (Kim, 9 november 2026). Wat er
  achter elke knop staat, zie je op /extras/spellen, /extras/links,
  /extras/documenten en /extras/filmpjes. Zichtbaar zonder account: er staat
  niets van een kind op.

  De teksten staan in inhoud/extras.ts.
*/
export default async function ExtrasPage() {
  const session = await getSessionProfile();
  const materiaal = await haalMateriaal();

  function aantal(soort: string) {
    if (soort === "spellen") return spelKaarten.length;
    return materiaal.filter((m) => m.soort === soort).length;
  }

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          {extrasTekst.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">
          {extrasTekst.titel}
        </h1>
        <p className="mt-4 max-w-2xl text-sm text-ink-dim">
          {extrasTekst.intro}
        </p>

        <div className="mt-8 grid gap-4 sm:grid-cols-2">
          {soorten.map((s) => {
            const n = aantal(s.slug);
            return (
              <Link
                key={s.slug}
                href={`/extras/${s.slug}`}
                className="flex flex-col rounded-2xl border-2 border-border bg-surface px-6 py-6 transition hover:border-forest hover:shadow-md"
              >
                <span aria-hidden className="text-4xl">
                  {s.icoon}
                </span>
                <span className="mt-3 font-display text-xl font-semibold text-ink">
                  {s.titel}
                </span>
                <span className="mt-2 block text-sm text-ink-dim">
                  {s.tekst}
                </span>
                <span className="mt-4 text-sm font-semibold text-forest-dark">
                  {n > 0 ? `Bekijk ze (${n})` : "Binnenkort"} &rarr;
                </span>
              </Link>
            );
          })}
        </div>

        {extrasTekst.tipsLink && (
          <p className="mt-10 text-sm text-ink-dim">
            {extrasTekst.tipsVraag}{" "}
            <Link
              href={extrasTekst.tipsLink}
              className="font-medium text-forest underline underline-offset-2 hover:text-forest-dark"
            >
              {extrasTekst.tipsLinkTekst}
            </Link>
            .
          </p>
        )}
      </main>
    </>
  );
}
