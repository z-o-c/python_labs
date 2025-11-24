import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "src,expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize(src, expected):
    assert normalize(src) == expected


@pytest.mark.parametrize(
    "src,expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ],
)
def test_tokenize(src, expected):
    assert tokenize(src) == expected


def test_count_and_top():
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]


def test_top_tie_breaker():
    freq = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq, 2) == [("aa", 2), ("bb", 2)]


def test_normalize_errors():
    with pytest.raises(ValueError):
        normalize("")  # пустая строка
    with pytest.raises(ValueError):
        normalize(123)  # не строка


def test_tokenize_errors():
    with pytest.raises(ValueError):
        tokenize("")  # пустая строка
    with pytest.raises(ValueError):
        tokenize(123)  # не строка


def test_count_freq_errors():
    with pytest.raises(ValueError):
        count_freq([])  # пустой список
    with pytest.raises(ValueError):
        count_freq("abc")  # не список


def test_top_n_errors():
    with pytest.raises(ValueError):
        top_n({})  # пустой словарь
    with pytest.raises(ValueError):
        top_n(["a", "b"])  # не словарь
