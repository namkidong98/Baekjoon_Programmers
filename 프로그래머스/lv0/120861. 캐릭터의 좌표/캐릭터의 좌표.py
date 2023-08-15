def solution(keyinput, board):
    x =0; y = 0
    for input in keyinput:
        if input == 'left':
            if x-1 >= ((board[0] // 2) * -1): 
                x -= 1
        elif input == 'right':
            if x+1 <= (board[0] // 2): 
                x += 1
        elif input == 'up':
            if y+1 <= (board[1] // 2): 
                y += 1
        elif input == 'down':
            if y-1 >= ((board[1] // 2) * -1): 
                y -= 1
    return [x, y]