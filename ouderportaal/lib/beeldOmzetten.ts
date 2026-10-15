/*
  Een iPhone bewaart foto's standaard als HEIC. Safari toont dat, maar Chrome,
  Edge en Firefox niet: daar verschijnt een gebroken afbeelding. Daarom zetten
  we zo'n foto in de browser om naar JPEG vóór hij opgeladen wordt.

  Enkel voor de browser: heic2any heeft een venster nodig.
*/

const HEIC = /\.(heic|heif)$/i;

export function isHeic(naamOfPad: string, soort = "") {
  return /image\/hei[cf]/i.test(soort) || HEIC.test(naamOfPad);
}

/** Geeft een JPEG terug als het een HEIC-foto is, anders het bestand zelf. */
export async function maakWebgeschikt(bestand: File): Promise<File> {
  if (!isHeic(bestand.name, bestand.type)) return bestand;
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
  const nieuweNaam = HEIC.test(naam) ? naam.replace(HEIC, ".jpg") : `${naam}.jpg`;
  return new File([jpeg], nieuweNaam, { type: "image/jpeg" });
}
