# SYSTEM_PORTAL

A retro-compatible personal web space, built to look "late 90s" while keeping the
modern conveniences of a simple static site. It renders natively in **Internet
Explorer 5.5 on Windows 98**, **RetroZilla 1.x**, and modern browsers.

Live at: https://untrustedinstaller.github.io/

## Pages

| File           | Purpose                                    |
| -------------- | ------------------------------------------ |
| `index.html`   | Home / welcome + recent updates log        |
| `about.html`   | About the site and its operator            |
| `projects.html`| Project index with status table            |
| `specs.html`   | System specs + hardware archive            |
| `links.html`   | Hand-picked links                          |
| `contact.html` | Contact, guestbook note, colophon          |
| `style.css`    | The one shared stylesheet (CSS1 only)      |
| `img/`         | 88x31 badge GIFs                           |
| `favicon.ico`  | Small favicon (16/32 px)                   |

## Compatibility approach

The floor is **IE 5.5 on Windows 98**; everything else is a bonus. The rules:

- **Tables for layout** (no flexbox, no grid, no `position: fixed`).
- **HTML 4.01 Transitional**, with inline fallback attributes
  (`bgcolor`, `align`, `width`) so pages survive a missing stylesheet.
- **CSS 1 only** in `style.css` (plus a couple of safe CSS2 touches IE 5.5 handles).
  No media queries, no CSS variables, no `border-radius`, no PNG-24 alpha.
- **Web-safe colors** and system fonts (Verdana / Arial / Courier New).
- **Zero JavaScript.** Nothing on the site needs a script.
- **GIF images only** (1-bit transparency) - palette GIFs, not PNG-24.
- Fixed **760px** layout that fits an 800x600 screen; a `<meta name="viewport"
  content="width=760">` makes it fit phone screens too.
- `iso-8859-1` charset with HTML entities for anything non-ASCII
  (no smart quotes or em-dashes - they are not in latin-1).

## Editing

- The nav bar, sidebar, and footer are duplicated in each page - that is how the
  90s did it (there is no build step). Change them in all six files or keep
  them consistent.
- Placeholder content is marked with `EDIT ME` HTML comments
  (your e-mail in `contact.html`, specs in `specs.html`, project rows in
  `projects.html`, bio in `about.html`, links in `links.html`).
- To add a page: copy an existing one, change the `<title>`, the nav
  (`nav-current` marks the active page), and the sidebar menu highlight.

## Regenerating the badges

```sh
python3 make-badges.py   # requires Pillow; rewrites img/*.gif and favicon.ico
```

## Testing on a real vintage machine

Push to GitHub and visit the site from the old box directly, or test online:

- Old browsers in your modern machine: **oldweb.today** (pick
  "Internet Explorer 5.5" under Windows 98).
- RetroZilla for Windows 98: download from the usual retro-computing archives
  (it's a Mozilla 1.x fork patched for modern page rendering).

## Deploy

GitHub Pages serves the repo root automatically from the `main` branch
(Settings -> Pages -> "Deploy from a branch", branch `main`, root folder).
Just push.