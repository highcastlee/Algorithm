import math
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    list1 = []
    list2 = []
    for i in range(len(str1)-1):
        s1 = str1[i]
        s2 = str1[i+1]
        if s1.isalpha() and s2.isalpha():
            list1.append(s1+s2)
    for j in range(len(str2)-1):
        s1 = str2[j]
        s2 = str2[j+1]
        if s1.isalpha() and s2.isalpha():
            list2.append(s1+s2)

    maxresult = {}
    minresult= {}
    for l in list1:
            maxresult[l] = max(list1.count(l),list2.count(l))
            minresult[l] = min(list1.count(l),list2.count(l))

    for l in list2:
            maxresult[l] = max(list1.count(l),list2.count(l))
            minresult[l] = min(list1.count(l),list2.count(l))

    maxCount = 0
    minCount = 0
    for d in maxresult:
        if maxresult[d] < 0:
            continue
        maxCount += maxresult[d]
    for d in minresult:
        if minresult[d] < 0:
            continue
        minCount += minresult[d]
    jakade = 0
    if minCount == maxCount == 0:
        jakade = 1
    else:
        jakade = minCount/maxCount

    answer = math.floor(jakade * 65536)
    return answer