# Abstract class for Person
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.__name = name  # Private attribute
        self.__age = age  # Private attribute
        self._gender = gender  # Protected attribute

    @abstractmethod
    def display_info(self):
        pass

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


# Derived class: Student (inherits from Person)
class Student(Person):
    def __init__(self, name: str, age: int, gender: str, student_id: str, grade: str):
        super().__init__(name, age, gender)
        self.__student_id = student_id  # Private attribute
        self._grade = grade  # Protected attribute

    def display_info(self):
        print(f"Student Name: {self.get_name()}")
        print(f"Age: {self.get_age()}")
        print(f"Gender: {self._gender}")
        print(f"Student ID: {self.__student_id}")
        print(f"Grade: {self._grade}")
        print("-" * 30)

    def get_student_id(self):
        return self.__student_id

    def update_grade(self, new_grade: str):
        self._grade = new_grade


# Derived class: Teacher (inherits from Person)
class Teacher(Person):
    def __init__(self, name: str, age: int, gender: str, employee_id: str, subject: str):
        super().__init__(name, age, gender)
        self.__employee_id = employee_id  # Private attribute
        self._subject = subject  # Protected attribute

    def display_info(self):
        print(f"Teacher Name: {self.get_name()}")
        print(f"Age: {self.get_age()}")
        print(f"Gender: {self._gender}")
        print(f"Employee ID: {self.__employee_id}")
        print(f"Subject: {self._subject}")
        print("-" * 30)

    def get_employee_id(self):
        return self.__employee_id

    def update_subject(self, new_subject: str):
        self._subject = new_subject


# Polymorphism demonstration (handling both Student and Teacher)
def display_person_info(person: Person):
    person.display_info()


# Function to manage students
def manage_students():
    students = []
    while True:
        try:
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student by ID")
            print("4. Update Student Grade")
            print("5. Remove Student")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter student's name: ")
                age = int(input("Enter student's age: "))
                gender = input("Enter student's gender: ")
                student_id = input("Enter student's ID: ")
                grade = input("Enter student's grade: ")
                student = Student(name, age, gender, student_id, grade)
                students.append(student)
                print("Student added successfully!")

            elif choice == '2':
                if not students:
                    print("No students found.")
                else:
                    for student in students:
                        display_person_info(student)

            elif choice == '3':
                student_id = input("Enter student ID to search: ")
                student_found = False
                for student in students:
                    if student.get_student_id() == student_id:
                        display_person_info(student)
                        student_found = True
                        break
                if not student_found:
                    print("Student not found with the given ID.")

            elif choice == '4':
                student_id = input("Enter student ID to update grade: ")
                student_found = False
                for student in students:
                    if student.get_student_id() == student_id:
                        new_grade = input("Enter new grade: ")
                        student.update_grade(new_grade)
                        print("Grade updated successfully!")
                        student_found = True
                        break
                if not student_found:
                    print("Student not found with the given ID.")

            elif choice == '5':
                student_id = input("Enter student ID to remove: ")
                student_found = False
                for student in students:
                    if student.get_student_id() == student_id:
                        students.remove(student)
                        print(f"Student with ID {student_id} removed.")
                        student_found = True
                        break
                if not student_found:
                    print("Student not found with the given ID.")

            elif choice == '6':
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError as e:
            print(f"Error: {e}. Please enter valid input.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Function to manage teachers
def manage_teachers():
    teachers = []
    while True:
        try:
            print("1. Add Teacher")
            print("2. View All Teachers")
            print("3. Search Teacher by ID")
            print("4. Update Teacher Subject")
            print("5. Remove Teacher")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter teacher's name: ")
                age = int(input("Enter teacher's age: "))
                gender = input("Enter teacher's gender: ")
                employee_id = input("Enter teacher's ID: ")
                subject = input("Enter teacher's subject: ")
                teacher = Teacher(name, age, gender, employee_id, subject)
                teachers.append(teacher)
                print("Teacher added successfully!")

            elif choice == '2':
                if not teachers:
                    print("No teachers found.")
                else:
                    for teacher in teachers:
                        display_person_info(teacher)

            elif choice == '3':
                employee_id = input("Enter teacher ID to search: ")
                teacher_found = False
                for teacher in teachers:
                    if teacher.get_employee_id() == employee_id:
                        display_person_info(teacher)
                        teacher_found = True
                        break
                if not teacher_found:
                    print("Teacher not found with the given ID.")

            elif choice == '4':
                employee_id = input("Enter teacher ID to update subject: ")
                teacher_found = False
                for teacher in teachers:
                    if teacher.get_employee_id() == employee_id:
                        new_subject = input("Enter new subject: ")
                        teacher.update_subject(new_subject)
                        print("Subject updated successfully!")
                        teacher_found = True
                        break
                if not teacher_found:
                    print("Teacher not found with the given ID.")

            elif choice == '5':
                employee_id = input("Enter teacher ID to remove: ")
                teacher_found = False
                for teacher in teachers:
                    if teacher.get_employee_id() == employee_id:
                        teachers.remove(teacher)
                        print(f"Teacher with ID {employee_id} removed.")
                        teacher_found = True
                        break
                if not teacher_found:
                    print("Teacher not found with the given ID.")

            elif choice == '6':
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError as e:
            print(f"Error: {e}. Please enter valid input.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Login functionality with retry option use(Dictionary)
def login():
    users = {
        'Junayed Bin Karim': '12345',
        'teacher1': '6789',
        'Junayed': '1234'  # New user added here
    }
    
    print("Please log in to access the system.")
    
    while True:
        username = input("Username: ")
        password = input("Password: ")
        
        if username in users and users[username] == password:
            print("Login successful!")
            break  # Exit the loop if login is successful
        else:
            print("Invalid username or password. Please try again.")


# Main program logic
if __name__ == "__main__":
    login()
    while True:
        try:
            print("1. Manage Students")
            print("2. Manage Teachers")
            print("3. Exit")
            main_choice = input("Enter your choice: ")

            if main_choice == '1':
                manage_students()
            elif main_choice == '2':
                manage_teachers()
            elif main_choice == '3':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice! Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
