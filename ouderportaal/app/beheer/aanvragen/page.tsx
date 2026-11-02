import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import {
  archiveerBehandeld,
  markeerAllesGezien,
  verwijderAanvraag,
  zetAfgehandeld,
  zetArchief,
  zetStap,
} from "./actions";
import { Kopieer } from "./Kopieer";
import { MET_DE_HAND, vindWaarde, type Aanvraag } from "@/lib/aanvraaglijsten";
import { STAPPEN } from "@/lib/aanvraagstappen";

/* Aanvragen komen binnen terwijl je kijkt, dus niets bewaren. */
export const dynamic = "force-dynamic";

function tijdstip(waarde: string, metSeconden = false) {
  return new Date(waarde).toLocaleString("nl-BE", {
    day: "numeric",
    month: "long",
    hour: "2-digit",
    minute: "2-digit",
    ...(metSeconden ? { second: "2-digit" as const } : {}),
  });
}

/*
  Dezelfde persoon twee keer in de lijst.

  Dat kan twee dingen betekenen: iemand heeft het formulier twee keer ingevuld,
  of er is twee keer verstuurd met één invulbeurt (een tweede klik terwijl de
  eerste nog bezig was). Het verschil zie je aan de tijd: liggen ze seconden uit
  elkaar, dan is het dat tweede. Daarom staan bij een dubbel de seconden erbij.

  We vergelijken op mailadres of telefoonnummer binnen hetzelfde onderwerp,
  want dat is wat een gezin uniek maakt. Bij de winactie telt dit dubbel: wie
  er twee keer in staat, zou anders twee kansen hebben bij de loting.
*/
function sleutelVan(a: Aanvraag) {
  const mail = vindWaarde(a.gegevens, "mail")?.trim().toLowerCase();
  const gsm = vindWaarde(a.gegevens, "gsm")?.replace(/\D/g, "");
  const wie = mail || (gsm && gsm.length >= 8 ? gsm : null);
  return wie ? `${a.onderwerp}|${wie}` : null;
}

function zoekDubbels(aanvragen: Aanvraag[]) {
  const perSleutel = new Map<string, Aanvraag[]>();
  for (const a of aanvragen) {
    const sleutel = sleutelVan(a);
    if (!sleutel) continue;
    perSleutel.set(sleutel, [...(perSleutel.get(sleutel) ?? []), a]);
  }
  const dubbel = new Set<string>();
  for (const groep of perSleutel.values()) {
    if (groep.length > 1) groep.forEach((a) => dubbel.add(a.id));
  }
  return dubbel;
}

/*
  De naam van het onderwerp zoals hij op een knopje past.

  In de databank staat "Aanvraag gratis proefles via de website", want dat
  was ooit het onderwerp van de mail. Op een rij filterknopjes is dat staartje
  alleen maar ruis, en het staat bij elk onderwerp hetzelfde.

  Gaat de inschrijving over een bepaald traject, dan zit dat woordje middenin:
  "Inschrijving via de website — Vakantiekampen". Daarom knippen we het eruit
  waar het ook staat, en niet alleen achteraan. Zo houdt elk kamp, elke
  pluswerking en elk traject zijn eigen knopje.
*/
function kort(onderwerp: string) {
  const zonder = onderwerp
    .replace(/\s*via de website\s*/i, " ")
    .replace(/\s+/g, " ")
    .trim();
  return zonder || onderwerp;
}

/*
  De drie tabbladen. Kim op 2 november 2026: "voor degene die ik nog echt moet
  behandelen, dat die enkel nog op het scherm staan, dat de anderen op een
  tweede tabblad komen. Nu moet ik altijd scrollen door iedereen." En ze wou
  ook een archief, nog altijd verdeeld per soort.
*/
const TABS = [
  { sleutel: "", naam: "Te behandelen" },
  { sleutel: "behandeld", naam: "Behandeld" },
  { sleutel: "archief", naam: "Archief" },
] as const;
type Tab = (typeof TABS)[number]["sleutel"];

function opTab(a: Aanvraag, tab: Tab) {
  if (tab === "archief") return Boolean(a.gearchiveerd);
  if (a.gearchiveerd) return false;
  return tab === "behandeld" ? a.afgehandeld : !a.afgehandeld;
}

function filterLink(tab: string, onderwerp: string, stap: string) {
  const vraag = new URLSearchParams();
  if (tab) vraag.set("tab", tab);
  if (onderwerp) vraag.set("onderwerp", onderwerp);
  if (stap) vraag.set("stap", stap);
  const tekst = vraag.toString();
  return tekst ? `/beheer/aanvragen?${tekst}` : "/beheer/aanvragen";
}

