# Program to check if a number is even or not
def is_even(number):
    return number % 2 == 0

def main():
    try:
        num = int(input("Enter a number: "))
        if is_even(num):
            print(f"{num} is an even number.")
        else:
            print(f"{num} is an odd number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
