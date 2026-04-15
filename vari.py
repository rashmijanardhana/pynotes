#Python Variable Scope
def show_value():
    x = 10  # Local variable
    print(x)

show_value()
# print(x)  # NameError: x is not defined

x = 20  # Global variable

def display():
    print(x)

display()
print(x)

value = 50

def update():
    value = 10  # Local variable shadows global
    print("Inside function:", value)

update()
print("Outside function:", value)

count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1

def outer():
    message = "Hello"

    def inner():
        print(message)  # Accessing enclosing variable

    inner()

outer()

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    inner()
    inner()

outer()

x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)

    inner()

outer()

print(len([1, 2, 3]))  # Built-in function

for i in range(3):
    loop_var = i

print(loop_var)  # Accessible outside loop

total = 100

def calculate():
    total = 50

    def adjust():
        nonlocal total
        total += 10

    adjust()
    return total

print(calculate())  # Output: 60
print(total)        # Output: 100

