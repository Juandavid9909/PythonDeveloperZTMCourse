def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x) # nonlocal
        
    inner()
    print("outer:", x) # nonlocal
    
outer()