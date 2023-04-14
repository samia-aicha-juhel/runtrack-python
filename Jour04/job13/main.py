liste = [10,20,30,20,10,50,60,40,80,50,40] # initialisation de la liste
liste_sans_doublons = [] # initialisation de la liste sans doublons

for element in liste: # pour chaque élément de la liste
    if element not in liste_sans_doublons: # si l'élément n'est pas déjà dans la liste sans doublons
        liste_sans_doublons.append(element) # on l'ajoute à la liste sans doublons

print(liste_sans_doublons) # affichage de la liste sans doublons