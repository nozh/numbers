import random

def sum_of_powers(num):
    # Split number into its base 10 digits
    digits = [int(d) for d in str(num)]
    # Calculate sum of their power of 4
    return sum(d ** 4 for d in digits)

# Generate 3 random positive integers up to 10000
nums = [random.randint(1, 10000) for _ in range(3)]

# Alternatively, offer user to input manually
user_choice = input("Do you want to input numbers manually? (y/n): ")
if user_choice.lower() == "y":
    nums = []
    num = int(input(f"Enter positive integer: "))
    nums.append(num)

# Initialize variables
cycles = 0

# Loop over the numbers
for num in nums:
    # Initialize variables for each number
    cycle_sums = []
    cycle = 0
    seen = set()

    # Start cycling through the number
    while True:
        # Split number into its base 10 digits and calculate sum of their power of 4
        s = sum_of_powers(num)
        # Append sum to cycle_sums
        cycle_sums.append(s)


        power_str = ' + '.join([f'{int(d)}^4'.rjust(3) for d in str(num)])
        sum_str = ' + '.join([f'{int(d)**4}' for d in str(num)])
        # Print current cycle information
        print(f"{cycle+1}. [{num}] => {power_str} = {sum_str} => {s}")

        # Check if sum has been seen before
        if s in seen:
            print(f" {s} repeated after {cycle} iterations. ")
            break
        seen.add(s)

        # Update variables for next iteration
        num = s
        cycle += 1

        # Ask user if they want to continue after every 20 cycles
        if cycle % 20 == 0:
            user_choice = input("Do you want to continue? (y/n): ")
            if user_choice.lower() == "n":
                print("Exiting...")
                exit()

