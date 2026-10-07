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

        {/* Zoals op het prikbord: de blaadjes vullen de kolommen op. */}
        <div className={`mt-8 ${bordKlassen}`}>
          <div className="columns-1 gap-5 sm:columns-2 lg:columns-3">
            {tipsTekst.stappen.map((stap, i) => (
              <Blaadje key={stap.kop} nummer={i}>
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
          </div>
        </div>

        {tipsTekst.nota && (
          <p className="mt-8 max-w-2xl rounded-md bg-amber/10 px-4 py-3 text-sm text-ink">
            {tipsTekst.nota}
          </p>
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
