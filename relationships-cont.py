class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def reading (self):
        print("read")


class Student(Person):
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        super().__init__(name, age)

#polymorphism ->> we are able to override the parent methods
    def reading(self):
        print(f"Students with id {self.student_id} is reading")

student = Student("Nelson", 27, 1)
student.reading()



class Parent(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def pay_fees(self):
        pass

parent = Parent("Muriithi", 35)
parent.reading()
parent.pay_fees()



class Department:
    def __init__(self, name):
        self.name= name
        #instance attribute to store all employees related to the department
        self.employees=[]

    #instance method that can add an employee to the department
    def add_employee(self, employee):
        #store the employee instance inside the employee list
        self.employees.append(employee)


    @classmethod
    def add_employees(self, *args):
        
       return args
       
class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Employee {self.name}"
classroom = Department("Classroom")
mercy = Employee("Mercy")
classroom.add_employee(mercy)
brian = Employee("brian")
classroom.add_employee(brian)
print("Classroom employees", classroom.employees)


hr = Department("Human Resource")
johnson = Employee("johnson")
mitchelle = Employee("mitchelle")
hr.add_employee(johnson)
hr.add_employee(mitchelle)
print("HR department", hr.employees)

print(Department.add_employees(Employee("edna"), Employee("sam"), Employee("dean"), Employee("tonny")))