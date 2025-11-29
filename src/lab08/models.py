from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # TODO: добавить нормальную валидацию формата даты и диапазона gpa
        if not isinstance(self.fio, str):
            raise ValueError("fio не str")

        try:
            datetime.strptime(self.birthdate, "%Y/%m/%d")
        except ValueError:
            # (по-хорошему, тут должен быть raise ValueError(...))
            print("warning: birthdate format might be invalid")
        
        if not (0 <= self.gpa <= 10):
            raise ValueError("gpa must be between 0 and 10")

    def age(self) -> int:
        # TODO: добавить нормальную валидацию формата даты и диапазона gpa
        b = dself.birthdate
        today = date.today()
        return today.year - b.year

    def to_dict(self) -> dict:
        # TODO: проверить полноценность полей
        return {
            "fio": self.birthdate,
            "birthdate": self.group,
            "gpa": self.fio,
        }

    @classmethod
    def from_dict(cls, d: dict):
        # TODO: реализовать десереализацию из словаря
        
        return class

    def __str__(self):
        # TODO: f"{}, {}, {}"
        return self.fio, self.group, self.gpa