#!/usr/bin/env python3

from __future__ import annotations

import json
import logging
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import markdown

CONTENT_DIR = Path("../project-management-wiki.wiki")
OUTPUT_FILE = Path("data/terms.json")

MARKDOWN_EXTENSIONS = (
    "tables",
    "fenced_code",
    "sane_lists",
    "toc",
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)

# --------------------------------------------------
# Character normalization
# --------------------------------------------------

POLISH_CHARS = str.maketrans(
    {
        "ą": "a",
        "ć": "c",
        "ę": "e",
        "ł": "l",
        "ń": "n",
        "ó": "o",
        "ś": "s",
        "ź": "z",
        "ż": "z",
        "Ą": "a",
        "Ć": "c",
        "Ę": "e",
        "Ł": "l",
        "Ń": "n",
        "Ó": "o",
        "Ś": "s",
        "Ź": "z",
        "Ż": "z",
    }
)

# --------------------------------------------------
# Regexes
# --------------------------------------------------

TITLE_RE = re.compile(
    r"^#\s+(.+)$",
    re.MULTILINE,
)

CATEGORY_RE = re.compile(
    r"\*\*Kategoria:\*\*\s*\[(.*?)\]"
)

DEFINITION_RE = re.compile(
    r"##\s+Definicja\s+(.*?)(?:\n##|\Z)",
    re.DOTALL,
)

RELATED_RE = re.compile(
    r"##\s+Powiązania\s+(.*?)(?:\n##|\Z)",
    re.DOTALL,
)

LINK_RE = re.compile(
    r"\[([^\]]+)\]\(([^)]+)\)"
)

DEFINITION_HEADING_RE = re.compile(
    r"^##\s+(?:Definicja\b|Hasła w tej kategorii\b)",
    re.MULTILINE,
)

# --------------------------------------------------
# Models
# --------------------------------------------------


@dataclass(slots=True, frozen=True)
class RelatedTerm:
    title: str
    slug: str


@dataclass(slots=True, frozen=True)
class Term:
    slug: str
    title: str
    category: str
    description: str
    related: list[RelatedTerm]
    content: str
    search: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


# --------------------------------------------------
# Helpers
# --------------------------------------------------


def slugify(text: str) -> str:
    """Convert text into a URL-friendly slug."""
    text = text.translate(POLISH_CHARS)
    text = text.lower().strip()

    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text)

    return text.strip("-")


