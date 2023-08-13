def solution(quiz):
    ans = []
    for i in quiz:
        i = i.split()
        if i[1] == '+':
            if int(i[0]) + int(i[2]) == int(i[4]):
                ans.append('O')
            else:
                ans.append('X')
        else:
            if int(i[0]) - int(i[2]) == int(i[4]):
                ans.append('O')
            else:
                ans.append('X')
    return ans