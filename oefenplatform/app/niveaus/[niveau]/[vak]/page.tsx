import Link from "next/link";
import { haalKorteUitleg } from "@/lib/korteUitleg";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { Leidraad } from "@/components/Leidraad";
import {
  HoofdstukTegels,
  type HoofdstukTegel,
} from "@/components/HoofdstukTegels";
import { getSessionProfile } from "@/lib/auth";
import { heeftVolledigeToegang, hoofdstukToegankelijk } from "@/lib/toegang";
import { createClient } from "@/lib/supabase/server";
import {
  PRIJS_NU_EUR,
  TIJDELIJKE_PRIJS,
  TIJDELIJKE_PRIJS_KORT,
} from "@/lib/prijs";
import { schooljaarEindeLabel } from "@/lib/schooljaar";
import { vindNiveau } from "@/lib/niveaus";
import { sorteerHoofdstukken } from "@/lib/hoofdstukvolgorde";
import { vakIcoon } from "@/lib/vakbeeld";
import { vindVaknoot, vindWegwijzer } from "@/inhoud/vaknoten";
import { isWelzijn } from "@/lib/welzijn";
import { Zoekvak } from "@/components/Zoekvak";
import { RichtingKeuze } from "@/components/RichtingKeuze";
import { leerrichting, valtWeg } from "@/lib/leerrichting";
import {
  extraSoort,
  magExtraBundel,
  sorteerExtraBundels,
  type ExtraBundel,
} from "@/lib/extraBundels";

