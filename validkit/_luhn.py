def luhn_check(digits: str) -> bool:
    if not isinstance(digits, str):
        raise TypeError("luhn_check erwartet einen String")

    cleaned = digits.replace(" ", "").replace("-", "")
    if cleaned == "":
        raise ValueError("Die Eingabe darf nicht leer sein")
    if not cleaned.isdigit():
        raise ValueError("Die Eingabe darf nur Ziffern, Leerzeichen und Bindestriche enthalten")

    total = 0
    for index, char in enumerate(reversed(cleaned)):
        value = int(char)
        if index % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9
        total += value

    return total % 10 == 0
