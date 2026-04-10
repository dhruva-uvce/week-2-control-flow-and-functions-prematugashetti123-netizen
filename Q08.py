# Q08. Sum of Digits (while loop)
#
# Ask the user for a positive integer.
# Print the sum of its digits using a while loop.
#
# Sample Input:   Enter a number: 9876
# Sample Output:  Sum of digits of 9876 = 30

# --- YOUR CODE HERE ---
n = int(input("Enter a number: "))

temp = n
total = 0

while n > 0:
    total += n % 10
    n //= 10

print(f"Sum of digits of {temp} = {total}")