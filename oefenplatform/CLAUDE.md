@AGENTS.md

<!-- BEGIN:nextjs-agent-rules -->

# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->

# Vaste regel: elke aanpassing op "Wat is er nieuw?"

Kim, 8 november 2026: alles wat we aan het oefenplatform aanpassen, moet
automatisch op de pagina /nieuw komen. Daarom: zet bij elke wijziging die
ouders of kinderen merken (nieuw vak, nieuwe vragen, iets rechtgezet, een
knop erbij) in dezelfde commit een vakje vooraan in de lijst `updates` in
`inhoud/nieuw.ts`. Datum zoals "8 november 2026", korte titel, uitleg in
gewone woorden voor ouders, `opVraag: true` als het kwam door een melding,
de enquête of een review. Geen namen van ouders of kinderen (de pagina is
publiek), geen woorden als "fiche" of "commit". Puur technisch werk dat
niemand ziet, hoeft er niet op. Toon het vakje aan Kim samen met de rest,
voor het live gaat.
