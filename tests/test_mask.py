import pytest

from validkit import mask_secret


def test_keeps_first_four_and_masks_rest() -> None:
    assert mask_secret("geheim1234", keep=4) == "gehe******"


def test_text_shorter_than_keep_unchanged() -> None:
    assert mask_secret("abc", keep=4) == "abc"


def test_keep_zero_masks_everything() -> None:
    assert mask_secret("abc", keep=0) == "***"


def test_default_keep_is_four() -> None:
    assert mask_secret("geheim1234") == "gehe******"


def test_keep_equal_to_length_unchanged() -> None:
    assert mask_secret("abc", keep=3) == "abc"


def test_empty_string_unchanged() -> None:
    assert mask_secret("", keep=4) == ""
    assert mask_secret("", keep=0) == ""


def test_negative_keep_raises_value_error() -> None:
    with pytest.raises(ValueError):
        mask_secret("geheim1234", keep=-1)


def test_negative_keep_error_message_hides_secret() -> None:
    with pytest.raises(ValueError) as exc_info:
        mask_secret("geheim1234", keep=-1)
    assert "geheim1234" not in str(exc_info.value)


def test_non_string_raises_type_error() -> None:
    with pytest.raises(TypeError):
        mask_secret(1234)


def test_non_string_error_message_hides_input() -> None:
    with pytest.raises(TypeError) as exc_info:
        mask_secret(b"geheim1234")
    assert "geheim1234" not in str(exc_info.value)


def test_each_masked_char_becomes_exactly_one_star() -> None:
    text = "geheim1234"
    keep = 4
    result = mask_secret(text, keep=keep)
    assert len(result) == len(text)
    assert result[:keep] == text[:keep]
    assert set(result[keep:]) == {"*"}


def test_at_most_first_keep_chars_in_plaintext() -> None:
    text = "abcdefghij"
    keep = 3
    result = mask_secret(text, keep=keep)
    assert result[:keep] == "abc"
    assert "*" * (len(text) - keep) == result[keep:]
