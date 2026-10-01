"use client";

import Link from "next/link";
import { useEffect, useMemo, useRef, useState } from "react";
import { MeldingKnop } from "@/components/MeldingKnop";
import {
  haalOefenstand,
  registreerAntwoord,
  registreerSticker,
} from "@/app/voortgang-actions";
import {
  KleurVraag,
  SleepVraag,
  VraagTekst,
  leesVraag,
} from "@/components/Figuren";
import {
  gegevenKeuzes,
  heeftMeerdereAntwoorden,
  invulAntwoorden,
  juisteKeuzes,
  schrijfInvul,
  schrijfKeuzes,
  woordkern,
  zelfdeKeuzes,
} from "@/lib/antwoord";
import { bewaarActiefKind, leesActiefKind } from "@/lib/actiefkind";
import { beurtnummer, type GetoondeVariant } from "@/lib/spellingvariant";

/*
  toonVoortgang: staat er een voortgangsbalk bij de vragen van dit kind?

  Een ouder van twee kinderen meldde op 29 september 2026 dat haar ene kind
  blij was dat die balk er níét is (het zag hoeveel vragen er waren en
  blokkeerde), terwijl het andere er net door geholpen wordt: voorspelbaarheid.
  De keuze hangt dus aan het kind, niet aan het platform. De ouder zet ze op
  /account; standaard staat ze uit.
*/
type Kind = { id: string; naam: string; toonVoortgang?: boolean };

type Vraag = {
  id: string;
  type: "meerkeuze" | "invultekst" | "waarofniet";
  vraag: string;
  opties: string[] | null;
  /** Een lijstje nummers betekent: er is meer dan één juist antwoord. */
  antwoord: number | string | boolean | number[] | string[];
  uitleg: string | null;
  volgnummer: number;
  afbeeldingUrl?: string | null;
  /**
   * Per getoonde plaats het nummer dat de optie in de databank heeft. De opties
   * worden geschud voor ze getoond worden (zie lib/optievolgorde.ts), maar het
   * antwoord van een kind wordt opgeslagen met het nummer uit de databank, zodat
   * de pagina waar ouders meekijken blijft kloppen.
   */
  optieVolgorde?: number[] | null;
  /**
   * Wisselende woorden, enkel bij spelling. Beurt 1 is de vraag hierboven, de
   * lijst is beurt 2 en verder. Welke beurt dit kind krijgt, hangt af van hoe
   * vaak het deze vraag al maakte. Zie lib/spellingvariant.ts.
   */
  varianten?: GetoondeVariant[] | null;
};

/** De vraag zoals dit kind ze nu voor zich krijgt, met het nummer van de beurt. */
function metBeurt(
  vraag: Vraag,
  beurten: number,
): { vraag: Vraag; beurt: number } {
  const lijst = vraag.varianten ?? [];
  const beurt = beurtnummer(beurten, lijst.length);
  if (beurt === 0) return { vraag, beurt };
  const v = lijst[beurt - 1];
  return { vraag: { ...vraag, ...v }, beurt };
}

/** Het aangeklikte antwoord omgerekend naar hoe het opgeslagen moet worden. */
function zoalsOpgeslagen(vraag: Vraag, gegeven: Gegeven): Gegeven {
  if (vraag.type !== "meerkeuze") return gegeven;
  const volgorde = vraag.optieVolgorde;
  if (!volgorde) return gegeven;
  const terug = (i: number) =>
    i >= 0 && i < volgorde.length ? volgorde[i] : i;
  if (Array.isArray(gegeven)) return gegeven.map(terug).sort((a, b) => a - b);
  if (typeof gegeven === "number") return terug(gegeven);
  return gegeven;
}

type Gegeven = string | number | boolean | number[] | null;

type Status = {
  gecontroleerd: boolean;
  correct: boolean;
  gegevenAntwoord: Gegeven;
};

/**
 * Zet een ingetypt antwoord om naar een vorm die we kunnen vergelijken.
 * Hoofdletters, een lidwoord vooraan ("de longen"), een punt achteraan en
 * dubbele spaties mogen het verschil niet maken tussen juist en fout — een
 * kind dat het antwoord kent, hoort het ook juist te hebben.
 */
function normaliseerAntwoord(waarde: string): string {
  const tekst = zonderAccenten(waarde)
    .trim()
    .toLowerCase()
    .replace(/[.!?]+$/, "")
    .replace(/\s+/g, " ")
    .replace(/^(de|het|een) /, "");
  return normaliseerGetal(tekst) ?? tekst;
}

/**
 * Haalt de accenten van een woord af: "tête" wordt "tete", "sœur" wordt
 * "soeur". Bij Frans staan er accenten in bijna elk antwoord, en die zijn op
 * een toetsenbord lastig te typen — de œ van sœur al helemaal. Een kind dat
 * het woord kent maar de ê niet vindt, hoort daarom niet fout te staan. De
 * juiste schrijfwijze blijft wel zichtbaar: staat er een accentverschil, dan
 * zet het platform het correcte woord erbij (zie AccentNota).
 */
function zonderAccenten(waarde: string): string {
  return waarde
    .replace(/œ/g, "oe")
    .replace(/Œ/g, "OE")
    .replace(/æ/g, "ae")
    .replace(/Æ/g, "AE")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "");
}

