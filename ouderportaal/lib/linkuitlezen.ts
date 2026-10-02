import "server-only";

/*
  Een link naar een bericht van sociale media uitlezen, zodat Kim bij
  "In de kijker" alleen het adres moet plakken.

  WAT HIER NIET GEBEURT
  We plaatsen géén echt Facebook- of Instagramvenster op de website. Zo'n
  venster laadt een script van Meta en zet cookies bij elke bezoeker, ook
  bij wie niets aanklikt, en dan moet er een cookiebanner op heel de site.
  Zie de uitleg bovenaan website/content/inkijker.ts.

  Daarom halen wij de gegevens hier éénmalig op, op onze eigen server, en
  bewaren we ze bij ons. De bezoeker van de website doet nooit een verzoek
  naar Facebook, TikTok of YouTube.

  WAT WERKT EN WAT NIET
  - TikTok en YouTube hebben een open leesvenster (oEmbed). Daar krijgen we
    de titel, wie het postte en een voorbeeldbeeld van.
  - Een gewone website (een blog, een nieuwsbericht) zet die gegevens in
    haar og-labels. Die lezen we uit de pagina zelf.
  - Facebook en Instagram zetten er een inlogmuur voor. Daar krijgen we
    meestal niets terug, en dan vult Kim het zelf aan. Dat is geen fout,
    dus we zeggen het vriendelijk in plaats van een foutmelding te geven.
*/

export type Kanaal =
  | "facebook"
  | "instagram"
  | "linkedin"
  | "tiktok"
  | "youtube"
  | "anders";

export type Gevonden = {
  kanaal: Kanaal;
  /* Wie het postte. Leeg als we het niet vonden. */
  van: string | null;
  titel: string | null;
  tekst: string | null;
  /* Het volledige adres van het voorbeeldbeeld, nog niet opgeslagen. */
  beeldUrl: string | null;
  /* Wat we tegen Kim zeggen: hoeveel we konden ophalen. */
  bericht: string;
};

/* Een trage of te grote pagina mag het scherm niet laten hangen. */
const WACHT_MS = 8000;
const MAX_HTML = 512 * 1024;

/* Zonder een gewone browsernaam weigeren veel sites te antwoorden. */
const BROWSERNAAM =
  "Mozilla/5.0 (compatible; ConnectopiaBot/1.0; +https://www.connectopia.one)";

async function haalOp(adres: string, type: "html" | "json") {
  const stop = AbortSignal.timeout(WACHT_MS);
  const antwoord = await fetch(adres, {
    signal: stop,
    redirect: "follow",
    headers: {
      "user-agent": BROWSERNAAM,
      accept:
        type === "json"
          ? "application/json"
          : "text/html,application/xhtml+xml",
      "accept-language": "nl,en;q=0.8",
    },
  });
  if (!antwoord.ok) return null;
  if (type === "json") return antwoord.json();

  /*
    Alleen het begin van de pagina lezen: de og-labels staan in de <head>,
    en een hele nieuwssite binnenhalen heeft geen zin.
  */
  const tekst = await antwoord.text();
  return tekst.slice(0, MAX_HTML);
}

export function kanaalVanLink(link: string): Kanaal {
  let gastheer = "";
  try {
    gastheer = new URL(link).hostname.toLowerCase();
  } catch {
    return "anders";
  }
  if (/(^|\.)facebook\.com$|(^|\.)fb\.watch$/.test(gastheer)) return "facebook";
  if (/(^|\.)instagram\.com$/.test(gastheer)) return "instagram";
  if (/(^|\.)linkedin\.com$/.test(gastheer)) return "linkedin";
  if (/(^|\.)tiktok\.com$/.test(gastheer)) return "tiktok";
  if (/(^|\.)youtube\.com$|(^|\.)youtu\.be$/.test(gastheer)) return "youtube";
  return "anders";
}

/* Een og-label uit de pagina plukken, met of zonder aanhalingstekens. */
function ogLabel(html: string, naam: string): string | null {
  const patronen = [
    new RegExp(
      `<meta[^>]+(?:property|name)=["']${naam}["'][^>]*content=["']([^"']*)["']`,
      "i",
    ),
    new RegExp(
      `<meta[^>]+content=["']([^"']*)["'][^>]*(?:property|name)=["']${naam}["']`,
      "i",
    ),
  ];
  for (const patroon of patronen) {
    const treffer = html.match(patroon);
    if (treffer?.[1]) return ontsnap(treffer[1]).trim() || null;
  }
  return null;
}

