import type { MetadataRoute } from "next";
import { site } from "@/content/site";

/*
  Zegt zoekmachines dat ze alles mogen lezen, behalve de bedanktpagina, en
  waar de lijst met pagina's staat (zie app/sitemap.ts).
*/
export default function robots(): MetadataRoute.Robots {
  return {
    rules: { userAgent: "*", allow: "/", disallow: "/bedankt" },
    sitemap: `${site.webadres}/sitemap.xml`,
  };
}