/* Voldoet een aanvraag aan de gekozen stap-filter? "geen mail" is wie nog
   geen mail kreeg, want dat is wat je meestal zoekt. */
function opStap(a: Aanvraag, stap: string) {
  if (!stap) return true;
  if (stap === "nieuw") return !a.gezien;
  if (stap === "geen mail") return !(a.stappen ?? []).includes("mail verstuurd");
  return (a.stappen ?? []).includes(stap);
}

/* Eén knopje in de filterrij. Aan staat het in het donkergroen. */
function Knopje({
  href,
  aan,
  children,
}: {
  href: string;
  aan: boolean;
  children: React.ReactNode;
}) {
  return (
    <a
      href={href}
      className={`rounded-full px-3 py-1 text-sm transition ${
        aan
          ? "bg-forest text-white"
          : "border border-border text-ink-dim hover:border-forest hover:text-forest-dark"
      }`}
    >
      {children}
    </a>
  );
}

export default async function AanvragenBeheer({
  searchParams,
}: {
  searchParams: Promise<{
    fout?: string;
    succes?: string;
    onderwerp?: string;
    stap?: string;
    tab?: string;
  }>;
}) {
  const session = await requireBeheerder();
  const {
    fout,
    succes,
    onderwerp: gekozen = "",
    stap = "",
    tab: tabWaarde = "",
  } = await searchParams;
  const tab: Tab = TABS.some((t) => t.sleutel === tabWaarde)
    ? (tabWaarde as Tab)
    : "";
  const naam = session.profile?.full_name ?? session.email ?? "";
  const hier = filterLink(tab, gekozen, stap);

  /*
    De kolommen stappen en gearchiveerd komen uit aanvragen-status.sql. Is
    dat nog niet gedraaid, dan lezen we zonder, zodat de lijst gewoon blijft
    werken, en zeggen we wat er moet gebeuren.
  */
  const db = createAdminClient();
  const VELDEN = "id, onderwerp, soort, gegevens, gezien, afgehandeld, created_at";
  let statusKlaar = true;
  const eerste = await db
    .from("aanvragen")
    .select(`${VELDEN}, stappen, gearchiveerd`)
    .order("created_at", { ascending: false })
    .limit(1000);
  let data: unknown[] | null = eerste.data;
  let error = eerste.error;
  if (error && /stappen|gearchiveerd/.test(error.message)) {
    statusKlaar = false;
    const zonder = await db
      .from("aanvragen")
      .select(VELDEN)
      .order("created_at", { ascending: false })
      .limit(1000);
    data = zonder.data;
    error = zonder.error;
  }

  /*
    Enkel wat van buiten komt. Een kind dat Kim zelf op een kamplijst zette,
    staat in dezelfde tabel (zie lib/aanvraaglijsten.ts), maar is geen
    aanvraag. Kim op 2 november 2026: "mijn dingen zouden daar niet bij
    moeten staan, enkel de externe aanvragen."
  */
  const alles = ((data ?? []) as unknown as Aanvraag[]).filter(
    (a) => a.soort !== MET_DE_HAND,
  );
  const opDitTab = alles.filter((a) => opTab(a, tab));

  /*
    Filteren op soort aanvraag. Kim vroeg dit op 8 oktober 2026: "kan ik ook
    de aanvragen die binnenkomen filteren? Op vakantiekamp, proefles,
    meetesten enzo?" De knopjes tellen wat er op dit tabblad staat, zodat het
    archief ook per soort verdeeld blijft.

    De onderwerpen komen uit de aanvragen zelf en niet uit een vaste lijst.
    Zet de website er morgen een formulier bij, dan staat dat knopje hier
    vanzelf.
  */
  const perOnderwerp = new Map<string, number>();
  for (const a of opDitTab) {
    perOnderwerp.set(a.onderwerp, (perOnderwerp.get(a.onderwerp) ?? 0) + 1);
  }
  /* Staat er een soort gekozen die op dit tabblad leeg is, laat dat knopje
     dan toch staan, anders zie je niet waarom de lijst leeg is. */
  if (gekozen && !perOnderwerp.has(gekozen)) perOnderwerp.set(gekozen, 0);
  const onderwerpen = [...perOnderwerp.entries()].sort(
    (a, b) => b[1] - a[1] || kort(a[0]).localeCompare(kort(b[0]), "nl"),
  );

  const vanSoort = opDitTab.filter((a) => !gekozen || a.onderwerp === gekozen);
  const aanvragen = vanSoort.filter((a) => opStap(a, stap));

  const STAPFILTERS = [
    { sleutel: "", naam: "Alles" },
    { sleutel: "nieuw", naam: "Nieuw" },
    ...(statusKlaar
      ? [
          { sleutel: "geen mail", naam: "Nog geen mail" },
          ...STAPPEN.map((s) => ({ sleutel: s.sleutel as string, naam: s.naam })),
        ]
      : []),
  ];

  const telTab = (t: Tab) => alles.filter((a) => opTab(a, t)).length;
  const nieuw = alles.filter((a) => !a.gezien).length;
  const gefilterd = Boolean(gekozen || stap);
  /* Dubbels zoeken we in de hele lijst: twee aanvragen van dezelfde persoon
     blijven dubbel, ook al staan ze op een ander tabblad. */
  const dubbels = zoekDubbels(alles);
  /* De mailadressen van wat er nu in de lijst staat, elk één keer en in de
     volgorde waarin ze binnenkwamen. Een vakje met een vraag over mail kan ook
     iets anders bevatten dan een adres, dus we houden enkel wat op een adres
     lijkt. */
  const adressen = Array.from(
    new Set(
      aanvragen
        .map((a) => vindWaarde(a.gegevens, "mail")?.trim())
        .filter((m): m is string => !!m && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(m))
        .map((m) => m.toLowerCase()),
    ),
  );

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
          Aanvragen van de website
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {telTab("")} te behandelen
          {nieuw > 0 ? ` · ${nieuw} nieuw` : ""}
          {gefilterd ? ` · ${aanvragen.length} getoond` : ""}
        </p>

        {/* De twee manieren om naar dezelfde aanvragen te kijken: elke aanvraag
            apart, of gegroepeerd per kampdag. Kim vroeg dat tweede op
            11 oktober 2026. */}
        <div className="mt-4 flex flex-wrap gap-2">
          <span className="rounded-full bg-forest px-3 py-1 text-sm text-white">
            Alle aanvragen
          </span>
          <a
            href="/beheer/aanvragen/lijsten"
            className="rounded-full border border-border px-3 py-1 text-sm text-ink-dim transition hover:border-forest hover:text-forest-dark"
          >
            Lijsten uit de inschrijvingen
          </a>
        </div>

        {!statusKlaar && (
          <div className="mt-4 rounded-lg border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            <p className="font-medium">Nog één SQL-bestand te draaien.</p>
            <p className="mt-1 text-ink-dim">
              Voor de knoppen mail verstuurd, gebeld, ingeschreven en het
              archief: open Supabase, ga naar de SQL Editor en voer{" "}
              <code className="rounded bg-ink/5 px-1">
                website/supabase/aanvragen-status.sql
              </code>{" "}
              uit. Tot dan werken Te behandelen en Behandeld al wel.
            </p>
          </div>
        )}

        {/* De tabbladen: wat nog moet, wat behandeld is, en het archief. */}
        <div className="mt-6 flex flex-wrap gap-1 border-b border-border">
          {TABS.map((t) => {
            const aan = tab === t.sleutel;
            return (
              <a
                key={t.sleutel}
                href={filterLink(t.sleutel, gekozen, "")}
                className={`-mb-px rounded-t-md border px-4 py-2 text-sm font-medium transition ${
                  aan
                    ? "border-border border-b-surface bg-surface text-ink"
                    : "border-transparent text-ink-dim hover:text-forest-dark"
                }`}
              >
                {t.naam}{" "}
                <span className="font-normal opacity-70">{telTab(t.sleutel)}</span>
              </a>
            );
          })}
        </div>

        {/* Filteren op soort aanvraag, binnen dit tabblad. */}
        {onderwerpen.length > 1 && (
          <div className="mt-4 flex flex-wrap gap-2">
            <Knopje href={filterLink(tab, "", stap)} aan={!gekozen}>
              Alle soorten
            </Knopje>
            {onderwerpen.map(([naam, aantal]) => (
              <Knopje
                key={naam}
                href={filterLink(tab, naam, stap)}
                aan={gekozen === naam}
              >
                {kort(naam)} <span className="opacity-70">{aantal}</span>
              </Knopje>
            ))}
          </div>
        )}

        {/* En op wat er al gebeurde. */}
        {opDitTab.length > 0 && (
          <div className="mt-2 flex flex-wrap gap-2">
            {STAPFILTERS.map((s) => {
              const aantal = vanSoort.filter((a) => opStap(a, s.sleutel)).length;
              return (
                <Knopje
                  key={s.sleutel}
                  href={filterLink(tab, gekozen, s.sleutel)}
                  aan={stap === s.sleutel}
                >
                  {s.naam}
                  {s.sleutel && <span className="opacity-70"> {aantal}</span>}
                </Knopje>
              );
            })}
          </div>
        )}
        {dubbels.size > 0 && (
          <p className="mt-2 rounded-md bg-amber/10 px-3 py-2 text-sm text-ink">
            {dubbels.size} aanvragen staan er meer dan één keer in, van dezelfde
            persoon. Ze zijn gemarkeerd, met de seconden erbij: liggen ze
            seconden uit elkaar, dan is er twee keer verstuurd met één
            invulbeurt en mag je er één verwijderen.
          </p>
        )}

        {/* Staat de tabel er nog niet, dan zeggen we wat er moet gebeuren in
            plaats van een leeg scherm te tonen. */}
        {error && (
          <div className="mt-6 rounded-lg border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            <p className="font-medium">Deze lijst kan nog niet gelezen worden.</p>
            <p className="mt-2 text-ink-dim">
              Waarschijnlijk staat de tabel er nog niet. Open Supabase, ga naar
              de SQL Editor en voer het bestand{" "}
              <code className="rounded bg-ink/5 px-1">
                website/supabase/aanvragen.sql
              </code>{" "}
              uit. Daarna verschijnen de aanvragen hier vanzelf.
            </p>
            <p className="mt-2 text-xs text-ink-dim">{error.message}</p>
          </div>
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

        <div className="mt-4 flex flex-wrap items-start gap-3">
          {/* Eén knop voor alle mailadressen van wat er nu in de lijst staat.
              Samen met de filter erboven is dat precies wat je nodig hebt om
              bijvoorbeeld iedereen van het vakantiekamp in één keer te mailen:
              filter op dat kamp, kopieer, en plak in het bcc-vak. */}
          {adressen.length > 1 && (
            <div>
              <Kopieer
                waarde={adressen.join("; ")}
                wat={`de ${adressen.length} mailadressen van deze lijst`}
                label={`Kopieer de ${adressen.length} mailadressen`}
                stijl="vol"
              />
              <p className="mt-1.5 text-xs text-ink-dim">
                Van wat er nu in de lijst staat, elk adres één keer. Plak het in
                het bcc-vak, zodat niemand de adressen van de anderen ziet.
              </p>
            </div>
          )}

          {nieuw > 0 && (
            <form action={markeerAllesGezien}>
              <input type="hidden" name="terug" value={hier} />
              <button
                type="submit"
                className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
              >
                Alles als gelezen markeren
              </button>
            </form>
          )}

          {tab === "behandeld" && statusKlaar && vanSoort.length > 0 && (
            <form action={archiveerBehandeld}>
              <input type="hidden" name="terug" value={hier} />
              <input type="hidden" name="onderwerp" value={gekozen} />
              <button
                type="submit"
                className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
              >
                {gekozen
                  ? `Deze ${vanSoort.length} van ${kort(gekozen)} naar het archief`
                  : `Alle ${vanSoort.length} behandelde naar het archief`}
              </button>
            </form>
          )}
        </div>

        {!error && !aanvragen.length && (
          <p className="mt-6 text-sm text-ink-dim">
            {gefilterd ? (
              <>
                Geen aanvragen die hieraan voldoen.{" "}
                <a href={filterLink(tab, "", "")} className="underline">
                  Toon alles van dit tabblad
                </a>
                .
              </>
            ) : tab === "" ? (
              "Niets meer te behandelen."
            ) : tab === "behandeld" ? (
              "Hier komt wat je op behandeld zet."
            ) : (
              "Het archief is nog leeg."
            )}
          </p>
        )}

        <ul className="mt-6 space-y-3">
          {aanvragen.map((aanvraag) => {
            const mail = vindWaarde(aanvraag.gegevens, "mail");
            const gsm = vindWaarde(aanvraag.gegevens, "gsm");
            const isDubbel = dubbels.has(aanvraag.id);
            const stappen = aanvraag.stappen ?? [];
            return (
              <li
                key={aanvraag.id}
                className={`rounded-lg border bg-surface p-4 ${
                  aanvraag.gezien ? "border-border" : "border-forest/50"
                }`}
              >
                <div className="flex flex-wrap items-start justify-between gap-2">
                  <div>
                    <p className="font-medium text-ink">{aanvraag.onderwerp}</p>
                    <p className="mt-0.5 text-xs text-ink-dim">
                      {tijdstip(aanvraag.created_at, isDubbel)}
                      {!aanvraag.gezien && " · nieuw"}
                      {aanvraag.afgehandeld && " · behandeld"}
                      {aanvraag.gearchiveerd && " · in het archief"}
                    </p>
                    {isDubbel && (
                      <p className="mt-1 inline-block rounded-full bg-amber/15 px-2 py-0.5 text-xs font-medium text-ink">
                        staat meer dan één keer in de lijst
                      </p>
                    )}
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {mail && (
                      <Kopieer waarde={mail} wat={`het mailadres ${mail}`} />
                    )}
                    {mail && (
                      <a
                        href={`mailto:${mail}`}
                        className="rounded-md bg-forest px-3 py-1.5 text-sm font-medium text-white transition hover:bg-forest-dark"
                      >
                        Mailen
                      </a>
                    )}
                    {gsm && (
                      <Kopieer waarde={gsm} wat={`het nummer ${gsm}`} />
                    )}
                    {gsm && (
                      <a
                        href={`tel:${gsm.replace(/\s/g, "")}`}
                        className="rounded-md border border-border px-3 py-1.5 text-sm text-ink hover:border-forest"
                      >
                        Bellen
                      </a>
                    )}
                  </div>
                </div>

                <dl className="mt-3 grid gap-x-6 gap-y-1.5 sm:grid-cols-2">
                  {Object.entries(aanvraag.gegevens).map(([vraag, antwoord]) => (
                    <div key={vraag}>
                      <dt className="text-xs text-ink-dim">{vraag}</dt>
                      <dd className="text-sm text-ink">{antwoord}</dd>
                    </div>
                  ))}
                </dl>

                {/* Wat er al gebeurde. Een knop die aan staat is donkergroen
                    met een vinkje; nog eens klikken zet hem uit. */}
                {statusKlaar && (
                  <div className="mt-4 flex flex-wrap gap-2">
                    {STAPPEN.map((s) => {
                      const aan = stappen.includes(s.sleutel);
                      return (
                        <form key={s.sleutel} action={zetStap}>
                          <input type="hidden" name="id" value={aanvraag.id} />
                          <input type="hidden" name="stap" value={s.sleutel} />
                          <input type="hidden" name="aan" value={aan ? "nee" : "ja"} />
                          <input type="hidden" name="terug" value={hier} />
                          <button
                            type="submit"
                            aria-pressed={aan}
                            className={`rounded-full px-3 py-1 text-sm transition ${
                              aan
                                ? "bg-forest text-white hover:bg-forest-dark"
                                : "border border-border text-ink-dim hover:border-forest hover:text-forest-dark"
                            }`}
                          >
                            {aan ? "✓ " : ""}
                            {s.naam}
                          </button>
                        </form>
                      );
                    })}
                  </div>
                )}

                <div className="mt-3 flex flex-wrap gap-2 border-t border-border/60 pt-3">
                  {!aanvraag.gearchiveerd && (
                    <form action={zetAfgehandeld}>
                      <input type="hidden" name="id" value={aanvraag.id} />
                      <input
                        type="hidden"
                        name="afgehandeld"
                        value={aanvraag.afgehandeld ? "nee" : "ja"}
                      />
                      <input type="hidden" name="terug" value={hier} />
                      <button
                        type="submit"
                        className={`rounded-md px-3 py-1.5 text-sm ${
                          aanvraag.afgehandeld
                            ? "border border-border text-ink-dim hover:border-forest hover:text-forest-dark"
                            : "bg-forest font-medium text-white hover:bg-forest-dark"
                        }`}
                      >
                        {aanvraag.afgehandeld
                          ? "Toch nog niet behandeld"
                          : "Behandeld"}
                      </button>
                    </form>
                  )}
                  {statusKlaar && (
                    <form action={zetArchief}>
                      <input type="hidden" name="id" value={aanvraag.id} />
                      <input
                        type="hidden"
                        name="archief"
                        value={aanvraag.gearchiveerd ? "nee" : "ja"}
                      />
                      <input type="hidden" name="terug" value={hier} />
                      <button
                        type="submit"
                        className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
                      >
                        {aanvraag.gearchiveerd
                          ? "Uit het archief halen"
                          : "Naar het archief"}
                      </button>
                    </form>
                  )}
                  <form action={verwijderAanvraag}>
                    <input type="hidden" name="id" value={aanvraag.id} />
                    <input type="hidden" name="terug" value={hier} />
                    <button
                      type="submit"
                      className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-danger hover:text-danger"
                    >
                      Verwijderen
                    </button>
                  </form>
                </div>
              </li>
            );
          })}
        </ul>
      </main>
    </>
  );
}
