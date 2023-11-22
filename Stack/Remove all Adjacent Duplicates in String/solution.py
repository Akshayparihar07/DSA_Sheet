def removeDuplicates(self, s: str) -> str:
    # Initialize an empty stack to store unique characters
    stack = []
    
    # Initialize an empty string to store the final result
    ans = ""
    
    # Iterate through each character in the input string
    for char in s:
        # Check if the stack is not empty and the top of the stack is equal to the current character
        if stack and stack[-1] == char:
            # Pop characters from the stack until it becomes empty or the top is different from the current character
            while stack and stack[-1] == char:
                stack.pop()
        else:
            # If the stack is empty or the top is different, push the current character onto the stack
            stack.append(char)

    # Build the final result by popping characters from the stack
    while stack:
        ans += stack.pop()

    # Reverse the final result and return
    return ans[::-1]
