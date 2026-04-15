#Python if...else Statement
age = 20

if age >= 18:
    print("Eligible to vote")

    temperature = 15

if temperature > 25:
    print("It's warm outside")
else:
    print("It's cold outside")

    score = 85

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: D")

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Access granted")
    else:
        print("Incorrect password")

age = 25
is_verified = True

if age > 18 and is_verified:
    print("User can proceed")

x = 10

if x > 5: print("x is greater than 5")

num = 7

result = "Even" if num % 2 == 0 else "Odd"
print(result)  # Output: Odd

day = "Sunday"

if day in ["Saturday", "Sunday"]:
    print("Weekend")
else:
    print("Weekday")

username = "Alice"

if username.lower() == "alice":
    print("Welcome Alice")

value = 5

if value > 0:
    pass  # Placeholder for future logic

print("Program continues...")