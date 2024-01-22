import random
import tkinter as tk
from tkinter import messagebox
from sudokuQuestions import sudoku_questions
# print(sudoku_questions)
def is_valid(board, row, col, num):
    # Check if the number can be placed in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number can be placed in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    # Find the first empty cell (cell with 0) in the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    # Find an empty location
    empty_loc = find_empty_location(board)

    # If there is no empty location, the puzzle is solved
    if not empty_loc:
        return True

    row, col = empty_loc

    # Try placing numbers 1 to 9 in the empty location
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number in the empty cell
            board[row][col] = num

            # Recursively try to solve the remaining puzzle
            if solve_sudoku(board):
                return True

            # If placing the current number doesn't lead to a solution, backtrack
            board[row][col] = 0

    # If no number can be placed in the current empty cell, backtrack
    return False

def print_sudoku(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def display_sudoku_gui(question_board, solved_board):
    def restart_game():
        root.destroy()  # Close the current GUI
        start_game()  # Restart the game with a new puzzle

    root = tk.Tk()
    root.title("Sudoku Solver")
    root.geometry("365x584+300+100")

    question_label = tk.Label(root, text="Sudoku Question:")
    question_label.pack()

    question_frame = tk.Frame(root)
    question_frame.pack()

    for i in range(9):
        for j in range(9):
            cell_value = question_board[i][j]
            cell_label = tk.Label(question_frame, text=str(cell_value) if cell_value != 0 else " ", width=3, height=1, relief="solid", borderwidth=1)
            cell_label.grid(row=i, column=j)

    solution_label = tk.Label(root, text="\nSudoku Solution:")
    solution_label.pack()

    solution_frame = tk.Frame(root)
    solution_frame.pack()

    for i in range(9):
        for j in range(9):
            cell_value = solved_board[i][j]
            cell_label = tk.Label(solution_frame, text=str(cell_value) if cell_value != 0 else " ", width=3, height=1, relief="solid", borderwidth=1)
            cell_label.grid(row=i, column=j)

    restart_button = tk.Button(root, text="Restart", command=restart_game)
    restart_button.pack()

    root.mainloop()


def start_game():
    # Select a random Sudoku puzzle
    selected_question = random.choice(sudoku_questions)

    sudoku_board = [row.copy() for row in selected_question]

    print("Sudoku Puzzle:")
    print_sudoku(sudoku_board)

    # Create a copy of the original puzzle to display the question
    question_board = [row.copy() for row in selected_question]

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku:")
        print_sudoku(sudoku_board)

        # Display the question and solution in a Tkinter GUI
        display_sudoku_gui(question_board, sudoku_board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    start_game()