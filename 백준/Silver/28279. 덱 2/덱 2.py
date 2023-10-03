import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
my_deque = deque()

for i in range(N):
    command = list(map(int, input().split()))
    if command[0] == 1:
        my_deque.appendleft(command[1])
    elif command[0] == 2:
        my_deque.append(command[1])
    elif command[0] == 3:
        print(my_deque.popleft() if my_deque else -1)
    elif command[0] == 4:
        print(my_deque.pop() if my_deque else -1)
    elif command[0] == 5:
        print(len(my_deque))
    elif command[0] == 6:
        print(0 if my_deque else 1)
    elif command[0] == 7:
        print(my_deque[0] if my_deque else -1)
    elif command[0] == 8:
        print(my_deque[-1] if my_deque else -1)