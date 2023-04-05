# Scope - what variables do I have access to?
total = 100 # Global scope

if True:
    x = 10 # Global scope

def some_func():
    total1 = 100 # some_func scope
    
# Scope changes in functions, in all the cases except this is global scope

a = 1

def confusion():
    a = 5
    return a

print(a) # 1
print(confusion()) # 5

# 1. start with locar
# 2. parent local?
# 3. global
# 4. built in python functions