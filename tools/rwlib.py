# -*- coding: utf-8 -*-
"""Gemensamma hjälpfunktioner för robin-profil-verktygen. Enbart standardbibliotek. Python 3.8+."""
import re
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KITS = ROOT / "kits"
DOCS = ROOT / "docs"
EVALS = ROOT / "evals"
MEMORY_DIR = ROOT / "memory"
INBOX = ROOT / "inbox"
PLUGIN = ROOT.parent / "robin-plugin" / "ROBIN_PLUGIN.md"

ROW_RE = re.compile(r"^\d{4}-\d{2}-\d{2} \| [FPBLRM]/[UTSH] \| [^|]+ \| [^|]+ \| .+$")
LOGGRAD_RE = re.compile(r"^Föreslagen loggrad:\s*(\d{4}-\d{2}-\d{2}) \| ([FPBLRM]/[UTSH]) \| (.+)$")
CHANGELOG_TOP_RE = re.compile(r"^## v(\d+\.\d+\.\d+)\D+(\d{4}-\d{2}-\d{2})", re.M)
KIT_HEADER_RE = re.compile(r"Genererad ur robin-profil v(\d+\.\d+\.\d+)")
MARKERS = (
    "DoD:", "Parametrar:", "Konflikter:", "Antaganden:", "Förbud:",
    "Tes:", "Invändning:", "Rekommendation:",
    "Bevis:", "Antaget:",
    "Problem:", "Alternativ A:", "Alternativ B:",
    "Premiss utan stöd:", "Föreslagen loggrad:",
    "Nivå:", "Läge:", "Loggformat:",
)

BUDGETS = {"SOUL.md": 400, "USER.md": 600, "AGENTS.md": 900, "HEARTBEAT.md": 150}
MEMORY_BEKRAFTAT_BUDGET = 500
GEMINI_POST_MAX = 300
CHATGPT_BOX_MAX = 1400


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    """Skriver UTF-8 med LF. open() i stället för Path.write_text(newline=...) som kräver Python 3.10."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(path), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def today():
    return datetime.date.today().isoformat()


def current_version():
    """(version, datum) från översta posten i CHANGELOG.md."""
    m = CHANGELOG_TOP_RE.search(read(ROOT / "CHANGELOG.md"))
    return (m.group(1), m.group(2)) if m else ("0.0.0", today())


def word_count(text):
    return len(re.findall(r"\S+", text))


def strip_html_comments(text):
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def parse_karna(text=None):
    """Lista av (sektion, stycke) ur KARNA.md. '## ' delar sektioner, blankrad delar stycken."""
    if text is None:
        text = read(KITS / "KARNA.md")
    text = strip_html_comments(text)
    out = []
    buf = []
    state = {"section": None}

    def flush():
        if buf and state["section"] is not None:
            out.append((state["section"], " ".join(s.strip() for s in buf)))
        del buf[:]

    for line in text.splitlines():
        if line.startswith("## "):
            flush()
            state["section"] = line[3:].strip()
        elif line.startswith("#") or not line.strip():
            flush()
        elif state["section"] is not None:
            buf.append(line)
    flush()
    return out


def section_text(markdown, start_prefix, stop_prefix):
    """Rader från rubriken som börjar med start_prefix fram till rubriken som börjar med stop_prefix."""
    out = []
    on = False
    for line in markdown.splitlines():
        if line.startswith(start_prefix):
            on = True
        elif on and line.startswith(stop_prefix):
            break
        if on:
            out.append(line)
    return "\n".join(out).strip()


def fenced_rows(markdown):
    """Icke-tomma rader inne i ```-block."""
    rows = []
    infence = False
    for line in markdown.splitlines():
        if line.strip().startswith("```"):
            infence = not infence
            continue
        if infence and line.strip():
            rows.append(line.rstrip())
    return rows


def is_swedish(text):
    sv = len(re.findall(r"\b(och|att|är|inte|som|för|med|det|en|ett)\b", text, re.I))
    en = len(re.findall(r"\b(the|and|is|not|with|that|for|this|are|of)\b", text, re.I))
    return sv > en


def clean(line):
    return line.strip().lstrip("*-#> ").strip()


def first_nonempty(text):
    for line in text.splitlines():
        if line.strip():
            return clean(line)
    return ""


def has_marker(text, marker):
    """Markören står på egen rad och har innehåll: på samma rad, eller på nästa icke-tomma rad som inte är en annan markör."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        s = clean(line)
        if s.startswith(marker):
            rest = s[len(marker):].strip().strip("*").strip()
            if rest and rest not in ("—", "-"):
                return True
            for nxt in lines[i + 1:]:
                if nxt.strip():
                    return not clean(nxt).startswith(MARKERS)
            return False
    return False


def last_marker(text):
    last = None
    for line in text.splitlines():
        s = clean(line)
        for m in MARKERS:
            if s.startswith(m):
                last = m
    return last
