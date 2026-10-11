import Link from "next/link";
import { notFound } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import { FicheRegels } from "@/components/FicheRegels";
import { Kopieer } from "../../aanvragen/Kopieer";
import { KINDVELDEN, samen, type Kind } from "@/lib/kind";
import { datumTekst, leeftijd, type Activiteit } from "@/lib/activiteiten";
import { bewaarNotitie, haalKindWeg, voegKindToe } from "../actions";

export const dynamic = "force-dynamic";

type Gezin = { id: string; full_name: string | null; telefoon: string | null };
type KindRij = Kind & { profile_id: string };
type Deelname = { kind_id: string; notitie: string | null };

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
        .select("id, naam, soort, datum, plaats, archief")
        .eq("id", id)
        .maybeSingle(),
      db.from("deelnames").select("kind_id, notitie").eq("activiteit_id", id),
      db.from("kinderen").select(`${KINDVELDEN}, profile_id`).order("naam"),
    ]);

  if (!activiteit) notFound();
  const kamp = activiteit as Activiteit;

  const deelnames = (deelnamesData ?? []) as Deelname[];
  const alleKinderen = (kinderenData ?? []) as unknown as KindRij[];
  const notitieVan = new Map(deelnames.map((d) => [d.kind_id, d.notitie]));

  const { data: gezinnenData } = await db
    .from("profiles")
    .select("id, full_name, telefoon");
  const gezinnen = new Map(
    ((gezinnenData ?? []) as Gezin[]).map((g) => [g.id, g]),
  );

  const opDeLijst = alleKinderen
    .filter((kind) => notitieVan.has(kind.id))
    .sort((a, b) => a.naam.localeCompare(b.naam, "nl"));
  const rest = alleKinderen.filter((kind) => !notitieVan.has(kind.id));

  /* De lijst als tabel met tabs ertussen, om in een rekenblad te plakken. */
  const tabel = [
    ["Kind", "Leeftijd", "Gezin", "Telefoon", "Allergieën", "Medicatie", "Ophalen"].join(
      "\t",
    ),
    ...opDeLijst.map((kind) =>
      [
        kind.naam,
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

        <ul className="mt-5 space-y-3">
          {opDeLijst.map((kind) => {
            const gezin = gezinnen.get(kind.profile_id);
            const jaar = leeftijd(kind.geboortedatum);
            const notitie = notitieVan.get(kind.id) ?? "";
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
                  <div className="flex flex-wrap gap-2 print:hidden">
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
      </main>
    </>
  );
}
