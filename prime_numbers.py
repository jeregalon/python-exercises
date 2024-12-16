# returns if a number is prime or not

def isPrime(num):
    end_num = num // 2 + 1
    for i in range(2, end_num):
        if num % i == 0:
            return False
    return True

prime_numbers = []

for z in range(2, 100):
    if (isPrime(z)):
        prime_numbers.append(z)

print(prime_numbers)