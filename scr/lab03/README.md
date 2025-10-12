# Лабораторная работа 3: Статистический анализ текста

## Реализованные функций

### 1. normalize(text)
- Нормализует текст: удаляет спецсимволы, приводит к нижнему регистру
- Заменяет букву "ё" на "е"
- Возвращает очищенную строку

```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if not isinstance(text, str):
        raise ValueError("normalize: text не str")
    
    if len(text) == 0:
        raise ValueError("normalize: пустой text")

    result = (((text.replace("\t"," ")).replace("\r"," ")).replace("\n"," "))
    result = " ".join((result.strip()).split())

    if casefold:
        result = result.casefold()

    if yo2e:
        result = result.replace('ё', 'е')

    return result
```

### 2. tokenize(text)  
- Разделяет текст на слова (токены)
- Использует не-буквенно-цифровые символы как разделители
- Сохраняет слова с дефисами

```python
def tokenize(text: str) -> list[str]:
    import re

    if not isinstance(text, str):
        raise ValueError("tokenize: text не str")
    
    if len(text) == 0:
        raise ValueError("tokenize: пустой text")
    
    split_result = re.split(r"[^\w-]+", text)
    
    return [item for item in split_result if len(item) >= 1]
```

### 3. count_freq(tokens)
- Подсчитывает частоту каждого слова
- Возвращает словарь {слово: количество}

```python
def count_freq(tokens: list[str]) -> dict[str, int]:

    from collections import Counter

    if not isinstance(tokens, list):
        raise ValueError("tokenize: text не str")
    
    if len(tokens) == 0:
        raise ValueError("count_freq: пустой tokens")

    return dict(sorted(dict(Counter(tokens)).items(), key=lambda item: (-item[1], item[0])))
```

### 4. top_n(freq, n)
- Возвращает N самых частых слов
- Сортировка по убыванию частоты, при равенстве - по алфавиту
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    if not isinstance(freq, dict):
        raise ValueError("top_n: freq не  dict")
    
    if len(freq) == 0:
        raise ValueError("top_n: пустой freq")
    
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]
```

## Тест-кейсы

### in
![Задание B★](./images/lab03/img02.png)

### out
![Задание B★](./images/lab03/img02.png)
