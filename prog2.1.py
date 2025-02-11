# Program to compute distance between two points
import math

def compute_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    # Taking input from the user
    x1, y1 = map(float, input("Enter coordinates of first point (x1 y1): ").split())
    x2, y2 = map(float, input("Enter coordinates of second point (x2 y2): ").split())
    
    distance = compute_distance(x1, y1, x2, y2)
    print(f"Distance between points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")

if __name__ == "__main__":
    main()
