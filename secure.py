from database import *
from encryption import *

print("🔐 SecureVault")
print("----------------------")

while True:
    print("\n1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Website: ")
        password = input("Password: ")

        encrypted_password = encrypt(password)

        add(site, str(encrypted_password))

        print("✅ Password saved successfully!")

    elif choice == "2":
        print("\n📂 Stored Passwords:")
        print(show())

    elif choice == "3":
        print("🔒 SecureVault closed.")
        break

    else:
        print("❌ Invalid choice!")