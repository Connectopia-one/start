import Link from "next/link";
import { requireStaff } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import {
  ACTIVITEITVELDEN,
  datumTekst,
  type Activiteit,
} from "@/lib/activiteiten";

export const dynamic = "force-dynamic";

/*
  De dagen waarop een begeleider de aanwezigheden kan aanduiden.

  Kim op 11 oktober 2026: "kan ik dan ergens de aanwezigheden aanduiden of de
  begeleiders. Dan hebben we ineens ook de juiste aantallen die maand."

  Wat vandaag of straks doorgaat staat bovenaan, wat voorbij is daaronder met
  de laatste dag eerst. Een activiteit zonder datum staat er niet bij: daar is
  geen dag om aanwezig op te zijn.
*/
export default async function TeamAanwezigheden() {
  const session = await requireStaff();
  const naam = session.profile?.full_name ?? session.email ?? "";
  const rol = session.profile?.role ?? "ouder";

  const supabase = await createClient();
  const [{ data: activiteitenData }, { data: deelnamesData }] =
    await Promise.all([
      supabase
        .from("activiteiten")
        .select(ACTIVITEITVELDEN)
        .eq("archief", false)
        .not("datum", "is", null)
        .order("datum", { ascending: true }),
      supabase.from("deelnames").select("activiteit_id, aanwezig"),
    ]);

  const activiteiten = (activiteitenData ?? []) as Activiteit[];
  const deelnames = (deelnamesData ?? []) as {
    activiteit_id: string;
    aanwezig: boolean | null;
  }[];

  const aantal = new Map<string, number>();
  const open = new Map<string, number>();
  for (const rij of deelnames) {
    aantal.set(rij.activiteit_id, (aantal.get(rij.activiteit_id) ?? 0) + 1);
    if (rij.aanwezig === null)
      open.set(rij.activiteit_id, (open.get(rij.activiteit_id) ?? 0) + 1);
  }

  const vandaag = new Date().toISOString().slice(0, 10);
  const komend = activiteiten.filter((a) => (a.datum ?? "") >= vandaag);
  const voorbij = activiteiten
    .filter((a) => (a.datum ?? "") < vandaag)
    .reverse()
    .slice(0, 20);

  return (
    <>
      <Header naam={naam} rol={rol} terugHref="/team" terugLabel="Team" />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">
          Aanwezigheden
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          Kies de dag en vink aan wie er was. Wat je niet aanduidt, geldt als
          aanwezig.
        </p>

        {activiteiten.length === 0 && (
          <p className="mt-6 text-sm text-ink-dim">
            Er staat nog geen dag met een datum klaar.
          </p>
        )}

        {komend.length > 0 && (
          <section className="mt-8">
            <h2 className="font-display text-base font-semibold text-ink">
              Vandaag en daarna
            </h2>
            <ul className="mt-3 space-y-2">
              {komend.map((activiteit) => (
                <Rij
                  key={activiteit.id}
                  activiteit={activiteit}
                  aantal={aantal.get(activiteit.id) ?? 0}
                  open={open.get(activiteit.id) ?? 0}
                />
              ))}
            </ul>
          </section>
        )}

        {voorbij.length > 0 && (
          <section className="mt-8">
            <h2 className="font-display text-base font-semibold text-ink">
              Voorbij
            </h2>
            <ul className="mt-3 space-y-2">
              {voorbij.map((activiteit) => (
                <Rij
                  key={activiteit.id}
                  activiteit={activiteit}
                  aantal={aantal.get(activiteit.id) ?? 0}
                  open={open.get(activiteit.id) ?? 0}
                />
              ))}
            </ul>
          </section>
        )}
      </main>
    </>
  );
}

function Rij({
  activiteit,
  aantal,
  open,
}: {
  activiteit: Activiteit;
  aantal: number;
  open: number;
}) {
  return (
    <li className="rounded-lg border border-border bg-surface p-4">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <div>
          <Link
            href={`/team/aanwezigheden/${activiteit.id}`}
            className="font-medium text-ink underline-offset-2 hover:underline"
          >
            {activiteit.naam}
          </Link>
          <p className="mt-0.5 text-xs text-ink-dim">
            {datumTekst(activiteit.datum)}
            {activiteit.plaats && ` · ${activiteit.plaats}`}
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-2">
          {open > 0 ? (
            <span className="rounded-full bg-amber/15 px-2.5 py-0.5 text-xs font-medium text-ink">
              {open} aan te duiden
            </span>
          ) : (
            aantal > 0 && (
              <span className="rounded-full bg-forest/10 px-2.5 py-0.5 text-xs font-medium text-forest-dark">
                alles aangeduid
              </span>
            )
          )}
          <Link
            href={`/team/aanwezigheden/${activiteit.id}`}
            className="rounded-md bg-forest px-3 py-1.5 text-sm font-medium text-white hover:bg-forest-dark"
          >
            Aanduiden
          </Link>
        </div>
      </div>
    </li>
  );
}
