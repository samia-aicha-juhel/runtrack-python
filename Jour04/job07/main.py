def samia_l():
    l = [8, 24, 48, 2, 16]
    long = len(l)
    mult3 = 0
    for samia_l in range (long) :
        if l[samia_l] %3 == 0 :
            mult3 = mult3 + 1
            print ("Nombre de multiples de 3 : ", mult3)
samia_l()