/**
 * Was het antwoord juist, maar schreef het kind het zonder de accenten? Dan
 * geven we het woord zoals het hoort te staan. De vakfiche Frans vraagt
 * uitdrukkelijk een redelijk correcte spelling, dus verzwijgen doen we het
 * verschil niet.
 */
function accentverschil(vraag: Vraag, gegeven: Gegeven): string | null {
  if (vraag.type !== "invultekst" || typeof gegeven !== "string") return null;
  const getypt = gegeven.trim().toLowerCase();
  const antwoorden = invulAntwoorden(vraag.antwoord);
  if (antwoorden.some((a) => getypt === a.toLowerCase())) return null;
  return (
    antwoorden.find(
      (a) =>
        a !== zonderAccenten(a) &&
        zonderAccenten(getypt) === zonderAccenten(a.toLowerCase()),
    ) ?? null
  );
}

/**
 * Was het antwoord juist, maar schreef het kind het met een kleine letter waar
 * een hoofdletter hoort? Dan zeggen we dat erbij.
 *
 * Marjolein meldde dit op 29 september 2026: bij "de Engelse naam voor de maand
 * december" stond in de uitleg dat een maand in het Engels een hoofdletter
 * krijgt, maar wie "december" typte, kreeg gewoon een vinkje. Fout rekenen is
 * te hard — een kind dat het woord kent, kent het — maar zwijgen klopt ook
 * niet, want dan spreekt het platform zichzelf tegen.
 *
 * Het gaat altijd over een echte hoofdletter in het antwoord: December,
 * Wednesday, Brussel, Mars, de O van zuurstof. Een gewoon woord staat in onze
 * bestanden nergens met een hoofdletter, dus niemand krijgt deze zin te zien
 * waar ze niet hoort.
 */
function hoofdletterverschil(vraag: Vraag, gegeven: Gegeven): string | null {
  if (vraag.type !== "invultekst" || typeof gegeven !== "string") return null;
  const getypt = gegeven.trim();
  const antwoorden = invulAntwoorden(vraag.antwoord);
  if (antwoorden.some((a) => getypt === a.trim())) return null;
  return (
    antwoorden.find(
      (a) =>
        a !== a.toLowerCase() &&
        getypt.toLowerCase() === a.trim().toLowerCase(),
    ) ?? null
  );
}

/**
 * Telt dit ingetypte antwoord als juist? Buiten de taalvakken tellen enkelvoud
 * en meervoud allebei mee: "kieuw" naast "kieuwen", "herbivoor" naast
 * "herbivoren". Zie woordkern in lib/antwoord.ts.
 */
function zelfdeWoord(
  getypt: string,
  antwoord: string,
  soepel: boolean,
): boolean {
  const a = normaliseerAntwoord(getypt);
  const b = normaliseerAntwoord(antwoord);
  if (a === b) return true;
  // "50%" en "50" zijn hetzelfde antwoord, ook bij een taalvak: dit gaat over
  // schrijfwijze van een getal, niet over spelling.
  if (zelfdeGetal(a, b)) return true;
  if (!soepel) return false;
  // Getallen laten we met rust: daar is 3 niet hetzelfde als 3en.
  if (/\d/.test(a) || /\d/.test(b)) return false;
  return woordkern(a) === woordkern(b);
}

/**
 * Was het antwoord juist, maar schreef het kind het anders dan het hoort? Dan
 * zetten we de juiste schrijfwijze eronder: de accenten (tête) of de vorm die
 * we verwachtten (kieuwen). Verzwijgen doen we het verschil niet, want de
 * spelling hoort ook bij de leerstof.
 */
function schrijfwijzeNota(
  vraag: Vraag,
  gegeven: Gegeven,
  soepel: boolean,
): { tekst: string; soort: "accent" | "hoofdletter" | "vorm" } | null {
  const accent = accentverschil(vraag, gegeven);
  if (accent) return { tekst: accent, soort: "accent" };
  const hoofdletter = hoofdletterverschil(vraag, gegeven);
  if (hoofdletter) return { tekst: hoofdletter, soort: "hoofdletter" };
  if (vraag.type !== "invultekst" || typeof gegeven !== "string" || !soepel)
    return null;
  const getypt = normaliseerAntwoord(gegeven);
  const antwoorden = invulAntwoorden(vraag.antwoord);
  if (antwoorden.some((a) => normaliseerAntwoord(a) === getypt)) return null;
  // Wie "50%" typte waar wij "50" schreven, hoeft geen verbetering te zien.
  if (antwoorden.some((a) => zelfdeGetal(getypt, normaliseerAntwoord(a))))
    return null;
  const anders = antwoorden.find((a) => zelfdeWoord(gegeven, a, true));
  return anders ? { tekst: anders, soort: "vorm" } : null;
}

/**
 * Een getal kan je op meer dan één juiste manier typen: "3,5" en "3.5",
 * "2 500" en "2500", "0,50" en "0,5". Is het antwoord een getal, dan
 * herleiden we het tot één vorm. Zo telt een kind dat het juiste getal typt
 * niet fout omdat het een punt gebruikte of een nul te veel schreef.
 */
