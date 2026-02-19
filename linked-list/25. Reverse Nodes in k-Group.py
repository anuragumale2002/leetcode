# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverses nodes of the list in groups of k.

        Optimal Iterative Approach:
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        - Pure pointer manipulation
        """

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # Not enough nodes left

            group_next = kth.next

            # Reverse group
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect with previous part
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
