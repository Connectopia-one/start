"use client";

import { useMemo, useState, type ChangeEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { maakBulkLeerstofUploadUrl, registreerBulkLeerstof, verwijderLeerstof } from "./actions";
import { NIVEAUS } from "@/lib/niveaus";

export type Hoofdstuk = { id: string; titel: string; niveau: string; volgnummer: number };
export type Vak = { id: string; naam: string; hoofdstukken: Hoofdstuk[] };
export type Bundel = { id: string; hoofdstuk_id: string; titel: string };

type Rij = {
  bestand: File;
  hoofdstukId: string;
  titel: string;
  /* Vervangt deze bundel wat er al bij het hoofdstuk stond? Staat aan zodra er
     al iets staat: een nieuwe versie uploaden is veel vaker de bedoeling dan
     twee bundels naast elkaar willen. */
  vervang: boolean;
  status: "wacht" | "bezig" | "klaar" | "fout";
  melding?: string;
};

/* Maakt van een bestandsnaam of hoofdstuktitel losse woorden, zonder accenten. */
function woorden(tekst: string): string[] {
  return tekst
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/\.[a-z0-9]+$/, "")
    .replace(/[^a-z0-9]+/g, " ")
    .split(" ")
    .filter((w) => w.length >= 3);
}

/*
  Zoekt bij een bestandsnaam het hoofdstuk dat er het best bij past.
  Elk woord dat in allebei voorkomt telt mee; staat de hele titel in de
  bestandsnaam, dan telt dat extra zwaar.
*/
function raadHoofdstuk(bestandsnaam: string, hoofdstukken: Hoofdstuk[]): string {
  const uitNaam = woorden(bestandsnaam);
  const plat = uitNaam.join(" ");
  let beste = "";
  let besteScore = 0;
  let evenGoed = 0;

  for (const h of hoofdstukken) {
    const uitTitel = woorden(h.titel);
    if (uitTitel.length === 0) continue;
    let score = uitTitel.filter((w) => uitNaam.includes(w)).length;
    if (plat.includes(uitTitel.join(" "))) score += 3;
    if (score > besteScore) {
      besteScore = score;
      beste = h.id;
      evenGoed = 1;
    } else if (score === besteScore && score > 0) {
      evenGoed++;
    }
  }

  // Passen er twee even goed — bijvoorbeeld een hoofdstuk met dezelfde titel
  // in twee categorieën — dan kiezen we niets. Liever zelf laten kiezen dan
  // de bundel stilletjes bij het verkeerde hoofdstuk zetten.
  return evenGoed === 1 ? beste : "";
}

/* "breuken-en-kommagetallen.pdf" wordt "Breuken en kommagetallen". */
function titelUitBestandsnaam(bestandsnaam: string): string {
  const kaal = bestandsnaam.replace(/\.[a-z0-9]+$/i, "").replace(/[_-]+/g, " ").trim();
  return kaal.charAt(0).toUpperCase() + kaal.slice(1);
}

function niveauLabel(niveau: string): string {
  const n = NIVEAUS.find((x) => x.slug === niveau);
  return n ? `${n.emoji} ${n.naam}` : niveau;
}

