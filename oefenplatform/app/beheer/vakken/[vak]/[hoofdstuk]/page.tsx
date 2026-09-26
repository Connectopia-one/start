import Link from "next/link";
import { notFound } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import {
  bulkImportVragen,
  verwijderVraag,
  verwijderLeerstof,
  verwijderLeerbundelBlok,
  verplaatsLeerbundelBlok,
  bewaarLeestekst,
} from "./actions";
import { NieuwLeerstofForm } from "./NieuwLeerstofForm";
import { NieuwLeerbundelForm } from "./NieuwLeerbundelForm";
import { schrijfWoordenlijst, type Woord } from "@/lib/woordenlijst";
import { NieuwVraagForm } from "./NieuwVraagForm";

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
  },
  {
    "type": "invultekst",
    "vraag": "Hoe noem je dieren die alleen planten eten?",
    "antwoord": ["planteneters", "herbivoren"],
    "uitleg": "Allebei juist. Het eerste woord tonen we als het antwoord."
  },
  {
    "type": "meerkeuze",
    "vraag": "Welke van deze steden liggen in Italie?",
    "opties": ["Rome", "Madrid", "Milaan", "Lyon"],
    "antwoord": [0, 2],
    "uitleg": "Rome en Milaan. Er waren er dus twee juist."
  },
  {
    "type": "meerkeuze",
    "vraag": "Welke hoek zie je in de afbeelding?",
    "opties": ["Scherpe hoek", "Rechte hoek", "Stompe hoek"],
    "antwoord": 1,
    "afbeelding_url": "https://voorbeeld.com/rechte-hoek.png"
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
    .select("id, titel, volgnummer, leestekst, woordenlijst")
    .eq("vak_id", vak.id)
    .eq("volgnummer", volgnummer)
    .single();
  if (!hoofdstuk) notFound();

  const { data: vragenRuw } = await supabase
    .from("vragen")
    .select("id, volgnummer, type, vraag, opties, antwoord, uitleg, afbeelding_pad")
    .eq("hoofdstuk_id", hoofdstuk.id)
    .order("volgnummer", { ascending: true });

  const vragen = await Promise.all(
    (vragenRuw ?? []).map(async (v) => {
      if (!v.afbeelding_pad) return { ...v, afbeeldingUrl: null as string | null };
      if (v.afbeelding_pad.startsWith("http")) return { ...v, afbeeldingUrl: v.afbeelding_pad };
      const { data } = await supabase.storage.from("vraagafbeeldingen").createSignedUrl(v.afbeelding_pad, 3600);
      return { ...v, afbeeldingUrl: data?.signedUrl ?? null };
    })
  );

  const { data: bundelRuw } = await supabase
    .from("leerbundel")
    .select("id, volgnummer, soort, tekst, afbeelding_pad")
    .eq("hoofdstuk_id", hoofdstuk.id)
    .order("volgnummer", { ascending: true });

  const bundel = await Promise.all(
    (bundelRuw ?? []).map(async (b) => {
      if (!b.afbeelding_pad) return { ...b, afbeeldingUrl: null as string | null };
      const { data } = await supabase.storage.from("leerbundel").createSignedUrl(b.afbeelding_pad, 3600);
      return { ...b, afbeeldingUrl: data?.signedUrl ?? null };
    })
  );

  const { data: leerstof } = await supabase
    .from("leerstof")
    .select("id, titel, bestandspad, created_at")
    .eq("hoofdstuk_id", hoofdstuk.id)
    .order("created_at", { ascending: false });

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
          {vragen.map((v) => (
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
                  {v.afbeeldingUrl && (
                    <a
                      href={v.afbeeldingUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="mt-2 inline-block"
                    >
                      {/* eslint-disable-next-line @next/next/no-img-element */}
                      <img
                        src={v.afbeeldingUrl}
                        alt="Afbeelding bij de vraag"
                        className="max-h-32 rounded-md border border-border"
                      />
                    </a>
                  )}
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
          {!vragen.length && <li className="text-sm text-ink-dim">Nog geen vragen.</li>}
        </ul>

        <section className="mt-8 rounded-xl border border-border bg-surface p-5">
          <h2 className="font-display text-base font-semibold text-ink">Vraag toevoegen</h2>
          <NieuwVraagForm hoofdstukId={hoofdstuk.id} vakSlug={vakSlug} volgnummer={volgnummerStr} />
        </section>

        <section className="mt-8 rounded-xl border border-border bg-surface p-5">
          <h2 className="font-display text-base font-semibold text-ink">Bulk-import via JSON</h2>
          <p className="mt-2 text-sm text-ink-dim">
            Plak hier een JSON-lijst met vragen — handig als je ze al met DeepSeek/Gemini
            voorbereid hebt. Vraag je AI-tool om exact dit formaat te gebruiken. Het veld
            <code className="mx-1 rounded bg-paper px-1 py-0.5 text-xs">afbeelding_url</code>
            is optioneel — enkel een volledige externe link (geen upload mogelijk via bulk-import;
            gebruik daarvoor het formulier &quot;Vraag toevoegen&quot; hieronder).
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

        {/* Begrijpend lezen: de tekst hoort bij het hoofdstuk, niet bij één
            vraag, en blijft bij het oefenen boven de vragen staan. */}
        <section className="mt-8 rounded-xl border border-border bg-surface p-5">
          <h2 className="font-display text-base font-semibold text-ink">
            Leestekst (begrijpend lezen)
          </h2>
          <p className="mt-2 text-sm text-ink-dim">
            Staat hier een tekst, dan leest het kind die boven de vragen, en blijft
            ze staan zolang het oefent. Een lege regel begint een nieuwe alinea.
            Zet een moeilijk woord tussen sterretjes, zoals{" "}
            <code className="rounded bg-paper px-1 py-0.5 text-xs">*echolocatie*</code>:
            het krijgt dan een stippellijntje en toont de uitleg uit de woordenlijst.
            Laat het vak leeg om de tekst weer weg te halen.
          </p>
          <form action={bewaarLeestekst} className="mt-4 space-y-3">
            <input type="hidden" name="hoofdstuk_id" value={hoofdstuk.id} />
            <input type="hidden" name="vak_slug" value={vakSlug} />
            <input type="hidden" name="volgnummer" value={volgnummerStr} />
            <textarea
              name="leestekst"
              rows={10}
              defaultValue={hoofdstuk.leestekst ?? ""}
              placeholder="De tekst die het kind leest."
              className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
            <label className="block text-sm text-ink">
              Woordenlijst, één per regel als{" "}
              <span className="font-mono text-xs">woord = uitleg</span>
              <textarea
                name="woordenlijst"
                rows={5}
                defaultValue={schrijfWoordenlijst(hoofdstuk.woordenlijst as Woord[] | null)}
                placeholder="echolocatie = je weg vinden door te luisteren naar de echo van je eigen geluid"
                className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </label>
            <button
              type="submit"
              className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Leestekst bewaren
            </button>
          </form>
        </section>

        <section className="mt-8 rounded-xl border border-border bg-surface p-5">
          <h2 className="font-display text-base font-semibold text-ink">Leerbundel (met afbeeldingen)</h2>
          <p className="mt-2 text-sm text-ink-dim">
            Bouw hier de theorie op die het kind in het platform zelf leest, blokje per blokje:
            een tussentitel, een stuk tekst, een weetje of een afbeelding. Met de pijltjes zet je
            een blokje hoger of lager.
          </p>

          <ol className="mt-4 space-y-2">
            {bundel.map((b, i) => (
              <li key={b.id} className="rounded-lg border border-border px-3 py-2 text-sm">
                <div className="flex items-start justify-between gap-3">
                  <div className="min-w-0">
                    <p className="text-xs uppercase tracking-wide text-ink-dim">{b.soort}</p>
                    {b.afbeeldingUrl ? (
                      /* eslint-disable-next-line @next/next/no-img-element */
                      <img
                        src={b.afbeeldingUrl}
                        alt={b.tekst || "Afbeelding in de leerbundel"}
                        className="mt-1 max-h-28 rounded-md border border-border"
                      />
                    ) : null}
                    {b.tekst ? <p className="mt-1 whitespace-pre-line text-ink">{b.tekst}</p> : null}
                  </div>
                  <div className="flex shrink-0 items-center gap-2">
                    <form action={verplaatsLeerbundelBlok}>
                      <input type="hidden" name="id" value={b.id} />
                      <input type="hidden" name="richting" value="omhoog" />
                      <input type="hidden" name="vak_slug" value={vakSlug} />
                      <input type="hidden" name="volgnummer" value={volgnummerStr} />
                      <button type="submit" disabled={i === 0} className="text-xs text-ink-dim hover:text-ink disabled:opacity-30">
                        &uarr;
                      </button>
                    </form>
                    <form action={verplaatsLeerbundelBlok}>
                      <input type="hidden" name="id" value={b.id} />
                      <input type="hidden" name="richting" value="omlaag" />
                      <input type="hidden" name="vak_slug" value={vakSlug} />
                      <input type="hidden" name="volgnummer" value={volgnummerStr} />
                      <button
                        type="submit"
                        disabled={i === bundel.length - 1}
                        className="text-xs text-ink-dim hover:text-ink disabled:opacity-30"
                      >
                        &darr;
                      </button>
                    </form>
                    <form action={verwijderLeerbundelBlok}>
                      <input type="hidden" name="id" value={b.id} />
                      <input type="hidden" name="vak_slug" value={vakSlug} />
                      <input type="hidden" name="volgnummer" value={volgnummerStr} />
                      <button type="submit" className="text-xs text-danger hover:underline">
                        Verwijderen
                      </button>
                    </form>
                  </div>
                </div>
              </li>
            ))}
            {!bundel.length && <li className="text-sm text-ink-dim">Nog geen leerbundel voor dit hoofdstuk.</li>}
          </ol>

          <NieuwLeerbundelForm hoofdstukId={hoofdstuk.id} vakSlug={vakSlug} volgnummer={volgnummerStr} />
        </section>

        <section className="mt-8 rounded-xl border border-border bg-surface p-5">
          <h2 className="font-display text-base font-semibold text-ink">Bestanden om te downloaden</h2>
          <p className="mt-2 text-sm text-ink-dim">
            PDF&apos;s die kinderen naast de oefeningen kunnen lezen of afdrukken — dezelfde toegang
            als de oefenvragen van dit hoofdstuk.
          </p>

          <ul className="mt-4 space-y-2">
            {(leerstof ?? []).map((l) => (
              <li
                key={l.id}
                className="flex items-center justify-between rounded-lg border border-border px-3 py-2 text-sm"
              >
                <span className="text-ink">{l.titel}</span>
                <form action={verwijderLeerstof}>
                  <input type="hidden" name="id" value={l.id} />
                  <input type="hidden" name="bestandspad" value={l.bestandspad} />
                  <input type="hidden" name="vak_slug" value={vakSlug} />
                  <input type="hidden" name="volgnummer" value={volgnummerStr} />
                  <button type="submit" className="text-xs text-danger hover:underline">
                    Verwijderen
                  </button>
                </form>
              </li>
            ))}
            {!leerstof?.length && <li className="text-sm text-ink-dim">Nog geen leerstof geüpload.</li>}
          </ul>

          <NieuwLeerstofForm hoofdstukId={hoofdstuk.id} vakSlug={vakSlug} volgnummer={volgnummerStr} />
        </section>
      </main>
    </>
  );
}
