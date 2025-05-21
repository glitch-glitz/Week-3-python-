#Many to many (student and courses)
class Student:
    def __init__(self,name):
        self.name = name
        self.courses= []

    def enroll(self, course):
        #only if it does not exist
        if course not in self.curse:
            self.courses.append(course)
            #add reverse relationship
            course.students.append(self)

    def __repr__(self):
        return f"Student {self.name} with courses {len(self.courses)}"

class Course:
    def __init__ (self, title):
        self.title =title
        #this can be used to store all students that belong to a course
        self.students = []

    def __repr__(self):
        return f"Course {self.title} with students {len(self.students)}"