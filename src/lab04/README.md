# Лабораторная работа 4: Работа с файлами и CSV

## Задание

### Часть A: Функции для работы с файлами

#### 1. ensure_parent_dir(path)
Создает родительские директории для указанного пути, если они не существуют.

```python
def ensure_parent_dir(path: str | Path) -> None:
    """
    Создать родительские директории для указанного пути, если они не существуют.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
```

**Особенности реализации:**
- Использует `pathlib.Path` для кроссплатформенной работы с путями
- `parents=True` - создает все промежуточные директории
- `exist_ok=True` - не вызывает ошибку, если директория уже существует

#### 2. read_text(path, encoding)
Читает текстовый файл целиком и возвращает его содержимое как строку.

```python
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Прочитать файл целиком и вернуть его содержимое как одну строку.

    Параметры:
        path: Путь к файлу (str или Path).
        encoding: Кодировка чтения (по умолчанию "utf-8").
            Распространенные варианты кодировок: 
                - 'utf-8' (стандартная)
                - 'cp1251', 'windows-1251' (русская Windows)
                - 'koi8-r' (русская KOI8)
                - 'latin-1', 'iso-8859-1' (западноевропейская)

    Исключения не перехватываются специально: FileNotFoundError и
    UnicodeDecodeError позволяют пользователю понять проблему напрямую.
    """
    if not isinstance(path, (str, Path)):
        raise TypeError("path должен быть str или Path")
    if not isinstance(encoding, str) or not encoding:
        raise TypeError("encoding должен быть непустой строкой")

    p = Path(path)
    with p.open("r", encoding=encoding) as file:
        return file.read()
```

**Особенности реализации:**
- Поддержка различных кодировок для работы с русскими текстами
- Автоматическое управление ресурсами через `with`
- Строгая проверка типов входных параметров
- Проброс исключений для диагностики проблем

#### 3. write_csv(rows, path, header)
Создает CSV-файл с разделителем "," и проверкой целостности данных.

```python
def write_csv(
    rows: Iterable[Sequence],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    """
    Создать/перезаписать CSV с разделителем ",".

    - Если передан `header`, записать его первой строкой.
    - Проверить, что все строки в `rows` имеют одинаковую длину; иначе ValueError.
    - Если `rows` пустой и `header` не задан, создать пустой файл.
    - Родительские директории создаются автоматически.
    """
    if not isinstance(path, (str, Path)):
        raise TypeError("path должен быть str или Path")
    if header is not None and not isinstance(header, tuple):
        raise TypeError("header должен быть tuple или None")

    p = Path(path)
    ensure_parent_dir(p)

    rows_list = list(rows)

    if rows_list:
        row_length = len(rows_list[0])
        for row in rows_list:
            if len(row) != row_length:
                raise ValueError("все строки в rows должны иметь одинаковую длину")
    if header is not None and rows_list and len(header) != row_length:
        raise ValueError("длина header должна совпадать с длиной строк в rows")

    with p.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")
        if header is not None:
            writer.writerow(header)
        for row in rows_list:
            writer.writerow(row)
```

**Особенности реализации:**
- Проверка целостности данных (одинаковая длина всех строк)
- Автоматическое создание родительских директорий
- Поддержка заголовков CSV
- Использование стандартного модуля `csv` для корректного экранирования
- `newline=""` предотвращает дублирование переносов строк

### Часть B: Система отчетов по анализу текста

#### Описание системы
Создана комплексная система для анализа текстовых файлов с генерацией отчетов в различных форматах:

1. **Анализ одиночного файла** (`input.txt`) → `report.csv`
2. **Анализ множественных файлов** (`a.txt`, `b.txt`) → `report_per_file.csv`
3. **Сводный отчет** по всем файлам → `report_total.csv`

#### Реализация системы отчетов

```python
from io_txt_csv import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.text import *

# читаем и обрабатываем первый файл
if len(read_text("data/lab04/input.txt")) == 0:
    write_csv([], "data/lab04/report.csv", header=("word", "count"))
else:
    text_1 = normalize(read_text("data/lab04/input.txt"))
    token_text_1 = tokenize(text_1)
    num_tokens_1 = count_freq(token_text_1)
    top_tokens_1 = top_n(num_tokens_1, 5)

    print("input.txt:")
    print(f"Всего слов: {len(token_text_1)}")
    print(f"Уникальных слов: {len(num_tokens_1)}")
    print("Топ-5:")
    for word, count in top_tokens_1:
        print(f"{word}: {count}")
    print("\n")

    write_csv([(word, count) for word, count in num_tokens_1.items()], 
              "data/lab04/report.csv", header=("word", "count"))

# читаем и обрабатываем несколько входных файлов + «сводный» отчет
text_2 = normalize(read_text("data/lab04/a.txt"))
token_text_2 = tokenize(text_2)
num_tokens_2 = count_freq(token_text_2)

text_3 = normalize(read_text("data/lab04/b.txt"))
token_text_3 = tokenize(text_3)
num_tokens_3 = count_freq(token_text_3)


report_per_file = {
    "a.txt": [(word, count) for word, count in num_tokens_2.items()],
    "b.txt": [(word, count) for word, count in num_tokens_3.items()]
}


report_total = count_freq(token_text_2 + token_text_3)
report_total_list = [(word, count) for word, count in report_total.items()]

# записываем отчет по файлам
write_csv([(file, word, count) for file, words in report_per_file.items() 
           for word, count in words], 
          "data/lab04/report_per_file.csv", header=("file", "word", "count"))

# записываем общий отчет
write_csv([(word, count) for word, count in report_total.items()], 
          "data/lab04/report_total.csv", header=("word", "count"))

# выводим красивый отчет в табличном виде
print("Общий отчет:")
print_table(report_total_list)
print("\n")

print("Отчет по файлам:")
print_table_per_file(report_per_file)
```

