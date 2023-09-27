str_list = []
max = 0
for i in range(5):
    str = input()
    if len(str) > max : max = len(str)
    if len(str) < 15: # 뒤에 공백을 붙여서 모두 15칸의 문자열로 변형
        str = str + (' ' * (15-len(str)))
    str_list.append(str) # str_list에 변형한 문자열을 다음 원소로 추가

ans = ''
for i in range(max): # 열에 해당
    for j in range(5): # 행에 해당
        if str_list[j][i] != ' ' : # 공백이 아닐때
            ans += str_list[j][i]

print(ans)