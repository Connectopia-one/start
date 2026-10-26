import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { Quiz } from "@/components/Quiz";
import { Leidraad } from "@/components/Leidraad";
import { getSessionProfile } from "@/lib/auth";
import { heeftVolledigeToegang } from "@/lib/toegang";
import { createClient } from "@/lib/supabase/server";
import {
  PRIJS_NU_EUR,
  TIJDELIJKE_PRIJS,
  TIJDELIJKE_PRIJS_KORT,
} from "@/lib/prijs";
import { schooljaarEindeLabel } from "@/lib/schooljaar";
import { vindNiveau } from "@/lib/niveaus";
import { isTaalvak } from "@/lib/taalvak";
import { isRekenvak } from "@/lib/rekenvak";
import { vindPrent } from "@/lib/prent";
import type { VraagContext } from "@/components/Quiz";
import type { Woord } from "@/components/Leestekst";
import { vakIcoon } from "@/lib/vakbeeld";
import { maakVraag } from "@/lib/vraagrij";
import { EXAMENS_VOOR_STER } from "@/lib/examen";

/*
  Een examen over een heel vak binnen één niveau.

  Gevraagd op 12 oktober 2026 door een tester die zich via dit platform
  voorbereidt op de Examencommissie: "Nu is het heel goed per hoofdstuk toetsen
  (wat ik zeker goed vind en behouden moet worden) maar ook zou ik graag een
  toets / examen per vak hebben. Wat je dan kan doen om je totale kennis te
  testen." Zelfde mail: "Het zijn ook altijd wel dezelfde vragen."

  Drie keuzes die daaruit volgen:

  1. De vragen worden elke keer opnieuw door elkaar getrokken uit álle
     hoofdstukken van dat vak. Herladen geeft een ander examen; dat is meteen
     het antwoord op dat tweede punt.
  2. Er wordt niets bijgehouden. Geen antwoorden, geen sticker, geen vinkje bij
     een hoofdstuk. Een examen meet wat je al kan; het hoort de voortgang van
     hoofdstukken die je nog niet maakte niet in te kleuren. Daarom krijgt de
     Quiz hier examen={true} en geen hoofdstukId.
  3. De pittige hoofdstukken blijven eruit. Die liggen bewust boven de leerstof
     van het niveau, en een examen hoort te meten of je het niveau zelf
     beheerst.
*/

const AANTAL_VRAGEN = 40;
const PITTIG = /\s*—\s*pittig$/i;

/* Door elkaar, zonder de lijst van de aanroeper aan te raken. */
function schud<T>(lijst: T[]): T[] {
  const kopie = [...lijst];
  for (let i = kopie.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [kopie[i], kopie[j]] = [kopie[j], kopie[i]];
  }
  return kopie;
}

/*
  Zoals op het echte examen: een vast deel van de vragen in de vormen van de
  Examencommissie (een tabel, een keuzelijst, volgorde, koppelen, slepen,
  klikken, open of tekenen), zodat het niet van het toeval afhangt of een kind
  ze tegenkomt. Heeft een vak er minder, dan komen ze er allemaal in.
  Gevraagd door Kim op 26 oktober 2026, eerst tien van de veertig en dezelfde
  avond de helft, "zodat het examen echt lijkt".
*/
const EXAMENVORMEN_MINSTENS = 20;
const GEWONE_VORMEN = new Set(["meerkeuze", "invultekst", "waarofniet"]);

function kiesExamenvragen(lijst: { id: string; type: string }[]): string[] {
  const vormen = schud(lijst.filter((v) => !GEWONE_VORMEN.has(v.type)));
  const vast = vormen.slice(0, EXAMENVORMEN_MINSTENS);
  const gekozen = new Set(vast.map((v) => v.id));
  const rest = schud(lijst.filter((v) => !gekozen.has(v.id))).slice(
    0,
    AANTAL_VRAGEN - vast.length,
  );
  return [...vast, ...rest].map((v) => v.id);
}

/*
  De vragen van één casus komen na elkaar, op de plaats van de eerste, zoals
  op het examen. Elke vraag draagt haar casus zelf, dus ook een losse vraag uit
  een casus is te beantwoorden; samen leest het wel rustiger.
*/
function casussenSamen<T extends { casus?: string | null }>(lijst: T[]): T[] {
  const uit: T[] = [];
  const gedaan = new Set<string>();
  for (const v of lijst) {
    if (!v.casus) {
      uit.push(v);
      continue;
    }
    if (gedaan.has(v.casus)) continue;
    gedaan.add(v.casus);
    uit.push(...lijst.filter((w) => w.casus === v.casus));
  }
  return uit;
}

