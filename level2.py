# Take a string input from the user
text = input("enter a string: ")

# Define all vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Initialize a counter to keep track of vowels
count = 0

# Loop through each character in the input string
for char in text:
    
    # Check if the current character is a vowel
    if char in vowels:
        
        # If it is a vowel, increase the counter by 1
        count += 1

# After the loop, print the total number of vowels found
print("number of vowels: ", count)