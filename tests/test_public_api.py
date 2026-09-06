import validkit


def test_import_validkit() -> None:
    assert validkit is not None


def test_all_exports_exactly_nine_names() -> None:
    assert len(validkit.__all__) == 9
    assert set(validkit.__all__) == {
        "is_valid_email",
        "luhn_check",
        "is_valid_iban",
        "is_valid_isbn13",
        "normalize_phone",
        "strip_accents",
        "mask_secret",
        "slugify",
        "clamp",
    }


def test_all_names_are_unique() -> None:
    assert len(validkit.__all__) == len(set(validkit.__all__))


def test_public_functions_are_callable() -> None:
    for name in validkit.__all__:
        assert callable(getattr(validkit, name))


def test_dir_exposes_exactly_nine_public_functions() -> None:
    public = [n for n in dir(validkit) if not n.startswith("_")]
    assert set(public) == set(validkit.__all__)
