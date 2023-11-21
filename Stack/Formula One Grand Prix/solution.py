 def findDriver(arr):
        n = len(arr)
        left_visibility = [0] * n
        right_visibility = [0] * n
        score = [0] * n

        # Calculate left visibility
        left_stack = []
        for i in range(n):
            while left_stack and arr[i] > arr[left_stack[-1]]:
                left_stack.pop()
            left_visibility[i] = i  if not left_stack else i - left_stack[-1]
            left_stack.append(i)

        # Calculate right visibility
        right_stack = []
        for i in range(n - 1, -1, -1):
            while right_stack and arr[i] > arr[right_stack[-1]]:
                right_stack.pop()
            right_visibility[i] = n - i if not right_stack else right_stack[-1] - i
            right_stack.append(i)

        # Calculate score
        for i in range(n):
            score[i] = (left_visibility[i] + right_visibility[i]) * (i + 1) % 1000000007

        max_score = max(score)
        winning_driver = score.index(max_score) + 1
        return winning_driver
