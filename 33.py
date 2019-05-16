def betuszonyeg(size):
    n = size
    betuk = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z", "&"]
    # Két háromszöggel meg lehet csinálni

    # Első háromszög
    for i in range(n):
        for j in range(2 * n - 2, 2 * i, -1):
            print("-", end="")

        for l in range(i + 1):
            print(betuk[l], end="")
            if i == 0:
                print(end="")
            else:
                print("-", end="")

        for k in range(i - 1, -1, -1):
            print(betuk[k], end="")
            if k == 0:
                print(end="")
            else:
                print("-", end="")

        for j in range(2 * n - 2, 2 * i, -1):
            print("-", end="")
        print("")

    # Második háromszög
    for i in range(n - 2, -1, -1):
        for j in range(2 * n - 2, 2 * i, -1):
            print("-", end="")

        for k in range(i + 1):
            print(betuk[k], end="")
            if i == 0:
                print(end="")
            else:
                print("-", end="")

        for l in range(i - 1, -1, -1):
            print(betuk[l], end="")
            if l == 0:
                print(end="")
            else:
                print("-", end="")

        for j in range(2 * n - 2, 2 * i, -1):
            print("-", end="")
        print("")


n = int(input("Adj meg egy számot 1 és 27 között: "))
betuszonyeg(n)
