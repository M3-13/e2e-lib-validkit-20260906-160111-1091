"""Normalisierung von Telefonnummern nach E.164.

``normalize_phone`` erkennt die drei üblichen Schreibweisen — internationale
Form mit führendem ``+``, internationale Form mit führendem ``00`` und die
nationale Form ohne Landeskennzahl — und vereinheitlicht sie zu einer
E.164-Nummer (``+<Landeskennzahl><nationale Rufnummer>``).
"""

_MAX_E164_DIGITS = 15
_MIN_E164_DIGITS = 3

# Reine Formatierungszeichen, die in einer geschriebenen Telefonnummer
# gefahrlos entfernt werden dürfen (Leerzeichen, Tabulator, Bindestrich,
# Klammern, Punkt, Schrägstrich).
_SEPARATORS = " \t-()./"
_SEPARATOR_TRANSLATION = str.maketrans("", "", _SEPARATORS)


def normalize_phone(text: str, country_code: str) -> str:
    """Normalisiere ``text`` zu einer E.164-Nummer.

    ``country_code`` wird ohne führendes ``+`` erwartet (z. B. ``"49"``).
    Eine nationale Rufnummer wird um die Landeskennzahl ergänzt, eine
    bereits internationale Nummer (``+`` oder ``00``) wird übernommen.
    """
    if not isinstance(text, str):
        raise TypeError("text muss ein String sein")
    if not isinstance(country_code, str):
        raise TypeError("country_code muss ein String sein")

    cc = country_code.strip()
    if cc.startswith("+"):
        cc = cc[1:]
    if not cc or not cc.isdigit():
        raise ValueError("country_code ist ungültig")

    cleaned = text.strip()

    if cleaned.startswith("+"):
        return _format_e164(_to_digits(cleaned[1:]))

    if cleaned.startswith("00"):
        return _format_e164(_to_digits(cleaned[2:]))

    digits = _to_digits(cleaned)
    if digits.startswith("0"):
        digits = digits[1:]
    if not digits:
        raise ValueError("Telefonnummer hat keine nationale Rufnummer")
    if digits.startswith(cc):
        return _format_e164(digits)
    return _format_e164(cc + digits)


def _to_digits(part: str) -> str:
    """Entferne Formatierungszeichen und prüfe, dass nur Ziffern bleiben."""
    digits = part.translate(_SEPARATOR_TRANSLATION)
    if not digits:
        raise ValueError("Telefonnummer enthält keine Ziffern")
    if not digits.isdigit():
        raise ValueError("Telefonnummer enthält ungültige Zeichen")
    return digits


def _format_e164(digits: str) -> str:
    """Prüfe die Ziffernlänge und stelle die ``+``-Schreibweise her."""
    if not _MIN_E164_DIGITS <= len(digits) <= _MAX_E164_DIGITS:
        raise ValueError("Telefonnummer hat eine unplausible Länge")
    return "+" + digits