/* &amp; en &#39; horen niet op een kaartje. */
function ontsnap(tekst: string): string {
  return tekst
    .replace(/&amp;/g, "&")
    .replace(/&quot;/g, '"')
    .replace(/&#0?39;|&apos;|&rsquo;/g, "'")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&nbsp;/g, " ")
    .replace(/&#(\d+);/g, (_, code) => String.fromCodePoint(Number(code)));
}

function kort(tekst: string | null, maximum: number): string | null {
  if (!tekst) return null;
  const schoon = tekst.replace(/\s+/g, " ").trim();
  if (!schoon) return null;
  if (schoon.length <= maximum) return schoon;
  /* Liever afbreken op een spatie dan middenin een woord. */
  const stuk = schoon.slice(0, maximum);
  const spatie = stuk.lastIndexOf(" ");
  return (spatie > maximum - 25 ? stuk.slice(0, spatie) : stuk) + "…";
}

const OEMBED: Partial<Record<Kanaal, (link: string) => string>> = {
  tiktok: (link) => `https://www.tiktok.com/oembed?url=${encodeURIComponent(link)}`,
  youtube: (link) =>
    `https://www.youtube.com/oembed?format=json&url=${encodeURIComponent(link)}`,
};

type OembedAntwoord = {
  title?: unknown;
  author_name?: unknown;
  thumbnail_url?: unknown;
  provider_name?: unknown;
};

function tekstVeld(waarde: unknown): string | null {
  return typeof waarde === "string" && waarde.trim() ? waarde.trim() : null;
}

export async function leesLink(link: string): Promise<Gevonden> {
  const adres = link.trim();
  const kanaal = kanaalVanLink(adres);
  const leeg: Gevonden = {
    kanaal,
    van: null,
    titel: null,
    tekst: null,
    beeldUrl: null,
    bericht: "",
  };

  if (!/^https:\/\//i.test(adres)) {
    return { ...leeg, bericht: "De link moet met https:// beginnen." };
  }

  /* 1. Het open leesvenster van TikTok en YouTube. */
  const oembed = OEMBED[kanaal];
  if (oembed) {
    try {
      const data = (await haalOp(oembed(adres), "json")) as OembedAntwoord | null;
      if (data) {
        const titel = kort(tekstVeld(data.title), 120);
        return {
          kanaal,
          van: tekstVeld(data.author_name),
          titel,
          tekst: kort(tekstVeld(data.title), 300),
          beeldUrl: tekstVeld(data.thumbnail_url),
          bericht: titel
            ? "Opgehaald. Kijk het even na en pas aan wat je anders wil."
            : "Niets gevonden. Vul het zelf even aan.",
        };
      }
    } catch {
      /* Een leesvenster dat niet antwoordt, is geen reden om te stoppen. */
    }
  }

  /* 2. De og-labels van de pagina zelf. */
  try {
    const html = (await haalOp(adres, "html")) as string | null;
    if (html) {
      const titel = kort(
        ogLabel(html, "og:title") ?? kort(titelTag(html), 120),
        120,
      );
      const tekst = kort(ogLabel(html, "og:description"), 300);
      const beeldUrl = ogLabel(html, "og:image");
      const van =
        ogLabel(html, "og:site_name") ?? ogLabel(html, "article:author");

      if (titel || tekst || beeldUrl) {
        return {
          kanaal,
          van,
          titel,
          tekst,
          beeldUrl: beeldUrl && /^https:\/\//i.test(beeldUrl) ? beeldUrl : null,
          bericht: "Opgehaald. Kijk het even na en pas aan wat je anders wil.",
        };
      }
    }
  } catch {
    /* Ook hier: niets gevonden is geen fout. */
  }

  return {
    ...leeg,
    bericht:
      kanaal === "facebook" || kanaal === "instagram"
        ? "Facebook en Instagram geven dit niet vrij. Schrijf er zelf even bij waar het over gaat."
        : "Niets gevonden bij deze link. Vul het zelf even aan.",
  };
}

function titelTag(html: string): string | null {
  const treffer = html.match(/<title[^>]*>([\s\S]{0,300}?)<\/title>/i);
  return treffer?.[1] ? ontsnap(treffer[1]).trim() || null : null;
}

/* ──────────────────────────────────────────────────────────────── */

const MAX_BEELD = 5 * 1024 * 1024;

const SOORTEN: Record<string, string> = {
  "image/jpeg": "jpg",
  "image/png": "png",
  "image/webp": "webp",
  "image/gif": "gif",
};

/*
  Het voorbeeldbeeld halen we binnen en bewaren we in onze eigen bak. Zo
  doet de bezoeker van de website nooit een verzoek naar TikTok of YouTube,
  en blijft het beeld staan als hun adres verloopt.
*/
export async function haalBeeldBinnen(
  adres: string,
): Promise<{ bytes: Uint8Array; soort: string; extensie: string } | null> {
  if (!/^https:\/\//i.test(adres)) return null;

  const antwoord = await fetch(adres, {
    signal: AbortSignal.timeout(WACHT_MS),
    redirect: "follow",
    headers: { "user-agent": BROWSERNAAM, accept: "image/*" },
  });
  if (!antwoord.ok) return null;

  const soort = (antwoord.headers.get("content-type") || "")
    .split(";")[0]
    .trim()
    .toLowerCase();
  const extensie = SOORTEN[soort];
  if (!extensie) return null;

  const buffer = await antwoord.arrayBuffer();
  if (buffer.byteLength === 0 || buffer.byteLength > MAX_BEELD) return null;

  return { bytes: new Uint8Array(buffer), soort, extensie };
}
