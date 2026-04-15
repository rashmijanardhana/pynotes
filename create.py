#Python String
single_quote = 'Hello'
double_quote = "World"
multi_line = """This is
a multi-line
string"""

print(single_quote)
print(double_quote)
print(multi_line)

text = "Python"

print(text[0])    # P
print(text[-1])   # n

word = "Programming"

print(word[0:6])   # Output: Progra
print(word[:4])    # Output: Prog
print(word[4:])    # Output: ramming

name = "Python"

# name[0] = "J"  # Raises TypeError
print(name)

first = "Hello"
second = "World"

print(first + " " + second)  # Hello World
print(first * 3)             # HelloHelloHello

message = "Data Science"

print(len(message))         # Output: 12
print("Data" in message)    # True
print("AI" not in message)  # True

text = "  python programming  "

print(text.upper())     # PYTHON PROGRAMMING
print(text.lower())     # python programming
print(text.strip())     # python programming
print(text.replace("python", "Java"))  # Java programming

sentence = "Python is powerful"

words = sentence.split(" ")
print(words)  # ['Python', 'is', 'powerful']

joined = "-".join(words)
print(joined)  # Python-is-powerful

name = "Alice"
score = 95

print(f"{name} scored {score} marks.")                # f-string
print("{} scored {} marks.".format(name, score))      # format method

word = "Code"

for char in word:
    print(char)
    