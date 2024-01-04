def isCircuit(gas, cost, n):
    # If the total gas is less than the total cost, it's impossible to complete the circuit
    if sum(gas) < sum(cost):
        return -1 
    
    total_gas = 0  # Variable to track the total gas accumulated
    start = 0      # Variable to store the starting index of the circuit
    
    # Loop through each gas station
    for i in range(n):
        diff = gas[i] - cost[i]  # Calculate the difference between gas and cost at the current station
        
        total_gas += diff  # Accumulate the difference to the total gas
        
        # If the total gas becomes negative, reset it to zero and update the starting index
        if total_gas < 0:
            total_gas = 0
            start = i + 1  # Set the starting index to the next station
            
    return start  # Return the starting index of the circuit
    
# Input number of gas stations
n = int(input())
# Input gas values for each station
gas = list(map(int, input().split()))
# Input cost values for each station
cost = list(map(int, input().split()))

# Call the isCircuit function and store the result
ans = isCircuit(gas, cost, n)

# Print the result
print(ans)
