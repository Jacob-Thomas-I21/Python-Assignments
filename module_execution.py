# -*- coding: utf-8 -*-
"""Module execution

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HNrQNkbcEMy3T44XRJMeBzRLNCgFtxEq

# **Excercise 2**
"""

# Import Employee from employee.py
from employee import Employee

# Import Course, CoreCourse, and ElectiveCourse from course_catalog.py
from course_catalog import Course, CoreCourse, ElectiveCourse

def module_execution():

    emp1 = Employee("Alice Johnson", 60000)

    print(f"Employee Name: {emp1.get_name()}")
    print(f"Employee Salary: ${emp1.get_salary()}")

    core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
    elective_course = ElectiveCourse("ART201", "Modern Art", 2, "liberal arts")

    print("\nCourse Catalog:")
    print(core_course.display_course_info())
    print(elective_course.display_course_info())


module_execution()