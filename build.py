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

        if target.startswith(("http://", "https://", "#/term/")):
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

    if not match:
        return md

    return md[match.start():]


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

    files = sorted(content_dir.glob("*.md"))

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
