import { notFound } from "next/navigation";
import { requireStaff } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { Aanwezigheid, AanwezigheidStand } from "@/components/Aanwezigheid";
import {
  ACTIVITEITVELDEN,
  datumTekst,
  leeftijd,
  type Activiteit,
} from "@/lib/activiteiten";
import { alleAanwezig } from "@/app/beheer/activiteiten/actions";

export const dynamic = "force-dynamic";

type Deelname = {
  kind_id: string;
  notitie: string | null;
  aanwezig: boolean | null;
};
type KindRij = { id: string; naam: string; geboortedatum: string | null };

/*
  Aanduiden wie er was, op één dag.

  Dit scherm is voor een begeleider met een gsm in de hand: namen, twee
  knopjes, en de notitie van die dag als er een staat. De fiches met de
  allergieën staan apart op /team/kinderen, zodat deze lijst kort blijft.
*/
export default async function TeamAanwezigheid({
  params,
  searchParams,
}: {
  params: Promise<{ id: string }>;
  searchParams: Promise<{ fout?: string }>;
}) {
  const { id } = await params;
  const { fout } = await searchParams;
  const session = await requireStaff();
  const naam = session.profile?.full_name ?? session.email ?? "";
  const rol = session.profile?.role ?? "ouder";

  const supabase = await createClient();
  const [{ data: activiteitData }, { data: deelnamesData }] = await Promise.all(
    [
      supabase
        .from("activiteiten")
        .select(ACTIVITEITVELDEN)
        .eq("id", id)
        .maybeSingle(),
      supabase
        .from("deelnames")
        .select("kind_id, notitie, aanwezig")
        .eq("activiteit_id", id),
    ],
  );

  if (!activiteitData) notFound();
  const activiteit = activiteitData as Activiteit;
  const deelnames = (deelnamesData ?? []) as Deelname[];

  const { data: kinderenData } = await supabase
    .from("kinderen")
    .select("id, naam, geboortedatum")
    .order("naam");

  const kinderen = ((kinderenData ?? []) as KindRij[]).filter((kind) =>
    deelnames.some((d) => d.kind_id === kind.id),
  );
  const deelnameVan = new Map(deelnames.map((d) => [d.kind_id, d]));
  const nietAangeduid = deelnames.filter((d) => d.aanwezig === null).length;
  const aanwezigen = deelnames.filter((d) => d.aanwezig !== false).length;
  const terug = `/team/aanwezigheden/${id}`;

  return (
    <>
      <Header
        naam={naam}
        rol={rol}
        terugHref="/team/aanwezigheden"
        terugLabel="Aanwezigheden"
      />
      <main className="mx-auto w-full max-w-xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">
          {activiteit.naam}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {datumTekst(activiteit.datum)}
          {activiteit.plaats && ` · ${activiteit.plaats}`}
        </p>
        {kinderen.length > 0 && (
          <p className="mt-0.5 text-sm text-ink-dim">
            <AanwezigheidStand
              aanwezigen={aanwezigen}
              nietAangeduid={nietAangeduid}
            />
          </p>
        )}

        {fout && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            {fout}
          </p>
        )}

        {kinderen.length === 0 && (
          <p className="mt-6 text-sm text-ink-dim">
            Er staat nog geen kind op deze dag. Kim duidt dat aan bij het gezin.
          </p>
        )}

        {nietAangeduid > 0 && (
          <form action={alleAanwezig} className="mt-6">
            <input type="hidden" name="activiteit_id" value={id} />
            <input type="hidden" name="terug" value={terug} />
            <button
              type="submit"
              className="rounded-md border border-forest px-3 py-1.5 text-sm font-medium text-forest-dark hover:bg-forest/10"
            >
              Iedereen op aanwezig zetten
            </button>
            <p className="mt-1.5 text-xs text-ink-dim">
              Daarna vink je enkel nog af wie er niet was.
            </p>
          </form>
        )}

        <ul className="mt-6 space-y-2">
          {kinderen.map((kind) => {
            const deelname = deelnameVan.get(kind.id);
            const jaar = leeftijd(kind.geboortedatum);
            return (
              <li
                key={kind.id}
                className="flex flex-wrap items-center justify-between gap-3 rounded-lg border border-border bg-surface p-4"
              >
                <div>
                  <p className="font-medium text-ink">
                    {kind.naam}
                    {jaar !== null && (
                      <span className="ml-2 text-xs font-normal text-ink-dim">
                        {jaar} jaar
                      </span>
                    )}
                  </p>
                  {deelname?.notitie && (
                    <p className="mt-0.5 text-xs text-ink-dim">
                      {deelname.notitie}
                    </p>
                  )}
                </div>
                <Aanwezigheid
                  activiteitId={id}
                  kindId={kind.id}
                  waarde={deelname?.aanwezig ?? null}
                  terug={terug}
                />
              </li>
            );
          })}
        </ul>
      </main>
    </>
  );
}
