import string
import secrets
import os

def generate_password(length):
    charset = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(secrets.choice(charset) for _ in range(length))
    return password

min_length = 10
max_length = 12

num_passwords = int(input("Inserisci il numero di password da generare: "))
output_filename = "passwords.txt"

if not os.path.exists(output_filename):
    open(output_filename, 'w').close()

with open(output_filename, "a") as file:
    for i in range(num_passwords):
        length = secrets.randbelow(max_length - min_length + 1) + min_length
        password = generate_password(length)
        file.write(f"Password {i + 1}: {password}\n")
        print(f"Password {i + 1} generata e aggiunta al file")

print("Generazione delle password e aggiunta al file completato in", output_filename)