/*
  De hoofdstukken van één vak binnen één niveau. Dit is de tweede laag knoppen:
  van /niveaus/<niveau> (de vakken) kom je hier, en van hier ga je naar
  /vakken/<vak>/<volgnummer> (de oefeningen zelf). Dat laatste webadres blijft
  zoals het was, zodat oude links en bladwijzers blijven werken.
*/
export default async function NiveauVakPage({
  params,
}: {
  params: Promise<{ niveau: string; vak: string }>;
}) {
  const { niveau: niveauSlug, vak: vakSlug } = await params;
  const niveau = vindNiveau(niveauSlug);
  if (!niveau) notFound();

  const session = await getSessionProfile();
  const supabase = await createClient();

  const { data: vak } = await supabase
    .from("vakken")
    .select(
      "id, naam, slug, hoofdstukken(id, titel, volgnummer, gratis, niveau)",
    )
    .eq("slug", vakSlug)
    .single();
  if (!vak) notFound();

  const hoofdstukken = sorteerHoofdstukken(
    (
      vak.hoofdstukken as {
        id: string;
        titel: string;
        volgnummer: number;
        gratis: boolean;
        niveau: string;
      }[]
    ).filter((h) => h.niveau === niveau.slug),
  );
  if (!hoofdstukken.length) notFound();

  const volledigeToegang = heeftVolledigeToegang(session?.profile ?? null);
  // Een woordje bij dit vak, als er een is. De tekst staat in
  // inhoud/vaknoten.ts, zodat aanpassen geen code vraagt.
  const noot = vindVaknoot(niveau.slug, vak.slug);
  const wegwijzer = vindWegwijzer(niveau.slug, vak.slug);

  const { data: kinderen } = session
    ? await supabase
        .from("kinderen")
        .select("id, naam")
        .eq("profile_id", session.userId)
        .order("naam")
    : { data: [] };

  /*
    Extra bundels over het hele vak (supabase/extra-bundels.sql): examens op
    papier, lesbundels, ... Zolang dat bestand niet gedraaid is, geeft dit een
    fout en blijft de lijst gewoon leeg. Verbetersleutels komen enkel mee voor
    beheerder en begeleiders (dat regelt de databank zelf).
  */
  const { data: extraRijen } = await supabase
    .from("extra_bundels")
    .select("id, soort, titel, omschrijving, alleen_begeleiding")
    .eq("vak_id", vak.id)
    .eq("niveau", niveau.slug);
  const extraBundels = sorteerExtraBundels(
    ((extraRijen ?? []) as Pick<
      ExtraBundel,
      "id" | "soort" | "titel" | "omschrijving" | "alleen_begeleiding"
    >[]).filter((b) => magExtraBundel(b, session?.profile ?? null)),
  );

  const uitleg = await haalKorteUitleg(
    supabase,
    hoofdstukken.map((h) => h.id),
  );

  /*
    Bedrijfs- en welzijnswetenschappen (zie lib/leerrichting.ts): per
    hoofdstuk hoeveel vragen zij niet nodig hebben. Zolang
    supabase/niet-voor-dg.sql niet gedraaid is, geeft dit een fout en blijft
    alles zoals het was.
  */
  const richting = await leerrichting();
  const dg = Boolean(wegwijzer?.richtingKeuze) && richting !== "algemeen";
  const dgTelling = new Map<string, { weg: number; totaal: number }>();
  if (wegwijzer?.richtingKeuze) {
    // Per blok van 1000: Supabase geeft nooit meer dan 1000 rijen tegelijk,
    // en geschiedenis Beyond alleen heeft er al meer dan 1200.
    const ids = hoofdstukken.map((h) => h.id);
    for (let van = 0; ; van += 1000) {
      const { data: rijen, error } = await supabase
        .from("vragen")
        .select("id, hoofdstuk_id, niet_voor_dg")
        .in("hoofdstuk_id", ids)
        .order("id")
        .range(van, van + 999);
      if (error || !rijen) break;
      for (const r of rijen as { hoofdstuk_id: string; niet_voor_dg: boolean }[]) {
        const t = dgTelling.get(r.hoofdstuk_id) ?? { weg: 0, totaal: 0 };
        t.totaal++;
        if (r.niet_voor_dg) t.weg++;
        dgTelling.set(r.hoofdstuk_id, t);
      }
      if (rijen.length < 1000) break;
    }
  }
  const dgStatus = (id: string): "deels" | "niet" | undefined => {
    if (!dg) return undefined;
    const t = dgTelling.get(id);
    if (!t || !t.weg) return undefined;
    return t.weg >= t.totaal ? "niet" : "deels";
  };

  // Hoofdstukken die voor de gekozen richting wegvallen (wiskunde basis).
  const zichtbaar = hoofdstukken.filter(
    (h) => !valtWeg(h.titel, wegwijzer?.weglaten, richting),
  );

  const tegels: HoofdstukTegel[] = zichtbaar.map((h) => ({
    dg: dgStatus(h.id),
    id: h.id,
    titel: h.titel,
    korteUitleg: uitleg.get(h.id) ?? null,
    volgnummer: h.volgnummer,
    gratis: h.gratis,
    mag: hoofdstukToegankelijk(h.gratis, session?.profile ?? null),
  }));

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <Link
          href={`/niveaus/${niveau.slug}`}
          className="text-sm text-ink-dim hover:text-ink"
        >
          &larr; {niveau.emoji} {niveau.naam}
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          <span aria-hidden>{vakIcoon(vak.slug)}</span> {vak.naam}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {zichtbaar.length}{" "}
          {zichtbaar.length === 1 ? "hoofdstuk" : "hoofdstukken"} in{" "}
          {niveau.emoji} {niveau.naam}
        </p>

        {/* Febe vroeg in de enquête van november 2026 om een examen over het
            hele vak, terwijl dat er al was: onderaan, onder alle hoofdstukken.
            Daarom ook hier bovenaan, als korte wegwijzer. */}
        {volledigeToegang && (
          <p className="mt-3 flex flex-wrap gap-2 text-sm">
            <Link
              href={`/niveaus/${niveau.slug}/${vak.slug}/examen`}
              className="rounded-full border border-border bg-surface px-3 py-1 text-forest-dark transition hover:border-forest"
            >
              <span aria-hidden>📝</span> Examen van 40 vragen over het hele vak
              {dg && richting === "bedrijf" && " (voor bedrijfswetenschappen)"}
              {dg && richting === "welzijn" && " (voor welzijnswetenschappen)"}
              {dg && richting === "dg" && " (voor bedrijfs- en welzijnswetenschappen)"}
            </Link>
            {!wegwijzer?.richtingKeuze && hoofdstukken.some((h) => isWelzijn(h.titel)) && (
              <Link
                href={`/niveaus/${niveau.slug}/${vak.slug}/examen?welzijn=1`}
                className="rounded-full border border-info/50 bg-surface px-3 py-1 text-info transition hover:border-info"
              >
                <span aria-hidden>🩺</span> Examen voor welzijnswetenschappen
              </Link>
            )}
            <a
              href={`/niveaus/${niveau.slug}/${vak.slug}/cursus`}
              download
              className="rounded-full border border-border bg-surface px-3 py-1 text-forest-dark transition hover:border-forest"
            >
              <span aria-hidden>📚</span> Hele cursus downloaden
            </a>
          </p>
        )}

        {wegwijzer && (
          <div className="mt-5 rounded-xl border-2 border-forest bg-forest/10 px-5 py-4">
            <p className="font-display text-base font-semibold text-forest-dark">
              <span aria-hidden>👉</span> {wegwijzer.titel}
            </p>
            <p className="mt-2 text-sm text-ink">{wegwijzer.tekst}</p>
            {wegwijzer.richtingKeuze && (
              <RichtingKeuze keuze={richting} uitleg={wegwijzer.keuzeUitleg} />
            )}
            {wegwijzer.lijst && (
              <details className="mt-3 rounded-lg border border-forest/40 bg-paper px-4 py-2">
                <summary className="cursor-pointer text-sm font-semibold text-forest-dark">
                  {wegwijzer.lijstKop ?? "Bekijk per hoofdstuk"}
                </summary>
                <ul className="mt-2 space-y-2 pb-1 text-sm text-ink">
                  {wegwijzer.lijst.map((r) => (
                    <li key={r.kop}>
                      <span className="font-semibold">{r.kop}</span>: {r.tekst}
                    </li>
                  ))}
                </ul>
              </details>
            )}
            {wegwijzer.knop && volledigeToegang && (
              <Link
                href={`/niveaus/${niveau.slug}/${vak.slug}/${wegwijzer.knop.href}`}
                className="mt-3 inline-block rounded-full bg-forest px-4 py-2 text-sm font-semibold text-white transition hover:bg-forest-dark"
              >
                {wegwijzer.knop.label} &rarr;
              </Link>
            )}
          </div>
        )}

        {noot && (
          <p className="mt-5 rounded-xl border border-border bg-surface px-5 py-4 text-sm text-ink-dim">
            {noot}
          </p>
        )}

        {!volledigeToegang && (
          <div className="mt-6 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            Volledige toegang tot alle hoofdstukken kost{" "}
            <strong>€{PRIJS_NU_EUR} per schooljaar</strong>
            {TIJDELIJKE_PRIJS && <> ({TIJDELIJKE_PRIJS_KORT})</>}, geldig tot en
            met {schooljaarEindeLabel()} — de opbrengsten gaan volledig naar vzw
            Connectopia.{" "}
            <Link
              href={session ? "/betalen" : "/registreren"}
              className="font-medium text-forest-dark underline-offset-2 hover:underline"
            >
              {session ? "Nu vrijgeven" : "Account maken en starten"}
            </Link>
          </div>
        )}

        {/* Onze titels volgen de vakfiche, niet het boek van het kind. Het
            zoekvak zoekt ook in de vragen, zie app/zoeken/page.tsx. */}
        <Zoekvak niveau={niveau.slug} vak={vak.slug} vakNaam={vak.naam} />

        <HoofdstukTegels
          vakSlug={vak.slug}
          hoofdstukken={tegels}
          kinderen={kinderen ?? []}
        />

        {/* Een examen over het hele vak, onderaan: eerst oefen je per
            hoofdstuk, daarna test je of het blijft plakken. Gevraagd door een
            tester die zich voorbereidt op de Examencommissie. */}
        {volledigeToegang && (
          <Link
            href={`/niveaus/${niveau.slug}/${vak.slug}/examen`}
            className="mt-8 flex items-center justify-between gap-4 rounded-xl border border-border bg-surface px-5 py-4 transition hover:border-forest"
          >
            <span>
              <span className="font-display font-semibold text-ink">
                <span aria-hidden>📝</span> Examen over het hele vak
              </span>
              <span className="mt-0.5 block text-sm text-ink-dim">
                Veertig vragen door elkaar uit alle hoofdstukken. Telt niet mee
                in je voortgang.
              </span>
            </span>
            <span aria-hidden className="text-ink-dim">
              &rarr;
            </span>
          </Link>
        )}

        {/* De hele cursus in één pdf: alle leerbundels van dit vak na elkaar
            (Lotte en Kim, november 2026). Een gewone link, geen Link: het is
            een download en geen pagina. */}
        {volledigeToegang && (
          <a
            href={`/niveaus/${niveau.slug}/${vak.slug}/cursus`}
            download
            className="mt-3 flex items-center justify-between gap-4 rounded-xl border border-border bg-surface px-5 py-4 transition hover:border-forest"
          >
            <span>
              <span className="font-display font-semibold text-ink">
                <span aria-hidden>📚</span> Hele cursus downloaden
              </span>
              <span className="mt-0.5 block text-sm text-ink-dim">
                Alle leerbundels van dit vak samen in één pdf, in de volgorde
                van de hoofdstukken. Handig om af te drukken of door te bladeren.
              </span>
            </span>
            <span aria-hidden className="text-ink-dim">
              &darr;
            </span>
          </a>
        )}

        {/* Extra bundels over het hele vak, los van de hoofdstukken (Kim,
            10 november 2026). Gewone links, want het zijn downloads. */}
        {extraBundels.length > 0 && (
          <section className="mt-8">
            <h2 className="font-display text-lg font-semibold text-ink">
              <span aria-hidden>🗂️</span> Extra bundels
            </h2>
            <p className="mt-0.5 text-sm text-ink-dim">
              Bundels over het hele vak om af te drukken, los van de hoofdstukken.
            </p>
            <ul className="mt-3 space-y-3">
              {extraBundels.map((b) => (
                <li key={b.id}>
                  <a
                    href={`/niveaus/${niveau.slug}/${vak.slug}/extra/${b.id}`}
                    target="_blank"
                    rel="noopener"
                    className="flex items-center justify-between gap-4 rounded-xl border border-border bg-surface px-5 py-4 transition hover:border-forest"
                  >
                    <span>
                      <span className="font-display font-semibold text-ink">
                        <span aria-hidden>
                          {b.alleen_begeleiding ? "🔑" : extraSoort(b.soort).icoon}
                        </span>{" "}
                        {b.titel}
                      </span>
                      <span className="mt-0.5 block text-sm text-ink-dim">
                        {b.omschrijving ?? extraSoort(b.soort).naam}
                        {b.alleen_begeleiding && " · alleen voor de begeleiding"}
                      </span>
                    </span>
                    <span aria-hidden className="text-ink-dim">
                      &darr;
                    </span>
                  </a>
                </li>
              ))}
            </ul>
          </section>
        )}

        <Leidraad />
      </main>
    </>
  );
}
