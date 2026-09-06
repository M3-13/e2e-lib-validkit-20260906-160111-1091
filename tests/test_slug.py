import time

import pytest

from validkit import slugify


def test_slugify_basic_accents_and_punctuation() -> None:
    assert slugify("Héllo, Wörld!") == "hello-world"


def test_slugify_collapses_spaces_and_hyphens() -> None:
    assert slugify("  Schöne  Grüße  ") == "schone-grusse"


def test_slugify_only_special_characters_is_empty() -> None:
    assert slugify("!!!") == ""


def test_slugify_empty_string_is_empty() -> None:
    assert slugify("") == ""


def test_slugify_strips_leading_and_trailing_hyphens() -> None:
    assert slugify("-hello-world-") == "hello-world"


def test_slugify_preserves_digits() -> None:
    assert slugify("Café 123") == "cafe-123"


def test_slugify_lowercases() -> None:
    assert slugify("UPPER Case") == "upper-case"


def test_slugify_uppercase_sharp_s() -> None:
    assert slugify("GROẞES") == "grosses"


def test_slugify_non_string_raises_typeerror() -> None:
    with pytest.raises(TypeError):
        slugify(123)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        slugify(None)  # type: ignore[arg-type]


def test_slugify_typeerror_message_has_no_input_value() -> None:
    with pytest.raises(TypeError) as exc_info:
        slugify(12345)  # type: ignore[arg-type]
    assert "12345" not in str(exc_info.value)


def test_slugify_redos_safe_ten_thousand_chars() -> None:
    payload = "a" * 10_000 + "!"
    start = time.perf_counter()
    result = slugify(payload)
    elapsed = time.perf_counter() - start
    assert elapsed < 1.0
    assert result == "a" * 10_000


def test_slugify_redos_safe_non_alphanumeric() -> None:
    payload = "a-" * 5_000 + "!"
    start = time.perf_counter()
    result = slugify(payload)
    elapsed = time.perf_counter() - start
    assert elapsed < 1.0
    assert result == "a-" * 4_999 + "a"
