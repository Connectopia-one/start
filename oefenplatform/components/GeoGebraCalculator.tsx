"use client";

import { useEffect, useRef } from "react";

declare global {
  interface Window {
    GGBApplet?: new (
      params: Record<string, unknown>,
      useBrowserForJS: boolean
    ) => { inject: (elementId: string) => void };
  }
}

const CONTAINER_ID = "ggb-rekenmachine";

export function GeoGebraCalculator() {
  const wrapperRef = useRef<HTMLDivElement>(null);
  const geplaatst = useRef(false);

  useEffect(() => {
    function plaatsApplet() {
      if (geplaatst.current || !window.GGBApplet) return;
      geplaatst.current = true;
      const breedte = wrapperRef.current?.clientWidth ?? 600;
      const applet = new window.GGBApplet(
        {
          appName: "classic",
          width: breedte,
          height: 480,
          showToolBar: true,
          showAlgebraInput: true,
          showMenuBar: false,
          language: "nl",
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

  return (
    <div className="mt-6">
      <p className="mb-3 text-sm text-ink-dim">
        De officiële GeoGebra-rekenmachine, rechtstreeks hier ingebouwd — handig om grafieken,
        meetkunde en berekeningen te oefenen zoals bij de examencommissie.
      </p>
      <div ref={wrapperRef} id={CONTAINER_ID} className="overflow-hidden rounded-xl border border-border" />
    </div>
  );
}
