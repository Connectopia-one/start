import { requireStaff } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";

type Kind = {
  id: string;
  naam: string;
  geboortedatum: string | null;
  allergieen: string | null;
  diagnoses: string | null;
  noodcontact_naam: string | null;
  noodcontact_telefoon: string | null;
  toestemming_fotos: boolean;
  toestemming_social_media: boolean;
  profiles: { full_name: string } | { full_name: string }[] | null;
};

function gezinsnaam(kind: Kind): string {
  const profiel = Array.isArray(kind.profiles) ? kind.profiles[0] : kind.profiles;
  return profiel?.full_name ?? "";
}

export default async function TeamKinderenPage() {
  const session = await requireStaff();
  const naam = session.profile?.full_name ?? session.email ?? "";
  const rol = session.profile?.role ?? "ouder";

  const supabase = await createClient();
  const { data } = await supabase
    .from("kinderen")
    .select(
      "id, naam, geboortedatum, allergieen, diagnoses, noodcontact_naam, noodcontact_telefoon, toestemming_fotos, toestemming_social_media, profiles(full_name)"
    )
    .order("naam");

  const kinderen = (data as Kind[] | null) ?? [];

  return (
    <>
      <Header naam={naam} rol={rol} terugHref="/team" terugLabel="Team" />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">Inlichtingenfiches</h1>
        <p className="mt-1 text-sm text-ink-dim">Alle kinderen, over alle klasjes heen.</p>

        <div className="mt-6 space-y-4">
          {kinderen.map((kind) => (
            <div key={kind.id} className="rounded-xl border border-border bg-surface p-5 text-sm">
              <p className="font-display font-semibold text-ink">
                {kind.naam}
                {kind.geboortedatum && (
                  <span className="ml-2 font-sans text-xs font-normal text-ink-dim">
                    geboren {new Date(kind.geboortedatum).toLocaleDateString("nl-BE")}
                  </span>
                )}
              </p>
              {gezinsnaam(kind) && <p className="text-xs text-ink-dim">Gezin: {gezinsnaam(kind)}</p>}

              {kind.allergieen && (
                <p className="mt-2">
                  <strong className="text-ink">Allergieën: </strong>
                  <span className="text-ink-dim">{kind.allergieen}</span>
                </p>
              )}
              {kind.diagnoses && (
                <p className="mt-1">
                  <strong className="text-ink">Diagnoses: </strong>
                  <span className="text-ink-dim">{kind.diagnoses}</span>
                </p>
              )}
              {(kind.noodcontact_naam || kind.noodcontact_telefoon) && (
                <p className="mt-1">
                  <strong className="text-ink">Noodcontact: </strong>
                  <span className="text-ink-dim">
                    {[kind.noodcontact_naam, kind.noodcontact_telefoon].filter(Boolean).join(" — ")}
                  </span>
                </p>
              )}
              <div className="mt-2 flex flex-wrap gap-2">
                <span
                  className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${kind.toestemming_fotos ? "bg-forest/10 text-forest-dark" : "bg-danger/10 text-danger"}`}
                >
                  {kind.toestemming_fotos ? "Toestemming foto's" : "Geen toestemming foto's"}
                </span>
                <span
                  className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${kind.toestemming_social_media ? "bg-forest/10 text-forest-dark" : "bg-danger/10 text-danger"}`}
                >
                  {kind.toestemming_social_media ? "Toestemming social media" : "Geen toestemming social media"}
                </span>
              </div>
            </div>
          ))}
          {kinderen.length === 0 && <p className="text-sm text-ink-dim">Nog geen fiches ingevuld.</p>}
        </div>
      </main>
    </>
  );
}
