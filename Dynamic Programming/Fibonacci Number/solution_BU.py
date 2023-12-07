class Solution:
    def fib(self, n: int) -> int:
        # Initialize an array to store Fibonacci numbers
        dp = [-1 for _ in range(n+1)]

        # Base cases for 0 and 1
        dp[0] = 0
        dp[1] = 1

        # Fill the array with Fibonacci numbers from bottom-up
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        # Return the Fibonacci number for the given input
        return dp[n]
