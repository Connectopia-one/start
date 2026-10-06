"use client";

import Link from "next/link";
import { useCallback, useEffect, useState } from "react";
import { VraagTekst } from "@/components/Figuren";
import {
  haalDagvraag,
  type Dagvraag as DagvraagType,
} from "@/app/dagvraag-actions";
import {
  gegevenKeuzes,
  heeftMeerdereAntwoorden,
  juisteKeuzes,
  schrijfKeuzes,
  zelfdeKeuzes,
} from "@/lib/antwoord";
import { WEEKDOEL } from "@/lib/dagvraag";
import { NIVEAUS, vindNiveau } from "@/lib/niveaus";
import { zonderOordeel } from "@/lib/uitleg";
import {
  leesWeekstand,
  noteerVraagGedaan,
  tekenVandaagAf,
  vraagAlGedaan,
  type Weekstand,
} from "@/lib/weekdoel";

const NIVEAU_KEY = "oefenplatform_dagvraag_niveau";
const OPEN_KEY = "oefenplatform_dagvraag_open";

type Gegeven = number | number[] | boolean | null;

/**
 * De vraag van de dag op de startpagina.
 *
 * Eén vraag per dag, met een doel van drie dagen per week. Er wordt niets van
 * opgeslagen in de databank: geen voortgang, geen sticker, geen rapport. Dat is
 * met opzet. Eén losse vraag hoort geen vinkje te zetten op een hoofdstuk dat
 * een kind nooit geopend heeft, en een extraatje dat meetelt voor een rapport
 * is geen extraatje meer.
 */
