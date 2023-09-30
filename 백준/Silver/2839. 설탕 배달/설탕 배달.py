N = int(input())
five = N // 5
min = N + 1
for i in range(five+1): # 0 ~ 5로 나눠질 수 있는 최대몫
    three, left = divmod(N-(5*i), 3)
    if left == 0:
        sum = i + three
        if sum < min: min = sum
if min != N + 1:
    print(min)
else:
    print(-1)