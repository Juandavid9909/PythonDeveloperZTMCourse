# Tuple
# They are lists that can't be updated, so is inmutable
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])
print(5 in my_tuple)

user = {
    "basket": [1, 2, 3],
    "greet": "hello",
    "age": 20,
    (1, 2): [4, 5, 6]
}

# Convert a dictionary to tule
print(user.items())
print(user[(1, 2)])

new_tuple = my_tuple[1:2]
x, y, z, *other = (1, 2, 3, 4, 5)

print(new_tuple)
print(x)

# How many times the value occurs
print(my_tuple.count(5))

# Return the index of the value
print(my_tuple.index(5))

print(len(my_tuple))