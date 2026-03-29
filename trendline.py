import argparse

def get_best_fit_line(x_vals, y_vals):
    # Basically implementing the y = mx + b math from the ML lectures
    n = len(x_vals)
    
    # Getting all our sums ready for the regression formula
    sum_x = sum(x_vals)
    sum_y = sum(y_vals)
    sum_xy = sum(x * y for x, y in zip(x_vals, y_vals))
    sum_x_sq = sum(x ** 2 for x in x_vals)
    
    # The bottom part of the slope fraction
    bottom = (n * sum_x_sq) - (sum_x ** 2)
    
    # Just a failsafe so the program doesn't crash if they enter weird data
    if bottom == 0:
        return 0, sum_y / n
        
    # Calculate slope (m) and intercept (b)
    m = ((n * sum_xy) - (sum_x * sum_y)) / bottom
    b = (sum_y - (m * sum_x)) / n
    
    return m, b

def main():
    parser = argparse.ArgumentParser(description="A simple ML trend predictor.")
    parser.add_argument("-d", "--data", type=str, required=True, 
                        help="Put your numbers in quotes separated by commas")
    
    args = parser.parse_args()

    # Try to clean up the input so it doesn't break if they add spaces
    try:
        y_vals = [float(num.strip()) for num in args.data.split(",")]
    except ValueError:
        print("Whoops! Make sure you only type numbers and commas.")
        return

    if len(y_vals) < 2:
        print("I need at least two numbers to figure out a trend!")
        return

    # Making dummy X values (1, 2, 3...) to match the Y values they typed
    x_vals = list(range(1, len(y_vals) + 1))
    
    # Run the math
    slope, intercept = get_best_fit_line(x_vals, y_vals)
    
    # Predict what comes next
    next_x = len(x_vals) + 1
    prediction = (slope * next_x) + intercept

    print("\n--- Linear Regression Predictor ---")
    print(f"Your Data: {y_vals}")
    print(f"The Equation: y = {slope:.2f}x + {intercept:.2f}")
    print(f"Next Predicted Number: {prediction:.2f}")
    print("-----------------------------------\n")

if __name__ == "__main__":
    main()