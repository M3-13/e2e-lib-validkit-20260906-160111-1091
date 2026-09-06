import pytest

from validkit import clamp


def test_value_within_range_unchanged() -> None:
    assert clamp(5.0, 0.0, 10.0) == 5.0


def test_value_below_range_clamped_to_low() -> None:
    assert clamp(-1.0, 0.0, 10.0) == 0.0


def test_value_above_range_clamped_to_high() -> None:
    assert clamp(11.0, 0.0, 10.0) == 10.0


def test_low_greater_than_high_raises_value_error() -> None:
    with pytest.raises(ValueError):
        clamp(1.0, 5.0, 0.0)


def test_non_numeric_raises_type_error() -> None:
    with pytest.raises(TypeError):
        clamp("5", 0.0, 10.0)
    with pytest.raises(TypeError):
        clamp(5.0, None, 10.0)
    with pytest.raises(TypeError):
        clamp(5.0, 0.0, "10")


def test_bool_is_not_numeric() -> None:
    with pytest.raises(TypeError):
        clamp(True, 0.0, 10.0)


def test_value_equal_to_low_returns_low() -> None:
    assert clamp(0.0, 0.0, 10.0) == 0.0


def test_value_equal_to_high_returns_high() -> None:
    assert clamp(10.0, 0.0, 10.0) == 10.0


def test_negative_range() -> None:
    assert clamp(-7.0, -10.0, -1.0) == -7.0
    assert clamp(-20.0, -10.0, -1.0) == -10.0
    assert clamp(0.0, -10.0, -1.0) == -1.0


def test_integer_arguments() -> None:
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(11, 0, 10) == 10


def test_error_messages_do_not_leak_input_values() -> None:
    with pytest.raises(ValueError) as exc_info:
        clamp(42.0, 5.0, 0.0)
    assert "42" not in str(exc_info.value)
    assert "5" not in str(exc_info.value)
    assert "0" not in str(exc_info.value)

    with pytest.raises(TypeError) as exc_info:
        clamp(42.0, 0.0, "10")
    assert "42" not in str(exc_info.value)
