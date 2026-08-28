import base64
import hashlib
import os

from cryptography.fernet import Fernet


def derive_key(master_password):
    digest = hashlib.sha256(
        master_password.encode("utf-8")
    ).digest()

    return base64.urlsafe_b64encode(digest)


def encrypt_password(password, master_password):
    key = derive_key(master_password)
    cipher = Fernet(key)

    return cipher.encrypt(
        password.encode("utf-8")
    ).decode("utf-8")


def decrypt_password(encrypted_password, master_password):
    key = derive_key(master_password)
    cipher = Fernet(key)

    return cipher.decrypt(
        encrypted_password.encode("utf-8")
    ).decode("utf-8")
