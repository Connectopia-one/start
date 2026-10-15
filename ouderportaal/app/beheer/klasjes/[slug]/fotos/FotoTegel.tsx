"use client";

import { useEffect, useRef, useState, type ReactNode } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { dngNaarJpeg, draaiFoto, heicNaarJpeg, soortVanInhoud } from "@/lib/beeldOmzetten";
import { maakFotoUploadUrl, vervangFotoBestand } from "./actions";

/*
  Eén foto in het beheer. Toont de browser hem niet, dan verschijnt er een
  knop die het bestand ophaalt en nakijkt. Is het een HEIC-foto van een
  iPhone of een RAW-foto (DNG), dan wordt hij omgezet naar JPEG en vervangen. Is het iets anders,
  dan zegt de tegel wat er in het bestand zit, zodat we verder kunnen zoeken.
*/
export function FotoTegel({
  id,
  url,
  bestandspad,
  bijschrift,
  slug,
  children,
}: {
  id: string;
  url: string;
  bestandspad: string;
  bijschrift: string | null;
  slug: string;
  children?: ReactNode;
}) {
  const router = useRouter();
  const beeld = useRef<HTMLImageElement>(null);
  const [gebroken, setGebroken] = useState(false);
  const [bezig, setBezig] = useState(false);
  const [melding, setMelding] = useState<string | null>(null);

  /* Een fout tijdens het laden kan vallen vóór React meeluistert. */
  useEffect(() => {
    const img = beeld.current;
    if (img && img.complete && img.naturalWidth === 0) setGebroken(true);
  }, []);

  /* Laadt het nieuwe bestand op en zet het in de plaats van het oude. */
  async function vervang(jpeg: File) {
    const klasjeId = bestandspad.split("/")[0];
    const { path, token } = await maakFotoUploadUrl(klasjeId, jpeg.name);
    const supabase = createClient();
    const { error } = await supabase.storage.from("fotos").uploadToSignedUrl(path, token, jpeg);
    if (error) throw new Error(`Opladen mislukt: ${error.message}`);

    const uitkomst = await vervangFotoBestand({ id, slug, oudPad: bestandspad, nieuwPad: path });
    if (!uitkomst.gelukt) throw new Error(uitkomst.bericht);
    router.refresh();
  }

  async function draai(richting: "links" | "rechts") {
    setBezig(true);
    setMelding(null);
    try {
      const antwoord = await fetch(url);
      if (!antwoord.ok) throw new Error(`De opslag gaf fout ${antwoord.status}.`);
      const naam = bestandspad.split("/").pop() ?? "foto";
      await vervang(await draaiFoto(await antwoord.blob(), naam, richting));
    } catch (err) {
      setMelding(err instanceof Error ? err.message : "Er ging iets mis.");
    } finally {
      setBezig(false);
    }
  }

  async function herstel() {
    setBezig(true);
    setMelding(null);
    try {
      const antwoord = await fetch(url);
      if (!antwoord.ok) {
        const tekst = (await antwoord.text()).slice(0, 200);
        throw new Error(`De opslag gaf fout ${antwoord.status}: ${tekst}`);
      }
      const blob = await antwoord.blob();
      const soort = await soortVanInhoud(blob);

      if (soort !== "heic" && soort !== "dng") {
        const kb = Math.round(blob.size / 1024);
        throw new Error(
          `Dit formaat kan ik niet omzetten. Formaat: ${soort}, ${kb} kB, opgegeven als "${blob.type || "leeg"}", bestand ${bestandspad.split("/").pop()}.`,
        );
      }

      const naam = bestandspad.split("/").pop() ?? "foto";
      const jpeg = soort === "dng" ? await dngNaarJpeg(blob, naam) : await heicNaarJpeg(blob, naam);
      await vervang(jpeg);
    } catch (err) {
      setMelding(err instanceof Error ? err.message : "Er ging iets mis.");
    } finally {
      setBezig(false);
    }
  }

  return (
    <div className="overflow-hidden rounded-lg border border-border bg-surface">
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        ref={beeld}
        src={url}
        alt={bijschrift ?? ""}
        onError={() => setGebroken(true)}
        onLoad={() => setGebroken(false)}
        className="aspect-square w-full object-cover"
      />
      {gebroken && (
        <div className="space-y-1 px-2 pt-2 text-xs">
          <p className="text-ink-dim">Deze foto toont niet in deze browser.</p>
          <button
            type="button"
            onClick={herstel}
            disabled={bezig}
            className="rounded-md bg-forest px-2 py-1 font-medium text-white hover:bg-forest-dark disabled:opacity-60"
          >
            {bezig ? "Bezig…" : "Nakijken en herstellen"}
          </button>
          {melding && <p className="text-danger">{melding}</p>}
        </div>
      )}
      {!gebroken && (
        <div className="flex items-center gap-2 px-2 pt-2 text-xs">
          <span className="text-ink-dim">Draaien:</span>
          <button
            type="button"
            onClick={() => draai("links")}
            disabled={bezig}
            aria-label="Een kwartslag naar links draaien"
            className="rounded-md border border-border px-2 py-0.5 text-ink hover:bg-paper disabled:opacity-60"
          >
            ↺
          </button>
          <button
            type="button"
            onClick={() => draai("rechts")}
            disabled={bezig}
            aria-label="Een kwartslag naar rechts draaien"
            className="rounded-md border border-border px-2 py-0.5 text-ink hover:bg-paper disabled:opacity-60"
          >
            ↻
          </button>
          {bezig && <span className="text-ink-dim">Bezig…</span>}
          {melding && <span className="text-danger">{melding}</span>}
        </div>
      )}
      {children}
    </div>
  );
}
