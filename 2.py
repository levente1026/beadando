def alsoHaromszogMatrix(M):
    for i in range(0, len(M)):
        for j in range(i + 1, len(M)):
            if (M[i][j] != 0):
                return False
    return True

M = [[1, 0, 0, 0],
     [1, 4, 0, 0],
     [4, 6, 2, 0],
     [0, 4, 7, 6]]

if alsoHaromszogMatrix(M):
    print("Igen")
else:
    print("Nem")