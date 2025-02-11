import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_of_primes(limit):
    return sum(n for n in range(2, limit) if is_prime(n))

def main():
    limit = 2000000
    result = sum_of_primes(limit)
    print(f"Sum of all primes below {limit}: {result}")

if __name__ == "__main__":
    main()
