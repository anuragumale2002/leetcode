# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swaps every two adjacent nodes in the linked list.

        Optimal Iterative Approach:
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        """

        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Swapping
            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev to next pair
            prev = first

        return dummy.next
