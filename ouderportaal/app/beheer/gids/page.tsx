import { requireBeheerder } from "@/lib/auth";
import { createAdminClient, tabelOntbreekt } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import {
  bewaarAanmelding,
  markeerGezien,
  verwijderAanmelding,
  zetZichtbaar,
} from "./actions";

/* De aanmeldingen komen binnen terwijl je kijkt, dus niets bewaren. */
export const dynamic = "force-dynamic";

type Aanmelding = {
  id: string;
  naam: string;
  omschrijving: string;
  regio: string | null;
  link: string | null;
  wie: string;
  zichtbaar: boolean;
  gezien: boolean;
  volledige_naam: string | null;
  contact: string | null;
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

const veld =
  "mt-1 block w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink";

export default async function GidsBeheer({
  searchParams,
}: {
  searchParams: Promise<{ fout?: string; succes?: string }>;
}) {
  const session = await requireBeheerder();
  const { fout, succes } = await searchParams;
  const naam = session.profile?.full_name ?? session.email ?? "";

  const db = createAdminClient();
  const { data, error } = await db
    .from("gids_aanmeldingen")
    .select(
      "id, naam, omschrijving, regio, link, wie, zichtbaar, gezien, volledige_naam, contact, created_at",
    )
    .order("created_at", { ascending: false })
    .limit(200);

  const leesfout = error
    ? tabelOntbreekt(error, "voor de gids", "website/supabase/gids.sql") ??
      `De aanmeldingen konden niet gelezen worden: ${error.message}`
    : null;

  const lijst = (data ?? []) as Aanmelding[];
  const nieuw = lijst.filter((a) => !a.gezien).length;
  const wachtend = lijst.filter((a) => !a.zichtbaar).length;

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
          Gids &ldquo;Waar kan je terecht&rdquo;
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {lijst.length} aanmelding{lijst.length === 1 ? "" : "en"}
          {nieuw > 0 ? ` · ${nieuw} nieuw` : ""}
          {wachtend > 0 ? ` · ${wachtend} wacht op jou` : ""}
        </p>
        <p className="mt-2 max-w-2xl text-sm text-ink-dim">
          Dit zijn de organisaties die iemand aanbracht via het formulier op
          www.connectopia.one/waar-kan-je-terecht. Pas de omschrijving gerust
          aan zodat ze even lang is als de andere, en zet ze dan in de gids. Ze
          komt alfabetisch bij de partners te staan.
        </p>

        {leesfout && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            {leesfout}
          </p>
        )}
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
          <form action={markeerGezien} className="mt-6">
            <button
              type="submit"
              className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
            >
              Alles als gezien markeren
            </button>
          </form>
        )}

        <ul className="mt-6 space-y-3">
          {lijst.map((a) => (
            <li
              key={a.id}
              className={`rounded-lg border bg-surface p-4 ${
                a.gezien ? "border-border" : "border-forest"
              }`}
            >
              <div className="flex flex-wrap items-center gap-2 text-xs text-ink-dim">
                <span>{tijdstip(a.created_at)}</span>
                {!a.gezien && (
                  <span className="font-semibold text-forest-dark">nieuw</span>
                )}
                {a.zichtbaar ? (
                  <span className="font-semibold text-forest-dark">
                    staat in de gids
                  </span>
                ) : (
                  <span className="font-semibold text-danger">
                    nog niet in de gids
                  </span>
                )}
              </div>

              <p className="mt-2 text-sm text-ink-dim">
                {a.wie === "zelf"
                  ? "Meldde zichzelf aan"
                  : "Aangebracht door iemand anders"}
                {a.volledige_naam ? `: ${a.volledige_naam}` : ""}
                {a.contact ? ` · ${a.contact}` : ""}
              </p>

              <form action={bewaarAanmelding} className="mt-3 grid gap-3">
                <input type="hidden" name="id" value={a.id} />
                <label className="block text-sm font-medium text-ink">
                  Naam
                  <input
                    name="naam"
                    defaultValue={a.naam}
                    maxLength={120}
                    required
                    className={veld}
                  />
                </label>
                <label className="block text-sm font-medium text-ink">
                  Omschrijving ({a.omschrijving.length} tekens; de andere
                  kaartjes zitten rond 130 tot 155)
                  <textarea
                    name="omschrijving"
                    defaultValue={a.omschrijving}
                    rows={3}
                    maxLength={400}
                    required
                    className={veld}
                  />
                </label>
                <div className="grid gap-3 sm:grid-cols-2">
                  <label className="block text-sm font-medium text-ink">
                    Regio
                    <input
                      name="regio"
                      defaultValue={a.regio ?? ""}
                      maxLength={80}
                      className={veld}
                    />
                  </label>
                  <label className="block text-sm font-medium text-ink">
                    Website
                    <input
                      name="link"
                      defaultValue={a.link ?? ""}
                      maxLength={400}
                      className={veld}
                    />
                  </label>
                </div>
                <div>
                  <button
                    type="submit"
                    className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
                  >
                    Aanpassing bewaren
                  </button>
                </div>
              </form>

              {a.link && (
                <a
                  href={a.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="mt-2 inline-block break-all text-sm text-forest-dark underline"
                >
                  Hun website bekijken
                </a>
              )}

              <div className="mt-3 flex flex-wrap gap-2">
                <form action={zetZichtbaar}>
                  <input type="hidden" name="id" value={a.id} />
                  <input
                    type="hidden"
                    name="zichtbaar"
                    value={a.zichtbaar ? "nee" : "ja"}
                  />
                  <button
                    type="submit"
                    className={
                      a.zichtbaar
                        ? "rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
                        : "rounded-md bg-forest px-3 py-1.5 text-sm font-medium text-white hover:bg-forest-dark"
                    }
                  >
                    {a.zichtbaar ? "Uit de gids halen" : "In de gids zetten"}
                  </button>
                </form>

                {!a.gezien && (
                  <form action={markeerGezien}>
                    <input type="hidden" name="id" value={a.id} />
                    <button
                      type="submit"
                      className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
                    >
                      Gezien
                    </button>
                  </form>
                )}

                <form action={verwijderAanmelding}>
                  <input type="hidden" name="id" value={a.id} />
                  <button
                    type="submit"
                    className="rounded-md border border-danger/40 px-3 py-1.5 text-sm text-danger hover:bg-danger/10"
                  >
                    Verwijderen
                  </button>
                </form>
              </div>
            </li>
          ))}

          {lijst.length === 0 && !leesfout && (
            <li className="text-sm text-ink-dim">
              Er heeft nog niemand een organisatie aangebracht.
            </li>
          )}
        </ul>
      </main>
    </>
  );
}
