import type { NextConfig } from "next";

/*
  Met STATIC_EXPORT=1 bouwt Next de site als losse html-bestanden in de map
  out/. Dat gebruiken we om een klikbaar voorbeeld te kunnen delen. Gewoon
  "npm run build" blijft de normale build voor online zetten.
*/
const statischeExport = process.env.STATIC_EXPORT === "1";

const nextConfig: NextConfig = statischeExport
  ? { output: "export", trailingSlash: true, images: { unoptimized: true } }
  : {};

export default nextConfig;
