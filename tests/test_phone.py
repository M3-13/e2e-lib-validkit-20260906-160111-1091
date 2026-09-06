import pytest

from validkit import normalize_phone


def test_national_number_gets_country_code() -> None:
    assert normalize_phone("030 1234567", "49") == "+49301234567"


def test_international_plus_is_kept() -> None:
    assert normalize_phone("+44 20 7946 0958", "44") == "+442079460958"


def test_international_double_zero_is_unified() -> None:
    assert normalize_phone("0049301234567", "49") == "+49301234567"


def test_separators_are_stripped() -> None:
    assert normalize_phone("030-1234567", "49") == "+49301234567"
    assert normalize_phone("(030) 1234567", "49") == "+49301234567"
    assert normalize_phone("030.1234567", "49") == "+49301234567"
    assert normalize_phone("030/1234567", "49") == "+49301234567"


def test_already_present_country_code_is_not_doubled() -> None:
    assert normalize_phone("49301234567", "49") == "+49301234567"


def test_country_code_with_leading_plus_is_tolerated() -> None:
    assert normalize_phone("030 1234567", "+49") == "+49301234567"


def test_non_european_single_digit_country_code() -> None:
    assert normalize_phone("+1 415 555 0100", "1") == "+14155550100"


def test_invalid_characters_raise_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("abc", "49")


def test_empty_input_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("", "49")


def test_only_country_code_without_national_number_raises() -> None:
    with pytest.raises(ValueError):
        normalize_phone("0", "49")


def test_implausibly_long_number_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("0" + "1" * 20, "49")


def test_non_string_text_raises_type_error() -> None:
    with pytest.raises(TypeError):
        normalize_phone(301234567, "49")  # type: ignore[arg-type]


def test_none_text_raises_type_error() -> None:
    with pytest.raises(TypeError):
        normalize_phone(None, "49")  # type: ignore[arg-type]


def test_non_string_country_code_raises_type_error() -> None:
    with pytest.raises(TypeError):
        normalize_phone("030 1234567", 49)  # type: ignore[arg-type]


def test_invalid_country_code_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "abc")


def test_error_messages_do_not_leak_input() -> None:
    with pytest.raises(ValueError) as exc_info:
        normalize_phone("0049abc1234567", "49")
    assert "abc" not in str(exc_info.value)
    assert "1234567" not in str(exc_info.value)
    assert "0049" not in str(exc_info.value)
