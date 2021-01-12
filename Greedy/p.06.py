
def solution(food_times, k):
    temp = k
    answer = 0
    while temp:
        for j in range(len(food_times)):
            if food_times[j] == 0:
                count += 1
            else:
                food_times[j] -= 1
                temp -= 1
                count = 0
                if temp == 1:
                    answer = j+1

    return answer