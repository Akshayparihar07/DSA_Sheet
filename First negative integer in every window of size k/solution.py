def printFirstNegativeInteger(A, N, K):
    # Initialize a queue to keep track of indices of negative elements in the current window
    negative_indices_queue = []

    # Initialize a list to store the first negative integer in each window
    result = []

    # Process the first window
    for i in range(K):
        # If the element is negative, add its index to the queue
        if A[i] < 0:
            negative_indices_queue.append(i)

    # Store the result from the first window
    if negative_indices_queue:
        result.append(A[negative_indices_queue[0]])
    else:
        result.append(0)

    # Process the remaining windows
    for i in range(K, N):
        # Removal: Remove indices that are outside the current window
        if negative_indices_queue and i - negative_indices_queue[0] >= K:
            negative_indices_queue.pop(0)

        # Addition: Add the index of a negative element to the queue
        if A[i] < 0:
            negative_indices_queue.append(i)

        # Store the answer for the current window
        if negative_indices_queue:
            result.append(A[negative_indices_queue[0]])
        else:
            result.append(0)

    return result
