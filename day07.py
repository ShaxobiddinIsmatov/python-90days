# Лекция 2. Циклы. List. Len.

# Ниже код который указывает количество учеников. Сделан через Len
# который # определяет количество элементов в списке.
# А так же цикл for котрый указывает номер ученика и его номер

pupil = ['Ivan', 'Petr', 'Sidor', 'Vasya']
print(f'В классе {len(pupil)} учеников')

for i in range(len(pupil)):
    print(f'{i + 1}-ученик: {pupil[i]}')

# Ниже код который имеет словарь с именами учеников и их полом.
# И выводит пол ученика по его имени. Таблица
students = {
    'Ivan' : 'male',
    'Anna' : 'female',
}

print(students['Ivan'])

# Ниже код таблица с тремя данными. Имя, пол и возраст. 
# И выводит пол ученика по его имени. Таблица

students2 = [
    {'name': 'Ivan', 'gender': 'male', 'age': 20},
    {'name': 'Anna', 'gender': 'female', 'age': 19},
]

for student in students2:
    print(student['name'], student['gender'], student['age'])