export function Dagvraag() {
  const [niveau, setNiveau] = useState<string | null>(null);
  const [geladen, setGeladen] = useState(false);
  const [vraag, setVraag] = useState<DagvraagType | null>(null);
  const [niveaus, setNiveaus] = useState<string[]>([]);
  const [gegeven, setGegeven] = useState<Gegeven>(null);
  const [gecontroleerd, setGecontroleerd] = useState(false);
  const [stand, setStand] = useState<Weekstand | null>(null);
  /*
    Dichtgeklapt tot je erop klikt. Kim op 29 september 2026: "kan de vraag van
    vandaag in en uitklikbaar zijn zodat je het moet open klikken om te doen?
    nu neemt het veel plaats in beslag." De startpagina is de weg naar de
    hoofdstukken; de vraag van de dag is een extraatje en hoort dus niet het
    halve scherm te vullen. Wie hem openzet, vindt hem de volgende keer weer
    open.
  */
  const [open, setOpen] = useState(false);

  // localStorage is een bron buiten React; pas na het eerste tekenen uitlezen,
  // anders verschilt wat de server maakte van wat de browser toont.
  useEffect(() => {
    let bewaard: string | null = null;
    let stondOpen = false;
    try {
      bewaard = localStorage.getItem(NIVEAU_KEY);
      stondOpen = localStorage.getItem(OPEN_KEY) === "ja";
    } catch {
      // privénavigatie: dan maar zonder onthouden
    }
    const huidige = leesWeekstand();
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setNiveau(bewaard);
    setOpen(stondOpen);
    setStand(huidige);
    setGeladen(true);
  }, []);

  useEffect(() => {
    if (!geladen) return;
    let geannuleerd = false;
    haalDagvraag(niveau)
      .then((antwoord) => {
        if (geannuleerd) return;
        setVraag(antwoord.vraag);
        setNiveaus(antwoord.niveaus);
        setGegeven(null);
        // Wie déze vraag al deed, ziet ze meteen met het antwoord erbij.
        // Verstoppen heeft geen zin. Maar het gaat om deze ene vraag, niet om
        // de dag: er staat er één per categorie, en een vraag die het kind nog
        // niet gezien heeft, hoort gewoon open te staan.
        setGecontroleerd(vraagAlGedaan(antwoord.vraag?.id ?? ""));
      })
      .catch(() => {
        // Lukt het ophalen niet, dan blijft de startpagina gewoon zonder kader.
      });
    return () => {
      geannuleerd = true;
    };
  }, [geladen, niveau]);

  const kiesNiveau = useCallback((slug: string) => {
    setVraag(null);
    setNiveau(slug);
    try {
      localStorage.setItem(NIVEAU_KEY, slug);
    } catch {
      // niet kunnen onthouden is geen reden om de keuze te weigeren
    }
  }, []);

  if (!geladen || !vraag || !stand) return null;

  const meerdere = heeftMeerdereAntwoorden(vraag);
  const ingevuld = Array.isArray(gegeven)
    ? gegeven.length > 0
    : gegeven !== null;
  const correct = gecontroleerd && isCorrect(vraag, gegeven);

  const controleer = () => {
    setGecontroleerd(true);
    noteerVraagGedaan(vraag.id);
    // Het weekdoel telt dagen, geen vragen: een tweede categorie op dezelfde
    // dag zet dus geen tweede bolletje bij.
    setStand(tekenVandaagAf(stand));
  };

  const klapOm = () => {
    const nieuw = !open;
    setOpen(nieuw);
    try {
      localStorage.setItem(OPEN_KEY, nieuw ? "ja" : "nee");
    } catch {
      // privénavigatie: dan onthoudt het gewoon niets
    }
  };

  return (
    <section className="mt-6 rounded-xl border border-amber/40 bg-amber/5 p-5">
      <div className="flex flex-wrap items-baseline justify-between gap-2">
        <button
          type="button"
          onClick={klapOm}
          aria-expanded={open}
          className="flex items-baseline gap-2 text-left"
        >
          <span aria-hidden className="text-ink-dim">
            {open ? "▾" : "▸"}
          </span>
          <span className="font-display text-lg font-semibold text-ink">
            ☀️ De vraag van vandaag
          </span>
        </button>
        <Weekteller stand={stand} />
      </div>

      {!open && (
        <button
          type="button"
          onClick={klapOm}
          className="mt-1 text-sm text-ink-dim underline-offset-2 hover:text-ink hover:underline"
        >
          {gecontroleerd
            ? "Je deed ze al. Klik om ze nog eens te bekijken."
            : "Klik open voor de vraag van vandaag."}
        </button>
      )}

      {open && niveaus.length > 1 && (
        <div className="mt-3 flex flex-wrap items-center gap-1.5">
          <span className="mr-1 text-xs text-ink-dim">
            Voor welke categorie?
          </span>
          {NIVEAUS.filter((n) => niveaus.includes(n.slug)).map((n) => (
            <button
              key={n.slug}
              type="button"
              onClick={() => kiesNiveau(n.slug)}
              className={`rounded-full px-2.5 py-1 text-xs transition ${
                n.slug === niveau
                  ? "bg-forest text-white"
                  : "border border-border bg-surface text-ink hover:border-forest"
              }`}
            >
              {n.emoji} {n.naam}
            </button>
          ))}
        </div>
      )}

      {open && (
        <div className="mt-3 rounded-xl border border-border bg-surface p-5">
          <p className="mb-2 text-xs text-ink-dim">
            {vindNiveau(vraag.niveau)?.emoji} {vraag.vak} &middot;{" "}
            {vraag.hoofdstuk}
          </p>

          <VraagTekst tekst={vraag.vraag} />

          {vraag.afbeeldingUrl && (
            // eslint-disable-next-line @next/next/no-img-element
            <img
              src={vraag.afbeeldingUrl}
              alt="Afbeelding bij deze vraag"
              className="mt-3 max-h-64 rounded-md border border-border"
            />
          )}

          {meerdere && !gecontroleerd && (
            <p className="mt-3 rounded-md bg-amber/10 px-3 py-2 text-xs text-ink">
              Let op: hier is meer dan één antwoord juist. Duid ze allemaal aan.
            </p>
          )}

          {vraag.type === "meerkeuze" && (
            <div className="mt-3 space-y-2">
              {vraag.opties?.map((optie, i) => {
                const aangeduid = meerdere
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
                      type={meerdere ? "checkbox" : "radio"}
                      name={`dagvraag-${vraag.id}`}
                      checked={aangeduid}
                      disabled={gecontroleerd}
                      onChange={() => {
                        if (!meerdere) return setGegeven(i);
                        const nu = gegevenKeuzes(gegeven);
                        setGegeven(
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
                  disabled={gecontroleerd}
                  onClick={() => setGegeven(optie)}
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

          {!gecontroleerd ? (
            <button
              type="button"
              onClick={controleer}
              disabled={!ingevuld}
              className="mt-4 rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark disabled:cursor-not-allowed disabled:opacity-40"
            >
              Controleer
            </button>
          ) : (
            <div
              className={`mt-4 rounded-md px-3 py-2 text-sm ${
                gegeven === null
                  ? "bg-info/10 text-ink"
                  : correct
                    ? "bg-forest/10 text-forest-dark"
                    : "bg-danger/10 text-danger"
              }`}
            >
              <p className="font-medium">
                {gegeven === null
                  ? "Je deed deze vraag vandaag al."
                  : correct
                    ? "Juist!"
                    : "Niet helemaal juist."}
              </p>
              {!correct && (
                <p className="mt-1 text-ink">{juisteAntwoord(vraag)}</p>
              )}
              {vraag.uitleg && (
                <p className="mt-1 text-ink">{zonderOordeel(vraag.uitleg)}</p>
              )}
            </div>
          )}

          {gecontroleerd && (
            <p className="mt-3 text-sm">
              <Link
                href={`/vakken/${vraag.vakSlug}/${vraag.hoofdstukNummer}`}
                className="text-forest-dark underline-offset-2 hover:underline"
              >
                Verder oefenen in {vraag.hoofdstuk} &rarr;
              </Link>
            </p>
          )}
        </div>
      )}

      {open && gecontroleerd && (
        <p className="mt-3 text-xs text-ink-dim">
          {niveaus.length > 1
            ? "Deze is voor vandaag. Kies hierboven een andere categorie voor nog een vraag, of kom morgen terug."
            : "Deze is voor vandaag. Morgen staat er een nieuwe."}
        </p>
      )}
    </section>
  );
}

/** Het telraampje: drie bolletjes voor deze week, en hoeveel weken op rij. */
function Weekteller({ stand }: { stand: Weekstand }) {
  const gedaan = stand.dagen.length;
  const gehaald = gedaan >= WEEKDOEL;

  return (
    <p className="flex items-center gap-2 text-xs text-ink-dim">
      <span className="flex gap-1" aria-hidden>
        {Array.from({ length: WEEKDOEL }, (_, i) => (
          <span
            key={i}
            className={`inline-block h-2.5 w-2.5 rounded-full ${
              i < gedaan ? "bg-forest" : "border border-border bg-surface"
            }`}
          />
        ))}
      </span>
      <span>
        {gehaald
          ? `Weekdoel gehaald 🎉${stand.wekenOpRij > 1 ? ` · ${stand.wekenOpRij} weken op rij` : ""}`
          : `${gedaan} van de ${WEEKDOEL} deze week`}
      </span>
    </p>
  );
}

function isCorrect(vraag: DagvraagType, gegeven: Gegeven): boolean {
  if (gegeven === null) return false;
  if (vraag.type === "waarofniet") return gegeven === vraag.antwoord;
  return zelfdeKeuzes(gegevenKeuzes(gegeven), juisteKeuzes(vraag.antwoord));
}

function juisteAntwoord(vraag: DagvraagType): string {
  if (vraag.type === "waarofniet") {
    return `Juist was: ${vraag.antwoord === true ? "waar" : "niet waar"}.`;
  }
  const juist = juisteKeuzes(vraag.antwoord);
  const voor =
    juist.length > 1
      ? `Er waren ${juist.length} juiste antwoorden: `
      : "Juist was: ";
  return `${voor}${schrijfKeuzes(vraag.opties, juist)}.`;
}
