class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.all_students.append(self)

    def mean_in_total(course, students = all_students):
        '''
        :param course: course
        :param students: all of students on this course
        :return: mean in total for this course

        The function finds the mean in total of the course

        '''
        total_grade = []
        for student in students:
            for course_pr in student.courses_in_progress:
                if course == course_pr:
                    total_grade += student.grades[course]
        return f"На курсе '{course}' средний балл по всем студентам {sum(total_grade) / len(total_grade)}"

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

    @property
    def __mean(self):
        """

        :return: returns the mean of all courses
        The decorator finds the average of all grades from all courses.

        """
        all_grades = []
        for course, grades in self.grades.items():
            all_grades += grades
        mean = sum(all_grades) / len(all_grades)
        return mean

    def __gt__(self, other):
        return self.__mean > other.__mean

    def __lt__(self, other):
        return self.__mean < other.__mean

    def __eq__(self, other):
        return self.__mean == other.__mean

    def __str__(self):
        """

        :return: prints the reviewer name
        the function prints the reviewer name

        """

        if len(self.courses_in_progress) > 0:
            courses_in_progress = ", ".join(self.courses_in_progress)
        else:
            courses_in_progress = "Нет курсов в процессе изучения"

        if len(self.finished_courses) > 0:
            closed_courses = ", ".join(self.finished_courses)
        else:
            closed_courses = "Нет завершённых курсов"

        text = (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.__mean}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {closed_courses}\n")
        return text

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    all_lecturers = []

    def __init__(self, name, surname):
        self.grades = {}
        Lecturer.all_lecturers.append(self)
        super().__init__(name, surname)

    def mean_in_total(course, lecturers = all_lecturers):
        '''
        :param course: course
        :param lecturers: all of lecturers on this course
        :return: mean in total for this course

        The function finds the mean in total of the course

        '''
        total_grade = []
        for lecturer in lecturers:
            for course_pr in lecturer.courses_attached:
                if course == course_pr:
                    total_grade += lecturer.grades[course]
        return f"На курсе '{course}' средний балл по всем лекторам {sum(total_grade) / len(total_grade)}"
    @property
    def __mean(self):
        """

        :return: returns the mean of all courses
        The decorator finds the average of all grades from all courses.

        """
        all_grades = []
        for course, grades in self.grades.items():
            all_grades += grades
        mean = sum(all_grades) / len(all_grades)
        return mean

    def __gt__(self, other):
        return self.__mean > other.__mean

    def __lt__(self, other):
        return self.__mean < other.__mean

    def __eq__(self, other):
        return self.__mean == other.__mean

    def __str__(self):
        """

        :return: prints the reviewer name
        the function prints the reviewer name

        """
        text = (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.__mean}\n")
        return text


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

    def __str__(self):
        """

        :return: prints the reviewer name
        the function prints the reviewer name

        """
        text =(f"Имя: {self.name}\n"
               f"Фамилия: {self.surname}\n")
        return text

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

bad_lecturer = Lecturer('Misha', 'Bad')
bad_lecturer.courses_attached += ['Python']
cool_lecturer = Lecturer('Donald', 'Duck')
cool_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 4)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 3)
best_student.rate_lecturer(bad_lecturer, 'Python', 7)
best_student.rate_lecturer(cool_lecturer, 'Python', 40)

worst_student = Student('Andrew', 'Tate', 'male')
worst_student.courses_in_progress += ['Python']


cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(worst_student, 'Python', 2)
cool_reviewer.rate_hw(worst_student, 'Python', 1)
cool_reviewer.rate_hw(worst_student, 'Python', 1)

mean1 = Student.mean_in_total('Python')
mean2 = Lecturer.mean_in_total('Python')

print(best_student.grades)
print(worst_student.grades)
print(cool_lecturer.grades)
print(cool_reviewer)
print(cool_lecturer)
print(best_student)
print(mean1)
print(mean2)
print(best_student > worst_student)
print(cool_lecturer > bad_lecturer)