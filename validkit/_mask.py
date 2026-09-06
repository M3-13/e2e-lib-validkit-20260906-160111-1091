def mask_secret(text: str, keep: int = 4) -> str:
    """Maskiere ein Geheimnis: die ersten ``keep`` Zeichen bleiben erhalten,
    jedes weitere Zeichen wird durch genau ein ``*`` ersetzt.

    ``keep == 0`` maskiert den gesamten Text; negatives ``keep`` ist ein
    ValueError; ein Nicht-String ``text`` ist ein TypeError.
    """
    if not isinstance(text, str):
        raise TypeError("mask_secret erwartet einen String")
    if not isinstance(keep, int):
        raise TypeError("keep muss eine Ganzzahl sein")
    if keep < 0:
        raise ValueError("keep darf nicht negativ sein")
    if keep == 0:
        return "*" * len(text)
    if len(text) <= keep:
        return text
    return text[:keep] + "*" * (len(text) - keep)
