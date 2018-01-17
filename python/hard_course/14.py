from simplecrypt import decrypt, DecryptionException

with open("encrypted.bin", "br") as f,  open("passwords.txt", "r") as passwords:
    text = f.read()
    for password in passwords:
        password = password.rstrip()
        try:
            plain_text = decrypt(password, text)
            print(password)
            print(plain_text)
        except DecryptionException:
            pass
