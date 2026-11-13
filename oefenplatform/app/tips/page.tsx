import Link from "next/link";
import { Blaadje, bordKlassen } from "@/components/Blaadje";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { tipsTekst } from "@/inhoud/tips";

export const metadata = {
  title: "Zo gebruiken wij het — Oefenplatform Connectopia",
  description:
    "Hoe wij zelf met het oefenplatform werken: een vak kiezen, door de tocht gaan, notities nemen, en dan de oefeningen van deel 1 en deel 2.",
};

/*
  Een tipspagina, geen handleiding.

  Elke stap is een memoblaadje op een prikbord, zoals op /weetjes. Kim vroeg
  die vorm uitdrukkelijk: negen stappen onder elkaar lezen als een reglement,
  negen briefjes op een bord lezen als tips.

  Ook zichtbaar zonder account, net als /materiaal: wie nog twijfelt of dit
  iets voor zijn kind is, mag eerst zien hoe ermee gewerkt wordt. Er staat
  geen gegeven van een kind op, dus er is niets af te schermen.

  De tekst staat volledig in inhoud/tips.ts, zodat aanpassen geen code vraagt.
*/
export default async function TipsPage() {
  const session = await getSessionProfile();

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          {tipsTekst.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">
          {tipsTekst.titel}
        </h1>
        <p className="mt-4 max-w-2xl text-sm text-ink-dim">{tipsTekst.intro}</p>

        {/* Een raster, geen kolommen: de stappen moeten rij per rij van links
            naar rechts te lezen zijn. In kolommen staan stap 1, 2 en 3 onder
            elkaar en komt 4 pas ernaast, en dat leest lastig bij een
            volgorde. Met items-start houdt elk blaadje zijn eigen hoogte. */}
        <div className={`mt-8 ${bordKlassen} pb-5`}>
          <div className="grid grid-cols-1 items-start gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {tipsTekst.stappen.map((stap, i) => (
              <Blaadje key={stap.kop} nummer={i} inRaster>
                <p className="font-display text-[13px] font-semibold uppercase tracking-wide text-ink-dim">
                  Stap {i + 1}
                </p>
                <h2 className="mt-1 font-display text-[17px] font-semibold leading-snug text-ink">
                  {stap.kop}
                </h2>
                <p className="mt-2 text-[15px] leading-relaxed text-ink">
                  {stap.tekst}
                </p>
              </Blaadje>
            ))}
            {tipsTekst.briefjes.map((briefje, i) => (
              <Blaadje
                key={briefje.kop}
                nummer={tipsTekst.stappen.length + i}
                inRaster
              >
                <p className="font-display text-[13px] font-semibold uppercase tracking-wide text-ink-dim">
                  📌 {briefje.label}
                </p>
                <h2 className="mt-1 font-display text-[17px] font-semibold leading-snug text-ink">
                  {briefje.kop}
                </h2>
                <p className="mt-2 text-[15px] leading-relaxed text-ink">
                  {briefje.tekst}
                </p>
              </Blaadje>
            ))}
          </div>
        </div>

        {/* Voor gezinnen uit Nederland: welk niveau past ongeveer. Een gewoon
            vak onder het bord, want een tabel leest niet op een post-it. */}
        {tipsTekst.nederland && (
          <section id="nederland" className="mt-10 scroll-mt-6 rounded-[20px] border border-forest/20 bg-white/70 p-6">
            <h2 className="font-display text-xl font-semibold text-ink">
              {tipsTekst.nederland.kop}
            </h2>
            <p className="mt-2 max-w-2xl text-[15px] leading-relaxed text-ink">
              {tipsTekst.nederland.intro}
            </p>
            <div className="mt-4 overflow-x-auto">
              <table className="w-full border-collapse text-left text-[14px] sm:text-[15px]">
                <thead>
                  <tr>
                    {tipsTekst.nederland.tabelKoppen.map((kop) => (
                      <th
                        key={kop}
                        className="border-b-2 border-forest/30 py-2 pr-4 font-display font-semibold text-forest"
                      >
                        {kop}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {tipsTekst.nederland.tabel.map((rij) => (
                    <tr key={rij[0]}>
                      {rij.map((cel, i) => (
                        <td
                          key={i}
                          className={`border-b border-forest/10 py-2 pr-3 align-top text-ink ${i === 0 ? "whitespace-nowrap font-semibold" : ""}`}
                        >
                          {cel}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <div className="mt-6 grid grid-cols-1 gap-4 sm:grid-cols-2">
              {tipsTekst.nederland.vakken.map((vak) => (
                <div key={vak.kop} className="rounded-xl border border-forest/15 p-4">
                  <h3 className="font-display text-[16px] font-semibold text-ink">
                    {vak.kop}
                  </h3>
                  <p className="mt-1 text-[15px] leading-relaxed text-ink">
                    {vak.tekst}
                  </p>
                </div>
              ))}
            </div>
          </section>
        )}

        {tipsTekst.oproepLink && (
          <p className="mt-8">
            <Link
              href={tipsTekst.oproepLink}
              className="inline-block rounded-md bg-forest px-4 py-2 text-sm font-semibold text-white transition hover:bg-forest-dark"
            >
              {tipsTekst.oproepTekst}
            </Link>
          </p>
        )}
      </main>
    </>
  );
}
