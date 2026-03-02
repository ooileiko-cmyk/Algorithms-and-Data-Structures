# run_generator.py
from generator import Generator

gen = Generator()

# Генеруємо одного студента
student = gen.generate_single()

print(student)         # вызов repr
print(student.get_info())  # вызов get_info