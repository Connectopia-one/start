import type { Metadata } from "next";
import { Fraunces, IBM_Plex_Sans } from "next/font/google";
import "./globals.css";

const display = Fraunces({
  variable: "--font-display",
  subsets: ["latin"],
  weight: ["500", "600"],
});

const body = IBM_Plex_Sans({
  variable: "--font-body",
  subsets: ["latin"],
  weight: ["400", "500", "600"],
});

export const metadata: Metadata = {
  title: "Oefenplatform Connectopia",
  description: "Oefen voor de examencommissie — vakken en hoofdstukken van Connectopia.",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="nl" className={`${display.variable} ${body.variable} h-full`}>
      <body className="min-h-full flex flex-col bg-paper text-ink antialiased">{children}</body>
    </html>
  );
}
