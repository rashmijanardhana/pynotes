#python variables and literals
# Variable assignment
count = 10
price = 99.99
name = "Python"

print(count)   # Output: 10
print(price)   # Output: 99.99
print(name)    # Output: Python

a, b, c = 1, 2, 3

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

value = 100
print(value)  # Output: 100

value = "Reassigned"
print(value)  # Output: Reassigned

integer_literal = 42
float_literal = 3.14
complex_literal = 2 + 3j

print(integer_literal)  # Output: 42
print(float_literal)    # Output: 3.14
print(complex_literal)  # Output: (2+3j)

single_quote = 'Hello'
double_quote = "World"
multi_line = """This is
a multi-line
string"""

print(single_quote)  
print(double_quote)  
print(multi_line)
is_active = True
is_logged_in = False

print(is_active)      # Output: True
print(is_logged_in)   # Output: False
result = None

if result is None:
    print("No value assigned yet")

list_literal = [1, 2, 3]
tuple_literal = (4, 5, 6)
set_literal = {7, 8, 9}
dict_literal = {"a": 1, "b": 2}

print(list_literal)   # Output: [1, 2, 3]
print(tuple_literal)  # Output: (4, 5, 6)
print(set_literal)    # Output: {7, 8, 9}
print(dict_literal)   # Output: {'a': 1, 'b': 2}

binary = 0b1010
octal = 0o12
hexadecimal = 0xA

print(binary)       # Output: 10
print(octal)        # Output: 10
print(hexadecimal)  # Output: 10

x = 5
y = 3

sum_result = x + y
product_result = x * y

print(sum_result)      # Output: 8
print(product_result)  # Output: 15