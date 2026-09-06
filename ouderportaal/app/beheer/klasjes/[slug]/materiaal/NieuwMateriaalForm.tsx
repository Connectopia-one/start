"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { maakMateriaalUploadUrl, registreerMateriaal } from "./actions";

type Type = "pdf" | "link" | "aankondiging";

export function NieuwMateriaalForm({ klasjeId, slug }: { klasjeId: string; slug: string }) {
  const router = useRouter();
  const [type, setType] = useState<Type>("pdf");
  const [status, setStatus] = useState<"idle" | "bezig" | "fout">("idle");
  const [fout, setFout] = useState<string | null>(null);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setStatus("bezig");
    setFout(null);

    const form = e.currentTarget;
    const data = new FormData(form);
    const titel = String(data.get("titel") || "").trim();

    try {
      if (!titel) throw new Error("Vul een titel in.");

      if (type === "pdf") {
        const bestand = data.get("bestand");
        if (!(bestand instanceof File) || bestand.size === 0) {
          throw new Error("Kies een PDF-bestand om te uploaden.");
        }
        const { path, token } = await maakMateriaalUploadUrl(klasjeId, bestand.name);
        const supabase = createClient();
        const { error: uploadError } = await supabase.storage
          .from("materialen")
          .uploadToSignedUrl(path, token, bestand);
        if (uploadError) throw new Error("Uploaden mislukt: " + uploadError.message);

        await registreerMateriaal({ klasjeId, slug, type: "pdf", titel, bestandspad: path });
      } else if (type === "link") {
        const link = String(data.get("link") || "").trim();
        if (!link) throw new Error("Vul een link in.");
        await registreerMateriaal({ klasjeId, slug, type: "link", titel, inhoud: link });
      } else {
        const tekst = String(data.get("tekst") || "").trim();
        if (!tekst) throw new Error("Vul een tekst in.");
        await registreerMateriaal({ klasjeId, slug, type: "aankondiging", titel, inhoud: tekst });
      }

      form.reset();
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
        <label htmlFor="titel" className="text-sm font-medium text-ink">
          Titel
        </label>
        <input
          id="titel"
          name="titel"
          required
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
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
          <label className="flex items-center gap-1.5">
            <input
              type="radio"
              name="type"
              value="aankondiging"
              checked={type === "aankondiging"}
              onChange={() => setType("aankondiging")}
            />{" "}
            Aankondiging
          </label>
        </div>
      </fieldset>

      {type === "pdf" && (
        <div className="space-y-1.5">
          <label htmlFor="bestand" className="text-sm font-medium text-ink">
            PDF-bestand
          </label>
          <input id="bestand" name="bestand" type="file" accept="application/pdf" className="w-full text-sm" />
        </div>
      )}
      {type === "link" && (
        <div className="space-y-1.5">
          <label htmlFor="link" className="text-sm font-medium text-ink">
            Link
          </label>
          <input
            id="link"
            name="link"
            type="url"
            placeholder="https://..."
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
      )}
      {type === "aankondiging" && (
        <div className="space-y-1.5">
          <label htmlFor="tekst" className="text-sm font-medium text-ink">
            Tekst
          </label>
          <textarea
            id="tekst"
            name="tekst"
            rows={3}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
      )}

      <button
        type="submit"
        disabled={status === "bezig"}
        className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-60"
      >
        {status === "bezig" ? "Bezig met uploaden…" : "Toevoegen"}
      </button>
    </form>
  );
}
