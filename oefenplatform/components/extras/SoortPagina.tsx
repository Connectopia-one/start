import Link from "next/link";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import {
  extrasTekst,
  scholen,
  soorten,
  spelKaarten,
  vindSpel,
  type School,
  type Soort,
} from "@/inhoud/extras";
import { materiaalGroepSuggesties, materiaalTekst } from "@/inhoud/materiaal";
import { haalMateriaal, type MateriaalItem } from "@/lib/extrasMateriaal";

/*
  Eén pagina achter een van de vier grote knoppen op /extras. Alles staat per
  schoolniveau: lagere school, middelbare school, en voor iedereen. Een kop
  zonder iets eronder wordt niet getoond.
*/

type Kaart = {
  sleutel: string;
  href: string;
  extern: boolean;
  icoon: string;
  titel: string;
  niveau?: string;
  tekst: string | null;
  groep?: string;
};

function spelHref(spel: string, niveauInSpel?: string) {
  return niveauInSpel
    ? `/extras/${spel}?niveau=${niveauInSpel}`
    : `/extras/${spel}`;
}

function kaartenVoor(
  soort: Soort,
  school: School,
  materiaal: MateriaalItem[],
): Kaart[] {
  if (soort === "spellen") {
    return spelKaarten
      .filter((k) => k.school === school)
      .map((k, i) => {
        const spel = vindSpel(k.spel);
        return {
          sleutel: `${k.spel}-${k.niveauInSpel ?? i}`,
          href: spelHref(k.spel, k.niveauInSpel),
          extern: false,
          icoon: spel?.icoon ?? "🎲",
          titel: spel?.titel ?? k.spel,
          niveau: k.niveau,
          tekst: k.tekst,
        };
      });
  }
  const icoon =
    soort === "documenten" ? "🖨️" : soort === "filmpjes" ? "🎬" : "🔗";
  return materiaal
    .filter((m) => m.soort === soort && m.school === school)
    .map((m) => ({
      sleutel: m.id,
      href: m.href,
      extern: true,
      icoon,
      titel: m.titel + (m.type === "pdf" ? " (pdf)" : ""),
      tekst: m.omschrijving,
      groep: m.groep,
    }));
}

/* Kaarten van één schoolniveau verdeeld onder hun kopje. Eerst de kopjes uit
   inhoud/materiaal.ts in die volgorde, dan andere kopjes, en wat geen kopje
   heeft helemaal onderaan. */
function perKopje(
  kaarten: Kaart[],
): { kop: string | null; kaarten: Kaart[] }[] {
  const zonder = (g?: string) => !g || g === "Allerlei";
  const koppen = Array.from(
    new Set(kaarten.filter((k) => !zonder(k.groep)).map((k) => k.groep!)),
  );
  koppen.sort((a, b) => {
    const ia = materiaalGroepSuggesties.indexOf(a);
    const ib = materiaalGroepSuggesties.indexOf(b);
    return (ia < 0 ? 99 : ia) - (ib < 0 ? 99 : ib);
  });
  const uit: { kop: string | null; kaarten: Kaart[] }[] = koppen.map((kop) => ({
    kop,
    kaarten: kaarten.filter((k) => k.groep === kop),
  }));
  const rest = kaarten.filter((k) => zonder(k.groep));
  if (rest.length) uit.push({ kop: null, kaarten: rest });
  return uit;
}

export async function SoortPagina({ soort }: { soort: Soort }) {
  const session = await getSessionProfile();
  const info = soorten.find((s) => s.slug === soort)!;
  const materiaal = soort === "spellen" ? [] : await haalMateriaal();

  const blokken = scholen
    .map((school) => ({
      school,
      kaarten: kaartenVoor(soort, school.slug, materiaal),
    }))
    .filter((b) => b.kaarten.length > 0);

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <Link
          href="/extras"
          className="text-sm text-forest-dark hover:underline"
        >
          &larr; {extrasTekst.terug}
        </Link>
        <h1 className="mt-4 font-display text-2xl font-semibold text-ink">
          <span aria-hidden>{info.icoon}</span> {info.titel}
        </h1>
        <p className="mt-2 max-w-2xl text-sm text-ink-dim">{info.tekst}</p>

        {blokken.length > 1 && (
          <nav className="mt-6 flex flex-wrap gap-2 text-sm">
            {blokken.map((b) => (
              <a
                key={b.school.slug}
                href={`#${b.school.slug}`}
                className="rounded-full border border-border bg-surface px-4 py-1.5 font-medium text-forest-dark transition hover:border-forest"
              >
                {b.school.titel}
              </a>
            ))}
          </nav>
        )}

        {blokken.length === 0 && (
          <p className="mt-8 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            {info.leeg}
          </p>
        )}

        {blokken.map((b) => (
          <section
            key={b.school.slug}
            id={b.school.slug}
            className="mt-10 scroll-mt-6"
          >
            <h2 className="font-display text-xl font-semibold text-ink">
              {b.school.titel}
            </h2>
            <p className="mt-1 text-sm text-ink-dim">{b.school.tekst}</p>
            {perKopje(b.kaarten).map((blok) => (
              <div key={blok.kop ?? "rest"}>
                {blok.kop && (
                  <h3 className="mt-6 font-display text-base font-semibold text-forest-dark">
                    {blok.kop}
                  </h3>
                )}
                <div className="mt-3 grid gap-4 sm:grid-cols-2">
                  {blok.kaarten.map((k) => {
                    const binnen = (
                      <>
                        <span className="font-display text-lg font-semibold text-ink">
                          <span aria-hidden>{k.icoon}</span> {k.titel}
                          {k.extern && (
                            <span aria-hidden className="text-forest">
                              {" "}
                              ↗
                            </span>
                          )}
                        </span>
                        {k.niveau && (
                          <span className="mt-2 inline-block self-start rounded-full bg-forest/10 px-3 py-1 text-sm font-semibold text-forest-dark">
                            {k.niveau}
                          </span>
                        )}
                        {k.tekst && (
                          <span className="mt-2 block text-sm text-ink-dim">
                            {k.tekst}
                          </span>
                        )}
                      </>
                    );
                    const klassen =
                      "flex flex-col rounded-xl border border-border bg-surface px-6 py-5 transition hover:border-forest hover:shadow-sm";
                    return k.extern ? (
                      <a
                        key={k.sleutel}
                        href={k.href}
                        target="_blank"
                        rel="noopener noreferrer"
                        className={klassen}
                      >
                        {binnen}
                      </a>
                    ) : (
                      <Link key={k.sleutel} href={k.href} className={klassen}>
                        {binnen}
                      </Link>
                    );
                  })}
                </div>
              </div>
            ))}
          </section>
        ))}

        {soort !== "spellen" && (
          <>
            {soort !== "documenten" && (
              <p className="mt-10 rounded-xl border border-border bg-surface px-5 py-4 text-sm text-ink-dim">
                {materiaalTekst.externNota}
              </p>
            )}
            <p className="mt-10 text-sm text-ink-dim">{materiaalTekst.nota}</p>
            {materiaalTekst.oproepLink && (
              <p className="mt-4">
                <Link
                  href={materiaalTekst.oproepLink}
                  className="inline-block rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
                >
                  {materiaalTekst.oproepTekst}
                </Link>
              </p>
            )}
          </>
        )}
      </main>
    </>
  );
}
