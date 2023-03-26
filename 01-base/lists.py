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

print(letters.index("d", 0, 4)) #returns the position or the parameter in the range we specified
print("d" in letters)
print(letters.count("d"))

new_basket = letters.copy()
letters.reverse()
# letters.sort()
# sorted(letters)
print(sorted(basket))

# Common List Patterns
basket.sort()
basket.reverse()
print(basket[::-1]) # reverse a list without .reverse()

print(list(range(1, 100))) # create a list with the specified range, if we don't put the first parameter it will start since 0
sentence = "!"
new_sentence = sentence.join(["hi", "my", "name", "is", "JOJO"])
new_sentence = " ".join(["hi", "my", "name", "is", "JOJO"])

print(new_sentence) # return "hi!my!name!is!JOJO"

# List Unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a) # 1
print(b) # 2
print(c) # 3
print(other) # [4, 5, 6, 7, 8]
print(d) # 9

# None
weapons = None