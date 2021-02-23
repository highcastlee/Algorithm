
n = int(input())

words = []
for i in range(n):
    words.append(input().strip())

words = list(set(words))
words.sort()
words = sorted(words, key=lambda x:len(x))

for i in words:
    print(i)