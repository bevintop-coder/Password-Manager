from database import *
from encryption import *


print("SecureVault")



site=input("Website:")

password=input("Password:")



encrypted=encrypt(password)



add(site,str(encrypted))



print(show())