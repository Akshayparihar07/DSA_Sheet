# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, fast and slow, both starting at the head of the linked list
        fast = head
        slow = head

        # Iterate through the linked list until the fast pointer reaches the end or encounters a cycle
        while fast and fast.next and slow:
            # Move the fast pointer two steps at a time
            fast = fast.next.next
            # Move the slow pointer one step at a time
            slow = slow.next

            # Check if the fast and slow pointers meet, indicating the presence of a cycle
            if fast == slow:
                return True
        
        # If the loop completes without detecting a cycle, return False
        return False
