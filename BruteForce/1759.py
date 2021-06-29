from itertools import combinations

L,C = map(int,input().split())

letters = input().split()

l = sorted(letters)
combi = sorted(combinations(l, L))

for let in combi:
    letter = list(let)
    count = 0
    if 'a' in letter:
        count += 1
    if 'e' in letter:
        count += 1
    if 'i' in letter:
        count += 1
    if 'o' in letter:
        count += 1
    if 'u' in letter:
        count += 1
    if count == 0 or len(letter)-count < 2 :
        continue
    print(''.join(letter))
