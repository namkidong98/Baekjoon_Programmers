import sys

input = sys.stdin.readline

N, K = map(int, input().split())
price_list = [] # N개의 동전 가치를 입력 받는 리스트
ans = 0         # 필요한 동전의 개수

for _ in range(N):
    price_list.append(int(input()))

price_list = price_list[::-1] # 역순으로 정렬
for price in price_list:
    if K >= price:
        ans += K // price
        K %= price
print(ans)