import pytest

from validkit import is_valid_isbn13


def test_valid_isbn_with_hyphens() -> None:
    assert is_valid_isbn13("978-3-16-148410-0") is True


def test_valid_isbn_plain_digits() -> None:
    assert is_valid_isbn13("9783161484100") is True


def test_valid_isbn_with_spaces() -> None:
    assert is_valid_isbn13("978 3 16 148410 0") is True


def test_wrong_check_digit() -> None:
    assert is_valid_isbn13("978-3-16-148410-1") is False


def test_invalid_prefix() -> None:
    assert is_valid_isbn13("1234567890123") is False


def test_too_short() -> None:
    assert is_valid_isbn13("97831614841") is False


def test_too_long() -> None:
    assert is_valid_isbn13("97831614841000") is False


def test_non_digit_characters() -> None:
    assert is_valid_isbn13("978-3-16-14841X-0") is False


def test_empty_string() -> None:
    assert is_valid_isbn13("") is False


def test_only_separators() -> None:
    assert is_valid_isbn13("---   ") is False


def test_thirteen_zeros() -> None:
    assert is_valid_isbn13("0000000000000") is False


def test_valid_979_prefix() -> None:
    assert is_valid_isbn13("979-1-2345-6789-6") is True


def test_invalid_979_prefix_check_digit() -> None:
    assert is_valid_isbn13("9791234567890") is False


@pytest.mark.parametrize("value", [9783161484100, None, ["9783161484100"], 13.0])
def test_non_string_raises_type_error(value: object) -> None:
    with pytest.raises(TypeError):
        is_valid_isbn13(value)  # type: ignore[arg-type]