export default async function ExamenPage({
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
      "id, naam, slug, hoofdstukken(id, titel, niveau, leestekst, woordenlijst)",
    )
    .eq("slug", vakSlug)
    .single();
  if (!vak) notFound();

  const hoofdstukken = (
    vak.hoofdstukken as {
      id: string;
      titel: string;
      niveau: string;
      leestekst: string | null;
      woordenlijst: Woord[] | null;
    }[]
  ).filter((h) => h.niveau === niveau.slug && !PITTIG.test(h.titel));
  if (!hoofdstukken.length) notFound();

  const terug = `/niveaus/${niveau.slug}/${vak.slug}`;
  const volledigeToegang = heeftVolledigeToegang(session?.profile ?? null);

  /*
    Een examen loopt over alle hoofdstukken heen, ook de hoofdstukken die niet
    gratis zijn. Het hoort dus achter een account, net als de uitdagingshoek.
  */
  if (!volledigeToegang) {
    return (
      <>
        <Header
          naam={session?.profile?.full_name}
          rol={session?.profile?.role}
        />
        <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
          <Link href={terug} className="text-sm text-ink-dim hover:text-ink">
            &larr; {vak.naam}
          </Link>
          <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
            Examen {vak.naam}
          </h1>
          <div className="mt-6 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            Een examen gaat over alle hoofdstukken van dit vak samen, dus het
            hoort bij de volledige toegang. Die kost €{PRIJS_NU_EUR} per
            schooljaar
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
          <Leidraad />
        </main>
      </>
    );
  }

  /*
    Eerst enkel de nummers ophalen en daarvan veertig trekken, en pas dan die
    veertig rijen zelf. Een vak heeft al snel vijfhonderd vragen; die allemaal
    binnenhalen om er veertig te houden, laat een gsm onnodig wachten.
  */
  const hoofdstukIds = hoofdstukken.map((h) => h.id);
  const { data: nummers } = await supabase
    .from("vragen")
    .select("id, type")
    .in("hoofdstuk_id", hoofdstukIds);

  const gekozen = kiesExamenvragen(
    (nummers ?? []) as { id: string; type: string }[],
  );

  const { data: vragenRuw } = gekozen.length
    ? await supabase.from("vragen").select("*").in("id", gekozen)
    : { data: [] };

  const vragen = casussenSamen(
    schud(
      await Promise.all(
        (vragenRuw ?? []).map((rij) => maakVraag(supabase, rij)),
      ),
    ),
  );

  /*
    Een vraag over een leestekst ("in die tekst over de schoolreis vertrekt de
    bus om zes uur") of over een prent is zonder die tekst of die prent niet te
    beantwoorden. Bij een hoofdstuk staat ze boven de hele reeks; hier loopt
    alles door elkaar, dus geeft de Quiz ze mee per hoofdstuk en zet ze boven de
    vraag waar je op staat. Door Kim gemeld op 13 oktober 2026.
  */
  const contexten: Record<string, VraagContext> = {};
  for (const h of hoofdstukken) {
    const prent = vindPrent(vak.slug as string, h.titel);
    if (!h.leestekst && !prent) continue;
    contexten[h.id] = {
      leestekst: h.leestekst,
      woorden: h.woordenlijst ?? [],
      prent,
    };
  }

  const { data: kinderen } = session
    ? await supabase
        .from("kinderen")
        .select("*")
        .eq("profile_id", session.userId)
        .order("naam")
    : { data: [] };

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link href={terug} className="text-sm text-ink-dim hover:text-ink">
          &larr; {vakIcoon(vak.slug)} {vak.naam}
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          Examen {vak.naam}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {vragen.length} vragen door elkaar uit de {hoofdstukken.length}{" "}
          hoofdstukken van {niveau.emoji} {niveau.naam}.
        </p>

        <div className="mt-5 rounded-xl border border-border bg-surface px-5 py-4 text-sm text-ink-dim">
          <p>
            Dit examen telt niet mee in je voortgang. De vinkjes en sterren bij
            de hoofdstukken blijven zoals ze zijn, dus je kan het zo vaak
            proberen als je wil.
          </p>
          <p className="mt-2">
            Leg dit examen {EXAMENS_VOOR_STER} keer zonder fouten af en je
            verdient de examenster van dit vak. Een examen dat je met Opnieuw
            proberen overdoet, telt niet mee: dan krijg je dezelfde vragen.
          </p>
          <p className="mt-2">
            Elke keer dat je dit examen opnieuw opent, krijg je andere vragen.{" "}
            <Link
              href={`${terug}/examen`}
              className="font-medium text-forest-dark underline-offset-2 hover:underline"
            >
              Nieuw examen
            </Link>
          </p>
        </div>

        <div className="mt-8">
          {vragen.length === 0 ? (
            <p className="rounded-xl border border-border bg-surface px-5 py-4 text-sm text-ink-dim">
              Er staan nog geen vragen bij dit vak.
            </p>
          ) : (
            <Quiz
              vragen={vragen}
              kinderen={(kinderen ?? []).map((k) => ({
                id: k.id,
                naam: k.naam,
                toonVoortgang: Boolean(k.toon_voortgang),
              }))}
              taalvak={isTaalvak(vak.slug)}
              rekenmachine={isRekenvak(vak.slug as string)}
              contexten={contexten}
              /* Daarmee telt een feilloos examen mee voor de examenster van dit
                 vak. Het examen blijft buiten de voortgang; zie
                 supabase/examens.sql. */
              examenVakId={vak.id as string}
              examenNiveau={niveau.slug}
              examen
            />
          )}
        </div>

        <Leidraad />
      </main>
    </>
  );
}
