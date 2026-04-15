empty_set = set()
unique_numbers = {1, 2, 3, 4}
mixed_set = {1, "Python", 3.5, True}

print(empty_set)
print(unique_numbers)
print(mixed_set)

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)  # Output: {1, 2, 3, 4}

fruits = {"apple", "banana"}

fruits.add("orange")
print(fruits)

colors = {"red", "green"}
colors.update(["blue", "yellow"])

print(colors)

numbers = {10, 20, 30, 40}

numbers.remove(20)
numbers.discard(50)  # No error if element doesn't exist

print(numbers)

data = {5, 10, 15}

print(len(data))       # Output: 3
print(10 in data)      # True
print(100 not in data) # True

languages = {"Python", "Java", "Go"}

for lang in languages:
    print(lang)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Union → {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersection → {3, 4}
print(A - B)  # Difference → {1, 2}
print(A ^ B)  # Symmetric Difference → {1, 2, 5, 6}

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Union → {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersection → {3, 4}
print(A - B)  # Difference → {1, 2}
print(A ^ B)  # Symmetric Difference → {1, 2, 5, 6}

A = {1, 2, 3}
B = {1, 2}

print(B.issubset(A))     # True
print(A.issuperset(B))   # True

values_set = {1, 2, 3}

list_version = list(values_set)
tuple_version = tuple(values_set)

print(list_version)   # [1, 2, 3]
print(tuple_version)  # (1, 2, 3)