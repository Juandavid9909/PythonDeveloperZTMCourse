class User:
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print("logged in")
        
class Wizard(User):
    def __init__(self, name, power, email):
        super(self.email)
        
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

wizard1 = Wizard("Merlin", 50, "merlin@gmail.com")
archer1 = Archer("Robin", 100)

print(wizard1.email)

# introspection
print(dir(wizard1))