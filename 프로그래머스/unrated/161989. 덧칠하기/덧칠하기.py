def solution(n, m, section):
    ans = 0; cur = section[0]
    for i in section:
        if i < cur:
            continue
        cur = i + m
        ans += 1
    return ans
        
        