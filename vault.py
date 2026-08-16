from database import *
from encryption import *

print("🔐 SecureVault")
print("================")

site = input("Website: ")
username = input("Username: ")
password = input("Password: ")

encrypted = encrypt(password)

data = f"Username: {username} | Password: {encrypted}"

add(site, data)

print("\n✅ Credentials saved!")
print("--------------------")
print(show())