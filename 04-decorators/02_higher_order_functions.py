# Higher Order Function HOC is a function that accepts another function in its parameters or returns a different function
def greet(func):
    func()
    
def greet2():
    def func():
        return 5
    return func