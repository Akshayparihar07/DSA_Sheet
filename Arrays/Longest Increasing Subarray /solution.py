def lenOfLongIncSubArr(a, n):
    # Initialize length variables
    # 'len' represents the current length of the increasing subarray
    # 'max_len' represents the maximum length encountered so far
    len = 1
    max_len = 1
    
    # Iterate through the array
    for i in range(n-1):
        # Check if the current element is less than the next element
        if a[i] < a[i+1]:
            # If true, increment the length of the increasing subarray
            len += 1
        else:
            # If not true, reset the length to 1 since the subarray is no longer increasing
            len = 1
        
        # Update the maximum length encountered so far
        max_len = max(len, max_len)
    
    # Return the maximum length of the increasing subarray
    return max_len
