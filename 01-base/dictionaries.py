# Dictionary
dictionary = {
    123: [1, 2, 3],
    "b": "hello",
    "x": True
}

my_list = [
    {
        "a": [1, 2, 3],
        "b": "hello",
        "x": True
    },
    {
        "a": [4, 5, 6],
        "b": "hello",
        "x": True
    }
]

print(my_list[0]["a"][2])
print(dictionary[123])

# Methods
user = {
    "basket": [1, 2, 3],
    "greet": "hello"
}

user2 = dict(name = "JohnJohn")

print(user["age"]) # Error
print(user.get("age")) # None
print(user.get("age", 55)) # 55

print("hello" in user) # check keys and values
print("hello" in user.keys()) # check only keys
print("hello" in user.values()) # check only values

print(user.items()) # create a list of tuples with the dictionary
user.clear() # set the dictionary to {}

user2 = user.copy() # create a copy without reference
print(user.clear())
print(user2)

print(user.pop("age")) # deletes de property age in a dictionary
print(user.popitem()) # delete a random property in the dictionary
print(user.update({ "age": 55 })) # update a key value