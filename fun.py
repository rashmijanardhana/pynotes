#Python Functions
def greet():
    print("Hello, Python!")

greet()

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Bob")

def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

student_info(age=20, name="Alice")

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # Output: 10

def display_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_profile(name="Alice", role="Engineer")

def complete_profile(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

complete_profile("Python", level="Advanced", year=2025)

square = lambda x: x ** 2
print(square(5))  # Output: 25

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
