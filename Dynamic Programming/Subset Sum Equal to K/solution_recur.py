def iss(arr, N, sum):
            # Base Case
            if sum == 0 or N == 0:
                if sum == 0:
                    return True
                return False
        
            # Invalid Case
            if arr[N-1] > sum: 
                # Don't Take
                return iss(arr, N-1, sum)
        
            # Valid Case
            else:       # Don't Take          # Take
                return iss(arr, N-1, sum) or iss(arr, N-1, sum-arr[N-1])  

                
        return iss(arr, N, sum)
