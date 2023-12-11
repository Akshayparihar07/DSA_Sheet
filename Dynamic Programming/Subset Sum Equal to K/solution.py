def subset_sum_exists(i, k, arr, dp):
    if k == 0:
        return True

    if i == 0:
        return k - arr[i] == 0

    if dp[i][k] is not False:
        return dp[i][k]

    not_take = subset_sum_exists(i - 1, k, arr, dp)

    take = False

    if k >= arr[i]:
        take = subset_sum_exists(i - 1, k - arr[i], arr, dp)

    dp[i][k] = take or not_take

    return dp[i][k]
    
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    
    dp = [[False] * (k + 1) for _ in range(n)] 
    return subset_sum_exists(n-1, k, arr, dp)

print(main())
