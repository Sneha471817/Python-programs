def sum_even_fibonacci(limit):
    a, b = 1, 2
    even_sum = 0
    while b <= limit:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b
    return even_sum

def main():
    limit = 4000000
    result = sum_even_fibonacci(limit)
    print(f"Sum of even Fibonacci numbers below {limit}: {result}")

if __name__ == "__main__":
    main()