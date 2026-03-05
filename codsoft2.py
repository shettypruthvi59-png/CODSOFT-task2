import tkinter as tk
from tkinter import messagebox
import math

# Game variables
board = [" " for _ in range(9)]
buttons = []
human_score = 0
ai_score = 0
draw_score = 0

# Check winner
def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False


def is_draw():
    return " " not in board


# Minimax with Alpha-Beta Pruning
def minimax(is_maximizing, alpha, beta):

    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False, alpha, beta)
                board[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, score)

                if beta <= alpha:
                    break

        return best_score

    else:

        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True, alpha, beta)
                board[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, score)

                if beta <= alpha:
                    break

        return best_score


# AI move
def ai_move():

    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False, -math.inf, math.inf)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"
    buttons[move]["text"] = "O"

    check_game_end()


# Button click
def player_move(index):

    if board[index] == " ":
        board[index] = "X"
        buttons[index]["text"] = "X"

        if not check_game_end():
            ai_move()


# Check game result
def check_game_end():

    global human_score, ai_score, draw_score

    if check_winner("X"):
        human_score += 1
        update_score()
        messagebox.showinfo("Game Over", "You Win!")
        reset_board()
        return True

    if check_winner("O"):
        ai_score += 1
        update_score()
        messagebox.showinfo("Game Over", "AI Wins!")
        reset_board()
        return True

    if is_draw():
        draw_score += 1
        update_score()
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset_board()
        return True

    return False


# Reset board
def reset_board():

    global board
    board = [" " for _ in range(9)]

    for btn in buttons:
        btn["text"] = ""


# Update scoreboard
def update_score():
    score_label.config(
        text=f"Human: {human_score}    AI: {ai_score}    Draw: {draw_score}"
    )


# GUI setup
root = tk.Tk()
root.title("Tic Tac Toe AI")

score_label = tk.Label(root, text="Human: 0    AI: 0    Draw: 0", font=("Arial", 14))
score_label.grid(row=0, column=0, columnspan=3, pady=10)

# Create board buttons
for i in range(9):

    btn = tk.Button(
        root,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: player_move(i)
    )

    btn.grid(row=(i//3)+1, column=i%3)
    buttons.append(btn)


restart_btn = tk.Button(root, text="Restart Game", font=("Arial", 12), command=reset_board)
restart_btn.grid(row=4, column=0, columnspan=3, pady=10)


root.mainloop()