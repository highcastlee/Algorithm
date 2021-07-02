
S = input()
T = input()

ls = len(S)
lt = len(T)

def deleteA(s):
    return s[:-1]

def deleteB(s):
    s = s[:-1]
    return s[::-1]

count = 0

for _ in range(lt-ls):
    if T[-1] == 'A':
        T = deleteA(T)
    else:
        T = deleteB(T)

if S == T :
    print(1)
else:
    print(0)

