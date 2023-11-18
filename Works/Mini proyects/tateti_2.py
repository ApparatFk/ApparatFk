def print_board(board):
    for row in board:
        print(" " + " | ".join(row))
        print("---|---|---")

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def get_free_positions(board):
    return [(x, y) for x in range(3) for y in range(3) if board[x][y] == ' ']

def make_move(board, position, player):
    x, y = position
    board[x][y] = player

def tictactoe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn, moves = 0, 0
    
    while moves < 9:
        print_board(board)
        player = players[turn]
        free_positions = get_free_positions(board)
        
        if not free_positions:
            print("It's a tie!")
            break
        
        print(f"Player {player}, enter your move (row, column):")
        try:
            move = input()
            x, y = map(int, move.split())
            if (x, y) in free_positions:
                make_move(board, (x, y), player)
                if check_winner(board, player):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                turn = 1 - turn
                moves += 1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter row and column numbers like '0 1'.")
    
    if moves == 9 and not check_winner(board, player):
        print_board(board)
        print("It's a tie!")

tictactoe()