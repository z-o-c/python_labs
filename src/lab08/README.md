# Лабораторная работа 8: ООП в Python: `@dataclass Student`, методы и сериализация

## Реализованные компоненты

### 1. Модель `Student` ([models](src/lab08/models.py))

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

 ![models](/images/lab08/img03.png)

### 2. Функции сериализации ([serialize](src/lab08/serialize.py))

#### `students_to_json(students: list[Student], path: str | Path) -> None`

Сериализует список студентов в JSON файл.

**Параметры:**
- `students` — список объектов `Student`
- `path` — путь к выходному JSON файлу


#### `students_from_json(path: str | Path) -> list[Student]`

Десериализует список студентов из JSON файла.

**Параметры:**
- `path` — путь к JSON файлу

**Возвращает:**
- Список объектов `Student`

 ![models](/images/lab08/img02.png)

`students_input.json`

 ![models](/images/lab08/img01.png)

 `students_output.json` Сортировка по GPA (по убыванию)
 
 ![models](/images/lab08/img04.png)