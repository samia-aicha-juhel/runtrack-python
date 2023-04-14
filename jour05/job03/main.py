def tapis_diagonal(n):
  for i in range(n):
        for j in range(n):
            if i + j == n - 1: # Si on est sur la diagonale inverse
                print("X", end=" ") # On affiche un X
            else:
                print(".", end=" ") # Sinon, on affiche un point
        print() # On passe à la ligne suivante  
tapis_diagonal(10)