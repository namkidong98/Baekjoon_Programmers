N = int(input()) # 도시의 개수
distance = [int(x) for x in input().split()] # 도시 사이의 거리
price = [int(x) for x in input().split()]    # 각 도시의 리터 비용

left = 0 # 현재 남은 리터
total = 0 # 전체 비용
min = max(price) # 현재 지점까지 오면서 가장 싼 리터 비용
for idx in range(N - 1):
    if price[idx] < min:
        min = price[idx]
    if left < distance[idx]:
        total += (distance[idx]-left) * min
print(total)