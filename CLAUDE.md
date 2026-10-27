# STARR Story Bank

This repo is the source of truth for Henry's STARR Story Bank, a claude.ai artifact.

- Live page: https://claude.ai/artifact/F3rmG6bm93r686FWEofkSL
- Page source: `index.html` (one self-contained file, published as-is)
- Publish settings: `artifact.json` (URL, capabilities, contract)

## Keep the repo and the live page in sync

1. Edit `index.html` here, never a copy somewhere else.
2. Publish it to the live page with the Artifact tool: `url` = the live page URL above, `file_path` = this repo's `index.html`. Omit `capabilities` unless they change. If they change, pass the full set and update `artifact.json` in the same commit.
3. Commit and push the change with a message that says what changed on the page.

If the live page was changed from somewhere else, read it first (Artifact `read` on the URL), copy the result into `index.html`, commit that as "Sync from live page", then make your change.

## What is NOT in this repo

Stories and practice recordings live in the artifact's own database and asset store on claude.ai, not in git. Collections:

- `stories/{id}`: prompt, title, competency, company, status, notes, situation, task, action, result, reflection, createdAt, updatedAt
- `recordings/{id}`: storyId, videoId (asset id), frameIds, fileName, kind, durationSec, sizeBytes, uploadedAt, transcript, transcriptSource, feedback, feedbackAt
- `pitches/{id}`: "Tell me about yourself" answers. name, target, lengthSec (30, 60, 90 or 120), status, notes, present, past, future, createdAt, updatedAt

Read or write them with the ArtifactData tool against the live page URL. Do not commit story text, transcripts or recordings unless Henry asks.

## Transcribing practice recordings

The page's Claude can't hear audio. When Henry asks to transcribe new recordings:

1. List `recordings` where `transcript` is empty.
2. Download each video with Artifact `read` and `path` = its `videoId`.
3. Run `tools/transcribe.py` on it (setup steps are in that file).
4. Write the text back with ArtifactData `update`: `transcript` and `transcriptSource: "claude"`.

## Writing style for story content

Plain sentences, modest tone, no semicolons, no colon-led lists. Never invent metrics; use bracketed placeholders like `[X users]`.

## Design

The seafloor look came from the mockup in `design/seafloor-mockup/` (a Design canvas at https://claude.ai/artifact/EnTyGt3V1DDTFM5NoT15CM). The story table stays plain and readable on purpose. It sits above the water effects and stacks into blocks on phones.
