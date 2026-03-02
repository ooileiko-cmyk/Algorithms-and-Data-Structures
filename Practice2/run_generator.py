# run_generator.py
from generator import Generator

gen = Generator()
student = gen.generate_single()
print(student)
print(student.get_info())

students_1000 = gen.generate_1000()
print(len(students_1000))