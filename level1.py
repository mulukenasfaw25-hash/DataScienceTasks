# Function to check if a number is prime
def is_prime(n):
    # Any number less than or equal to 1 is NOT prime
    if n <= 1:
        return False

    # Loop from 2 up to the square root of n
    # We use sqrt(n) because a larger factor of n must be paired
    # with a smaller factor that has already been checked
    for i in range(2, int(n**0.5) + 1):
        
        # If n is divisible by i, it means n has a factor
        # so it is NOT a prime number
        if n % i == 0:
            return False

    # If no factors were found, the number is prime
    return True


# Take input from the user and convert it to an integer
n = int(input("enter a number: "))

# Call the function and print the result
if is_prime(n):
    print("prime number")  # If function returns True
else:
    print("is not a prime number")  # If function returns False
