"use client";

import { useMemo, useRef, useState } from "react";
import type { Kamp } from "@/content/kampen";
import { kampRegels } from "@/content/kampen";
import { berekenPrijs, euro } from "@/lib/kampprijs";
import { kampInschrijven } from "@/app/kampen/acties";
import { Verstuurknop } from "@/components/Verstuurknop";

/*
  De kampinschrijving op /kampen/inschrijven, naar het voorbeeld van de
  inschrijfpagina van Young Engineers Demerland: bovenaan de kampen als
  kaartjes, met "Kies dit" vul je het formulier eronder in.

  Twee dingen anders dan bij Young Engineers: je kan meer dan één kamp tegelijk
  kiezen, en zoveel kinderen als nodig, elk met zijn eigen dagen.

  De kinderen gaan als één verborgen vakje (JSON) mee; de server rekent de
  prijs zelf opnieuw uit met dezelfde functie (lib/kampprijs.ts).
*/

type Kind = {
  sleutel: number;
  voornaam: string;
  achternaam: string;
  leeftijd: string;
  dagen: string[];
};

const veldStijl =
  "mt-1.5 block h-11 w-full rounded-full border border-border bg-cream px-4 text-[16px] text-ink outline-none focus:border-green";
const labelStijl = "text-[15px] font-bold text-ink";

function Ster() {
  return (
    <span className="text-orange" aria-hidden>
      {" "}
      *
    </span>
  );
}

