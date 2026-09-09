import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("a", "A"),
    ("тест", "Тест"),
    ("какой прекрасный день!", "Какой прекрасный день!")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("invalid_input", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("TXT", "TXT"),
    (None),
    ["list"],
    {"key": "value"},
])
def test_capitalize_negative(invalid_input):
    with pytest.raises(TypeError):
        string_utils.capitalize(invalid_input)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("no_spaces", "no_spaces"),
    ("  a b  ", "a b  "),
    ("\t", "\t"),
    ("  04 апреля 2023 ", "04 апреля 2023 "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("invalid_input", [
    ("", ""),
    ("   ", ""),
    (123),
    (None),
    ["list"],
])
def test_trim_negative(invalid_input):
    with pytest.raises(TypeError):
        string_utils.trim(invalid_input)


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "p", False),
    ("SkyPro", "U", False),
    ("", "a", False),
    ("aaa", "a", True),
    ("abc", "d", False),
    ("123", "f", False),
    ("123", "2", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("invalid_string, invalid_symbol", [
    (None, "a"),
    ("123", "a"),
    ("abc", None),
    ("abc", 123),
    ("     ", " "),
    ("     ", True),
    ("чудо", [5687352]),
])
def test_contains_negative(invalid_string, invalid_symbol):
    with pytest.raises(TypeError):
        string_utils.contains(invalid_string, invalid_symbol)


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("aaaa", "a", ""),
    ("abcabc", "bc", "aa"),
    ("no_match", "z", "no_match"),
    ("", "a", ""),
    ("test", "", "test"),
    (" а б в ", " ", "абв"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("invalid_string, invalid_symbol", [
    (None, "a"),
    ("123", "a"),
    ([ ], None),
    ("abc", None),
    ("привет", "e"),
])
def test_delete_symbol_negative(invalid_string, invalid_symbol):
    with pytest.raises(TypeError):
        string_utils.delete_symbol(invalid_string, invalid_symbol)
