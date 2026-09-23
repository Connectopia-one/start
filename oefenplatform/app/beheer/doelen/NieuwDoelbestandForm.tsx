"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { NIVEAUS } from "@/lib/niveaus";
import { doelenBlokken } from "@/inhoud/onderwijsdoelen";
import { maakDoelUploadUrl, registreerDoelbestand } from "./actions";

type Type = "link" | "pdf";

const veld =
  "w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest";

export function NieuwDoelbestandForm() {
  const router = useRouter();
  const [niveau, setNiveau] = useState<string>(NIVEAUS[0]?.slug ?? "start");
  const [type, setType] = useState<Type>("pdf");
  const [status, setStatus] = useState<"idle" | "bezig" | "fout">("idle");
  const [fout, setFout] = useState<string | null>(null);

  /* De vakken die op /onderwijsdoelen bij dit niveau staan, zodat het document
     onder het juiste kopje terechtkomt. Een eigen vak typen mag ook. */
  const vakken = doelenBlokken.find((b) => b.slug === niveau)?.vakken ?? [];

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setStatus("bezig");
    setFout(null);

    const form = e.currentTarget;
    const data = new FormData(form);
    const titel = String(data.get("titel") || "").trim();
    const vak = String(data.get("vak") || "").trim();
    const geldigSinds = String(data.get("geldigSinds") || "").trim();
    const omschrijving = String(data.get("omschrijving") || "").trim();

    try {
      if (!titel) throw new Error("Vul een titel in.");

      if (type === "pdf") {
        const bestand = data.get("bestand");
        if (!(bestand instanceof File) || bestand.size === 0) {
          throw new Error("Kies een PDF-bestand om te uploaden.");
        }
        const { path, token } = await maakDoelUploadUrl(bestand.name);
        const supabase = createClient();
        const { error: uploadError } = await supabase.storage
          .from("materiaal")
          .uploadToSignedUrl(path, token, bestand);
        if (uploadError) throw new Error("Uploaden mislukt: " + uploadError.message);

        await registreerDoelbestand({
          niveau, vak, titel, type: "pdf", bestandspad: path, geldigSinds, omschrijving,
        });
      } else {
        const link = String(data.get("link") || "").trim();
        if (!link) throw new Error("Vul een link in.");
        if (!/^https?:\/\//i.test(link)) {
          throw new Error("Een link begint met https:// — plak het volledige adres uit je browser.");
        }
        await registreerDoelbestand({
          niveau, vak, titel, type: "link", link, geldigSinds, omschrijving,
        });
      }

      form.reset();
      setType("pdf");
      setStatus("idle");
      router.refresh();
    } catch (err) {
      setStatus("fout");
      setFout(err instanceof Error ? err.message : "Er ging iets mis.");
    }
  }

  return (
    <form onSubmit={onSubmit} className="mt-4 space-y-4">
      {fout && <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}

      <div className="space-y-1.5">
        <label htmlFor="niveau" className="text-sm font-medium text-ink">
          Bij welk niveau?
        </label>
        <select
          id="niveau"
          value={niveau}
          onChange={(e) => setNiveau(e.target.value)}
          className={veld}
        >
          {NIVEAUS.map((n) => (
            <option key={n.slug} value={n.slug}>
              {n.emoji} {n.naam} — {n.omschrijving}
            </option>
          ))}
        </select>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="vak" className="text-sm font-medium text-ink">
          Bij welk vak? <span className="font-normal text-ink-dim">(mag je leeg laten)</span>
        </label>
        <input id="vak" name="vak" list="doelen-vakken" className={veld} />
        <datalist id="doelen-vakken">
          {vakken.map((v) => (
            <option key={v.naam} value={v.naam} />
          ))}
        </datalist>
        <p className="text-xs text-ink-dim">
          Laat je dit leeg, dan staat het document bovenaan bij het niveau zelf, en niet bij één
          bepaald vak.
        </p>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="titel" className="text-sm font-medium text-ink">
          Titel
        </label>
        <input
          id="titel"
          name="titel"
          required
          placeholder="Vakfiche wiskunde 1ste graad A-stroom"
          className={veld}
        />
      </div>

      <fieldset className="space-y-2">
        <legend className="text-sm font-medium text-ink">Type</legend>
        <div className="flex gap-4 text-sm">
          <label className="flex items-center gap-1.5">
            <input
              type="radio"
              name="type"
              value="pdf"
              checked={type === "pdf"}
              onChange={() => setType("pdf")}
            />{" "}
            PDF
          </label>
          <label className="flex items-center gap-1.5">
            <input
              type="radio"
              name="type"
              value="link"
              checked={type === "link"}
              onChange={() => setType("link")}
            />{" "}
            Link
          </label>
        </div>
      </fieldset>

      {type === "pdf" ? (
        <div className="space-y-1.5">
          <label htmlFor="bestand" className="text-sm font-medium text-ink">
            PDF-bestand
          </label>
          <input
            id="bestand"
            name="bestand"
            type="file"
            accept="application/pdf"
            className="w-full text-sm"
          />
        </div>
      ) : (
        <div className="space-y-1.5">
          <label htmlFor="link" className="text-sm font-medium text-ink">
            Link
          </label>
          <input id="link" name="link" type="url" placeholder="https://..." className={veld} />
        </div>
      )}

      <div className="space-y-1.5">
        <label htmlFor="geldigSinds" className="text-sm font-medium text-ink">
          Geldig sinds <span className="font-normal text-ink-dim">(mag je leeg laten)</span>
        </label>
        <input
          id="geldigSinds"
          name="geldigSinds"
          placeholder="1 september 2025"
          className={veld}
        />
        <p className="text-xs text-ink-dim">
          Komt op de pagina bij het document te staan, zodat een ouder ziet van wanneer deze
          versie is.
        </p>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="omschrijving" className="text-sm font-medium text-ink">
          Omschrijving <span className="font-normal text-ink-dim">(mag je leeg laten)</span>
        </label>
        <textarea id="omschrijving" name="omschrijving" rows={2} className={veld} />
      </div>

      <button
        type="submit"
        disabled={status === "bezig"}
        className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-60"
      >
        {status === "bezig" ? "Bezig…" : "Toevoegen"}
      </button>
    </form>
  );
}
