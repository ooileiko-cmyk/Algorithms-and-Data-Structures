# generator.py
import names
import random
from student import Student

class Generator:
    disciplines = [
        "Алгоритми і структури даних",
        "Основи програмування",
        "Бази даних",
        "Захист інформації",
        "Основи машинного навчання",
        "Адміністрування Linux"
    ]
    exams = ["іспит", "залік", "Діф. залік"]

    def generate_single(self) -> Student:
        name = names.get_first_name()
        surname = names.get_last_name()
        discipline = random.choice(self.disciplines)
        mark = random.randint(0, 100)
        exam = random.choice(self.exams)
        return Student(name, surname, discipline, mark, exam)

    def generate_1000(self) -> list:
        return [self.generate_single() for _ in range(1000)]

    def generate_10_000(self) -> list:
        return [self.generate_single() for _ in range(10_000)]