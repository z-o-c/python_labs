from dataclasses import dataclass
from datetime import datetime, date


@dataclass  #  декоратор для автоматической генерации методов __init__, __repr__, __eq__, (order=False, frozen=False, slots=False, unsafe_hash=False)
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self) -> None:
        """
        Валидация данных студента.
        Args:
            fio: ФИО студента
            birthdate: Дата рождения студента
            group: Группа студента
            gpa: GPA студента
        Raises:
            ValueError: Если данные студента некорректны
        """
        if not isinstance(self.fio, str):
            raise ValueError("fio не str")

        if len(self.fio) == 0:
            raise ValueError("fio не может быть пустым")

        if not isinstance(self.group, str):
            raise ValueError("group не str")

        if len(self.group) == 0:
            raise ValueError("group не может быть пустым")

        if not isinstance(self.gpa, float):
            raise ValueError("gpa не float")

        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa должен быть между 0 и 5")

        if not isinstance(self.birthdate, str):
            raise ValueError("birthdate должен быть строкой")

        try:
            datetime.strptime(
                self.birthdate, "%Y.%m.%d"
            )  #  преобразует строку в объект datetime формата YYYY.MM.DD
        except ValueError:
            raise ValueError(
                f"birthdate должен быть в формате YYYY.MM.DD, получено: {self.birthdate}"
            )

    def age(self) -> int:
        """
        Вычисляет возраст студента.
        Returns:
            Возраст студента
        """
        birth_date = datetime.strptime(
            self.birthdate, "%Y.%m.%d"
        ).date()  # преобразует строку в объект date формата YYYY.MM.DD
        today = date.today()  # получает текущую дату

        # вычисление возраста студента, учитывая прошел ли день рождения в этом году
        return (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )  # сравнение кортежей лексикографически по элементам (месяц, день), возвращает True(1) или False(0)

    def to_dict(self) -> dict:
        """
        Сериализует объект Student в словарь.
        Returns:
            Словарь с данными студента
        """
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        """
        Десериализует словарь в объект Student.
        Args:
            data: Словарь с данными студента
        Returns:
            Объект Student
        """
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"],
        )

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Student.
        Returns:
            Строковое представление объекта Student
        """
        return f"Студент: {self.fio}, Группа: {self.group}, GPA: {self.gpa}, Возраст: {self.age()}"


if __name__ == "__main__":
    try:
        student = Student(
            fio="Иванов Иван Иванович", birthdate="2005.01.01", group="BIVT-25", gpa=4.5
        )
        print(student)
        print(f"Словарь: {student.to_dict()}")
    except ValueError as e:
        print(f"Ошибка: {e}")
