import Link from "next/link";
import { Header } from "@/components/Header";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { huidigSchooljaar } from "@/lib/schooljaar";
import { zetVolledigeToegang } from "./actions";

type Rij = {
  id: string;
  full_name: string;
  role: string;
  is_plusklas: boolean;
  toegang_schooljaar: string | null;
  created_at: string;
  kinderen: { id: string; naam: string }[] | null;
};

export const metadata = { title: "Gezinnen — Oefenplatform Connectopia" };

function datum(waarde: string) {
  return new Date(waarde).toLocaleDateString("nl-BE", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
}

export default async function GezinnenPage({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; melding?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout, melding } = await searchParams;

  /* Met de service-sleutel, want we willen ook accounts zonder kind zien. */
  const admin = createAdminClient();
  const { data } = await admin
    .from("profiles")
    .select("id, full_name, role, is_plusklas, toegang_schooljaar, created_at, kinderen(id, naam)")
    .order("created_at", { ascending: false });

  const rijen = (data ?? []) as Rij[];
  const gezinnen = rijen.filter((r) => r.role !== "beheerder");
  const schooljaar = huidigSchooljaar();
  const metToegang = gezinnen.filter(
    (r) => r.is_plusklas || r.toegang_schooljaar === schooljaar
  ).length;

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">Gezinnen</h1>
        <p className="mt-2 text-sm text-ink-dim">
          Wie heeft volledige toegang, en waar komt die vandaan? Toegang uitzetten
          raakt niets van wat een gezin opgebouwd heeft: de kinderen, hun voortgang
          en hun stickers blijven staan, ze zien daarna enkel nog de gratis
          hoofdstukken. Zet je de toegang later weer aan, dan pikken ze op waar ze
          gestopt waren.
        </p>
        <p className="mt-2 text-sm text-ink-dim">
          Een gezin dat betaald heeft voor dit schooljaar ({schooljaar}) houdt zijn
          toegang, ook als de knop hier op uit staat. Die knop gaat enkel over de
          gratis toegang die je zelf geeft, bijvoorbeeld met een code.
        </p>

        {fout && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>
        )}
        {melding && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">
            {melding}
          </p>
        )}

        <p className="mt-6 text-sm text-ink-dim">
          {gezinnen.length} {gezinnen.length === 1 ? "account" : "accounts"}, waarvan{" "}
          <span className="font-medium text-ink">{metToegang}</span> met volledige toegang.
        </p>

        <ul className="mt-3 space-y-2">
          {gezinnen.map((r) => {
            const kinderen = r.kinderen ?? [];
            const betaald = r.toegang_schooljaar === schooljaar;
            return (
              <li
                key={r.id}
                className="rounded-lg border border-border bg-surface px-4 py-3"
              >
                <div className="flex flex-wrap items-center justify-between gap-3">
                  <div>
                    <p className="text-sm font-medium text-ink">{r.full_name}</p>
                    <p className="mt-0.5 text-xs text-ink-dim">
                      {kinderen.length === 0
                        ? "nog geen kind toegevoegd"
                        : `${kinderen.length} ${kinderen.length === 1 ? "kind" : "kinderen"}: ${kinderen
                            .map((k) => k.naam)
                            .join(", ")}`}
                      {" · sinds "}
                      {datum(r.created_at)}
                      {r.role === "begeleider" && " · begeleider"}
                    </p>
                  </div>
                  <div className="flex items-center gap-3">
                    <span
                      className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${
                        r.is_plusklas
                          ? "bg-forest/10 text-forest-dark"
                          : betaald
                            ? "bg-amber/15 text-amber"
                            : "bg-ink-dim/10 text-ink-dim"
                      }`}
                    >
                      {r.is_plusklas
                        ? "Gratis toegang van jou"
                        : betaald
                          ? `Betaald ${r.toegang_schooljaar}`
                          : "Enkel de gratis hoofdstukken"}
                    </span>
                    <form action={zetVolledigeToegang}>
                      <input type="hidden" name="id" value={r.id} />
                      <input type="hidden" name="aan" value={r.is_plusklas ? "nee" : "ja"} />
                      <button
                        type="submit"
                        className="rounded-full border border-border px-3 py-1 text-xs font-medium text-ink hover:border-forest hover:text-forest-dark"
                      >
                        {r.is_plusklas ? "Toegang uitzetten" : "Toegang aanzetten"}
                      </button>
                    </form>
                  </div>
                </div>
              </li>
            );
          })}
          {!gezinnen.length && (
            <li className="text-sm text-ink-dim">Er heeft zich nog niemand geregistreerd.</li>
          )}
        </ul>
      </main>
    </>
  );
}
