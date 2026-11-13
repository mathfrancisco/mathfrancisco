# Audit, design research & provenance

_Review snapshot: 2026-11-12. These findings describe repository documentation and sampled source files, not a full independent production audit._

## Existing profile audit

**Profile:** https://github.com/mathfrancisco/mathfrancisco

- Existing README was approximately 452 lines and had a remote capsule header, remote typing animation, three external statistics cards, many badges, and three inline Mermaid diagrams.
- Strong current content: grounded project descriptions, technology context, practical engineering philosophy, professional experience.
- Friction: important project decisions were below many repeated visual elements; remote render dependencies could slow the first impression; long inline diagrams pushed evidence down the page.
- This redesign moves to own-repository assets, three distinctive project illustrations, one optional collapsed architecture preview, a short engineering-decision table and a strong human introduction.
- Removed external statistics widgets (availability, stale estimates, and source limits) rather than presenting unstable numbers. Avoided the existing resume direct URL because public reachability was not confirmed.

## Benchmark set: 15 inspected READMEs

Each reference below was read through its public GitHub README. Observations are directional design notes, not endorsements or assets copied into this package.

| Source | Relevant visual/content technique | Decision for this profile |
| --- | --- | --- |
| [anuraghazra](https://github.com/anuraghazra/anuraghazra) | Strong custom visual introduction, little prose | Adapt local graphic header |
| [DenverCoder1](https://github.com/DenverCoder1/DenverCoder1) | Typing SVG, long visual content, `<details>` | Keep disclosure; avoid remote typing dependency |
| [lowlighter](https://github.com/lowlighter/lowlighter) | Rich generated activity dashboard | Avoid heavy, stale third-party stats |
| [ashutosh1919](https://github.com/ashutosh1919/ashutosh1919) | Small greeting animation and stats | Small motion is fine, not enough as evidence |
| [cassidoo](https://github.com/cassidoo/cassidoo) | Human, short, memorable personality | Adapt conversational first paragraph |
| [abhisheknaiidu](https://github.com/abhisheknaiidu/abhisheknaiidu) | Compact social context and live activity | Skip noisy counters; emphasize source links |
| [rishavanand](https://github.com/rishavanand/rishavanand) | Product-focused project index | Present problem + links |
| [jstrieb](https://github.com/jstrieb/jstrieb) | Theme-aware SVG stats and external projects | Use theme-aware local SVG instead |
| [Aakarsh-B](https://github.com/Aakarsh-B/Aakarsh-B) | Banner-first identity and links | Use tasteful banner, no generic stock art |
| [ABSphreak](https://github.com/ABSphreak/ABSphreak) | Expressive animations and icons | Restrain volume and weight |
| [codeSTACKr](https://github.com/codeSTACKr/codeSTACKr) | Human background + expandable content | Use progressive disclosure |
| [rafaballerini](https://github.com/rafaballerini/rafaballerini) | Recognizable personal identity, technology icons | Tone over badges |
| [kautukkundan templates](https://github.com/kautukkundan/Awesome-Profile-README-templates) | Large collection of profile formats | Treat templates as patterns, not copy-paste |
| [awesome profile collection](https://github.com/abhisheknaiidu/awesome-github-profile-readme) | Broad examples by category | Evaluate for recruiter clarity |
| [beydemirfurkan design gallery](https://github.com/beydemirfurkan/awesome-github-profile) | Design-led local SVGs, editorial treatment, cost disclosure | Local-only graphics + measured complexity |

Additional inspiration: [profile gallery](https://github.com/nitr0yukkuri/awesome-github-profile-gallery), [GitHub README docs](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme).

## Technical verification and limitations

- **Supported:** Markdown, images, GIF, `<details>` disclosure, and Mermaid. [GitHub docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) · [collapsed sections](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections).
- **Supported:** `<picture>` with `prefers-color-scheme` media to switch SVG for light/dark mode. [GitHub Changelog](https://github.blog/changelog/2022-08-15-specify-theme-context-for-images-in-markdown-ga/).
- **Not guaranteed:** interactive controls or SVG scripts / SVG animation everywhere. GitHub's file viewer states SVG inline scripting and animation are unsupported; some Markdown `<img>` contexts may show subtle CSS animation, but never depend on it. [GitHub Docs](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files).
- **External:** stat servers and live animations can be delayed, unavailable or rate-limited. The new README has no required external image requests.
- **SVG animation fallback:** static shapes and text are meaningful with all animation disabled. CSS uses `prefers-reduced-motion` to turn off optional effects.
- **Typography:** system font stacks; if a font is missing, fallback to Arial/monospace.
- **Image provenance:** project graphics are original *symbolic architecture illustrations*, not fabricated app screenshots or telemetry.

## Verified project boundaries

**Opportunity Radar:** [README](https://github.com/mathfrancisco/Opportunity-Radar) and [current architecture](https://github.com/mathfrancisco/Opportunity-Radar/blob/main/docs/47-arquitetura-atual.md). Python/FastAPI/APScheduler, modular monolith, React/PostgreSQL, determinism and Groq optional. Do not state embeddings or Ollama used in active pipeline.

**AI Library:** [README](https://github.com/mathfrancisco/ai-library-plataform-mvp), [architecture](https://github.com/mathfrancisco/ai-library-plataform-mvp/blob/main/docs/02-architecture.md). Java 21/Spring AI/Next.js, full-text + pgvector, Groq chat, local ONNX embeddings, tenancy. V2/V3 separate.

**Personal RAG:** [README.en](https://github.com/mathfrancisco/Personal-RAG-Assistant/blob/main/README.en.md), [EVALUATION.md](https://github.com/mathfrancisco/Personal-RAG-Assistant/blob/main/docs/EVALUATION.md). ChromaDB/Ollama/Streamlit, optional Gemini, metrics harness. No published numerical quality results verified.

**URL Shortener:** [README](https://github.com/mathfrancisco/URL-Shortener); Java/Spring Boot, React, MongoDB. **LiveChat:** [README](https://github.com/mathfrancisco/LiveChat-App); do not treat every listed non-functional target as a measured production SLO.

**Professional metrics:** The older profile includes self-reported career metrics such as daily users and test coverage. This version intentionally does not promote them as independently verified benchmarks.
