import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

my_deque = deque()
for idx, x in enumerate(list(map(int, input().split()))):
    my_deque.append((idx+1, x)) # 풍선의 번호와 풍선 안 종이의 숫자를 짝지어서 deque에 할당

for _ in range(N):
    idx, x = my_deque.popleft()
    print(idx, end=' ')     # 해당 풍선번호 출력
    if x > 0: x -= 1
    my_deque.rotate(x * -1) # 해당 풍선의 종이 만큼 rotate