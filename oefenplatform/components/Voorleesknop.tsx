"use client";

import { useEffect, useState } from "react";

/*
  Voorlezen met de stem van het toestel zelf (de Web Speech API van de
  browser). Caroline en Sarah vroegen het in de enquête van november 2026.
  De leesmodus van Chrome was niet bruikbaar; Kim testte op 6 november de
  stemmen van Chrome en vond "Google Nederlands" absoluut de beste. Die nemen
  we dus eerst. Op een iPad of een ander toestel nemen we de beste
  Nederlandse stem die daar staat, met een Vlaamse stem vóór een andere.

  Staat standaard uit; de ouder zet het per kind aan in Mijn account.
  Kan het toestel niet voorlezen, dan verschijnt er geen knop.
*/

function kiesStem(stemmen: SpeechSynthesisVoice[]) {
  const nl = stemmen.filter((s) => s.lang.toLowerCase().startsWith("nl"));
  return (
    nl.find((s) => s.name === "Google Nederlands") ??
    nl.find((s) => /natural/i.test(s.name)) ??
    nl.find((s) => s.lang.toLowerCase() === "nl-be") ??
    nl[0] ??
    null
  );
}

/** Tekens die een stem anders hardop zou zeggen of zou overslaan. */
export function alsSpreektekst(tekst: string) {
  return tekst
    .replace(/\$/g, "")
    .replace(/[*_`#]/g, "")
    .replace(/(\d)\s*\/\s*(\d)/g, "$1 gedeeld door $2")
    .replace(/²/g, " kwadraat")
    .replace(/³/g, " tot de derde")
    .replace(/√/g, "wortel ")
    .replace(/[−–]/g, " min ")
    .replace(/×/g, " maal ")
    .replace(/÷/g, " gedeeld door ")
    .replace(/\bbv\./gi, "bijvoorbeeld")
    .replace(/\bvb\./gi, "voorbeeld")
    .replace(/\.{2,}|…/g, " ... ")
    .replace(/_{2,}/g, " ... ")
    .replace(/\p{Extended_Pictographic}/gu, "")
    .replace(/\s+/g, " ")
    .trim();
}

export function Voorleesknop({
  tekst,
  label = "Lees voor",
}: {
  tekst: string;
  label?: string;
}) {
  const [kan, setKan] = useState(false);
  const [bezig, setBezig] = useState(false);

  useEffect(() => {
    if (typeof window === "undefined" || !("speechSynthesis" in window)) return;
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setKan(true);
    // Sommige browsers laden de stemmen pas later in.
    window.speechSynthesis.getVoices();
    return () => window.speechSynthesis.cancel();
  }, []);

  if (!kan) return null;

  const lees = () => {
    const spraak = window.speechSynthesis;
    spraak.cancel();
    if (bezig) {
      setBezig(false);
      return;
    }
    const zin = new SpeechSynthesisUtterance(alsSpreektekst(tekst));
    const stem = kiesStem(spraak.getVoices());
    if (stem) zin.voice = stem;
    zin.lang = stem?.lang ?? "nl-BE";
    zin.rate = 0.95;
    zin.onend = () => setBezig(false);
    zin.onerror = () => setBezig(false);
    setBezig(true);
    spraak.speak(zin);
  };

  return (
    <button
      type="button"
      onClick={lees}
      aria-label={bezig ? "Stop met voorlezen" : label}
      className="inline-flex items-center gap-1.5 rounded-full border border-border bg-paper px-3 py-1 text-xs text-ink-dim transition hover:border-forest hover:text-ink"
    >
      <span aria-hidden>{bezig ? "⏹" : "🔊"}</span> {bezig ? "Stop" : label}
    </button>
  );
}