export function KampInschrijving({ kampen }: { kampen: Kamp[] }) {
  const [filter, setFilter] = useState<"Alle" | "Hasselt" | "Genk">("Alle");
  const [gekozen, setGekozen] = useState<string[]>([]);
  const [volgende, setVolgende] = useState(1);
  const [kinderen, setKinderen] = useState<Kind[]>([
    { sleutel: 0, voornaam: "", achternaam: "", leeftijd: "", dagen: [] },
  ]);
  const [vt, setVt] = useState(false);
  const formulier = useRef<HTMLDivElement>(null);

  const gekozenKampen = kampen.filter((k) => gekozen.includes(k.id));
  const zichtbaar = kampen.filter((k) => filter === "Alle" || k.plaats === filter);

  /* Een kamp kiezen zet al zijn dagen aan bij elk kind; uitzetten haalt ze
     weg. Daarna kan je per kind nog dagen uitvinken. */
  function kies(kamp: Kamp) {
    const aan = !gekozen.includes(kamp.id);
    const dagen = kamp.dagen.map((d) => d.naam);
    setGekozen((oud) => (aan ? [...oud, kamp.id] : oud.filter((id) => id !== kamp.id)));
    setKinderen((oud) =>
      oud.map((kind) => ({
        ...kind,
        dagen: aan
          ? [...new Set([...kind.dagen, ...dagen])]
          : kind.dagen.filter((d) => !dagen.includes(d)),
      })),
    );
    if (aan) {
      setTimeout(
        () => formulier.current?.scrollIntoView({ behavior: "smooth", block: "start" }),
        50,
      );
    }
  }

  function wijzig(sleutel: number, deel: Partial<Kind>) {
    setKinderen((oud) => oud.map((k) => (k.sleutel === sleutel ? { ...k, ...deel } : k)));
  }

  function voegKindToe() {
    const dagen = gekozenKampen.flatMap((k) => k.dagen.map((d) => d.naam));
    setKinderen((oud) => [
      ...oud,
      { sleutel: volgende, voornaam: "", achternaam: oud[0]?.achternaam ?? "", leeftijd: "", dagen },
    ]);
    setVolgende((n) => n + 1);
  }

  const prijs = useMemo(() => berekenPrijs(kinderen, vt), [kinderen, vt]);
  const nogTeBevestigen = gekozenKampen.some((k) => k.bevestigen);
  const geenDagen = kinderen.some((k) => k.dagen.length === 0);

  return (
    <div className="grid gap-8">
      {/* De kampen */}
      <div>
        <div className="flex flex-wrap items-center justify-between gap-3">
          <h2 className="text-2xl text-green">Kies je kamp</h2>
          <div className="flex flex-wrap gap-2">
            {(["Alle", "Hasselt", "Genk"] as const).map((f) => (
              <button
                key={f}
                type="button"
                onClick={() => setFilter(f)}
                className={`rounded-full border-2 px-4 py-1.5 text-[15px] font-bold transition ${
                  filter === f
                    ? "border-green bg-green text-cream"
                    : "border-green text-green hover:bg-sage-soft"
                }`}
              >
                {f}
              </button>
            ))}
          </div>
        </div>

        <div className="mt-5 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {zichtbaar.map((kamp) => {
            const aan = gekozen.includes(kamp.id);
            return (
              <div
                key={kamp.id}
                className={`flex flex-col overflow-hidden rounded-[20px] border-2 bg-surface shadow-[0_2px_10px_rgba(47,74,34,0.07)] ${
                  aan ? "border-green" : "border-border"
                }`}
              >
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={`/fotos/${kamp.foto}`}
                  alt={kamp.fotoBeschrijving}
                  className="aspect-[16/10] w-full object-cover"
                />
                <div className="bg-orange px-5 py-2 text-[14px] font-extrabold uppercase tracking-wide text-cream">
                  Vakantiekamp · {kamp.plaats}
                </div>
                <div className="flex flex-1 flex-col p-5">
                  <h3 className="text-[19px] font-extrabold text-green">{kamp.titel}</h3>
                  <p className="font-hand text-xl text-orange">{kamp.thema}</p>
                  <p className="mt-2 text-[15px] text-ink">
                    <strong>Wanneer:</strong> {kamp.wanneer}, {kampRegels.uren.toLowerCase()}
                  </p>
                  <p className="text-[15px] text-ink">
                    <strong>Waar:</strong> {kamp.adres}
                  </p>
                  <p className="text-[15px] text-ink">
                    <strong>Prijs:</strong> {euro(kampRegels.prijsPerDag)} per dag
                  </p>
                  {kamp.opmerking ? (
                    <p className="mt-2 rounded-[12px] bg-purple-soft px-3 py-2 text-[14px] text-ink">
                      {kamp.opmerking}
                    </p>
                  ) : null}
                  {kamp.volzet ? (
                    <p className="mt-2 rounded-[12px] bg-orange-soft px-3 py-2 text-[14px] font-bold text-ink">
                      Volzet. Je kan je nog op de wachtlijst zetten.
                    </p>
                  ) : null}
                  <div className="mt-auto pt-4">
                    <button
                      type="button"
                      onClick={() => kies(kamp)}
                      className={`w-full rounded-full border-2 px-5 py-2.5 text-[16px] font-extrabold transition ${
                        aan
                          ? "border-green bg-sage-soft text-green"
                          : "border-green bg-green text-cream hover:bg-green-mid"
                      }`}
                    >
                      {aan ? "✓ Gekozen" : kamp.volzet ? "Kies dit (wachtlijst)" : "Kies dit"}
                    </button>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Het formulier */}
      <div
        ref={formulier}
        className="scroll-mt-6 rounded-[20px] border border-border bg-surface p-6 shadow-[0_2px_10px_rgba(47,74,34,0.07)]"
      >
        <h2 className="text-2xl text-green">Inschrijven</h2>
        {gekozenKampen.length === 0 ? (
          <p className="mt-2 text-ink-dim">
            Klik eerst bij een kamp op &quot;Kies dit&quot;. Je mag er meer dan één kiezen.
          </p>
        ) : (
          <form action={kampInschrijven} className="mt-4 grid gap-6">
            <input
              type="hidden"
              name="kinderen"
              value={JSON.stringify(
                kinderen.map(({ voornaam, achternaam, leeftijd, dagen }) => ({
                  voornaam,
                  achternaam,
                  leeftijd,
                  dagen,
                })),
              )}
            />
            <div className="hidden" aria-hidden>
              <label>
                Laat dit veld leeg
                <input type="text" name="adres" tabIndex={-1} autoComplete="off" />
              </label>
            </div>

            {kinderen.map((kind, i) => (
              <fieldset
                key={kind.sleutel}
                className="rounded-[16px] border border-border bg-cream/60 p-5"
              >
                <div className="flex items-center justify-between gap-3">
                  <legend className="text-[18px] font-extrabold text-green">
                    {i === 0 ? "Je kind" : `Kind ${i + 1}`}
                  </legend>
                  {i > 0 ? (
                    <button
                      type="button"
                      onClick={() =>
                        setKinderen((oud) => oud.filter((k) => k.sleutel !== kind.sleutel))
                      }
                      className="text-[14px] font-bold text-orange underline-offset-4 hover:underline"
                    >
                      Dit kind wissen
                    </button>
                  ) : null}
                </div>
                <div className="mt-3 grid gap-4 sm:grid-cols-3">
                  <label className="block">
                    <span className={labelStijl}>
                      Voornaam
                      <Ster />
                    </span>
                    <input
                      required
                      value={kind.voornaam}
                      onChange={(e) => wijzig(kind.sleutel, { voornaam: e.target.value })}
                      className={veldStijl}
                    />
                  </label>
                  <label className="block">
                    <span className={labelStijl}>
                      Achternaam
                      <Ster />
                    </span>
                    <input
                      required
                      value={kind.achternaam}
                      onChange={(e) => wijzig(kind.sleutel, { achternaam: e.target.value })}
                      className={veldStijl}
                    />
                  </label>
                  <label className="block">
                    <span className={labelStijl}>
                      Leeftijd
                      <Ster />
                    </span>
                    <input
                      required
                      type="number"
                      min={4}
                      max={18}
                      value={kind.leeftijd}
                      onChange={(e) => wijzig(kind.sleutel, { leeftijd: e.target.value })}
                      className={veldStijl}
                    />
                  </label>
                </div>

                <p className={`mt-4 ${labelStijl}`}>Welke dagen komt {kind.voornaam || "dit kind"}?</p>
                <div className="mt-2 grid gap-3 sm:grid-cols-2">
                  {gekozenKampen.map((kamp) => (
                    <div key={kamp.id}>
                      <p className="text-[14px] font-bold text-sage">{kamp.titel}</p>
                      {kamp.dagen.map((dag) => (
                        <label key={dag.naam} className="mt-1 flex items-center gap-2.5 text-[16px] text-ink">
                          <input
                            type="checkbox"
                            checked={kind.dagen.includes(dag.naam)}
                            onChange={(e) =>
                              wijzig(kind.sleutel, {
                                dagen: e.target.checked
                                  ? [...kind.dagen, dag.naam]
                                  : kind.dagen.filter((d) => d !== dag.naam),
                              })
                            }
                            className="h-[18px] w-[18px] shrink-0 accent-green"
                          />
                          {dag.label}
                        </label>
                      ))}
                    </div>
                  ))}
                </div>
              </fieldset>
            ))}

            <div>
              <button
                type="button"
                onClick={voegKindToe}
                className="rounded-full border-2 border-green px-5 py-2 text-[15px] font-extrabold text-green transition hover:bg-sage-soft"
              >
                + Nog een kind inschrijven
              </button>
              {kampRegels.broerZusKorting > 0 ? (
                <p className="mt-1.5 text-[14px] text-ink-dim">
                  Een broer of zus krijgt {euro(kampRegels.broerZusKorting)} korting per kampdag.
                </p>
              ) : null}
            </div>

            {/* De ouder */}
            <div>
              <h3 className="text-[18px] font-extrabold text-green">Je gegevens</h3>
              <div className="mt-3 grid gap-4 sm:grid-cols-2">
                {[
                  { naam: "ouder", label: "Naam van de ouder", type: "text", nodig: true, auto: "name" },
                  { naam: "email", label: "E-mailadres", type: "email", nodig: true, auto: "email" },
                  { naam: "gsm", label: "Gsm-nummer", type: "tel", nodig: true, auto: "tel" },
                  { naam: "gemeente", label: "Gemeente waar jullie wonen", type: "text", nodig: false, auto: "address-level2" },
                ].map((v) => (
                  <label key={v.naam} className="block">
                    <span className={labelStijl}>
                      {v.label}
                      {v.nodig ? <Ster /> : null}
                    </span>
                    <input
                      name={v.naam}
                      type={v.type}
                      required={v.nodig}
                      autoComplete={v.auto}
                      className={veldStijl}
                    />
                  </label>
                ))}
              </div>
            </div>

            <label className="flex items-start gap-2.5 text-[16px] text-ink">
              <input
                type="checkbox"
                name="vt"
                value="ja"
                checked={vt}
                onChange={(e) => setVt(e.target.checked)}
                className="mt-1 h-[18px] w-[18px] shrink-0 accent-green"
              />
              <span>
                We hebben recht op een verhoogde tegemoetkoming (halve prijs)
                {vt ? (
                  <span className="mt-1 block text-[14px] text-ink-dim">
                    Mail het attest naar info@matmgroep.com. Je betaalt nu al de helft.
                  </span>
                ) : null}
              </span>
            </label>

            <fieldset>
              <legend className={labelStijl}>
                Mogen we foto&apos;s nemen waar je kind op staat?
                <Ster />
              </legend>
              <div className="mt-2 grid gap-1.5">
                {[
                  "Ja, ook voor de website en sociale media",
                  "Ja, maar enkel om naar de ouders te sturen",
                  "Nee, liever niet",
                ].map((keuze) => (
                  <label key={keuze} className="flex items-center gap-2.5 text-[16px] text-ink">
                    <input
                      type="radio"
                      name="fotos"
                      value={keuze}
                      required
                      className="h-[18px] w-[18px] shrink-0 accent-green"
                    />
                    {keuze}
                  </label>
                ))}
              </div>
            </fieldset>

            <label className="block">
              <span className={labelStijl}>Iets dat we moeten weten? (allergie, eerder ophalen, ...)</span>
              <textarea
                name="boodschap"
                rows={3}
                className="mt-1.5 block w-full rounded-[14px] border border-border bg-cream px-4 py-3 text-[16px] text-ink outline-none focus:border-green"
              />
            </label>

            {/* De prijs */}
            <div className="rounded-[16px] bg-sage-soft px-5 py-4">
              <p className="text-[15px] font-bold text-sage">Te betalen</p>
              <p className="mt-1 text-[15px] text-ink">
                {prijs.dagen} {prijs.dagen === 1 ? "kampdag" : "kampdagen"} × {euro(kampRegels.prijsPerDag)} ={" "}
                {euro(prijs.subtotaal)}
              </p>
              {prijs.korting > 0 ? (
                <p className="text-[15px] text-ink">Korting broer of zus: −{euro(prijs.korting)}</p>
              ) : null}
              {prijs.vtKorting > 0 ? (
                <p className="text-[15px] text-ink">Verhoogde tegemoetkoming: −{euro(prijs.vtKorting)}</p>
              ) : null}
              <p className="mt-1 text-[22px] font-extrabold text-green">{euro(prijs.totaal)}</p>
              <p className="mt-1 text-[14px] text-ink-dim">
                Je betaalt met een overschrijving. Na het inschrijven zie je het
                rekeningnummer en de mededeling.
                {nogTeBevestigen ? " Voor een kamp dat nog bevestigd moet worden, betaal je pas na onze bevestiging." : ""}
              </p>
            </div>

            <div className="rounded-[16px] bg-purple-soft px-5 py-4">
              <p className="text-[15px] text-ink">
                We gebruiken deze gegevens enkel om je inschrijving te regelen en
                je te contacteren over het kamp. We geven ze aan niemand door.
              </p>
              <label className="mt-3 flex items-start gap-2.5 text-[15px] font-bold text-ink">
                <input
                  type="checkbox"
                  required
                  className="mt-0.5 h-[18px] w-[18px] shrink-0 accent-green"
                />
                Dat is goed
                <Ster />
              </label>
            </div>

            {geenDagen ? (
              <p className="text-[15px] font-bold text-orange">Vink bij elk kind minstens één dag aan.</p>
            ) : null}
            <div className={geenDagen ? "pointer-events-none opacity-50" : undefined}>
              <Verstuurknop />
            </div>
          </form>
        )}
      </div>
    </div>
  );
}