function normaliseerGetal(tekst: string): string | null {
  const zonderSpaties = tekst.replace(/(\d) (?=\d{3}\b)/g, "$1");
  const treffer = zonderSpaties.match(/^(-?)(\d*)(?:[.,](\d+))?$/);
  if (!treffer || (!treffer[2] && !treffer[3])) return null;
  const heel = (treffer[2] || "0").replace(/^0+(?=\d)/, "");
  const deel = (treffer[3] ?? "").replace(/0+$/, "");
  const getal = deel ? `${heel},${deel}` : heel;
  return getal === "0" ? "0" : treffer[1] + getal;
}

/**
 * Een teken dat bij een getal hoort maar het antwoord niet verandert: het
 * procentteken, het euroteken en het gradenteken. Een kind dat "50%" typt op
 * "Hoeveel procent is de helft?" heeft het even goed als een kind dat "50"
 * typt — het wist het antwoord. Echte maateenheden (kg, m, cm, l) staan hier
 * bewust niet tussen: daar maakt de eenheid wél het verschil tussen juist en
 * fout.
 *
 * Gemeld door een kind uit de testgroep op 28 september 2026: "ik had 50%
 * ingetypt maar het was fout. Het goede antwoord was 50."
 */
const GETALTEKENS: { teken: RegExp; soort: string }[] = [
  {
    teken: /^\s*(%|procent|percent)\s*|\s*(%|procent|percent)\s*$/,
    soort: "procent",
  },
  { teken: /^\s*(€|euro)\s*|\s*(€|euro)\s*$/, soort: "euro" },
  { teken: /^\s*(°|graden|graad)\s*|\s*(°|graden|graad)\s*$/, soort: "graden" },
];

/**
 * Splitst "50%" in het getal 50 en het soort teken. Staat er geen getal in,
 * dan geeft dit niets terug en verandert er niets aan de vergelijking.
 */
function getalMetTeken(tekst: string): { getal: string; soort: string } | null {
  for (const { teken, soort } of GETALTEKENS) {
    if (!teken.test(tekst)) continue;
    const kaal = normaliseerGetal(tekst.replace(teken, "").trim());
    if (kaal) return { getal: kaal, soort };
  }
  const kaal = normaliseerGetal(tekst.trim());
  return kaal ? { getal: kaal, soort: "" } : null;
}

/**
 * Is dit hetzelfde getal, op een teken na dat er niet toe doet? "50" en "50%"
 * wel, "50%" en "50 euro" niet — wie een ander teken meetypt, bedoelt iets
 * anders.
 */
function zelfdeGetal(getypt: string, antwoord: string): boolean {
  const a = getalMetTeken(getypt);
  const b = getalMetTeken(antwoord);
  if (!a || !b || a.getal !== b.getal) return false;
  return a.soort === b.soort || a.soort === "" || b.soort === "";
}

function isCorrect(vraag: Vraag, gegeven: Gegeven, soepel = false): boolean {
  if (gegeven === null) return false;
  if (vraag.type === "invultekst") {
    // Staat er meer dan één antwoord in, dan telt elk ervan juist. Zie lib/antwoord.ts.
    return invulAntwoorden(vraag.antwoord).some((a) =>
      zelfdeWoord(String(gegeven), a, soepel),
    );
  }
  // Bij meerkeuze moet het aangeduide precies overeenkomen met wat juist is.
  // Wie er één aanduidt terwijl er twee juist waren, heeft de vraag fout — net
  // zoals op het examen, waar daar geen halve punten voor bestaan.
  if (vraag.type === "meerkeuze") {
    return zelfdeKeuzes(gegevenKeuzes(gegeven), juisteKeuzes(vraag.antwoord));
  }
  return gegeven === vraag.antwoord;
}

/** Heeft het kind al iets aangeduid of ingevuld? */
function isIngevuld(gegeven: Gegeven): boolean {
  if (gegeven === null || gegeven === "") return false;
  return !Array.isArray(gegeven) || gegeven.length > 0;
}

