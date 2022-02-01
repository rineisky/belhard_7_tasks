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

    def __init__(cls, value: int = 0):
        cls.value = value

    def increase(cls, num: int = 1) -> int:
        cls.value += num

    def decrease(cls, num: int = 1) -> int:
        cls.value -= num

    def __iter__(cls):
        return cls

    def __next__(cls):
        value = cls.value
        cls.value += 1
        return value
