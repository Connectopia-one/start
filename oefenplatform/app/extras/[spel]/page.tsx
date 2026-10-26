import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { extrasTekst, spellen, vindSpel } from "@/inhoud/extras";

export function generateStaticParams() {
  return spellen.map((spel) => ({ spel: spel.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ spel: string }>;
}) {
  const spel = vindSpel((await params).spel);
  return { title: `${spel?.titel ?? extrasTekst.label} — Oefenplatform Connectopia` };
}

/*
  Het spel zelf is één los html-bestand in public/spellen/. Het staat hier in
  een kader onder de gewone menubalk, zodat je altijd terug kan naar de rest
  van het platform. Voor het digibord staat er een knop bij die het spel op
  een eigen, volle pagina opent.
*/
export default async function SpelPage({
  params,
}: {
  params: Promise<{ spel: string }>;
}) {
  const spel = vindSpel((await params).spel);
  if (!spel) notFound();

  const session = await getSessionProfile();
  const bron = `/spellen/${spel.slug}.html`;

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="flex w-full flex-1 flex-col">
        <div className="mx-auto flex w-full max-w-6xl flex-wrap items-center justify-between gap-3 px-6 py-3 text-sm">
          <Link href="/extras" className="text-forest-dark hover:underline">
            &larr; {extrasTekst.terug}
          </Link>
          <a
            href={bron}
            target="_blank"
            rel="noopener"
            className="rounded-md border border-border bg-surface px-3 py-1.5 font-semibold text-forest-dark transition hover:border-forest"
          >
            {extrasTekst.volledigScherm}
          </a>
        </div>
        <iframe
          src={bron}
          title={spel.titel}
          className="h-[calc(100vh-8rem)] min-h-[560px] w-full border-t border-border"
        />
      </main>
    </>
  );
}
