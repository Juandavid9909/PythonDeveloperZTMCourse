picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

def show_tree():
    for image in picture:
        for pixel in image:
            if(pixel):
                print("*", end="")
            else:
                print(" ", end="")
        print("")
        
show_tree()

# Parameters
def say_hello(name="Darth Vader", emoji=">:)"):
    print(f"helllloooo {name} {emoji}");
    
# Positional rguments
say_hello("Andrei", ":P")
say_hello("Dan", ":P")

# Keyword arguments
say_hello(emoji=":P", name="Juan")

# Return
def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)
    
total = sum(10, 20)
print(total)