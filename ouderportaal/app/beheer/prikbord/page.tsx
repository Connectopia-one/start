import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import {
  handelMeldingAf,
  markeerGezien,
  verwijderBriefje,
  zetZichtbaar,
} from "./actions";

/* De briefjes komen binnen terwijl je kijkt, dus niets bewaren. */
export const dynamic = "force-dynamic";

type Briefje = {
  id: string;
  bord: string;
  tekst: string;
  naam: string | null;
  volledige_naam: string | null;
  contact: string | null;
  wanneer: string | null;
  zichtbaar: boolean;
  gemeld: number;
  gezien: boolean;
  created_at: string;
};

type Melding = {
  id: string;
  briefje_id: string;
  reden: string | null;
  afgehandeld: boolean;
  created_at: string;
};

function tijdstip(waarde: string) {
  return new Date(waarde).toLocaleString("nl-BE", {
    day: "numeric",
    month: "long",
    hour: "2-digit",
    minute: "2-digit",
  });
}

export default async function PrikbordBeheer({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; succes?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout, succes } = await searchParams;
  const naam = session.profile?.full_name ?? session.email ?? "";

  const db = createAdminClient();
  const [{ data: briefjesData }, { data: meldingenData }] = await Promise.all([
    db
      .from("prikbord_briefjes")
      .select(
        "id, bord, tekst, naam, volledige_naam, contact, wanneer, zichtbaar, gemeld, gezien, created_at",
      )
      .order("created_at", { ascending: false })
      .limit(200),
    db
      .from("prikbord_meldingen")
      .select("id, briefje_id, reden, afgehandeld, created_at")
      .eq("afgehandeld", false)
      .order("created_at", { ascending: false })
      .limit(200),
  ]);

  const briefjes = (briefjesData ?? []) as Briefje[];
  const meldingen = (meldingenData ?? []) as Melding[];
  const nieuw = briefjes.filter((b) => !b.gezien).length;

  const meldingenPer = new Map<string, Melding[]>();
  for (const melding of meldingen) {
    const rij = meldingenPer.get(melding.briefje_id) ?? [];
    rij.push(melding);
    meldingenPer.set(melding.briefje_id, rij);
  }

  return (
    <>
      <Header
        naam={naam}
        rol="beheerder"
        terugHref="/beheer"
        terugLabel="Beheer"
      />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">
          Prikbord
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {briefjes.length} briefje{briefjes.length === 1 ? "" : "s"}
          {nieuw > 0 ? ` · ${nieuw} nieuw` : ""}
          {meldingen.length > 0
            ? ` · ${meldingen.length} openstaande melding${meldingen.length === 1 ? "" : "en"}`
            : ""}
        </p>

        {fout && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            {fout}
          </p>
        )}
        {succes && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">
            {succes}
          </p>
        )}

        {nieuw > 0 && (
          <form action={markeerGezien} className="mt-4">
            <button
              type="submit"
              className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
            >
              Alles als gezien markeren
            </button>
          </form>
        )}

        <ul className="mt-6 space-y-3">
          {briefjes.map((briefje) => {
            const eigenMeldingen = meldingenPer.get(briefje.id) ?? [];
            return (
              <li
                key={briefje.id}
                className={`rounded-lg border bg-surface p-4 ${
                  briefje.gezien ? "border-border" : "border-forest"
                }`}
              >
                <div className="flex flex-wrap items-center gap-2 text-xs text-ink-dim">
                  <span className="rounded-full bg-paper px-2 py-0.5 font-medium">
                    {briefje.bord}
                  </span>
                  <span>{tijdstip(briefje.created_at)}</span>
                  {!briefje.gezien && (
                    <span className="font-semibold text-forest-dark">
                      nieuw
                    </span>
                  )}
                  {!briefje.zichtbaar && (
                    <span className="font-semibold text-danger">
                      niet zichtbaar
                    </span>
                  )}
                  {briefje.gemeld > 0 && (
                    <span className="font-semibold text-danger">
                      {briefje.gemeld}x gemeld
                    </span>
                  )}
                </div>

                {briefje.wanneer && (
                  <p className="mt-2 text-sm font-semibold text-ink">
                    {briefje.wanneer}
                  </p>
                )}
                <p className="mt-1 whitespace-pre-line text-ink">
                  {briefje.tekst}
                </p>

                <p className="mt-2 text-sm text-ink-dim">
                  Op het bord als <strong>{briefje.naam ?? "—"}</strong> · bij
                  ons bekend als {briefje.volledige_naam ?? "—"}
                  {briefje.contact ? ` · ${briefje.contact}` : ""}
                </p>

                {eigenMeldingen.length > 0 && (
                  <ul className="mt-3 space-y-2 border-l-2 border-danger/40 pl-3">
                    {eigenMeldingen.map((melding) => (
                      <li key={melding.id} className="text-sm">
                        <p className="text-ink">
                          {melding.reden || "Zonder uitleg gemeld."}
                        </p>
                        <div className="mt-1 flex items-center gap-3 text-xs text-ink-dim">
                          <span>{tijdstip(melding.created_at)}</span>
                          <form action={handelMeldingAf}>
                            <input type="hidden" name="id" value={melding.id} />
                            <button
                              type="submit"
                              className="underline hover:text-forest-dark"
                            >
                              Afvinken
                            </button>
                          </form>
                        </div>
                      </li>
                    ))}
                  </ul>
                )}

                <div className="mt-3 flex flex-wrap gap-2">
                  <form action={zetZichtbaar}>
                    <input type="hidden" name="id" value={briefje.id} />
                    <input
                      type="hidden"
                      name="zichtbaar"
                      value={briefje.zichtbaar ? "nee" : "ja"}
                    />
                    <button
                      type="submit"
                      className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
                    >
                      {briefje.zichtbaar
                        ? "Van het bord halen"
                        : "Terug op het bord"}
                    </button>
                  </form>

                  {!briefje.gezien && (
                    <form action={markeerGezien}>
                      <input type="hidden" name="id" value={briefje.id} />
                      <button
                        type="submit"
                        className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
                      >
                        Gezien
                      </button>
                    </form>
                  )}

                  <form action={verwijderBriefje}>
                    <input type="hidden" name="id" value={briefje.id} />
                    <button
                      type="submit"
                      className="rounded-md border border-danger/40 px-3 py-1.5 text-sm text-danger hover:bg-danger/10"
                    >
                      Verwijderen
                    </button>
                  </form>
                </div>
              </li>
            );
          })}

          {briefjes.length === 0 && (
            <li className="text-sm text-ink-dim">
              Er hangt nog geen enkel briefje op het prikbord.
            </li>
          )}
        </ul>
      </main>
    </>
  );
}
