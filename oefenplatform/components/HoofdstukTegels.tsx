"use client";

import Link from "next/link";
import { splitsDeel } from "@/lib/hoofdstukvolgorde";
import { KindKeuze, useActiefKind, type Kind } from "@/components/KindKeuze";

export type HoofdstukTegel = {
  id: string;
  titel: string;
  volgnummer: number;
  gratis: boolean;
  /** Mag dit kind erin? Vrijgegeven of gratis. */
  mag: boolean;
};

/**
 * Het uitdagingshoofdstuk van een vak: één hoofdstuk dat alle andere door
 * elkaar haalt, met moeilijkere vragen. Het staat altijd achteraan en krijgt
 * een eigen kleurtje, zodat het opvalt zonder een extra kolom in de databank.
 */
function isUitdaging(titel: string) {
  return titel.trim().toLowerCase().startsWith("uitdaging");
}

/**
 * Het pittige broertje van een hoofdstuk: dezelfde leerstof, moeilijkere
 * vragen. "Getallenkennis — pittig" hoort meteen naast "Getallenkennis" te
 * staan en niet achteraan bij de rest, want het kind kiest per onderwerp.
 * Het herkennen gebeurt aan de titel, zodat er geen kolom in de databank bij
 * moet en een import volstaat.
 */
const PITTIG = "— pittig";

function isPittig(titel: string) {
  return titel.trim().toLowerCase().endsWith(PITTIG);
}

function basisTitel(titel: string) {
  const t = titel.trim();
  return isPittig(t) ? t.slice(0, t.length - PITTIG.length).trim() : t;
}

/**
 * De hoofdstukken van één vak als vakjes in plaats van als lijst, met per
 * vakje of het actieve kind het al gemaakt heeft. Een hoofdstuk mag zo vaak
 * opnieuw als een kind wil, dus "gemaakt" is een geruststelling en geen slot.
 */
export function HoofdstukTegels({
  vakSlug,
  hoofdstukken,
  kinderen,
}: {
  vakSlug: string;
  hoofdstukken: HoofdstukTegel[];
  kinderen: Kind[];
}) {
  const { actiefKindId, status, kies } = useActiefKind(
    kinderen,
    hoofdstukken.map((h) => h.id),
  );

  const gemaakt = hoofdstukken.filter((h) => status.get(h.id)?.gemaakt).length;

  // Een pittig hoofdstuk krijgt het volgnummer van zijn gewone hoofdstuk en
  // komt daar net achter; het uitdagingshoofdstuk blijft helemaal achteraan.
  const plaats = new Map<string, number>();
  // Bij ✨ Spark is een thema opgesplitst in een deel 1 en een deel 2, en hoort
  // "Getallenleer — pittig" achter "Getallenleer — deel 2". Daarom onthouden we
  // per thema ook het hóógste volgnummer, als terugval op de volle titel.
  const plaatsVanThema = new Map<string, number>();
  for (const h of hoofdstukken) {
    if (isPittig(h.titel) || isUitdaging(h.titel)) continue;
    plaats.set(h.titel.trim(), h.volgnummer);
    const { thema } = splitsDeel(h.titel);
    plaatsVanThema.set(thema, Math.max(plaatsVanThema.get(thema) ?? 0, h.volgnummer));
  }
  const sleutel = (h: HoofdstukTegel): [number, number, number] => {
    if (isUitdaging(h.titel)) return [2, h.volgnummer, 0];
    if (isPittig(h.titel)) {
      const basis = basisTitel(h.titel);
      const bij =
        plaats.get(basis) ??
        plaatsVanThema.get(splitsDeel(basis).thema) ??
        h.volgnummer;
      return [1, bij, 1];
    }
    return [1, h.volgnummer, 0];
  };
  const opVolgorde = [...hoofdstukken].sort((a, b) => {
    const [ga, na, pa] = sleutel(a);
    const [gb, nb, pb] = sleutel(b);
    return ga - gb || na - nb || pa - pb;
  });

  return (
    <>
      <KindKeuze
        kinderen={kinderen}
        actiefKindId={actiefKindId}
        onKies={kies}
      />

      {actiefKindId && (
        <p className="mt-4 text-sm text-ink-dim">
          {gemaakt === 0
            ? "Nog geen enkel hoofdstuk gemaakt. Kies er eentje om te starten."
            : `Al ${gemaakt} van de ${hoofdstukken.length} hoofdstukken gemaakt. Je mag ze zo vaak opnieuw doen als je wil.`}
        </p>
      )}

      <div className="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {opVolgorde.map((h) => {
          const s = status.get(h.id);
          const uitdaging = isUitdaging(h.titel);
          const pittig = isPittig(h.titel);
          return (
            <Link
              key={h.id}
              href={`/vakken/${vakSlug}/${h.volgnummer}`}
              className={`relative flex min-h-[6rem] flex-col rounded-xl border bg-surface p-4 transition hover:shadow-sm ${
                uitdaging || pittig
                  ? "border-amber/50 hover:border-amber"
                  : s?.gemaakt
                    ? "border-forest/40 hover:border-forest"
                    : "border-border hover:border-forest"
              }`}
            >
              {/* Het merkteken zweeft in de hoek in plaats van in een eigen
                  regel te staan: zo begint elk vakje met zijn titel, ook de
                  vakjes die nog geen teken hebben. */}
              {s?.perfect ? (
                <span
                  aria-hidden
                  title="Foutloos gemaakt"
                  className="absolute right-3 top-3 text-lg"
                >
                  ⭐
                </span>
              ) : s?.gemaakt ? (
                <span
                  aria-hidden
                  title="Al gemaakt"
                  className="absolute right-3 top-3 text-lg"
                >
                  ✅
                </span>
              ) : null}

              <span
                className={`flex-1 text-sm font-medium text-ink ${s?.gemaakt ? "pr-7" : ""}`}
              >
                {h.titel}
              </span>

              <span className="mt-3 flex flex-wrap items-center gap-2">
                {uitdaging ? (
                  <span className="rounded-full bg-amber/15 px-2.5 py-0.5 text-xs font-medium text-amber">
                    Extra uitdaging
                  </span>
                ) : pittig ? (
                  <span className="rounded-full bg-amber/15 px-2.5 py-0.5 text-xs font-medium text-amber">
                    Moeilijker
                  </span>
                ) : null}
                {h.gratis ? (
                  <span className="rounded-full bg-forest/10 px-2.5 py-0.5 text-xs font-medium text-forest-dark">
                    Gratis
                  </span>
                ) : h.mag ? (
                  <span className="rounded-full bg-forest/10 px-2.5 py-0.5 text-xs font-medium text-forest-dark">
                    Vrijgegeven
                  </span>
                ) : (
                  <span className="rounded-full bg-ink-dim/10 px-2.5 py-0.5 text-xs font-medium text-ink-dim">
                    Op slot
                  </span>
                )}
                {s?.perfect ? (
                  <span className="text-xs text-forest-dark">Foutloos</span>
                ) : s?.gemaakt ? (
                  <span className="text-xs text-ink-dim">Al gemaakt</span>
                ) : null}
              </span>
            </Link>
          );
        })}
      </div>
    </>
  );
}
