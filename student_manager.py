def add_student(name, age, grade):
    with open("students.txt", "a") as file:
        file.write(f"{name}, {age}, {grade}\n")
   

def display_students():
    with open("students.txt", "r") as file:
        for line in file:
            print(line.strip())

def find_student(name):
    with open("students.txt", "r") as file:
        for line in file.readlines():
            #print (line)
            lin = line.strip().split(",")
            if lin[0] == name:
                return {"name":lin[0],"age":lin[1],"grade":lin[2]}
        
        return None

#name = input("Enter name: ")
#age = input("Enter age: ")
#grade = input("Enter grade: ")
#add_student("Amy", "12", "C")
#display_students()
print (find_student("Bill"))