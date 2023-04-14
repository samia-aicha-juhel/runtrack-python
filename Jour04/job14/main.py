chaine_caracteres = "Le python est un langage très utile pour l'analyse de données."

n = 4 # la longueur minimale des mots à trouver

mots_plus_longs = [] # initialisation de la liste des mots plus longs

mot_en_cours = "" # initialisation du mot en cours

for caractere in chaine_caracteres:

    # si le caractère rencontré n'est pas un espace
    if caractere != " ":
        mot_en_cours += caractere # ajouter le caractère au mot en cours
        
    # si le caractère rencontré est un espace
    else:
        # vérifier si la longueur du mot en cours est supérieure à n
        if len(mot_en_cours) > n:
            mots_plus_longs.append(mot_en_cours) # ajouter le mot à la liste des mots plus longs
            
        mot_en_cours = "" # réinitialiser le mot en cours

# ajouter le dernier mot (non suivi par un espace) à la liste des mots plus longs, s'il y a lieu
if len(mot_en_cours) > n:
    mots_plus_longs.append(mot_en_cours)

print("Les mots plus longs que", n, "sont :", mots_plus_longs)