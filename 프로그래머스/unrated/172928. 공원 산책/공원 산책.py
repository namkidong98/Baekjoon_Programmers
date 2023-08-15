def solution(park, routes):
    row = len(park); col = len(park[0]) # park의 가로 세로 길이 구하기
    move = {'E':1, 'W':-1, 'S':1, 'N':-1} # 방향마다 움직이는 방향
    for i in range(row):
        for j in range(col):
            if park[i][j] == 'S':
                start = i, j # 출발 지점을 튜플로 설정
    
    for route in routes:
        x, y = start # 매 시행마다 현재 위치를 갱신
        exclude = False # 매 시행마다 exclude 초기화
        
        direction, distance = route.split() # 방향과 이동 거리를 추출
        distance = int(distance)
        
        if direction == 'E' or direction == 'W': # 좌우로 이동
            if 0 <= (y + (move[direction] * distance)) < col: # park의 범위 안에 있다면
                for i in range(1, distance + 1): 
                    if park[x][y + (move[direction] * i)] == 'X': # 방해물이 있다면 
                        exclude = True # 해당 명령은 제외
                        break
                if exclude == False: # 해당 명령을 제외하라는 지시가 없으면
                    y = y + move[direction] * distance
        
        elif direction == 'N' or direction == 'S': # 상하로 이동
            if 0 <= (x + (move[direction] * distance)) < row: # park의 범위 안에 있다면
                for i in range(1, distance + 1): 
                    if park[x + (move[direction] * i)][y] == 'X': # 방해물이 있다면 
                        exclude = True # 해당 명령은 제외
                        break
                if exclude == False: # 해당 명령을 제외하라는 지시가 없으면
                    x = x + move[direction] * distance
        
        start = x, y # 시행이 끝날 때 현재의 위치를 start에 할당
        print(start)
    return list(start)
        