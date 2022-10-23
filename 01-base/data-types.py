#Fundamental Data Types
# int and float
print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4)) # 0.5

print(type(20 + 1.1))
print(2 ** 2)
print(2 // 4)
print(5 % 4)

# math functions
print(round(3.1))
print(abs(-20))

# operator precedence (), **, * /, + -
print(20 - 3 * 4)

#bin and complex
print(bin(5))
print(complex(1 + 2j))
print(int('0b101', 2))

# augmented assignment operator
some_value = 5
some_value = some_value + 2
some_value += 2

# strings
print(type("Hi hello there 24!"))
username = "supercoder"
password = "supersecret"

long_string = """
WOW
0 0
---
"""

first_name = "Juan"
last_name = "David"
full_name = first_name + " " + last_name

# type conversion
print(type(int(str(100))))

# Escape Sequence
weather = 'It\'s kind of sunny'

# formatted strings
name = "Johnny"
age = 55

print(f"hi {name}. You are {age} years old")
print("hi {}. You are {} years old".format(name, age))
print("hi {new_name}. You are {age} years old".format(new_name = "sally", age = 100))

# string indexes
selfish = "01234567"
print(selfish[0:3])
print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[::2])
print(selfish[-1])
print(selfish[::-1])

# string functions
greet = "hellloooo"
print(len("hellloooo"))
print(greet[0:len(greet)])

quote = "to be or not to be"
print(quote.upper()) #upper, capitalize, lower
print((quote.find("be")))
print(quote.replace("be", "me"))

# booleans
is_cool = False
is_cool = True
print(bool("True"))