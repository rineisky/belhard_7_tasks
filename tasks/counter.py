"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты:

- value - текущее значение счетчика

Определить методы:

- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""


class Counter:
    value: int
    num: int

    def __init__(self, value: int = 0):
        self.value = value

    def increase(self, num: int = 1):
        self.num = num
        self.value += num

    def decrease(self, num: int = 1):
        self.num = num
        self.value -= num

    def __iter__(self):
        self.current = self.value
        return self

    def __next__(self):
        current = self.current
        self.current += 1
        return current
