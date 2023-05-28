my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = (5, 4, 3)

# Create a tuple with each index, this means [(1, 10), (2, 20)...]
print(list(zip(my_list, your_list, their_list)))