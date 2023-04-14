def distance_toilettes(marches, hauteur):
    # Calcul de la distance parcourue en descendant et remontant les marches
    distance = marches * 2 * hauteur

    # Conversion de la distance en mètres
    distance = distance / 100
    
    # Calcul de la distance par semaine
    distance = distance * 5 * 7
    
    # Formatage de la distance pour l'affichage
    distance_format = "{:.2f}".format(distance)
    
    # Construction du message de sortie
    message = f"Pour {marches} marches de {hauteur} cm, le gardien parcours {distance_format} m par semaine."
    return message
print(distance_toilettes(100, 20))
print(distance_toilettes(50, 30))
print(distance_toilettes(80, 15))