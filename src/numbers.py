import math

def divisors(n):
    """
    Returns a list of all the divisors of a given number n.
    """
    divisors_list = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors_list.append(i)
    return divisors_list

def prime_factors(n):
    """
    Returns a list of prime factors of a given number n.
    """
    factors_list = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors_list.append(i)
    if n > 1:
        factors_list.append(n)
    return factors_list

def sum_of_digits(n):
    """
    Returns the sum of digits of a given number n.
    """
    digits_sum = 0
    for digit in str(n):
        digits_sum += int(digit)
    return digits_sum

def radical(n):
    """
    Returns the radical of a given number n.
    """
    rad = 1
    for p in set(prime_factors(n)):
        rad *= p
    return rad

