# Numbers Library

The `numbers` library is a Python package for working with numbers. It provides several functions for calculating properties of numbers, including:

- `divisors(n)`: Returns a list of all the divisors of `n`.
- `prime_factors(n)`: Returns a list of the prime factors of `n`.
- `sum_of_digits(n)`: Returns the sum of the digits of `n`.
- `radical(n)`: Returns the radical of `n`, which is the product of the distinct prime factors of `n`.

## Usage

Here's an example of how to use the `numbers` library:

```python
import numbers

n = int(input("Enter a number: "))

divisors = numbers.divisors(n)
prime_factors = numbers.prime_factors(n)
sum_of_digits = numbers.sum_of_digits(n)
radical = numbers.radical(n)

print(f"Divisors of {n}: {divisors}")
print(f"Prime factors of {n}: {prime_factors}")
print(f"Sum of digits of {n}: {sum_of_digits}")
print(f"Radical of {n}: {radical}")

