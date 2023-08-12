def solution(order):
    ans = 0
    while order > 1:
        for i in [3, 6, 9]:
            if order % 10 == i:
                ans += 1
        order //= 10
    return ans