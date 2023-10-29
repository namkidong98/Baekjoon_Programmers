# 1026 보물, 실버 4

import sys
input = sys.stdin.readline

N = int(input())
A = [x for x in map(int, input().split())]
B = [x for x in map(int, input().split())]

A = sorted(A) # 오름차순으로 정렬
total = 0
for idx in range(len(A)):
    total += A[idx] * max(B) # B의 제일 큰 수와 곱해서 더하고
    B.remove(max(B))         # 해당 숫자는 B에서 제거(다음 번으로 큰 수가 다음 시행에서 추출될 수 있도록)
print(total)