#Python break and continue
for number in range(1, 10):
    if number == 5:
        break
    print(number)

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

count = 0

while True:
    if count == 3:
        break
    print(count)
    count += 1

num = 0

while num < 5:
    num += 1
    if num == 2:
        continue
    print(num)

for i in range(3):
    for j in range(5):
        if j == 2:
            break
        print(f"i={i}, j={j}")

found = False

for number in range(10):
    if number == 7:
        found = True
        break

print("Found:", found)

for n in range(5):
    if n == 10:
        break
else:
    print("Loop completed without break")

for char in "python123":
    if char.isdigit():
        continue
    print(char)

while True:
    user_input = input("Enter 'q' to quit: ")
    if user_input.lower() == 'q':
        break

numbers = [1, -2, 3, -4, 5]

for num in numbers:
    if num < 0:
        continue
    print(num)