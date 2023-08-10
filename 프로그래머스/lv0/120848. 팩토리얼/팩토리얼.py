def solution(n):
    i = 1
    ans = 1
    while(ans * i <= n):
        ans *= i
        i += 1
    return i - 1