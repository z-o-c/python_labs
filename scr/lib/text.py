def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализует текст путем удаления специальных символов и приведения к единому формату.
    
    Функция выполняет следующие преобразования:
    - Удаляет символы табуляции (\t) и переноса строки (\n)
    - Убирает лишние пробелы (в начале, конце и множественные внутри строки)
    - При необходимости приводит текст к нижнему регистру с использованием casefold()
    - Заменяет букву 'ё' на 'е' (опционально)
    """

    if not isinstance(text, str):
        raise ValueError("normalize: text не str")

    result = (((text.replace("\t"," ")).replace("\r"," ")).replace("\n"," "))
    result = " ".join((result.strip()).split())

    if casefold:
        result = result.casefold()

    if yo2e:
        result = result.replace('ё', 'е')

    return result

try:
    print(f"\nnormalize")
    print("Тест 1:", normalize("ПрИвЕт\nМИр\t"))
    print("Тест 2:", normalize("ёжик, Ёлка"))
    print("Тест 3:", normalize("Hello\r\nWorld"))
    print("Тест 3:", normalize("  двойные   пробелы  "))

except ValueError as e:
    print(f"Ошибка! {e}")


def tokenize(text: str) -> list[str]:
    """
    Функция разделяет входную строку на части, используя в качестве разделителей
    любые символы, которые не являются буквами или цифрами.
    """
    import re

    if not isinstance(text, str):
        raise ValueError("tokenize: text не str")
    
    split_result = re.split("[^\w-]+", text)
    
    return [item for item in split_result if len(item) >= 1]
    
try:
    print(f"\ntokenize")
    print("Тест 1:", tokenize("привет мир"))
    print("Тест 2:", tokenize("hello,world!!!"))
    print("Тест 3:", tokenize("по-настоящему круто"))
    print("Тест 4:", tokenize("2025 год"))
    print("Тест 5:", tokenize("emoji 😀 не слово"))

except ValueError as e:
    print(f"Ошибка! {e}")


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    AAAAAAAAAA
    """
    from collections import Counter

    if not isinstance(tokens, list):
        raise ValueError("tokenize: text не str")

    return dict(Counter(tokens))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    AAAAAAAAAAAAA
    """

    if not isinstance(freq, dict):
        raise ValueError("top_n: freq не  dict")
    
    return sorted(freq.items())[:n]

try:
    print(f"\ncount_freq + top_n")
    print("Тест 1:", top_n(count_freq(["a","b","a","c","b","a"]), 2))
    print("Тест 2:", top_n(count_freq(["bb","aa","bb","aa","cc"]), 2))

except ValueError as e:
    print(f"Ошибка! {e}")