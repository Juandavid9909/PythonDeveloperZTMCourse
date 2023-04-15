class PlayerCharacter:
    # Class Object Attribute
    membership= True
    
    def __init__(self, name = "anonymous", age = 0):
        if self.membership:
            self.name = name
            self.age = age
        
    def shout(self):
        print(f"my name is {self.name}")
        
    # CLS is used to instanciate a new class object (we decide what name we want)
    @classmethod
    def adding_things(cls, num1,  num2):
        return cls("Teddy", num1 + num2)
        
player1 = PlayerCharacter("Cindy", 44)

print(player1.name)