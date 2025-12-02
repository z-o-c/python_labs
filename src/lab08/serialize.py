import json
from pathlib import Path
from .models import Student


def students_to_json(students: list[Student], path: str | Path) -> None:
    """
    Сериализует список студентов в JSON файл.

    Args:
        students: Список объектов Student
        path: Путь к выходному JSON файлу (str или Path)

    Raises:
        ValueError: Если path пустой или не заканчивается на .json, если students не является списком
        FileNotFoundError: Если родительская директория не существует и не может быть создана
    """
    if not isinstance(students, list):
        raise ValueError("students должен быть списком")

    if not isinstance(path, (str, Path)):
        raise ValueError("path должен быть строкой или Path")

    path = Path(path)  # преобразует строку в Path

    if not str(path):
        raise ValueError("path пустой")

    if not str(path).endswith(".json"):
        raise ValueError("path должен указывать на .json файл")

    # Создание родительских директорий
    path.parent.mkdir(parents=True, exist_ok=True)

    data = [
        s.to_dict() for s in students
    ]  # преобразует список объектов Student в список словарей

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> list[Student]:
    """
    Десериализует список студентов из JSON файла.

    Args:
        path: Путь к JSON файлу (str или Path)

    Returns:
        Список объектов Student

    Raises:
        FileNotFoundError: Если файл не найден
        ValueError: Если path пустой, не заканчивается на .json или JSON имеет неправильную структуру, если path не является строкой или Path
    """
    if not isinstance(path, (str, Path)):
        raise ValueError("path должен быть строкой или Path")

    path = Path(path)  # преобразует строку в Path

    if not str(path):
        raise ValueError("path пустой")

    if not str(path).endswith(".json"):
        raise ValueError("path должен указывать на .json файл")

    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    if not path.is_file():
        raise ValueError(f"Это директория, а не файл: {path}")

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)  # десериализует JSON файл в список словарей

    # проверка, на случай если file(73 строка) не является списком словарей
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")

    students = []  # список объектов Student
    for i, item in enumerate(data):  # перебирает список словарей
        if not isinstance(item, dict):
            raise ValueError(f"Элемент {i} не является словарем")

        try:
            student = Student.from_dict(item)  # десериализует словарь в объект Student
            students.append(student)  # добавляет объект Student в список
        except (KeyError, ValueError) as e:
            raise ValueError(f"Ошибка при создании Student: {e}") from e

    return students  # возвращает список объектов Student


if __name__ == "__main__":
    # Десериализация из входного файла
    students = students_from_json("data/lab08/students_input.json")
    print("Загружено студентов:", len(students))
    for student in students:
        print(student)

    # Сортировка: отсортировать по GPA (по убыванию)
    students = sorted(students, key=lambda s: s.gpa, reverse=True)

    # Сериализация в выходной файл
    output = "data/lab08/students_output.json"
    students_to_json(students, output)
    print(f"\nСтуденты сохранены в {output}")
