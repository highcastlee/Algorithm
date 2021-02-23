# Python3

###리스트 관련 함수
>- q= deque() -> 양방향 접근 가능 </br>
> - q.popleft() || q.appendLeft()
> - list.rotate(dir) : dir이 양수면 오른쪽으로 회전, 음수면 왼쪽으로 회전시킴<br/>
> - list끼리의 합은 요소 연결
> - list * n은 요소 반복
> - del(c[1])로 list 요소 삭제
> - c.insert(0,'k') 0 위치에 k 추가
> - c.remove('k') 요소 중 첫 'k'를 삭제
> - list.extend(list2) list에 list2를 연결
> - a = list.copy()  list 깊은 복사
> - list.reverse() list 뒤집기
> - if 'a' in list: list에 a 존재 확인
> - if 'a' not in list: 존재 확인2
> - set(list) list 중복 제거(객체형으로 바뀜)


###문자열 관련 함수
> - s[::-1] -> 문자열 s를 뒤집어서 리턴
> - s.reverse() or reversed(s) 한 후, join하면 문자열 뒤집기
> - eval('1+2')  -> '3'  // 계산된 값
> - '_'.join(['a','b']) -> "a_b"
> 구분자를 넣어 리스트 요소를 문자열로 합침
> - **a.isalpha() : a가 문자인지 체크**
> - **a.isdigit() : a가 숫자인지 체크**
> - a.split('+') : '+'를 기준으로 문자 나눠서 리스트 반환(기준 미포함)
> - a.partition('+') : '+'를 기준으로 문자 나눠서 리스트 반환(기준 포함) 
> - 문자열.count(x) : 문자에 x가 등장하는 횟수
> - 문자열.count(x, start) : start index에서 시작해서 x가 등장하는 횟수
> - 문자열.find(x) : 문자열 중 x의 인덱스. 없으면 -1
> - 문자열.rfind(x) : x가 여러개 있으면 마지막 인덱스 반환
> - 문자열.upper() or lower() : 대소문자 변환
> - 문자열.swapcase() : 대소문자 상호변환
> - 문자열.capitalize() : 첫 대문자 후 소문자
> - 문자열.strip() : 양쪽 공백 제거
> - 문자열.replace(a,b): 문자열 중 a를 b로 바꿈

###math 함수
>- math.factorial(5) # 5 팩토리얼
>- math.sqrt(6) # 6의 제곱근 출력
>- math.gcd(35, 14) 최대 공약수
>- 최소 공배수는 x*y // gcd(x,y)
>- math.pi
>- math.e
>- math.ceil(-3.14) -3 올림
>- math.floor(-3.14) -4 내림
>- math.trunc(-3.14) -3 0으로 내림
>- int(-3.14) : -3
>- math.round(3.14) 3 반올림
>- math.round(3.1415, 2) 3.14
>- 사사오입 원칙 : 반올림이 5이면 짝수일 때 내림, 홀수일 때 올림
><br/> ex) round(4.5) : 4 | round(3.5) : 4

###내장 산술 함수
> - abs(-2) : 2 절댓값 
> - pow(4, 2) : 4의 2제곱 16
> - pow(4,2,4) : 16을 4로 나눈 나머지
> - divmod(5, 2) : (2,1) 5를 2로 나눈 몫과 나머지

###import sys
>- sys.stdin.readline().split()
>- sys.stdin.readline().rstrip()
>- sys.setrecursionlimit(111111)
<br>//phthon은 재귀 깊이 제한이 3000이라서 늘려야줘야함

###strip() 함수
>- strip([chars]) : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거합니다.
>- lstrip([chars]) : 인자로 전달된 문자를 String의 왼쪽에서 제거합니다.
>- rstrip([chars]) : 인자로 전달된 문자를 String의 오른쪽에서 제거합니다.
>- ex)
>text = ' Water boils at 100 degrees '
</br>print('[' + text.rstrip() + ']')
</br>print('[' + text.lstrip() + ']')
</br>print('[' + text.strip() + ']')
>[ Water boils at 100 degrees]
</br>[Water boils at 100 degrees ]
</br>[Water boils at 100 degrees]

###from itertools import permutations
>- permutations: 순열
>- combinations: 조합
>- product: 중복 허용 순열
>- combinations_with_replacement: 중복 허용 조합


###import heapq
>- 다익스트라 최단 경로 알고리즘을 비롯한 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용
>- 힙에 원소를 삽입할 때는 heap.heappush()
>- 힙에서 원소를 꺼내고자 할 때는 heap.heappop()


###from bisect import bisect_left, bisect_right
>- 이진 탐색을 쉽게 구현할 수 있도록 해주는 라이브러리
>- '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적
>- from bisect import bisect_left, bisect_right
<br>a = [1, 2, 4, 4, 8]
<br>x = 4
<br>print(bisect_left(a, x))
<br>print(bisect_right(a, x))

###from collections import Counter
>- 등장 횟수를 세는 기능 제공
>- 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.
>- from collections import Counter
<br>counter = Counter(['red', 'blue', 'red' ,'green', 'blue', 'blue'])
<br>print(counter['red']) # 'red'가 등장한 횟수
<br>print(counter['blue']) # 'blue'가 등장한 횟수
<br>print(dict(counter)) # 딕셔너리형으로 변환

