# ЛР7 — Тестирование: pytest + стиль (black)

>  Тестируем функции из `src/lib/text.py` (ЛР3) и `src/lib/text.py` (функции `json_to_csv`, `csv_to_json` из ЛР5).

---

## Результат ЛР

 **Выполнено:**

- Папка `tests/` с автотестами для:
  - `normalize`, `tokenize`, `count_freq`, `top_n` из `src/lib/text.py` (ЛР3);
  - `json_to_csv`, `csv_to_json` из `src/lib/text.py` (ЛР5).
- Конфиг: `pyproject.toml` с настройками pytest и black.
- Покрытие кода: **64%** (194 строки, 69 непокрытых).

---

## Реализованные тесты

### A. Тесты для `src/lib/text.py`

**Файл:** `tests/test_text.py`

#### 1. `normalize(text: str) -> str`

**Позитивные тесты (параметризованные):**
- Нормализация регистра и пробелов
- Обработка символов табуляции и переноса строки
- Замена буквы 'ё' на 'е'
- Удаление множественных пробелов

**Пример:**
```python
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
```

#### 2. `tokenize(text: str) -> list[str]`

**Позитивные тесты (параметризованные):**
- Разделение по знакам препинания
- Обработка составных слов (дефис)
- Обработка цифр
- Обработка эмодзи

#### 3. `count_freq(tokens: list[str]) -> dict[str, int]`

**Позитивные тесты:**
- Подсчет частоты слов
- Интеграция с `top_n`

#### 4. `top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]`

**Позитивные тесты:**
- Получение топ-N элементов
- Сортировка по частоте (убывание)
- **Сортировка по алфавиту при равных частотах** (tie-breaker)

**Пример теста tie-breaker:**
```python
def test_top_tie_breaker():
    freq = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq, 2) == [("aa", 2), ("bb", 2)]  # Сортировка по алфавиту
```

---

### B. Тесты для `src/lib/text.py` (функции конвертации)

**Файл:** `tests/test_json_csv.py`

#### 1. `json_to_csv(json_path: str, csv_path: str)`

**Позитивные тесты:**
-  Корректная конвертация JSON → CSV
-  Проверка количества записей
-  Проверка набора ключей/заголовков
-  Обработка отсутствующих полей (заполнение пустыми строками)

**Негативные тесты:**
-  Пустой JSON → `ValueError`
-  Несуществующий файл → `FileNotFoundError`
-  Директория вместо файла → `IsADirectoryError`
-  Неверный тип данных → `TypeError`
-  Неправильные расширения файлов → `ValueError`
-  Неподдерживаемая структура JSON → `ValueError`
-  Пустые пути → `ValueError`

#### 2. `csv_to_json(csv_path: str, json_path: str)`

**Позитивные тесты:**
-  Корректная конвертация CSV → JSON
-  Проверка количества записей
-  Проверка набора ключей

**Негативные тесты:**
-  Пустой CSV → `ValueError`
-  CSV без заголовка → `ValueError`
-  Несуществующий файл → `FileNotFoundError`
-  Директория вместо файла → `IsADirectoryError`
-  Неверный тип данных → `TypeError`
-  Неправильные расширения файлов → `ValueError`
-  Пустые пути → `ValueError`
-  Обработка ошибок csv.Sniffer → корректная обработка `csv.Error`

---

## Конфигурация проекта

### `pyproject.toml`

Настроены следующие секции:

```toml
[tool.pytest.ini_options]
pythonpath = [".", "src"]
addopts = "-q --cov=src --cov-report=term-missing"
testpaths = ["tests"]

[tool.coverage.run]
omit = [
    "src/__init__.py",
    "src/lib/__init__.py",
]

[tool.black]
line-length = 88
target-version = ["py311"]
```

---

## Команды запуска

### Установка зависимостей

#### Через `pyproject.toml`
```bash
pip install -e ".[dev]"
```

Зависимости для разработки:
- `pytest==9.0.1`
- `pytest-cov==7.0.0`
- `black==25.11.0`

### Запуск тестов

**Базовый запуск:**
```bash
pytest
```

**С подробным выводом:**
```bash
pytest -v
```

**С покрытием кода:**
```bash
pytest --cov=src --cov-report=term-missing
```

**Только определенный файл:**
```bash
pytest tests/test_text.py
pytest tests/test_json_csv.py
```

### Проверка стиля кода

**Форматирование:**
```bash
black .
```

**Проверка без изменений:**
```bash
black --check .
```

---

## Результаты тестирования

### Статистика тестов

- **Всего тестов:** 34
- **Успешно пройдено:** 34 ✅
- **Провалено:** 0

### Покрытие кода

**Текущее покрытие:** **64%**

```
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
src\lib\text.py     194     69    64%   102-114, 125-158, 195-203, 226-279
-----------------------------------------------
TOTAL               194     69    64%
```

**Непокрытые функции:**
- `print_table` (строки 102-114)
- `print_table_per_file` (строки 125-158)
- `read_text` (строки 195-203)
- `csv_to_xlsx` (строки 226-279)

Эти функции не входили в требования задания, поэтому тесты для них не написаны.

---

## Особенности реализации

### Использование фикстур pytest

**`tmp_path`** — встроенная фикстура для работы с временными файлами:
```python
def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    # ... тест
```

### Параметризация тестов

Использование `@pytest.mark.parametrize` для тестирования множества входных данных:
```python
@pytest.mark.parametrize(
    "src,expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
    ],
)
def test_normalize(src, expected):
    assert normalize(src) == expected
```

### Mock для обхода проверок

Использование `unittest.mock` для тестирования граничных случаев:
```python
from unittest.mock import patch

def test_json_to_csv_empty_paths():
    with patch('pathlib.Path.exists', return_value=True), \
         patch('pathlib.Path.is_file', return_value=True):
        with pytest.raises(ValueError, match="json_path пустой"):
            json_to_csv("", "out.csv")
```

### Проверка исключений

Использование `pytest.raises` для проверки корректной обработки ошибок:
```python
def test_normalize_errors():
    with pytest.raises(ValueError):
        normalize("")  # пустая строка
    with pytest.raises(ValueError):
        normalize(123)  # не строка
```

---

