import Link from "next/link";
import { Header } from "@/components/Header";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { vindNiveau } from "@/lib/niveaus";
import { zetAfgehandeld, wisMelding } from "./actions";

export const dynamic = "force-dynamic";

const SOORT_LABEL: Record<string, string> = {
  fout: "Fout",
  onduidelijk: "Onduidelijk",
  "te-moeilijk": "Te moeilijk",
  "te-makkelijk": "Te makkelijk",
  andere: "Iets anders",
};

function datum(iso: string) {
  return new Date(iso).toLocaleDateString("nl-BE", {
    day: "numeric",
    month: "long",
    hour: "2-digit",
    minute: "2-digit",
  });
}

export default async function MeldingenPage() {
  const session = await requireBeheerder();
  const supabase = await createClient();

  const { data: meldingen } = await supabase
    .from("meldingen")
    // In één stuk, zonder spatie voor de haakjes: supabase leest deze tekst
    // ook bij het typen, en van een samengeplakte tekst maakt het niets meer.
    .select(
      "id, soort, bericht, afgehandeld, afgehandeld_op, antwoord, profile_id, aangemaakt_op, hoofdstuk:hoofdstukken(id, titel, volgnummer, niveau, vak:vakken(naam, slug)), vraag:vragen(volgnummer, vraag), melder:profiles(full_name)",
    )
    .order("afgehandeld", { ascending: true })
    .order("aangemaakt_op", { ascending: false });

  const rijen = meldingen ?? [];
  const open = rijen.filter((m) => !m.afgehandeld);

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          Meldingen
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {open.length === 0
            ? "Er staat niets open."
            : `${open.length} melding${open.length === 1 ? "" : "en"} wacht${open.length === 1 ? "" : "en"} op jou.`}{" "}
          Afgehandelde meldingen blijven onderaan staan.
        </p>

        <div className="mt-8 space-y-4">
          {rijen.map((m) => {
            // Supabase geeft een gekoppelde tabel terug als object; de
            // typegenerator maakt er soms een lijst van. Dit haalt er in
            // allebei de gevallen één rij uit.
            const hoofdstuk = (
              Array.isArray(m.hoofdstuk) ? m.hoofdstuk[0] : m.hoofdstuk
            ) as {
              id: string;
              titel: string;
              volgnummer: number;
              niveau: string;
              vak: unknown;
            } | null;
            const vak = hoofdstuk
              ? ((Array.isArray(hoofdstuk.vak)
                  ? hoofdstuk.vak[0]
                  : hoofdstuk.vak) as { naam: string; slug: string } | null)
              : null;
            const vraag = (Array.isArray(m.vraag) ? m.vraag[0] : m.vraag) as {
              volgnummer: number;
              vraag: string;
            } | null;
            const melder = (
              Array.isArray(m.melder) ? m.melder[0] : m.melder
            ) as { full_name: string | null } | null;
            const niveau = hoofdstuk ? vindNiveau(hoofdstuk.niveau) : null;

            return (
              <article
                key={m.id}
                className={`rounded-xl border px-5 py-4 text-sm ${
                  m.afgehandeld
                    ? "border-border bg-paper opacity-60"
                    : "border-amber/40 bg-surface"
                }`}
              >
                <div className="flex flex-wrap items-baseline justify-between gap-2">
                  <p className="font-medium text-ink">
                    {niveau ? `${niveau.emoji} ` : ""}
                    {vak?.naam ?? "Onbekend vak"} —{" "}
                    {hoofdstuk?.titel ?? "onbekend hoofdstuk"}
                  </p>
                  <span className="rounded-full bg-amber/15 px-3 py-1 text-xs text-ink">
                    {SOORT_LABEL[m.soort] ?? m.soort}
                  </span>
                </div>

                {vraag && (
                  <p className="mt-1 text-xs text-ink-dim">
                    Over vraag {vraag.volgnummer}: {vraag.vraag}
                  </p>
                )}

                <p className="mt-3 whitespace-pre-wrap text-ink">{m.bericht}</p>

                <p className="mt-3 text-xs text-ink-dim">
                  {datum(m.aangemaakt_op)}
                  {melder?.full_name
                    ? ` · ${melder.full_name}`
                    : " · zonder account"}
                </p>

                {m.afgehandeld && m.antwoord && (
                  <p className="mt-2 text-xs text-ink-dim">
                    Je schreef terug: &laquo;&nbsp;{m.antwoord}&nbsp;&raquo;
                  </p>
                )}

                <div className="mt-3 flex flex-wrap items-center gap-4">
                  {vak && hoofdstuk && (
                    <Link
                      href={`/beheer/vakken/${vak.slug}/${hoofdstuk.volgnummer}`}
                      className="text-forest-dark hover:underline"
                    >
                      Naar het hoofdstuk &rarr;
                    </Link>
                  )}
                  <form action={wisMelding}>
                    <input type="hidden" name="id" value={m.id} />
                    <button
                      type="submit"
                      className="text-ink-dim hover:text-danger"
                    >
                      Wissen
                    </button>
                  </form>
                </div>

                {/* Afvinken staat apart, want er hoort een veld bij: wie
                    ingelogd meldde, krijgt jouw woordje bovenaan het platform
                    te zien. Zie supabase/melding-antwoord.sql. */}
                <form
                  action={zetAfgehandeld}
                  className="mt-3 border-t border-border pt-3"
                >
                  <input type="hidden" name="id" value={m.id} />
                  <input
                    type="hidden"
                    name="naar"
                    value={m.afgehandeld ? "false" : "true"}
                  />

                  {!m.afgehandeld &&
                    (m.profile_id ? (
                      <div className="mb-2">
                        <label
                          htmlFor={`antwoord-${m.id}`}
                          className="block text-xs text-ink-dim"
                        >
                          Een woordje terug, mag leeg blijven.{" "}
                          {melder?.full_name ?? "Deze persoon"} ziet het de
                          volgende keer bovenaan het platform.
                        </label>
                        <input
                          id={`antwoord-${m.id}`}
                          name="antwoord"
                          maxLength={500}
                          placeholder="Bedankt, we hebben het aangepast."
                          className="mt-1 w-full rounded-md border border-border bg-surface px-2 py-1.5 text-sm text-ink"
                        />
                      </div>
                    ) : (
                      <p className="mb-2 text-xs text-ink-dim">
                        Deze melding kwam binnen zonder account, dus we kunnen
                        er niets op terugsturen.
                      </p>
                    ))}

                  <button
                    type="submit"
                    className="text-sm text-ink-dim hover:text-ink"
                  >
                    {m.afgehandeld ? "Terug openzetten" : "Afgehandeld"}
                  </button>
                </form>
              </article>
            );
          })}

          {rijen.length === 0 && (
            <p className="text-sm text-ink-dim">
              Er zijn nog geen meldingen binnengekomen. Ze verschijnen hier
              zodra iemand op &laquo;&nbsp;Iets gezien dat niet
              klopt&nbsp;&raquo; klikt in een hoofdstuk.
            </p>
          )}
        </div>
      </main>
    </>
  );
}