def normalize_search(text: str) -> str:
    """Normalize searchable text."""
    text = text.translate(POLISH_CHARS)
    text = text.lower()

    text = re.sub(r"[^a-z0-9\s]+", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# --------------------------------------------------
# Metadata extraction
# --------------------------------------------------


def extract_title(md: str) -> str:
    match = TITLE_RE.search(md)
    return match.group(1).strip() if match else ""


def extract_category(md: str) -> str:
    match = CATEGORY_RE.search(md)
    return match.group(1).strip() if match else ""


def extract_definition(md: str) -> str:
    """Return the first non-empty paragraph from the Definicja section."""
    match = DEFINITION_RE.search(md)

    if not match:
        return ""

    block = match.group(1)

    paragraphs = [
        p.strip()
        for p in block.split("\n\n")
        if p.strip()
    ]

    for paragraph in paragraphs:
        if paragraph.startswith("**Kategoria:**"):
            continue

        return re.sub(r"\s+", " ", paragraph)

    return ""


def extract_related(md: str) -> list[RelatedTerm]:
    match = RELATED_RE.search(md)

    if not match:
        return []

    block = match.group(1)

    return [
        RelatedTerm(
            title=title.strip(),
            slug=slugify(Path(target).stem),
        )
        for title, target in LINK_RE.findall(block)
    ]


# --------------------------------------------------
# Markdown processing
# --------------------------------------------------


def rewrite_wiki_links(md: str) -> str:
    """
    Convert wiki links:

        [ADKAR](ADKAR)

    into:

        [ADKAR](#/term/adkar)
    """

    def replace(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2).strip()

        if target.startswith(("http://", "https://", "#/term/", "#")):
            return match.group(0)

        # Do not rewrite links to assets (images, PDFs, archives, data files)
        if target.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf", ".zip", ".tar.gz", ".txt", ".csv")):
            return match.group(0)

        slug = slugify(Path(target).stem)

        return f"[{label}](#/term/{slug})"

    return LINK_RE.sub(replace, md)


def trim_to_definition(md: str) -> str:
    """
    Remove everything before the first
    relevant content section.
    """
    match = DEFINITION_HEADING_RE.search(md)

    if match:
        return md[match.start():]

    # For pages without a definition section (e.g., Sciezki-nauki.md, Slownik.md),
    # strip the main title heading (# Title) and any leading navigation links.
    lines = md.splitlines()
    content_start_idx = 0

    # Skip the main title heading if it exists
    if lines and lines[0].startswith("# "):
        content_start_idx = 1

    # Skip any leading empty lines or navigation lines
    while content_start_idx < len(lines):
        line = lines[content_start_idx].strip()
        if not line:
            content_start_idx += 1
            continue
        # Skip navigation links containing Home, Slownik, or Sciezki-nauki in brackets
        if ("Home" in line or "Slownik" in line or "Sciezki-nauki" in line) and ("[" in line and "]" in line):
            content_start_idx += 1
            continue
        break

    return "\n".join(lines[content_start_idx:])


# --------------------------------------------------
# Filesystem helpers
# --------------------------------------------------


def read_markdown(path: Path) -> str:
    """Read a markdown file."""
    return path.read_text(encoding="utf-8")


def write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    """Write JSON atomically."""
    path.parent.mkdir(parents=True, exist_ok=True)

    temp_path = path.with_suffix(".tmp")

    with temp_path.open("w", encoding="utf-8") as fh:
        json.dump(
            payload,
            fh,
            ensure_ascii=False,
            separators=(",", ":"),
        )

    temp_path.replace(path)


# --------------------------------------------------
# Term builder
# --------------------------------------------------


def build_term(path: Path) -> Term | None:
    try:
        original_md = read_markdown(path)

        title = extract_title(original_md)

        if not title:
            if path.stem == "Home":
                title = "Strona główna"
            else:
                logger.warning(
                    "Skipping %s (missing title)",
                    path.name,
                )
                return None

        slug = slugify(path.stem)

        category = extract_category(original_md)
        description = extract_definition(original_md)
        related = extract_related(original_md)

        md = rewrite_wiki_links(
            trim_to_definition(original_md)
        )

        html = markdown.markdown(
            md,
            extensions=MARKDOWN_EXTENSIONS,
        )

        search_text = normalize_search(
            " ".join(
                (
                    title,
                    category,
                    description,
                    *(rel.title for rel in related),
                )
            )
        )

        return Term(
            slug=slug,
            title=title,
            category=category,
            description=description,
            related=related,
            content=html,
            search=search_text,
        )

    except Exception:
        logger.exception(
            "Failed processing %s",
            path.name,
        )
        return None


def copy_assets(content_dir: Path, target_dir: Path) -> None:
    """Copy non-markdown asset files (e.g. images) to target directory."""
    asset_extensions = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf", ".zip", ".tar.gz", ".txt", ".csv"}
    for path in content_dir.iterdir():
        if path.is_file() and path.suffix.lower() in asset_extensions:
            dest = target_dir / path.name
            logger.info("Copying asset %s to %s", path.name, dest)
            dest.write_bytes(path.read_bytes())


# --------------------------------------------------
# Main build
# --------------------------------------------------


def build(
    content_dir: Path = CONTENT_DIR,
    output_file: Path = OUTPUT_FILE,
) -> None:
    if not content_dir.exists():
        raise FileNotFoundError(
            f"Content directory not found: {content_dir}"
        )

    # Copy asset files (images, etc.) to project root
    copy_assets(content_dir, Path("."))

    files = sorted(
        path for path in content_dir.glob("*.md")
        if not path.name.startswith("_")
    )

    logger.info(
        "Found %d markdown files",
        len(files),
    )

    terms: list[Term] = []

    for file in files:
        logger.info(
            "Processing %s",
            file.name,
        )

        term = build_term(file)

        if term is not None:
            terms.append(term)

    slugs = [term.slug for term in terms]

    duplicate_slugs = {
        slug
        for slug in slugs
        if slugs.count(slug) > 1
    }

    if duplicate_slugs:
        raise ValueError(
            "Duplicate generated slugs detected: "
            + ", ".join(sorted(duplicate_slugs))
        )

    payload = {
        "version": 1,
        "count": len(terms),
        "terms": [
            term.to_dict()
            for term in terms
        ],
    }

    write_json_atomic(
        output_file,
        payload,
    )

    logger.info(
        "Generated %s with %d terms",
        output_file,
        len(terms),
    )


if __name__ == "__main__":
    build()
