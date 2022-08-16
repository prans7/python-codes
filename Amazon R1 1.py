txt = "amazoun ies niece coumpany"

vowels = 'a,e,i,o,u'

a = txt.split(" ")

b = vowels.split(",")

leng = len(a)

count = 0
acount = 0

for i in range(0, leng):
    k = len(a[i])
    for j in range(0, k):
        if a[i][j] in b:
            count = count + 1
        if a[i][j] and a[i][j + 1] in b:
            acount = acount + 1

print(count)
