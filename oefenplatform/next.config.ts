import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /*
    De lettertypes voor de pdf's van de opgeloste testen worden op de server
    van schijf gelezen. Zonder deze regel laat Next ze bij het uitrollen weg,
    want er staat nergens een import naar toe.
  */
  outputFileTracingIncludes: {
    "/begeleiding/**": ["./lettertypes/**"],
  },
  /*
    Sinds 8 november 2026 staan de hoofdstukken welzijnswetenschappen in het
    gewone vak natuurwetenschappen (zie supabase/welzijn-in-natuurwetenschappen.sql
    en lib/welzijn.ts). Oude links naar het aparte vak komen daar uit.
  */
  async redirects() {
    return [
      {
        source: "/niveaus/beyond-doorstroom/natuurwetenschappen-welzijnswetenschappen/:pad*",
        destination: "/niveaus/beyond-doorstroom/natuurwetenschappen",
        permanent: false,
      },
      {
        source: "/vakken/natuurwetenschappen-welzijnswetenschappen/:pad*",
        destination: "/niveaus/beyond-doorstroom/natuurwetenschappen",
        permanent: false,
      },
    ];
  },
};

export default nextConfig;
