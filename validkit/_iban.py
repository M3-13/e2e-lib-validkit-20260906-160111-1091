"""IBAN-Prüfung (ISO 13616).

Die Funktion entfernt Leerzeichen, ignoriert Groß-/Kleinschreibung, prüft das
Länderkürzel und die Länge gegen eine Tabelle gängiger Länder, stellt die IBAN
um (erste vier Zeichen ans Ende, Buchstaben zu Zahlen) und prüft mod 97 == 1.
"""

_IBAN_LENGTHS: dict[str, int] = {
    "AL": 28,
    "AD": 24,
    "AT": 20,
    "AZ": 28,
    "BH": 22,
    "BE": 16,
    "BA": 20,
    "BR": 29,
    "BG": 22,
    "CR": 22,
    "HR": 21,
    "CY": 28,
    "CZ": 24,
    "DK": 18,
    "DO": 28,
    "EE": 20,
    "FO": 18,
    "FI": 18,
    "FR": 27,
    "GE": 22,
    "DE": 22,
    "GI": 23,
    "GR": 27,
    "GL": 18,
    "GT": 28,
    "HU": 28,
    "IS": 26,
    "IE": 22,
    "IL": 23,
    "IT": 27,
    "JO": 30,
    "KZ": 20,
    "KW": 30,
    "LV": 21,
    "LB": 28,
    "LI": 21,
    "LT": 20,
    "LU": 20,
    "MK": 19,
    "MT": 31,
    "MR": 27,
    "MU": 30,
    "MC": 27,
    "MD": 24,
    "ME": 22,
    "NL": 18,
    "NO": 15,
    "PK": 24,
    "PS": 29,
    "PL": 28,
    "PT": 25,
    "QA": 29,
    "RO": 24,
    "SM": 27,
    "SA": 24,
    "RS": 22,
    "SK": 24,
    "SI": 19,
    "ES": 24,
    "SE": 24,
    "CH": 21,
    "TN": 24,
    "TR": 26,
    "AE": 23,
    "GB": 22,
    "VA": 22,
    "VG": 24,
}


def is_valid_iban(text: str) -> bool:
    """Prüft, ob *text* eine gültige IBAN ist.

    Leerzeichen werden entfernt, Groß-/Kleinschreibung ignoriert, Länderkürzel
    und Länge gegen die Tabelle geprüft, die IBAN umgestellt und die Prüfziffer
    über mod 97 == 1 verifiziert. Bei Nicht-String-Eingabe wird ein TypeError
    ausgelöst (ohne Eingabewert in der Meldung).
    """
    if not isinstance(text, str):
        raise TypeError("is_valid_iban expects a string")
    compact = text.replace(" ", "").upper()
    if len(compact) < 5 or not (compact.isascii() and compact.isalnum()):
        return False
    length = _IBAN_LENGTHS.get(compact[:2])
    if length is None or len(compact) != length:
        return False
    rearranged = compact[4:] + compact[:4]
    digits = "".join(str(ord(ch) - ord("A") + 10) if "A" <= ch <= "Z" else ch for ch in rearranged)
    return int(digits) % 97 == 1
