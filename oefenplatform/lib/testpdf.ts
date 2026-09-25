import "server-only";
import { readFile } from "node:fs/promises";
import path from "node:path";
import fontkit from "@pdf-lib/fontkit";
import { schrijfKeuzes } from "@/lib/antwoord";
import { PDFDocument, rgb, type PDFFont, type PDFPage } from "pdf-lib";

/*
  Maakt van één opgeloste test een pdf, zodat een begeleider die kan
  downloaden en bewaren zoals een leerbundel.

  We tekenen de pdf zelf met pdf-lib, dus zonder browser op de server. Dat
  houdt het licht genoeg om gewoon op Vercel te draaien. Gevolg: de
  tekeningetjes bij een breukvraag komen er niet in; daar staat een korte
  omschrijving tussen haakjes in de plaats.
*/

const A4 = { breedte: 595.28, hoogte: 841.89 };
const RAND = 52;
const REGEL = 14;

const GROEN = rgb(0.18, 0.29, 0.13);
const INKT = rgb(0.13, 0.13, 0.12);
const GRIJS = rgb(0.42, 0.42, 0.4);
const ROOD = rgb(0.65, 0.16, 0.16);

export type PdfVraag = {
  id: string;
  type: "meerkeuze" | "invultekst" | "waarofniet";
  vraag: string;
  opties: string[] | null;
  antwoord: number | string | boolean;
  uitleg: string | null;
};

export type PdfPoging = {
  vraag_id: string;
  correct: boolean;
  gegeven_antwoord: number | string | boolean | null;
  beantwoord_op: string;
};

export type PdfGegevens = {
  kindNaam: string;
  gezinNaam: string;
  vak: string;
  hoofdstuk: string;
  vragen: PdfVraag[];
  /* Alle pogingen van dit kind op dit hoofdstuk, nieuwste eerst. */
  pogingen: PdfPoging[];
  /* Bij begrijpend lezen: de tekst waar de vragen over gaan, met de
     woordenlijst. Zonder die tekst is zo'n test op papier niet te volgen. */
  leestekst?: string | null;
  woordenlijst?: { woord: string; uitleg: string }[] | null;
};

/*
  De vraagtekst bevat soms een code die het platform als tekening toont, zoals
  {{figuur cirkel 3/8}}. Op papier zetten we daar een omschrijving neer.
*/
function leesbaar(tekst: string): string {
  return tekst
    .replace(
      /\{\{\s*figuur\s+(\S+)\s+(\d+)\/(\d+)\s*\}\}/g,
      "($1: $2 van de $3 gekleurd)",
    )
    .replace(
      /\{\{\s*kleur\s+(\S+)\s+(\d+)\s*\}\}/g,
      "($1 in $2 stukken om te kleuren)",
    )
    .replace(
      /\{\{\s*sleep\s+klein-groot\s*\}\}/g,
      "(op volgorde zetten, klein naar groot)",
    )
    .replace(
      /\{\{\s*sleep\s+groot-klein\s*\}\}/g,
      "(op volgorde zetten, groot naar klein)",
    )
    .replace(/\{\{[^}]*\}\}/g, "")
    .replace(/[ \t]+/g, " ")
    .trim();
}

export function schrijfAntwoord(
  vraag: PdfVraag,
  waarde: number | string | boolean | number[] | null,
): string {
  if (waarde === null || waarde === undefined || waarde === "") return "—";
  if (vraag.type === "meerkeuze") return schrijfKeuzes(vraag.opties, waarde);
  if (vraag.type === "waarofniet")
    return waarde === true ? "Waar" : "Niet waar";
  return String(waarde);
}

let letterCache: { gewoon: Buffer; vet: Buffer } | null = null;

