# TrendLine

## What is this?
I built this for my CSA2001 BYOP capstone. It's a simple command-line tool that uses Linear Regression to predict the next number in a sequence. 

Instead of using heavy libraries like `scikit-learn` or `pandas`, I just wrote the math algorithm from scratch in Python to prove how the regression actually works under the hood.

## How to run it
You don't need to install anything special, just Python 3. 

Clone the repo, open your terminal, and run the script with the `-d` flag followed by your numbers in quotes.

**Example:**
`python3 trendline.py -d "12, 15, 18, 21"`

It will do the math and predict the next value in the trend.