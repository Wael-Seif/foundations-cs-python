# import json

# class Course:
#     def __init__(self, code, name, credit_hours, is_core=True):
#         self.code = code
#         self.name = name
#         self.credit_hours = credit_hours
#         self.is_core = is_core

#     def print(self):
#         return f"{self.code}: {self.name} ({self.credit_hours} credit hours)"


# class Student:
#     def __init__(self, student_id, name):
#         self.student_id = student_id
#         self.name = name
#         self.enrolled_courses = {}

#     def enroll(self, course):
#         if course.code in self.enrolled_courses:
#             print(f"Already enrolled in {course.name}.")

#         self.enrolled_courses[course.code] = course

#     def drop(self, course_code):
#         if course_code not in self.enrolled_courses:
#             print(f"Not enrolled in course code {course_code}.")
#         del self.enrolled_courses[course_code]

#     def list_courses(self):
#         return self.enrolled_courses.values

#     def print(self):
#         return f"{self.name} (ID: {self.student_id})"


# class CourseCatalog:
#     def __init__(self):
#         self.courses = {}

#     def add_course(self, course):
#         self.courses[course.code] = course

#     def get_course(self, course_code):
#         return self.courses.get(course_code, None)

#     def list_courses(self):
#         return list(self.courses.values())

#     def save_to_file(self, filename):
#         with open(filename, 'w') as file:
#             json.dump({code: vars(course) for code, course in self.courses.items()}, file)

#     def load_from_file(self, filename):
#         with open(filename, 'r') as file:
#             data = json.load(file)
#             for code, course_data in data.items():
#                 course = Course(course_data['code'], course_data['name'], course_data['credit_hours'], course_data['is_core'])
#                 self.add_course(course)


# class EnrollmentSystem:
#     def __init__(self):
#         self.catalog = CourseCatalog()
#         self.students = {}

#     def add_student(self, student):
#         self.students[student.student_id] = student

#     def get_student(self, student_id):
#         return self.students.get(student_id, None)

#     def enroll_student(self, student_id, course_code):
#         student = self.get_student(student_id)
#         course = self.catalog.get_course(course_code)
#         if student and course:
#             student.enroll(course)
#         else:
#             raise Exception("Student or course not found.")

#     def drop_student_course(self, student_id, course_code):
#         student = self.get_student(student_id)
#         if student:
#             student.drop(course_code)
#         else:
#             raise Exception("Student not found.")

#     def list_student_courses(self, student_id):
#         student = self.get_student(student_id)
#         if student:
#             return student.list_courses()
#         else:
#             raise Exception("Student not found.")

#     def save_catalog(self, filename):
#         self.catalog.save_to_file(filename)

#     def load_catalog(self, filename):
#         self.catalog.load_from_file(filename)


# def main():
#     system = EnrollmentSystem()

#     while True:
#         print("\nMenu:")
#         print("1. Add Course")
#         print("2. Enroll Student in Course")
#         print("3. Drop Course for Student")
#         print("4. List Student Courses")
#         print("5. Save Course Catalog")
#         print("6. Load Course Catalog")
#         print("7. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             code = input("Enter course code: ")
#             name = input("Enter course name: ")
#             credit_hours = int(input("Enter credit hours: "))
#             is_core = input("Is this a core course? (y/n): ").lower() == 'y'
#             course = Course(code, name, credit_hours, is_core)
#             system.catalog.add_course(course)
#             print(f"Course {name} added successfully.")

#         elif choice == '2':
#             student_id = input("Enter student ID: ")
#             course_code = input("Enter course code: ")
#             if student_id not in system.students:
#                 name = input("Enter student name: ")
#                 student = Student(student_id, name)
#                 system.add_student(student)
#             try:
#                 system.enroll_student(student_id, course_code)
#                 print(f"Student {student_id} enrolled in {course_code} successfully.")
#             except Exception as e:
#                 print(e)

#         elif choice == '3':
#             student_id = input("Enter student ID: ")
#             course_code = input("Enter course code: ")
#             try:
#                 system.drop_student_course(student_id, course_code)
#                 print(f"Student {student_id} dropped course {course_code} successfully.")
#             except Exception as e:
#                 print(e)

#         elif choice == '4':
#             student_id = input("Enter student ID: ")
#             try:
#                 courses = system.list_student_courses(student_id)
#                 if courses:
#                     print("Courses enrolled:")
#                     for course in courses:
#                         print(course)
#                 else:
#                     print("No courses found.")
#             except Exception as e:
#                 print(e)

#         elif choice == '5':
#             filename = input("Enter filename to save course catalog: ")
#             system.save_catalog(filename)
#             print("Course catalog saved successfully.")

#         elif choice == '6':
#             filename = input("Enter filename to load course catalog: ")
#             system.load_catalog(filename)
#             print("Course catalog loaded successfully.")

#         elif choice == '7':
#             print("Exiting the program.")
#             break

#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()
