# Program to add two numbers from command line arguments
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python add.py <num1> <num2>")
        return
    
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        print(f"Sum: {num1 + num2}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
