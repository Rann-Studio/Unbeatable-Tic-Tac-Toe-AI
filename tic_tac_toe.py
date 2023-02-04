import os
import time

board = [' ' for x in range(9)]


def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\n{row1}\n{row2}\n{row3}\n')


def player_move(icon):
    print("Player turn")
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")
        player_move(icon)


def ai_move(icon):
    print("AI turn ...")
    best_score = -10000
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = icon
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = icon


def minimax(board, depth, is_maximizing):
    result = check_winner()
    if result != None:
        if result == 'X':
            return -1
        elif result == 'O':
            return 1
        else:
            return 0
    if is_maximizing:
        best_score = -10000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 10000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


def check_winner():
    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or \
       (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or \
       (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or \
       (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or \
       (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or \
       (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or \
       (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or \
       (board[2] == 'X' and board[4] == 'X' and board[6] == 'X'):
        return 'X'
    elif (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or \
         (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or \
         (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or \
         (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or \
         (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or \
         (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or \
         (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or \
         (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
        return 'O'
    elif ' ' not in board:
        return 'Tie'
    else:
        return None


while True:
    print_board()
    player_move('X')
    print_board()
    if check_winner() != None:
        break
    ai_move('O')
    time.sleep(1.5)
    print_board()
    if check_winner() != None:
        break

result = check_winner()
if result == 'X':
    print("Player Win!")
elif result == 'O':
    print("AI Win!")
else:
    print("Tie!")
