# Ishant Kumar Gupta — Portfolio (Flask)

A responsive, IDE-themed developer portfolio built with **Python (Flask)**, Jinja templates,
vanilla CSS and JS. Includes:

- **Home** — terminal-style hero, about, skills, experience (git-log style), projects, education
- **Certifications** — every NPTEL + Google Cloud certificate as a clickable list, opens full-size in a modal
- **Internships** — Celebal, Kistechno, and Aerophantom internships in a distinct feature-row layout with certificate previews
- **Competitions** — Smart India Hackathon 2025 participation certificate, trophy-case style

## 1. Requirements
- Python 3.9+
- VS Code (with the Python extension, recommended)

## 2. Setup (in VS Code)

1. Unzip the project and open the `portfolio` folder in VS Code (`File → Open Folder…`).
2. Open a terminal in VS Code: `` Ctrl + ` `` (Windows/Linux) or `Cmd + `` ` (Mac).
3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

4. Activate it:

   - **Windows (PowerShell):** `venv\Scripts\Activate.ps1`
   - **Windows (cmd):** `venv\Scripts\activate.bat`
   - **Mac/Linux:** `source venv/bin/activate`

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## 3. Run the site

```bash
python app.py
```

You'll see something like:

```
 * Running on http://127.0.0.1:5000
```

Open that link in your browser (Ctrl/Cmd + click it in the VS Code terminal), or just visit
**http://127.0.0.1:5000**.

The pages are:
- `/` — Home
- `/certifications` — NPTEL & Google Cloud certificates
- `/internships` — Internship certificates
- `/competitions` — Smart India Hackathon certificate

Flask's debug mode is on, so the page auto-reloads whenever you edit a template, CSS, or JS file.

## 4. Project structure

```
portfolio/
├── app.py                  # Flask app + routes + certification/internship data
├── requirements.txt
├── templates/
│   ├── base.html            # shared layout, IDE-tab navigation
│   ├── index.html           # home page
│   ├── certifications.html  # certifications list + modal
│   ├── internships.html     # internship feature rows
│   └── competitions.html    # SIH certificate showcase
└── static/
    ├── css/style.css
    ├── js/script.js
    └── images/
        ├── profile.jpg
        ├── certs/            # NPTEL + Google Cloud certificate images
        └── internships/      # internship certificate images
```

## 5. Customizing

- **Text/experience/projects:** edit `templates/index.html` directly.
- **Certifications list:** edit the `CERTS` list at the top of `app.py` — add/remove dicts, each with
  `title`, `org`, `score`, `duration`, `short` (2–3 letter badge), `img` (path under `static/`), `file` (display filename).
- **Internships:** edit the `INTERNSHIPS` list in `app.py` the same way.
- **Colors/fonts:** all design tokens are CSS variables at the top of `static/css/style.css` (`:root { ... }`).
- **Replace certificate/profile images:** just drop a new file with the same name into `static/images/...`
  (or update the `img` path in `app.py`).

## 6. Deploying (optional)

This is a normal Flask app, so it can be deployed to Render, Railway, PythonAnywhere, or any host that
runs Python — just make sure `debug=False` in production and use a proper WSGI server (e.g. `gunicorn app:app`).
