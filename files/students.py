
# domain, model
class Student():

    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name
        self.mark = mark

# data
class StudentRepository():

    def __init__(self):

        self.path = r"D:\Mark\Desktop\Logika_Python\files\students.txt"
        self.students = []

    def addStudent(self, student):
        with open(self.path, "a", encoding="utf-8") as file:
            file.write(f"{student.surname} {student.name} {student.mark} \n")


StudentRepository().addStudent(Student("Avramenko", "Dima", 5))

    