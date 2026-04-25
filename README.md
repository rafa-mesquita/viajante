# Roteiro de Viagem

Espaço pessoal de planejamento de viagens. Cada destino tem sua própria seção com roteiro, ideias, preços, checklist e reservas.

📖 **Site:** https://rafa-mesquita.github.io/viajante (após primeiro deploy)

## Estrutura

```
docs/
├── index.md              # homepage (lista de destinos)
├── china-2026/           # primeira viagem
│   ├── index.md
│   ├── roteiro.md
│   ├── ideias.md
│   ├── precos.md
│   ├── destino-china.md
│   ├── checklist.md
│   ├── reservas.md
│   └── pesquisa/
└── (próximos destinos...)
```

## Adicionar novo destino

1. Criar pasta `docs/<destino>/`
2. Copiar a estrutura de `china-2026/` como template
3. Adicionar a entrada na seção `nav:` do `mkdocs.yml`
4. Linkar na homepage `docs/index.md`

## Rodar localmente

```bash
pip install mkdocs-material
mkdocs serve
```

Abre em http://localhost:8000.

## Deploy

Push em `main` → GitHub Actions builda e publica em GitHub Pages.
