import pytest

from validkit import luhn_check


def test_valid_card_number() -> None:
    assert luhn_check("4532015112830366") is True


def test_invalid_card_number() -> None:
    assert luhn_check("4532015112830367") is False


def test_card_number_with_spaces() -> None:
    assert luhn_check("4532 0151 1283 0366") is True


def test_card_number_with_hyphens() -> None:
    assert luhn_check("4532-0151-1283-0366") is True


def test_mixed_spaces_and_hyphens() -> None:
    assert luhn_check("4532 0151-1283 0366") is True


def test_single_zero() -> None:
    assert luhn_check("0") is True


def test_single_nonzero_digit() -> None:
    assert luhn_check("7") is False


def test_empty_input_raises_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check("")


def test_whitespace_only_raises_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check("   ")


def test_non_digit_characters_raise_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check("12a4")


def test_non_string_raises_type_error() -> None:
    with pytest.raises(TypeError):
        luhn_check(4532015112830366)  # type: ignore[arg-type]


def test_none_raises_type_error() -> None:
    with pytest.raises(TypeError):
        luhn_check(None)  # type: ignore[arg-type]


def test_error_message_does_not_leak_input() -> None:
    for bad_input in ("12a4", "4532-0151-x1283-0366"):
        with pytest.raises(ValueError) as exc_info:
            luhn_check(bad_input)
        assert bad_input not in str(exc_info.value)
