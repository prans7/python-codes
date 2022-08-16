

txt = input()

txtrev = txt[::-1]

a = txtrev.split(" ")

n = len(a)

for i in range(0, n):
    k = len(a[i])
    for j in range (0, k):
        if j == 0:
            print(a[i][j].capitalize(), end="")
        else:
            print(a[i][j].lower(), end="")

    print("", end=" ")