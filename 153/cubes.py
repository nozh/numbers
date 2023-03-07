import random

# Generate 3 random positive integers divisible by three
numbers = [random.randint(1, 100000) * 3 for _ in range(3)]

# Ask the user if they want to select a random number or enter one manually
print("Do you want to:")
print("1. Select a random number")
print("2. Enter a number manually")
choice = int(input())

if choice == 1:
    # Select one of the numbers based on user input
    print("Choose a starting number:")
    for i, n in enumerate(numbers):
        print(f"{i+1}. {n}")
    selection = int(input()) - 1
    n = numbers[selection]
else:
    # Ask the user to enter a number manually
    n = int(input("Enter a positive integer divisible by three: "))

print(f"Starting with {n}\n")

# Initialize variables for tracking cycles and previous numbers
cycle_count = 0
previous_numbers = []

# Start the main loop
while True:
    # Split the number into its base 10 digits
    digits = [int(d) for d in str(n)]
    
    # Take the sum of their cubes
    cube_sum = sum([d**3 for d in digits])
    
    # Output each cube in the current step, right-aligned
    cubes_str = ' + '.join([f'{d}^3'.rjust(3) for d in digits])
    cubes_sum_str = ' + '.join([f'{d**3}' for d in digits])

    print(f'{cycle_count}. [{n}] {cubes_str} = {str(cubes_sum_str)} =  {str(cube_sum).rjust(3)}')
    
    # Check if the number has already appeared in the sequence
    if cube_sum in previous_numbers:
        print(f"Number {n} repeated. Stopping cycle.")
        break
    
    # Add the number to the list of previous numbers
    previous_numbers.append(cube_sum)
    
    # Update the current number and cycle count
    n = cube_sum
    cycle_count += 1
    
    # Ask the user if they want to continue every 10 cycles
    if cycle_count % 20 == 0:
        choice = input("Continue? (y/n) ")
        if choice.lower() != 'y':
            break

