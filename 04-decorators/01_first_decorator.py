# @classmethod
# @staticmethod

def hello(func):
    func()
    
def greet():
    print("still here!")

# del hello

a = hello(greet)

print(a)