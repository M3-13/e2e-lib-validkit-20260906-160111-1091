import pytest

from validkit import is_valid_iban


def test_valid_german_iban() -> None:
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True


def test_valid_british_iban() -> None:
    assert is_valid_iban("GB82 WEST 1234 5698 7654 32") is True


def test_lowercase_and_extra_spaces_accepted() -> None:
    assert is_valid_iban("de89 3704 0044 0532 0130 00") is True


def test_invalid_check_digit() -> None:
    assert is_valid_iban("DE88 3704 0044 0532 0130 00") is False


def test_unknown_country() -> None:
    assert is_valid_iban("XX89 3704 0044 0532 0130 00") is False


def test_wrong_length() -> None:
    assert is_valid_iban("DE89 3704 0044 0532 0130") is False


def test_wrong_length_too_long() -> None:
    assert is_valid_iban("DE89 3704 0044 0532 0130 0000") is False


def test_non_string_raises_type_error() -> None:
    with pytest.raises(TypeError):
        is_valid_iban(12345)


def test_none_raises_type_error() -> None:
    with pytest.raises(TypeError):
        is_valid_iban(None)


def test_type_error_message_contains_no_value() -> None:
    with pytest.raises(TypeError) as excinfo:
        is_valid_iban(["DE89 3704 0044 0532 0130 00"])
    assert "DE89" not in str(excinfo.value)
