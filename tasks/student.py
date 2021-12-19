"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: float

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __gt__(self, other):
        return self.average_score > other.average_score

    def __le__(self, other):
        return self.average_score <= other.average_score

    def __ge__(self, other):
        return self.average_score >= other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __ne__(self, other):
        return self.average_score != other.average_score

    def __repr__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Группа: {self.group}," f" Средний балл: {self.average_score}."


some_list = [Student("2", "4", "3", 9.99), Student("2", "3", "2", 8.88), Student("3", "5", "5", 4.44),
             Student("4", "4", "4", 3.33), Student("5", "5", "5", 2.22)]

print(sorted(some_list))
print(sorted(some_list, reverse=True))
new_list = [student for student in some_list if student.average_score > 5]
print(new_list)
