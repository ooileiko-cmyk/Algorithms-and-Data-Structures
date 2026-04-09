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

    # 1. sort() — пузырьковая сортировка по объекту
    def sort(self):
        n = len(self.students)

        for i in range(n):
            for j in range(0, n - i - 1):
                if self.students[j] > self.students[j + 1]:
                    self.students[j], self.students[j + 1] = self.students[j + 1], self.students[j]

    # 2. sort_by() — сортировка вставками по атрибуту
    def sort_by(self, key):
        for i in range(1, len(self.students)):
            current = self.students[i]
            j = i - 1

            while j >= 0 and key(self.students[j]) > key(current):
                self.students[j + 1] = self.students[j]
                j -= 1

            self.students[j + 1] = current

    def show(self):
        for s in self.students:
            print(s)


# тестовые данные
students = [
    Student("Ivan", "Petrov", 85),
    Student("Anna", "Ivanova", 90),
    Student("Oleg", "Sidorov", 75),
    Student("Maria", "Petrova", 95),
]

group = StudentList(students)

print("До сортировки:")
group.show()

print("\nПосле sort():")
group.sort()
group.show()

print("\nПосле sort_by(mark):")
group.sort_by(lambda x: x.mark)
group.show()