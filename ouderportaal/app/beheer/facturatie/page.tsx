import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createAdminClient, tabelOntbreekt } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import { Kopieer } from "../aanvragen/Kopieer";
import {
  ACTIVITEITVELDEN,
  euro,
  korteDatum,
  langeDatum,
  leesMaand,
  maandGrenzen,
  maandNaam,
  schuifMaand,
  type Activiteit,
} from "@/lib/activiteiten";
import {
  allesAlsTabel,
  alsRegels,
  gezinNaam,
  maakFacturen,
  voldaanTekst,
  type DeelnameRij,
  type GezinRij,
  type KindRij,
  type Ontvangst,
} from "@/lib/facturatie";
import {
  haalStortingTerug,
  markeerGestort,
  noteerOntvangst,
  wisOntvangst,
} from "./actions";

/* Er kan elk moment een aanwezigheid bijkomen, dus niets bewaren. */
export const dynamic = "force-dynamic";

/*
  Het blad waarmee Kim haar facturen maakt.

  Per gezin staat er wat die maand gevolgd is, geteld per factuurregel: "5 x
  Les Young Engineers". Dat is precies wat ze in Billit intypt. Het rekenwerk
  staat in lib/facturatie.ts; deze pagina gaat over de opmaak.

  Wat hier niet in zit: de korting voor gezinnen met een verhoogde
  tegemoetkoming. Die spreekt Kim apart af, en een bedrag dat automatisch
  gehalveerd wordt zou je niet meer zien staan. Daarom staat de volle prijs er,
  met een regel die eraan herinnert.
*/
export default async function FacturatieBeheer({
  searchParams,
}: {
  searchParams: Promise<{ maand?: string; fout?: string; succes?: string }>;
}) {
  const session = await requireBeheerder();
  const { maand: gevraagd, fout, succes } = await searchParams;
  const naam = session.profile?.full_name ?? session.email ?? "";

  const maand = leesMaand(gevraagd);
  const { van, tot } = maandGrenzen(maand);

  const db = createAdminClient();
  const [
    { data: activiteitenData, error: activiteitenFout },
    { data: kinderenData },
    { data: gezinnenData },
    { data: ontvangstenData, error: ontvangstenFout },
    { count: zonderDatum },
  ] = await Promise.all([
    db
      .from("activiteiten")
      .select(ACTIVITEITVELDEN)
      .gte("datum", van)
      .lte("datum", tot),
    db.from("kinderen").select("id, naam, profile_id"),
    db.from("profiles").select("id, full_name").eq("role", "ouder"),
    db
      .from("ontvangsten")
      .select("id, profile_id, datum, bedrag, wijze, opmerking, gestort_op")
      .order("datum", { ascending: false }),
    db
      .from("activiteiten")
      .select("id", { count: "exact", head: true })
      .is("datum", null)
      .eq("archief", false),
  ]);

  const activiteiten = (activiteitenData ?? []) as Activiteit[];

  /* De deelnames van net deze dagen. Zonder dagen geen vraag naar de
     databank: .in() met een lege lijst geeft anders alles of niets,
     afhankelijk van de versie. */
  let deelnames: DeelnameRij[] = [];
  if (activiteiten.length > 0) {
    const { data } = await db
      .from("deelnames")
      .select("activiteit_id, kind_id, aanwezig")
      .in(
        "activiteit_id",
        activiteiten.map((a) => a.id),
      );
    deelnames = (data ?? []) as DeelnameRij[];
  }

  const kinderen = (kinderenData ?? []) as KindRij[];
  const gezinnen = (gezinnenData ?? []) as GezinRij[];
  const ontvangsten = (ontvangstenData ?? []) as Ontvangst[];
  const vanDezeMaand = ontvangsten.filter(
    (o) => o.datum >= van && o.datum <= tot,
  );
  const nogInDeKas = ontvangsten.filter(
    (o) => !o.gestort_op && o.wijze === "cash",
  );
  const inDeKas = nogInDeKas.reduce((som, o) => som + Number(o.bedrag), 0);

  const facturen = maakFacturen({
    activiteiten,
    deelnames,
    kinderen,
    gezinnen,
    ontvangsten: vanDezeMaand,
  });

  const leesfout = activiteitenFout
    ? (tabelOntbreekt(
        activiteitenFout,
        "voor de kampen en lessen",
        "ouderportaal/supabase/activiteiten.sql",
      ) ?? `Dit kon niet gelezen worden: ${activiteitenFout.message}`)
    : ontvangstenFout
      ? (tabelOntbreekt(
          ontvangstenFout,
          "voor wat er al betaald is",
          "ouderportaal/supabase/activiteiten.sql",
        ) ?? `Dit kon niet gelezen worden: ${ontvangstenFout.message}`)
      : null;

  const totaal = facturen.reduce((som, f) => som + f.totaal, 0);
  const openVinkjes = facturen.reduce((som, f) => som + f.nietAangeduid, 0);
  const naamVan = new Map(gezinnen.map((g) => [g.id, gezinNaam(g)]));

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
          Facturen van {maandNaam(maand)}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          Wat elk gezin die maand gevolgd heeft, geteld per factuurregel. Een
          kind telt mee tenzij het bij{" "}
          <Link
            href="/beheer/activiteiten"
            className="underline underline-offset-2"
          >
            de dag zelf
          </Link>{" "}
          op afwezig staat.
        </p>

        <div className="mt-4 flex flex-wrap items-center gap-2 print:hidden">
          <Link
            href={`/beheer/facturatie?maand=${schuifMaand(maand, -1)}`}
            className="rounded-full border border-border px-3 py-1 text-sm text-ink-dim transition hover:border-forest hover:text-forest-dark"
          >
            &larr; {maandNaam(schuifMaand(maand, -1))}
          </Link>
          <Link
            href={`/beheer/facturatie?maand=${schuifMaand(maand, 1)}`}
            className="rounded-full border border-border px-3 py-1 text-sm text-ink-dim transition hover:border-forest hover:text-forest-dark"
          >
            {maandNaam(schuifMaand(maand, 1))} &rarr;
          </Link>
        </div>

        {leesfout && (
          <p className="mt-6 rounded-lg border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
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

        {!leesfout && facturen.length === 0 && (
          <p className="mt-6 text-sm text-ink-dim">
            In {maandNaam(maand)} staat er nog geen kind op een dag met een
            datum. Zet de dagen klaar bij Kampen en lessen en duid daar de
            kinderen aan.
          </p>
        )}

        {facturen.length > 0 && (
          <>
            <div className="mt-6 rounded-xl border border-border bg-surface p-5">
              <p className="text-sm text-ink">
                {facturen.length}{" "}
                {facturen.length === 1 ? "gezin" : "gezinnen"} ·{" "}
                {activiteiten.length}{" "}
                {activiteiten.length === 1 ? "dag" : "dagen"} in deze maand ·
                samen {euro(totaal)}
              </p>
              {openVinkjes > 0 && (
                <p className="mt-1 text-sm text-ink-dim">
                  Bij {openVinkjes}{" "}
                  {openVinkjes === 1 ? "deelname" : "deelnames"} is de
                  aanwezigheid nog niet aangeduid. Die tellen hier mee als
                  aanwezig.
                </p>
              )}
              <p className="mt-1 text-xs text-ink-dim">
                De korting voor een verhoogde tegemoetkoming zit hier niet in:
                die pas je in Billit zelf aan.
              </p>
              <div className="mt-3 print:hidden">
                <Kopieer
                  waarde={allesAlsTabel(facturen)}
                  wat="alle factuurregels van deze maand"
                  label="Kopieer alles als tabel"
                />
              </div>
            </div>

            <div className="mt-6 space-y-4">
              {facturen.map((factuur) => {
                /* Zonder prijzen weten we het bedrag niet, en dan is
                   "voldaan" een belofte die we niet kunnen nakijken. */
                const voldaan =
                  factuur.totaal > 0 &&
                  factuur.betaald + 0.001 >= factuur.totaal;
                const zin = voldaanTekst(factuur, maandNaam(maand));
                return (
                  <section
                    key={factuur.gezin.id}
                    className="rounded-xl border border-border bg-surface p-5 print:break-inside-avoid"
                  >
                    <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
                      <h2 className="font-display text-lg font-semibold text-ink">
                        <Link
                          href={`/beheer/gezinnen/${factuur.gezin.id}`}
                          className="underline-offset-2 hover:underline"
                        >
                          {gezinNaam(factuur.gezin)}
                        </Link>
                      </h2>
                      <p className="text-sm text-ink-dim">
                        {factuur.totaal > 0 && euro(factuur.totaal)}
                        {factuur.zonderPrijs > 0 &&
                          ` · ${factuur.zonderPrijs} zonder prijs`}
                      </p>
                    </div>

                    <ul className="mt-3 space-y-2">
                      {factuur.regels.map((regel) => (
                        <li
                          key={regel.label}
                          className="border-b border-border/60 pb-2 last:border-0 last:pb-0"
                        >
                          <p className="text-sm font-medium text-ink">
                            {regel.aantal} x {regel.label}
                            {regel.prijs !== null && (
                              <span className="ml-2 font-normal text-ink-dim">
                                {euro(regel.prijs)} per keer ={" "}
                                {euro(regel.totaal)}
                              </span>
                            )}
                            {regel.prijs === null && regel.totaal > 0 && (
                              <span className="ml-2 font-normal text-ink-dim">
                                samen {euro(regel.totaal)}
                              </span>
                            )}
                          </p>
                          <p className="mt-0.5 text-xs text-ink-dim">
                            {regel.perKind
                              .map((kind) =>
                                kind.aantal === 1
                                  ? kind.naam
                                  : `${kind.naam} (${kind.aantal})`,
                              )
                              .join(", ")}
                            {regel.nietAangeduid > 0 &&
                              ` · ${regel.nietAangeduid} nog niet aangeduid`}
                            {regel.zonderPrijs > 0 &&
                              ` · bij ${regel.zonderPrijs} staat geen prijs`}
                          </p>
                        </li>
                      ))}
                    </ul>

                    {factuur.ontvangsten.length > 0 && (
                      <p className="mt-3 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">
                        Al betaald: {euro(factuur.betaald)} (
                        {factuur.ontvangsten
                          .map(
                            (o) =>
                              `${o.wijze} ${euro(Number(o.bedrag))} op ${korteDatum(o.datum)}`,
                          )
                          .join(", ")}
                        ).{" "}
                        {voldaan
                          ? "Deze factuur mag als voldaan verstuurd worden."
                          : "Dat is nog niet het volledige bedrag."}
                      </p>
                    )}

                    <div className="mt-3 flex flex-wrap gap-2 print:hidden">
                      <Kopieer
                        waarde={alsRegels(factuur)}
                        wat={`de factuurregels van ${gezinNaam(factuur.gezin)}`}
                        label="Kopieer de regels"
                        stijl="vol"
                      />
                      {zin && (
                        <Kopieer
                          waarde={zin}
                          wat="de vermelding dat de factuur betaald is"
                          label="Kopieer de voldaan-vermelding"
                        />
                      )}
                    </div>
                    <p className="mt-1.5 text-xs text-ink-dim print:hidden">
                      De regels staan als omschrijving, aantal en prijs per
                      keer, met een tab ertussen.
                    </p>
                  </section>
                );
              })}
            </div>
          </>
        )}

        {(zonderDatum ?? 0) > 0 && (
          <p className="mt-6 text-xs text-ink-dim">
            {zonderDatum}{" "}
            {zonderDatum === 1 ? "activiteit heeft" : "activiteiten hebben"}
            geen datum en valt dus in geen enkele maand.{" "}
            <Link
              href="/beheer/activiteiten"
              className="underline underline-offset-2"
            >
              Een datum zetten
            </Link>
          </p>
        )}

        {/* --------------------------------------------------------------
            Wat er al betaald is. Cash in de hand of een overschrijving die
            vooraf komt: beide bepalen of een factuur als voldaan mag.
            -------------------------------------------------------------- */}
        <h2 className="mt-12 font-display text-xl font-semibold text-ink">
          Al betaald
        </h2>
        <p className="mt-1 text-sm text-ink-dim">
          Noteer hier wat je cash in de hand kreeg of wat een gezin vooraf
          overschreef. Dan weet je bij de factuur of ze voldaan is.
        </p>

        <form
          action={noteerOntvangst}
          className="mt-4 grid gap-3 rounded-xl border border-border bg-surface p-5 sm:grid-cols-2 print:hidden"
        >
          <input type="hidden" name="maand" value={maand} />
          <label className="sm:col-span-2">
            <span className="text-sm font-medium text-ink">Van welk gezin</span>
            <select
              name="profile_id"
              defaultValue=""
              className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            >
              <option value="">Kies een gezin</option>
              {[...gezinnen]
                .sort((a, b) => gezinNaam(a).localeCompare(gezinNaam(b), "nl"))
                .map((gezin) => (
                  <option key={gezin.id} value={gezin.id}>
                    {gezinNaam(gezin)}
                  </option>
                ))}
            </select>
          </label>
          <label>
            <span className="text-sm font-medium text-ink">Bedrag</span>
            <input
              name="bedrag"
              inputMode="decimal"
              placeholder="50"
              className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
          </label>
          <label>
            <span className="text-sm font-medium text-ink">Hoe</span>
            <select
              name="wijze"
              defaultValue="cash"
              className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            >
              <option value="cash">cash</option>
              <option value="overschrijving">overschrijving</option>
            </select>
          </label>
          <label>
            <span className="text-sm font-medium text-ink">
              Wanneer <span className="text-ink-dim">(mag leeg)</span>
            </span>
            <input
              type="date"
              name="datum"
              className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
          </label>
          <label>
            <span className="text-sm font-medium text-ink">
              Opmerking <span className="text-ink-dim">(mag leeg)</span>
            </span>
            <input
              name="opmerking"
              placeholder="aan de deur, kamp 2 november"
              className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
          </label>
          <div className="sm:col-span-2">
            <button
              type="submit"
              className="rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Noteren
            </button>
          </div>
        </form>

        {nogInDeKas.length > 0 && (
          <section className="mt-6 rounded-xl border border-amber/40 bg-amber/10 p-5">
            <h3 className="font-display text-base font-semibold text-ink">
              Nog in de kas: {euro(inDeKas)}
            </h3>
            <p className="mt-1 text-sm text-ink-dim">
              Vink aan wat je samen gestort hebt en zet de dag erbij. Een
              storting is geen tweede inkomst: het is geld dat van je kas naar
              de rekening gaat. Zet de factuur in Billit op betaald op de dag
              dat je het geld kreeg, niet op de dag van de storting.
            </p>
            <form action={markeerGestort} className="mt-3">
              <input type="hidden" name="maand" value={maand} />
              <ul className="space-y-1.5">
                {nogInDeKas.map((rij) => (
                  <li key={rij.id} className="text-sm text-ink">
                    <label className="flex flex-wrap items-center gap-2">
                      <input
                        type="checkbox"
                        name="ontvangst"
                        value={rij.id}
                        className="h-4 w-4 rounded border-border text-forest focus:ring-forest"
                      />
                      <span className="font-medium">
                        {euro(Number(rij.bedrag))}
                      </span>
                      <span className="text-ink-dim">
                        {rij.profile_id
                          ? (naamVan.get(rij.profile_id) ?? "gezin onbekend")
                          : "gezin onbekend"}{" "}
                        · {langeDatum(rij.datum)}
                        {rij.opmerking && ` · ${rij.opmerking}`}
                      </span>
                    </label>
                  </li>
                ))}
              </ul>
              <div className="mt-3 flex flex-wrap items-end gap-2">
                <label>
                  <span className="text-sm font-medium text-ink">
                    Gestort op
                  </span>
                  <input
                    type="date"
                    name="gestort_op"
                    className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
                  />
                </label>
                <button
                  type="submit"
                  className="rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
                >
                  Op gestort zetten
                </button>
              </div>
            </form>
          </section>
        )}

        {vanDezeMaand.length > 0 && (
          <section className="mt-6">
            <h3 className="font-display text-base font-semibold text-ink">
              Betaald in {maandNaam(maand)}
            </h3>
            <ul className="mt-3 space-y-2">
              {vanDezeMaand.map((rij) => (
                <li
                  key={rij.id}
                  className="flex flex-wrap items-center justify-between gap-2 rounded-lg border border-border bg-surface px-4 py-3 text-sm"
                >
                  <span className="text-ink">
                    <span className="font-medium">
                      {euro(Number(rij.bedrag))}
                    </span>{" "}
                    <span className="text-ink-dim">
                      {rij.wijze} ·{" "}
                      {rij.profile_id
                        ? (naamVan.get(rij.profile_id) ?? "gezin onbekend")
                        : "gezin onbekend"}{" "}
                      · {langeDatum(rij.datum)}
                      {rij.gestort_op &&
                        ` · gestort op ${langeDatum(rij.gestort_op)}`}
                      {rij.opmerking && ` · ${rij.opmerking}`}
                    </span>
                  </span>
                  <span className="flex flex-wrap gap-2 print:hidden">
                    {rij.gestort_op && (
                      <form action={haalStortingTerug}>
                        <input type="hidden" name="id" value={rij.id} />
                        <input type="hidden" name="maand" value={maand} />
                        <button
                          type="submit"
                          className="rounded-md border border-border px-3 py-1 text-xs text-ink-dim hover:border-forest hover:text-forest-dark"
                        >
                          Terug naar de kas
                        </button>
                      </form>
                    )}
                    <form action={wisOntvangst}>
                      <input type="hidden" name="id" value={rij.id} />
                      <input type="hidden" name="maand" value={maand} />
                      <button
                        type="submit"
                        className="rounded-md border border-border px-3 py-1 text-xs text-ink-dim hover:border-danger hover:text-danger"
                      >
                        Weghalen
                      </button>
                    </form>
                  </span>
                </li>
              ))}
            </ul>
          </section>
        )}
      </main>
    </>
  );
}
