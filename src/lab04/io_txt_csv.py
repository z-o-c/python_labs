from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает текст из файла и возвращает его как строку.
    она пока ещё не доделана
    """

    p = Path(path)

    if not isinstance(path, (str, Path)):
        raise ValueError("path должен быть str или Path")
    
    if not isinstance(encoding, str):
        raise ValueError("encoding должен быть str")
    
    
    if len(encoding) == 0:
        raise ValueError("encoding пустой")
    
    if len(path) == 0:
        raise ValueError("path пустой")
    
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    try:
        with open(path, 'r', encoding=encoding) as file:
            return file.read()

    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{path}' не найден")

    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(
            f"Ошибка декодирования файла '{path}'. "
            f"Попробуйте другую кодировку. Ошибка: {e}"
        )

import csv
from pathlib import Path
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """
    Записывает данные в CSV файл.
    она пока ещё не доделана
    """
    if not isinstance(rows, Iterable):
        raise ValueError("rows должен быть Iterable")
    
    if not isinstance(path, (str, Path)):
        raise ValueError("path должен быть str или Path")
    
    if len(path) == 0:
        raise ValueError("path пустой")
    
    if len(rows) == 0:
        raise ValueError("rows пустой")

    p = Path(path)
    rows = list(rows)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)

        if header is not None:
            w.writerow(header)
            
        for r in rows:
            w.writerow(r)