def solution(numlist, n):
    ans = [] # 답을 담을 빈 리스트
    
    if n in numlist:
        ans.append(n)
    if n not in numlist:
        numlist.append(n)
        
    numlist.sort() # 우선 numlist를 오름차순 정렬
    
    if numlist.index(n) > 0 :
        front = numlist.index(n) - 1 # n의 인덱스 하나 전
    else:
        pass
        #return numlist
    if numlist.index(n) < len(numlist) - 1 :
        back = numlist.index(n) + 1  # n의 인덱스 하나 뒤
    else:
        pass
        #return numlist.reverse()
    
    i = 0 # ans에 들어간 원소의 개수
    while i < len(numlist) - 1:            
        try:
            back_dist = numlist[back] - n
        except:
            back_dist = 10000
        try:
            front_dist = n - numlist[front]
        except:
            front_dist = 10000
        if front_dist < 0:
            front_dist = 10000
        
        if back_dist <= front_dist: # 같은 경우에도 큰 수를 우선
            ans.append(numlist[back])
            back += 1 # 다음 시행을 위한 인덱스 변경
        else:
            ans.append(numlist[front])
            front -= 1 # 다음 시행을 위한 인덱스 변경
    
        i += 1 # 다음 시행으로
            
    return ans