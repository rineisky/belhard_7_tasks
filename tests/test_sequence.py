import pytest

from tasks.sequence import RandSequence


def test_creation():
    assert hasattr(RandSequence, "print_seq")
    assert hasattr(RandSequence, "generate")

    sequence = RandSequence(5)

    assert hasattr(sequence, "n")
    assert sequence.n == 5
    assert hasattr(sequence, "sequence")
    assert isinstance(sequence.sequence, list)
    assert len(sequence.sequence) == 5


@pytest.mark.parametrize(
    "n", (
        5, 10, 7, 4
    )
)
def test_generate_sequence(n):
    sequence = RandSequence(n)
    assert all(-n <= i <= n for i in sequence.sequence)

    sequence.generate(2 * n)
    assert all(-(2 * n) <= i <= 2 * n for i in sequence.sequence)

    sequence.generate()
    assert all(-n <= i <= n for i in sequence.sequence)
