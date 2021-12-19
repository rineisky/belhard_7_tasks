"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- n - длина последовательности
- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n и генерирует
    случайную последовательность длиной n в атрибут sequence
- метод generate, который принимает длину последовательности n (если n не передано,
    то сгенерировать длиной self.n) и генерирует последовательность в атрибут sequence.
    Для получения некоторого рандомного числа - воспользоваться функцией
    random.randint(-n, n)
- метод print_seq, который выводит последовательность на экран
"""
from random import randint


class RandSequence:
    n: int
    sequence = []

    def __init__(self, n):
        self.n = n
        self.sequence = self.generate()

    def generate(self, n=0):
        some_list = []
        if n == 0:
            n = self.n
        for i in range(n):
            some_list.append(randint(-n, n))
        self.sequence = some_list
        return self.sequence

    def print_seq(self):
        print(self.sequence)
