import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import ensure_parent_dir
from pathlib import Path
import csv
import openpyxl

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

try:
    csv_to_xlsx("data/lab05/samples/cities.csv", "data/lab05/out/cities_from_csv.xlsx")
except Exception as e:
    print(f"Ошибка: {e}")