/*
  Een iPhone bewaart foto's standaard als HEIC. Safari toont dat, maar Chrome,
  Edge en Firefox niet: daar verschijnt een gebroken afbeelding. Daarom zetten
  we zo'n foto in de browser om naar JPEG vóór hij opgeladen wordt.

  De naam is niet te vertrouwen: een HEIC-foto komt soms binnen als ".jpg".
  Daarom kijken we ook naar de eerste bytes van het bestand zelf.

  Enkel voor de browser: heic2any en het tekendoek hebben een venster nodig.
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
  if (tekst.startsWith("II*\0") || tekst.startsWith("MM\0*")) return "dng";
  if (tekst.slice(4, 8) === "ftyp") {
    const merk = tekst.slice(8, 12);
    if (/^(avif|avis)$/.test(merk)) return "avif";
    if (/^(heic|heix|hevc|hevx|heim|heis|mif1|msf1)$/.test(merk)) return "heic";
    return `ftyp-${merk}`;
  }
  return "onbekend";
}

/** Geeft een JPEG terug als het een HEIC- of RAW-foto is, anders het bestand zelf. */
export async function maakWebgeschikt(bestand: File): Promise<File> {
  const soort = await soortVanInhoud(bestand);
  if (soort === "dng" || /\.dng$/i.test(bestand.name)) return dngNaarJpeg(bestand, bestand.name);
  if (soort === "heic" || isHeic(bestand.name, bestand.type)) return heicNaarJpeg(bestand, bestand.name);
  return bestand;
}

function jpegNaam(naam: string) {
  const basis = naam.replace(/\.[^./]*$/, "");
  return `${basis || "foto"}.jpg`;
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
  return new File([jpeg], jpegNaam(naam), { type: "image/jpeg" });
}

/*
  Een iPhone met ProRAW aan bewaart foto's als DNG: ruwe sensorgegevens van
  zo'n 20 MB die geen enkele browser toont. Gelukkig zit er altijd een gewone
  JPEG-voorvertoning in. Die halen we eruit, draaien hem zoals de foto
  getrokken werd, en maken er een JPEG van hoogstens 2560 pixels van.
*/
export async function dngNaarJpeg(blob: Blob, naam: string): Promise<File> {
  const buf = await blob.arrayBuffer();
  const { kandidaten, stand, sensor } = jpegsInTiff(buf);

  let beste: ImageBitmap | null = null;
  for (const [begin, lengte] of kandidaten) {
    try {
      const bmp = await createImageBitmap(new Blob([buf.slice(begin, begin + lengte)], { type: "image/jpeg" }));
      if (!beste || bmp.width * bmp.height > beste.width * beste.height) {
        beste?.close();
        beste = bmp;
      } else {
        bmp.close();
      }
    } catch {
      /* Ruwe gegevens (lossless JPEG) kan de browser niet lezen: volgende. */
    }
  }
  if (!beste) throw new Error(`In de RAW-foto "${naam}" zit geen voorvertoning die de browser kan lezen.`);

  /*
    Een iPhone legt de voorvertoning vaak al rechtop, terwijl de DNG nog zegt
    dat er gedraaid moet worden. Draaien deed de foto dan op zijn zij vallen.
    Daarom draaien we enkel een kwartslag als de voorvertoning nog dezelfde
    vorm heeft als de sensor (allebei liggend), en nooit voor de andere standen.
  */
  const nogLiggend = sensor.w > 0 && beste.width > beste.height === sensor.w > sensor.h;
  const echteStand = stand >= 5 && stand <= 8 && nogLiggend ? stand : 1;
  const jpeg = await tekenAlsJpeg(beste, echteStand);
  beste.close();
  return new File([jpeg], jpegNaam(naam), { type: "image/jpeg" });
}

