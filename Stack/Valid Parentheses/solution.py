def isValid(self, s: str) -> bool:
    # Initialize an empty stack to keep track of opening brackets
    stack = []

    # Check if the length of the input string is odd, in which case it can't be balanced
    if len(s) % 2 != 0:
        return False

    # Iterate through each character in the string
    for char in s:
        # If the character is an opening bracket, push it onto the stack
        if char in "({[":
            stack.append(char)
        else:
            # If the stack is empty, there is no corresponding opening bracket, return False
            if not stack:
                return False

            # Check if the closing bracket matches the last opening bracket on the stack
            if char == ")" and stack[-1] != "(":
                return False
            elif char == "]" and stack[-1] != "[":
                return False
            elif char == "}" and stack[-1] != "{":
                return False

            # Pop the matching opening bracket from the stack
            stack.pop()

    # After iterating through the entire string, the stack should be empty for a valid expression
    return len(stack) == 0
