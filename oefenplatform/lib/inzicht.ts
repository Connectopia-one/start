export type VakScore = { vakId: string; naam: string; aantal: number; correct: number };

const MIN_AANTAL_VOOR_TIP = 3; // te weinig data geeft een misleidend percentage
const MIN_VERSCHIL_VOOR_TIP = 15; // procentpunten — anders is er geen echt verschil

/**
 * Vergelijkt de score per vak en geeft, als het verschil groot genoeg is om
 * betekenisvol te zijn, een korte positieve tip terug. Geeft null als er te
 * weinig data is of de scores te dicht bij elkaar liggen.
 */
export function genereerTip(vakScores: VakScore[]): string | null {
  const bruikbaar = vakScores.filter((v) => v.aantal >= MIN_AANTAL_VOOR_TIP);
  if (bruikbaar.length < 2) return null;

  const metPct = bruikbaar.map((v) => ({ ...v, pct: Math.round((v.correct / v.aantal) * 100) }));
  const beste = metPct.reduce((a, b) => (b.pct > a.pct ? b : a));
  const zwakste = metPct.reduce((a, b) => (b.pct < a.pct ? b : a));

  if (beste.vakId === zwakste.vakId || beste.pct - zwakste.pct < MIN_VERSCHIL_VOOR_TIP) {
    return null;
  }

  return `${beste.naam} gaat sterk (${beste.pct}% correct) — bij ${zwakste.naam} (${zwakste.pct}% correct) kan wat extra oefenen zeker helpen.`;
}
