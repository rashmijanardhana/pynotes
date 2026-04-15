#Python for While loop
count = 1

while count <= 5:
    print(count)
    count += 1

number = 5

while number > 0:
    print(number)
    number -= 1

user_input = ""

while user_input != "exit":
    user_input = input("Type 'exit' to stop: ")

#while True:
    #print("Running...")

count = 0

while True:
    if count == 3:
        break
    print(count)
    count += 1

number = 0

while number < 5:
    number += 1
    if number == 3:
        continue
    print(number)

x = 0

while x < 3:
    print(x)
    x += 1
else:
    print("Loop completed normally")

count = 0

while True:
    print("Executing at least once")
    count += 1
    if count == 3:
        break

i = 1

while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

age = -1

while age < 0:
    age = int(input("Enter a positive age: "))

print("Valid age entered:", age)