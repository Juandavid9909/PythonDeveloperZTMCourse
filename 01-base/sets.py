# Set
# Sets doesn't have indexes
my_set = {1, 2, 3, 4, 5, 5}

my_set.add(100)
my_set.add(2)

# There aren't duplicates
print(my_set)

# How to return an array with no duplicates
my_list = [1, 2, 3, 4, 5, 5]

print(set(my_list))

print(1 in my_set)
print(len(my_set))

new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

your_set = {4, 5, 6, 7, 8, 9, 10}

# Show the items that are in the first set and not in the second one
print(my_set.difference(your_set))

# Remove an element in a set, doesn't return anything
print(my_set.discard(5))

# Remove the duplicate values between 2 sets, doesn't return anything
print(my_set.difference_update(your_set))

# Return the values that are in both sets
print(my_set.intersection(your_set))
print(my_set & your_set)

# Returns a boolean that says if the sets are totally different or there are common items
print(my_set.isdisjoint(your_set))

# Join 2 sets
print(my_set.union(your_set))
print(my_set | your_set)

# Check if a set is subset of another
print(my_set.issubset(your_set))

# Check if a set is superset of another
print(your_set.issuperset(my_set))