# TermiMaze (CSA2001 Capstone)

## What is this?
This is my BYOP project for Fundamentals of AI & ML. 

Honestly, trying to picture how search algorithms (like BFS and DFS) actually work just by staring at standard Python output was giving me a headache. I wanted to see them run in real-time, but setting up a whole Django web app just to draw a simple grid felt like way too much work. 

Instead, I wrote this script. It uses basic terminal clearing to actually animate the "Uninformed Search" process right in your console so you can watch it solve the maze step-by-step.

## How to run it
I kept it super simple. You don't need to run any `pip install` commands or download external libraries. As long as you have Python 3 installed, it'll work perfectly.

Just clone the repo, open your terminal (I built and tested this in WSL), and run the script with either the `bfs` or `dfs` flag.

**To watch BFS (Breadth-First Search):**
`python3 maze_search.py -a bfs`
*(You'll see it spread out evenly like a ripple to find the absolute shortest path)*

**To watch DFS (Depth-First Search):**
`python3 maze_search.py -a dfs`
*(You'll see it immediately dive as deep as possible down one route before backtracking)*