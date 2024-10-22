def find_best_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return i, j

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False    

def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    while True:
        print("Player X turn:")
        while True:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the col (0, 1, 2): "))
            if board[row][col] != " ":
                print("This spot is already taken. Try again.")
                continue
            else:
                board[row][col] = "X"
                break
        print_board(board)       
        if check_win(board):
            print("Player X wins!")
            break
        if check_tie(board):
            print("The game is a tie!")
            break

        print("Player O turn:")
        row, col = find_best_move(board)
        board[row][col] = "O"
        print_board(board)
        if check_win(board):
            print("Player O wins!")
            break
        if check_tie(board):
            print("The game is a tie!")
            break

tic_tac_toe()
