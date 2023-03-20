import datetime

class Student:
    def __init__(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        self.__student_number = student_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__sex = sex
        self.__country_of_birth = country_of_birth

    def get_student_number(self):
        return self.__student_number

    def set_student_number(self, student_number):
        self.__student_number = student_number

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex

    def get_country_of_birth(self):
        return self.__country_of_birth

    def set_country_of_birth(self, country_of_birth):
        self.__country_of_birth = country_of_birth

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.__date_of_birth.year - ((today.month, today.day) < (self.__date_of_birth.month, self.__date_of_birth.day))
        return age

def set_file_location():
    file_location = input("Enter file location(ex: C:\\Users\\user\\{path}\\student_data.txt): ")
    return file_location

def write_to_file(students):
    with open(file_location, "w") as f:
        for student in students:
            f.write(f"{student.get_student_number()},{student.get_first_name()},{student.get_last_name()},{student.get_date_of_birth().strftime('%Y-%m-%d')},{student.get_sex()},{student.get_country_of_birth()}\n")
    print("Data written to file.")


def read_from_file():
    students = []
    try:
        with open(file_location, "r") as f:
            for line in f:
                data = line.strip().split(",")
                student = Student(data[0], data[1], data[2], datetime.datetime.strptime(data[3], "%Y-%m-%d").date(), data[4], data[5])
                students.append(student)
        print("Data read from file.")
        return students
    except FileNotFoundError:
        print("File not found.")
        return students


def add_student(students):
    if len(students) < 100:
        student_number = input("Enter student number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        date_of_birth = datetime.datetime.strptime(input("Enter date of birth (yyyy-mm-dd): "), "%Y-%m-%d").date()
        sex = input("Enter sex: ")
        country_of_birth = input("Enter country of birth: ")
        student = Student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth)
        students.append(student)
        print("Student added.")
    else:
        print("Maximum number of students reached.")


def find_student_by_number(students):
    student_number = input("Enter student number: ")
    for student in students:
        if student.get_student_number() == student_number:
            print(f"\nStudent number: {student.get_student_number()}")
            print(f"Name: {student.get_first_name()} {student.get_last_name()}")
            print(f"Age: {student.get_age()}")
            print(f"Sex: {student.get_sex()}")
            print(f"Country of birth: {student.get_country_of_birth()}")
            return
    print("Student not found.")


def show_all_students(students):
    for student in students:
        print(f"\nStudent number: {student.get_student_number()}")
        print(f"Name: {student.get_first_name()} {student.get_last_name()}")
        print(f"Age: {student.get_age()}")
        print(f"Sex: {student.get_sex()}")
        print(f"Country of birth: {student.get_country_of_birth()}\n")


def show_students_by_birth_year(students):
    birth_year = input("Enter birth year: ")
    for student in students:
        if student.get_date_of_birth().year == int(birth_year):
            print(f"\nStudent number: {student.get_student_number()}")
            print(f"Name: {student.get_first_name()} {student.get_last_name()}")
            print(f"Age: {student.get_age()}")
            print(f"Sex: {student.get_sex()}")
            print(f"Country of birth: {student.get_country_of_birth()}\n")


def modify_student_record(students):
    student_number = input("Enter student number: ")
    for student in students:
        if student.get_student_number() == student_number:
            operation_number = input("Enter operation number to modify (1=student number, 2=first name, 3=last name, 4=date of birth, 5=sex, 6=country of birth): ")
            if operation_number == "1":
                new_value = input("Enter new student number: ")
                student.set_student_number(new_value)
            elif operation_number == "2":
                new_value = input("Enter new first name: ")
                student.set_first_name(new_value)
            elif operation_number == "3":
                new_value = input("Enter new last name: ")
                student.set_last_name(new_value)
            elif operation_number == "4":
                new_value = datetime.datetime.strptime(input("Enter new date of birth (yyyy-mm-dd): "), "%Y-%m-%d").date()
                student.set_date_of_birth(new_value)
            elif operation_number == "5":
                new_value = input("Enter new sex: ")
                student.set_sex(new_value)
            elif operation_number == "6":
                new_value = input("Enter new country of birth: ")
                student.set_country_of_birth(new_value)
            else:
                print("Invalid operation number.")
                return
            print("Record modified.")
            return
    print("Student not found.")


def delete_student(students):
    student_number = input("Enter student number: ")
    for student in students:
        if student.get_student_number() == student_number:
            students.remove(student)
            print("Student deleted.")
            return
    print("Student not found.")

file_location = "student_data.txt"
students = []
while True:
    print("\n1. Set file location")
    print("2. Save student data to file")
    print("3. Load student data from file")
    print("4. Add a new student")
    print("5. Find a student by student number")
    print("6. Show all students")
    print("7. Show all students born in a given year")
    print("8. Modify a student record")
    print("9. Delete a student")
    print("10. Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        set_file_location()
    elif choice == "2":
        write_to_file(students)
    elif choice == "3":
        students = read_from_file()
    elif choice == "4":
        add_student(students)
    elif choice == "5":
        find_student_by_number(students)
    elif choice == "6":
        show_all_students(students)
    elif choice == "7":
        show_students_by_birth_year(students)
    elif choice == "8":
        modify_student_record(students)
    elif choice == "9":
        delete_student(students)
    elif choice == "10":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
    
