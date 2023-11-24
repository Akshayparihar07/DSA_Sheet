def nextLargerElement(self, arr, n):
    # Initialize the result array with -1 for elements without a next larger element
    result = [-1] * n
    
    # Stack to keep track of elements for which the next larger element is yet to be found
    stack = []
    
    # Traverse the array in reverse order
    for i in range(n-1, -1, -1):
        # Pop elements from the stack while they are smaller than or equal to the current element
        while stack and stack[-1] <= arr[i]:
            stack.pop()
            
        # If the stack is not empty, assign the top element of the stack as the next larger element
        if stack:
            result[i] = stack[-1]
            
        # Push the current element onto the stack for future comparisons
        stack.append(arr[i])
        
    # Return the result array containing the next larger element for each element in the input array
    return result
