"use client";

import { useEffect, useState } from "react";

type Foto = { id: string; url: string; aangemaakt: string };

/*
  De foto's van een klasje naar de computer, om ze daarna in de OneDrive-map
  te zetten voor sociale media. Gevraagd door Kim op 26 oktober 2026: de
  kinderen van de plusklas zaterdag mogen online komen.

  Kim en haar werknemer zetten allebei foto's op. Daarom onthoudt deze
  computer tot welke foto hij al gedownload heeft, en geeft de eerste knop
  enkel wat er sindsdien bijkwam, wie het ook opzette. Dat onthouden zit in
  de browser zelf: op een andere computer begint het opnieuw bij alles.

  Elke foto krijgt een vaste naam met de dag waarop hij opgezet werd en een
  stukje van zijn nummer, zodat een tweede download nooit een andere foto
  overschrijft. Chrome vraagt de eerste keer of de site meerdere bestanden
  mag downloaden; daar klik je op Toestaan.
*/
export function AllesDownloaden({ fotos, klasjeNaam, slug }: { fotos: Foto[]; klasjeNaam: string; slug: string }) {
  const sleutel = `fotos-gedownload-tot-${slug}`;
  const [tot, setTot] = useState<string | null>(null);
  const [bezig, setBezig] = useState(false);
  const [stand, setStand] = useState<string | null>(null);

  useEffect(() => {
    try {
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setTot(localStorage.getItem(sleutel));
    } catch {
      /* Geen geheugen in deze browser: dan is alles nieuw. */
    }
  }, [sleutel]);

  const nieuw = tot ? fotos.filter((f) => f.aangemaakt > tot) : fotos;
  const basis = klasjeNaam.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "klasje";

  async function download(lijst: Foto[]) {
    setBezig(true);
    let gelukt = 0;
    let laatste = tot ?? "";
    for (let i = 0; i < lijst.length; i++) {
      const f = lijst[i];
      setStand(`Foto ${i + 1} van ${lijst.length} downloaden…`);
      try {
        const antwoord = await fetch(f.url);
        if (!antwoord.ok) throw new Error();
        const blob = await antwoord.blob();
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = `${basis}-${f.aangemaakt.slice(0, 10)}-${f.id.slice(0, 6)}.jpg`;
        document.body.appendChild(link);
        link.click();
        link.remove();
        setTimeout(() => URL.revokeObjectURL(link.href), 10000);
        gelukt++;
        if (f.aangemaakt > laatste) laatste = f.aangemaakt;
      } catch {
        /* Eén foto die niet lukt, houdt de rest niet tegen. */
      }
      await new Promise((klaar) => setTimeout(klaar, 700));
    }
    if (gelukt === lijst.length && laatste) {
      try {
        localStorage.setItem(sleutel, laatste);
      } catch {
        /* Niet erg: dan biedt de knop ze de volgende keer opnieuw aan. */
      }
      setTot(laatste);
    }
    setStand(
      gelukt === lijst.length
        ? `${gelukt} ${gelukt === 1 ? "foto staat" : "foto's staan"} in je map Downloads.`
        : `${gelukt} van de ${lijst.length} foto's staan in je map Downloads. Herlaad de pagina en klik nog eens voor de rest.`,
    );
    setBezig(false);
  }

  if (!fotos.length) return null;

  return (
    <div className="mt-3 rounded-lg border border-border bg-surface px-4 py-3 text-sm">
      <p className="text-ink">
        De foto&apos;s opslaan op deze computer, bijvoorbeeld om ze in de OneDrive-map te zetten. Deze computer onthoudt
        wat al gedownload is, dus de eerste knop geeft enkel de foto&apos;s die er sindsdien bijkwamen.
      </p>
      <div className="mt-2 flex flex-wrap gap-2">
        <button
          type="button"
          onClick={() => download(nieuw)}
          disabled={bezig || nieuw.length === 0}
          className="rounded-md bg-forest px-3 py-1.5 font-medium text-white hover:bg-forest-dark disabled:opacity-60"
        >
          {nieuw.length === 0
            ? "Geen nieuwe foto's"
            : tot
              ? `Nieuwe foto's downloaden (${nieuw.length})`
              : `Alle ${nieuw.length} foto's downloaden`}
        </button>
        {tot && (
          <button
            type="button"
            onClick={() => download(fotos)}
            disabled={bezig}
            className="rounded-md border border-forest px-3 py-1.5 font-medium text-forest-dark hover:bg-forest/10 disabled:opacity-60"
          >
            Toch alle {fotos.length} downloaden
          </button>
        )}
      </div>
      {stand && <p className="mt-2 text-ink-dim">{stand}</p>}
    </div>
  );
}
