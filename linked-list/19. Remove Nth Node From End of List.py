# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of a singly linked list.

        Optimal Approach:
        - Uses two-pointer technique.
        - Time Complexity: O(n)
        - Space Complexity: O(1)

        Why it works:
        1. Move 'fast' pointer n steps ahead.
        2. Move both 'fast' and 'slow' together until fast reaches last node.
        3. Now slow.next is the node to remove.
        """

        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both until fast reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node
        slow.next = slow.next.next

        return dummy.next
