def isPrime(n):
    for i in range(2, n**2):
        if n % i == 0:
            return "NO"
        else:
            return "YES"
n = int(input())
print(isPrime(n))