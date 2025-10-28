import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import ensure_parent_dir
from pathlib import Path
import json
import csv

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
    all_fields = list(data[0].keys())  # берем ключи первого объекта как стартовый набор полей
    
    for item in data[1:]:  # проходим остальные объекты и добавляем недостающие поля в all_fields
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
        
        file.seek(0)  # Возвращаемся к началу файла полсе file.read(1024)
        
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

try:
    json_to_csv("data/lab05/samples/empty_json.json", "data/lab05/out/empty_from_json.csv")
    csv_to_json("data/lab05/samples/no_header_csv.csv", "data/lab05/out/no_header_from_csv.json")
    json_to_csv("data/lab05/samples/test_missing_fields.json", "data/lab05/out/missing_fields_from_json.csv")
    json_to_csv("data/lab05/samples/people.json", "data/lab05/out/people_from_json.csv")
    csv_to_json("data/lab05/samples/people.csv", "data/lab05/out/people_from_csv.json")
except Exception as e:
    print(f"Ошибка: {e}")