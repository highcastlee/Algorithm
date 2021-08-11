def solution(scores):
    n = len(scores)
    
    def getGrade(score):
        if score >= 90 : return 'A'
        elif score >= 80 : return 'B'
        elif score >= 70 : return 'C'
        elif score >= 50 : return 'D'
        else : return 'F'
    
    graph = [ [i[j] for i in scores] for j in range(n)]
    
    answer = []

    for i in range(n):
        sum = 0
        sumCount = n
        for j in range(n):
            if i != j :
                sum += graph[i][j]
                continue
            else:
                if (max(graph[i]) == graph[i][j] or min(graph[i]) == graph[i][j]) and graph[i].count(graph[i][j]) == 1:
                    sumCount -= 1
                    continue
                sum += graph[i][j]
        answer.append(getGrade(sum/sumCount))        
        
    return ''.join(answer)