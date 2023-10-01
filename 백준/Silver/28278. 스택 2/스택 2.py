import sys

N = int(input())
stack = []

for _ in range(N):
    command = list(map(int,sys.stdin.readline().split()))
    if command[0] == 1:   # push
        stack.append(int(command[1]))
    elif command[0] == 2:
        print(stack.pop() if len(stack) else -1)
    elif command[0] == 3: # len
        print(len(stack))
    elif command[0] == 4: # empty
        print(0 if len(stack) else 1)
    elif command[0] == 5: # top
        print(stack[-1] if len(stack) else -1)