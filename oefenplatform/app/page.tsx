import Link from "next/link";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { heeftVolledigeToegang, hoofdstukToegankelijk } from "@/lib/toegang";
import { createClient } from "@/lib/supabase/server";
import { PRIJS_SCHOOLJAAR_EUR } from "@/lib/mollie";

type Hoofdstuk = { id: string; titel: string; volgnummer: number; gratis: boolean };
type Vak = { id: string; naam: string; slug: string; hoofdstukken: Hoofdstuk[] };

export default async function HomePage() {
  const session = await getSessionProfile();
  const supabase = await createClient();

  const { data: vakken } = await supabase
    .from("vakken")
    .select("id, naam, slug, hoofdstukken(id, titel, volgnummer, gratis)")
    .order("volgorde", { ascending: true });

  const volledigeToegang = heeftVolledigeToegang(session?.profile ?? null);

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">
          Oefenen voor de examencommissie
        </h1>
        <p className="mt-2 max-w-2xl text-sm text-ink-dim">
          Interactieve oefeningen per vak, gemaakt door Connectopia. Van elk vak is één hoofdstuk
          gratis te proberen. Kinderen van de externe plusklas hebben altijd gratis volledige
          toegang.
        </p>

        {!volledigeToegang && (
          <div className="mt-6 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            Volledige toegang tot alle hoofdstukken kost{" "}
            <strong>€{PRIJS_SCHOOLJAAR_EUR} per schooljaar</strong> — de opbrengsten gaan volledig
            naar vzw Connectopia.{" "}
            <Link href={session ? "/betalen" : "/registreren"} className="font-medium text-forest-dark underline-offset-2 hover:underline">
              {session ? "Nu vrijgeven" : "Account maken en starten"}
            </Link>
          </div>
        )}

        <div className="mt-8 space-y-8">
          {(vakken as Vak[] | null)?.map((vak) => (
            <section key={vak.id}>
              <h2 className="font-display text-lg font-semibold text-forest-dark">{vak.naam}</h2>
              <ul className="mt-3 space-y-2">
                {vak.hoofdstukken
                  .sort((a, b) => a.volgnummer - b.volgnummer)
                  .map((h) => {
                    const mag = hoofdstukToegankelijk(h.gratis, session?.profile ?? null);
                    return (
                      <li key={h.id}>
                        <Link
                          href={`/vakken/${vak.slug}/${h.volgnummer}`}
                          className="flex items-center justify-between rounded-lg border border-border bg-surface px-4 py-3 text-sm hover:border-forest"
                        >
                          <span className="text-ink">{h.titel}</span>
                          {h.gratis ? (
                            <span className="rounded-full bg-forest/10 px-2.5 py-0.5 text-xs font-medium text-forest-dark">
                              Gratis
                            </span>
                          ) : mag ? (
                            <span className="rounded-full bg-forest/10 px-2.5 py-0.5 text-xs font-medium text-forest-dark">
                              Vrijgegeven
                            </span>
                          ) : (
                            <span className="rounded-full bg-ink-dim/10 px-2.5 py-0.5 text-xs font-medium text-ink-dim">
                              Op slot
                            </span>
                          )}
                        </Link>
                      </li>
                    );
                  })}
              </ul>
            </section>
          ))}
          {!vakken?.length && (
            <p className="text-sm text-ink-dim">Er zijn nog geen vakken toegevoegd.</p>
          )}
        </div>
      </main>
    </>
  );
}
