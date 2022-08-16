
from math import sqrt

num = int(input("Enter a number to check if it is prime or not"))

num_sqrt = int(sqrt(num))

count = 0

for i in range(2, num_sqrt+1):
    if num%i == 0:
        count = count + 1

if count == 0:
    print("Number is prime")
else:
    print("Number is composite")