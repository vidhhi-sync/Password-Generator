
import random
import string

# Take password length from the user
length = int(input("Enter the desired password length: "))

# Define character combinations
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display the password
print("Your generated password is:", password)
