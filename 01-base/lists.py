li = [1, 2, 3, 4, 5]
li2 = ["a", "b", "c"]
li3 = [1, 2, "a", True]

amazon_cart = ["notebooks", "sunglasses", "toys", "grapes"]
amazon_cart[0] = "laptop"
new_cart = amazon_cart
new_cart[0] = "gum"

print(amazon_cart[1:3])
print(amazon_cart[0::2])

print(new_cart)
print(amazon_cart)

# Matrix
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

print(matrix[0][1])

# List methods
basket = [1, 2, 3, 4, 5]

print(len(basket))

#adding
# new_list = basket.append(100) # insert the item in the end
# new_list = basket.insert(5, 100) # insert the item in the index (first parameter)
new_list = basket.extend([100, 101])
print(new_list)

#removing
basket.pop() # delete the last item
basket.remove(4) # delete the item in the index
basket.clear() # []
print(basket)

print(basket.index(2)) # returns the position

letters = ["a", "x", "b", "c", "d", "e", "d"]

print(letters.index("d", 0, 4))
print("d" in letters)
print(letters.count("d"))

new_basket = letters.copy()
letters.reverse()
# letters.sort()
# sorted(letters)
print(sorted(basket))