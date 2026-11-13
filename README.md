
<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:0F766E,100:C9A227&height=175&section=header&text=Build.%20Measure.%20Improve.&fontSize=38&fontColor=FFFFFF&fontAlignY=39&animation=fadeIn" alt="Build. Measure. Improve." />

# Hey, I'm Matheus Francisco 👋

### Software Engineer · Applied AI · Backend & Full Stack

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&duration=3000&pause=900&color=0F9D8A&center=true&vCenter=true&width=760&height=55&lines=Building+reliable+software;Java+%2B+Spring+Boot+%2B+TypeScript;LLM+Applications+%2B+RAG+%2B+AI+Agents;From+system+design+to+production;Good+engineering+is+more+than+code." alt="Animated introduction" width="95%" />

<br/>

[![Portfolio](https://img.shields.io/badge/Portfolio-Explore_my_work-C9A227?style=for-the-badge&logo=vercel&logoColor=white)](https://portifolio-ia-nine.vercel.app/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matheus-francisco0/)
[![Resume](https://img.shields.io/badge/Resume-View_CV-334155?style=for-the-badge&logo=readme&logoColor=white)](https://portifolio-ia-nine.vercel.app/cv.pdf)
[![Email](https://img.shields.io/badge/Email-Let's_talk-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:math.francisco2@gmail.com)

<br/>

`🇧🇷 Brazil (UTC-3)` · `🌍 Remote opportunities` · `🇺🇸 Fluent English`

</div>

---

## 👨‍💻 A little about me

I'm a **Software Engineer working at the intersection of backend engineering, full-stack products and Applied AI**.

My professional experience spans enterprise payment systems, distributed backend services, web and mobile applications, and production conversational AI platforms.

I work primarily with **Java, Spring Boot, Python, TypeScript, React and NestJS**, building software that needs to be reliable beyond the happy path.

When working with AI, I focus on the engineering around the model:

- **Data & retrieval:** ingestion, indexing, RAG and source-grounded responses.
- **Agents & integrations:** tool calling, APIs, orchestration and business rules.
- **Reliability:** fallbacks, guardrails, error handling and observability.
- **Quality:** automated tests, evaluation, latency and measurable behavior.
- **Architecture:** clear boundaries, pragmatic design and maintainability.

> **My engineering philosophy:** An LLM is one component of a system. Reliability comes from everything we build around it.

---

## 🚀 Featured engineering projects

A selection of projects demonstrating how I design systems, make technical decisions and turn ideas into working software.

### 01 · Opportunity Radar — AI-assisted job intelligence

**Local-first platform for collecting, normalizing and evaluating professional opportunities.**

[![Repository](https://img.shields.io/badge/Source_Code-Opportunity_Radar-181717?style=flat-square&logo=github)](https://github.com/mathfrancisco/Opportunity-Radar)
[![Architecture](https://img.shields.io/badge/Architecture-Explore-0F766E?style=flat-square)](https://github.com/mathfrancisco/Opportunity-Radar/blob/main/docs/47-arquitetura-atual.md)

`Python` `FastAPI` `PostgreSQL` `React` `Docker` `Groq` `GitHub Actions`

Opportunity Radar transforms public, permitted job sources into a structured decision-support system.

**Engineering highlights**

- Scheduled collection from supported public ATS and feeds.
- Raw source evidence and canonical opportunity normalization.
- Deduplication and deterministic eligibility scoring.
- Optional LLM analysis that explains results without overriding business rules.
- React dashboard with opportunity tracking and human-controlled decisions.
- Containerized development environment and automated quality checks.

**What makes it different:** The system does not blindly trust AI-generated judgments. Eligibility is deterministic, source evidence is preserved and the final decision remains with the user.

<details open>
<summary><strong>🧩 Architecture — From raw sources to decisions</strong></summary>

<br/>

```mermaid
flowchart TB
    A["Public ATS & Job Feeds"] --> B["Scheduled Collectors"]
    B --> C["Raw Source Evidence"]
    C --> D["Normalization & Deduplication"]
    D --> E[("PostgreSQL")]
    E --> F["Deterministic Matching"]
    F --> G["Opportunity Inbox"]

    F -. "Optional context" .-> H["Groq LLM Analysis"]
    H -. "Advisory only" .-> G

    G --> I(["Human Decision"])

    classDef source fill:#164E63,color:#ffffff,stroke:#0891B2
    classDef storage fill:#334155,color:#ffffff,stroke:#64748B
    classDef logic fill:#0F766E,color:#ffffff,stroke:#14B8A6
    classDef ai fill:#713F12,color:#ffffff,stroke:#CA8A04
    classDef human fill:#166534,color:#ffffff,stroke:#22C55E

    class A,B,C source
    class E storage
    class D,F logic
    class H ai
    class I human
```

**Key architectural decision**

AI generates commentary and explanations, not eligibility verdicts. This keeps matching predictable, auditable and independent of model availability.

[Read the system architecture →](https://github.com/mathfrancisco/Opportunity-Radar/blob/main/docs/47-arquitetura-atual.md)

</details>

### 02 · AI Library Platform — Java + Spring AI

**Intelligent digital library with hybrid retrieval, document understanding and AI assistance.**

[![Repository](https://img.shields.io/badge/Source_Code-AI_Library-181717?style=flat-square&logo=github)](https://github.com/mathfrancisco/ai-library-plataform-mvp)

`Java 21` `Spring Boot` `Spring AI` `PostgreSQL` `pgvector` `Next.js` `React`

A modular full-stack product integrating traditional application development with modern AI capabilities.

**Engineering highlights**

- Catalog federation and structured book metadata.
- Hybrid retrieval combining full-text and vector similarity.
- Document ingestion and source-grounded RAG.
- Tenant-scoped retrieval to protect private data.
- AI-assisted discovery, summaries and recommendations.
- Tool-enabled assistance with access boundaries.
- Modular application architecture and documented engineering decisions.

**What makes it different:** Rather than creating a basic chatbot wrapper, this project explores how AI fits into a complete Java software product.

### 03 · Personal RAG Assistant — Local-first AI

**Document question-answering with citations, local models and measurable retrieval quality.**

[![Repository](https://img.shields.io/badge/Source_Code-Personal_RAG-181717?style=flat-square&logo=github)](https://github.com/mathfrancisco/Personal-RAG-Assistant)

`Python` `LangChain` `ChromaDB` `Ollama` `Streamlit` `pytest`

**Engineering highlights**

- Multi-format document ingestion.
- Local-first execution without mandatory cloud API calls.
- Source citations for generated answers.
- Incremental indexing based on file changes.
- Provider abstraction for model flexibility.
- Retrieval evaluation with Recall@k.
- Latency measurement and optional tracing.

**What makes it different:** Retrieval quality and transparency are treated as engineering requirements, not afterthoughts.

<details>
<summary><strong>🔬 How a grounded RAG system works</strong></summary>

<br/>

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant App as Application
    participant Store as Vector Store
    participant LLM as Language Model
    participant Eval as Evaluation

    User->>App: Ask question
    App->>Store: Retrieve relevant chunks
    Store-->>App: Context + source references

    alt Relevant context found
        App->>LLM: Question + grounded context
        LLM-->>App: Answer
        App-->>User: Answer with citations
    else Insufficient evidence
        App-->>User: Explain missing context
    end

    App->>Eval: Record retrieval and latency metrics
```

**Engineering principle:** A confident answer is not necessarily a correct answer. Retrieval quality, source traceability and evaluation matter.

</details>

### 04 · URL Shortener — Full-stack Java

**URL management platform with authentication, analytics and a modern web interface.**

[![Repository](https://img.shields.io/badge/Source_Code-URL_Shortener-181717?style=flat-square&logo=github)](https://github.com/mathfrancisco/URL-Shortener)

`Java` `Spring Boot` `Spring Security` `MongoDB` `React` `TypeScript`

A complete full-stack application exploring REST APIs, user management, authentication, persistence and analytics.

### 05 · LiveChat — Real-time communication

**Real-time messaging using WebSocket-based client/server communication.**

[![Repository](https://img.shields.io/badge/Source_Code-LiveChat-181717?style=flat-square&logo=github)](https://github.com/mathfrancisco/LiveChat-App)

`Java` `Spring Boot` `WebSocket` `STOMP` `Angular`

An exploration of real-time messaging, event-driven features and frontend/backend integration.

<div align="center">

<br/>

[![Explore All Projects](https://img.shields.io/badge/Explore_All_Repositories-111827?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mathfrancisco?tab=repositories)

</div>

---

## 🧠 How I approach AI Engineering

I believe production AI is a **software engineering discipline**, not just a model integration problem.

| Engineering principle | My approach |
| --- | --- |
| 🎯 **Grounded responses** | Retrieval pipelines, source references and clear evidence boundaries. |
| 🛡️ **Human control** | Deterministic rules and advisory-only AI for critical decisions. |
| 📊 **Measurable quality** | Evaluation datasets, retrieval metrics and latency analysis. |
| 🔄 **Resilience** | Provider abstraction, graceful degradation and controlled fallbacks. |
| 🔐 **Security** | Data isolation, authorization and controlled tool execution. |
| 🏗️ **Pragmatic design** | Modular systems with clear responsibilities and limited complexity. |

### The engineering loop

```mermaid
flowchart LR
    A(["Problem"]) --> B["Design"]
    B --> C["Build"]
    C --> D["Test"]
    D --> E["Measure"]
    E --> F["Improve"]
    F --> B

    classDef start fill:#0F766E,color:#ffffff,stroke:#14B8A6
    classDef steps fill:#1E293B,color:#ffffff,stroke:#64748B
    class A start
    class B,C,D,E,F steps
```

*Good systems evolve through feedback, not assumptions.*

---

## 💼 Engineering in production

### CI&T — Software Engineer

Working on enterprise payment products across backend services, integrations and web/mobile applications.

**Technical contributions**

- Java/Spring Boot microservices and enterprise API integrations.
- NestJS BFF services with REST and GraphQL.
- React, React Native, Next.js and TypeScript applications.
- API contract design, OpenAPI and security validation.
- Azure AD and role-based access control.
- Automated testing, code reviews, CI/CD and observability.
- Production monitoring using tools such as Datadog.

### Conversational AI & Automation

Professional experience developing AI-enabled communication and credit-recovery systems.

Working across:

- Python/FastAPI services and business integrations.
- LLM-based conversational workflows.
- Retrieval-augmented generation and guardrails.
- WhatsApp and SMS communication.
- PostgreSQL and tenant-aware data handling.
- Monitoring, performance tuning and failure recovery.

### Selected engineering outcomes

<table>
<tr>
<td width="33%" align="center">

### 100K+

**Daily users**

Contributed to production web and mobile systems serving a large user base.

</td>
<td width="33%" align="center">

### 90%

**Backend test coverage**

Worked on automated testing and quality improvements.

</td>
<td width="33%" align="center">

### −25%

**Production incidents**

Contributed to reliability improvements in professional engineering work.

</td>
</tr>
</table>

<sub>Selected outcomes from professional projects; figures reflect specific systems and team efforts, not benchmarks of the public repositories.</sub>

---

## 🛠️ My engineering toolkit

<div align="center">

### Backend & APIs

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![NestJS](https://img.shields.io/badge/NestJS-E0234E?style=for-the-badge&logo=nestjs&logoColor=white)

### Frontend & Mobile

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![React Native](https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Angular](https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white)

### AI & Data

![LLM Agents](https://img.shields.io/badge/LLM_Agents-334155?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-0F766E?style=for-the-badge)
![Spring AI](https://img.shields.io/badge/Spring_AI-6DB33F?style=for-the-badge&logo=spring&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

### Cloud, DevOps & Quality

![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

</div>

<details>
<summary><strong>Additional engineering concepts & practices</strong></summary>

<br/>

`Distributed Systems` · `Microservices` · `Modular Monoliths` · `REST APIs` · `GraphQL` · `BFF` · `DDD` · `Clean Architecture` · `SOLID` · `Automated Testing` · `CI/CD` · `Observability` · `RAG Evaluation` · `Tool Calling` · `API Security` · `Performance Optimization`

</details>

---

## 🎓 Education & certifications

**Education**

- **B.Sc. in Artificial Intelligence** — UNIVESP, in progress.
- **Systems Analysis and Development** — UNIFEOB, expected December 2026.
- **Technical education in Electronics.**

**Professional certifications**

- Claude Certified Developer — Foundations
- Oracle Agentic AI Foundations Associate
- Oracle AI Database Certified Foundations Associate

---

## 📈 GitHub activity

<div align="center">

<img width="95%" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=mathfrancisco&theme=github_dark" alt="GitHub contribution overview" />

<img width="48%" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=mathfrancisco&theme=github_dark" alt="GitHub activity statistics" />
<img width="48%" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=mathfrancisco&theme=github_dark" alt="Repository language statistics" />

</div>

---

## ☕ Beyond the code

<details>
<summary><strong>Open my developer terminal</strong></summary>

<br/>

```text
$ whoami
> Software Engineer building reliable products and applied AI.

$ cat engineering-principles.txt
> Understand the problem before choosing the technology.
> Keep business rules explicit.
> Measure before optimizing.
> Design for failure, not just success.
> Make the system observable.
> Prefer maintainability over unnecessary complexity.

$ echo $CURRENT_INTERESTS
> AI Agents | RAG | System Design | Backend Architecture

$ git status
> Always learning. Always improving.

$ ./ship.sh
> Build thoughtfully. Test thoroughly. Ship responsibly. 🚀
```

</details>

---

## 🤝 Let's build something meaningful

I'm open to remote opportunities involving:

**AI Engineering · Backend Development · Full-Stack Engineering · Applied LLM Systems**

I enjoy working on products that combine solid software fundamentals, thoughtful architecture and practical AI capabilities.

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-Explore_Projects-C9A227?style=for-the-badge&logo=vercel&logoColor=white)](https://portifolio-ia-nine.vercel.app/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Let's_Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matheus-francisco0/)
[![Email](https://img.shields.io/badge/Email-Get_in_Touch-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:math.francisco2@gmail.com)

<br/>

**Reliable systems. Useful AI. Thoughtful engineering.**

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:0F766E,100:C9A227&height=110&section=footer" alt="Footer" />

</div>
