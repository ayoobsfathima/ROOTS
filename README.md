# Roots

A single-page prototype that lets a clinician enter a child's CARS2-ST visit
history and see a predicted developmental trajectory, using the ordinal
Disease Course Mapping method from Poulet & Durrleman (2023) fit on
synthetic CARS2-ST data (n=300).

This page contains **Trajectory Explorer**.

At the top there are three resource cards:
1. **Original Article** — the Poulet & Durrleman (2023) paper, linked to
   `assets/original-article.pdf`
2. **Journal Club Presentation** — linked to `assets/journal-club-presentation.pptx`
3. **About Roots** — a 1-page PDF (`assets/about-roots.pdf`) explaining what
   the model does, how it was built, pros & cons, and how to use/interpret
   the Trajectory Explorer. Generated from `make_about_pdf.py` — edit that
   script and re-run `python3 make_about_pdf.py` to update the wording.

## Files

- `index.html` — the entire app (HTML + CSS + JS in one file, no build step).
  The fitted model parameters (n=300, CARS2-ST) are embedded directly in the
  `<script>` tag as the `MODEL` constant — nothing else needs to load except
  Chart.js from a CDN.
- `assets/original-article.pdf` — the original paper
- `assets/journal-club-presentation.pptx` — the journal club slides
- `assets/about-roots.pdf` — model information for ROOTS;
