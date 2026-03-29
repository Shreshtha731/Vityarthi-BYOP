# TermiTask 

## What is this?
TermiTask is a really simple command-line to-do list. I built this for my BYOP capstone because I was getting annoyed having to constantly open web browsers or other apps just to see what university assignments I had due while I was in the middle of writing code in the terminal.

It runs entirely in Python and saves your tasks locally to a JSON file, so you don't need to set up a database.

## How to run it
You just need Python 3 installed. No weird libraries or `pip install` required.

Clone the repo, open your terminal in the folder, and run:

**To add a task:**
`python3 task_manager.py -a "Finish BYOP Report" -d "Friday"`

**To see your tasks:**
`python3 task_manager.py -v`

**To see only the stuff you haven't finished yet:**
`python3 task_manager.py -p`

**To mark something as done (using the ID number):**
`python3 task_manager.py -c 1`