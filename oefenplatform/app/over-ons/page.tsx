import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { PRIJS_SCHOOLJAAR_EUR } from "@/lib/mollie";

export default async function OverOnsPage() {
  const session = await getSessionProfile();

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          Over ons
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">
          📚 Over ons oefenplatform
        </h1>
        <p className="mt-4 text-sm text-ink-dim">
          Beste ouder, begeleider of leerling,
        </p>
        <p className="mt-3 text-sm text-ink-dim">
          Welkom op het oefenplatform van Connectopia vzw! Wij zijn een vereniging zonder
          winstoogmerk die zich met hart en ziel inzet voor kinderen en jongeren die net dat
          beetje extra nodig hebben.
        </p>

        <div className="mt-8 space-y-8">
          <section>
            <h2 className="font-display text-lg font-semibold text-ink">
              🧠 Wat maakt ons bijzonder?
            </h2>
            <p className="mt-2 text-sm text-ink-dim">
              Connectopia vzw richt zich in de eerste plaats op hoogbegaafde (HB) en
              uitzonderlijk hoogbegaafde (UHB) kinderen, vaak met dubbele diagnoses zoals ASS
              (autismespectrumstoornis) of ADHD. Wij begrijpen dat deze kinderen op een andere
              manier leren en dat zij nood hebben aan duidelijkheid, structuur en rust.
            </p>
            <p className="mt-2 text-sm text-ink-dim">
              Daarom is ons oefenplatform bewust prikkelarm opgebouwd:
            </p>
            <ul className="mt-2 list-disc space-y-1 pl-5 text-sm text-ink-dim">
              <li>Geen overbodige animaties of afleidende kleuren.</li>
              <li>Heldere, rustige lay-out.</li>
              <li>Duidelijke instructies en overzichtelijke oefeningen.</li>
            </ul>
            <p className="mt-2 text-sm text-ink-dim">
              Maar: het platform is er voor iedereen! Of je kind nu hoogbegaafd is, extra
              ondersteuning nodig heeft, of gewoon wat bij wil oefenen voor de examens — iedereen
              is welkom.
            </p>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">
              📖 Hoe is onze leerstof samengesteld?
            </h2>
            <p className="mt-2 text-sm text-ink-dim">
              Ons oefenaanbod is niet zomaar uit de lucht gegrepen. We baseren ons op:
            </p>
            <ul className="mt-2 list-disc space-y-1 pl-5 text-sm text-ink-dim">
              <li>de officiële vakfiches van de Examencommissie voor de 1ste, 2de en 3de graad;</li>
              <li>de minimumdoelen van het lager onderwijs voor het 5de en 6de leerjaar.</li>
            </ul>
            <p className="mt-2 text-sm text-ink-dim">
              Al het materiaal wordt door ons zelf samengesteld en geredigeerd. We volgen de
              officiële leerplannen op de voet, zodat jouw kind gericht kan oefenen op wat écht
              belangrijk is.
            </p>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">
              📖 Wat bieden we momenteel aan?
            </h2>
            <p className="mt-2 text-sm text-ink-dim">
              Op dit moment kan je bij ons terecht voor oefenmateriaal voor:
            </p>
            <ul className="mt-2 list-disc space-y-1 pl-5 text-sm text-ink-dim">
              <li>Wiskunde</li>
              <li>Nederlands</li>
              <li>Engels</li>
              <li>Geschiedenis</li>
              <li>Natuurwetenschappen</li>
            </ul>
            <p className="mt-2 text-sm text-ink-dim">
              We breiden ons aanbod verder uit, dus hou onze website in de gaten!
            </p>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">
              👥 Voor wie is dit platform bedoeld?
            </h2>
            <p className="mt-2 text-sm text-ink-dim">Het platform is geschikt voor:</p>
            <ul className="mt-2 list-disc space-y-1 pl-5 text-sm text-ink-dim">
              <li>kinderen die zich voorbereiden op de examens van de Examencommissie;</li>
              <li>hoogbegaafde kinderen die extra uitdaging of oefening nodig hebben;</li>
              <li>
                leerlingen met ASS, ADHD of andere neurodivergente profielen die baat hebben bij
                een prikkelarme leeromgeving;
              </li>
              <li>kinderen in het 5de en 6de leerjaar die alvast willen proeven van de secundaire leerstof.</li>
            </ul>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">💶 Hoeveel kost het?</h2>
            <p className="mt-2 text-sm text-ink-dim">
              We vragen €{PRIJS_SCHOOLJAAR_EUR} per schooljaar voor een account. Met één account
              kunnen meerdere kinderen uit hetzelfde gezin gebruikmaken van het platform. Zo kan
              je kostenefficiënt meerdere kinderen tegelijk laten oefenen.
            </p>
            <p className="mt-3 rounded-md bg-amber/10 px-4 py-3 text-sm text-ink">
              ⚠️ <strong>Belangrijk:</strong> deel je inloggegevens niet met derden. Elk account
              is strikt persoonlijk en bedoeld voor gezinsgebruik.
            </p>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">
              🎁 Gratis toegang voor Connectopia-leden
            </h2>
            <p className="mt-2 text-sm text-ink-dim">
              Kinderen die bij ons aangesloten zijn via een plusklas, pluswerking of ander
              Connectopia-traject ontvangen gratis toegang tot alle materialen op het platform.
              Bovendien krijgen zij ook persoonlijke begeleiding op maat. Zo zorgen we ervoor dat
              elke leerling de ondersteuning krijgt die hij of zij nodig heeft.
            </p>
          </section>

          <section>
            <h2 className="font-display text-lg font-semibold text-ink">
              💬 Fouten ontdekt? Laat het ons weten!
            </h2>
            <p className="mt-2 text-sm text-ink-dim">
              Wij zijn een vzw en maken dit materiaal uit eigen beweging en met veel
              enthousiasme. Toch kan het gebeuren dat er een foutje insluipt. Mocht je iets
              tegenkomen dat niet klopt, dan horen we dat graag. Stuur dan een mailtje naar:
            </p>
            <p className="mt-2 text-sm">
              📧{" "}
              <a href="mailto:info@matmgroep.com" className="text-forest-dark underline-offset-2 hover:underline">
                info@matmgroep.com
              </a>
            </p>
            <p className="mt-2 text-sm text-ink-dim">
              Wij bekijken het zo snel mogelijk en passen het aan waar nodig.
            </p>
          </section>

          <section className="border-t border-border pt-6">
            <p className="text-sm text-ink-dim">🙏 Hartelijk dank voor je vertrouwen!</p>
            <p className="mt-2 text-sm text-ink-dim">
              Wij hopen dat jouw kind met veel plezier en succes zal oefenen op ons platform.
              Samen maken we leren leuk, rustig en doelgericht!
            </p>
            <p className="mt-4 text-sm text-ink">
              Met vriendelijke groeten,
              <br />
              Team Connectopia vzw
            </p>
          </section>
        </div>
      </main>
    </>
  );
}
