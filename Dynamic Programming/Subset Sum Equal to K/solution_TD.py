def iss(arr, N, sum, dp):
    # Base Case
    if sum == 0:
        return True
    if N == 0:
        return False
        
    # DP check
    if dp[N][sum] is not None:
        return dp[N][sum]
        
    # Invalid Case
    if arr[N-1] > sum:
        # Don't Take
        dp[N][sum] = iss(arr, N-1, sum, dp)
        
    else:  # Valid Case
        # Don't Take or Take
        dp[N][sum] = iss(arr, N-1, sum, dp) or iss(arr, N-1, sum-arr[N-1], dp)
        
    return dp[N][sum]

                
dp = [[None]*(sum+1) for _ in range(N+1)]
return iss(arr, N, sum, dp)