function VraagKaart({
  vraag,
  status,
  alsVakjes,
  soepel,
  onAntwoord,
  onControleer,
}: {
  vraag: Vraag;
  status: Status;
  /** Vakjes in plaats van bolletjes: er kan meer dan één antwoord juist zijn. */
  alsVakjes: boolean;
  /** Buiten de taalvakken telt een enkelvoud ook als het meervoud gevraagd is. */
  soepel: boolean;
  onAntwoord: (v: string | number | boolean | number[]) => void;
  onControleer: () => void;
}) {
  const gegeven = status.gegevenAntwoord;
  // Een invulvraag kan ook een kleur- of sleepoefening zijn, zie Figuren.tsx.
  const { interactie } = leesVraag(vraag.vraag);

  return (
    <div className="rounded-xl border border-border bg-surface p-5">
      <VraagTekst tekst={vraag.vraag} />

      {vraag.afbeeldingUrl && (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={vraag.afbeeldingUrl}
          alt="Afbeelding bij deze vraag"
          className="mt-3 max-h-64 rounded-md border border-border"
        />
      )}

      {vraag.type === "meerkeuze" && (
        <div className="mt-3 space-y-2">
          {vraag.opties?.map((optie, i) => {
            const aangeduid = alsVakjes
              ? gegevenKeuzes(gegeven).includes(i)
              : gegeven === i;
            return (
              <label
                key={i}
                className={`flex cursor-pointer items-center gap-2 rounded-md border px-3 py-2 text-sm ${
                  aangeduid ? "border-forest bg-forest/5" : "border-border"
                }`}
              >
                <input
                  type={alsVakjes ? "checkbox" : "radio"}
                  name={vraag.id}
                  checked={aangeduid}
                  disabled={status.gecontroleerd}
                  onChange={() => {
                    if (!alsVakjes) return onAntwoord(i);
                    const nu = gegevenKeuzes(gegeven);
                    onAntwoord(
                      nu.includes(i)
                        ? nu.filter((k) => k !== i)
                        : [...nu, i].sort((a, b) => a - b),
                    );
                  }}
                  className="accent-forest"
                />
                {optie}
              </label>
            );
          })}
        </div>
      )}

      {vraag.type === "waarofniet" && (
        <div className="mt-3 flex gap-2">
          {[true, false].map((optie) => (
            <button
              key={String(optie)}
              type="button"
              disabled={status.gecontroleerd}
              onClick={() => onAntwoord(optie)}
              className={`rounded-md border px-4 py-2 text-sm ${
                gegeven === optie
                  ? "border-forest bg-forest/5 text-forest-dark"
                  : "border-border text-ink"
              }`}
            >
              {optie ? "Waar" : "Niet waar"}
            </button>
          ))}
        </div>
      )}

      {vraag.type === "invultekst" && interactie?.soort === "kleur" && (
        <KleurVraag
          vorm={interactie.vorm}
          delen={interactie.delen}
          uitgeschakeld={status.gecontroleerd}
          onAntwoord={onAntwoord}
        />
      )}

      {vraag.type === "invultekst" &&
        interactie?.soort === "sleep" &&
        vraag.opties && (
          <SleepVraag
            id={vraag.id}
            items={vraag.opties}
            richting={interactie.richting}
            uitgeschakeld={status.gecontroleerd}
            onAntwoord={onAntwoord}
          />
        )}

      {vraag.type === "invultekst" && !interactie && (
        /*
          Geen hulp van de browser of de telefoon in dit vakje.

          Een ouder meldde op 1 oktober 2026 dat een verkeerd gespeld antwoord
          meteen een rode kronkellijn kreeg: het kind wist dus al dat het fout
          was voor het op Controleer klikte, en dat nodigt uit tot gokken in
          plaats van tot nadenken. Erger nog op een telefoon, waar de
          autocorrectie een spelfout stilletjes zou rechtzetten en het kind
          niets meer leert.

          spellCheck zet de kronkellijn uit, autoCorrect de stille verbetering,
          autoCapitalize de hoofdletter die een telefoon er vanzelf van maakt,
          en autoComplete het lijstje met wat hier eerder getypt werd.
        */
        <input
          type="text"
          disabled={status.gecontroleerd}
          value={typeof gegeven === "string" ? gegeven : ""}
          onChange={(e) => onAntwoord(e.target.value)}
          spellCheck={false}
          autoCorrect="off"
          autoCapitalize="off"
          autoComplete="off"
          className="mt-3 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          placeholder="Typ je antwoord..."
        />
      )}

      {!status.gecontroleerd ? (
        <button
          type="button"
          onClick={onControleer}
          disabled={!isIngevuld(gegeven)}
          className="mt-4 rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark disabled:cursor-not-allowed disabled:opacity-40"
        >
          Controleer
        </button>
      ) : (
        <div
          className={`mt-4 rounded-md px-3 py-2 text-sm ${
            status.correct
              ? "bg-forest/10 text-forest-dark"
              : "bg-danger/10 text-danger"
          }`}
        >
          <p className="font-medium">
            {status.correct ? "Juist!" : "Niet helemaal juist."}
          </p>
          {status.correct &&
            (() => {
              const nota = schrijfwijzeNota(
                vraag,
                status.gegevenAntwoord,
                soepel,
              );
              if (!nota) return null;
              return (
                <p className="mt-1 text-ink">
                  {nota.soort === "accent"
                    ? "Let op de accenten: je schrijft het als "
                    : nota.soort === "hoofdletter"
                      ? "Let op de hoofdletter: je schrijft het als "
                      : "Wij schreven het als "}
                  <strong>{nota.tekst}</strong>.
                </p>
              );
            })()}
          {!status.correct && vraag.type === "invultekst" && (
            <p className="mt-1 text-ink">
              Juist was: <strong>{schrijfInvul(vraag.antwoord)}</strong>
            </p>
          )}
          {!status.correct && alsVakjes && vraag.opties && (
            <p className="mt-1 text-ink">
              {juisteKeuzes(vraag.antwoord).length > 1
                ? `Er waren ${juisteKeuzes(vraag.antwoord).length} juiste antwoorden: `
                : "Juist was: "}
              <strong>
                {schrijfKeuzes(vraag.opties, juisteKeuzes(vraag.antwoord))}
              </strong>
            </p>
          )}
          {vraag.uitleg && <p className="mt-1 text-ink">{vraag.uitleg}</p>}
        </div>
      )}
    </div>
  );
}

