import hashlib

def check_password(password):
    # Vérifie si le mot de passe respecte les exigences de sécurité
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in "!@#$%^&*" for char in password):
        return False
    return True

while True:
    password = input("Choisissez un mot de passe : ")
    if check_password(password):
        # Si le mot de passe est valide, on le crypte en utilisant SHA-256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        print("Mot de passe valide. Le mot de passe crypté est : " + hashed_password)
        break
    else:
        print("Le mot de passe ne respecte pas les exigences de sécurité. Veuillez en choisir un nouveau.")