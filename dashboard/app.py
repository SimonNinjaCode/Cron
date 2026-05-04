#!/usr/bin/env python3
"""Delphi Dashboard — read-only web UI for the cron pipeline."""

import re
import argparse
from pathlib import Path
from datetime import datetime
from urllib.parse import quote, unquote

from flask import Flask, render_template, request, abort, redirect, url_for
import markdown as md_lib
from pygments.formatters import HtmlFormatter

BASE_DIR = Path(__file__).parent.parent.resolve()
EXCLUDED_DIRS = {"dashboard", ".claude", ".git", ".venv", "__pycache__"}

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.jinja_env.filters["urlquote"] = lambda s: quote(str(s), safe="")


def safe_resolve(rel_path: str) -> Path:
    """Resolve a relative path inside BASE_DIR; abort 403 on traversal."""
    try:
        resolved = (BASE_DIR / rel_path).resolve()
    except Exception:
        abort(403)
    base = str(BASE_DIR)
    if not str(resolved).startswith(base + "/") and str(resolved) != base:
        abort(403)
    return resolved


def _field(content: str, name: str) -> str:
    m = re.search(rf"\*\*{name}:\*\*\s*`?([^`\n]+)`?", content)
    return m.group(1).strip() if m else ""


def _prompt_section(content: str) -> str | None:
    m = re.search(r"^## Prompt\s*\n(.*)", content, re.MULTILINE | re.DOTALL)
    if not m:
        return None
    text = m.group(1).strip()
    # Drop a leading "> Prompt not yet written..." stub line
    if text.startswith("> Prompt not yet written"):
        return None
    return text


def discover_jobs() -> list[dict]:
    jobs = []
    for d in sorted(BASE_DIR.iterdir()):
        if not d.is_dir():
            continue
        if d.name.startswith(".") or d.name in EXCLUDED_DIRS:
            continue
        readme = d / "README.md"
        if not readme.exists():
            continue
        content = readme.read_text()
        outputs = sorted(
            [f for f in d.glob("*.md") if f.name != "README.md"],
            reverse=True,
        )
        latest = outputs[0] if outputs else None
        status = _field(content, "Status")
        jobs.append({
            "name": d.name,
            "cadence": _field(content, "Cadence"),
            "cron": _field(content, "Cron"),
            "output_pattern": _field(content, "Output"),
            "status": status,
            "is_active": "active" in status.lower() and "local" not in status.lower(),
            "is_local": "local only" in status.lower(),
            "has_diagram": (d / "diagram.mmd").exists(),
            "has_prompt": _prompt_section(content) is not None,
            "output_count": len(outputs),
            "latest_rel": str(latest.relative_to(BASE_DIR)) if latest else None,
            "latest_date": re.search(r"(\d{4}-\d{2}-\d{2})", latest.name).group(1)
                           if latest and re.search(r"\d{4}-\d{2}-\d{2}", latest.name) else "",
        })
    return jobs


def get_all_outputs() -> list[dict]:
    rows = []
    for d in sorted(BASE_DIR.iterdir()):
        if not d.is_dir() or d.name.startswith(".") or d.name in EXCLUDED_DIRS:
            continue
        if not (d / "README.md").exists():
            continue
        for f in sorted(d.glob("*.md"), reverse=True):
            if f.name == "README.md":
                continue
            m = re.search(r"(\d{4}-\d{2}-\d{2})\.md$", f.name)
            date_str = m.group(1) if m else ""
            try:
                date_sort = datetime.fromisoformat(date_str) if date_str else \
                            datetime.fromtimestamp(f.stat().st_mtime)
            except ValueError:
                date_sort = datetime.fromtimestamp(f.stat().st_mtime)
            rows.append({
                "job": d.name,
                "filename": f.name,
                "date": date_str,
                "date_sort": date_sort,
                "rel": str(f.relative_to(BASE_DIR)),
            })
    rows.sort(key=lambda x: x["date_sort"], reverse=True)
    return rows


@app.route("/")
def index():
    return redirect(url_for("jobs"))


@app.route("/jobs")
def jobs():
    return render_template("jobs.html", jobs=discover_jobs())


@app.route("/job")
def job():
    name = unquote(request.args.get("name", ""))
    if not name or "/" in name or name.startswith("."):
        abort(400)
    folder = BASE_DIR / name
    if not folder.is_dir() or not (folder / "README.md").exists():
        abort(404)
    safe_resolve(name)

    content = (folder / "README.md").read_text()
    status = _field(content, "Status")

    mmd_file = folder / "diagram.mmd"
    mmd_content = mmd_file.read_text() if mmd_file.exists() else None

    prompt_raw = _prompt_section(content)
    prompt_html = md_lib.markdown(
        prompt_raw, extensions=["tables", "fenced_code"]
    ) if prompt_raw else None

    outputs = []
    for f in sorted(folder.glob("*.md"), reverse=True):
        if f.name == "README.md":
            continue
        m = re.search(r"(\d{4}-\d{2}-\d{2})\.md$", f.name)
        outputs.append({
            "filename": f.name,
            "date": m.group(1) if m else "",
            "rel": str(f.relative_to(BASE_DIR)),
        })

    return render_template(
        "job.html",
        name=name,
        cadence=_field(content, "Cadence"),
        cron=_field(content, "Cron"),
        status=status,
        is_active="active" in status.lower() and "local" not in status.lower(),
        is_local="local only" in status.lower(),
        mmd_content=mmd_content,
        prompt_html=prompt_html,
        outputs=outputs,
    )


@app.route("/outputs")
def outputs():
    all_rows = get_all_outputs()
    job_filter = request.args.get("job", "")
    filtered = [r for r in all_rows if r["job"] == job_filter] if job_filter else all_rows
    job_names = sorted({r["job"] for r in all_rows})
    return render_template(
        "outputs.html",
        outputs=filtered,
        job_names=job_names,
        job_filter=job_filter,
    )


@app.route("/view")
def view():
    path = request.args.get("path", "")
    if not path:
        abort(400)
    resolved = safe_resolve(path)
    if not resolved.exists() or not resolved.is_file():
        abort(404)
    content = resolved.read_text()
    html = md_lib.markdown(content, extensions=["tables", "fenced_code", "toc"])
    return render_template("viewer.html", html=html, title=resolved.name, path=path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delphi Dashboard")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()
    print(f"Starting dashboard at http://{args.host}:{args.port}")
    app.run(host=args.host, port=args.port, debug=False)
