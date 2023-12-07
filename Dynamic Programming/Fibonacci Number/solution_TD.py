class Solution:
    def fib(self, n: int) -> int:
        def fibonacci_recursive(n):
            # Base case: return n for 0 and 1
            if n <= 1:
                return n

            # Check if the result for n is already computed
            if dp[n] != -1:
                return dp[n]

            # Compute and store the Fibonacci value for n
            dp[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

            return dp[n]

        # Initialize memoization table with -1
        dp = [-1 for _ in range(n + 1)]

        # Start the recursive Fibonacci calculation
        return fibonacci_recursive(n)
