"use client";

import Link from "next/link";
import { splitsDeel, themaNaam } from "@/lib/hoofdstukvolgorde";
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

type Groep = { naam: string; leden: HoofdstukTegel[] };

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

  // De hoofdstukken komen per thema bij elkaar te staan, onder een kopje:
  // "Getallenleer — deel 1", "— deel 2" en "— pittig" samen onder
  // "Getallenleer". Testouder Sandy Van De Sande op 28 oktober 2026: bij
  // wiskunde stond alles door elkaar, bij techniek mooi per onderwerp. Dat
  // kwam omdat techniek in één keer ingeladen is, met volgnummers netjes na
  // elkaar, en wiskunde in stukken. Daarom kijken we hier naar het thema in de
  // titel en niet naar het volgnummer.
  //
  // De volgorde van de thema's is die van de lijst die we krijgen (zie
  // sorteerHoofdstukken). Het uitdagingshoofdstuk blijft helemaal achteraan.
  const groepen = new Map<string, Groep>();
  const uitdagingen: HoofdstukTegel[] = [];
  for (const h of hoofdstukken) {
    if (isUitdaging(h.titel)) {
      uitdagingen.push(h);
      continue;
    }
    const basis = basisTitel(h.titel);
    const sleutel = splitsDeel(basis).thema;
    let groep = groepen.get(sleutel);
    if (!groep) {
      groep = { naam: themaNaam(basis), leden: [] };
      groepen.set(sleutel, groep);
    }
    groep.leden.push(h);
  }
  // Binnen een thema: eerst de delen op volgorde, dan het pittige hoofdstuk.
  for (const groep of groepen.values()) {
    groep.leden.sort((a, b) => {
      const pa = isPittig(a.titel) ? 1 : 0;
      const pb = isPittig(b.titel) ? 1 : 0;
      return (
        pa - pb ||
        splitsDeel(a.titel).deel - splitsDeel(b.titel).deel ||
        a.volgnummer - b.volgnummer
      );
    });
  }

  // Een hoofdstuk dat alleen in zijn thema staat, krijgt geen eigen kopje:
  // dat zou zijn titel twee keer zetten. Zulke hoofdstukken na elkaar komen
  // samen in één gewoon raster.
  const blokken: { naam: string | null; leden: HoofdstukTegel[] }[] = [];
  for (const groep of groepen.values()) {
    if (groep.leden.length > 1) {
      blokken.push(groep);
      continue;
    }
    const vorige = blokken[blokken.length - 1];
    if (vorige && vorige.naam === null) vorige.leden.push(...groep.leden);
    else blokken.push({ naam: null, leden: [...groep.leden] });
  }
  if (uitdagingen.length) blokken.push({ naam: null, leden: uitdagingen });

  const tegel = (h: HoofdstukTegel, inGroep: boolean) => {
    const s = status.get(h.id);
    const uitdaging = isUitdaging(h.titel);
    const pittig = isPittig(h.titel);
    // Onder een kopje volstaat "Deel 1" of "Pittig": het thema staat er al
    // boven.
    const { deel } = splitsDeel(h.titel);
    const label = !inGroep
      ? h.titel
      : pittig
        ? "Pittig"
        : deel
          ? `Deel ${deel}`
          : h.titel;
    return (
      <Link
        key={h.id}
        href={`/vakken/${vakSlug}/${h.volgnummer}`}
        title={h.titel}
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
            title="Hier al aan gewerkt"
            className="absolute right-3 top-3 text-lg"
          >
            ✅
          </span>
        ) : null}

        <span
          className={`flex-1 text-sm font-medium text-ink ${s?.gemaakt ? "pr-7" : ""}`}
        >
          {label}
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
          {/* Het vinkje in de hoek zegt al genoeg dat een kind hier
              geweest is. Kim op 30 september 2026: "kan de zin al gemaakt
              weg? want ookal heb je 2 oefeningen gemaakt zegt die al
              gemaakt. enkel het groen vinkje is voldoende." Het woord
              beloofde meer dan het vinkje bedoelt. Bij de ster blijft er
              wél een woord staan: die is verdiend en overdrijft niets. */}
          {s?.perfect ? (
            <span className="text-xs text-forest-dark">Foutloos</span>
          ) : null}
        </span>
      </Link>
    );
  };

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

      <div className="mt-6 space-y-6">
        {blokken.map((blok, i) =>
          blok.naam ? (
            <section key={blok.naam + i}>
              <h2 className="mb-2 font-display text-base font-semibold text-ink">
                {blok.naam}
              </h2>
              <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
                {blok.leden.map((h) => tegel(h, true))}
              </div>
            </section>
          ) : (
            <div key={i} className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
              {blok.leden.map((h) => tegel(h, false))}
            </div>
          ),
        )}
      </div>
    </>
  );
}
