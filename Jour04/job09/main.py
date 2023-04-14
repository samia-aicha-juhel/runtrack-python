L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
# initialisation des variables max et min
max_element = L[0] 
min_element = L[0]
# boucle pour parcourir toute la liste
for p in range(1, len(L)):
    if L[p] > max_element:
        max_element = L[p]
    if L[p] < min_element:
        min_element = L[p]
    print(f"Le maximum de la liste est {max_element} et le minimum est {min_element}")