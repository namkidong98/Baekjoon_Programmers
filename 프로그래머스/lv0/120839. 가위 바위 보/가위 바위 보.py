def solution(rsp):
    win = {'2' : '0', '0' : '5', '5' : '2'}
    ans = ""
    for i in list(rsp):
        ans += win[i]
    return ans