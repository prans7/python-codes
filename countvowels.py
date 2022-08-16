s1 = "Hi Arnav how are you"

s = s1.casefold()

vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

n = len(s)

for i in range(0, n):
    if s[i] in vowels:
        vowels[s[i]] = vowels[s[i]] + 1

print(vowels)
