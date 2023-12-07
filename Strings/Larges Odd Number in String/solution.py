class Solution:
    def largestOddNumber(self, num: str) -> str:
      
        # Iterate through the digits in reverse order
        for i in range(len(num)-1, -1, -1):
          
            # Check if the current digit is odd
            if num[i] in {'1', '3', '5', '7', '9'}:
                # Return the substring from the beginning up to the current index
                return num[:i+1]
              
        # If no odd digit is found, return an empty string
        return ''
