def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализует текст путем удаления специальных символов и приведения к единому формату.
    
    Функция выполняет следующие преобразования:
    - Удаляет символы табуляции (\t) и переноса строки (\n)
    - Убирает лишние пробелы (в начале, конце и множественные внутри строки)
    - При необходимости приводит текст к нижнему регистру с использованием casefold()
    - Заменяет букву 'ё' на 'е' (опционально)

    Examples:
        normalize("ПрИвЕт\nМИр\t") == "привет мир"
        normalize("ёжик, Ёлка") == "ежик, елка"
    """

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

def tokenize(text: str) -> list[str]:
    """
    Функция разделяет входную строку на части, используя в качестве разделителей
    любые символы, которые не являются буквами или цифрами.

    Examples:
        tokenize("привет, мир!") == ["привет", "мир"]
        tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
        tokenize("2025 год") == ["2025", "год"]
    """
    import re

    if not isinstance(text, str):
        raise ValueError("tokenize: text не str")
    
    if len(text) == 0:
        raise ValueError("tokenize: пустой text")
    
    split_result = re.split(r"[^\w-]+", text)
    
    return [item for item in split_result if len(item) >= 1]
    

def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Подсчитывает частоту встречаемости слов в списке токенов.

    Examples:
        count_freq(["a","b","a","c","b","a"]) == {"a":3, "b":2, "c":1}
        count_freq(["bb","aa","bb","aa","cc"]) == {"aa":2, "bb":2, "cc":1}
    """
    from collections import Counter

    if not isinstance(tokens, list):
        raise ValueError("tokenize: text не str")
    
    if len(tokens) == 0:
        raise ValueError("count_freq: пустой tokens")

    return dict(sorted(Counter(tokens).items(), key=lambda item: (-item[1], item[0])))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Возвращает топ-N самых частых слов с сортировкой по убыванию частоты.

    Examples:
        top_n({"a":3, "b":2, "c":1}, 2) == [("a",3), ("b",2)]
        top_n({"aa":2, "bb":2, "cc":1}, 2) == [("aa",2), ("bb",2)]
    """

    if not isinstance(freq, dict):
        raise ValueError("top_n: freq не  dict")
    
    if len(freq) == 0:
        raise ValueError("top_n: пустой freq")
    
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]

def print_table(words_data: list[tuple[str, int]]) -> None:
    """
    Выводит форматированную таблицу слов и их частот в отсортированном виде.
    
    Функция принимает список кортежей (слово, частота) и выводит их в виде
    читаемой таблицы с выравниванием колонок. Ширина первой колонки автоматически
    подстраивается под самое длинное слово в данных или заголовке.
    """
    if not words_data:
        raise ValueError("print_table: words_data пуст")
    
    max_word_length = max(len(word) for word, count in words_data)

    if len("слово") > max_word_length:
        max_word_length = len("слово")
    
    print(f"{'слово':<{max_word_length}} | частота")
    print("-" * max_word_length + "-|-" + "-" * 7)
    
    for word, count in words_data:
        print(f"{word:<{max_word_length}} | {count}")

def print_table_per_file(words_data: dict[str, list[tuple[str, int]]]) -> None:
    """
    Выводит форматированную таблицу слов и их частот в отсортированном виде для каждого файла.
    
    Функция принимает список кортежей (слово, частота) и выводит их в виде
    читаемой таблицы с выравниванием колонок. Ширина первой колонки автоматически
    подстраивается под самое длинное слово в данных или заголовке для каждого файла.
    """
    if not words_data:
        raise ValueError("print_table_per_file: words_data пуст")
    
    max_word_length = max(len(word) for file, words in words_data.items() for word, count in words)

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

from pathlib import Path
from typing import Union

def ensure_parent_dir(path: Union[str, Path]) -> None:
    """
    Создать родительские директории для указанного пути, если они не существуют.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

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

    Examples:
        content = read_text("file.txt")  # UTF-8 по умолчанию
        content = read_text("file.txt", encoding="windows-1251")
        content = read_text("file.txt", encoding="cp1251")
    """

    if not isinstance(path, (str, Path)):
        raise TypeError("path должен быть str или Path")
    if not isinstance(encoding, str) or not encoding:
        raise TypeError("encoding должен быть непустой строкой")

    p = Path(path)

    with p.open("r", encoding=encoding) as file:
        return file.read()


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV файл в формат XLSX (Excel).
    
    Функция читает CSV файл и создает новый XLSX файл с теми же данными.
    Первая строка CSV интерпретируется как заголовок таблицы.
    
    Особенности:
    - Использует библиотеку openpyxl для создания Excel файлов
    - Создает лист с названием "Sheet1"
    - Автоматически подбирает ширину колонок по содержимому (минимум 8 символов)
    - Поддерживает UTF-8 кодировку
    - Создает родительские директории для выходного файла при необходимости
    
    Raises:
        FileNotFoundError: Если исходный CSV файл не найден
        IsADirectoryError: Если csv_path указывает на директорию
        TypeError: Если аргументы не являются строками
        ValueError: Если пути пустые или имеют неправильные расширения
    """
    import openpyxl
    import csv

    path_csv = Path(csv_path)
    path_xlsx = Path(xlsx_path)

    if not path_csv.exists():
        raise FileNotFoundError(f"Файл не найден: {path_csv}")
    if not path_csv.is_file():
        raise IsADirectoryError(f"Это директория, а не файл: {path_csv}")
    if not isinstance(csv_path, str):
        raise TypeError("csv_path должен быть строкой")
    if not isinstance(xlsx_path, str):
        raise TypeError("xlsx_path должен быть строкой")
    if not csv_path:
        raise ValueError("csv_path пустой")
    if not xlsx_path:
        raise ValueError("xlsx_path пустой")

    if not csv_path.endswith('.csv'):
        raise ValueError("csv_path должен указывать на .csv файл")
    if not xlsx_path.endswith('.xlsx'):
        raise ValueError("xlsx_path должен указывать на .xlsx файл")

    # Создание родительских директорий для выходного файла
    ensure_parent_dir(path_xlsx)
    
    with path_csv.open("r", newline="", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Sheet1"

        for row in csv_reader:
            sheet.append(row)

    # Расчет и установка автоширины колонок
    for col_idx, column in enumerate(sheet.columns, 1):
        max_length = 8  # минимальная ширина
        column_letter = openpyxl.utils.get_column_letter(col_idx)
        
        for cell in column:
            try:
                if cell.value and len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except (TypeError, ValueError): # если значение не строковое или нет значения
                pass

        sheet.column_dimensions[column_letter].width = max_length + 2
        
    workbook.save(path_xlsx)


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON файл в формат CSV.
    
    Функция читает JSON файл, содержащий список словарей (объектов),
    и создает CSV файл с соответствующими колонками и строками.
    
    Особенности:
    - Поддерживает только JSON структуру: список словарей [{"key": "value"}, ...]
    - Автоматически определяет все поля из всех объектов
    - Заполняет отсутствующие поля пустыми строками
    - Порядок колонок определяется полями первого объекта
    - Использует UTF-8 кодировку
    - Создает родительские директории для выходного файла при необходимости
    
    Raises:
        FileNotFoundError: Если исходный JSON файл не найден
        IsADirectoryError: Если json_path указывает на директорию
        TypeError: Если аргументы не являются строками
        ValueError: Если пути пустые, имеют неправильные расширения,
                   JSON пустой, не является списком или содержит не-словари
    """
    import csv
    import json

    path_json = Path(json_path)
    path_csv = Path(csv_path)

    if not path_json.exists():
        raise FileNotFoundError(f"Файл не найден: {path_json}")
    if not path_json.is_file():
        raise IsADirectoryError(f"Это директория, а не файл: {path_json}")
    if not isinstance(json_path, str):
        raise TypeError("json_path должен быть строкой")
    if not isinstance(csv_path, str):
        raise TypeError("csv_path должен быть строкой")
    if not json_path:
        raise ValueError("json_path пустой")
    if not csv_path:
        raise ValueError("csv_path пустой")
    
    if not json_path.endswith('.json'):
        raise ValueError("json_path должен указывать на .json файл")
    if not csv_path.endswith('.csv'):
        raise ValueError("csv_path должен указывать на .csv файл")
        
    # Создание родительских директорий для выходного файла
    ensure_parent_dir(path_csv)

    data = []
    with path_json.open("r", encoding="utf-8") as file:
        data = json.load(file)
    
    # Проверка: пустой JSON или неподдерживаемая структура
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    # Проверка: список с не-словарями
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Элемент {i} не является словарем")
    
    # Собираем все поля, начиная с полей первого объекта
    all_fields = list(data[0].keys())  # начинаем с полей первого объекта
    for item in data[1:]:  # добавляем поля из остальных объектов
        for field in item.keys():
            if field not in all_fields:
                all_fields.append(field)
        
    with path_csv.open("w", newline="", encoding="utf-8") as file:
        csv_writer = csv.DictWriter(file, fieldnames=all_fields, delimiter=",")
        csv_writer.writeheader()
        for row in data:
            # Заполняем отсутствующие поля пустыми строками
            complete_row = {field: row.get(field, "") for field in all_fields}
            csv_writer.writerow(complete_row)

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV файл в формат JSON (список словарей).
    
    Функция читает CSV файл с заголовками и создает JSON файл,
    где каждая строка CSV становится отдельным словарем.
    
    Особенности:
    - Требует наличия заголовков в первой строке CSV
    - Автоматически определяет наличие заголовков через csv.Sniffer
    - Все значения сохраняются как строки (без преобразования типов)
    - Использует UTF-8 кодировку
    - Создает родительские директории для выходного файла при необходимости
    - Результирующий JSON форматируется с отступами для читаемости
     
    Raises:
        FileNotFoundError: Если исходный CSV файл не найден
        IsADirectoryError: Если csv_path указывает на директорию
        TypeError: Если аргументы не являются строками
        ValueError: Если пути пустые, имеют неправильные расширения,
                   CSV файл пустой или не содержит заголовков
    """
    import csv
    import json
    
    path_csv = Path(csv_path)
    path_json = Path(json_path)

    if not path_csv.exists():
        raise FileNotFoundError(f"Файл не найден: {path_csv}")
    if not path_csv.is_file():
        raise IsADirectoryError(f"Это директория, а не файл: {path_csv}")
    if not csv_path:
        raise ValueError("csv_path пустой")
    if not json_path:
        raise ValueError("json_path пустой")
    if not isinstance(csv_path, str):
        raise TypeError("csv_path должен быть строкой")
    if not isinstance(json_path, str):
        raise TypeError("json_path должен быть строкой")

    if not csv_path.endswith('.csv'):
        raise ValueError("csv_path должен указывать на .csv файл")
    if not json_path.endswith('.json'):
        raise ValueError("json_path должен указывать на .json файл")

    # Создание родительских директорий для выходного файла
    ensure_parent_dir(path_json)

    data = []
    with path_csv.open("r", newline="", encoding="utf-8") as file:
        # Используем csv.Sniffer для определения наличия заголовков
        sample = file.read(1024)  # Читаем первые 1024 символа для анализа
        if not sample.strip():
            raise ValueError("CSV файл пустой")
        
        file.seek(0)  # Возвращаемся к началу файла
        
        # Проверяем наличие заголовков через Sniffer
        sniffer = csv.Sniffer()
        try:
            has_header = sniffer.has_header(sample)
        except csv.Error:
            # Если Sniffer не может определить, считаем что заголовок есть
            has_header = True
        
        if not has_header:
            raise ValueError("CSV файл, вероятно, не содержит заголовок (эвритический подход)")
        
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            data.append(row)
    
    with path_json.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)