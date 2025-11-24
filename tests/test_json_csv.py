import json, csv
from pathlib import Path

import pytest

from src.lib.text import json_to_csv, csv_to_json


def write_json(path: Path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def read_csv_rows(path: Path):
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
    write_json(src, data)

    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst)
    assert len(rows) == 2
    assert set(rows[0]) >= {"name", "age"}


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("name,age\nAlice,22\nBob,25\n", encoding="utf-8")

    csv_to_json(str(src), str(dst))
    obj = json.loads(dst.read_text(encoding="utf-8"))
    assert isinstance(obj, list) and len(obj) == 2
    assert set(obj[0]) == {"name", "age"}


def test_json_to_csv_empty_raises(tmp_path: Path):
    src = tmp_path / "empty.json"
    src.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_csv_to_json_no_header_raises(tmp_path: Path):
    src = tmp_path / "bad.csv"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.json"))


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json")


def test_json_to_csv_missing_input(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        json_to_csv(str(tmp_path / "missing.json"), str(tmp_path / "out.csv"))


def test_json_to_csv_directory_input(tmp_path: Path):
    directory = tmp_path / "dir_input"
    directory.mkdir()
    with pytest.raises(IsADirectoryError):
        json_to_csv(str(directory), str(tmp_path / "out.csv")) # директория вместо json файла


def test_json_to_csv_type_checks(tmp_path: Path):
    src = tmp_path / "data.json"
    src.write_text('[{"name": "Ann"}]', encoding="utf-8")
    dst = tmp_path / "out.csv"
    dst.parent.mkdir(exist_ok=True)

    with pytest.raises(TypeError):
        json_to_csv(src, str(dst))  # передали Path вместо str

    with pytest.raises(TypeError):
        json_to_csv(str(src), dst)  # передали Path вместо str


# проверка на .json и .csv файлы
def test_json_to_csv_wrong_extensions(tmp_path: Path):
    src = tmp_path / "data.json"
    txt_src = tmp_path / "data.txt"
    src.write_text('[{"name": "Ann"}]', encoding="utf-8")
    txt_src.write_text("{}", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(txt_src), str(tmp_path / "out.csv")) # не json файл

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.txt")) # не csv файл


def test_json_to_csv_structure_checks(tmp_path: Path):
    src = tmp_path / "bad.json"
    dst = tmp_path / "out.csv"

    src.write_text('{"name": "Ann"}', encoding="utf-8")
    with pytest.raises(ValueError, match="список"):
        json_to_csv(str(src), str(dst)) # не список объектов

    src.write_text('["not a dict"]', encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst)) # не словарь


def test_json_to_csv_adds_missing_fields(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "city": "NY"},
    ]
    write_json(src, data)

    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst)
    assert set(rows[0]) == {"name", "age", "city"} # проверка на наличие всех полей
    assert rows[1]["age"] == "" # проверка на наличие пустых полей
    assert rows[1]["city"] == "NY" # проверка на наличие значений


def test_csv_to_json_directory_input(tmp_path: Path):
    directory = tmp_path / "dir_input"
    directory.mkdir()
    with pytest.raises(IsADirectoryError):
        csv_to_json(str(directory), str(tmp_path / "out.json")) # директория вместо csv файла


def test_csv_to_json_type_checks(tmp_path: Path):
    src = tmp_path / "data.csv"
    src.write_text("name\nAnn\n", encoding="utf-8")
    dst = tmp_path / "out.json"

    with pytest.raises(TypeError):
        csv_to_json(src, str(dst))  # передали Path вместо str

    with pytest.raises(TypeError):
        csv_to_json(str(src), dst)  # передали Path вместо str


# проверка на .csv и .json файлы
def test_csv_to_json_wrong_extensions(tmp_path: Path):
    src = tmp_path / "data.csv"
    src.write_text("name\nAnn\n", encoding="utf-8")
    txt_src = tmp_path / "data.txt"
    txt_src.write_text("name\nAnn\n", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(txt_src), str(tmp_path / "out.json")) # не csv файл

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.txt")) # не json файл


def test_csv_to_json_empty_raises(tmp_path: Path):
    src = tmp_path / "bad.csv"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.json"))
