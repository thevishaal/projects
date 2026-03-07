# Student Management System
class StudentManager:
    def __init__(self):
        self.students_list = []

    def add_student(self, student):
        self.students_list.append(student)
        print("Student added!\n")

    def delete_student(self, name):
        flag = False
        for student in self.students_list:
            if student.name == name:
                self.students_list.remove(student)
                print("Student Deleted!\n")
                flag = True
                break
        
        if not flag:
            print("No student found.\n")

    def show_students(self):
        for student in self.students_list:
            student.show()
        
        if not self.students_list:
            print("No Students avialable.\n")

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show(self):
        print(f"Name: {self.name}\nAge: {self.age}\nCourse: {self.course}\n")

Manager = StudentManager()
while True:
    print("1 Add Student")
    print("2 Show Students")
    print("3 Delete Student")
    print("4 Exit")

    choice = input("Enter Choice:").strip()

    if choice == "1":
        name = input("Enter Student Name: ").strip()
        age = int(input("Enter Student Age: "))
        course = input("Enter Student Course: ").strip()

        student = Student(name, age, course)
        Manager.add_student(student)

    elif choice == "2":
        Manager.show_students()

    elif choice == "3":
        name = input("Enter Student Name: ").strip()  
        Manager.delete_student(name)

    elif choice == "4":
        print("System Exit.")
        break
    
    else: 
        print("Please select right choice.")