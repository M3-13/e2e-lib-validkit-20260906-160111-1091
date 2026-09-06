"""Begrenzen eines numerischen Werts auf einen Bereich [low, high]."""

from numbers import Real


def clamp(value: float, low: float, high: float) -> float:
    args = (value, low, high)
    if any(isinstance(arg, bool) for arg in args) or not all(isinstance(arg, Real) for arg in args):
        raise TypeError("clamp expects numeric arguments")
    if low > high:
        raise ValueError("low must not be greater than high")
    return min(max(value, low), high)
