from collections.abc import Iterator

from tasks.counter import Counter


def test_creation():
    counter = Counter()
    assert counter.value == 0

    counter = Counter(10)
    assert counter.value == 10

    assert hasattr(counter, "increase")
    assert hasattr(counter, "decrease")

    assert issubclass(Counter, Iterator)


def test_increase():
    counter = Counter()

    assert counter.value == 0
    counter.increase()
    assert counter.value == 1
    counter.increase(10)
    assert counter.value == 11


def test_decrease():
    counter = Counter(10)

    assert counter.value == 10
    counter.decrease()
    assert counter.value == 9
    counter.decrease(5)
    assert counter.value == 4


def test_iteration():
    counter = Counter()

    assert counter.value == 0
    iterator = iter(counter)
    assert iterator is counter
    assert next(iterator) == 0
    assert next(iterator) == 1
    assert next(iterator) == 2
