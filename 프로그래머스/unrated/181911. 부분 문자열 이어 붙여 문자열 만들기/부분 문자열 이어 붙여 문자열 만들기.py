def solution(my_strings, parts):
    ans = ''
    idx = 0
    for s, e in parts:
        ans += my_strings[idx][s:e+1]
        idx += 1
    return ans