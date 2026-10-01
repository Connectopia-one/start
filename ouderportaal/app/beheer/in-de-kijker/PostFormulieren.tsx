"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { bewaarNieuwePost, maakBeeldUploadUrl, zetBeeld } from "./actions";

/*
  De twee formulieren van "In de kijker".

  Het beeld gaat rechtstreeks naar Supabase Storage, niet door een server
  action heen: zo blijft het buiten de limiet van ongeveer 4,5MB die Vercel
  op een gewoon verzoek zet. Dezelfde aanpak als bij de foto's van een klasje.
*/

const BAK = "social";

const KANALEN = [
  ["facebook", "Facebook"],
  ["instagram", "Instagram"],
  ["linkedin", "LinkedIn"],
  ["tiktok", "TikTok"],
  ["youtube", "YouTube"],
  ["anders", "Elders online"],
] as const;

const veld =
  "w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest";

async function laadBeeldOp(bestand: File) {
  const { pad, token } = await maakBeeldUploadUrl(bestand.name);
  const supabase = createClient();
  const { error } = await supabase.storage
    .from(BAK)
    .uploadToSignedUrl(pad, token, bestand);
  if (error) throw new Error(`Het beeld opladen mislukte: ${error.message}`);
  return pad;
}

function eersteBestand(data: FormData, naam: string): File | null {
  const bestand = data.get(naam);
  return bestand instanceof File && bestand.size > 0 ? bestand : null;
}

export function NieuwePostForm() {
  const router = useRouter();
  const [bezig, setBezig] = useState(false);
  const [fout, setFout] = useState<string | null>(null);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setBezig(true);
    setFout(null);

    const form = e.currentTarget;
    const data = new FormData(form);

    try {
      const bestand = eersteBestand(data, "beeld");
      const beeld = bestand ? await laadBeeldOp(bestand) : null;

      await bewaarNieuwePost({
        titel: String(data.get("titel") || "") || null,
        tekst: String(data.get("tekst") || ""),
        van: String(data.get("van") || ""),
        kanaal: String(data.get("kanaal") || "anders"),
        link: String(data.get("link") || ""),
        eigen: data.get("eigen") === "ja",
        beeld,
      });

      form.reset();
      setBezig(false);
      router.refresh();
    } catch (err) {
      setBezig(false);
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
        <label htmlFor="link" className="text-sm font-medium text-ink">
          De link naar het bericht
        </label>
        <input
          id="link"
          name="link"
          type="url"
          required
          placeholder="https://www.facebook.com/..."
          className={veld}
        />
        <p className="text-xs text-ink-dim">
          Het volledige adres van het bericht zelf, zoals het in je adresbalk
          staat als je het bericht opent.
        </p>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="tekst" className="text-sm font-medium text-ink">
          Wat er op het kaartje komt
        </label>
        <textarea id="tekst" name="tekst" rows={3} required className={veld} />
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <label htmlFor="van" className="text-sm font-medium text-ink">
            Van wie is het bericht?
          </label>
          <input
            id="van"
            name="van"
            required
            defaultValue="Connectopia"
            className={veld}
          />
        </div>
        <div className="space-y-1.5">
          <label htmlFor="kanaal" className="text-sm font-medium text-ink">
            Waar staat het?
          </label>
          <select
            id="kanaal"
            name="kanaal"
            defaultValue="facebook"
            className={veld}
          >
            {KANALEN.map(([sleutel, naam]) => (
              <option key={sleutel} value={sleutel}>
                {naam}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="titel" className="text-sm font-medium text-ink">
          Kop boven het kaartje (mag leeg blijven)
        </label>
        <input id="titel" name="titel" className={veld} />
      </div>

      <div className="space-y-1.5">
        <label htmlFor="beeld" className="text-sm font-medium text-ink">
          Een beeld erbij (mag leeg blijven)
        </label>
        <input
          id="beeld"
          name="beeld"
          type="file"
          accept="image/*"
          className="w-full text-sm"
        />
        <p className="text-xs text-ink-dim">
          Een schermafbeelding van het bericht of de foto die je erbij postte.
          Zonder beeld is het kaartje gewoon tekst.
        </p>
      </div>

      <label className="flex items-center gap-2 text-sm text-ink">
        <input
          type="checkbox"
          name="eigen"
          value="ja"
          defaultChecked
          className="h-4 w-4 rounded border-border"
        />
        Dit is een bericht van onszelf
      </label>

      <button
        type="submit"
        disabled={bezig}
        className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-60"
      >
        {bezig ? "Bezig…" : "Op de website zetten"}
      </button>
    </form>
  );
}

/* Een beeld bij een bericht dat er al staat, of een beeld vervangen. */
export function BeeldForm({
  id,
  heeftBeeld,
}: {
  id: string;
  heeftBeeld: boolean;
}) {
  const router = useRouter();
  const [bezig, setBezig] = useState(false);
  const [fout, setFout] = useState<string | null>(null);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setBezig(true);
    setFout(null);

    const form = e.currentTarget;
    const bestand = eersteBestand(new FormData(form), "beeld");
    if (!bestand) {
      setBezig(false);
      setFout("Kies eerst een beeld.");
      return;
    }

    try {
      const beeld = await laadBeeldOp(bestand);
      await zetBeeld({ id, beeld });
      form.reset();
      setBezig(false);
      router.refresh();
    } catch (err) {
      setBezig(false);
      setFout(err instanceof Error ? err.message : "Er ging iets mis.");
    }
  }

  return (
    <form onSubmit={onSubmit} className="mt-3 space-y-2">
      {fout && <p className="text-sm text-danger">{fout}</p>}
      <div className="flex flex-wrap items-center gap-2">
        <input
          name="beeld"
          type="file"
          accept="image/*"
          aria-label={heeftBeeld ? "Ander beeld kiezen" : "Een beeld kiezen"}
          className="text-sm"
        />
        <button
          type="submit"
          disabled={bezig}
          className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark disabled:opacity-60"
        >
          {bezig
            ? "Bezig…"
            : heeftBeeld
              ? "Beeld vervangen"
              : "Beeld toevoegen"}
        </button>
      </div>
    </form>
  );
}
