print("a" > "b")
print(0 != 0)
print(1 >= 0)
print(-2 <= 0)

# < > == >= <= !=
# and or not

print(not(True))
print(not(1 == 1))

is_magician = False
is_expert = True

# check if magician AND expert : "you are a master magician"
if is_expert and is_magician:
    print("you are a master magician")
    
# check if magician but not expert: "at least you're getting there"
elif is_magician and not is_expert:
    print("at least you're getting there")
    
# if you're not a magician: "You need magic powers"
elif not is_magician:
    print("You need magic powers")
    
    
# is vs ==
print(True == 1) # True
print("" == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([] == []) # True

# is checks if the location in memory is the same
print(True is 1) # False
print("1" is 1) # False
print([] is 1) # False
print(10 is 10.0) # False
print([1, 2, 3] is [1, 2, 3]) # False