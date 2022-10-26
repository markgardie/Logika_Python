import time
 
class Student:
    def __init__(self, surname, name, mark):
        self.Surname = surname
        self.Name = name
        self.Mark = mark
 
students = []
 
def print_class(students):
    for student in students:
        print(student.surname, student.name, "-", student.mark)
    print("\n")
 
def print_five(students):
    print("Відмінники: ")
    for student in students:
        if student.mark == 5:
            print(student.surname)
    print("\n")
 
def find_average(students):
    average = 0
    for student in students:
        average += student.mark
    average /= len(students)
    print("Середня оцінка класу:", average)
 
start_time = time.time()
with open("students.txt", "r", encoding = "utf-8") as file:
    for line in file:
        data = line.split(" ")
        student = Student(data[0], data[1], int(data[2]))
        students.append(student)
 
#print_class(students)
print_five(students)
find_average(students)
print("Час виконання: ", (time.time()-start_time), "секунд")
