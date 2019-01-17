a = [[1, 2, 3]
    , [4, 5, ""]
    , [7, 8, 6]]
i = 1
j = 2

# print(a[i][j])
while (True):

    b = input("move")
    if b == "w" or b == "x" or b == "a" or b == "d":

        if (b == "x"):
            a[i][j], a[i - 1][j] = a[i - 1][j], a[i][j]
            i = i - 1
        elif (b == "d"):
            a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]
            j = j - 1

        elif (b == "a"):
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
            j = j + 1
        elif (b == "w"):
            a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
            i = i + 1
        if (a == [[1, 2, 3], [4, 5, 6], [7, 8, ""]]):
            print("you won")
            print("\n", a[0], "\n", a[1], "\n", a[2])
            break


    else:
        print("invalid")
    print("\n", a[0], "\n", a[1], "\n", a[2])
