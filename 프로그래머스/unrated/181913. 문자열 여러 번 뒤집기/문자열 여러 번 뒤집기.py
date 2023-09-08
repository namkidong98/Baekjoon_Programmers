def solution(my_string, queries):
    for query in queries:
        s , e = query
        new = my_string[:s] #s 앞까지 긁어옴
        
        part = my_string[s : e + 1] # 뒤집을 부분 일단 슬라이싱
        new += part[::-1] # 가져온 것을 역순으로 돌려서 추가
        
        new += my_string[e+1:] # 나머지 뒷부분을 추가
        
        my_string = new # 해당 시행을 바뀐 문자열로 갱신
    return my_string