export function BulkLeerstofForm({ vakken, bundels }: { vakken: Vak[]; bundels: Bundel[] }) {
  const router = useRouter();
  const [vakId, setVakId] = useState(vakken[0]?.id ?? "");
  const [niveau, setNiveau] = useState("");
  const [rijen, setRijen] = useState<Rij[]>([]);
  const [bezig, setBezig] = useState(false);
  const [wisBezig, setWisBezig] = useState("");

  /* Wat staat er al per hoofdstuk? */
  const bundelsPerHoofdstuk = useMemo(() => {
    const kaart = new Map<string, Bundel[]>();
    for (const b of bundels) {
      kaart.set(b.hoofdstuk_id, [...(kaart.get(b.hoofdstuk_id) ?? []), b]);
    }
    return kaart;
  }, [bundels]);

  /* De categorieën waarin dit vak effectief hoofdstukken heeft. */
  const niveausVanVak = useMemo(() => {
    const vak = vakken.find((v) => v.id === vakId);
    if (!vak) return [];
    const aanwezig = new Set(vak.hoofdstukken.map((h) => h.niveau));
    return NIVEAUS.filter((n) => aanwezig.has(n.slug));
  }, [vakId, vakken]);

  const hoofdstukken = useMemo(() => {
    const vak = vakken.find((v) => v.id === vakId);
    if (!vak) return [];
    const volgorde: string[] = NIVEAUS.map((n) => n.slug);
    return vak.hoofdstukken
      .filter((h) => !niveau || h.niveau === niveau)
      .slice()
      .sort(
        (a, b) =>
          volgorde.indexOf(a.niveau) - volgorde.indexOf(b.niveau) || a.volgnummer - b.volgnummer,
      );
  }, [vakId, niveau, vakken]);

  function kiesBestanden(e: ChangeEvent<HTMLInputElement>) {
    const gekozen = Array.from(e.target.files ?? []);
    setRijen(
      gekozen.map((bestand) => {
        const hoofdstukId = raadHoofdstuk(bestand.name, hoofdstukken);
        return {
          bestand,
          hoofdstukId,
          titel: titelUitBestandsnaam(bestand.name),
          vervang: (bundelsPerHoofdstuk.get(hoofdstukId)?.length ?? 0) > 0,
          status: "wacht" as const,
        };
      }),
    );
  }

  function pasAan(index: number, wijziging: Partial<Rij>) {
    setRijen((oud) => oud.map((r, i) => (i === index ? { ...r, ...wijziging } : r)));
  }

  async function uploadAlles() {
    setBezig(true);
    const supabase = createClient();

    for (let i = 0; i < rijen.length; i++) {
      const rij = rijen[i];
      if (rij.status === "klaar") continue;

      if (!rij.hoofdstukId) {
        pasAan(i, { status: "fout", melding: "Kies eerst een hoofdstuk." });
        continue;
      }
      if (!rij.titel.trim()) {
        pasAan(i, { status: "fout", melding: "Vul een titel in." });
        continue;
      }

      pasAan(i, { status: "bezig", melding: undefined });
      try {
        const { path, token } = await maakBulkLeerstofUploadUrl(rij.hoofdstukId, rij.bestand.name);
        const { error } = await supabase.storage
          .from("leerstof")
          .uploadToSignedUrl(path, token, rij.bestand);
        if (error) throw new Error(error.message);

        await registreerBulkLeerstof({
          hoofdstukId: rij.hoofdstukId,
          titel: rij.titel.trim(),
          bestandspad: path,
          vervang: rij.vervang,
        });
        pasAan(i, { status: "klaar", melding: undefined });
      } catch (err) {
        pasAan(i, {
          status: "fout",
          melding: err instanceof Error ? err.message : "Er ging iets mis.",
        });
      }
    }

    setBezig(false);
    router.refresh();
  }

  function alBij(hoofdstukId: string): Bundel[] {
    return hoofdstukId ? bundelsPerHoofdstuk.get(hoofdstukId) ?? [] : [];
  }

  const nogTeDoen = rijen.filter((r) => r.status !== "klaar").length;
  const klaar = rijen.filter((r) => r.status === "klaar").length;

  return (
    <div className="mt-6 space-y-6">
      <div className="space-y-1.5">
        <label htmlFor="vak" className="text-sm font-medium text-ink">
          1. Kies het vak
        </label>
        <select
          id="vak"
          value={vakId}
          onChange={(e) => {
            setVakId(e.target.value);
            setNiveau("");
            setRijen([]);
          }}
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        >
          {vakken.map((v) => (
            <option key={v.id} value={v.id}>
              {v.naam}
            </option>
          ))}
        </select>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="niveau" className="text-sm font-medium text-ink">
          2. Kies de categorie
        </label>
        <select
          id="niveau"
          value={niveau}
          onChange={(e) => {
            setNiveau(e.target.value);
            setRijen([]);
          }}
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        >
          <option value="">Alle categorieën</option>
          {niveausVanVak.map((n) => (
            <option key={n.slug} value={n.slug}>
              {n.emoji} {n.naam} — {n.omschrijving}
            </option>
          ))}
        </select>
        <p className="text-xs text-ink-dim">
          Heeft dit vak in meerdere categorieën een hoofdstuk met dezelfde titel, kies dan hier de
          juiste. Anders kan een bundel bij het verkeerde hoofdstuk belanden.
        </p>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="bestanden" className="text-sm font-medium text-ink">
          3. Kies alle pdf&apos;s tegelijk
        </label>
        <input
          id="bestanden"
          type="file"
          /* Ook de extensie meegeven: op sommige computers herkent de browser
             het type van een pdf niet, en dan blijven de bestanden grijs staan
             in het keuzevenster. */
          accept=".pdf,application/pdf"
          multiple
          onChange={kiesBestanden}
          className="block w-full cursor-pointer text-sm text-ink-dim file:mr-3 file:cursor-pointer file:rounded-md file:border-0 file:bg-forest file:px-4 file:py-2 file:text-sm file:font-medium file:text-white hover:file:bg-forest-dark"
        />
        <p className="text-xs text-ink-dim">
          Noem je bestanden naar het hoofdstuk, bijvoorbeeld <em>getallenkennis.pdf</em>, dan zet
          het platform er zelf het juiste hoofdstuk bij.
        </p>
      </div>

      {rijen.length > 0 && (
        <div className="space-y-3">
          <p className="text-sm font-medium text-ink">4. Kijk de koppeling na en pas aan waar nodig</p>

          {rijen.map((rij, i) => (
            <div
              key={rij.bestand.name + i}
              className="rounded-lg border border-border bg-surface p-3"
            >
              <div className="flex items-start justify-between gap-3">
                <p className="truncate text-sm font-medium text-ink">{rij.bestand.name}</p>
                <span className="shrink-0 text-xs text-ink-dim">
                  {rij.status === "klaar" && "✓ geüpload"}
                  {rij.status === "bezig" && "bezig…"}
                  {rij.status === "fout" && <span className="text-danger">mislukt</span>}
                  {rij.status === "wacht" && `${Math.round(rij.bestand.size / 1024)} kB`}
                </span>
              </div>

              {rij.melding && <p className="mt-1 text-xs text-danger">{rij.melding}</p>}

              <div className="mt-2 grid gap-2 sm:grid-cols-2">
                <select
                  value={rij.hoofdstukId}
                  onChange={(e) =>
                    pasAan(i, {
                      hoofdstukId: e.target.value,
                      vervang: (bundelsPerHoofdstuk.get(e.target.value)?.length ?? 0) > 0,
                    })
                  }
                  disabled={rij.status === "klaar"}
                  className="rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest disabled:opacity-60"
                >
                  <option value="">— kies een hoofdstuk —</option>
                  {hoofdstukken.map((h) => (
                    <option key={h.id} value={h.id}>
                      {niveauLabel(h.niveau)} — {h.titel}
                    </option>
                  ))}
                </select>

                <input
                  value={rij.titel}
                  onChange={(e) => pasAan(i, { titel: e.target.value })}
                  disabled={rij.status === "klaar"}
                  placeholder="Titel zoals het kind ze ziet"
                  className="rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest disabled:opacity-60"
                />
              </div>

              {/* Staat er al een bundel bij dit hoofdstuk, zeg dat dan meteen —
                  anders zet je er ongemerkt een tweede naast. */}
              {rij.status !== "klaar" && alBij(rij.hoofdstukId).length > 0 && (
                <div className="mt-2 rounded-md border border-amber/40 bg-amber/10 px-3 py-2">
                  <p className="text-xs text-ink">
                    Hier staat al:{" "}
                    {alBij(rij.hoofdstukId)
                      .map((b) => b.titel)
                      .join(", ")}
                  </p>
                  <label className="mt-1.5 flex items-start gap-2 text-xs text-ink">
                    <input
                      type="checkbox"
                      checked={rij.vervang}
                      onChange={(e) => pasAan(i, { vervang: e.target.checked })}
                      className="mt-0.5 accent-forest"
                    />
                    <span>
                      De oude vervangen door deze. Vink uit als je ze allebei wil laten staan.
                    </span>
                  </label>
                </div>
              )}
            </div>
          ))}

          <div className="flex items-center gap-3">
            <button
              type="button"
              onClick={uploadAlles}
              disabled={bezig || nogTeDoen === 0}
              className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-60"
            >
              {bezig ? "Bezig met uploaden…" : `Alles uploaden (${nogTeDoen})`}
            </button>
            {klaar > 0 && (
              <p className="text-sm text-forest-dark">
                {klaar} van de {rijen.length} staan erop.
              </p>
            )}
          </div>
        </div>
      )}

      {/* Wat er nu bij dit vak staat, zodat je een verouderde bundel ook gewoon
          kan weghalen zonder er een nieuwe voor in de plaats te zetten. */}
      {hoofdstukken.some((h) => alBij(h.id).length > 0) && (
        <div className="space-y-2 border-t border-border pt-5">
          <p className="text-sm font-medium text-ink">Wat er nu al bij dit vak staat</p>
          {hoofdstukken.map((h) =>
            alBij(h.id).map((b) => (
              <div
                key={b.id}
                className="flex items-center justify-between gap-3 rounded-lg border border-border bg-surface px-3 py-2"
              >
                <p className="min-w-0 text-sm text-ink">
                  <span className="text-ink-dim">{h.titel}</span> — {b.titel}
                </p>
                <button
                  type="button"
                  disabled={wisBezig === b.id}
                  onClick={async () => {
                    setWisBezig(b.id);
                    try {
                      await verwijderLeerstof(b.id);
                      router.refresh();
                    } finally {
                      setWisBezig("");
                    }
                  }}
                  className="shrink-0 rounded-md border border-border px-3 py-1.5 text-xs text-danger hover:bg-danger/10 disabled:opacity-60"
                >
                  {wisBezig === b.id ? "bezig…" : "Weghalen"}
                </button>
              </div>
            )),
          )}
        </div>
      )}
    </div>
  );
}
