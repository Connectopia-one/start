import Link from "next/link";
import { notFound } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import { FicheRegels } from "@/components/FicheRegels";
import { Aanwezigheid, AanwezigheidStand } from "@/components/Aanwezigheid";
import { Kopieer } from "../../aanvragen/Kopieer";
import { KINDVELDEN, samen, type Kind } from "@/lib/kind";
import {
  ACTIVITEITVELDEN,
  datumTekst,
  euro,
  factuurLabel,
  leeftijd,
  type Activiteit,
} from "@/lib/activiteiten";
import { SOORTEN } from "@/lib/activiteiten";
import {
  alleAanwezig,
  bewaarNotitie,
  haalKindWeg,
  herhaalActiviteit,
  pasActiviteitAan,
  voegKindToe,
} from "../actions";

export const dynamic = "force-dynamic";

type Gezin = { id: string; full_name: string | null; telefoon: string | null };
type KindRij = Kind & { profile_id: string };
type Deelname = {
  kind_id: string;
  notitie: string | null;
  aanwezig: boolean | null;
};

/*
  De lijst van één kamp, les of werking.

  Dit is het blad dat Kim meeneemt: wie komt er, hoe oud is dat kind, wie is de
  ouder en op welk nummer bereik je die, en wat staat er op de fiche dat die
  dag telt. De fiche zelf staat eronder met FicheRegels, hetzelfde component
  als op het gezinsscherm, zodat allebei dezelfde dingen tonen.
*/
export default async function ActiviteitLijst({
  params,
  searchParams,
}: {
  params: Promise<{ id: string }>;
  searchParams: Promise<{ fout?: string; succes?: string }>;
}) {
  const { id } = await params;
  const { fout, succes } = await searchParams;
  const session = await requireBeheerder();
  const naam = session.profile?.full_name ?? session.email ?? "";

  const db = createAdminClient();
  const [{ data: activiteit }, { data: deelnamesData }, { data: kinderenData }] =
    await Promise.all([
      db
        .from("activiteiten")
        .select(ACTIVITEITVELDEN)
        .eq("id", id)
        .maybeSingle(),
      db
        .from("deelnames")
        .select("kind_id, notitie, aanwezig")
        .eq("activiteit_id", id),
      db.from("kinderen").select(`${KINDVELDEN}, profile_id`).order("naam"),
    ]);

  if (!activiteit) notFound();
  const kamp = activiteit as Activiteit;

  const deelnames = (deelnamesData ?? []) as Deelname[];
  const alleKinderen = (kinderenData ?? []) as unknown as KindRij[];
  const deelnameVan = new Map(deelnames.map((d) => [d.kind_id, d]));

  const { data: gezinnenData } = await db
    .from("profiles")
    .select("id, full_name, telefoon");
  const gezinnen = new Map(
    ((gezinnenData ?? []) as Gezin[]).map((g) => [g.id, g]),
  );

  const opDeLijst = alleKinderen
    .filter((kind) => deelnameVan.has(kind.id))
    .sort((a, b) => a.naam.localeCompare(b.naam, "nl"));
  const rest = alleKinderen.filter((kind) => !deelnameVan.has(kind.id));

  const aanwezigen = deelnames.filter((d) => d.aanwezig !== false).length;
  const nietAangeduid = deelnames.filter((d) => d.aanwezig === null).length;

  /* De lijst als tabel met tabs ertussen, om in een rekenblad te plakken. */
  const tabel = [
    [
      "Kind",
      "Aanwezig",
      "Leeftijd",
      "Gezin",
      "Telefoon",
      "Allergieën",
      "Medicatie",
      "Ophalen",
    ].join("\t"),
    ...opDeLijst.map((kind) =>
      [
        kind.naam,
        deelnameVan.get(kind.id)?.aanwezig === false
          ? "afwezig"
          : deelnameVan.get(kind.id)?.aanwezig === true
            ? "aanwezig"
            : "",
        leeftijd(kind.geboortedatum) ?? "",
        gezinnen.get(kind.profile_id)?.full_name ?? "",
        gezinnen.get(kind.profile_id)?.telefoon ?? "",
        kind.allergieen ?? "",
        kind.medicatie ?? "",
        kind.ophalen ?? "",
      ]
        .map((v) => String(v).replace(/\s+/g, " "))
        .join("\t"),
    ),
  ].join("\n");

  const wanneer = datumTekst(kamp.datum);

  return (
    <>
      <Header
        naam={naam}
        rol="beheerder"
        terugHref="/beheer/activiteiten"
        terugLabel="Kampen en lessen"
      />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">
          {kamp.naam}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {kamp.soort}
          {wanneer && ` · ${wanneer}`}
          {kamp.plaats && ` · ${kamp.plaats}`}
          {` · ${opDeLijst.length} ${opDeLijst.length === 1 ? "kind" : "kinderen"}`}
        </p>
        <p className="mt-0.5 text-sm text-ink-dim">
          Op de factuur: {factuurLabel(kamp)}
          {kamp.prijs === null
            ? " · geen prijs ingevuld"
            : ` · ${euro(Number(kamp.prijs))} per kind`}
          {opDeLijst.length > 0 && " · "}
          {opDeLijst.length > 0 && (
            <AanwezigheidStand
              aanwezigen={aanwezigen}
              nietAangeduid={nietAangeduid}
            />
          )}
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

        {/* Een kind erbij zetten kan ook hier, niet enkel op het gezinsscherm.
            Handig als je de lijst voor je hebt en er nog iemand bij komt. */}
        {rest.length > 0 && (
          <form
            action={voegKindToe}
            className="mt-6 flex flex-wrap items-end gap-2 print:hidden"
          >
            <input type="hidden" name="activiteit_id" value={kamp.id} />
            <label className="min-w-[14rem] flex-1">
              <span className="text-sm font-medium text-ink">
                Een kind erbij zetten
              </span>
              <select
                name="kind_id"
                defaultValue=""
                className="mt-1 w-full rounded-md border border-border bg-surface px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              >
                <option value="">Kies een kind</option>
                {rest.map((kind) => (
                  <option key={kind.id} value={kind.id}>
                    {kind.naam}
                    {gezinnen.get(kind.profile_id)?.full_name
                      ? ` — ${gezinnen.get(kind.profile_id)?.full_name}`
                      : ""}
                  </option>
                ))}
              </select>
            </label>
            <button
              type="submit"
              className="rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Toevoegen
            </button>
          </form>
        )}

        {opDeLijst.length > 0 && (
          <div className="mt-5 print:hidden">
            <Kopieer
              waarde={tabel}
              wat={`de lijst van ${kamp.naam}`}
              label="Kopieer de lijst"
              stijl="vol"
            />
            <p className="mt-1.5 text-xs text-ink-dim">
              Plak je dit in een rekenblad, dan komt elke kolom apart te staan.
              Op papier zetten doe je met ctrl+p; de knoppen gaan niet mee.
            </p>
          </div>
        )}

        {opDeLijst.length === 0 && (
          <p className="mt-6 text-sm text-ink-dim">
            Er staat nog geen kind op deze lijst. Kies er hierboven een, of duid
            het aan bij het gezin zelf.
          </p>
        )}

        {nietAangeduid > 0 && (
          <form action={alleAanwezig} className="mt-5 print:hidden">
            <input type="hidden" name="activiteit_id" value={kamp.id} />
            <button
              type="submit"
              className="rounded-md border border-forest px-3 py-1.5 text-sm font-medium text-forest-dark hover:bg-forest/10"
            >
              Iedereen op aanwezig zetten
            </button>
            <p className="mt-1.5 text-xs text-ink-dim">
              Daarna vink je enkel nog af wie er niet was. Wat niet aangeduid
              is, telt op de factuur mee als aanwezig.
            </p>
          </form>
        )}

        <ul className="mt-5 space-y-3">
          {opDeLijst.map((kind) => {
            const gezin = gezinnen.get(kind.profile_id);
            const jaar = leeftijd(kind.geboortedatum);
            const deelname = deelnameVan.get(kind.id);
            const notitie = deelname?.notitie ?? "";
            const leeg =
              !kind.allergieen && !kind.medicatie && !kind.noodcontact_telefoon;
            return (
              <li
                key={kind.id}
                className="rounded-lg border border-border bg-surface p-4 text-sm print:break-inside-avoid"
              >
                <div className="flex flex-wrap items-start justify-between gap-2">
                  <div>
                    <p className="font-display font-semibold text-ink">
                      {kind.naam}
                      {jaar !== null && (
                        <span className="ml-2 font-sans text-xs font-normal text-ink-dim">
                          {jaar} jaar
                        </span>
                      )}
                    </p>
                    <p className="mt-0.5 text-xs text-ink-dim">
                      {samen(gezin?.full_name, gezin?.telefoon) ||
                        "gezin onbekend"}
                    </p>
                  </div>
                  <div className="flex flex-wrap items-center gap-2 print:hidden">
                    <Aanwezigheid
                      activiteitId={kamp.id}
                      kindId={kind.id}
                      waarde={deelname?.aanwezig ?? null}
                      terug={`/beheer/activiteiten/${kamp.id}`}
                    />
                    <Link
                      href={`/beheer/gezinnen/${kind.profile_id}`}
                      className="rounded-md border border-border px-3 py-1.5 text-sm text-ink hover:border-forest"
                    >
                      Naar het gezin
                    </Link>
                    <form action={haalKindWeg}>
                      <input
                        type="hidden"
                        name="activiteit_id"
                        value={kamp.id}
                      />
                      <input type="hidden" name="kind_id" value={kind.id} />
                      <button
                        type="submit"
                        className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-danger hover:text-danger"
                      >
                        Van de lijst
                      </button>
                    </form>
                  </div>
                </div>

                {deelname?.aanwezig === false && (
                  <p className="mt-1 text-xs font-medium text-danger">
                    Afwezig: telt niet mee op de factuur.
                  </p>
                )}

                {leeg ? (
                  <p className="mt-2 rounded-md bg-amber/10 px-3 py-2 text-xs text-ink">
                    De fiche van dit kind is nog niet ingevuld. Vraag de ouder
                    om ze aan te vullen op ouders.connectopia.one.
                  </p>
                ) : (
                  <div className="mt-2">
                    <FicheRegels kind={kind} />
                  </div>
                )}

                <div className="mt-2 flex flex-wrap gap-2">
                  <span
                    className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${
                      kind.toestemming_fotos
                        ? "bg-forest/10 text-forest-dark"
                        : "bg-danger/10 text-danger"
                    }`}
                  >
                    {kind.toestemming_fotos
                      ? "Foto's mogen"
                      : "Geen foto's"}
                  </span>
                  <span
                    className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${
                      kind.toestemming_social_media
                        ? "bg-forest/10 text-forest-dark"
                        : "bg-danger/10 text-danger"
                    }`}
                  >
                    {kind.toestemming_social_media
                      ? "Social media mag"
                      : "Niet op social media"}
                  </span>
                  {kind.alleen_naar_huis && (
                    <span className="rounded-full bg-amber/15 px-2.5 py-0.5 text-xs font-medium text-ink">
                      Mag alleen naar huis
                    </span>
                  )}
                </div>

                {/* Iets dat enkel voor deze dag geldt. */}
                <form
                  action={bewaarNotitie}
                  className="mt-3 flex flex-wrap items-end gap-2 print:hidden"
                >
                  <input type="hidden" name="activiteit_id" value={kamp.id} />
                  <input type="hidden" name="kind_id" value={kind.id} />
                  <label className="min-w-[12rem] flex-1">
                    <span className="text-xs text-ink-dim">
                      Notitie voor deze dag
                    </span>
                    <input
                      name="notitie"
                      defaultValue={notitie}
                      placeholder="komt pas om 10u"
                      className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-1.5 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                    />
                  </label>
                  <button
                    type="submit"
                    className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
                  >
                    Bewaren
                  </button>
                </form>
                {notitie && (
                  <p className="mt-1 hidden text-sm text-ink print:block">
                    <strong>Notitie: </strong>
                    {notitie}
                  </p>
                )}
              </li>
            );
          })}
        </ul>

        {/* Twee dingen die je maar af en toe nodig hebt, dus dichtgeklapt: ze
            horen niet in de weg te staan als je met de lijst in de zaal
            staat. */}
        <details className="mt-10 rounded-xl border border-border bg-surface p-5 print:hidden">
          <summary className="cursor-pointer font-display text-base font-semibold text-ink">
            Deze activiteit aanpassen
          </summary>
          <form
            action={pasActiviteitAan}
            className="mt-4 grid gap-3 sm:grid-cols-2"
          >
            <input type="hidden" name="id" value={kamp.id} />
            <label className="sm:col-span-2">
              <span className="text-sm font-medium text-ink">Naam</span>
              <input
                name="naam"
                defaultValue={kamp.naam}
                required
                className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </label>
            <label>
              <span className="text-sm font-medium text-ink">Soort</span>
              <select
                name="soort"
                defaultValue={kamp.soort}
                className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              >
                {[...new Set([kamp.soort, ...SOORTEN])].map((soort) => (
                  <option key={soort} value={soort}>
                    {soort}
                  </option>
                ))}
              </select>
            </label>
            <label>
              <span className="text-sm font-medium text-ink">Datum</span>
              <input
                type="date"
                name="datum"
                defaultValue={kamp.datum ?? ""}
                className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </label>
            <label className="sm:col-span-2">
              <span className="text-sm font-medium text-ink">Plaats</span>
              <input
                name="plaats"
                defaultValue={kamp.plaats ?? ""}
                className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </label>
            <label>
              <span className="text-sm font-medium text-ink">
                Op de factuur
              </span>
              <input
                name="factuurregel"
                defaultValue={kamp.factuurregel ?? ""}
                placeholder="Les Young Engineers"
                className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </label>
            <label>
              <span className="text-sm font-medium text-ink">
                Prijs per kind
              </span>
              <input
                name="prijs"
                defaultValue={kamp.prijs === null ? "" : String(kamp.prijs)}
                inputMode="decimal"
                placeholder="20"
                className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </label>
            <div className="sm:col-span-2">
              <button
                type="submit"
                className="rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
              >
                Bewaren
              </button>
              <p className="mt-1.5 text-xs text-ink-dim">
                Alle dagen van dezelfde reeks horen dezelfde factuurregel te
                hebben: op het maandoverzicht worden ze dan één regel met een
                aantal ervoor.
              </p>
            </div>
          </form>
        </details>

        <details className="mt-4 rounded-xl border border-border bg-surface p-5 print:hidden">
          <summary className="cursor-pointer font-display text-base font-semibold text-ink">
            Elke week herhalen
          </summary>
          <form action={herhaalActiviteit} className="mt-4 flex flex-wrap items-end gap-3">
            <input type="hidden" name="id" value={kamp.id} />
            <label>
              <span className="text-sm font-medium text-ink">
                Aantal weken erbij
              </span>
              <input
                type="number"
                name="keren"
                min={1}
                max={20}
                defaultValue={4}
                className="mt-1 w-24 rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </label>
            <label className="flex items-center gap-2 pb-2 text-sm text-ink">
              <input
                type="checkbox"
                name="kinderen"
                value="ja"
                defaultChecked
                className="h-4 w-4 rounded border-border text-forest focus:ring-forest"
              />
              Dezelfde kinderen mee overzetten
            </label>
            <button
              type="submit"
              className="rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Zetten
            </button>
          </form>
          <p className="mt-2 text-xs text-ink-dim">
            Maakt dezelfde dag telkens een week later, met dezelfde plaats,
            factuurregel en prijs. Zo hoef je een wekelijkse les maar één keer
            in te vullen en kan je per dag de aanwezigheden aanduiden.
          </p>
        </details>
      </main>
    </>
  );
}
