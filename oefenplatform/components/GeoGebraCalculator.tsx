"use client";

import { useEffect, useRef, useState } from "react";

/*
  De officiële GeoGebra-rekenmachine, zoals de examencommissie ze aanbiedt.

  GeoGebra noemt een indeling van het scherm een "perspectief" en heeft daar
  letters voor. Wij zetten er drie knoppen op, want de vragen van statistiek
  vragen alle drie om een ander scherm:

    AG  algebra en grafiek naast elkaar, de gewone rekenmachine
    B   de kansrekenmachine (binomiaal, normaal, de staarten)
    S   het rekenblad, om een hele dataset in te typen en door te rekenen

  Zonder die knoppen moet een kind het menu van GeoGebra zelf doorzoeken, en
  dat menu staat uit (showMenuBar: false) omdat het ook de bestandsopties van
  GeoGebra opent.
*/

type GGBApi = {
  setPerspective: (code: string) => void;
};

declare global {
  interface Window {
    GGBApplet?: new (
      params: Record<string, unknown>,
      useBrowserForJS: boolean
    ) => { inject: (elementId: string) => void };
  }
}

const CONTAINER_ID = "ggb-rekenmachine";

const SCHERMEN = [
  { code: "AG", naam: "Gewone rekenmachine" },
  { code: "B", naam: "Kansrekenmachine" },
  { code: "S", naam: "Rekenblad" },
] as const;

export function GeoGebraCalculator() {
  const geplaatst = useRef(false);
  const api = useRef<GGBApi | null>(null);
  const [klaar, setKlaar] = useState(false);
  const [scherm, setScherm] = useState<string>("AG");

  useEffect(() => {
    function plaatsApplet() {
      if (geplaatst.current || !window.GGBApplet) return;
      geplaatst.current = true;
      // Niet clientWidth van de container gebruiken: dit tabblad kan bij het laden
      // nog verborgen zijn (display: none) door de tabbladen-component, waardoor
      // dat altijd 0 zou teruggeven en de rekenmachine kapot zou renderen.
      const breedte = Math.min(624, window.innerWidth - 48);
      const applet = new window.GGBApplet(
        {
          appName: "classic",
          width: breedte,
          height: 480,
          showToolBar: true,
          showAlgebraInput: true,
          showMenuBar: false,
          language: "nl",
          appletOnLoad: (ggb: GGBApi) => {
            api.current = ggb;
            setKlaar(true);
          },
        },
        true
      );
      applet.inject(CONTAINER_ID);
    }

    if (window.GGBApplet) {
      plaatsApplet();
      return;
    }

    const script = document.createElement("script");
    script.src = "https://www.geogebra.org/apps/deployggb.js";
    script.async = true;
    script.onload = plaatsApplet;
    document.body.appendChild(script);
  }, []);

  function kies(code: string) {
    if (!api.current) return;
    api.current.setPerspective(code);
    setScherm(code);
  }

  return (
    <div className="mt-6">
      <p className="mb-3 text-sm text-ink-dim">
        De officiële GeoGebra-rekenmachine, rechtstreeks hier ingebouwd — handig om grafieken,
        meetkunde en berekeningen te oefenen zoals bij de examencommissie.
      </p>
      {klaar ? (
        <div className="mb-3 flex flex-wrap gap-2">
          {SCHERMEN.map((s) => {
            const aan = s.code === scherm;
            return (
              <button
                key={s.code}
                type="button"
                onClick={() => kies(s.code)}
                aria-pressed={aan}
                className={`rounded-full border px-4 py-1.5 text-sm font-medium transition ${
                  aan
                    ? "border-forest bg-forest text-white"
                    : "border-border bg-surface text-ink hover:border-forest/50"
                }`}
              >
                {s.naam}
              </button>
            );
          })}
        </div>
      ) : null}
      <div id={CONTAINER_ID} className="overflow-hidden rounded-xl border border-border" />
      {klaar ? (
        <p className="mt-2 text-xs text-ink-dim">
          Kansrekenmachine: kies bovenaan de verdeling (binomiaal of normaal), vul de getallen in
          en duid aan welke staart je wil. Rekenblad: typ je gegevens in kolom A en vraag onderaan
          de centrummaten en de spreidingsmaten op.
        </p>
      ) : null}
    </div>
  );
}