/** Zoekt in een TIFF/DNG alle stukken die met een JPEG-begin (FF D8) starten. */
function jpegsInTiff(buf: ArrayBuffer) {
  const v = new DataView(buf);
  const le = v.getUint16(0) === 0x4949;
  const u16 = (o: number) => v.getUint16(o, le);
  const u32 = (o: number) => v.getUint32(o, le);
  const kandidaten: [number, number][] = [];
  let stand = 1;
  const sensor = { w: 0, h: 0 };
  const gezien = new Set<number>();

  function waarden(o: number): number[] {
    const type = u16(o + 2);
    const aantal = u32(o + 4);
    const grootte = type === 3 ? 2 : 4;
    const plek = aantal * grootte <= 4 ? o + 8 : u32(o + 8);
    const uit: number[] = [];
    for (let i = 0; i < Math.min(aantal, 4096); i++) {
      if (plek + i * grootte + grootte > buf.byteLength) break;
      uit.push(type === 3 ? u16(plek + i * grootte) : u32(plek + i * grootte));
    }
    return uit;
  }

  function leesIfd(start: number, eerste: boolean) {
    let ifd = start;
    while (ifd > 0 && ifd + 2 < buf.byteLength && !gezien.has(ifd)) {
      gezien.add(ifd);
      const n = u16(ifd);
      const tags = new Map<number, number[]>();
      for (let i = 0; i < n; i++) {
        const o = ifd + 2 + i * 12;
        if (o + 12 > buf.byteLength) break;
        tags.set(u16(o), waarden(o));
      }
      if (eerste && tags.get(0x0112)) stand = tags.get(0x0112)![0];
      const [w, h] = [tags.get(0x0100)?.[0] ?? 0, tags.get(0x0101)?.[0] ?? 0];
      if (w * h > sensor.w * sensor.h) Object.assign(sensor, { w, h });
      const stukken: [number[] | undefined, number[] | undefined][] = [
        [tags.get(0x0111), tags.get(0x0117)],
        [tags.get(0x0144), tags.get(0x0145)],
        [tags.get(0x0201), tags.get(0x0202)],
      ];
      for (const [plekken, lengtes] of stukken) {
        if (plekken?.length === 1 && lengtes?.length === 1) {
          const [b, l] = [plekken[0], lengtes[0]];
          if (b + l <= buf.byteLength && v.getUint8(b) === 0xff && v.getUint8(b + 1) === 0xd8) {
            kandidaten.push([b, l]);
          }
        }
      }
      for (const sub of tags.get(0x014a) ?? []) leesIfd(sub, false);
      if (eerste) eerste = false;
      ifd = ifd + 2 + n * 12 + 4 <= buf.byteLength ? u32(ifd + 2 + n * 12) : 0;
    }
  }

  leesIfd(u32(4), true);
  kandidaten.sort((a, b) => b[1] - a[1]);
  return { kandidaten, stand, sensor };
}

/** Draait een foto een kwartslag naar links of naar rechts. */
export async function draaiFoto(blob: Blob, naam: string, richting: "links" | "rechts"): Promise<File> {
  const bmp = await createImageBitmap(blob);
  const jpeg = await tekenAlsJpeg(bmp, richting === "rechts" ? 6 : 8);
  bmp.close();
  return new File([jpeg], jpegNaam(naam), { type: "image/jpeg" });
}

async function tekenAlsJpeg(bmp: ImageBitmap, stand: number): Promise<Blob> {
  const schaal = Math.min(1, 2560 / Math.max(bmp.width, bmp.height));
  const w = Math.round(bmp.width * schaal);
  const h = Math.round(bmp.height * schaal);
  const gedraaid = stand >= 5 && stand <= 8;
  const doek = document.createElement("canvas");
  doek.width = gedraaid ? h : w;
  doek.height = gedraaid ? w : h;
  const ctx = doek.getContext("2d")!;
  /* De EXIF-stand: 3 = ondersteboven, 6 = kwartslag rechts, 8 = kwartslag links. */
  const vormen: Record<number, [number, number, number, number, number, number]> = {
    2: [-1, 0, 0, 1, w, 0],
    3: [-1, 0, 0, -1, w, h],
    4: [1, 0, 0, -1, 0, h],
    5: [0, 1, 1, 0, 0, 0],
    6: [0, 1, -1, 0, h, 0],
    7: [0, -1, -1, 0, h, w],
    8: [0, -1, 1, 0, 0, w],
  };
  const vorm = vormen[stand];
  if (vorm) ctx.setTransform(...vorm);
  ctx.drawImage(bmp, 0, 0, w, h);
  return new Promise((klaar, mis) =>
    doek.toBlob((b) => (b ? klaar(b) : mis(new Error("Omzetten mislukt."))), "image/jpeg", 0.85),
  );
}
