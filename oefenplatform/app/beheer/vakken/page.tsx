import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import {
  maakVak,
  verwijderVak,
  maakHoofdstuk,
  wisselGratis,
  verwijderHoofdstuk,
  wisselRekenmachine,
  bulkImportVakInhoud,
} from "../actions";
import { NIVEAUS, vindNiveau } from "@/lib/niveaus";

type Hoofdstuk = { id: string; titel: string; volgnummer: number; gratis: boolean; niveau: string };
type Vak = { id: string; naam: string; slug: string; rekenmachine: boolean; hoofdstukken: Hoofdstuk[] };

const VOORBEELD_VAK_JSON = `{
  "hoofdstukken": [
    {
      "titel": "Probleemoplossend denken",
      "niveau": "spark",
      "gratis": false,
      "vragen": [
        {
          "type": "meerkeuze",
          "vraag": "Hoeveel is 7 x 8?",
          "opties": ["54", "56", "58"],
          "antwoord": 1,
          "uitleg": "7 x 8 = 56"
        },
        {
          "type": "waarofniet",
          "vraag": "Een vierkant heeft 4 gelijke zijden.",
          "antwoord": true
        }
      ]
    },
    {
      "titel": "Getallenleer",
      "niveau": "spark",
      "vragen": [
        {
          "type": "invultekst",
          "vraag": "3/4 als procent is ___.",
          "antwoord": "75%"
        }
      ]
    }
  ]
}`;

export default async function BeheerVakkenPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout } = await searchParams;
  const supabase = await createClient();

  const { data: vakken } = await supabase
    .from("vakken")
    .select("id, naam, slug, rekenmachine, hoofdstukken(id, titel, volgnummer, gratis, niveau)")
    .order("volgorde", { ascending: true });

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">Vakken &amp; hoofdstukken</h1>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}

        <div className="mt-6 space-y-8">
          {(vakken as Vak[] | null)?.map((vak) => (
            <section key={vak.id} className="rounded-xl border border-border bg-surface p-5">
              <div className="flex items-center justify-between">
                <h2 className="font-display text-lg font-semibold text-ink">{vak.naam}</h2>
                <div className="flex items-center gap-3">
                  <form action={wisselRekenmachine}>
                    <input type="hidden" name="id" value={vak.id} />
                    <input type="hidden" name="rekenmachine" value={String(vak.rekenmachine)} />
                    <button
                      type="submit"
                      className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${
                        vak.rekenmachine ? "bg-forest/10 text-forest-dark" : "bg-ink-dim/10 text-ink-dim"
                      }`}
                    >
                      {vak.rekenmachine ? "Rekenmachine aan" : "Rekenmachine uit"}
                    </button>
                  </form>
                  <form action={verwijderVak}>
                    <input type="hidden" name="id" value={vak.id} />
                    <button type="submit" className="text-xs text-danger hover:underline">
                      Vak verwijderen
                    </button>
                  </form>
                </div>
              </div>

              <ul className="mt-4 space-y-2">
                {vak.hoofdstukken
                  .sort((a, b) => a.volgnummer - b.volgnummer)
                  .map((h) => (
                    <li
                      key={h.id}
                      className="flex items-center justify-between rounded-lg border border-border px-3 py-2 text-sm"
                    >
                      <Link
                        href={`/beheer/vakken/${vak.slug}/${h.volgnummer}`}
                        className="text-forest-dark hover:underline"
                      >
                        {h.volgnummer}. {h.titel}
                      </Link>
                      <div className="flex items-center gap-3">
                        <span className="text-xs text-ink-dim">
                          {vindNiveau(h.niveau)?.emoji} {vindNiveau(h.niveau)?.naam}
                        </span>
                        <form action={wisselGratis}>
                          <input type="hidden" name="id" value={h.id} />
                          <input type="hidden" name="gratis" value={String(h.gratis)} />
                          <button
                            type="submit"
                            className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${
                              h.gratis ? "bg-forest/10 text-forest-dark" : "bg-ink-dim/10 text-ink-dim"
                            }`}
                          >
                            {h.gratis ? "Gratis" : "Op slot"}
                          </button>
                        </form>
                        <form action={verwijderHoofdstuk}>
                          <input type="hidden" name="id" value={h.id} />
                          <button type="submit" className="text-xs text-danger hover:underline">
                            Verwijderen
                          </button>
                        </form>
                      </div>
                    </li>
                  ))}
              </ul>

              <form action={maakHoofdstuk} className="mt-4 flex flex-wrap items-center gap-2">
                <input type="hidden" name="vak_id" value={vak.id} />
                <input
                  name="titel"
                  required
                  placeholder="Titel nieuw hoofdstuk"
                  className="min-w-0 flex-1 rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                />
                <select
                  name="niveau"
                  defaultValue="start"
                  className="rounded-md border border-border bg-paper px-2 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                >
                  {NIVEAUS.map((n) => (
                    <option key={n.slug} value={n.slug}>
                      {n.emoji} {n.naam}
                    </option>
                  ))}
                </select>
                <label className="flex items-center gap-1.5 text-xs text-ink-dim">
                  <input type="checkbox" name="gratis" className="accent-forest" />
                  Gratis
                </label>
                <button
                  type="submit"
                  className="shrink-0 rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
                >
                  Toevoegen
                </button>
              </form>

              <details className="mt-4 rounded-lg border border-border">
                <summary className="cursor-pointer px-3 py-2 text-sm font-medium text-ink">
                  Bulk-import: meerdere hoofdstukken tegelijk (JSON)
                </summary>
                <div className="border-t border-border p-3">
                  <p className="text-sm text-ink-dim">
                    Plak hier vragen voor meerdere hoofdstukken in één keer — handig na het
                    voorbereiden met DeepSeek/Gemini op basis van een vakfiche. Een hoofdstuk met
                    een titel die hierboven al bestaat krijgt de vragen erbij; een nieuwe titel
                    wordt automatisch als hoofdstuk aangemaakt. Vraag je AI-tool om exact dit
                    formaat te gebruiken:
                  </p>
                  <pre className="mt-3 overflow-x-auto rounded-md bg-paper p-3 text-xs text-ink-dim">
                    {VOORBEELD_VAK_JSON}
                  </pre>
                  <form action={bulkImportVakInhoud} className="mt-3 space-y-3">
                    <input type="hidden" name="vak_id" value={vak.id} />
                    <textarea
                      name="json"
                      required
                      rows={8}
                      placeholder={VOORBEELD_VAK_JSON}
                      className="w-full rounded-md border border-border bg-paper px-3 py-2 font-mono text-xs outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                    />
                    <button
                      type="submit"
                      className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
                    >
                      Importeren
                    </button>
                  </form>
                </div>
              </details>
            </section>
          ))}
        </div>

        <form action={maakVak} className="mt-8 flex flex-wrap items-center gap-2">
          <input
            name="naam"
            required
            placeholder="Naam nieuw vak (bv. Wiskunde)"
            className="min-w-0 flex-1 rounded-md border border-border bg-surface px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
          <label className="flex items-center gap-1.5 text-xs text-ink-dim">
            <input type="checkbox" name="rekenmachine" className="accent-forest" />
            Rekenmachine (GeoGebra)
          </label>
          <button
            type="submit"
            className="shrink-0 rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
          >
            Vak toevoegen
          </button>
        </form>
      </main>
    </>
  );
}
