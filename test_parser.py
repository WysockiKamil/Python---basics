import pytest
from parser import Simple_parser

@pytest.mark.parametrize("input_text, expected_output", [
    ("2 + 3", 5),
    ("7 * 8", 56),
    ("10 - 4", 6),
    ("9 / 3", 3.0),
    ("0 * 10", 0),
    ("2 / 0", "Dzielenie przez zero jest niedozwolone."),
    ("5 & 2", "Nieprawidłowy operator. Dozwolone operatory to: +, -, *, /"),
    ("5.5 + 2", "Liczby muszą być całkowite."),
    ("5 +", "Wymagany format: liczba operator liczba (np. 2 + 3, 7 * 8)"),
    ("+ 5 2", "Liczby muszą być całkowite.")
])
def test_simple_parser(input_text, expected_output):
    if isinstance(expected_output, str):
        with pytest.raises(ValueError) as exc_info:
            Simple_parser(input_text)
        assert str(exc_info.value) == expected_output
    else:
        assert Simple_parser(input_text) == expected_output