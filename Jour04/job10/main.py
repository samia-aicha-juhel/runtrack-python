L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
long = len(L)
p = 1
for i in range (0, long) :
     if 25 <= L[i] <= 90 :
          p = p*L[i]
print ("produit des valeurs comprises entre 25 et 90 : ", p)