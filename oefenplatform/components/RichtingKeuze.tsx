"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import type { Leerrichting } from "@/lib/leerrichting";

/*
  Zie lib/leerrichting.ts. Drie knoppen; de keuze blijft een jaar bewaard en
  geldt voor elk vak met een keuze "Ik leer voor".

  Kim, 9 november 2026: niet "dit mag je overslaan", want dan klinkt het
  alsof de leerling zelf moet zoeken. Wat wegvalt, laten wij weg zodra je
  kiest, en de zin eronder zegt wat er gebeurd is.
*/
const COOKIE = "leerrichting";

type Keuze = Exclude<Leerrichting, "dg">;

function bewaarKeuze(waarde: Keuze) {
  document.cookie = `${COOKIE}=${waarde}; path=/; max-age=${60 * 60 * 24 * 365}; samesite=lax`;
}

const KNOPPEN: { waarde: Keuze; label: string }[] = [
  { waarde: "algemeen", label: "Een andere richting" },
  { waarde: "bedrijf", label: "Bedrijfswetenschappen" },
  { waarde: "welzijn", label: "Welzijnswetenschappen" },
];

export function RichtingKeuze({
  keuze,
  uitleg,
}: {
  keuze: Leerrichting;
  /* Wat er wegvalt of bijkomt bij elke keuze. Zonder tekst de standaardzin. */
  uitleg?: Partial<Record<Leerrichting, string>>;
}) {
  const router = useRouter();
  const [bezig, setBezig] = useState(false);

  function kies(waarde: Keuze) {
    setBezig(true);
    bewaarKeuze(waarde);
    router.refresh();
    setTimeout(() => setBezig(false), 600);
  }

  const knop = (actief: boolean) =>
    `rounded-full border-2 px-4 py-2 text-sm font-semibold transition ${
      actief
        ? "border-forest bg-forest text-white"
        : "border-forest/40 bg-surface text-forest-dark hover:border-forest"
    }`;

  const zin =
    uitleg?.[keuze] ??
    (keuze !== "algemeen"
      ? "🟠 Je krijgt enkel de vragen die je nodig hebt. Bij hoofdstukken met een oranje bolletje laten we een stuk weg."
      : undefined);

  return (
    <div className="mt-3">
      <p className="text-sm font-semibold text-ink">Ik leer voor:</p>
      <div className="mt-2 flex flex-wrap gap-2" aria-busy={bezig}>
        {KNOPPEN.map((k) => (
          <button
            key={k.waarde}
            type="button"
            className={knop(keuze === k.waarde)}
            onClick={() => kies(k.waarde)}
          >
            {k.label}
          </button>
        ))}
      </div>
      {zin && <p className="mt-2 text-sm text-ink">{zin}</p>}
    </div>
  );
}
