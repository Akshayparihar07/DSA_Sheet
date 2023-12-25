#include <bits/stdc++.h> 

// Function to recursively calculate the minimum cost to reach the last stone
// with the given jumps
int solve(int n, vector<int> &heights, vector<int> &dp ){
    // Base case: If there is only one stone, the cost is 0
    if (n == 0) return 0;

    // Check if the solution for this state is already computed
    if (dp[n] != -1) return dp[n]; 

    // Calculate the cost of reaching the current stone by jumping one step
    int left = solve(n-1, heights, dp) + abs(heights[n] - heights[n-1]);
    
    // Calculate the cost of reaching the current stone by jumping two steps
    int right = INT_MAX;
    if (n-2 >= 0) right = solve(n-2, heights, dp) + abs(heights[n] - heights[n-2]);
    
    // Store the minimum cost for the current state in the DP array
    return dp[n] = min(left, right);
}

// Function to find the minimum cost to reach the last stone
int frogJump(int n, vector<int> &heights)
{
    // DP array to store the minimum cost for each stone
    vector<int> dp(n+1, -1);
    
    // Call the recursive function to find the minimum cost
    return solve(n-1, heights, dp);
}
