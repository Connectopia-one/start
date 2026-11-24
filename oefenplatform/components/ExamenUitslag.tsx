import Link from "next/link";
import type { SupabaseClient } from "@supabase/supabase-js";
import { VraagTekst } from "@/components/Figuren";
import { Formule } from "@/components/Formule";
import { formatAntwoord } from "@/lib/antwoordWeergave";
import { type VraagType } from "@/lib/vraagvorm";
import { NIVEAUS } from "@/lib/niveaus";

/*
  De uitslag van de examens over een heel vak, voor de ouder (Voortgang van
  een kind) en voor de begeleiding. Kim, 24 november 2026: "wat ik nu wel
  jammer vind is dat we niet kunnen zien hoeveel ze halen op het examen en
  wat ze fout doen en hun dus niet goed kunnen begeleiden."

  Sinds die dag bewaart een examen per vraag of ze juist was en wat het kind
  antwoordde (kolom antwoorden, zie supabase/examen-antwoorden.sql). Van de
  examens van daarvoor is enkel de score bewaard.
*/

export type ExamenRij = {
  id: string;
  niveau: string;
  aantal: number;
  juist: number;
  afgelegd_op: string;
  antwoorden?: PerVraag[] | null;
  vakken: { naam: string } | null;
};

type PerVraag = {
  v: string;
  j: boolean;
  g: number | string | boolean | number[] | null;
};

type Vraag = {
  id: string;
  type: VraagType;
  vraag: string;
  opties: string[] | null;
  antwoord: number | string | boolean | number[] | string[];
  uitleg: string | null;
  afbeelding_pad: string | null;
  hoofdstukken: { titel: string } | null;
};

