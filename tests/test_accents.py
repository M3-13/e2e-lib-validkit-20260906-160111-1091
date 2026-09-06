import pytest

from validkit._accents import strip_accents


def test_strip_accents_removes_diacritics() -> None:
    assert strip_accents("café au lait \u2013 München") == "cafe au lait \u2013 Munchen"


def test_strip_accents_leaves_unaccented_text_unchanged() -> None:
    assert strip_accents("plain text 123") == "plain text 123"


def test_strip_accents_handles_empty_string() -> None:
    assert strip_accents("") == ""


def test_strip_accents_handles_only_combining_characters() -> None:
    assert strip_accents("\u0301\u0308") == ""


def test_strip_accents_raises_typeerror_for_non_string() -> None:
    with pytest.raises(TypeError):
        strip_accents(123)  # type: ignore[arg-type]


def test_strip_accents_typeerror_message_hides_value() -> None:
    with pytest.raises(TypeError) as exc_info:
        strip_accents(None)  # type: ignore[arg-type]
    assert "None" not in str(exc_info.value)
