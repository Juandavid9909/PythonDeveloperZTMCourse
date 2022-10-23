# name = "Andrei Neagoie"
# age = 50
# relationship_status = "single"

# relationship_status = 'it\'s complicated'

# print(relationship_status)

birth_year = int(input("what year were you born? "))
age = 2022 - birth_year

print(f"your age is: {age}")



# Password checker
username = input("what is your username? ")
password = input("what is your password? ")

password_length = len(password)
hidden_password = "*" * password_length

print(f"{username}, your password, {hidden_password} is {password_length} letters long")