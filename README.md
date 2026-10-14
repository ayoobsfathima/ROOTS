# Roots

A single-page prototype that lets a clinician enter a child's CARS2-ST visit
history and see a predicted developmental trajectory, using the ordinal
Disease Course Mapping method from Poulet & Durrleman (2023) fit on
synthetic CARS2-ST data (n=300).

This page contains only the **Trajectory Explorer** (the population-structure
/ subtype heatmap tab from the earlier demo was intentionally left out).

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
- `assets/about-roots.pdf` — not yet added; see above

## Deploy on Render (onrender.com)

Render serves this as a **Static Site**:

1. Push this folder to a GitHub repo (can be the same repo as your existing
   demo, in its own subfolder, or a brand-new repo — either works).
2. Go to [dashboard.render.com](https://dashboard.render.com) → **New +** →
   **Static Site**.
3. Connect your GitHub account/repo if you haven't already, and select the
   repo containing `index.html`.
4. Settings:
   - **Build Command**: leave blank (nothing to build)
   - **Publish Directory**: `.` (or the subfolder path, e.g. `roots_app`, if
     `index.html` isn't at the repo root)
5. Click **Create Static Site**. Render gives you a free `https://roots-xxxx.onrender.com`
   URL within a minute or two, and redeploys automatically on every push.

No server, no environment variables, no database — it's a static file.

## Local preview

Just open `index.html` directly in a browser, or serve it locally:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```
