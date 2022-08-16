def even(start, n):
    a = []
    if start % 2 != 0:
        start = start + 1
    var = start

    for i in range(n):
        a.append(var)
        var = var + 2

    return a


b = even(3, 7)

print(b)

