class Student:
    def init(self, name, surname, mark):
        self.name = name
        self.surname = surname
        self.mark = mark

    def repr(self):
        return f"{self.surname} {self.name} - {self.mark}"

    # сравнение объектов (для sort)
    def lt(self, other):
        return self.surname < other.surname


class StudentList:
    def init(self, students):
        self.students = students