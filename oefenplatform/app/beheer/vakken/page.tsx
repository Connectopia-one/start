import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import {
  maakVak,
  hernoemVak,
  verwijderVak,
  maakHoofdstuk,
  hernoemHoofdstuk,
  wisselGratis,
  zetNiveauGratis,
  verwijderHoofdstuk,
  wisselRekenmachine,
  bulkImportVakInhoud,
} from "../actions";
import { NIVEAUS, vindNiveau } from "@/lib/niveaus";
import { sorteerHoofdstukken } from "@/lib/hoofdstukvolgorde";

/*
  Beheer → Vakken, in drie stappen.

  Kim op 29 september 2026: "omdat de vakken in het beheer nu al vrij veel zijn
  is dat best onoverzichtelijk ... nu moet ik heel lang scrollen eer ik bij het
  juiste vak zit en dan moet ik zoeken of het spark of start is en er komen nog
  2 graden bij."

  Daarom staat er niet langer alles onder elkaar, maar kies je eerst een
  categorie, dan een vak, en pas dan zie je de hoofdstukken — dezelfde twee
  lagen die de kinderen op /niveaus al hebben. Waar je staat zit in het
  webadres (?niveau=…&vak=…), zodat elke knop je na het bewaren terugzet waar
  je was; elk formulier stuurt dat mee in "terug_niveau" en "terug_vak". Zie
  vakkenPagina() in ../actions.ts.
*/

type Hoofdstuk = {
  id: string;
  titel: string;
  volgnummer: number;
  gratis: boolean;
  niveau: string;
};
type Vak = {
  id: string;
  naam: string;
  slug: string;
  rekenmachine: boolean;
  hoofdstukken: Hoofdstuk[];
};

const VOORBEELD_VAK_JSON = `{
  "hoofdstukken": [
    {
      "titel": "Probleemoplossend denken",
      "niveau": "spark",
      "gratis": false,
      "vragen": [
        {
          "type": "meerkeuze",
          "vraag": "Hoeveel is 7 x 8?",
          "opties": ["54", "56", "58"],
          "antwoord": 1,
          "uitleg": "7 x 8 = 56"
        },
        {
          "type": "waarofniet",
          "vraag": "Een vierkant heeft 4 gelijke zijden.",
          "antwoord": true
        }
      ]
    },
    {
      "titel": "Getallenleer",
      "niveau": "spark",
      "vragen": [
        {
          "type": "invultekst",
          "vraag": "3/4 als procent is ___.",
          "antwoord": "75%"
        }
      ]
    }
  ]
}`;

const veldKlasse =
  "min-w-0 flex-1 rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest";
const bewaarKlasse =
  "shrink-0 rounded-md border border-forest px-3 py-2 text-sm font-medium text-forest-dark hover:bg-forest hover:text-white";

/** "3 hoofdstukken" of "1 hoofdstuk". */
function telWoord(aantal: number, enkel: string, meer: string) {
  return `${aantal} ${aantal === 1 ? enkel : meer}`;
}

