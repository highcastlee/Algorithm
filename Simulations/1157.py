import string

s = input()

counts = [0 for _ in range(len(s))]

letters = []

for letter in s.upper():
    letters.append(letter)
    counts[letters.index(letter)] += 1

print(counts)
print(letters)
if counts.count(max(counts)) > 1: print('?')
else: print(letters[counts.index(max(counts))])

# 관련 파이썬 함수
# .upper() or .lower()
# .index()
# .count()