"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { materiaalGroepSuggesties } from "@/inhoud/materiaal";
import { maakMateriaalUploadUrl, registreerMateriaal } from "./actions";

type Type = "link" | "pdf";
type Soort = "links" | "documenten" | "filmpjes";
type Schoolniveau = "lager" | "middelbaar" | "iedereen";

const veld =
  "w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest";

/*
  Sinds 9 november 2026 kies je bij elk item onder welke knop van de Leuke
  extra's het komt (links, documenten of filmpjes) en voor wie het is. De
  kopje blijft: daarmee verdeel je binnen een schoolniveau, bv. "Materiaal en
  oefensites" en "Studie- en oefentips".
*/
export function NieuwMateriaalForm({ groepen }: { groepen: string[] }) {
  const router = useRouter();
  const [type, setType] = useState<Type>("link");
  const [soort, setSoort] = useState<Soort>("links");
  /* Kopjes die al gebruikt zijn, aangevuld met de voorstellen uit inhoud/materiaal.ts. */
  const voorstellen = Array.from(
    new Set([...materiaalGroepSuggesties, ...groepen]),
  );
  const [status, setStatus] = useState<"idle" | "bezig" | "fout">("idle");
  const [fout, setFout] = useState<string | null>(null);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setStatus("bezig");
    setFout(null);

    const form = e.currentTarget;
    const data = new FormData(form);
    const titel = String(data.get("titel") || "").trim();
    const groep = String(data.get("groep") || "").trim();
    const schoolniveau = String(
      data.get("schoolniveau") || "iedereen",
    ) as Schoolniveau;
    const omschrijving = String(data.get("omschrijving") || "").trim();

    try {
      if (!titel) throw new Error("Vul een titel in.");

      if (type === "pdf") {
        const bestand = data.get("bestand");
        if (!(bestand instanceof File) || bestand.size === 0) {
          throw new Error("Kies een PDF-bestand om te uploaden.");
        }
        const { path, token } = await maakMateriaalUploadUrl(bestand.name);
        const supabase = createClient();
        const { error: uploadError } = await supabase.storage
          .from("materiaal")
          .uploadToSignedUrl(path, token, bestand);
        if (uploadError)
          throw new Error("Uploaden mislukt: " + uploadError.message);

        await registreerMateriaal({
          groep,
          type: "pdf",
          titel,
          bestandspad: path,
          omschrijving,
          soort,
          schoolniveau,
        });
      } else {
        const link = String(data.get("link") || "").trim();
        if (!link) throw new Error("Vul een link in.");
        if (!/^https?:\/\//i.test(link)) {
          throw new Error(
            "Een link begint met https:// — plak het volledige adres uit je browser.",
          );
        }
        await registreerMateriaal({
          groep,
          type: "link",
          titel,
          link,
          omschrijving,
          soort,
          schoolniveau,
        });
      }

      form.reset();
      setType("link");
      setSoort("links");
      setStatus("idle");
      router.refresh();
    } catch (err) {
      setStatus("fout");
      setFout(err instanceof Error ? err.message : "Er ging iets mis.");
    }
  }

  return (
    <form onSubmit={onSubmit} className="mt-4 space-y-4">
      {fout && (
        <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
          {fout}
        </p>
      )}

      <div className="space-y-1.5">
        <label htmlFor="titel" className="text-sm font-medium text-ink">
          Titel
        </label>
        <input id="titel" name="titel" required className={veld} />
      </div>

      <fieldset className="space-y-2">
        <legend className="text-sm font-medium text-ink">Type</legend>
        <div className="flex gap-4 text-sm">
          <label className="flex items-center gap-1.5">
            <input
              type="radio"
              name="type"
              value="link"
              checked={type === "link"}
              onChange={() => {
                setType("link");
                if (soort === "documenten") setSoort("links");
              }}
            />{" "}
            Link
          </label>
          <label className="flex items-center gap-1.5">
            <input
              type="radio"
              name="type"
              value="pdf"
              checked={type === "pdf"}
              onChange={() => {
                setType("pdf");
                setSoort("documenten");
              }}
            />{" "}
            PDF
          </label>
        </div>
      </fieldset>

      {type === "link" ? (
        <div className="space-y-1.5">
          <label htmlFor="link" className="text-sm font-medium text-ink">
            Link
          </label>
          <input
            id="link"
            name="link"
            type="url"
            placeholder="https://..."
            className={veld}
          />
        </div>
      ) : (
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
      )}

      <div className="space-y-1.5">
        <label htmlFor="soort" className="text-sm font-medium text-ink">
          Onder welke knop?
        </label>
        <select
          id="soort"
          name="soort"
          value={soort}
          onChange={(e) => setSoort(e.target.value as Soort)}
          className={veld}
        >
          <option value="links">🔗 Leuke links</option>
          <option value="documenten">🖨️ Afdrukbare documenten</option>
          <option value="filmpjes">🎬 Leuke filmpjes</option>
        </select>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="schoolniveau" className="text-sm font-medium text-ink">
          Voor wie?
        </label>
        <select
          id="schoolniveau"
          name="schoolniveau"
          defaultValue="lager"
          className={veld}
        >
          <option value="lager">Lagere school (Basis en Start)</option>
          <option value="middelbaar">
            Middelbare school (Spark, Boost en Beyond)
          </option>
          <option value="iedereen">Voor iedereen</option>
        </select>
        <p className="text-xs text-ink-dim">
          Zet in de titel of de omschrijving gerust welk leerjaar of welk vak,
          bv. &quot;5de en 6de leerjaar&quot;.
        </p>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="groep" className="text-sm font-medium text-ink">
          Onder welk kopje?{" "}
          <span className="font-normal text-ink-dim">(mag je leeg laten)</span>
        </label>
        <input
          id="groep"
          name="groep"
          list="materiaal-groepen"
          className={veld}
        />
        <datalist id="materiaal-groepen">
          {voorstellen.map((g) => (
            <option key={g} value={g} />
          ))}
        </datalist>
        <p className="text-xs text-ink-dim">
          Kies er een uit de lijst of typ een nieuw kopje. Het verschijnt
          vanzelf op de pagina.
        </p>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="omschrijving" className="text-sm font-medium text-ink">
          Omschrijving{" "}
          <span className="font-normal text-ink-dim">(mag je leeg laten)</span>
        </label>
        <textarea
          id="omschrijving"
          name="omschrijving"
          rows={2}
          className={veld}
        />
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
