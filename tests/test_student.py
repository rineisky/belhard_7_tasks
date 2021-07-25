from tasks.student import Student


def test_creation():
    student = Student("surname", "name", 1, 3)

    assert hasattr(student, "surname")
    assert student.surname == "surname"
    assert hasattr(student, "name")
    assert student.name == "name"
    assert hasattr(student, "group")
    assert student.group == 1
    assert hasattr(student, "average_score")
    assert student.average_score == 3


def test_magic():
    students_list = [
        Student("Targaryen", "Daenerys", 27, 8.8),
        Student("Snow", "Jon", 27, 3.7),
        Student("Stark", "Arya", 27, 5.1),
        Student("Stark", "Sansa", 27, 6.2),
        Student("Clegane", "Sandor", 27, 2.2)
    ]

    assert Student("-", "-", 1, 8.8) == students_list[0]
    assert Student("-", "-", 1, 9) != students_list[0]
    assert Student("-", "-", 1, 7) < students_list[0]
    assert Student("-", "-", 1, 7) <= students_list[0]
    assert Student("-", "-", 1, 9) > students_list[0]
    assert Student("-", "-", 1, 9) >= students_list[0]

    assert sorted(students_list) == [
        Student("Clegane", "Sandor", 27, 2.2),
        Student("Snow", "Jon", 27, 3.7),
        Student("Stark", "Arya", 27, 5.1),
        Student("Stark", "Sansa", 27, 6.2),
        Student("Targaryen", "Daenerys", 27, 8.8),
    ]
