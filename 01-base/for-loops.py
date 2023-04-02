for item in (1, 2, 3, 4, 5):
    for x in ["a", "b", "c"]:
        print(item, x)
        
user = {
    "name": "Golem",
    "age": 5006,
    "can_swim": False
}

for item in user:
    print(item)
    
for key, value in user.items():
    print(key, value)
    
for item in user.values():
    print(item)
    
for item in user.keys():
    print(item)
    
# Counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counter = 0

for item in my_list:
    counter += item
    
print(counter)

# Range
for number in range(0, 10, 2):
    print(number)
    
# Enumerate
for i, char in enumerate("Helllooo"):
    print(i, char)