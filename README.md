<div align="center">

# Matheus Francisco

### Software Engineer · Java · Spring Boot · Full Stack · AI Engineering

**Building reliable software — from distributed backends and product interfaces  
to production AI systems.**

`Java` · `Spring Boot` · `TypeScript` · `React` · `Microservices` · `AI/LLM` · `Cloud`

[![Portfolio](https://img.shields.io/badge/Portfolio-View_my_work-C9A227?style=flat-square)](https://portifolio-ia-nine.vercel.app)
[![Resume](https://img.shields.io/badge/Resume-View_PDF-8C6F1C?style=flat-square&logo=readme&logoColor=white)](https://portifolio-ia-nine.vercel.app/cv.pdf)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Matheus_Francisco-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matheus-francisco0/)
[![Email](https://img.shields.io/badge/Email-math.francisco2%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:math.francisco2@gmail.com)
[![Location](https://img.shields.io/badge/São_Paulo-Brazil_·_Remote-2F8F5B?style=flat-square)](#)

</div>

---

## About me

I'm a **Software Engineer focused on Java, Spring Boot and full-stack development**, with hands-on experience building and integrating production systems across backend services, web applications, mobile products and cloud environments.

I work with **Java/Spring Boot, TypeScript, React, React Native, Next.js and NestJS**, designing APIs, BFFs, integrations and reusable application layers for production systems.

I also build **AI-powered products** using Python, FastAPI, LLM agents, RAG and conversational AI, with a strong focus on reliability, observability, guardrails and maintainable architecture.

My engineering interests include **distributed systems, microservices, API design, software architecture, cloud-native applications and production AI systems**.

---

## Featured projects

| Project | Stack / focus | What it demonstrates |
| --- | --- | --- |
| [URL Shortener](https://github.com/mathfrancisco/URL-Shortenere) | Java · Spring Boot · Angular · MySQL · Docker · AWS | Full-stack architecture, REST APIs, persistence and cloud deployment |
| [LiveChat](https://github.com/mathfrancisco/LiveChat-App) | Java · Spring Boot · WebSocket · STOMP · Angular | Real-time communication, event-driven features and client/server integration |
| [Multi-channel AI Agent](https://portifolio-ia-nine.vercel.app/work) | Python · LLM · RAG · Voice AI · Messaging | Production conversational AI, tools, safety and observability |
| [Reliable Messaging](https://portifolio-ia-nine.vercel.app/work) | Messaging · Idempotency · Throttling | Provider integration, reliability and failure-aware delivery |
| [Model Routing](https://portifolio-ia-nine.vercel.app/work) | LLM routing · Context caching · Evaluation | Cost-aware AI architecture and model orchestration |
| [AI System Designs](https://portifolio-ia-nine.vercel.app/system-design) | Architecture · Retrieval · Agents · Evaluation | System-design diagrams and engineering trade-offs |

---

## What I work with

```text
BACKEND         Java · Spring Boot · TypeScript · NestJS · Python · FastAPI
FRONTEND        React · React Native · Next.js · Angular · Vue
ARCHITECTURE    Microservices · BFF · REST · GraphQL · Distributed Systems
AI              LLM Agents · RAG · Conversational AI · Voice AI · Guardrails
DATA            PostgreSQL · Redis · MySQL
CLOUD           AWS · GCP · Docker · Kubernetes · CI/CD · Observability
ENGINEERING     DDD · Clean Architecture · SOLID · TDD · Code Review
```

---

## Production engineering

### CI&T — Software Engineer

I work on enterprise payment products across web, mobile and backend integrations.

My work includes:

- Building web and mobile features with **React, React Native, Next.js and TypeScript**.
- Developing **REST and GraphQL BFF services with NestJS**.
- Integrating applications with **Java/Spring Boot microservices**.
- Reviewing API contracts, OpenAPI specifications, pagination and security behavior before implementation.
- Implementing **role-based access control with Azure AD** across frontend and BFF layers.
- Extracting reusable payment-domain logic into shared libraries for web and mobile applications.
- Participating in technical refinements, architecture discussions, code reviews, unit testing and CI/CD.
- Working with **GitLab CI, Docker, Kubernetes and Datadog** in production delivery workflows.

### Production AI systems

I have also worked on a **multi-tenant conversational AI platform** for automated credit recovery across **WhatsApp, SMS and Voice AI**.

The platform work spans product interfaces, APIs, AI-agent behavior, retrieval, messaging integrations, multi-tenant data and cloud operations.

```mermaid
flowchart LR
    Customer((Customer))

    subgraph Channels
        WA[WhatsApp]
        SMS[SMS]
        Voice[Voice AI]
    end

    subgraph Platform["Conversational AI Platform"]
        UI[Product + Operator UI]
        API[Platform APIs]
        Gateway[Channel Gateway]
        Context[Context + Tenant Data]
        Agent[LLM Agent]
        Guardrails[Policies + Guardrails]
        Tools[Business Tools]
    end

    subgraph Operations
        Data[(PostgreSQL / RAG)]
        Observe[Logs · Traces · Evaluation]
        Human[Human Recovery Path]
    end

    Customer --> WA
    Customer --> SMS
    Customer --> Voice

    UI --> API
    API --> Gateway

    WA --> Gateway
    SMS --> Gateway
    Voice --> Gateway

    Gateway --> Context
    Context --> Agent

    Guardrails -. constrains .-> Agent

    Agent <--> Data
    Agent --> Tools
    Tools --> Customer

    Gateway --> Observe
    Agent --> Observe
    Tools --> Observe

    Agent -. escalate .-> Human
```

> I treat the model as one component of the system. Production trust comes from explicit boundaries, observable decisions and recoverable paths around it.

---

## Selected engineering outcomes

<table>
  <tr>
    <td width="50%" valign="top">
      <strong>Full-stack product delivery</strong>
      <br /><br />
      Worked across product interfaces, platform APIs, backend integrations and shared application layers for production systems.
    </td>
    <td width="50%" valign="top">
      <strong>Production AI architecture</strong>
      <br /><br />
      Built conversational AI capabilities involving LLM agents, RAG, voice integrations, guardrails, observability and human recovery paths.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <strong>Product scale</strong>
      <br /><br />
      Contributed to React and React Native products supporting more than 100,000 daily active users across multiple regions.
    </td>
    <td width="50%" valign="top">
      <strong>Reliability and performance</strong>
      <br /><br />
      Worked on initiatives involving higher test coverage, fewer production incidents and lower database-query latency.
    </td>
  </tr>
</table>

<div align="center">

[![Explore production case studies](https://img.shields.io/badge/Explore_Production_Case_Studies-111416?style=for-the-badge&logo=readme&logoColor=C9A227)](https://portifolio-ia-nine.vercel.app/work)
[![View system diagrams](https://img.shields.io/badge/View_System_Diagrams-111416?style=for-the-badge&logo=diagramsdotnet&logoColor=4FB17E)](https://portifolio-ia-nine.vercel.app/system-design)

</div>

---

## Core stack

<details open>
<summary><strong>Backend & Software Engineering</strong></summary>

<br />

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![NestJS](https://img.shields.io/badge/NestJS-E0234E?style=for-the-badge&logo=nestjs&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

<br />

`Microservices` · `BFF` · `REST APIs` · `GraphQL` · `Distributed Systems` ·
`DDD` · `Clean Architecture` · `SOLID` · `TDD`

</details>

<details>
<summary><strong>Frontend & Product Interfaces</strong></summary>

<br />

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![React Native](https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white)
![Angular](https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)

</details>

<details>
<summary><strong>AI Engineering</strong></summary>

<br />

![LLM Agents](https://img.shields.io/badge/LLM_Agents-1A1A1A?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-8C6F1C?style=for-the-badge)
![Voice AI](https://img.shields.io/badge/Voice_AI-6B4EFF?style=for-the-badge)

<br />

`Conversational AI` · `Prompt Engineering` · `RAG` · `Tool Use` ·
`Guardrails` · `Evaluation` · `Observability`

</details>

<details>
<summary><strong>Data, Cloud & Delivery</strong></summary>

<br />

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)

<br />

`CI/CD` · `GitLab CI` · `Observability` · `Datadog` · `Cloud-Native Delivery`

</details>

---

## Experience

<table>
  <tr>
    <td width="50%" valign="top">
      <strong>CI&T — Software Engineer</strong>
      <br /><br />
      Enterprise payment products, full-stack delivery, BFFs, API integrations and Java/Spring Boot microservices.
    </td>
    <td width="50%" valign="top">
      <strong>Conversational AI / SaaS Projects</strong>
      <br /><br />
      Full-stack platforms involving Python, LLM agents, RAG, messaging, voice integrations, multi-tenant data and cloud infrastructure.
    </td>
  </tr>
</table>

For my full professional experience:  
[LinkedIn profile](https://www.linkedin.com/in/matheus-francisco0/)

---

## Education

<table>
  <tr>
    <td width="50%" valign="top">
      <strong>B.Sc. in Artificial Intelligence — UNIVESP</strong>
      <br />
      2026–2030
    </td>
    <td width="50%" valign="top">
      <strong>Systems Analysis and Development — UNIFEOB</strong>
      <br />
      Technology degree
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <strong>Technical Degree in Electronics — IFSP</strong>
    </td>
    <td width="50%" valign="top">
      <strong>Continuous learning</strong>
      <br />
      Backend, cloud, software architecture and AI engineering.
    </td>
  </tr>
</table>

---

## GitHub statistics

<div align="center">

<img
  src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=mathfrancisco&theme=github_dark"
  alt="Matheus Francisco GitHub profile details"
/>

<br />

<img
  width="49%"
  src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=mathfrancisco&theme=github_dark"
  alt="Languages by repository"
/>

<img
  width="49%"
  src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=mathfrancisco&theme=github_dark"
  alt="Languages by commits"
/>

<br />

<img
  width="49%"
  src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=mathfrancisco&theme=github_dark"
  alt="GitHub statistics"
/>

<img
  width="49%"
  src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=mathfrancisco&theme=github_dark&utcOffset=-3"
  alt="Most productive coding time"
/>

<br />

<img
  src="https://streak-stats.demolab.com?user=mathfrancisco&theme=github-dark-blue&hide_border=true"
  alt="GitHub contribution streak"
/>

</div>

---

## Let's connect

Based in **São Paulo, Brazil (UTC-3)** and open to remote software engineering opportunities involving **Java/Spring Boot, backend architecture, full-stack products, distributed systems, cloud-native applications and AI-enabled software**.

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-Explore_my_work-C9A227?style=for-the-badge)](https://portifolio-ia-nine.vercel.app)
[![Blog](https://img.shields.io/badge/Blog-Read_articles-111416?style=for-the-badge&logo=readme&logoColor=white)](https://portifolio-ia-nine.vercel.app/blog)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Let's_connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matheus-francisco0/)
[![Email](https://img.shields.io/badge/Email-Start_a_conversation-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:math.francisco2@gmail.com)

</div>

---

<div align="center">

**Building reliable software — from distributed backends to production AI systems.**

</div>