async function letters() {
  if (letterCache) return letterCache;
  const map = path.join(process.cwd(), "lettertypes");
  const [gewoon, vet] = await Promise.all([
    readFile(path.join(map, "DejaVuSans.ttf")),
    readFile(path.join(map, "DejaVuSans-Bold.ttf")),
  ]);
  letterCache = { gewoon, vet };
  return letterCache;
}

/*
  DejaVu kent heel veel tekens, maar geen emoji. Eén teken dat het lettertype
  niet kent laat pdf-lib de hele pdf weigeren, dus halen we die er vooraf uit.
*/
function maakVeilig(gekend: Set<number>) {
  return (tekst: string) =>
    [...tekst]
      .filter((teken) => gekend.has(teken.codePointAt(0) ?? 0))
      .join("");
}

function breek(
  tekst: string,
  letter: PDFFont,
  grootte: number,
  breedte: number,
): string[] {
  const regels: string[] = [];
  for (const alinea of tekst.split("\n")) {
    let regel = "";
    for (const woord of alinea.split(/\s+/).filter(Boolean)) {
      const poging = regel ? `${regel} ${woord}` : woord;
      if (letter.widthOfTextAtSize(poging, grootte) <= breedte) {
        regel = poging;
      } else {
        if (regel) regels.push(regel);
        regel = woord;
      }
    }
    regels.push(regel);
  }
  return regels.length ? regels : [""];
}

