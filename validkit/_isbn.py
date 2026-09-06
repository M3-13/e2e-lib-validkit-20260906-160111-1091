def is_valid_isbn13(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    digits = text.replace("-", "").replace(" ", "")

    if len(digits) != 13 or not all(c in "0123456789" for c in digits):
        return False

    if not digits.startswith(("978", "979")):
        return False

    total = sum(int(c) * (1 if i % 2 == 0 else 3) for i, c in enumerate(digits))

    return total % 10 == 0