export default async function BeheerVakkenPage({
  searchParams,
}: {
  searchParams: Promise<{
    fout?: string;
    melding?: string;
    niveau?: string;
    vak?: string;
  }>;
}) {
  const session = await requireBeheerder();
  const {
    fout,
    melding,
    niveau: niveauParam,
    vak: vakParam,
  } = await searchParams;
  const supabase = await createClient();

  const { data } = await supabase
    .from("vakken")
    .select(
      "id, naam, slug, rekenmachine, hoofdstukken(id, titel, volgnummer, gratis, niveau)",
    )
    .order("volgorde", { ascending: true });

  const vakken = (data as Vak[] | null) ?? [];
  const niveau = niveauParam ? vindNiveau(niveauParam) : undefined;
  const vak =
    niveau && vakParam ? vakken.find((v) => v.slug === vakParam) : undefined;

  // De verborgen velden die elke knop meestuurt, zodat je na het bewaren weer
  // op deze pagina staat en niet helemaal vooraan.
  const terug = (
    <>
      {niveau && (
        <input type="hidden" name="terug_niveau" value={niveau.slug} />
      )}
      {vak && <input type="hidden" name="terug_vak" value={vak.slug} />}
    </>
  );

  const hoofdstukkenHier = vak
    ? sorteerHoofdstukken(
        vak.hoofdstukken.filter((h) => h.niveau === niveau!.slug),
      )
    : [];
  const gratisHier = hoofdstukkenHier.filter((h) => h.gratis).length;
  const allesGratis =
    hoofdstukkenHier.length > 0 && gratisHier === hoofdstukkenHier.length;

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        {/* Het kruimelpad: één stap terug, nooit meer. */}
        {!niveau && (
          <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
            &larr; Beheer
          </Link>
        )}
        {niveau && !vak && (
          <Link
            href="/beheer/vakken"
            className="text-sm text-ink-dim hover:text-ink"
          >
            &larr; Alle categorie&euml;n
          </Link>
        )}
        {niveau && vak && (
          <Link
            href={`/beheer/vakken?niveau=${niveau.slug}`}
            className="text-sm text-ink-dim hover:text-ink"
          >
            &larr; {niveau.emoji} {niveau.naam}
          </Link>
        )}

        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          {vak
            ? `${niveau!.emoji} ${niveau!.naam} — ${vak.naam}`
            : niveau
              ? `${niveau.emoji} ${niveau.naam}`
              : "Vakken & hoofdstukken"}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {vak
            ? telWoord(hoofdstukkenHier.length, "hoofdstuk", "hoofdstukken") +
              (hoofdstukkenHier.length
                ? `, waarvan er ${gratisHier} gratis ${gratisHier === 1 ? "staat" : "staan"}.`
                : " in deze categorie.")
            : niveau
              ? "Kies het vak dat je wil bijwerken."
              : "Kies eerst een categorie, dan een vak. Zo hoef je niet door alles te scrollen."}
        </p>

        {fout && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            {fout}
          </p>
        )}

        {melding && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">
            {melding}
          </p>
        )}

        {/* ------------------------------------------------ stap 1: categorie */}
        {!niveau && (
          <ul className="mt-6 grid gap-3 sm:grid-cols-2">
            {NIVEAUS.map((n) => {
              const vakkenHier = vakken.filter((v) =>
                v.hoofdstukken.some((h) => h.niveau === n.slug),
              );
              const aantalHoofdstukken = vakken.reduce(
                (som, v) =>
                  som +
                  v.hoofdstukken.filter((h) => h.niveau === n.slug).length,
                0,
              );
              return (
                <li key={n.slug}>
                  <Link
                    href={`/beheer/vakken?niveau=${n.slug}`}
                    className="block h-full rounded-xl border border-border bg-surface px-4 py-4 hover:border-forest hover:bg-forest/5"
                  >
                    <p className="font-display text-base font-semibold text-ink">
                      {n.emoji} {n.naam}
                    </p>
                    <p className="mt-0.5 text-xs text-ink-dim">
                      {n.omschrijving}
                    </p>
                    <p className="mt-2 text-xs text-ink-dim">
                      {aantalHoofdstukken === 0
                        ? "Nog geen hoofdstukken"
                        : `${telWoord(vakkenHier.length, "vak", "vakken")} · ${telWoord(
                            aantalHoofdstukken,
                            "hoofdstuk",
                            "hoofdstukken",
                          )}`}
                    </p>
                  </Link>
                </li>
              );
            })}
          </ul>
        )}

        {/* ----------------------------------------------------- stap 2: vak */}
        {niveau && !vak && (
          <>
            {(() => {
              const metInhoud = vakken.filter((v) =>
                v.hoofdstukken.some((h) => h.niveau === niveau.slug),
              );
              const zonderInhoud = vakken.filter(
                (v) => !v.hoofdstukken.some((h) => h.niveau === niveau.slug),
              );
              return (
                <>
                  {metInhoud.length === 0 && (
                    <p className="mt-6 rounded-lg border border-border bg-surface px-4 py-4 text-sm text-ink-dim">
                      In deze categorie staat nog geen enkel hoofdstuk. Kies
                      hieronder een vak om er het eerste aan te maken of vragen
                      te importeren.
                    </p>
                  )}

                  {metInhoud.length > 0 && (
                    <ul className="mt-6 grid gap-3 sm:grid-cols-2">
                      {metInhoud.map((v) => {
                        const hier = v.hoofdstukken.filter(
                          (h) => h.niveau === niveau.slug,
                        );
                        const gratis = hier.filter((h) => h.gratis).length;
                        return (
                          <li key={v.id}>
                            <Link
                              href={`/beheer/vakken?niveau=${niveau.slug}&vak=${v.slug}`}
                              className="block h-full rounded-xl border border-border bg-surface px-4 py-4 hover:border-forest hover:bg-forest/5"
                            >
                              <p className="font-display text-base font-semibold text-ink">
                                {v.naam}
                              </p>
                              <p className="mt-1 text-xs text-ink-dim">
                                {telWoord(
                                  hier.length,
                                  "hoofdstuk",
                                  "hoofdstukken",
                                )}{" "}
                                · {gratis} gratis
                              </p>
                            </Link>
                          </li>
                        );
                      })}
                    </ul>
                  )}

                  {zonderInhoud.length > 0 && (
                    <details className="mt-6 rounded-lg border border-border">
                      <summary className="cursor-pointer px-3 py-2 text-sm text-ink-dim hover:text-ink">
                        Vakken zonder hoofdstukken in deze categorie (
                        {zonderInhoud.length})
                      </summary>
                      <ul className="flex flex-wrap gap-2 border-t border-border p-3">
                        {zonderInhoud.map((v) => (
                          <li key={v.id}>
                            <Link
                              href={`/beheer/vakken?niveau=${niveau.slug}&vak=${v.slug}`}
                              className="inline-block rounded-full border border-border px-3 py-1 text-sm text-forest-dark hover:border-forest hover:bg-forest/5"
                            >
                              {v.naam}
                            </Link>
                          </li>
                        ))}
                      </ul>
                    </details>
                  )}
                </>
              );
            })()}

            {/* Een nieuw vak maak je hier, bij de vakken zelf. Het stond eerst
                een stap hoger, bij de categorieën, en daar zocht Kim het
                tevergeefs. Een vak hoort trouwens niet bij één categorie: je
                geeft het daarna in elke categorie zijn eigen hoofdstukken. */}
            <details className="mt-6 rounded-lg border border-border">
              <summary className="cursor-pointer px-3 py-2 text-sm font-medium text-ink">
                Een vak toevoegen
              </summary>
              <div className="border-t border-border p-3">
                <form
                  action={maakVak}
                  className="flex flex-wrap items-center gap-2"
                >
                  {terug}
                  <input
                    name="naam"
                    required
                    placeholder="Naam nieuw vak (bv. Duits)"
                    className={veldKlasse}
                  />
                  <label className="flex items-center gap-1.5 text-xs text-ink-dim">
                    <input
                      type="checkbox"
                      name="rekenmachine"
                      className="accent-forest"
                    />
                    Rekenmachine (GeoGebra)
                  </label>
                  <button
                    type="submit"
                    className="shrink-0 rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
                  >
                    Vak toevoegen
                  </button>
                </form>
                <p className="mt-2 text-xs text-ink-dim">
                  Een vak staat los van de categorie&euml;n: hetzelfde vak kan
                  hoofdstukken hebben in {niveau.emoji} {niveau.naam} én in de
                  andere. Na het toevoegen sta je meteen bij de hoofdstukken van
                  je nieuwe vak in {niveau.naam}.
                </p>
              </div>
            </details>
          </>
        )}

        {/* ---------------------------------------------- stap 3: hoofdstukken */}
        {niveau && vak && (
          <>
            {/* Een heel niveau in één keer open of op slot. Veertien
                hoofdstukken los aanklikken is vragen om er één te vergeten. */}
            {hoofdstukkenHier.length > 0 && (
              <form
                action={zetNiveauGratis}
                className="mt-6 flex flex-wrap items-center gap-3 rounded-lg bg-paper px-3 py-3"
              >
                {terug}
                <input type="hidden" name="vak_id" value={vak.id} />
                <input type="hidden" name="niveau" value={niveau.slug} />
                <input
                  type="hidden"
                  name="gratis"
                  value={allesGratis ? "nee" : "ja"}
                />
                <span className="text-sm text-ink">
                  Heel {niveau.naam} van {vak.naam} in één keer
                </span>
                <button
                  type="submit"
                  className="ml-auto rounded-full border border-forest/40 bg-surface px-3 py-1 text-xs font-medium text-forest-dark hover:bg-forest hover:text-surface"
                >
                  {allesGratis ? "Alles op slot zetten" : "Alles gratis zetten"}
                </button>
              </form>
            )}

            <ul className="mt-4 space-y-2">
              {hoofdstukkenHier.map((h) => (
                <li
                  key={h.id}
                  className="rounded-lg border border-border bg-surface px-3 py-2 text-sm"
                >
                  <div className="flex items-center justify-between gap-3">
                    <Link
                      href={`/beheer/vakken/${vak.slug}/${h.volgnummer}`}
                      className="text-forest-dark hover:underline"
                    >
                      {h.titel}
                    </Link>
                    <div className="flex items-center gap-3">
                      <form action={wisselGratis}>
                        {terug}
                        <input type="hidden" name="id" value={h.id} />
                        <input
                          type="hidden"
                          name="gratis"
                          value={String(h.gratis)}
                        />
                        <button
                          type="submit"
                          className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${
                            h.gratis
                              ? "bg-forest/10 text-forest-dark"
                              : "bg-ink-dim/10 text-ink-dim"
                          }`}
                        >
                          {h.gratis ? "Gratis" : "Op slot"}
                        </button>
                      </form>
                      <form action={verwijderHoofdstuk}>
                        {terug}
                        <input type="hidden" name="id" value={h.id} />
                        <button
                          type="submit"
                          className="text-xs text-danger hover:underline"
                        >
                          Verwijderen
                        </button>
                      </form>
                    </div>
                  </div>
                  <details className="mt-2">
                    <summary className="cursor-pointer text-xs text-ink-dim hover:text-ink">
                      Titel aanpassen
                    </summary>
                    <form
                      action={hernoemHoofdstuk}
                      className="mt-2 flex flex-wrap items-center gap-2"
                    >
                      {terug}
                      <input type="hidden" name="id" value={h.id} />
                      <input
                        name="titel"
                        required
                        defaultValue={h.titel}
                        className={veldKlasse}
                      />
                      <button type="submit" className={bewaarKlasse}>
                        Bewaren
                      </button>
                      <p className="w-full text-xs text-ink-dim">
                        Het webadres blijft hetzelfde. Let op: een bulk-import
                        zoekt een hoofdstuk op zijn categorie en zijn titel, dus
                        importeer eerst en hernoem daarna.
                      </p>
                    </form>
                  </details>
                </li>
              ))}
            </ul>

            {hoofdstukkenHier.length === 0 && (
              <p className="mt-6 rounded-lg border border-border bg-surface px-4 py-4 text-sm text-ink-dim">
                {vak.naam} heeft nog geen hoofdstukken in {niveau.emoji}{" "}
                {niveau.naam}. Maak er hieronder een aan, of importeer een
                bestand.
              </p>
            )}

            <form
              action={maakHoofdstuk}
              className="mt-4 flex flex-wrap items-center gap-2"
            >
              {terug}
              <input type="hidden" name="vak_id" value={vak.id} />
              {/* De categorie ligt vast: je staat er nu in. Wil je er een in een
                  andere categorie, klik dan eerst naar die categorie. */}
              <input type="hidden" name="niveau" value={niveau.slug} />
              <input
                name="titel"
                required
                placeholder={`Titel nieuw hoofdstuk in ${niveau.naam}`}
                className={veldKlasse}
              />
              <label className="flex items-center gap-1.5 text-xs text-ink-dim">
                <input
                  type="checkbox"
                  name="gratis"
                  className="accent-forest"
                />
                Gratis
              </label>
              <button
                type="submit"
                className="shrink-0 rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
              >
                Toevoegen
              </button>
            </form>

            <details className="mt-6 rounded-lg border border-border">
              <summary className="cursor-pointer px-3 py-2 text-sm font-medium text-ink">
                Vragen importeren (JSON)
              </summary>
              <div className="border-t border-border p-3">
                <p className="text-sm text-ink-dim">
                  Plak hier de vragen voor één of meerdere hoofdstukken van{" "}
                  {vak.naam}. Een hoofdstuk met een titel die in die categorie
                  al bestaat krijgt de vragen erbij; een nieuwe titel wordt
                  aangemaakt. De categorie komt uit het veld <code>niveau</code>{" "}
                  in het bestand zelf, dus je kan hiermee ook een ander niveau
                  dan {niveau.naam} inlezen.
                </p>
                <pre className="mt-3 overflow-x-auto rounded-md bg-paper p-3 text-xs text-ink-dim">
                  {VOORBEELD_VAK_JSON}
                </pre>
                <form action={bulkImportVakInhoud} className="mt-3 space-y-3">
                  {terug}
                  <input type="hidden" name="vak_id" value={vak.id} />
                  <textarea
                    name="json"
                    required
                    rows={8}
                    placeholder={VOORBEELD_VAK_JSON}
                    className="w-full rounded-md border border-border bg-paper px-3 py-2 font-mono text-xs outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                  />
                  <label className="flex items-start gap-2 rounded-md border border-border bg-paper px-3 py-2 text-xs text-ink">
                    <input
                      type="checkbox"
                      name="vervang"
                      className="mt-0.5 accent-forest"
                    />
                    <span>
                      <span className="font-medium">
                        Bestaande vragen vervangen
                      </span>{" "}
                      — is een hoofdstuk verouderd, vink dit dan aan: de oude
                      vragen gaan weg en enkel die uit dit bestand blijven over.
                      Het hoofdstuk houdt zijn plek, zijn webadres en zijn
                      leerbundel, dus je hoeft het niet te verwijderen. Wat
                      kinderen al maakten blijft meetellen in hun voortgang;
                      enkel welk vraagje het precies was, is daarna niet meer na
                      te lezen. Laat je dit uit staan, dan komen de vragen er
                      gewoon bij.
                    </span>
                  </label>
                  <button
                    type="submit"
                    className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark"
                  >
                    Importeren
                  </button>
                </form>
              </div>
            </details>

            <details className="mt-4 rounded-lg border border-border">
              <summary className="cursor-pointer px-3 py-2 text-sm font-medium text-ink">
                Instellingen van {vak.naam}
              </summary>
              <div className="space-y-4 border-t border-border p-3">
                <form
                  action={hernoemVak}
                  className="flex flex-wrap items-center gap-2"
                >
                  {terug}
                  <input type="hidden" name="id" value={vak.id} />
                  <input
                    name="naam"
                    required
                    defaultValue={vak.naam}
                    className={veldKlasse}
                  />
                  <button type="submit" className={bewaarKlasse}>
                    Bewaren
                  </button>
                  <p className="w-full text-xs text-ink-dim">
                    Het webadres van dit vak is nu{" "}
                    <code>/vakken/{vak.slug}</code>. Dat past mee aan met de
                    naam, zolang je het niet zelf anders gezet hebt.
                  </p>
                </form>

                <div className="flex flex-wrap items-center gap-3">
                  <form action={wisselRekenmachine}>
                    {terug}
                    <input type="hidden" name="id" value={vak.id} />
                    <input
                      type="hidden"
                      name="rekenmachine"
                      value={String(vak.rekenmachine)}
                    />
                    <button
                      type="submit"
                      className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${
                        vak.rekenmachine
                          ? "bg-forest/10 text-forest-dark"
                          : "bg-ink-dim/10 text-ink-dim"
                      }`}
                    >
                      {vak.rekenmachine
                        ? "Rekenmachine aan"
                        : "Rekenmachine uit"}
                    </button>
                  </form>
                  <form action={verwijderVak} className="ml-auto">
                    {terug}
                    <input type="hidden" name="id" value={vak.id} />
                    <button
                      type="submit"
                      className="text-xs text-danger hover:underline"
                    >
                      Vak verwijderen
                    </button>
                  </form>
                </div>
                <p className="text-xs text-ink-dim">
                  Een vak verwijderen neemt àl zijn hoofdstukken mee, ook die
                  van de andere categorie&euml;n.
                </p>
              </div>
            </details>
          </>
        )}
      </main>
    </>
  );
}
