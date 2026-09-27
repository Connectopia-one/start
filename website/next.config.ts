import type { NextConfig } from "next";

/*
  De site draait op Vercel als een gewone Next-app. Dat is nodig sinds het
  prikbord: bezoekers hangen daar zelf briefjes op, en dat vraagt een
  server die met de databank praat.
*/
const nextConfig: NextConfig = {
  /*
    Van de oude site naar de nieuwe.

    Op de one.com-site stonden de artikels onder /blog-en-tips. Die adressen
    staan nog in Google, in gedeelde berichten en in de bladwijzers van
    ouders. Zonder deze regel geven ze een foutpagina zodra het domein
    overgezet is. De losse artikels hebben nu andere adressen, dus we sturen
    iedereen naar het overzicht: daar vindt hij het artikel terug.

    Het is een blijvende omleiding (permanent), zodat Google de nieuwe
    adressen overneemt in plaats van de oude te blijven tonen.

    Merk je na de overzetting nog een oud adres dat niet uitkomt, voeg het
    hier dan bij: van, naar, en permanent op true.
  */
  async redirects() {
    return [
      { source: "/blog-en-tips", destination: "/blog", permanent: true },
      { source: "/blog-en-tips/:pad*", destination: "/blog", permanent: true },
    ];
  },
};

export default nextConfig;
