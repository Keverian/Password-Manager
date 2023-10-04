import base64

import bcrypt
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sqlite3

def gen_salt():
    return bcrypt.gensalt()

def hash_master_password(password, salt):
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password

# TODO: function that derive keys from master password
def derive_key(password, salt):
    password = password.encode('utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = kdf.derived(password)
    return key



# TODO: function that encrypt passwords from key
def encrypt_pw(key, password):
    password = password.encode('utf-8')
    key = base64.urlsafe_b64encode(key)
    f = Fernet(key)
    encry_pw = f.encrypt(password)
    return encry_pw

def decrypt_pw(key, password):
    password = password.encode('utf-8')
    key = base64.urlsafe_b64encode(key)
    f = Fernet(key)
    decry_pw = f.decrypt(password)
    return decry_pw
# TODO
