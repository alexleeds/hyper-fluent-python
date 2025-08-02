# Fluent Python Learning Skeleton

This repository scaffolds a literate, test‑driven journey through *Fluent Python* (2nd ed.) with strong typing,
property‑based tests, live debugging notebooks, and Rust ports for performance contrast.

| Path | Purpose |
|------|---------|
| `notebooks/` | Jupyter or VS Code notebooks that walk through each exercise, with step‑through debugging notes. |
| `src/` | Production‑quality Python implementations (type‑hinted, linted). |
| `tests/` | Canonical and AI‑generated edge‑case tests (pytest + hypothesis). |
| `rust/` | Idiomatic Rust ports of the same exercises, plus Criterion benchmarks. |
| `docs/` | Explanations, performance charts, and published docs (MkDocs Material or Quarto). |
| `.prompts/` | Saved AI prompts so the conversation is reproducible. |

```bash
pip install -r requirements-dev.txt
pre-commit install
```

Then open **notebooks/** and start with *Example 1‑1: The Pythonic Card Deck*.
