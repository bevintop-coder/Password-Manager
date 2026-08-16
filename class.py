from database import *
from encryption import *

class SecureVault:

    def add_password(self):
        site = input("Website: ")
        username = input("Username: ")
        password = input("Password: ")

        encrypted_password = encrypt(password)

        add(site, f"{username}:{encrypted_password}")

        print("✅ Password encrypted and stored.")

    def show_passwords(self):
        print("\n🔐 Your Vault")
        print("----------------")
        print(show())


vault = SecureVault()

print("🔒 SecureVault")
print("================")

vault.add_password()
vault.show_passwords()