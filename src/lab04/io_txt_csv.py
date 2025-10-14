from pathlib import Path
import csv
from typing import Iterable, Sequence


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
    with p.open("r", encoding=encoding) as f:
        return f.read()

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
    p.parent.mkdir(parents=True, exist_ok=True)

    rows_list = list(rows)

    # Проверка одинаковой длины строк
    row_length: int | None = None
    if rows_list:
        row_length = len(rows_list[0])
        for row in rows_list:
            if len(row) != row_length:
                raise ValueError("все строки в rows должны иметь одинаковую длину")
    if header is not None and rows_list and len(header) != row_length:
        raise ValueError("длина header должна совпадать с длиной строк в rows")

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")
        if header is not None:
            writer.writerow(header)
        for row in rows_list:
            writer.writerow(row)

# from src.io_txt_csv import read_text, write_csv
# txt = read_text("data/input.txt")
# write_csv([("word","count"),("test",3)], "data/check.csv")