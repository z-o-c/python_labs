from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    path_json = Path(json_path)
    path_csv = Path(csv_path)
    if not json_path.endswith('.json'):
        raise ValueError("json_path должен указывать на .json файл")
    if not csv_path.endswith('.csv'):
        raise ValueError("csv_path должен указывать на .csv файл")
    if not json_path:
        raise ValueError("json_path пустой")
    if not csv_path:
        raise ValueError("csv_path пустой")
    if not path_json.exists():
        raise FileNotFoundError(f"Файл не найден: {path_json}")
    if not path_json.is_file():
        raise IsADirectoryError(f"Это директория, а не файл: {path_json}")
    if not path_json.exists():
        raise FileNotFoundError(f"Файл не найден: {path_json}")
    if not path_json.is_file():
        raise IsADirectoryError(f"Это директория, а не файл: {path_json}")
    if not isinstance(json_path, str):
        raise TypeError("json_path должен быть строкой")
    if not isinstance(csv_path, str):
        raise TypeError("csv_path должен быть строкой")



def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """