def solution(numLog):
    dic = {1:'w', -1:"s", 10:'d', -10:'a'}
    n = numLog[0]
    ans = ''
    for i in numLog[1:]:
        ans += dic[i - n]
        n = i
    return ans