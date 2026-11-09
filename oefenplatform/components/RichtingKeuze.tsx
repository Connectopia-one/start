"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

/* Zie lib/leerrichting.ts. Twee knoppen; de keuze blijft een jaar bewaard. */
const COOKIE = "leerrichting";

export function RichtingKeuze({ dg }: { dg: boolean }) {
  const router = useRouter();
  const [bezig, setBezig] = useState(false);

  function kies(waarde: "dg" | "algemeen") {
    setBezig(true);
    document.cookie = `${COOKIE}=${waarde}; path=/; max-age=${60 * 60 * 24 * 365}; samesite=lax`;
    router.refresh();
    setTimeout(() => setBezig(false), 600);
  }

  const knop = (actief: boolean) =>
    `rounded-full border-2 px-4 py-2 text-sm font-semibold transition ${
      actief
        ? "border-forest bg-forest text-white"
        : "border-forest/40 bg-surface text-forest-dark hover:border-forest"
    }`;

  return (
    <div className="mt-3">
      <p className="text-sm font-semibold text-ink">Ik leer voor:</p>
      <div className="mt-2 flex flex-wrap gap-2" aria-busy={bezig}>
        <button type="button" className={knop(!dg)} onClick={() => kies("algemeen")}>
          De andere richtingen (alles)
        </button>
        <button type="button" className={knop(dg)} onClick={() => kies("dg")}>
          Bedrijfs- of welzijnswetenschappen
        </button>
      </div>
      {dg && (
        <p className="mt-2 text-sm text-ink">
          <span aria-hidden>🟠</span> Je krijgt enkel de vragen die je nodig
          hebt. Bij hoofdstukken met een oranje bolletje valt een stuk weg.
        </p>
      )}
    </div>
  );
}
