class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):

        """

        :param lecturer: shows a lecturer's name
        :param course: shows a course's name
        :param grade:  shows a grade's name
        :return: new grade in grade list from lecturer

        the function checks if a lecturer and a student are at the same course and if a
        lecturer exists. Then the function put a grade to a lecturer.

        Also, the function checks if a grade is between 0 and 10

        """

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 0 < grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]

                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)



class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):

        """

            :param student: shows a student's name
            :param course: shows a course's name
            :param grade:  shows a grade's name
            :return: new grade in grade list from lecturer

            the function checks if a reviewer and a student are at the same course and if a
            student exists. Then the function put a grade to a student.

            Also, the function checks if a grade is between 0 and 10

            """

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if 0 < grade <= 10:
                if course in student.grades:
                    student.grades[course] += [grade]

                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Donald', 'Duck')
cool_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 4)
best_student.rate_lecturer(cool_lecturer, 'Python', 40)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
print(cool_lecturer.grades)