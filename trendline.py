import time
import os
import argparse
from collections import deque

# A simple text-based maze. 
# 'S' is Start, 'E' is End, '#' are walls, and ' ' are open paths.
MAZE = [
    "S #       ",
    "  #  ###  ",
    "     #    ",
    " ### # ###",
    "   # #   E",
    "   #     #"
]

def print_maze(maze, visited=None, path=None):
    """Clears the terminal and draws the maze with the current search state."""
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\n--- AI Maze Search ---")
    
    for r in range(len(maze)):
        row_str = ""
        for c in range(len(maze[0])):
            char = maze[r][c]
            
            # Color coding for the terminal
            if char == 'S' or char == 'E':
                row_str += f"\033[92m{char}\033[0m " # Green
            elif char == '#':
                row_str += "█ " # Solid block for walls
            elif path and (r, c) in path:
                row_str += "\033[93m*\033[0m " # Yellow star for the final path
            elif visited and (r, c) in visited:
                row_str += "\033[90m.\033[0m " # Grey dot for searched areas
            else:
                row_str += "  "
        print(row_str)
    print("----------------------\n")
    time.sleep(0.1) # Slow it down so we can see the animation

def get_neighbors(r, c, maze):
    """Finds all valid moves (up, down, left, right)."""
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        # Check if we are inside the maze and not hitting a wall
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != '#':
            moves.append((nr, nc))
    return moves

def solve_maze(algo_type):
    # Find the starting position 'S'
    start_node = None
    for r in range(len(MAZE)):
        for c in range(len(MAZE[0])):
            if MAZE[r][c] == 'S':
                start_node = (r, c)
                break

    # The 'frontier' is what we are checking next.
    # A Queue (pop left) makes it BFS. A Stack (pop right) makes it DFS.
    frontier = deque([(start_node, [start_node])]) 
    visited = set([start_node])

    while frontier:
        # This is the magic line that changes the algorithm!
        if algo_type == 'bfs':
            current, path = frontier.popleft() # BFS: Check oldest first (ripples out)
        else:
            current, path = frontier.pop()     # DFS: Check newest first (dives deep)

        r, c = current

        # Did we find the end?
        if MAZE[r][c] == 'E':
            print_maze(MAZE, visited, path)
            print(f"Goal found using {algo_type.upper()} in {len(path)} steps!")
            return

        # Animate the search process
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