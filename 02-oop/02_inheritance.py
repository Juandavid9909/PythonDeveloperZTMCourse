class User:
    def sign_in(self):
        print("logged in")
        
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        
    def attack(self):
        print(f"attacking with arros: arroes left - {self.num_arrows}")

wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)

wizard1.attack()
archer1.attack()

print(isinstance(wizard1, Wizard))