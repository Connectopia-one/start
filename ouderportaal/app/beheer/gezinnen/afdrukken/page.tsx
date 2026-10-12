import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { FicheRegels } from "@/components/FicheRegels";
import {
  KINDVELDEN,
  watOntbreekt,
  watOntbreektGezin,
  lijstZin,
  samen,
  type Kind,
} from "@/lib/kind";

export const dynamic = "force-dynamic";

/*
  Alle inlichtingenfiches op papier.

  Kim op 12 oktober 2026: "kan ik ook de inlichtingsfiches afdrukken zodat we
  die op papier hebben in geval van stroompanne of als het internet plat ligt."

  Dat is de enige reden dat deze bladzijde bestaat, en ze bepaalt hoe ze eruit
  ziet: geen knoppen, geen menu, alles open, en elk kind in een blok dat niet
  over twee bladen mag breken. Wat op het scherm weggelaten wordt omdat het
  leeg is, blijft ook hier weg, maar wat ontbreekt staat er wél bij: op een
  kamp wil je weten dat je geen noodnummer hebt, niet dat de regel er niet is.

  De fiches per kampdag staan apart, op de bladzijde van de activiteit zelf;
  die print even goed. Deze bladzijde is er voor de volledige map.
*/
export default async function AfdrukkenPage() {
  const session = await requireBeheerder();

  const supabase = await createClient();
  const [{ data: gezinnen }, { data: kinderen }] = await Promise.all([
    supabase
      .from("profiles")
      .select("id, full_name, telefoon, adres")
      .eq("role", "ouder")
      .order("full_name"),
    supabase.from("kinderen").select(`profile_id, ${KINDVELDEN}`).order("naam"),
  ]);

  const kinderenVan = new Map<string, Kind[]>();
  for (const rij of (kinderen ?? []) as unknown as (Kind & {
    profile_id: string;
  })[]) {
    const lijst = kinderenVan.get(rij.profile_id) ?? [];
    lijst.push(rij);
    kinderenVan.set(rij.profile_id, lijst);
  }

  const vandaag = new Date().toLocaleDateString("nl-BE", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });

  return (
    <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
      <div className="flex flex-wrap items-center justify-between gap-3 print:hidden">
        <Link
          href="/beheer/gezinnen"
          className="text-sm text-ink-dim hover:text-ink"
        >
          &larr; Gezinnen
        </Link>
        <p className="text-sm text-ink-dim">
          Druk deze bladzijde af met Ctrl en P, of Cmd en P op een Mac.
        </p>
      </div>

      <h1 className="mt-4 font-display text-2xl font-semibold text-ink">
        Inlichtingenfiches
      </h1>
      <p className="mt-1 text-sm text-ink-dim">
        Connectopia vzw · uitgedraaid op {vandaag} door{" "}
        {session.profile?.full_name ?? session.email}
      </p>
      <p className="mt-3 text-xs text-ink-dim">
        Deze bladzijden bevatten medische en persoonlijke gegevens van
        kinderen. Hou ze bij je en gooi ze na het kamp weg bij het
        vertrouwelijk papier.
      </p>

      {(gezinnen ?? []).length === 0 && (
        <p className="mt-8 text-sm text-ink-dim">Er zijn nog geen gezinnen.</p>
      )}

      {(gezinnen ?? []).map((gezin) => {
        const eigen = kinderenVan.get(gezin.id) ?? [];
        const gezinsgegevens = watOntbreektGezin(gezin);
        return (
          <section key={gezin.id} className="mt-8">
            <h2 className="border-b border-border pb-1 font-display text-lg font-semibold text-ink">
              {gezin.full_name}
            </h2>
            <p className="mt-1 text-sm text-ink-dim">
              {samen(gezin.telefoon, gezin.adres) || "geen contactgegevens"}
            </p>
            {gezinsgegevens.length > 0 && (
              <p className="mt-1 text-sm text-danger">
                Nog nodig van dit gezin: {lijstZin(gezinsgegevens)}.
              </p>
            )}

            {eigen.length === 0 && (
              <p className="mt-2 text-sm text-danger">
                Er staat nog geen kind op dit gezin.
              </p>
            )}

            <div className="mt-3 space-y-3">
              {eigen.map((kind) => {
                const ontbreekt = watOntbreekt(kind);
                return (
                  <div
                    key={kind.id}
                    className="rounded-lg border border-border bg-surface p-4 text-sm print:break-inside-avoid"
                  >
                    <p className="font-medium text-ink">
                      {kind.naam}
                      {kind.geboortedatum && (
                        <span className="ml-2 text-xs font-normal text-ink-dim">
                          geboren{" "}
                          {new Date(kind.geboortedatum).toLocaleDateString(
                            "nl-BE",
                            { day: "numeric", month: "long", year: "numeric" },
                          )}
                        </span>
                      )}
                    </p>
                    <FicheRegels kind={kind} />
                    {ontbreekt.length > 0 && (
                      <p className="mt-2 text-danger">
                        Nog nodig: {lijstZin(ontbreekt)}.
                      </p>
                    )}
                  </div>
                );
              })}
            </div>
          </section>
        );
      })}
    </main>
  );
}
