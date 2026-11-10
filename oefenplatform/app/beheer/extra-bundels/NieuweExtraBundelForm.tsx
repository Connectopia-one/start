"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { extraSoorten } from "@/lib/extraBundels";
import { maakExtraBundelUploadUrl, registreerExtraBundel } from "./actions";

const veld =
  "w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest";

export type VakKeuze = { id: string; naam: string; niveaus: { slug: string; naam: string }[] };

export function NieuweExtraBundelForm({ vakken }: { vakken: VakKeuze[] }) {
  const router = useRouter();
  const [vakId, setVakId] = useState(vakken[0]?.id ?? "");
  const [status, setStatus] = useState<"idle" | "bezig" | "fout" | "klaar">("idle");
  const [fout, setFout] = useState<string | null>(null);
  const niveaus = vakken.find((v) => v.id === vakId)?.niveaus ?? [];

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setStatus("bezig");
    setFout(null);
    const form = e.currentTarget;
    const data = new FormData(form);
    try {
      const titel = String(data.get("titel") || "").trim();
      if (!titel) throw new Error("Vul een titel in.");
      const bestand = data.get("bestand");
      if (!(bestand instanceof File) || bestand.size === 0) {
        throw new Error("Kies een pdf om te uploaden.");
      }
      const { path, token } = await maakExtraBundelUploadUrl(bestand.name);
      const supabase = createClient();
      const { error } = await supabase.storage
        .from("extrabundels")
        .uploadToSignedUrl(path, token, bestand);
      if (error) throw new Error("Uploaden mislukt: " + error.message);

      await registreerExtraBundel({
        vakId,
        niveau: String(data.get("niveau") || ""),
        soort: String(data.get("soort") || "examen"),
        titel,
        omschrijving: String(data.get("omschrijving") || ""),
        bestandspad: path,
        verbetersleutel: data.get("verbetersleutel") === "on",
      });
      // Vak, categorie en soort laten staan: zo zet je versie A, B en C
      // snel na elkaar op.
      (form.elements.namedItem("titel") as HTMLInputElement).value = "";
      (form.elements.namedItem("bestand") as HTMLInputElement).value = "";
      setStatus("klaar");
      router.refresh();
    } catch (err) {
      setStatus("fout");
      setFout(err instanceof Error ? err.message : "Er ging iets mis.");
    }
  }

  return (
    <form onSubmit={onSubmit} className="mt-4 space-y-4">
      {fout && (
        <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>
      )}
      {status === "klaar" && (
        <p className="rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">
          Opgeladen. Je kan meteen de volgende zetten.
        </p>
      )}

      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <label htmlFor="vak" className="text-sm font-medium text-ink">Vak</label>
          <select id="vak" value={vakId} onChange={(e) => setVakId(e.target.value)} className={veld}>
            {vakken.map((v) => (
              <option key={v.id} value={v.id}>{v.naam}</option>
            ))}
          </select>
        </div>
        <div className="space-y-1.5">
          <label htmlFor="niveau" className="text-sm font-medium text-ink">Categorie</label>
          <select id="niveau" name="niveau" key={vakId} className={veld}>
            {niveaus.map((n) => (
              <option key={n.slug} value={n.slug}>{n.naam}</option>
            ))}
          </select>
        </div>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="soort" className="text-sm font-medium text-ink">Soort</label>
        <select id="soort" name="soort" className={veld}>
          {extraSoorten.map((s) => (
            <option key={s.slug} value={s.slug}>{s.icoon} {s.naam}</option>
          ))}
        </select>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="titel" className="text-sm font-medium text-ink">Titel</label>
        <input id="titel" name="titel" required placeholder="bv. Examen versie A" className={veld} />
      </div>

      <div className="space-y-1.5">
        <label htmlFor="omschrijving" className="text-sm font-medium text-ink">
          Omschrijving <span className="font-normal text-ink-dim">(mag leeg)</span>
        </label>
        <input id="omschrijving" name="omschrijving" placeholder="bv. 40 aankruisvragen over het hele vak" className={veld} />
      </div>

      <label className="flex items-start gap-2 text-sm text-ink">
        <input type="checkbox" name="verbetersleutel" className="mt-1" />
        <span>
          Dit is een verbetersleutel
          <span className="block text-ink-dim">
            Ouders openen hem enkel met hun ouderpincode, zodat kinderen op het
            account van hun ouder de oplossingen niet zien. Jij en de begeleiders
            hebben geen pincode nodig.
          </span>
        </span>
      </label>

      <div className="space-y-1.5">
        <label htmlFor="bestand" className="text-sm font-medium text-ink">Pdf</label>
        <input id="bestand" name="bestand" type="file" accept="application/pdf" required className="block text-sm" />
      </div>

      <button
        type="submit"
        disabled={status === "bezig" || !vakken.length}
        className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-60"
      >
        {status === "bezig" ? "Bezig met opladen…" : "Bundel toevoegen"}
      </button>
    </form>
  );
}
