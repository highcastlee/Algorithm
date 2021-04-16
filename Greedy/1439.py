
s = input()

def solution(s):
    groupZero = 0
    groupOne = 0
    for i in range(0,len(s)-1):

        if s[i] == s[i+1]:
            continue
        if s[i] == '0':
            groupZero += 1
        else:
            groupOne += 1
    if s[-1] == '0':
        groupZero +=1
    else:
        groupOne +=1

    print(min(groupZero, groupOne))


solution(s)