def solution(board):
    move = [-1, 0, 1]
    new_board = [row[:] for row in board]  # deep copy로 new_board에 board를 복사
    
    for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == 1:
                for k in move:
                    for l in move:
                        if (0 <= (i + k) < len(board)) and (0 <= (j + l) < len(board[i])):
                            new_board[i + k][j + l] = 1  # new_board에 할당
                            
    return sum(i.count(0) for i in new_board)