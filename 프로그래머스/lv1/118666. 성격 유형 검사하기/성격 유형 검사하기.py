def solution(surveys, choices):
    dic = {'R':0, 'C':0,'J':0, 'A':0}; ans = []
    for i in range(len(surveys)):
        survey = surveys[i]; 
        choice = choices[i]; choice -= 4
        if 'R' in survey:
            if survey[0] == 'R':
                dic['R'] += (choice * -1)
            else:
                dic['R'] += choice
        if 'C' in survey:
            if survey[0] == 'C':
                dic['C'] += (choice * -1)
            else:
                dic['C'] += choice
        if 'J' in survey:
            if survey[0] == 'J':
                dic['J'] += (choice * -1)
            else:
                dic['J'] += choice
        if 'A' in survey:
            if survey[0] == 'A':
                dic['A'] += (choice * -1)
            else:
                dic['A'] += choice
    if dic['R'] >= 0:
        ans.append('R')
    else:
        ans.append('T')
    if dic['C'] >= 0:
        ans.append('C')
    else:
        ans.append('F')
    if dic['J'] >= 0:
        ans.append('J')
    else:
        ans.append('M')
    if dic['A'] >= 0:
        ans.append('A')
    else:
        ans.append('N')
    return "".join(ans)