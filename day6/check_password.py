import hashlib
import requests

def check_password_pwned(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
    if suffix in response.text:
        return True
    return False

password = input("Enter password: ")
if check_password_pwned(password):
    print("This password has been compromised!")
else:
    print("This password is safe.")

