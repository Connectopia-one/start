import { requireBeheerder } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";
import { Header } from "@/components/Header";
import { markeerAllesGezien, verwijderAanvraag, zetAfgehandeld } from "./actions";
import { Kopieer } from "./Kopieer";

/* Aanvragen komen binnen terwijl je kijkt, dus niets bewaren. */
export const dynamic = "force-dynamic";

type Aanvraag = {
  id: string;
  onderwerp: string;
  soort: string;
  gegevens: Record<string, string>;
  gezien: boolean;
  afgehandeld: boolean;
  created_at: string;
};

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
  Uit de antwoorden halen we het mailadres en het telefoonnummer naar boven,
  want dat is wat je nodig hebt om iemand terug te contacteren. De namen van
  de vakjes staan in website/content/formulier.ts; herkennen op een woord in
  de vraag werkt ook als die vraag ooit anders geformuleerd wordt.
*/
function vindWaarde(gegevens: Record<string, string>, woord: string) {
  const sleutel = Object.keys(gegevens).find((k) =>
    k.toLowerCase().includes(woord)
  );
  return sleutel ? gegevens[sleutel] : null;
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

const STATUSSEN = [
  { sleutel: "", naam: "Alles" },
  { sleutel: "nieuw", naam: "Nieuw" },
  { sleutel: "open", naam: "Nog open" },
  { sleutel: "afgehandeld", naam: "Afgehandeld" },
] as const;

function filterLink(onderwerp: string, status: string) {
  const vraag = new URLSearchParams();
  if (onderwerp) vraag.set("onderwerp", onderwerp);
  if (status) vraag.set("status", status);
  const tekst = vraag.toString();
  return tekst ? `/beheer/aanvragen?${tekst}` : "/beheer/aanvragen";
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
    status?: string;
  }>;
}) {
  const session = await requireBeheerder();
  const { fout, succes, onderwerp: gekozen = "", status = "" } = await searchParams;
  const naam = session.profile?.full_name ?? session.email ?? "";

  const db = createAdminClient();
  const { data, error } = await db
    .from("aanvragen")
    .select("id, onderwerp, soort, gegevens, gezien, afgehandeld, created_at")
    .order("created_at", { ascending: false })
    .limit(300);

  const alles = (data ?? []) as Aanvraag[];

  /*
    Filteren op soort aanvraag en op status. Kim vroeg dit op 8 oktober 2026:
    "kan ik ook de aanvragen die binnenkomen filteren? Op vakantiekamp,
    proefles, meetesten enzo?" Met acht formulieren door elkaar wordt de lijst
    anders onleesbaar.

    De onderwerpen komen uit de aanvragen zelf en niet uit een vaste lijst.
    Zet de website er morgen een formulier bij, dan staat dat knopje hier
    vanzelf, zonder dat hier iets moet veranderen.
  */
  const perOnderwerp = new Map<string, number>();
  for (const a of alles) {
    perOnderwerp.set(a.onderwerp, (perOnderwerp.get(a.onderwerp) ?? 0) + 1);
  }
  const onderwerpen = [...perOnderwerp.entries()].sort(
    (a, b) => b[1] - a[1] || kort(a[0]).localeCompare(kort(b[0]), "nl"),
  );

  const aanvragen = alles.filter((a) => {
    if (gekozen && a.onderwerp !== gekozen) return false;
    if (status === "nieuw") return !a.gezien;
    if (status === "open") return !a.afgehandeld;
    if (status === "afgehandeld") return a.afgehandeld;
    return true;
  });

  const nieuw = alles.filter((a) => !a.gezien).length;
  const open = alles.filter((a) => !a.afgehandeld).length;
  const gefilterd = Boolean(gekozen || status);
  /* Dubbels zoeken we in de hele lijst: twee aanvragen van dezelfde persoon
     blijven dubbel, ook al staat er een filter aan. */
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
          {alles.length} aanvra{alles.length === 1 ? "ag" : "gen"}
          {nieuw > 0 ? ` · ${nieuw} nieuw` : ""}
          {open > 0 ? ` · ${open} nog open` : ""}
          {gefilterd ? ` · ${aanvragen.length} getoond` : ""}
        </p>

        {/* Filteren op soort aanvraag. De knopjes staan er alleen als er meer
            dan één soort binnengekomen is; bij één soort zouden ze niets
            doen. */}
        {onderwerpen.length > 1 && (
          <div className="mt-4 flex flex-wrap gap-2">
            <Knopje href={filterLink("", status)} aan={!gekozen}>
              Alle soorten
            </Knopje>
            {onderwerpen.map(([naam, aantal]) => (
              <Knopje
                key={naam}
                href={filterLink(naam, status)}
                aan={gekozen === naam}
              >
                {kort(naam)} <span className="opacity-70">{aantal}</span>
              </Knopje>
            ))}
          </div>
        )}

        {/* En op status: nieuw, nog open of afgehandeld. */}
        {alles.length > 0 && (
          <div className="mt-2 flex flex-wrap gap-2">
            {STATUSSEN.map((s) => (
              <Knopje
                key={s.sleutel}
                href={filterLink(gekozen, s.sleutel)}
                aan={status === s.sleutel}
              >
                {s.naam}
              </Knopje>
            ))}
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

        {/* Eén knop voor alle mailadressen van wat er nu in de lijst staat.
            Samen met de filter erboven is dat precies wat je nodig hebt om
            bijvoorbeeld iedereen van het vakantiekamp in één keer te mailen:
            filter op dat kamp, kopieer, en plak in het bcc-vak. We zetten ze
            achter puntkomma's, want dat is wat een mailprogramma verwacht, en
            elk adres staat er maar één keer in. */}
        {adressen.length > 1 && (
          <div className="mt-4">
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
          <form action={markeerAllesGezien} className="mt-4">
            <button
              type="submit"
              className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
            >
              Alles als gelezen markeren
            </button>
          </form>
        )}

        {!error && !aanvragen.length && (
          <p className="mt-6 text-sm text-ink-dim">
            {gefilterd ? (
              <>
                Geen aanvragen die hieraan voldoen.{" "}
                <a href="/beheer/aanvragen" className="underline">
                  Toon alles
                </a>
                .
              </>
            ) : (
              "Er is nog niets binnengekomen."
            )}
          </p>
        )}

        <ul className="mt-6 space-y-3">
          {aanvragen.map((aanvraag) => {
            const mail = vindWaarde(aanvraag.gegevens, "mail");
            const gsm = vindWaarde(aanvraag.gegevens, "gsm");
            const isDubbel = dubbels.has(aanvraag.id);
            return (
              <li
                key={aanvraag.id}
                className={`rounded-lg border bg-surface p-4 ${
                  aanvraag.afgehandeld
                    ? "border-border opacity-70"
                    : aanvraag.gezien
                      ? "border-border"
                      : "border-forest/50"
                }`}
              >
                <div className="flex flex-wrap items-start justify-between gap-2">
                  <div>
                    <p className="font-medium text-ink">{aanvraag.onderwerp}</p>
                    <p className="mt-0.5 text-xs text-ink-dim">
                      {tijdstip(aanvraag.created_at, isDubbel)}
                      {!aanvraag.gezien && " · nieuw"}
                      {aanvraag.afgehandeld && " · afgehandeld"}
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

                <div className="mt-4 flex flex-wrap gap-2">
                  <form action={zetAfgehandeld}>
                    <input type="hidden" name="id" value={aanvraag.id} />
                    <input
                      type="hidden"
                      name="afgehandeld"
                      value={aanvraag.afgehandeld ? "nee" : "ja"}
                    />
                    <button
                      type="submit"
                      className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
                    >
                      {aanvraag.afgehandeld
                        ? "Terug openzetten"
                        : "Afgehandeld"}
                    </button>
                  </form>
                  <form action={verwijderAanvraag}>
                    <input type="hidden" name="id" value={aanvraag.id} />
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
