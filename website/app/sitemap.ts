import type { MetadataRoute } from "next";
import { berichten } from "@/content/blog";
import { site } from "@/content/site";

/*
  De lijst met alle pagina's die Google mag kennen, te vinden op
  www.connectopia.one/sitemap.xml. Dien dat adres één keer in bij Google
  Search Console; daarna haalt Google de lijst zelf op.

  Een blogbericht komt er vanzelf bij. Maak je een nieuwe pagina, zet ze dan
  hieronder in de lijst. De bedanktpagina en de formulieren staan er bewust
  niet in.
*/
const paginas = [
  "",
  "/aanbod",
  "/over-ons",
  "/contact",
  "/oefenplatform",
  "/wegwijzer",
  "/waar-kan-je-terecht",
  "/hulp-en-advies",
  "/boekentips",
  "/blog",
  "/prikbord",
  "/kijkje",
  "/in-de-kijker",
  "/thuisonderwijs",
  "/observatielijst",
  "/professionals",
  "/voor-leerkrachten",
  "/steun-ons",
  "/meetesten",
  "/winactie",
];

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    ...paginas.map((pad) => ({
      url: `${site.webadres}${pad}`,
      priority: pad === "" ? 1 : pad === "/aanbod" ? 0.9 : 0.6,
    })),
    ...berichten.map((bericht) => ({
      url: `${site.webadres}/blog/${bericht.slug}`,
      lastModified: bericht.datum,
      priority: 0.5,
    })),
  ];
}
