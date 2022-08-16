
# a = list(map(int, input("Enter numbers").strip().split()))

#123

num = int(input("Enter a 3 digit number"))

sum1 = 0

while num != 0:
    n = num % 10
    sum1 = sum1*10 + n
    num = num // 10

print(sum1)


