import { schrijfInvul, schrijfKeuzes } from "@/lib/antwoord";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { requireIngelogd } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { VraagTekst } from "@/components/Figuren";
import { variantVoorBeurt } from "@/lib/spellingvariant";

type Vraag = {
  id: string;
  volgnummer: number;
  type: "meerkeuze" | "invultekst" | "waarofniet";
  // antwoord kan een lijstje nummers zijn: dan is er meer dan één juist.
  vraag: string;
  opties: string[] | null;
  antwoord: number | string | boolean | number[] | string[];
  uitleg: string | null;
  /** Wisselende woorden bij spelling; zie lib/spellingvariant.ts. */
  varianten?: unknown;
};

type VoortgangRij = {
  vraag_id: string;
  correct: boolean;
  gegeven_antwoord: number | string | boolean | number[] | null;
  beantwoord_op: string;
  /** Welke beurt het kind kreeg. 0 of niets: de vraag zelf. */
  variant?: number | null;
};

function formatAntwoord(
  vraag: Vraag,
  waarde: number | string | boolean | number[] | string[] | null,
): string {
  if (waarde === null || waarde === undefined || waarde === "") return "—";
  if (vraag.type === "meerkeuze") return schrijfKeuzes(vraag.opties, waarde);
  if (vraag.type === "waarofniet") {
    return waarde === true ? "Waar" : "Niet waar";
  }
  // Een invulvraag kan meer dan één juist antwoord hebben; we tonen het eerste.
  if (Array.isArray(waarde)) return schrijfInvul(waarde);
  return String(waarde);
}

export default async function HoofdstukAntwoordenPage({
  params,
}: {
  params: Promise<{ kindId: string; hoofdstukId: string }>;
}) {
  const session = await requireIngelogd();
  const { kindId, hoofdstukId } = await params;
  const supabase = await createClient();

  const { data: kind } = await supabase
    .from("kinderen")
    .select("id, naam, profile_id")
    .eq("id", kindId)
    .single();
  if (
    !kind ||
    (kind.profile_id !== session.userId &&
      session.profile?.role !== "beheerder")
  )
    notFound();

  const { data: hoofdstuk } = await supabase
    .from("hoofdstukken")
    .select("id, titel, vakken(naam)")
    .eq("id", hoofdstukId)
    .single<{ id: string; titel: string; vakken: { naam: string } }>();
  if (!hoofdstuk) notFound();

  const [{ data: vragen }, { data: voortgang }] = await Promise.all([
    // "*" en niet de kolommen apart: zolang spellingvarianten.sql nog niet
    // gedraaid is, bestaan "varianten" en "variant" nog niet, en een select op
    // die namen zou dit scherm dan helemaal leeg laten.
    supabase
      .from("vragen")
      .select("*")
      .eq("hoofdstuk_id", hoofdstukId)
      .order("volgnummer", { ascending: true }),
    supabase
      .from("voortgang")
      .select("*")
      .eq("kind_id", kindId)
      .order("beantwoord_op", { ascending: false }),
  ]);

  const laatsteAntwoordPerVraag = new Map<string, VoortgangRij>();
  for (const rij of (voortgang ?? []) as VoortgangRij[]) {
    if (!laatsteAntwoordPerVraag.has(rij.vraag_id))
      laatsteAntwoordPerVraag.set(rij.vraag_id, rij);
  }

  return (
    <>
      <Header naam={session.profile?.full_name} rol={session.profile?.role} />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <Link
          href={`/account/kinderen/${kindId}`}
          className="text-sm text-ink-dim hover:text-ink"
        >
          &larr; Voortgang — {kind.naam}
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          {hoofdstuk.vakken.naam} — {hoofdstuk.titel}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          Antwoorden van de laatste poging per vraag.
        </p>

        <div className="mt-6 space-y-3">
          {((vragen ?? []) as Vraag[]).map((rij) => {
            const laatste = laatsteAntwoordPerVraag.get(rij.id);
            // Kreeg het kind bij een spellingvraag een ander woord, dan staat
            // dát woord hier, niet de vraag zoals ze in de databank staat.
            const vraag = variantVoorBeurt(
              rij,
              rij.varianten,
              laatste?.variant,
            );
            return (
              <div
                key={vraag.id}
                className="rounded-xl border border-border bg-surface p-5"
              >
                <VraagTekst tekst={vraag.vraag} />
                {!laatste ? (
                  <p className="mt-2 text-sm text-ink-dim">
                    Nog niet geprobeerd.
                  </p>
                ) : (
                  <>
                    <div
                      className={`mt-3 rounded-md px-3 py-2 text-sm ${
                        laatste.correct
                          ? "bg-forest/10 text-forest-dark"
                          : "bg-danger/10 text-danger"
                      }`}
                    >
                      Antwoord van {kind.naam}:{" "}
                      <strong>
                        {formatAntwoord(vraag, laatste.gegeven_antwoord)}
                      </strong>
                    </div>
                    {!laatste.correct && (
                      <p className="mt-2 text-sm text-ink-dim">
                        Juiste antwoord:{" "}
                        <strong className="text-ink">
                          {formatAntwoord(vraag, vraag.antwoord)}
                        </strong>
                      </p>
                    )}
                    {vraag.uitleg && (
                      <p className="mt-2 text-sm text-ink-dim">
                        {vraag.uitleg}
                      </p>
                    )}
                    <p className="mt-2 text-xs text-ink-dim">
                      {new Date(laatste.beantwoord_op).toLocaleDateString(
                        "nl-BE",
                        {
                          day: "numeric",
                          month: "short",
                          year: "numeric",
                        },
                      )}
                    </p>
                  </>
                )}
              </div>
            );
          })}
          {!vragen?.length && (
            <p className="text-sm text-ink-dim">
              Dit hoofdstuk heeft nog geen vragen.
            </p>
          )}
        </div>
      </main>
    </>
  );
}
