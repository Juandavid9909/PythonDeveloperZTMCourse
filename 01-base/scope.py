# Scope - what variables do I have access to?
total = 100 # Global scope

if True:
    x = 10 # Global scope

def some_func():
    total1 = 100 # some_func scope
    
# Scope changes in functions, in all the cases except this is global scope