import random
import hashlib

def generate_password(length=12):
    # Génère un mot de passe aléatoire avec des lettres minuscules, majuscules, des chiffres et des  spéciaux
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

def hash_password(password):
    # Hache le mot de passe en utilisant SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Génère un nouveau mot de passe aléatoire
new_password = generate_password()
print("Nouveau mot de passe : " + new_password)

# Hache le mot de passe
hashed_password = hash_password(new_password)
print("Mot de passe haché : " + hashed_password)