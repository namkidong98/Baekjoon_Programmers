def solution(my_string):
    ans = []
    s = 0
    for i in range(len(my_string)):
        ans.append(my_string[s:])
        s += 1
    return sorted(ans)