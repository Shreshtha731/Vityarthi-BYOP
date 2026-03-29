import os
import time
from collections import deque

MAZE = [
    "S #       ",
    "  #  ###  ",
    "     #    ",
    " ### # ###",
    "   # #   E",
    "   #     #"
]

def print_maze(maze, visited=None):
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\n--- AI Maze Search ---")
    for r in range(len(maze)):
        row_str = ""
        for c in range(len(maze[0])):
            if visited and (r, c) in visited:
                row_str += ". "
            else:
                row_str += maze[r][c] + " "
        print(row_str)
    print("----------------------\n")
    time.sleep(0.1)

def get_neighbors(r, c, maze):
    moves = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != '#':
            moves.append((nr, nc))
    return moves