# MRO - Method Resolution Order
class A:
    num = 10
    
class B(A):
    pass

class C(A):
    num = 1
    
class D(B, C):
    pass

print(D.num) # 1
print(D.mro()) # Says the order of declaration