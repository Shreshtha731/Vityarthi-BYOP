import os
import time

MAZE = [
    "S #       ",
    "  #  ###  ",
    "     #    ",
    " ### # ###",
    "   # #   E",
    "   #     #"
]

def print_maze(maze):
    """Clears the terminal and draws the maze."""
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\n--- AI Maze Search ---")
    for r in range(len(maze)):
        row_str = ""
        for c in range(len(maze[0])):
            row_str += maze[r][c] + " "
        print(row_str)
    print("----------------------\n")

if __name__ == "__main__":
    print_maze(MAZE)