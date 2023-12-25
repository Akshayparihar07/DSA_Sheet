#include <bits/stdc++.h>

// Function to calculate the minimum energy required for the frog to jump across the heights
// Parameters:
//   n: Number of heights
//   heights: Vector containing the heights of the stones
// Returns: Minimum energy required for the frog to jump across the heights
int frogJump(int n, vector<int> &heights)
{
    // Initialize variables to keep track of the minimum energy at the current position and the two previous positions
    int prev = 0;       // Minimum energy at the previous position
    int prev2 = 0;      // Minimum energy at the position two steps back

    // Loop through each stone starting from the second stone
    for (int i = 1; i < n; i++) {
        // Calculate the energy required to jump left from the previous stone to the current stone
        int left = prev + abs(heights[i] - heights[i - 1]);

        // Calculate the energy required to jump right from the stone two steps back to the current stone
        int right = INT_MAX;
        if ((i - 2) >= 0) {
            right = prev2 + abs(heights[i] - heights[i - 2]);
        }

        // Choose the minimum energy between jumping left and jumping right
        int curr = min(left, right);

        // Update the variables for the next iteration
        prev2 = prev;   // Move the previous minimum to the position two steps back
        prev = curr;    // Update the current minimum energy for the next position
    }

    // Return the minimum energy required for the frog to jump across all the heights
    return prev;
}
