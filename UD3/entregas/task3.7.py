# TASK 3.7 - WORKING WITH CLASSES
# -------------------------------
class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(ID: {self.id}, Name: {self.name}, Age: {self.age})"

class Student:
    def __init__(self, id, person, degree):
        self.id = id
        self.person = person
        self.degree = degree

    def __str__(self):
        return f"Student(ID: {self.id}, {self.person}, Degree: {self.degree})"

class StudentGroup:
    def __init__(self, id, group_name):
        self.id = id
        self.group_name = group_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [student for student in self.students if student.id != student_id]

    def __str__(self):
        group_info = f"Student Group(ID: {self.id}, Name: {self.group_name})\n"
        group_info += "Students:\n"
        for student in self.students:
            group_info += f"{student}\n"
        return group_info

student1 = Student(1, Person(101, "Alejandro", 20), "Computer Science")
student2 = Student(2, Person(102, "Nicolás", 21), "Mathematics")
student3 = Student(3, Person(103, "Adrián", 22), "Physics")

print("Students:")
print(student1)
print(student2)
print(student3)

student_group = StudentGroup(1, "Science Group")
student_group.add_student(student1)
student_group.add_student(student2)
student_group.add_student(student3)

print("\nStudent Group Information:")
print(student_group)

student_group.remove_student(2)

print("\nStudent Group Information After Removing Nicolás:")
print(student_group)

student4 = Student(4, Person(104, "Diana", 23), "Chemistry")
student_group.add_student(student4)

print("\nStudent Group Information After Adding Diana:")
print(student_group)