export function Quiz({
  vragen: alleVragen,
  kinderen = [],
  hoofdstukId,
  taalvak = false,
}: {
  vragen: Vraag[];
  kinderen?: Kind[];
  hoofdstukId?: string;
  /** Bij een taalvak wordt een ingetypt antwoord streng vergeleken. */
  taalvak?: boolean;
}) {
  const [statussen, setStatussen] = useState<Record<string, Status>>(() =>
    Object.fromEntries(
      alleVragen.map((v) => [
        v.id,
        { gecontroleerd: false, correct: false, gegevenAntwoord: null },
      ]),
    ),
  );
  const [actiefKindId, setActiefKindId] = useState<string | null>(null);

  /*
    Gevraagd door een testgezin op 30 september 2026: "Telkens als je
    teruggaat naar een hoofdstuk die je al eerder hebt gedaan, start je
    volledig opnieuw. Zou het mogelijk zijn om enkel de vragen te krijgen die
    nog niet eerder werden opgelost?"

    Het is bewust een keuze en geen automatische filter. Een kind dat iets
    weken geleden juist had, mag dat gerust nog eens oefenen, en veel
    kinderen doen een hoofdstuk net graag een tweede keer helemaal. Daarom
    start het hoofdstuk altijd met álle vragen; wie wil, klikt de andere knop.

    null betekent: nog niet opgehaald, of er valt niets op te halen.
  */
  const [alJuist, setAlJuist] = useState<Set<string> | null>(null);
  /* Hoe vaak dit kind elke vraag al maakte, voor de wisselende woorden bij
     spelling. null betekent: nog niet opgehaald. */
  const [beurten, setBeurten] = useState<Record<string, number> | null>(null);
  /*
    Welke vragen het kind nu voor zich krijgt.

      "alles"     — het hele hoofdstuk opnieuw
      "verder"    — enkel de vragen die het nog nooit maakte
      "nietJuist" — enkel de vragen die het nog niet juist had

    Kim, 30 september 2026: "nu kan je enkel kiezen tussen of het heel
    hoofdstuk of die je fout had. niet waar je gebleven was." Wie halverwege
    stopte, wil gewoon verder. Dat is iets anders dan de fouten overdoen: bij
    "verder" vallen ook de vragen weg die het kind fóút had, want die maakte
    het al.
  */
  const [lijstKeuze, setLijstKeuze] = useState<
    "alles" | "verder" | "nietJuist"
  >("alles");
  // Telt mee bij "Opnieuw proberen", zodat ook wat een kind ingekleurd of
  // gesleept had weer leeg begint.
  const [ronde, setRonde] = useState(0);
  /*
    Eén vraag tegelijk op het scherm, niet de hele lijst onder elkaar. Kim op
    29 september 2026: "om bij het oefen gedeelte mss de oefeningen 1 per 1 te
    tonen ipv een scroll lijst. zo kunnen ze ook echt vraag per vraag een fout
    melden moest er 1 zijn."
  */
  const [huidige, setHuidige] = useState(0);
  const vraagKop = useRef<HTMLDivElement>(null);
  const eersteKeer = useRef(true);

  // Na "Volgende" begint de nieuwe vraag bovenaan, anders sta je midden in de
  // vorige te kijken. Bij het openen van het hoofdstuk niet scrollen.
  useEffect(() => {
    if (eersteKeer.current) {
      eersteKeer.current = false;
      return;
    }
    vraagKop.current?.scrollIntoView({ behavior: "smooth", block: "start" });
  }, [huidige]);

  useEffect(() => {
    if (!kinderen.length) return;
    const opgeslagen = leesActiefKind();
    const geldig = opgeslagen && kinderen.some((k) => k.id === opgeslagen);
    // Synchroniseert met localStorage (een externe bron) na mount — bewust hier,
    // niet in de lazy state-initializer, om een server/client-mismatch te vermijden.
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setActiefKindId(geldig ? opgeslagen : kinderen[0].id);
  }, [kinderen]);

  const kiesKind = (id: string) => {
    setActiefKindId(id);
    bewaarActiefKind(id);
    // Een ander kind heeft een andere voorgeschiedenis, dus de lijst gaat terug
    // naar alle vragen tot we weten wat dít kind al juist had.
    setAlJuist(null);
    setBeurten(null);
    setLijstKeuze("alles");
  };

  /* Wat had dit kind in dit hoofdstuk al juist? Mislukt de vraag, dan blijft
     alJuist leeg en krijgt het kind gewoon alle vragen: nooit minder oefenen
     door een fout. */
  useEffect(() => {
    if (!actiefKindId || !hoofdstukId) return;
    let geannuleerd = false;
    haalOefenstand(actiefKindId, hoofdstukId)
      .then((stand) => {
        if (geannuleerd) return;
        setAlJuist(new Set(stand.juist));
        setBeurten(stand.beurten);
      })
      .catch(() => {
        // Lukt het ophalen niet, dan krijgt het kind alle vragen en de vraag
        // zoals ze in de databank staat. Nooit minder oefenen door een fout.
        if (!geannuleerd) setBeurten({});
      });
    return () => {
      geannuleerd = true;
    };
  }, [actiefKindId, hoofdstukId]);

  /* De vragen die het kind nu voor zich krijgt, elk in de beurt die bij dit
     kind hoort. Bij een vraag zonder wisselende woorden is dat altijd de vraag
     zelf, en dat zijn ze bijna allemaal. */
  const vragen = useMemo(() => {
    let lijst = alleVragen;
    if (lijstKeuze === "nietJuist" && alJuist)
      lijst = alleVragen.filter((v) => !alJuist.has(v.id));
    if (lijstKeuze === "verder" && beurten)
      lijst = alleVragen.filter((v) => !(beurten[v.id] ?? 0));
    return lijst.map((v) => metBeurt(v, beurten?.[v.id] ?? 0));
  }, [lijstKeuze, alJuist, alleVragen, beurten]);

  /* Heeft dit hoofdstuk wisselende woorden, dan wachten we met tonen tot we
     weten welke beurt dit kind krijgt. Anders staat er even het ene woord en
     een tel later het andere. Een hoofdstuk zonder varianten wacht nergens op
     en verandert dus niet. */
  const heeftVarianten = alleVragen.some((v) => (v.varianten ?? []).length > 0);
  const wachtOpBeurt = heeftVarianten && Boolean(actiefKindId) && !beurten;

  // Hoeveel vragen van dit hoofdstuk staan er nog open? Is dat er geen enkele,
  // of zijn het er evenveel als het hoofdstuk telt, dan valt er niets te
  // kiezen en tonen we de balk niet.
  const nogOpen = alJuist
    ? alleVragen.filter((v) => !alJuist.has(v.id)).length
    : alleVragen.length;
  // En hoeveel heeft het nog nooit gemaakt? Dat is waar het gebleven was.
  const nooitGemaakt = beurten
    ? alleVragen.filter((v) => !(beurten[v.id] ?? 0)).length
    : 0;
  const toonKeuze = Boolean(
    alJuist && nogOpen > 0 && nogOpen < alleVragen.length,
  );

  // Staat er in dit hoofdstuk één vraag met meer dan één juist antwoord, dan
  // krijgen álle meerkeuzevragen vakjes. Zou enkel die ene vraag vakjes hebben,
  // dan verklapt het vakje het antwoord en oefent het kind net niet waar het om
  // gaat: zelf zien hoeveel antwoorden er juist zijn.
  // Bewust over het hele hoofdstuk en niet over de lijst van dit moment: of
  // er vakjes staan mag niet veranderen naargelang een kind alles opnieuw
  // doet of enkel de overige vragen.
  const alsVakjes = alleVragen.some((v) => heeftMeerdereAntwoorden(v));

  /* Tellen doen we over de vragen die het kind nú voor zich heeft, niet over
     alle statussen: staat de lijst op "enkel wat ik nog niet juist had", dan
     zou de balk anders vragen meetellen die niet op het scherm komen. */
  const aantalGecontroleerd = vragen.filter(
    (v) => statussen[v.vraag.id]?.gecontroleerd,
  ).length;
  const aantalCorrect = vragen.filter(
    (v) => statussen[v.vraag.id]?.correct,
  ).length;
  const klaar = vragen.length > 0 && aantalGecontroleerd === vragen.length;
  const perfect = klaar && aantalCorrect === vragen.length;

  /* De sticker hangt aan "alle vragen van dit hoofdstuk juist". Staat de lijst
     op enkel de overige vragen, dan waren de andere al juist — dat is net
     waarom ze wegvielen — dus is het hoofdstuk op dat moment volledig juist en
     is de sticker verdiend. */
  /* Bij "verder waar je gebleven was" vallen ook de fout beantwoorde vragen
     weg. Die zijn dan nóg niet juist, dus is het hoofdstuk niet volledig juist
     en is de ster niet verdiend. Vandaar deze controle: samen met wat al juist
     stond, moet de lijst op het scherm het hele hoofdstuk dekken. */
  const getoond = new Set(vragen.map((v) => v.vraag.id));
  const lijstDektAlles = alleVragen.every(
    (v) => getoond.has(v.id) || alJuist?.has(v.id),
  );

  const stickerGegeven = useRef(false);
  useEffect(() => {
    if (
      perfect &&
      lijstDektAlles &&
      actiefKindId &&
      hoofdstukId &&
      !stickerGegeven.current
    ) {
      stickerGegeven.current = true;
      registreerSticker(actiefKindId, hoofdstukId).catch(() => {});
    }
  }, [perfect, lijstDektAlles, actiefKindId, hoofdstukId]);

  const opnieuw = () => {
    stickerGegeven.current = false;
    setRonde((r) => r + 1);
    setHuidige(0);
    setStatussen(
      Object.fromEntries(
        alleVragen.map((v) => [
          v.id,
          { gecontroleerd: false, correct: false, gegevenAntwoord: null },
        ]),
      ),
    );
  };

  /* Van de ene lijst naar de andere. In elke richting begint het kind met een
     schone lei. */
  const kiesLijst = (keuze: "alles" | "verder" | "nietJuist") => {
    setLijstKeuze(keuze);
    opnieuw();
  };

  if (!vragen.length) {
    return (
      <p className="mt-8 text-sm text-ink-dim">
        Er zijn nog geen vragen in dit hoofdstuk.
      </p>
    );
  }

  const { vraag, beurt } = vragen[Math.min(huidige, vragen.length - 1)];
  /* Staat het kind op de laatste vraag van zijn reeks, dan is "Volgende" geen
     stap vooruit meer. Is er elders nog een vraag open, dan brengt de knop het
     daarnaartoe; is er niets meer open, dan staat ze grijs en zegt de regel
     eronder waarom. Zonder dat liep een kind vast op een reeks van één vraag. */
  const laatsteVanDeReeks = huidige >= vragen.length - 1;
  const nogOpenElders = vragen.findIndex(
    (v, i) => i !== huidige && !statussen[v.vraag.id]?.gecontroleerd,
  );
  const toonBalk = Boolean(
    kinderen.find((k) => k.id === actiefKindId)?.toonVoortgang,
  );
  const perVragen = vragen.length
    ? Math.round((aantalGecontroleerd / vragen.length) * 100)
    : 0;

  return (
    <div className="mt-8 space-y-4">
      {kinderen.length > 1 && (
        <div className="flex items-center gap-2 text-sm">
          <label htmlFor="actief-kind" className="text-ink-dim">
            Wie oefent er:
          </label>
          <select
            id="actief-kind"
            value={actiefKindId ?? ""}
            onChange={(e) => kiesKind(e.target.value)}
            className="rounded-md border border-border bg-surface px-2 py-1 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          >
            {kinderen.map((k) => (
              <option key={k.id} value={k.id}>
                {k.naam}
              </option>
            ))}
          </select>
        </div>
      )}
      {kinderen.length === 0 && (
        <p className="rounded-md bg-info/10 px-3 py-2 text-xs text-info">
          Voortgang wordt niet bijgehouden.{" "}
          <Link href="/account" className="underline underline-offset-2">
            Voeg een kind toe aan je account
          </Link>{" "}
          om een rapport per kind te krijgen.
        </p>
      )}

      {toonKeuze && (
        <div className="rounded-xl border border-border bg-surface px-4 py-3">
          <p className="text-sm text-ink">
            Je was hier al eens bezig.{" "}
            {nooitGemaakt > 0
              ? nooitGemaakt === 1
                ? "Er is nog één vraag die je nog niet maakte."
                : `Er zijn nog ${nooitGemaakt} vragen die je nog niet maakte.`
              : "Je maakte alle vragen al een keer."}{" "}
            {nogOpen === 1
              ? "Eén vraag had je nog niet juist."
              : `${nogOpen} vragen had je nog niet juist.`}
          </p>
          <div className="mt-2 flex flex-wrap gap-2">
            {nooitGemaakt > 0 && (
              <button
                type="button"
                onClick={() => kiesLijst("verder")}
                aria-pressed={lijstKeuze === "verder"}
                className={`rounded-md px-3 py-1.5 text-sm transition ${
                  lijstKeuze === "verder"
                    ? "bg-forest text-paper"
                    : "border border-border text-ink hover:border-forest"
                }`}
              >
                Verder waar je gebleven was
              </button>
            )}
            <button
              type="button"
              onClick={() => kiesLijst("nietJuist")}
              aria-pressed={lijstKeuze === "nietJuist"}
              className={`rounded-md px-3 py-1.5 text-sm transition ${
                lijstKeuze === "nietJuist"
                  ? "bg-forest text-paper"
                  : "border border-border text-ink hover:border-forest"
              }`}
            >
              {nogOpen === 1
                ? "Enkel die ene vraag"
                : `Enkel die ${nogOpen} die je nog niet juist had`}
            </button>
            <button
              type="button"
              onClick={() => kiesLijst("alles")}
              aria-pressed={lijstKeuze === "alles"}
              className={`rounded-md px-3 py-1.5 text-sm transition ${
                lijstKeuze === "alles"
                  ? "bg-forest text-paper"
                  : "border border-border text-ink hover:border-forest"
              }`}
            >
              Alle {alleVragen.length} opnieuw
            </button>
          </div>
        </div>
      )}

      {toonBalk && (
        <div className="sticky top-2 z-10 rounded-xl border border-border bg-surface/95 px-4 py-3 backdrop-blur">
          <div className="flex flex-wrap items-baseline justify-between gap-x-3">
            <p className="text-sm font-medium text-ink">
              {aantalGecontroleerd} van de {vragen.length} nagekeken
            </p>
            <p className="text-xs text-ink-dim">
              {klaar
                ? "Je bent er helemaal door."
                : `Nog ${vragen.length - aantalGecontroleerd} te gaan.`}
            </p>
          </div>
          <div
            role="progressbar"
            aria-valuemin={0}
            aria-valuemax={vragen.length}
            aria-valuenow={aantalGecontroleerd}
            aria-label="Hoeveel vragen je al nagekeken hebt"
            className="mt-2 h-2 w-full overflow-hidden rounded-full bg-border"
          >
            <div
              className="h-full rounded-full bg-forest transition-all duration-300"
              style={{ width: `${perVragen}%` }}
            />
          </div>
        </div>
      )}

      {alsVakjes && (
        <p className="rounded-md bg-amber/10 px-3 py-2 text-xs text-ink">
          Let op: bij de keuzevragen in dit hoofdstuk kan er méér dan één
          antwoord juist zijn. Duid alles aan wat klopt — net als op het examen
          krijg je de vraag maar goed als je ze allemaal hebt, niet de helft.
        </p>
      )}

      <div ref={vraagKop} className="scroll-mt-4">
        {wachtOpBeurt ? (
          <p className="rounded-xl border border-border bg-surface px-5 py-8 text-center text-sm text-ink-dim">
            Even kijken welke woorden er deze keer aan de beurt zijn...
          </p>
        ) : (
          <VraagKaart
            key={`${vraag.id}-${beurt}-${ronde}`}
            vraag={vraag}
            status={statussen[vraag.id]}
            alsVakjes={alsVakjes}
            soepel={!taalvak}
            onAntwoord={(v) =>
              setStatussen((s) => ({
                ...s,
                [vraag.id]: { ...s[vraag.id], gegevenAntwoord: v },
              }))
            }
            onControleer={() => {
              const correct = isCorrect(
                vraag,
                statussen[vraag.id].gegevenAntwoord,
                !taalvak,
              );
              setStatussen((s) => ({
                ...s,
                [vraag.id]: { ...s[vraag.id], gecontroleerd: true, correct },
              }));
              if (actiefKindId) {
                registreerAntwoord(
                  actiefKindId,
                  vraag.id,
                  hoofdstukId ?? null,
                  correct,
                  zoalsOpgeslagen(vraag, statussen[vraag.id].gegevenAntwoord),
                  beurt,
                ).catch(() => {});
              }
            }}
          />
        )}

        {/* Melden bij de vraag zelf: je staat erop, dus je hoeft ze niet meer
            uit een lijst te kiezen. */}
        {hoofdstukId && (
          <MeldingKnop
            key={`melding-${vraag.id}`}
            hoofdstukId={hoofdstukId}
            vragen={[]}
            /* Het nummer dat de vraag in het hélé hoofdstuk heeft, niet in
               de lijst die dit kind nu voor zich heeft. Anders meldt een
               kind "vraag 2" terwijl het in Beheer vraag 7 is. */
            vasteVraag={{
              id: vraag.id,
              volgnummer: alleVragen.findIndex((v) => v.id === vraag.id) + 1,
            }}
          />
        )}
      </div>

      <div className="flex items-center justify-between gap-3">
        <button
          type="button"
          onClick={() => setHuidige((i) => Math.max(0, i - 1))}
          disabled={huidige === 0}
          className="rounded-md border border-border px-4 py-2 text-sm text-ink-dim transition hover:border-forest hover:text-ink disabled:cursor-not-allowed disabled:opacity-40"
        >
          &larr; Vorige
        </button>

        {/* Het nummer staat er alleen als de ouder de voortgangsbalk aanzette.
            Voor een kind dat blokkeert op "nog zeventien te gaan" is dat net
            wat je niet wil tonen. */}
        {toonBalk && (
          <p className="text-xs text-ink-dim">
            Vraag {huidige + 1} van {vragen.length}
          </p>
        )}

        <button
          type="button"
          onClick={() =>
            laatsteVanDeReeks
              ? setHuidige(nogOpenElders)
              : setHuidige((i) => Math.min(vragen.length - 1, i + 1))
          }
          disabled={laatsteVanDeReeks && nogOpenElders < 0}
          className={`rounded-md px-4 py-2 text-sm font-medium transition disabled:cursor-not-allowed disabled:opacity-40 ${
            statussen[vraag.id]?.gecontroleerd
              ? "bg-forest text-white hover:bg-forest-dark"
              : "border border-border text-ink-dim hover:border-forest hover:text-ink"
          }`}
        >
          {laatsteVanDeReeks && nogOpenElders >= 0
            ? "Nog te doen "
            : "Volgende "}
          &rarr;
        </button>
      </div>

      {/* Waarom die knop grijs staat. Een testgezin liep hier vast: het kind
          stond op de laatste vraag van haar reeks, had ze nog niet nagekeken,
          en kon dus niet verder. Er stond niets bij, dus leek het platform
          kapot. Nu zegt het zelf wat er nog moet gebeuren. */}
      {laatsteVanDeReeks && nogOpenElders < 0 && !klaar && (
        <p className="text-center text-xs text-ink-dim">
          Dit is de laatste vraag van deze reeks. Klik hierboven op Controleer,
          dan is ze klaar.
        </p>
      )}

      {klaar && (
        <div
          className={`rounded-xl border px-5 py-4 text-center ${
            perfect
              ? "border-amber/40 bg-amber/10"
              : "border-forest/30 bg-forest/10"
          }`}
        >
          {perfect ? (
            <>
              <p className="text-3xl">🌟</p>
              <p className="mt-1 font-display text-lg font-semibold text-amber">
                Sticker verdiend!
              </p>
              <p className="mt-1 text-sm text-ink">
                Alle {vragen.length} vragen juist — helemaal correct, knap
                gedaan!
              </p>
            </>
          ) : (
            <p className="font-display text-lg font-semibold text-forest-dark">
              Je scoorde {aantalCorrect} / {vragen.length}
            </p>
          )}
          <button
            type="button"
            onClick={opnieuw}
            className={`mt-3 rounded-md border px-4 py-2 text-sm font-medium transition ${
              perfect
                ? "border-amber text-amber hover:bg-amber/10"
                : "border-forest text-forest-dark hover:bg-forest/10"
            }`}
          >
            Opnieuw proberen
          </button>
        </div>
      )}
    </div>
  );
}
