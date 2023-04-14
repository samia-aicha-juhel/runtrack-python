def tri_a_bulles(L) :
    n = len(L)
    for i in range(n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp

    return L

L = [4, 2, 7, 1, 6]
print(tri_a_bulles(L))