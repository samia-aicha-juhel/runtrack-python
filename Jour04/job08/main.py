L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
somme_paires = 0
for valeur in L:
    if valeur % 2 == 0:
        somme_paires += valeur
        print(somme_paires)
