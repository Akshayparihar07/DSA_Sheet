class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Initialize variables
        start_index = 0  # starting index of the current sequence
        result = ""     # variable to store the largest good integer
        current_length = 0  # length of the current sequence

        # Iterate through the characters of the input string
        for end_index in range(len(num)):
            # Check if the current character is the same as the character at the starting index
            if num[start_index] == num[end_index]:
                # Calculate the length of the current sequence
                current_length = end_index - start_index + 1

                # Check if the length is 3 (as per the problem statement)
                if current_length == 3:
                    # Update the result with the maximum of the current sequence and the previous result
                    result = max(result, num[start_index:end_index + 1])
            else:
                # If the current character is different, update the starting index
                start_index = end_index

        # Return the final result
        return result
