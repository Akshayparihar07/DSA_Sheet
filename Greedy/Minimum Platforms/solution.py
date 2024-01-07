def minimumPlatform(n, arr, dep):
    # Sort arrival and departure times separately
    arr.sort()
    dep.sort()

    # Initialize pointers for arrival and departure times
    i, j = 1, 0

    # Initialize variables to track the number of platforms needed and the maximum platforms needed simultaneously
    plat_needed, max_plat = 1, 1

    # Iterate through the arrival and departure times
    while i < n and j < n:
        # Check if the next train arrives before or at the same time as the departure of the current train
        if arr[i] <= dep[j]:
            # Increment the number of platforms needed and move to the next arrival time
            plat_needed += 1
            i += 1
        else:
            # Decrement the number of platforms needed as a train departs, and move to the next departure time
            plat_needed -= 1
            j += 1

        # Update the maximum number of platforms needed simultaneously
        max_plat = max(plat_needed, max_plat)

    # Return the maximum number of platforms needed simultaneously
    return max_plat
