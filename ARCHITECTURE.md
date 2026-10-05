# Architecture

## Current release boundary
React + TypeScript + Vite; static deployment. Dexie/IndexedDB is the single local learner store. A service worker precaches the built app and seed assets. No account, billing, backend service, telemetry collector or cloud secret is required. This is a personal learning vertical slice, not a multi-tenant commercial service.

## Modules
- `content.ts`: typed original lexicon, lessons, prerequisites, functional roadmap and versioned standard references.
- `types.ts`: content workflow, alignment, profile, attempts, independent review memory, mistakes and sessions.
- `learning.ts`: objective-evidence policy, FSRS transition, independent skill evidence and explainable daily plan.
- `db.ts`: database schema, atomic attempt→memory→mistake writes, idempotent attempt IDs, backup validation and transactional merge.
- `audio.ts`: playback interface; separate transcription and pronunciation-assessment contracts. No provider may turn a transcript match into a tone score.
- `LessonPlayer.tsx`: reusable hear, notice, choice, recall, assembly, recording, reading and dictation primitives. Draft checkpoints persist between steps.
- `Conversation.tsx`: two bounded original roleplays, typed pattern evaluation, optional local voice rehearsal. It is explicitly not a connected AI tutor.
- `MediaLab.tsx`: original audio-scene comprehension, transcript support, replay speed, local video/SRT import and A–B loop.
- `Practice.tsx`: targeted contexts, pitch teaching diagrams, isolated review queue.

## Evidence policy
An attempt records time, response latency, context, answer, expected answer, modality, and support used. `correct:null` records practice without evaluating it. A supported success cannot become unaided evidence by hiding support. Speaking is practice-only until a valid scoring provider and rubrics exist. Objective reading/listening/typing/tone answers can update their corresponding FSRS card. Scripted conversation and scene-comprehension evidence remain separate categories; they are not scheduled as isolated reading/listening questions.

## Content publishing architecture
Draft → linguistic review → pedagogical review → audio review → assessment review → published → deprecated. Reviewer identity, version and reviewed date are required for real published material. Current data deliberately stays draft. The reference checker is evidence collection, not automated approval. A future content studio should author versioned JSON against these contracts and run schema/reference/prerequisite validation before publishing an immutable pack. Learner progress should refer to stable content IDs and retain the version used for each assessment when publishing begins.

## Extensibility
Future entities: character components and confusables; grammar concepts; full `L1Profile`; audio speaker/license records; transcript segments; import jobs; assessment rubrics; personal interests; server sync outbox. Standards are data with version, effective date, source, level and category. Traditional characters exist as a field without competing with Simplified-first instruction.

For sync, preserve immutable attempt UUIDs and use server conflict resolution for profile and content versions. Keep raw voice in a separate consent-bound store with deletion/retention policies; do not attach raw voice to analytics. Do not claim cross-device persistence before implementing and testing it.

## Operational limits
IndexedDB can be cleared by the browser. Export is essential for portability. Backups merge atomically with explicit confirmation; matching IDs use the imported record. IndexedDB is not encrypted by this application. The current release does not defend against simultaneous conflicting writes from several browser tabs; use one active study tab. Imported media remains only in the tab. Offline behavior is available after a successful production load; device speech depends on the chosen voice.

## Commercial expansion gates
Native educator/audio review; unfamiliar-speaker assessment; real learner efficacy testing; independently reviewed Vietnamese instruction; licensed native audiovisual library; security and privacy review; backed-up sync; production monitoring; provider cost limits and consent; tested backup migrations. The present software is not evidence that these gates have been met.
