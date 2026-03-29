import time
import os
import argparse
from collections import deque

MAZE = [
    "S #       ",
    "  #  ###  ",
    "     #    ",
    " ### # ###",
    "   # #   E",
    "   #     #"
]

def print_maze(maze, visited=None, path=None):
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\n--- AI Maze Search ---")
    
    for r in range(len(maze)):
        row_str = ""
        for c in range(len(maze[0])):
            char = maze[r][c]
            
            if char == 'S' or char == 'E':
                row_str += f"\033[92m{char}\033[0m "
            elif char == '#':
                row_str += "█ "
            elif path and (r, c) in path:
                row_str += "\033[93m*\033[0m "
            elif visited and (r, c) in visited:
                row_str += "\033[90m.\033[0m "
            else:
                row_str += "  "
        print(row_str)
    print("----------------------\n")
    time.sleep(0.1)

def get_neighbors(r, c, maze):
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != '#':
            moves.append((nr, nc))
    return moves

def solve_maze(algo_type):
    start_node = None
    for r in range(len(MAZE)):
        for c in range(len(MAZE[0])):
            if MAZE[r][c] == 'S':
                start_node = (r, c)
                break

    frontier = deque([(start_node, [start_node])]) 
    visited = set([start_node])

    while frontier:
        if algo_type == 'bfs':
            current, path = frontier.popleft()
        else:
            current, path = frontier.pop()

        r, c = current

        if MAZE[r][c] == 'E':
            print_maze(MAZE, visited, path)
            print(f"Goal found using {algo_type.upper()} in {len(path)} steps!")
            return

        print_maze(MAZE, visited, None)

        for neighbor in get_neighbors(r, c, MAZE):
            if neighbor not in visited:
                visited.add(neighbor)
                frontier.append((neighbor, path + [neighbor]))

    print("No path found!")

def main():
    parser = argparse.ArgumentParser(description="Terminal Maze Solver using Uninformed Search.")
    parser.add_argument("-a", "--algo", type=str, choices=['bfs', 'dfs'], required=True, 
                        help="Choose the algorithm: 'bfs' or 'dfs'")
    
    args = parser.parse_args()
    solve_maze(args.algo)

if __name__ == "__main__":
    main()