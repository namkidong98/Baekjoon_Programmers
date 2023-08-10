def solution(num_list, n):
    idx = 0
    ans = [] #답을 저장하는 배열
    for i in range(len(num_list) // n):
        temp = []
        for j in range(n):
            temp.append(num_list[idx + j])
        ans.append(temp)
        idx += n # 인덱스 올리기
    return ans
            
            