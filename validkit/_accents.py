import unicodedata


def strip_accents(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("strip_accents() argument must be str")
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(c for c in decomposed if not unicodedata.combining(c))
