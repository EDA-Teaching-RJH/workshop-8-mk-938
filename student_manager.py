def add_student(name, age, grade):
    file = open("students.txt", "a")
    file.write(f"{name}, {age}, {grade}\n")
    file.close()

def display_students():
    pass

def find_student(student):
    pass

name = input("Enter name: ")
age = input("Enter age: ")
grade = input("Enter grade: ")
add_student(name, age, grade)
