"""Syntaxprüfung für E-Mail-Adressen."""

import re

# Lokaler Teil: erlaubte Zeichen ohne Punkt, mit Punkten als Trenner zwischen
# nicht-leeren Abschnitten (kein führender/abschließender/doppelter Punkt).
_LOCAL_PART = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*"

# Domain: ein oder mehrere Labels aus Alphanumerik und Bindestrich, jeweils
# ohne führenden/abschließenden Bindestrich, durch Punkte getrennt.
_DOMAIN_PART = (
    r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)*"
)

_EMAIL_RE = re.compile(rf"{_LOCAL_PART}@{_DOMAIN_PART}")


def is_valid_email(text: str) -> bool:
    """Prüft die Syntax einer E-Mail-Adresse; gibt ``True`` oder ``False`` zurück.

    Die Prüfung ist bewusst rein syntaktisch und terminiert linear in der
    Eingabelänge (kein katastrophales Backtracking).
    """
    if not isinstance(text, str):
        raise TypeError("is_valid_email() erwartet einen String")
    return _EMAIL_RE.fullmatch(text) is not None
