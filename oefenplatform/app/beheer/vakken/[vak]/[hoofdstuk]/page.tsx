import Link from "next/link";
import { notFound } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { maakVraag, bulkImportVragen, verwijderVraag } from "./actions";

const VOORBEELD_JSON = `[
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
  },
  {
    "type": "invultekst",
    "vraag": "De hoofdstad van Frankrijk is ___.",
    "antwoord": "Parijs"
  }
]`;

export default async function BeheerVragenPage({
  params,
  searchParams,
}: {
  params: Promise<{ vak: string; hoofdstuk: string }>;
  searchParams: Promise<{ fout?: string }>;
}) {
  const session = await requireBeheerder();
  const { vak: vakSlug, hoofdstuk: volgnummerStr } = await params;
  const { fout } = await searchParams;
  const volgnummer = Number(volgnummerStr);

  const supabase = await createClient();
  const { data: vak } = await supabase.from("vakken").select("id, naam, slug").eq("slug", vakSlug).single();
  if (!vak) notFound();

  const { data: hoofdstuk } = await supabase
    .from("hoofdstukken")
    .select("id, titel, volgnummer")
    .eq("vak_id", vak.id)
    .eq("volgnummer", volgnummer)
    .single();
  if (!hoofdstuk) notFound();

  const { data: vragen } = await supabase
    .from("vragen")
    .select("id, volgnummer, type, vraag, opties, antwoord, uitleg")
    .eq("hoofdstuk_id", hoofdstuk.id)
    .order("volgnummer", { ascending: true });

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <Link href="/beheer/vakken" className="text-sm text-ink-dim hover:text-ink">
          &larr; Vakken
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          {vak.naam} — {hoofdstuk.titel}
        </h1>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}

        <ul className="mt-6 space-y-2">
          {(vragen ?? []).map((v) => (
            <li key={v.id} className="rounded-lg border border-border bg-surface p-3 text-sm">
              <div className="flex items-start justify-between gap-3">
                <div>
                  <p className="font-medium text-ink">
                    {v.volgnummer}. {v.vraag}
                  </p>
                  <p className="mt-1 text-xs text-ink-dim">
                    {v.type}
                    {v.opties ? ` · opties: ${(v.opties as string[]).join(", ")}` : ""} · antwoord:{" "}
                    {JSON.stringify(v.antwoord)}
                  </p>
                </div>
                <form action={verwijderVraag}>
                  <input type="hidden" name="id" value={v.id} />
                  <input type="hidden" name="vak_slug" value={vakSlug} />
                  <input type="hidden" name="volgnummer" value={volgnummerStr} />
                  <button type="submit" className="shrink-0 text-xs text-danger hover:underline">
                    Verwijderen
                  </button>
                </form>
              </div>
            </li>
          ))}
          {!vragen?.length && <li className="text-sm text-ink-dim">Nog geen vragen.</li>}
        </ul>

        <section className="mt-8 rounded-xl border border-border bg-surface p-5">
          <h2 className="font-display text-base font-semibold text-ink">Vraag toevoegen</h2>
          <form action={maakVraag} className="mt-4 space-y-3">
            <input type="hidden" name="hoofdstuk_id" value={hoofdstuk.id} />
            <input type="hidden" name="vak_slug" value={vakSlug} />
            <input type="hidden" name="volgnummer" value={volgnummerStr} />

            <div className="space-y-1.5">
              <label className="text-sm font-medium text-ink">Type</label>
              <select
                name="type"
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              >
                <option value="meerkeuze">Meerkeuze</option>
                <option value="waarofniet">Waar of niet waar</option>
                <option value="invultekst">Invultekst</option>
              </select>
            </div>

            <div className="space-y-1.5">
              <label className="text-sm font-medium text-ink">Vraag</label>
              <textarea
                name="vraag"
                required
                rows={2}
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>

            <div className="space-y-1.5">
              <label className="text-sm font-medium text-ink">
                Opties <span className="font-normal text-ink-dim">(enkel bij meerkeuze, één per regel)</span>
              </label>
              <textarea
                name="opties"
                rows={3}
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>

            <div className="space-y-1.5">
              <label className="text-sm font-medium text-ink">Antwoord</label>
              <input
                name="antwoord"
                required
                placeholder='Meerkeuze: index (0, 1, 2...) · Waar/niet: "waar" of "niet waar" · Invultekst: het juiste woord'
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>

            <div className="space-y-1.5">
              <label className="text-sm font-medium text-ink">
                Uitleg <span className="font-normal text-ink-dim">(optioneel)</span>
              </label>
              <textarea
                name="uitleg"
                rows={2}
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>

            <button
              type="submit"
              className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Vraag toevoegen
            </button>
          </form>
        </section>

        <section className="mt-8 rounded-xl border border-border bg-surface p-5">
          <h2 className="font-display text-base font-semibold text-ink">Bulk-import via JSON</h2>
          <p className="mt-2 text-sm text-ink-dim">
            Plak hier een JSON-lijst met vragen — handig als je ze al met DeepSeek/Gemini
            voorbereid hebt. Vraag je AI-tool om exact dit formaat te gebruiken:
          </p>
          <pre className="mt-3 overflow-x-auto rounded-md bg-paper p-3 text-xs text-ink-dim">
            {VOORBEELD_JSON}
          </pre>
          <form action={bulkImportVragen} className="mt-4 space-y-3">
            <input type="hidden" name="hoofdstuk_id" value={hoofdstuk.id} />
            <input type="hidden" name="vak_slug" value={vakSlug} />
            <input type="hidden" name="volgnummer" value={volgnummerStr} />
            <textarea
              name="json"
              required
              rows={8}
              placeholder={VOORBEELD_JSON}
              className="w-full rounded-md border border-border bg-paper px-3 py-2 font-mono text-xs outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
            <button
              type="submit"
              className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Importeren
            </button>
          </form>
        </section>
      </main>
    </>
  );
}
