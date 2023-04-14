# initialiser la liste de nombres
liste_nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# arrondir chaque nombre dans la liste
for i in range(len(liste_nombres)):
    liste_nombres[i] = int(liste_nombres[i] + 0.5)

# trier la liste dans l'ordre croissant
for i in range(len(liste_nombres)):
    for j in range(i + 1, len(liste_nombres)):
        if liste_nombres[i] > liste_nombres[j]:
            temp = liste_nombres[i]
            liste_nombres[i] = liste_nombres[j]
            liste_nombres[j] = temp

# afficher la liste résultante
print(liste_nombres)