import random


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and \
                course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        # print(list(self.grades.values())[0])
        # print(len(list(self.grades.values())[0]))
        print(f'Средняя оценка за домашние задания: '
              f'{sum(list(self.grades.values())[0]) / len(list(self.grades.values())[0])}')
        print('Курсы в процессе изучения: ' + ', '.join(self.courses_in_progress))
        print('Завершенные курсы: ' + ', '.join(self.finished_courses))

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Оценки студента сравниваются с оценками студента!')
            return
        return (sum(list(self.grades.values())[0]) / len(list(self.grades.values())[0])) < \
               (sum(list(other.grades.values())[0]) / len(list(other.grades.values())[0]))



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Средняя оценка за лекции: {sum(list(self.grades.values())[0]) / len(list(self.grades.values())[0])}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Оценки лектора сравниваются с оценками лектора!')
            return
        return (sum(list(self.grades.values())[0]) / len(list(self.grades.values())[0])) < \
               (sum(list(other.grades.values())[0]) / len(list(other.grades.values())[0]))


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
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')


def average_grade(list_studs, course_title):
    av_gr = 0
    for s in list_studs:
        for c in i.courses_in_progress:
            if c == course_title:
                av_gr += sum(s.grades.get(course_title)) / len(s.grades.get(course_title))
    return av_gr


if __name__ == '__main__':
    list_of_students = []
    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python', 'Git']
    best_student.finished_courses += ['Как искать информацию в интернете']
    list_of_students.append(best_student)

    worst_student = Student('John', 'Bowman', 'your_gender')
    worst_student.courses_in_progress += ['Python', 'Git']
    worst_student.finished_courses += ['Как искать информацию в интернете']
    list_of_students.append(worst_student)

    list_of_lecturers = []
    cool_lecturer = Lecturer('Some', 'Buddy')
    cool_lecturer.courses_attached += ['Python']
    norm_lecturer = Lecturer('New', 'Hommie')
    norm_lecturer.courses_attached += ['Git']
    list_of_lecturers.extend([cool_lecturer, norm_lecturer])

    list_of_reviewers = []
    cool_reviewer = Reviewer('Fili', 'Trim')
    cool_reviewer.courses_attached += ['Python']
    norm_reviewer = Reviewer('Kili', 'Tram')
    norm_reviewer.courses_attached += ['Git']
    list_of_reviewers.extend([cool_reviewer, norm_reviewer])

    for t in range(1,8):
        for i in list_of_students:
            for j in i.courses_in_progress:
                for k in list_of_lecturers:
                    if j in k.courses_attached:
                        i.rate_lec(k, j, random.randint(5, 10))

        for i in list_of_students:
            for j in i.courses_in_progress:
                for k in list_of_reviewers:
                    if j in k.courses_attached:
                        k.rate_hw(i, j, random.randint(5, 10))

    print(list_of_students[0].__lt__(list_of_students[1]))
    print(list_of_lecturers[0].__lt__(list_of_lecturers[1]))

    #for i in list_of_students:
    #    print(i.grades)

    print(f"Средняя оценка по курсу Git: {average_grade(list_of_students, 'Git'):.1f}")
    print(f"Средняя оценка по курсу Python: {average_grade(list_of_students, 'Python'):.1f}")

    for i in list_of_students:
        i.__str__()
    for i in list_of_lecturers:
        i.__str__()
    for i in list_of_reviewers:
        i.__str__()
