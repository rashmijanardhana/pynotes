#Python Numbers and Mathematics
import math
import random
import statistics
integer_num = 10
float_num = 3.14
complex_num = 2 + 5j

print(type(integer_num))  # <class 'int'>
print(type(float_num))    # <class 'float'>
print(type(complex_num))  # <class 'complex'>

a = 12
b = 5

print(a + b)   # Addition → 17
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 60
print(a / b)   # Division → 2.4

x = 17
y = 5

print(x // y)  # Floor division → 3
print(x % y)   # Modulus → 2

base = 2
exponent = 4

result = base ** exponent
print(result)  # Output: 16


print(math.sqrt(16))   # Square root → 4.0
print(math.ceil(4.3))  # Ceiling → 5
print(math.floor(4.9)) # Floor → 4


angle = math.radians(30)

print(math.sin(angle))  # Sine of 30°
print(math.cos(angle))  # Cosine of 30°
print(math.tan(angle))  # Tangent of 30°

value = 3.5678

print(round(value))      # Output: 4
print(round(value, 2))   # Output: 3.57

number = -25

print(abs(number))       # Output: 25
print(math.copysign(10, -1))  # Output: -10.0


print(random.randint(1, 10))      # Random integer between 1 and 10
print(random.uniform(1.0, 5.0))   # Random float between 1.0 and 5.0


numbers = [10, 20, 30, 40, 50]

print(statistics.mean(numbers))   # Mean → 30
print(statistics.median(numbers)) # Median → 30
print(statistics.stdev(numbers))  # Standard deviation