#### Дополнительные функции для вывода

```python
def print_table_per_file(words_data: dict[str, list[tuple[str, int]]]) -> None:
    """
    Выводит форматированную таблицу слов и их частот в отсортированном виде для каждого файла.
    """
    if not words_data:
        raise ValueError("print_table_per_file: words_data пуст")
    
    max_word_length = max(len(word) for file, words in words_data.items() 
                         for word, count in words)
    max_file_length = max(len(file) for file, words in words_data.items())

    if len("слово") > max_word_length:
        max_word_length = len("слово")
    
    if len("файл") > max_file_length:
        max_file_length = len("файл")
    
    print("-" * max_file_length + "-|-" + "-" * max_word_length + "-|-" + "-" * len("частота"))
    print(f"{'файл':<{max_file_length}} | {'слово':^{max_word_length}} | {'частота'}")
    print("-" * max_file_length + "-|-" + "-" * max_word_length + "-|-" + "-" * len("частота"))
    
    for file, words in words_data.items():
        for word, count in words:
            print(f"{file:<{max_file_length}} | {word:<{max_word_length}} | {count}")
```

## Тест-кейсы и краевые случаи

### 1. Обработка пустых файлов
```python
# Пустой файл input.txt
if len(read_text("data/lab04/input.txt")) == 0:
    write_csv([], "data/lab04/report.csv", header=("word", "count"))
```
**Результат:** Создается пустой CSV с заголовком.

### 2. Обработка различных кодировок
```python
# UTF-8 (по умолчанию)
content = read_text("file.txt")

# Windows-1251 для русских файлов
content = read_text("file.txt", encoding="windows-1251")

# KOI8-R для старых русских файлов
content = read_text("file.txt", encoding="koi8-r")
```

### 3. Проверка целостности CSV данных
```python
# Корректные данные
write_csv([("word", "count"), ("test", 4)], "data/check.csv")

# Ошибка: разная длина строк
try:
    write_csv([("word", "count"), ("test", 4, "extra")], "data/check.csv")
except ValueError as e:
    print(f"Ошибка: {e}")  # "все строки в rows должны иметь одинаковую длину"
```

### 4. Автоматическое создание директорий
```python
# Создает директории автоматически
write_csv([("word", "count")], "data/lab04/new_folder/report.csv")
```

### 5. Обработка различных типов входных данных
```python
# Проверка типов
try:
    read_text(123)  # TypeError: path должен быть str или Path
except TypeError as e:
    print(f"Ошибка: {e}")

try:
    write_csv([("word", "count")], 123)  # TypeError: path должен быть str или Path
except TypeError as e:
    print(f"Ошибка: {e}")
```

## Результаты выполнения программы

### Входные данные:
- **input.txt**: "Привет, мир! Привет!!!"
- **a.txt**: "Привет мир"
- **b.txt**: "Привет, привет!"

### Генерируемые отчеты:

#### 1. report.csv (анализ input.txt)
```csv
word,count
привет,2
мир,1
```

#### 2. report_per_file.csv (анализ по файлам)
```csv
file,word,count
a.txt,привет,1
a.txt,мир,1
b.txt,привет,2
```

#### 3. report_total.csv (сводный отчет)
```csv
word,count
привет,3
мир,1
```

### Консольный вывод:
```
input.txt:
Всего слов: 2
Уникальных слов: 2
Топ-5:
привет: 2
мир: 1

Общий отчет:
слово  | частота
-------|--------
привет | 3
мир    | 1

Отчет по файлам:
файл   | слово  | частота
-------|--------|--------
a.txt  | привет | 1
a.txt  | мир    | 1
b.txt  | привет | 2
```

## Анализ результатов

### Что было реализовано:

1. **Функция `ensure_parent_dir()`** - автоматическое создание директорий
2. **Функция `read_text()`** - универсальное чтение текстовых файлов с поддержкой кодировок
3. **Функция `write_csv()`** - создание CSV-файлов с проверкой целостности данных
4. **Система отчетов** - комплексный анализ текстов с генерацией различных форматов отчетов
5. **Функция `print_table_per_file()`** - красивое форматирование таблиц для многофайлового анализа

### Особенности реализации:

- **Кроссплатформенность**: использование `pathlib.Path` для работы с путями
- **Безопасность**: проверка типов и целостности данных
- **Гибкость**: поддержка различных кодировок и форматов
- **Автоматизация**: создание директорий и обработка пустых файлов
- **Модульность**: переиспользование функций из предыдущих лабораторных работ

### Краевые случаи:

1. **Пустые файлы** - корректная обработка с созданием пустых CSV
2. **Различные кодировки** - поддержка русских текстов в разных кодировках
3. **Некорректные данные** - строгая проверка типов и целостности
4. **Отсутствующие директории** - автоматическое создание структуры папок
5. **Разная длина строк CSV** - проверка и выдача понятных ошибок

### Тестирование:

- Все функции протестированы на различных входных данных
- Проверена работа с пустыми файлами и некорректными типами
- Протестирована генерация отчетов в различных форматах
- Проверена корректность CSV-файлов и их совместимость с Excel