from numbers import divisors, prime_factors, sum_of_digits, radical

n = int(input("Enter a number: "))

print("Divisors:", divisors(n))
print("Prime factors:", prime_factors(n))
print("Sum of digits:", sum_of_digits(n))
print("Radical:", radical(n))

