# -*- coding: utf-8 -*-
"""Assignment 5 File and Exception Handling.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jnapF42kUistYXyUEBjBDsTv4PIs5WTn

# **Exercise 1: Read and display file contents**
"""

def read_file(filename):
    try:

        with open(filename, 'r') as file:
            content = file.read()
            print("File Contents:\n", content)

    except FileNotFoundError:
        print("Error: File not found.")

    except Exception as e:
        print("Error:", e)


read_file("sample.txt")

"""# **Exercise 2: Copy contents of one file to another**"""

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            dest.write(src.read())
        print(f"Contents copied from {source_file} to {destination_file}")

    except FileNotFoundError:
        print("Error: Source file not found.")

    except Exception as e:
        print("Error:", e)


copy_file("sample.txt", "copy.txt")

"""# **Exercise 3: Count the total number of words in a file**"""

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            print(f"Total number of words in {filename}: {word_count}")

    except FileNotFoundError:
        print("Error: File not found.")

    except Exception as e:
        print("Error:", e)

count_words("sample.txt")

"""# **Exercise 4: Convert user input string to an integer with exception handling**"""

def convert_to_integer():
    while True:

        try:
            num = int(input("Enter a number: "))
            print(f"Successfully converted to integer: {num}")
            break

        except ValueError:
            print("Error: Please enter a valid integer.")


convert_to_integer()

"""# **Exercise 5: Check for negative numbers in user-input list**"""

def check_negative_numbers():
    try:
        nums = list(map(int, input("Enter a list of integers separated by space: ").split()))
        if any(n < 0 for n in nums):
            raise ValueError("Negative numbers are not allowed!")
        print("All numbers are valid:", nums)

    except ValueError as e:
        print("Error:", e)

check_negative_numbers()

"""# **Exercise 6: Compute average of user-input list with exception handling**"""

def compute_average():
    try:
        nums = list(map(int, input("Enter a list of integers separated by space: ").split()))
        avg = sum(nums) / len(nums)
        print(f"Average of the numbers: {avg}")

    except ZeroDivisionError:
        print("Error: Cannot compute average of an empty list.")

    except ValueError:
        print("Error: Please enter valid integers.")

    finally:
        print("Program execution finished.")

compute_average()

"""# **Exercise 7: Write a string to a user-defined file with exception handling**"""

def write_to_file():
    try:
        filename = input("Enter the filename to write: ")
        content = input("Enter the content to write into the file: ")

        with open(filename, 'w') as file:
            file.write(content)
        print("File written successfully.")

    except Exception as e:
        print("Error:", e)

    else:
        print("Welcome! No errors encountered.")

write_to_file()

