import csv
from pathlib import Path
from lab08.models import Student


class Group:
    """
    Методы:
        __init__(storage_path) — инициализация группы и файла-хранилища
        _load() —
        _save() —
        list() — возвращает всех студентов в виде списка Student
        add(student) — добавляет нового студента в CSV
        find(substr) — возвращает список тех, у кого substr входит в fio
        remove(fio) — удаляет студента с таким ФИО
        update(fio, **fields) — обновляет данные студента
    """

    def __init__(self, storage_path: str | Path):
        """Инициализация группы"""
        self.storage_path = Path(storage_path)
        self.students = []
        self._load()

    def _load(self) -> None:
        """Логика чтения CSV файла и превращения строк в объекты Student"""
        if not self.storage_path.exists():
            return

        with open(self.storage_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.students.append(
                    Student(
                        fio=row["fio"],
                        birthdate=row["birthdate"],
                        group=row["group"],
                        gpa=float(row["gpa"]),
                    )
                )
            return

    def _save(self) -> None:
        """Логика сохранения списка self.students обратно в CSV файл"""
        with open(self.storage_path, "w", encoding="utf-8", newline="") as f:

            fieldnames = ["fio", "birthdate", "group", "gpa"]
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()

            for student in self.students:
                writer.writerow(
                    {
                        "fio": student.fio,
                        "birthdate": student.birthdate,
                        "group": student.group,
                        "gpa": student.gpa,
                    }
                )

    def add(self, student: Student) -> None:
        """Добавление студента в группу"""
        self.students.append(student)
        self._save()

    def list(self) -> list[Student]:
        """Возвращает список всех студентов в группе"""
        return self.students

    def find(self, substr: str) -> list[Student]:
        """Возвращает список тех, у кого substr входит в fio"""
        return [
            student
            for student in self.students
            if substr.lower() in student.fio.lower()
        ]

    def remove(self, fio: str) -> None:
        """Удаляет студента с таким ФИО"""
        self.students = [student for student in self.students if student.fio != fio]
        self._save()

    def update(self, fio: str, **fields) -> None:
        """Обновляет данные студента"""
        for student in self.students:
            if student.fio == fio:
                for field, value in fields.items():
                    if hasattr(student, field):
                        setattr(student, field, value)
                    else:
                        raise ValueError(f"Студент не имеет поля {field}")
                self._save()
                return

if __name__ == "__main__":
    group = Group("data/lab09/students.csv")

    # group.add(Student(fio="Васильев Василий Васильевич", birthdate="2005.01.01", group="BIVT-25", gpa=4.5))
    # group.add(Student(fio="Кузнецов Кузьма Кузьмич", birthdate="2006.02.02", group="BIVT-25", gpa=4.6))
    # group.add(Student(fio="Романов Роман Романович", birthdate="2007.03.03", group="BIVT-25", gpa=4.7))
    # print("\n".join([str(student) for student in group.list()]))

    # print(group.find("Романов"))

    # group.remove("Романов Роман Романович")
    # print("\n".join([str(student) for student in group.list()]))

    group.update("Васильев Василий Васильевич", gpa=4.7)
    print("\n".join([str(student) for student in group.list()]))