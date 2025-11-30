# Лабораторная работа 8: ООП в Python: `@dataclass Student`, методы и сериализация

## Реализованные компоненты

### 1. Модель `Student` (`models.py`)

Класс данных для представления студента с использованием `@dataclass`.

**Поля:**
- `fio: str` — ФИО студента
- `birthdate: str` — дата рождения в формате `YYYY.MM.DD`
- `group: str` — группа студента
- `gpa: float` — средний балл (0-5)

**Методы:**
- `__post_init__()` — валидация данных при создании объекта
- `age() -> int` — вычисление возраста студента (учитывает, прошел ли день рождения)
- `to_dict() -> dict` — сериализация в словарь
- `from_dict(data: dict) -> Student` — десериализация из словаря
- `__str__() -> str` — строковое представление объекта

**Валидация:**
- Проверка типов всех полей
- Проверка на пустые строки для `fio` и `group`
- Проверка диапазона `gpa` (0-5)
- Проверка формата даты `birthdate` (YYYY.MM.DD)

**Пример использования:**
```python
student = Student(
    fio="Иванов Иван Иванович",
    birthdate="2005.01.01",
    group="BIVT-25",
    gpa=4.5
)

print(student)  # Студент: Иванов Иван Иванович, Группа: BIVT-25, GPA: 4.5, Возраст: 19
print(student.age())  # 19
print(student.to_dict())  # {'fio': '...', 'birthdate': '...', ...}
```

### 2. Функции сериализации (`serialize.py`)

#### `students_to_json(students: list[Student], path: str | Path) -> None`

Сериализует список студентов в JSON файл.

**Параметры:**
- `students` — список объектов `Student`
- `path` — путь к выходному JSON файлу

**Пример:**
```python
students = [
    Student(fio="Иванов Иван", birthdate="2005.01.01", group="BIVT-25", gpa=4.5),
    Student(fio="Петров Пётр", birthdate="2006.02.02", group="BIVT-25", gpa=4.6),
]

students_to_json(students, "data/lab08/students.json")
```

#### `students_from_json(path: str | Path) -> list[Student]`

Десериализует список студентов из JSON файла.

**Параметры:**
- `path` — путь к JSON файлу

**Возвращает:**
- Список объектов `Student`

**Пример:**
```python
students = students_from_json("data/lab08/students.json")
for student in students:
    print(student)
```

