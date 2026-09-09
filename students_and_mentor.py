class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0.0
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        avg = self.average_grade()
        in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Нет'
        finished = ', '.join(self.finished_courses) if self.finished_courses else 'Нет'
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg:.1f}\n"
                f"Курсы в процессе изучения: {in_progress}\n"
                f"Завершенные курсы: {finished}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0.0
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        avg = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg:.1f}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def average_student_grade(students_list, course_name):
    all_grades = []
    for student in students_list:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    if not all_grades:
        return 0.0
    return round(sum(all_grades) / len(all_grades), 1)


def average_lecturer_grade(lecturers_list, course_name):
    all_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    if not all_grades:
        return 0.0
    return round(sum(all_grades) / len(all_grades), 1)


if __name__ == "__main__":
    student1 = Student('Ruoy', 'Eman', 'M')
    student2 = Student('Алёхина', 'Ольга', 'Ж')
    student3 = Student('Иван', 'Петров', 'M')

    lecturer1 = Lecturer('Иван', 'Иванов')
    lecturer2 = Lecturer('Петр', 'Петров')
    lecturer3 = Lecturer('Сидор', 'Сидоров')

    reviewer1 = Reviewer('Some', 'Buddy')
    reviewer2 = Reviewer('Елена', 'Смирнова')

    student1.courses_in_progress += ['Python', 'Git']
    student1.finished_courses += ['Введение в программирование']

    student2.courses_in_progress += ['Python', 'Java']
    student2.finished_courses += ['Алгоритмы']

    student3.courses_in_progress += ['Python']
    student3.finished_courses += ['Базы данных']

    lecturer1.courses_attached += ['Python', 'C++']
    lecturer2.courses_attached += ['Python', 'Java']
    lecturer3.courses_attached += ['Python']

    reviewer1.courses_attached += ['Python', 'Git']
    reviewer2.courses_attached += ['Python', 'Java']

    print("=== Примеры ошибочных ситуаций (возврат 'Ошибка') ===")
    print(student1.rate_lecture(reviewer1, 'Python', 5))
    print(student1.rate_lecture(lecturer1, 'Java', 5))
    print(reviewer1.rate_hw(student1, 'C++', 5))
    print(reviewer2.rate_hw(student3, 'Java', 5))
    print()

    reviewer1.rate_hw(student1, 'Python', 10)
    reviewer1.rate_hw(student1, 'Python', 9)
    reviewer1.rate_hw(student1, 'Git', 8)
    reviewer2.rate_hw(student2, 'Python', 7)
    reviewer2.rate_hw(student2, 'Java', 6)
    reviewer1.rate_hw(student3, 'Python', 9)
    reviewer2.rate_hw(student3, 'Python', 8)

    student1.rate_lecture(lecturer1, 'Python', 9)
    student1.rate_lecture(lecturer1, 'Python', 8)
    student2.rate_lecture(lecturer1, 'Python', 7)
    student2.rate_lecture(lecturer2, 'Python', 10)
    student2.rate_lecture(lecturer2, 'Java', 9)
    student3.rate_lecture(lecturer3, 'Python', 6)
    student3.rate_lecture(lecturer1, 'Python', 8)

    print("=== Студенты ===")
    print(student1)
    print()
    print(student2)
    print()
    print(student3)
    print("\n=== Лекторы ===")
    print(lecturer1)
    print()
    print(lecturer2)
    print()
    print(lecturer3)
    print("\n=== Проверяющие ===")
    print(reviewer1)
    print()
    print(reviewer2)

    print("\n=== Сравнение студентов ===")
    print(f"student1 > student2: {student1 > student2}")
    print(f"student1 < student3: {student1 < student3}")
    print(f"student2 == student3: {student2 == student3}")

    print("\n=== Сравнение лекторов ===")
    print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
    print(f"lecturer1 < lecturer3: {lecturer1 < lecturer3}")
    print(f"lecturer2 == lecturer3: {lecturer2 == lecturer3}")

    print("\n=== Подсчёт средних оценок по курсу 'Python' ===")
    students_python = [student1, student2, student3]
    avg_students = average_student_grade(students_python, 'Python')
    print(f"Средняя оценка за ДЗ по Python у всех студентов: {avg_students}")

    lecturers_python = [lecturer1, lecturer2, lecturer3]
    avg_lecturers = average_lecturer_grade(lecturers_python, 'Python')
    print(f"Средняя оценка за лекции по Python у всех лекторов: {avg_lecturers}")

    print("\n=== Курс 'Git' ===")
    avg_git = average_student_grade([student1, student2, student3], 'Git')
    print(f"Средняя оценка за ДЗ по Git: {avg_git}")

    avg_java_lect = average_lecturer_grade([lecturer1, lecturer2, lecturer3], 'Java')
    print(f"Средняя оценка за лекции по Java: {avg_java_lect}")