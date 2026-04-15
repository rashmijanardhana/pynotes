#Python Function Arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info("Alice", 25)

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="Alice")

def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Bob")

def login(username, password):
    print(f"User: {username}")

login("admin", "1234")
# login("admin")  # Raises TypeError

def calculate_sum(*numbers):
    return sum(numbers)

print(calculate_sum(1, 2, 3))      # 6
print(calculate_sum(5, 10, 15, 5)) # 35

def user_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

user_profile(name="Alice", role="Developer", level="Senior")

def full_profile(name, *skills, **info):
    print("Name:", name)
    print("Skills:", skills)
    print("Details:", info)

full_profile("Alice", "Python", "ML", age=30, city="Toronto")

def divide(a, b, /):
    return a / b

print(divide(10, 2))
# divide(a=10, b=2)  # Raises TypeError

def configure(*, mode="light"):
    print(f"Mode: {mode}")

configure(mode="dark")

def multiply(a, b, c):
    return a * b * c

values = (2, 3, 4)
print(multiply(*values))  # Output: 24

data = {"a": 1, "b": 2, "c": 3}
print(multiply(**data))   # Output: 6

