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
};

export default nextConfig;
