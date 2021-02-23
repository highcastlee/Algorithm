
alpa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input().strip()

count = 0
for a in alpa:
    word = word.replace(a, '*')

print(word)