def solution(n):
    ans = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            if divisor not in ans:
                ans.append(divisor)
        else:
            divisor += 1
    return ans
            