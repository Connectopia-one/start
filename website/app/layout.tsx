import type { Metadata } from "next";
import { Nunito, Caveat } from "next/font/google";
import { SiteHeader } from "@/components/SiteHeader";
import { SiteFooter } from "@/components/SiteFooter";
import { Bezoekersteller } from "@/components/Bezoekersteller";
import { site } from "@/content/site";
import "./globals.css";

const body = Nunito({
  variable: "--font-body",
  subsets: ["latin"],
  weight: ["400", "600", "700", "800", "900"],
});

const hand = Caveat({
  variable: "--font-hand",
  subsets: ["latin"],
  weight: ["600", "700"],
});

/*
  De titel, de omschrijving en de afbeelding die verschijnen als iemand een
  link van de site doorstuurt of opslaat. Het tabbladicoon en die afbeelding
  zijn de bestanden  app/icon.png  en  app/opengraph-image.png  —
  vervang gewoon het bestand als het logo ooit verandert.
*/
export const metadata: Metadata = {
  metadataBase: new URL(site.webadres),
  title: {
    default: `${site.naam} — ${site.baseline}`,
    template: `%s — ${site.naam}`,
  },
  description: site.omschrijving,
  openGraph: {
    type: "website",
    locale: "nl_BE",
    url: site.webadres,
    siteName: `${site.naam} ${site.vzw}`,
    title: `${site.naam} — ${site.baseline}`,
    description: site.omschrijving,
  },
  twitter: {
    card: "summary_large_image",
    title: `${site.naam} — ${site.baseline}`,
    description: site.omschrijving,
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="nl" className={`${body.variable} ${hand.variable} h-full`}>
      <body className="flex min-h-full flex-col bg-cream text-ink antialiased">
        <SiteHeader />
        <main className="flex-1">{children}</main>
        <SiteFooter />
        <Bezoekersteller />
      </body>
    </html>
  );
}
