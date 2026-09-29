import Link from "next/link";
import { Header } from "@/components/Header";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { plaatsBericht, wisBericht, zetBerichtActief } from "./actions";

export const metadata = { title: "Berichten — Oefenplatform Connectopia" };

type Rij = {
  id: string;
  titel: string;
  tekst: string;
  link: string | null;
  linktekst: string | null;
  actief: boolean;
  aangemaakt_op: string;
};

function datum(waarde: string) {
  return new Date(waarde).toLocaleDateString("nl-BE", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
}

export default async function BeheerBerichtenPage() {
  const session = await requireBeheerder();
  const supabase = await createClient();

  const { data, error } = await supabase
    .from("berichten")
    .select("id, titel, tekst, link, linktekst, actief, aangemaakt_op")
    .order("aangemaakt_op", { ascending: false });

  const rijen = (data ?? []) as Rij[];
  const staatAan = rijen.find((r) => r.actief);

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          Berichten
        </h1>
        <p className="mt-2 text-sm text-ink-dim">
          Wat je hier schrijft, staat bovenaan het platform bij elke ouder die
          inlogt. Er vertrekt geen mail: het bericht wacht op hen in het
          platform zelf, net zoals jouw antwoord op een ingestuurd weetje bij
          het kind uitkomt.
        </p>
        <p className="mt-2 text-sm text-ink-dim">
          Er staat er altijd maar één tegelijk: het nieuwste dat aan staat. Zet
          je een bericht uit, dan is het meteen bij iedereen weg. Een ouder kan
          het ook zelf wegklikken.
        </p>

        {error && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            De berichten konden niet geladen worden: {error.message}. Heb je{" "}
            <code>supabase/berichten.sql</code> al één keer uitgevoerd?
          </p>
        )}

        <form
          action={plaatsBericht}
          className="mt-8 space-y-4 rounded-xl border border-border bg-surface p-5"
        >
          <h2 className="font-display text-lg font-semibold text-ink">
            Een nieuw bericht
          </h2>

          <div>
            <label
              htmlFor="titel"
              className="block text-sm font-medium text-ink"
            >
              Titel
            </label>
            <input
              id="titel"
              name="titel"
              required
              maxLength={120}
              placeholder="Er is een nieuw onderdeel bij"
              className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink"
            />
          </div>

          <div>
            <label
              htmlFor="tekst"
              className="block text-sm font-medium text-ink"
            >
              Bericht
            </label>
            <textarea
              id="tekst"
              name="tekst"
              required
              rows={5}
              maxLength={2000}
              placeholder="Bij elk hoofdstuk van 🌱 Start staat nu een tocht met haltes, met een puzzel op het einde."
              className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink"
            />
            <p className="mt-1 text-xs text-ink-dim">
              Enters blijven staan, dus je mag gerust in alinea&apos;s
              schrijven.
            </p>
          </div>

          <div className="grid gap-4 sm:grid-cols-2">
            <div>
              <label
                htmlFor="link"
                className="block text-sm font-medium text-ink"
              >
                Link (mag leeg blijven)
              </label>
              <input
                id="link"
                name="link"
                maxLength={300}
                placeholder="/niveaus/start"
                className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink"
              />
            </div>
            <div>
              <label
                htmlFor="linktekst"
                className="block text-sm font-medium text-ink"
              >
                Tekst op de knop
              </label>
              <input
                id="linktekst"
                name="linktekst"
                maxLength={60}
                placeholder="Bekijken"
                className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink"
              />
            </div>
          </div>

          <button
            type="submit"
            className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
          >
            Bericht plaatsen
          </button>
          {staatAan && (
            <p className="text-xs text-ink-dim">
              Let op: &ldquo;{staatAan.titel}&rdquo; staat nu aan. Een nieuw
              bericht komt daarvoor in de plaats.
            </p>
          )}
        </form>

        <h2 className="mt-10 font-display text-lg font-semibold text-ink">
          Wat je al schreef
        </h2>
        <ul className="mt-3 space-y-3">
          {rijen.map((b) => (
            <li
              key={b.id}
              className="rounded-lg border border-border bg-surface p-4"
            >
              <div className="flex items-start justify-between gap-3">
                <div className="min-w-0">
                  <p className="text-xs uppercase tracking-wide text-ink-dim">
                    {datum(b.aangemaakt_op)} &middot;{" "}
                    {b.actief ? "staat aan" : "staat uit"}
                  </p>
                  <p className="font-medium text-ink">{b.titel}</p>
                  <p className="mt-1 whitespace-pre-line text-sm text-ink-dim">
                    {b.tekst}
                  </p>
                  {b.link && (
                    <p className="mt-1 truncate text-xs text-ink-dim">
                      Knop: {b.linktekst || "Bekijken"} &rarr; {b.link}
                    </p>
                  )}
                </div>
                <div className="flex shrink-0 flex-col items-end gap-2">
                  <form action={zetBerichtActief}>
                    <input type="hidden" name="id" value={b.id} />
                    <input
                      type="hidden"
                      name="naar"
                      value={b.actief ? "false" : "true"}
                    />
                    <button
                      type="submit"
                      className="text-sm text-forest-dark hover:underline"
                    >
                      {b.actief ? "Uitzetten" : "Aanzetten"}
                    </button>
                  </form>
                  <form action={wisBericht}>
                    <input type="hidden" name="id" value={b.id} />
                    <button
                      type="submit"
                      className="text-sm text-danger hover:underline"
                    >
                      Verwijderen
                    </button>
                  </form>
                </div>
              </div>
            </li>
          ))}
          {rijen.length === 0 && !error && (
            <li className="text-sm text-ink-dim">
              Je schreef nog geen bericht.
            </li>
          )}
        </ul>
      </main>
    </>
  );
}
