import { requireIngelogd } from "@/lib/auth";
import { Header } from "@/components/Header";
import { kalenderPerMaand, dagInfo } from "@/lib/kalender";

const DAGNAMEN = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"];

function bouwMaandRooster(jaar: number, maand: number): (number | null)[][] {
  const eersteDag = new Date(jaar, maand, 1);
  const aantalDagen = new Date(jaar, maand + 1, 0).getDate();
  const startWeekdag = (eersteDag.getDay() + 6) % 7; // maandag = 0

  const cellen: (number | null)[] = Array(startWeekdag).fill(null);
  for (let d = 1; d <= aantalDagen; d++) cellen.push(d);
  while (cellen.length % 7 !== 0) cellen.push(null);

  const weken: (number | null)[][] = [];
  for (let i = 0; i < cellen.length; i += 7) weken.push(cellen.slice(i, i + 7));
  return weken;
}

function datumSleutel(jaar: number, maand: number, dag: number): string {
  return `${jaar}-${String(maand + 1).padStart(2, "0")}-${String(dag).padStart(2, "0")}`;
}

function korteLocatie(label: string): string {
  if (label.includes("Atheneum")) return "Atheneum";
  if (label.includes("T2 Campus")) return "T2 Campus";
  if (label.includes("Level X")) return "Level X";
  return label;
}

const KLEUR = {
  les: { bg: "bg-forest/10", tekst: "text-forest-dark" },
  kamp: { bg: "bg-amber/15", tekst: "text-amber" },
  geenles: { bg: "bg-danger/10", tekst: "text-danger" },
} as const;

export default async function KalenderPage() {
  const session = await requireIngelogd();
  const naam = session.profile?.full_name ?? session.email ?? "";
  const isBeheerder = session.profile?.role === "beheerder";

  return (
    <>
      <Header naam={naam} isBeheerder={isBeheerder} terugHref="/portaal" terugLabel="Overzicht" />
      <main className="mx-auto w-full max-w-5xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">Kalender schooljaar 2026-2027</h1>
        <p className="mt-1 text-sm text-ink-dim">
          Vaste lesdagen: dinsdag Atheneum Hasselt, woensdag T2 Campus Genk, zaterdag Level X 28
          Hasselt. Hieronder zie je per dag of er les is.
        </p>

        <div className="mt-4 flex flex-wrap gap-4 text-xs">
          <span className="flex items-center gap-1.5">
            <span className="h-2.5 w-2.5 rounded-full bg-forest" /> Les
          </span>
          <span className="flex items-center gap-1.5">
            <span className="h-2.5 w-2.5 rounded-full bg-amber" /> Kamp
          </span>
          <span className="flex items-center gap-1.5">
            <span className="h-2.5 w-2.5 rounded-full bg-danger" /> Geen les
          </span>
        </div>

        <div className="mt-6 grid gap-6 md:grid-cols-2">
          {kalenderPerMaand().map(({ jaar, maand, naam: maandNaam }) => {
            const weken = bouwMaandRooster(jaar, maand);
            return (
              <div key={maandNaam} className="rounded-xl border border-border bg-surface p-4">
                <h2 className="font-display text-base font-semibold text-ink">{maandNaam}</h2>
                <div className="mt-3 grid grid-cols-7 gap-1.5">
                  {DAGNAMEN.map((d) => (
                    <div key={d} className="text-center text-[11px] font-medium text-ink-dim">
                      {d}
                    </div>
                  ))}
                  {weken.flatMap((week, wi) =>
                    week.map((dag, di) => {
                      if (dag === null) return <div key={`${wi}-${di}`} />;
                      const info = dagInfo(datumSleutel(jaar, maand, dag));
                      const kleur = info ? KLEUR[info.type] : null;
                      return (
                        <div
                          key={`${wi}-${di}`}
                          title={info ? `${info.label}${info.detail ? " — " + info.detail : ""}` : undefined}
                          className={`flex min-h-14 flex-col items-center justify-start gap-0.5 rounded-md border border-border p-1 text-center ${kleur ? kleur.bg : "bg-paper"}`}
                        >
                          <span className="text-[12px] font-medium text-ink">{dag}</span>
                          {info && (
                            <span className={`text-[9.5px] leading-tight ${kleur?.tekst}`}>
                              {info.type === "les"
                                ? korteLocatie(info.label)
                                : info.type === "kamp"
                                  ? "Kamp"
                                  : "Geen les"}
                            </span>
                          )}
                        </div>
                      );
                    })
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </main>
    </>
  );
}
