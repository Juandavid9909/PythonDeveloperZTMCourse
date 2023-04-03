# *args **kwargs
# *args and **kwargs allows a function to accept n arguments
def super_func(name, *args, i="hi", **kwargs):
    total = 0
    
    for items in kwargs.values():
        total += items
    
    return sum(args) + total

print(super_func("Andy", 1, 2, 3, 4, 5, num1=5, num2=10))

# Rule: params. *args: default parameters, **kwargs