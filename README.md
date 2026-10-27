# STARR Story Bank

A dashboard for building and practicing behavioral interview answers in STARR order (Situation, Task, Action, Result, Reflection). Each story is tied to the interview prompt it answers.

It runs as a claude.ai artifact: https://claude.ai/artifact/F3rmG6bm93r686FWEofkSL (private to its owner)

## What it does

- Stores stories with their prompt, competency, target company and status
- Drafts the five STARR parts from rough notes with Claude, leaving [placeholders] instead of inventing numbers
- Tracks coverage across 8 competencies and how complete each story is
- Holds practice recordings per story (video or audio, converted in the browser to fit 20 MB)
- Gives Claude feedback on each take from its transcript and three video stills
- Keeps versions of your "Tell me about yourself" answer, one text box each, with a word count and spoken-length estimate against a 30, 60, 90 or 120 second target
- Seafloor look with sand you can draw in and a short dive intro

## Repo layout

| Path | What it is |
| --- | --- |
| `index.html` | The whole page, published to the artifact as-is |
| `artifact.json` | Artifact URL and the capabilities the page declares |
| `design/seafloor-mockup/` | Design canvas source for the seafloor look |
| `tools/transcribe.py` | Local speech-to-text for practice recordings |
| `CLAUDE.md` | How Claude keeps this repo and the live page in sync |

## How the repo is tied to the page

`index.html` here is the source. Changes are made in this file, published to the artifact URL, then committed. Story data and recordings stay in the artifact's own storage on claude.ai and are not committed here.

The page needs claude.ai to save stories, store recordings and call Claude. Opened anywhere else, it shows the layout with a notice that stories can't load.
