# Algorithm
Algorithm with Python3

자주쓰는 모듈

**from collections import deque </br>**
>q= deque() </br>
>

**import sys**
>sys.stdin.readline().split()
>sys.stdin.readline().rstrip()

>sys.setrecursionlimit(111111)
<br>//phthon은 재귀 깊이 제한이 낮아서 늘려야줘야함

**strip() 함수**
- strip([chars]) : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거합니다.
- lstrip([chars]) : 인자로 전달된 문자를 String의 왼쪽에서 제거합니다.
- rstrip([chars]) : 인자로 전달된 문자를 String의 오른쪽에서 제거합니다.
>text = ' Water boils at 100 degrees '
</br>print('[' + text.rstrip() + ']')
</br>print('[' + text.lstrip() + ']')
</br>print('[' + text.strip() + ']')

>[ Water boils at 100 degrees]
</br>[Water boils at 100 degrees ]
</br>[Water boils at 100 degrees]

**from itertools import permutations**
- permutations: 순열
- combinations: 조합
- product: 중복 허용 순열
- combinations_with_replacement: 중복 허용 조합


**improt heapq**
- 다익스트라 최단 경로 알고리즘을 비롯한 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용
- 힙에 원소를 삽입할 때는 heap.heappush()
- 힙에서 원소를 꺼내고자 할 때는 heap.heappop()


**from bisect import bisect_left, bisect_right**
- 이진 탐색을 쉽게 구현할 수 있도록 해주는 라이브러리
- '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적
> from bisect import bisect_left, bisect_right
<br>a = [1, 2, 4, 4, 8]
<br>x = 4
<br>print(bisect_left(a, x))
<br>print(bisect_right(a, x))

**from collections import Counter**
- 등장 횟수를 세는 기능 제공
- 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.
>from collections import Counter
<br>counter = Counter(['red', 'blue', 'red' ,'green', 'blue', 'blue'])
<br>print(counter['red']) # 'red'가 등장한 횟수
<br>print(counter['blue']) # 'blue'가 등장한 횟수
<br>print(dict(counter)) # 딕셔너리형으로 변환


**math**
>import math
<br>print(math.factorial(5)) # 5 팩토리얼
<br>print(math.sqrt(6)) # 6의 제곱근 출력
<br>print(math.gcd(35, 14))
<br>print(math.pi)
<br>print(math.e)