function datum(waarde: string) {
  return new Date(waarde).toLocaleDateString("nl-BE", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
}

function niveauNaam(slug: string) {
  const n = NIVEAUS.find((x) => x.slug === slug);
  return n ? `${n.emoji} ${n.naam}` : slug;
}

/** De examens van een kind, met de nieuwste eerst. */
export async function haalExamens(
  supabase: SupabaseClient,
  kindId: string,
): Promise<ExamenRij[]> {
  const velden = "id, niveau, aantal, juist, afgelegd_op, vakken(naam)";
  const metAntwoorden = await supabase
    .from("examens")
    .select(`${velden}, antwoorden`)
    .eq("kind_id", kindId)
    .order("afgelegd_op", { ascending: false })
    .limit(50);
  if (!metAntwoorden.error)
    return (metAntwoorden.data ?? []) as unknown as ExamenRij[];
  // Bestaat de kolom antwoorden nog niet, dan enkel de score.
  const { data } = await supabase
    .from("examens")
    .select(velden)
    .eq("kind_id", kindId)
    .order("afgelegd_op", { ascending: false })
    .limit(50);
  return (data ?? []) as unknown as ExamenRij[];
}

/** Het lijstje examens met hun score. Een klik toont de foute vragen. */
export function ExamenLijst({
  examens,
  link,
}: {
  examens: ExamenRij[];
  /** Waar de uitslag van één examen staat. */
  link: (examenId: string) => string;
}) {
  return (
    <div className="mt-2 overflow-x-auto rounded-lg border border-border">
      <table className="kaartjes w-full text-sm">
        <thead className="bg-paper text-left text-xs text-ink-dim">
          <tr>
            <th className="px-3 py-2">Vak</th>
            <th className="px-3 py-2">Score</th>
            <th className="px-3 py-2">Wanneer</th>
            <th className="px-3 py-2">Fouten</th>
          </tr>
        </thead>
        <tbody>
          {examens.map((e) => {
            const fouten = e.aantal - e.juist;
            return (
              <tr key={e.id} className="border-t border-border">
                <td data-label="Vak" className="px-3 py-2 text-ink">
                  {e.vakken?.naam ?? "—"}
                  <span className="block text-xs text-ink-dim">
                    {niveauNaam(e.niveau)}
                  </span>
                </td>
                <td data-label="Score" className="px-3 py-2 text-ink">
                  {e.juist}/{e.aantal}
                  {e.aantal > 0 &&
                    ` (${Math.round((e.juist / e.aantal) * 100)}%)`}
                  {e.aantal > 0 && fouten === 0 ? " 🏅 feilloos" : ""}
                </td>
                <td data-label="Wanneer" className="px-3 py-2 text-ink-dim">
                  {datum(e.afgelegd_op)}
                </td>
                <td data-label="Fouten" className="px-3 py-2">
                  {fouten === 0 ? (
                    <span className="text-ink-dim">geen</span>
                  ) : e.antwoorden?.length ? (
                    <Link
                      href={link(e.id)}
                      className="text-forest-dark hover:underline"
                    >
                      Bekijk de {fouten} {fouten === 1 ? "fout" : "fouten"}{" "}
                      &rarr;
                    </Link>
                  ) : (
                    <span className="text-xs text-ink-dim">
                      enkel de score bewaard
                    </span>
                  )}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

/** De uitslag van één examen: eerst wat fout was, daarna wat juist was. */
export async function ExamenDetail({
  supabase,
  kindId,
  examenId,
  kindNaam,
}: {
  supabase: SupabaseClient;
  kindId: string;
  examenId: string;
  kindNaam: string;
}) {
  const { data } = await supabase
    .from("examens")
    .select("id, niveau, aantal, juist, afgelegd_op, antwoorden, vakken(naam)")
    .eq("id", examenId)
    .eq("kind_id", kindId)
    .maybeSingle();
  const examen = data as unknown as ExamenRij | null;
  if (!examen) return null;

  const perVraag = examen.antwoorden ?? [];
  const ids = perVraag.map((p) => p.v);
  const vragen = new Map<string, Vraag>();
  for (let i = 0; i < ids.length; i += 150) {
    const { data: rijen } = await supabase
      .from("vragen")
      .select(
        "id, type, vraag, opties, antwoord, uitleg, afbeelding_pad, hoofdstukken(titel)",
      )
      .in("id", ids.slice(i, i + 150));
    for (const r of (rijen ?? []) as unknown as Vraag[]) vragen.set(r.id, r);
  }

  const fout = perVraag.filter((p) => !p.j);
  const juist = perVraag.filter((p) => p.j);
  const kaart = (p: PerVraag, nr: number) => {
    const vraag = vragen.get(p.v);
    if (!vraag)
      return (
        <div
          key={p.v}
          className="rounded-xl border border-border bg-surface p-5 text-sm text-ink-dim"
        >
          Vraag {nr}: deze vraag werd intussen vervangen en staat niet meer in
          het platform.
        </div>
      );
    const prent =
      vraag.afbeelding_pad && vraag.afbeelding_pad.startsWith("/")
        ? vraag.afbeelding_pad
        : null;
    return (
      <div key={p.v} className="rounded-xl border border-border bg-surface p-5">
        <p className="mb-2 text-xs text-ink-dim">
          Vraag {nr}
          {vraag.hoofdstukken ? ` · ${vraag.hoofdstukken.titel}` : ""}
        </p>
        <VraagTekst tekst={vraag.vraag} />
        {prent && (
          // eslint-disable-next-line @next/next/no-img-element
          <img
            src={prent}
            alt="Afbeelding bij deze vraag"
            className="mt-3 max-h-48 rounded-md border border-border"
          />
        )}
        <div
          className={`mt-3 rounded-md px-3 py-2 text-sm text-ink ${
            p.j ? "bg-forest/10" : "bg-amber/10"
          }`}
        >
          Antwoord van {kindNaam}:{" "}
          <strong>
            {p.g === null ? (
              "overgeslagen"
            ) : (
              <Formule tekst={formatAntwoord(vraag, p.g)} />
            )}
          </strong>
        </div>
        {!p.j && (
          <p className="mt-2 text-sm text-ink-dim">
            Juiste antwoord:{" "}
            <strong className="text-ink">
              <Formule tekst={formatAntwoord(vraag, vraag.antwoord)} />
            </strong>
          </p>
        )}
        {!p.j && vraag.uitleg && (
          <p className="mt-2 text-sm text-ink-dim">
            <Formule tekst={vraag.uitleg} />
          </p>
        )}
      </div>
    );
  };
  const nummer = new Map(perVraag.map((p, i) => [p.v, i + 1]));

  return (
    <>
      <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
        Examen {examen.vakken?.naam ?? ""} — {kindNaam}
      </h1>
      <p className="mt-1 text-sm text-ink-dim">
        {niveauNaam(examen.niveau)} · {datum(examen.afgelegd_op)} · score{" "}
        <strong className="text-ink">
          {examen.juist}/{examen.aantal}
        </strong>
        {examen.aantal > 0 &&
          ` (${Math.round((examen.juist / examen.aantal) * 100)}%)`}
      </p>

      {perVraag.length === 0 ? (
        <p className="mt-6 text-sm text-ink-dim">
          Van dit examen is enkel de score bewaard. Vanaf 24 november 2026
          bewaren we bij elk examen ook welke vragen fout waren.
        </p>
      ) : (
        <>
          <h2 className="mt-8 font-display text-lg font-semibold text-forest-dark">
            {fout.length === 0
              ? "Geen enkele fout 🏅"
              : `Fout of overgeslagen (${fout.length})`}
          </h2>
          <div className="mt-2 space-y-3">
            {fout.map((p) => kaart(p, nummer.get(p.v) ?? 0))}
          </div>
          {juist.length > 0 && (
            <details className="mt-8">
              <summary className="cursor-pointer font-display text-lg font-semibold text-forest-dark">
                Juist ({juist.length})
              </summary>
              <div className="mt-2 space-y-3">
                {juist.map((p) => kaart(p, nummer.get(p.v) ?? 0))}
              </div>
            </details>
          )}
        </>
      )}
    </>
  );
}
