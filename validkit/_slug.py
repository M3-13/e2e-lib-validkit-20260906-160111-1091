import re
import unicodedata

_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("slugify() argument must be a string")

    decomposed = unicodedata.normalize("NFKD", text)
    stripped = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    lowered = stripped.lower().replace("\u00df", "ss")
    slug = _NON_ALNUM_RE.sub("-", lowered)
    return slug.strip("-")