export async function maakTestPdf(g: PdfGegevens): Promise<Uint8Array> {
  const pdf = await PDFDocument.create();
  pdf.registerFontkit(fontkit);

  const { gewoon, vet } = await letters();
  const letter = await pdf.embedFont(gewoon, { subset: true });
  const letterVet = await pdf.embedFont(vet, { subset: true });

  const gekend = new Set<number>([
    ...letter.getCharacterSet(),
    ...letterVet.getCharacterSet(),
  ]);
  const veilig = maakVeilig(gekend);

  const inhoudBreedte = A4.breedte - 2 * RAND;
  let bladzijde: PDFPage = pdf.addPage([A4.breedte, A4.hoogte]);
  let y = A4.hoogte - RAND;

  function nieuweBladzijde() {
    bladzijde = pdf.addPage([A4.breedte, A4.hoogte]);
    y = A4.hoogte - RAND;
  }

  function ruimte(nodig: number) {
    if (y - nodig < RAND) nieuweBladzijde();
  }

  function schrijf(
    tekst: string,
    opties: {
      grootte?: number;
      vetjes?: boolean;
      kleur?: typeof INKT;
      inspringen?: number;
    } = {},
  ) {
    const grootte = opties.grootte ?? 10;
    const gebruikt = opties.vetjes ? letterVet : letter;
    const x = RAND + (opties.inspringen ?? 0);
    const regels = breek(
      veilig(tekst),
      gebruikt,
      grootte,
      inhoudBreedte - (opties.inspringen ?? 0),
    );
    for (const regel of regels) {
      ruimte(REGEL);
      bladzijde.drawText(regel, {
        x,
        y: y - grootte,
        size: grootte,
        font: gebruikt,
        color: opties.kleur ?? INKT,
      });
      y -= Math.max(REGEL, grootte + 4);
    }
  }

  /* De laatste poging per vraag, en hoe vaak er geprobeerd werd. */
  const laatste = new Map<string, PdfPoging>();
  const keer = new Map<string, number>();
  for (const p of g.pogingen) {
    if (!laatste.has(p.vraag_id)) laatste.set(p.vraag_id, p);
    keer.set(p.vraag_id, (keer.get(p.vraag_id) ?? 0) + 1);
  }

  const beantwoord = g.vragen.filter((v) => laatste.has(v.id));
  const juist = beantwoord.filter((v) => laatste.get(v.id)!.correct).length;

  /* Kop */
  schrijf(`${g.vak} — ${g.hoofdstuk}`, {
    grootte: 16,
    vetjes: true,
    kleur: GROEN,
  });
  y -= 4;
  schrijf(`${g.kindNaam} · gezin ${g.gezinNaam}`, {
    grootte: 10,
    kleur: GRIJS,
  });
  schrijf(
    `${beantwoord.length} van de ${g.vragen.length} vragen beantwoord, waarvan ${juist} juist.`,
    { grootte: 10, kleur: GRIJS },
  );
  schrijf(
    `Afgedrukt op ${new Date().toLocaleDateString("nl-BE", { day: "numeric", month: "long", year: "numeric" })}. Per vraag staat het antwoord van de laatste poging.`,
    { grootte: 9, kleur: GRIJS },
  );
  y -= 10;

  /* Bij begrijpend lezen eerst de tekst zelf, anders slaan de vragen nergens
     op. De sterretjes rond moeilijke woorden zijn schermopmaak; op papier
     staat de uitleg gewoon in de woordenlijst eronder. */
  if (g.leestekst) {
    schrijf("De tekst", { grootte: 12, vetjes: true, kleur: GROEN });
    y -= 2;
    for (const alinea of g.leestekst.split(/\n\s*\n/)) {
      const stuk = alinea.trim().replace(/\*([^*\n]+)\*/g, "$1");
      if (!stuk) continue;
      schrijf(stuk, { grootte: 10 });
      y -= 4;
    }
    const lijst = g.woordenlijst ?? [];
    if (lijst.length) {
      y -= 2;
      schrijf("Moeilijke woorden", { grootte: 11, vetjes: true });
      for (const w of lijst) {
        schrijf(`${w.woord} — ${w.uitleg}`, { grootte: 9, kleur: GRIJS, inspringen: 10 });
      }
    }
    y -= 12;
  }

  g.vragen.forEach((vraag, i) => {
    const poging = laatste.get(vraag.id);
    ruimte(70);
    y -= 6;

    schrijf(`Vraag ${i + 1}`, { grootte: 9, vetjes: true, kleur: GRIJS });
    schrijf(leesbaar(vraag.vraag), { grootte: 11 });

    if (!poging) {
      schrijf("Nog niet geprobeerd.", {
        grootte: 10,
        kleur: GRIJS,
        inspringen: 12,
      });
      return;
    }

    const gegeven = schrijfAntwoord(vraag, poging.gegeven_antwoord);
    schrijf(
      `${poging.correct ? "Juist" : "Fout"} — ${g.kindNaam} antwoordde: ${gegeven}`,
      {
        grootte: 10,
        vetjes: true,
        kleur: poging.correct ? GROEN : ROOD,
        inspringen: 12,
      },
    );

    if (!poging.correct) {
      schrijf(
        `Het juiste antwoord was: ${schrijfAntwoord(vraag, vraag.antwoord)}`,
        {
          grootte: 10,
          inspringen: 12,
        },
      );
    }

    if (vraag.uitleg) {
      schrijf(vraag.uitleg, { grootte: 9, kleur: GRIJS, inspringen: 12 });
    }

    const aantal = keer.get(vraag.id) ?? 1;
    const datum = new Date(poging.beantwoord_op).toLocaleDateString("nl-BE", {
      day: "numeric",
      month: "long",
      year: "numeric",
    });
    schrijf(aantal > 1 ? `${datum} · ${aantal} keer geprobeerd` : datum, {
      grootte: 8,
      kleur: GRIJS,
      inspringen: 12,
    });
  });

  /* Voetnoot op elke bladzijde. */
  const bladen = pdf.getPages();
  bladen.forEach((blad, i) => {
    blad.drawText(
      veilig(
        `Connectopia · opvolging plusklas · ${i + 1} van ${bladen.length}`,
      ),
      {
        x: RAND,
        y: RAND - 22,
        size: 8,
        font: letter,
        color: GRIJS,
      },
    );
  });

  pdf.setTitle(`${g.vak} — ${g.hoofdstuk} — ${g.kindNaam}`);
  return pdf.save();
}
