
n = int(input())

words = []
for i in range(n):
    words.append(input())

noneGroup = 0

for word in words:
    alpha = []
    alpha.append(word[0])
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            alpha.append(word[i+1])
    for w in word:
        if alpha.count(w) > 1:
            noneGroup += 1
            break

print(n-noneGroup)


# list(a) == sorted(a, key=a.find)
# key=a.find는 a에서 찾는 문자 순서대로 정렬한다.
# ['a','b','a','b'] -> ['a','a','b','b']  이 두 가지가 다르면, 그룹이 아닌 문자
# ['h','a','p','p','y'] -> ['h','a','p','p','y'] 같으면 그룹 문자이다.
# 그룹 문자이면 count += 1 해서 체크
