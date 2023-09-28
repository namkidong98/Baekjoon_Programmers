chess = [1, 1, 2, 2, 2, 8]
input = [i for i in map(int, input().split())]
ans = ''
for idx in range(6):
    ans += str(chess[idx] - input[idx]) + ' '
print(ans)