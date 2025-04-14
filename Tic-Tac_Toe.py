
import math

board = [" "] * 9

def winner(b, p):
    return any(b[i] == b[j] == b[k] == p for i, j, k in [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ])

def minimax(b, is_max):
    if winner(b, "O"): return -1
    if winner(b, "X"): return 1
    if " " not in b: return 0
    best = -math.inf if is_max else math.inf
    for i in range(9):
        if b[i] == " ":
            b[i] = "X" if is_max else "O"
            score = minimax(b, not is_max)
            b[i] = " "
            best = max(best, score) if is_max else min(best, score)
    return best

def best_move():
    move, best_score = -1, -math.inf
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score, move = score, i
    return move

def play():
    while True:
        # Display the board
        print("\n" + "\n".join([" | ".join(board[i:i+3]) for i in range(0, 9, 3)]))

        # Check for a winner or draw
        if winner(board, "X"):
            print("AI Wins!")
            break
        if winner(board, "O"):
            print("You Win!")
            break
        if " " not in board:
            print("Draw!")
            break

        if board.count(" ") % 2:  # Player's turn
            while True:
                try:
                    move = int(input("Enter position (0-8): "))
                    if 0 <= move < 9 and board[move] == " ":
                        board[move] = "O"  # Store player move
                        break
                    print("Invalid move! Try again.")
                except ValueError:
                    print("Enter a number between 0 and 8.")
        else:  # AI's turn
            move = best_move()
            board[move] = "X"  # AI move updates the board properly

play()
