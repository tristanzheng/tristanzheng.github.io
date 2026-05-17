# Repository Guidelines

## Project Structure & Module Organization
- Content lives in top-level Markdown and content folders. Posts are in `_posts/` with date-prefixed filenames (e.g., `_posts/2026-02-20-chn-newyr-special.markdown`), drafts go in `_drafts/`, and standalone pages live at the repo root (`index.markdown`, `about.markdown`, `404.html`).
- Static assets are under `assets/`, with images in `assets/images/`.
- Site configuration is in `_config.yml`, and Ruby dependencies are in `Gemfile` and `Gemfile.lock`.
- Helper scripts are in `_scripts/` (e.g., `_scripts/optimize_images.py`).

## Build, Test, and Development Commands
- `bundle install` installs Ruby gems required for the site.
- `bundle exec jekyll serve` runs the site locally with live rebuilds.
- `bundle exec jekyll build` generates the static site output (typically to `_site/`).
- `_scripts/optimize_images.py` can be used to reduce image sizes before committing assets.

## Coding Style & Naming Conventions
- Use Markdown for posts and pages; keep front matter consistent with existing posts.
- Follow Jekyll post naming: `YYYY-MM-DD-title.markdown` in `_posts/`.
- Prefer descriptive, lower-kebab-case slugs and filenames.

## Testing Guidelines
- No automated tests are configured. Validate changes by running `bundle exec jekyll serve` and reviewing pages in a browser.

## Commit & Pull Request Guidelines
- Commit history favors short, direct messages (e.g., "Update ...", "fix typo."). Use concise present-tense summaries.
- PRs should describe the content change, include links to relevant posts or pages, and attach screenshots for layout or image-heavy updates.

## Security & Configuration Tips
- Keep `_config.yml` changes minimal and review carefully before deployment.
- Avoid committing large, unoptimized images; run the image optimization script when adding new photos.
