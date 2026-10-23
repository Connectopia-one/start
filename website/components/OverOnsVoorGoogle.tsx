import { site } from "@/content/site";
import { vindbaarheid } from "@/content/vindbaarheid";

/*
  Een stukje dat enkel zoekmachines lezen: wie we zijn, hoe je ons bereikt
  en waar we werken. Zo weet Google dat "Connectopia vzw" deze vzw uit
  Hasselt en Genk is, en niet een andere organisatie met dezelfde naam.
  De gegevens zelf staan in content/site.ts en content/vindbaarheid.ts.
*/
export function OverOnsVoorGoogle() {
  const { adres } = vindbaarheid;
  const heeftAdres = adres.straat && adres.postcode && adres.gemeente;

  const gegevens = {
    "@context": "https://schema.org",
    "@type": ["EducationalOrganization", "NGO"],
    "@id": `${site.webadres}/#vzw`,
    name: vindbaarheid.naam,
    alternateName: vindbaarheid.alternatieveNamen,
    url: site.webadres,
    logo: `${site.webadres}/logo.png`,
    description: vindbaarheid.omschrijving,
    email: site.email,
    telephone: "+32 468 35 74 96",
    sameAs: [site.facebook, site.instagram, site.linkedin].filter(Boolean),
    areaServed: vindbaarheid.regio.map((plaats) => ({
      "@type": "Place",
      name: plaats,
    })),
    ...(heeftAdres && {
      address: {
        "@type": "PostalAddress",
        streetAddress: adres.straat,
        postalCode: adres.postcode,
        addressLocality: adres.gemeente,
        addressCountry: "BE",
      },
    }),
    location: vindbaarheid.locaties.map((plek) => ({
      "@type": "Place",
      name: `${plek.naam}, ${plek.gemeente}`,
      address: {
        "@type": "PostalAddress",
        streetAddress: plek.straat,
        postalCode: plek.postcode,
        addressLocality: plek.gemeente,
        addressCountry: "BE",
      },
    })),
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{
        __html: JSON.stringify(gegevens).replace(/</g, "\\u003c"),
      }}
    />
  );
}
