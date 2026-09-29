"use client";

import { useEffect, useState, type ReactNode } from "react";
import { KlikbareLeerbundel } from "@/components/KlikbareLeerbundel";
import { Volgordepuzzel } from "@/components/Volgordepuzzel";
import type { KlikbareBundel } from "@/lib/leerbundel";

/*
  De drie tabbladen van een hoofdstuk, plus het slot op de oefeningen.

  Heeft een hoofdstuk een klikbare leerbundel (voorlopig enkel 🌱 Start), dan
  staan de oefeningen achter een sleutel: eerst de onderdelen doorklikken, dan
  de kleine volgordepuzzel. Dat kwam er na de melding van een kind dat de
  leerbundels oversloeg en daardoor de oefeningen niet kon.

  Eenmaal open blijft het open, ook als het kind later terugkomt: dat staat in
  de opslag van de browser. Er is geen kolom in de databank voor nodig.

  Het slot geldt niet per kind maar per browser. Dat is met opzet: het is een
  duwtje om eerst te lezen, geen controle die ergens geteld wordt.
*/

const MINSTENS = 3; // Onder drie onderdelen is de puzzel geen puzzel.

function slotSleutel(hoofdstukId: string) {
  return `connectopia-bundel-open-${hoofdstukId}`;
}

export function HoofdstukTabs({
  oefeningen,
  leerstof,
  aantalLeerstof,
  rekenmachine,
  bundel,
  hoofdstukId,
}: {
  oefeningen: ReactNode;
  leerstof: ReactNode;
  aantalLeerstof: number;
  rekenmachine: ReactNode | null;
  bundel?: KlikbareBundel | null;
  hoofdstukId?: string;
}) {
  const [tab, setTab] = useState<"oefeningen" | "leerstof" | "rekenmachine">(
    "oefeningen",
  );
  const [ontgrendeld, setOntgrendeld] = useState(false);
  const [gelezenUitOpslag, setGelezenUitOpslag] = useState(false);

  const opSlot = Boolean(
    bundel && hoofdstukId && bundel.secties.length >= MINSTENS,
  );

  // localStorage is een bron buiten React; pas na het eerste tekenen uitlezen,
  // anders verschilt wat de server maakte van wat de browser toont.
  useEffect(() => {
    if (!opSlot || !hoofdstukId) return;
    let open = false;
    try {
      open = window.localStorage.getItem(slotSleutel(hoofdstukId)) === "ja";
    } catch {
      // privénavigatie: dan blijft het slot dicht tot de puzzel gelukt is
    }
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setOntgrendeld(open);
    setGelezenUitOpslag(true);
  }, [opSlot, hoofdstukId]);

  function opgelost() {
    if (hoofdstukId) {
      try {
        window.localStorage.setItem(slotSleutel(hoofdstukId), "ja");
      } catch {
        // dan onthoudt de browser het niet, maar deze keer staat het wel open
      }
    }
    setOntgrendeld(true);
  }

  const oefeningenPaneel = !opSlot ? (
    oefeningen
  ) : !gelezenUitOpslag ? null : ontgrendeld ? (
    oefeningen
  ) : (
    <Slot naarLeerstof={() => setTab("leerstof")} />
  );

  return (
    <div className="mt-6">
      <div className="flex gap-2 border-b border-border">
        <button
          type="button"
          onClick={() => setTab("oefeningen")}
          className={`px-3 py-2 text-sm font-medium ${
            tab === "oefeningen"
              ? "border-b-2 border-forest text-forest-dark"
              : "text-ink-dim hover:text-ink"
          }`}
        >
          Oefeningen {opSlot && !ontgrendeld && gelezenUitOpslag && "🔒"}
        </button>
        <button
          type="button"
          onClick={() => setTab("leerstof")}
          className={`px-3 py-2 text-sm font-medium ${
            tab === "leerstof"
              ? "border-b-2 border-forest text-forest-dark"
              : "text-ink-dim hover:text-ink"
          }`}
        >
          Leerstof {aantalLeerstof > 0 && `(${aantalLeerstof})`}
        </button>
        {rekenmachine && (
          <button
            type="button"
            onClick={() => setTab("rekenmachine")}
            className={`px-3 py-2 text-sm font-medium ${
              tab === "rekenmachine"
                ? "border-b-2 border-forest text-forest-dark"
                : "text-ink-dim hover:text-ink"
            }`}
          >
            Rekenmachine
          </button>
        )}
      </div>

      <div className={tab === "oefeningen" ? "" : "hidden"}>
        {oefeningenPaneel}
      </div>
      <div className={tab === "leerstof" ? "" : "hidden"}>
        {bundel && hoofdstukId && (
          <KlikbareLeerbundel
            bundel={bundel}
            hoofdstukId={hoofdstukId}
            puzzel={
              opSlot && !ontgrendeld ? (
                <Volgordepuzzel
                  koppen={bundel.secties.map((s) => s.kop)}
                  hoofdstukId={hoofdstukId}
                  onOpgelost={opgelost}
                />
              ) : undefined
            }
          />
        )}
        {leerstof}
      </div>
      {rekenmachine && (
        <div className={tab === "rekenmachine" ? "" : "hidden"}>
          {rekenmachine}
        </div>
      )}
    </div>
  );
}

function Slot({ naarLeerstof }: { naarLeerstof: () => void }) {
  return (
    <div className="mt-6 rounded-xl border border-forest/40 bg-forest/5 px-5 py-6">
      <p className="font-display text-base font-semibold text-ink">
        🔒 Eerst de leerstof, dan de oefeningen
      </p>
      <p className="mt-2 text-sm text-ink-dim">
        Bij dit hoofdstuk hoort een leerbundel die je stuk voor stuk kan
        openklikken. Heb je alle onderdelen bekeken, dan krijg je een kleine
        puzzel, en daarna staan de oefeningen open. Je hoeft het maar één keer
        te doen.
      </p>
      <p className="mt-2 text-sm text-ink-dim">
        Lees je liever op papier? De pdf staat op dezelfde bladzijde, en
        daaronder kan je zeggen dat je ze al gelezen hebt. Dan krijg je de
        puzzel meteen.
      </p>
      <button
        type="button"
        onClick={naarLeerstof}
        className="mt-4 rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
      >
        Naar de leerstof
      </button>
    </div>
  );
}
