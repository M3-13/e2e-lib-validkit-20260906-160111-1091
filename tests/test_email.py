"""Tests für validkit._email.is_valid_email."""

import time

import pytest

from validkit import is_valid_email


def test_valid_email_simple() -> None:
    assert is_valid_email("test@example.com") is True


def test_valid_email_with_dots_and_subdomain() -> None:
    assert is_valid_email("a.b@sub.domain.org") is True


def test_missing_domain_is_invalid() -> None:
    assert is_valid_email("test@") is False


def test_missing_local_part_is_invalid() -> None:
    assert is_valid_email("@example.com") is False


def test_consecutive_dots_in_local_part_are_invalid() -> None:
    assert is_valid_email("a..b@example.com") is False


def test_space_is_invalid() -> None:
    assert is_valid_email("test example.com") is False


def test_empty_string_is_invalid() -> None:
    assert is_valid_email("") is False


def test_only_at_sign_is_invalid() -> None:
    assert is_valid_email("@") is False


def test_multiple_at_signs_are_invalid() -> None:
    assert is_valid_email("a@b@example.com") is False


def test_leading_dot_in_local_part_is_invalid() -> None:
    assert is_valid_email(".test@example.com") is False


def test_trailing_dot_in_local_part_is_invalid() -> None:
    assert is_valid_email("test.@example.com") is False


def test_domain_with_hyphen_is_valid() -> None:
    assert is_valid_email("test@sub-domain.example.com") is True


def test_domain_leading_hyphen_is_invalid() -> None:
    assert is_valid_email("test@-example.com") is False


@pytest.mark.parametrize(
    "value",
    [None, 42, 1.5, True, ["test@example.com"], {"a": 1}, b"test@example.com", object()],
)
def test_non_string_input_raises_type_error(value: object) -> None:
    with pytest.raises(TypeError):
        is_valid_email(value)  # type: ignore[arg-type]


def test_type_error_message_does_not_contain_input_value() -> None:
    with pytest.raises(TypeError) as exc_info:
        is_valid_email(123456789)  # type: ignore[arg-type]
    assert "123456789" not in str(exc_info.value)


def test_redos_resistance_valid_10k_chars_under_1s() -> None:
    start = time.monotonic()
    result = is_valid_email(("a" * 10_000) + "@example.com")
    elapsed = time.monotonic() - start
    assert result is True
    assert elapsed < 1.0


def test_redos_resistance_invalid_10k_chars_under_1s() -> None:
    start = time.monotonic()
    result = is_valid_email(("a" * 10_000) + "b@")
    elapsed = time.monotonic() - start
    assert result is False
    assert elapsed < 1.0
