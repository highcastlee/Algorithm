# def solution(name):
#     count1 = 0;
#     count2 = 0;
#     currentIndex = 0;
#     for i in range(len(name)):
#         if name[i] == 'A': continue;
#         nextIndex = i;
#         count1 += min((nextIndex-currentIndex),(len(name)-1-nextIndex)+currentIndex+1)
#         count1 += min(ord(name[i])-ord('A'), ord('Z')+1-ord(name[i]))
#         currentIndex = i;
        
#     currentIndex = 0;
#     for i in range(len(name),0,-1):
#         if i == len(name): ci = 0
#         else: ci = i
#         if name[ci] == 'A': continue;
#         nextIndex = ci;
#         count2 += min(abs(nextIndex-currentIndex),(len(name)-nextIndex+currentIndex))
#         count2 += min(ord(name[ci])-ord('A'), ord('Z')+1-ord(name[ci]))
#         currentIndex = ci;
        
#     answer = min(count1, count2)
#     return answer

def solution(name):
    answerArr = [0] * len(name)
    for i in range(len(name)):
        if name[i] != "A":
            if ord(name[i]) <= ord("M"): 
                answerArr[i] += ord(name[i]) - ord("A")
            else:
                answerArr[i] += ord("Z") - ord(name[i]) + 1
        else:
            answerArr[i] = 0

    currentIndex = 0
    rightMoveIndex = 0
    leftMoveIndex = 0
    answer = 0

    while True:
        rightCnt = 0
        leftCnt = 0

        if answerArr[currentIndex] != 0:
            answer += answerArr[currentIndex] # 위 아래 조작 횟수
            answerArr[currentIndex] = 0

        if sum(answerArr) == 0:
            break

        while True:
            rightMoveIndex += 1
            rightCnt += 1
            if answerArr[rightMoveIndex] != 0:
                break
       
        while True:
            leftMoveIndex -= 1
            leftCnt += 1
            if answerArr[leftMoveIndex] != 0:
                break

        if rightCnt < leftCnt or rightCnt == leftCnt:
            currentIndex = rightMoveIndex
            answer += rightCnt # 좌 우 이동 횟수
        else:
            currentIndex = leftMoveIndex
            answer += leftCnt # 좌 우 이동 횟수

        rightMoveIndex = currentIndex
        leftMoveIndex = currentIndex
    
    return answer

# def solution(name):
#     answer = 0
#     n = len(name)

#     def alphabet_to_num(char):
#         num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
#         return num_char[ord(char) - ord('A')]

#     for ch in name:
#         answer += alphabet_to_num(ch)

#     move = n - 1
#     for idx in range(n):
#         next_idx = idx + 1
#         while (next_idx < n) and (name[next_idx] == 'A'):
#             next_idx += 1
#         distance = min(idx, n - next_idx)
#         move = min(move, idx + n - next_idx + distance)

#     answer += move
#     return answer