-- Geschiedenis Beyond: vragen over leerstof die bedrijfs- en
-- welzijnswetenschappen (vakfiche 3DDG) niet nodig hebben.
-- Kim, 9 november 2026: een label bij die vragen en een apart examen.
-- Veilig om meer dan eens te draaien. Verwijdert niets.
alter table public.vragen add column if not exists niet_voor_dg boolean not null default false;
