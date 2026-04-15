#Python for Loop
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

for i in range(2, 10, 2):
    print(i)

word = "Python"

for char in word:
    print(char)

languages = ["Python", "Java", "C++"]

for index, lang in enumerate(languages):
    print(index, lang)

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

for number in range(1, 10):
    if number == 5:
        break
    print(number)

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

for num in range(3):
    print(num)
else:
    print("Loop completed successfully")

student = {"name": "Alice", "age": 22, "grade": "A"}

for key, value in student.items():
    print(key, ":", value)
