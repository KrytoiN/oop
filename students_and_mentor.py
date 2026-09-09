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


if __name__ == "__main__":
    reviewer = Reviewer('Some', 'Buddy')
    lecturer1 = Lecturer('Иван', 'Иванов')
    lecturer2 = Lecturer('Петр', 'Петров')
    student1 = Student('Ruoy', 'Eman', 'M')
    student2 = Student('Алёхина', 'Ольга', 'Ж')

    reviewer.courses_attached += ['Python']
    lecturer1.courses_attached += ['Python']
    lecturer2.courses_attached += ['Python', 'Java']
    student1.courses_in_progress += ['Python', 'Git']
    student1.finished_courses += ['Введение в программирование']
    student2.courses_in_progress += ['Python']

    reviewer.rate_hw(student1, 'Python', 10)
    reviewer.rate_hw(student1, 'Python', 9)
    reviewer.rate_hw(student1, 'Python', 8)
    reviewer.rate_hw(student2, 'Python', 7)

    student1.rate_lecture(lecturer1, 'Python', 9)
    student1.rate_lecture(lecturer1, 'Python', 8)
    student2.rate_lecture(lecturer1, 'Python', 7)
    student2.rate_lecture(lecturer2, 'Python', 10)
    student2.rate_lecture(lecturer2, 'Java', 9)

    print("=== Reviewer ===")
    print(reviewer)
    print("\n=== Lecturer1 ===")
    print(lecturer1)
    print("\n=== Lecturer2 ===")
    print(lecturer2)
    print("\n=== Student1 ===")
    print(student1)
    print("\n=== Student2 ===")
    print(student2)

    print("\n=== Сравнение лекторов ===")
    print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")   # 8.0 > 10.0? False
    print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")   # True
    print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}") # False

    print("\n=== Сравнение студентов ===")
    print(f"student1 > student2: {student1 > student2}")      # 9.0 > 7.0? True
    print(f"student1 < student2: {student1 < student2}")      # False
    print(f"student1 == student2: {student1 == student2}")    # False