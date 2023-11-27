def fibonacci(n):
    # Base cases: if n is 0 or 1, return n
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Check if the result for n has already been computed and stored in the array
    if arr[n] != -1:
        return arr[n]

    # Recursive case: compute Fibonacci number for n using the recursive formula
    # and store the result in the array for future use
    arr[n] = fibonacci(n-1) + fibonacci(n-2)
    return arr[n]

# Input: n, representing the index of the Fibonacci number to be calculated
n = 5  # Replace this with the desired value

# Initialize an array to store previously computed Fibonacci numbers
arr = [-1 for _ in range(n+1)]

# Call the Fibonacci function with input n
result = fibonacci(n)

# Output the result
print(result)
