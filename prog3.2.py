# Program to print decimal equivalents of fractions from 1/2 to 1/10
def main():
    for i in range(2, 11):
        print(f"1/{i} = {1/i:.6f}")

if __name__ == "__main__":
    main()
