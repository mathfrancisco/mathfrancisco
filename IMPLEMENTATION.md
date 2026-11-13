# Implementation guide (PT-BR)

## Entrega

- `README.md` — perfil final em inglês, com conteúdo conciso e imagens acessíveis.
- `assets/hero-dark.svg` / `hero-light.svg` — identidade visual original, adaptada ao tema GitHub.
- `assets/projects/*.svg` — três capas **ilustrativas**, que não simulam screenshots reais.
- `assets/architecture/opportunity-radar.svg` — fluxo estático legível, inclusive sem animação.
- `docs/ARCHITECTURES.md` — diagramas Mermaid nativos dos três projetos, com referências.
- `docs/RESEARCH_AND_AUDIT.md` — auditoria, 15 READMEs analisados, suporte e limites.
- `.github/workflows/profile-check.yml` + `scripts/validate_profile.py` — testes locais e na PR, sem precisar de APIs externas.

## Publicação

1. Abra https://github.com/mathfrancisco/mathfrancisco e crie a branch `feat/profile-engineering-console` a partir de `main` (caso ainda não exista).
2. Copie o conteúdo desta pasta **preservando os diretórios** para a raiz do repositório da branch.
3. Rode `python scripts/validate_profile.py` localmente. Depois, abra uma Pull Request da branch para `main`.
4. No GitHub, abra `README.md` em **Preview** e revise desktop/mobile, light/dark. Teste a expansão dos detalhes e todos os links de projetos.
5. Confira os previews dos SVGs no próprio README. A animação é opcional e a arte estática sempre permanece legível.
6. Só depois da revisão, faça merge. `main` fica inalterada até a aprovação.

## Atualizações

- Revalide features com código antes de afirmar novos resultados em READMEs.
- Para screenshots reais, capture a tela do projeto, retire quaisquer dados privados e acrescente novos assets com indicação de ambiente e data. Não substitua imagens ilustrativas por mockups que pareçam dados reais.
- Se incluir CI status / GitHub statistics futuramente, considere gerá-los por Actions no próprio repositório, sem dezenas de requisições externas na home.
- Confirme se o link do currículo em `.../cv.pdf` está público antes de exibi-lo; por isso esta versão não usa um link direto de currículo.
- Caso o SVG apareça estático, isso é intencional: o GitHub não garante animação em todos os contextos.
- Uma imagem quebrada localmente geralmente indica case mismatch de caminho/arquivo ou URL relativa incorreta.

## Decisões estéticas

Design: **Engineering Console + Applied AI Lab**. Paleta `#0B1017`, `#111A24`, `#36D7BC`, `#E3BD68`, `#74A9FF`. Sem robôs stock, sem card-wall de estatísticas, sem GIF pesado nem código JavaScript no README. Animações CSS imperceptíveis permanecem apenas no header, com `prefers-reduced-motion` e desenho estático como fallback.

## Restrições verificáveis

O validador checa XML dos SVGs, tamanho dos assets, referências relativas e ausência de dependências visuais externas no README, mas **não valida HTTP remoto nem reproduz o renderizador do GitHub**. O pipeline Mermaid depende da visualização do próprio GitHub; revisar visualmente após abrir a PR.
