from pathlib import Path
import csv
from typing import Iterable, Sequence


def ensure_parent_dir(path: str | Path) -> None:
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


# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..','..'))

# txt = read_text("data/lab04/input.txt")  # должен вернуть строку
# write_csv([("word","count"),("test",4)], "data/check.csv")  # создаст CSV