/*
  Een iPhone bewaart foto's standaard als HEIC. Safari toont dat, maar Chrome,
  Edge en Firefox niet: daar verschijnt een gebroken afbeelding. Daarom zetten
  we zo'n foto in de browser om naar JPEG vóór hij opgeladen wordt.

  De naam is niet te vertrouwen: een HEIC-foto komt soms binnen als ".jpg".
  Daarom kijken we ook naar de eerste bytes van het bestand zelf.

  Enkel voor de browser: heic2any heeft een venster nodig.
*/

const HEIC = /\.(heic|heif)$/i;

export function isHeic(naamOfPad: string, soort = "") {
  return /image\/hei[cf]/i.test(soort) || HEIC.test(naamOfPad);
}

/** Herkent het formaat aan de eerste bytes, los van naam of opgegeven soort. */
export async function soortVanInhoud(blob: Blob): Promise<string> {
  const b = new Uint8Array(await blob.slice(0, 16).arrayBuffer());
  const tekst = String.fromCharCode(...b);
  if (b[0] === 0xff && b[1] === 0xd8) return "jpeg";
  if (tekst.startsWith("\x89PNG")) return "png";
  if (tekst.startsWith("GIF8")) return "gif";
  if (tekst.startsWith("RIFF") && tekst.slice(8, 12) === "WEBP") return "webp";
  if (tekst.slice(4, 8) === "ftyp") {
    const merk = tekst.slice(8, 12);
    if (/^(avif|avis)$/.test(merk)) return "avif";
    if (/^(heic|heix|hevc|hevx|heim|heis|mif1|msf1)$/.test(merk)) return "heic";
    return `ftyp-${merk}`;
  }
  return "onbekend";
}

/** Geeft een JPEG terug als het een HEIC-foto is, anders het bestand zelf. */
export async function maakWebgeschikt(bestand: File): Promise<File> {
  if (!isHeic(bestand.name, bestand.type) && (await soortVanInhoud(bestand)) !== "heic") {
    return bestand;
  }
  return heicNaarJpeg(bestand, bestand.name);
}

export async function heicNaarJpeg(blob: Blob, naam: string): Promise<File> {
  const heic2any = (await import("heic2any")).default;
  let uit: Blob | Blob[];
  try {
    uit = await heic2any({ blob, toType: "image/jpeg", quality: 0.85 });
  } catch {
    throw new Error(`De foto "${naam}" kon niet omgezet worden naar JPEG.`);
  }
  const jpeg = Array.isArray(uit) ? uit[0] : uit;
  const basis = naam.replace(/\.[^./]*$/, "");
  return new File([jpeg], `${basis || "foto"}.jpg`, { type: "image/jpeg" });
}
