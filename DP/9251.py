
s1 = input()
s2 = input()

def solution(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    graph = [[0]*(l1+1) for _ in range(l2+1)]
    for i in range(1,l2+1):
        for j in range(1,l1+1):
            if s2[i-1] == s1[j-1]:
                graph[i][j] = graph[i-1][j-1] +1
            else:
                graph[i][j] = max(graph[i][j-1], graph[i-1][j])
    print(graph[l2][l1])
    return graph[l2][l1]
solution(s1,s2)








































# import sys
#
# s1 = input()
# s2 = input()
#
# len1 = len(s1)
# len2 = len(s2)
#
# matrix = [[0] * (len2+1) for _ in range(len1+1)]
#
# for i in range(1, len1+1):
#     for j in range(1, len2+1):
#         if s1[i-1] == s2[j-1]:
#             matrix[i][j] = matrix[i-1][j-1]+1
#         else:
#             matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
#
