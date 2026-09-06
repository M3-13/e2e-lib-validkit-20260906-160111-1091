# validkit

validkit ist eine kleine, eigenständige Python-Bibliothek (nur Standardbibliothek)
mit neun reinen, einzeln nutzbaren Prüf- und Normalisierungsfunktionen für E-Mails,
Luhn-Prüfziffern, IBAN, ISBN-13, Telefonnummern (E.164), Akzentbereinigung,
Geheimnis-Maskierung, Slugs und Wertebereichsbegrenzung. Sie bietet eine
typannotierte öffentliche API über `validkit/__init__.py`, aussagekräftige Fehler
bei ungültigen Eingaben und vollständige pytest-Unit-Tests inklusive Grenz- und
Fehlerfällen.

## Tech-Stack

- **Sprache**: Python
- **Version**: 3.10+
- **Testen**: pytest
- **Abhängigkeiten**: keine (nur Standardbibliothek)

## Installation

```bash
pip install -e .
```

## Verwendung

Nach der Installation lässt sich das Paket direkt importieren:

```python
import validkit

print(validkit.__all__)
```

`validkit.__all__` listet exakt die neun öffentlichen Funktionen:

```python
[
    "is_valid_email",
    "luhn_check",
    "is_valid_iban",
    "is_valid_isbn13",
    "normalize_phone",
    "strip_accents",
    "mask_secret",
    "slugify",
    "clamp",
]
```

## Öffentliche API

### is_valid_email

Prüft, ob eine Zeichenkette eine gültige E-Mail-Adresse ist.

```python
from validkit import is_valid_email

is_valid_email("test@example.com")  # -> True
is_valid_email("a.b@sub.domain.org")  # -> True
is_valid_email("test@")  # -> False
is_valid_email("@example.com")  # -> False
is_valid_email("a..b@example.com")  # -> False
is_valid_email("test example.com")  # -> False
```

Nicht-String-Eingaben lösen einen `TypeError` aus.

### luhn_check

Prüft eine Ziffernfolge (z. B. Kreditkartennummer) über die Luhn-Prüfziffer.

```python
from validkit import luhn_check

luhn_check("4532015112830366")  # -> True
luhn_check("4532015112830367")  # -> False
luhn_check("4532 0151 1283 0366")  # -> True
```

Ungültige Zeichen (`luhn_check("12a4")`) oder eine leere Eingabe lösen einen
`ValueError` aus.

### is_valid_iban

Prüft eine IBAN auf Prüfziffer, Länderkürzel und Länge.

```python
from validkit import is_valid_iban

is_valid_iban("DE89 3704 0044 0532 0130 00")  # -> True
is_valid_iban("GB82 WEST 1234 5698 7654 32")  # -> True
```

Eine IBAN mit falscher Prüfziffer, unbekanntem Länderkürzel oder falscher Länge
ergibt `False`.

### is_valid_isbn13

Prüft eine ISBN-13 inklusive Prüfziffer.

```python
from validkit import is_valid_isbn13

is_valid_isbn13("978-3-16-148410-0")  # -> True
is_valid_isbn13("978-3-16-148410-1")  # -> False
is_valid_isbn13("1234567890123")  # -> False
is_valid_isbn13("97831614841")  # -> False
```

### normalize_phone

Normalisiert eine Telefonnummer nach E.164 (`+` gefolgt von Landeskennzahl und
nationaler Rufnummer).

```python
from validkit import normalize_phone

normalize_phone("030 1234567", "49")  # -> "+49301234567"
normalize_phone("+44 20 7946 0958", "44")  # -> "+442079460958"
normalize_phone("0049301234567", "49")  # -> "+49301234567"
```

Ungültige Zeichen wie `normalize_phone("abc", "49")` lösen einen `ValueError` aus.

### strip_accents

Entfernt Akzente und diakritische Zeichen.

```python
from validkit import strip_accents

strip_accents("café au lait – München")  # -> "cafe au lait – Munchen"
```

Zeichen ohne Akzent bleiben unverändert.

### mask_secret

Maskiert ein Geheimnis und lässt höchstens die ersten `keep` Zeichen unverändert.

```python
from validkit import mask_secret

mask_secret("geheim1234", keep=4)  # -> "gehe********"
mask_secret("abc", keep=4)  # -> "abc"
mask_secret("abc", keep=0)  # -> "***"
```

Negative `keep`-Werte lösen einen `ValueError` aus.

### slugify

Erzeugt einen URL-freundlichen Slug (kleingeschrieben, Akzente entfernt,
Sonderzeichen zu Bindestrichen).

```python
from validkit import slugify

slugify("Héllo, Wörld!")  # -> "hello-world"
slugify("  Schöne  Grüße  ")  # -> "schone-grusse"
slugify("!!!")  # -> ""
```

### clamp

Begrenzt einen Wert auf den Bereich `[low, high]`.

```python
from validkit import clamp

clamp(5.0, 0.0, 10.0)  # -> 5.0
clamp(-1.0, 0.0, 10.0)  # -> 0.0
clamp(11.0, 0.0, 10.0)  # -> 10.0
```

Ein ungültiger Bereich wie `clamp(1.0, 5.0, 0.0)` löst einen `ValueError` aus.

## Features

- Neun reine, typannotierte Prüf- und Normalisierungsfunktionen
- Keine externen Abhängigkeiten (nur Standardbibliothek)
- Aussagekräftige Fehler ohne Klartext-Eingabewerte in Meldungen
- Vollständige pytest-Unit-Tests inklusive Normal-, Grenz- und Fehlerfällen
