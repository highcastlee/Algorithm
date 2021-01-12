
def solution(s):
    answer = len(s)
    for step in range(1,len(s)//2+1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer

# 공통 문자를 찾은 단계를 step으로 구분(최대는 문자열의 절반)
# prev와 step 이후 : step 만큼의 문자를 비교하며 counting
# 다를 경우, count가 2 이상이라면, compressed에 count와 prev를 입력
# prev를 비교가 끝난 j번째 문자부터 다시 설정하고 count를 초기화
# 해당 step 만큼의 비교가 끝나고 종합 compressed와 이전 step의 answer 중 더 작은 값을 선택
