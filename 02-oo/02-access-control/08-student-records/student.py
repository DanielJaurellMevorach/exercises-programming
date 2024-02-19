class Student:
    def __init__(self, name):
        self.name = name
        self.__course = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        score = self.calculate_letter_grade(score)
        self.__course.update({course_name: score})

    def get_courses(self):
        return self.__course