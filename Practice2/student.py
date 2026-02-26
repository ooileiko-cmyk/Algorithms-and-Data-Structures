# student.py
class Student:
    name: str
    surname: str
    discipline: str
    mark: int
    exam: str

    def init(self, name: str, surname: str, discipline: str, mark: int, exam: str = "іспит") -> None:
        self.name = name
        self.surname = surname
        self.discipline = discipline
        self.mark = mark
        self.exam = exam

    def get_info(self) -> str:
        """Метод для вывода краткой информации о студенте"""
        return f"Student({self.name}, {self.surname}, {self.discipline}, {self.exam}, {self.mark})"

    def repr(self):
        return f"Student({self.name}, {self.surname}, {self.discipline}, {self.exam}, {self.mark})"