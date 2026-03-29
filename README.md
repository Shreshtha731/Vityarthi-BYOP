# TermiMaze: AI Search Visualizer

## What is this?
I built this for my CSA2001 BYOP capstone. I was having a hard time visualizing how different pathfinding algorithms actually work just by looking at the code. I wanted to see them in action, but I didn't want to deal with the headache of setting up a massive React/Django web app just to draw a grid. 

So, I built a visualizer that animates the search process directly inside the Linux terminal. It demonstrates "Uninformed Search" strategies—specifically Breadth-First Search (BFS) and Depth-First Search (DFS).

## How to run it
You don't need to `pip install` anything, it uses pure Python 3 standard libraries.

1. Clone this repo and open your terminal.
2. Run the script and tell it which algorithm you want to watch using the `-a` flag.

**To watch BFS (searches evenly in all directions):**
`python3 maze_search.py -a bfs`

**To watch DFS (dives deep down one path before backtracking):**
`python3 maze_search.py -a dfs`