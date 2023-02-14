def get_prime_divisors(n):
    # Initialize the list of prime divisors
    divisors = []
    # Iterate over all possible divisors
    for i in range(2, n):
        # Check if the divisor is prime
        if is_prime(i):
            # Check if the divisor is a divisor of n
            if n % i == 0:
                # Add the divisor to the list
                divisors.append(i)
    return divisors

def matches_mask(n, mask):
    # Convert the number to a string
    n_str = str(n)
    # Check if the number matches the mask
    if len(n_str) != len(mask):
        return False
    for i in range(len(mask)):
        if mask[i] == '*':
            continue
        elif mask[i] == '?':
            continue
        elif mask[i] != n_str[i]:
            return False
    return True

def is_prime(n):
    # Check if n is a prime number
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True