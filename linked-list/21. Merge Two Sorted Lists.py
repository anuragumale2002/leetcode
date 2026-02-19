# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into one sorted list.

        Optimal Iterative Approach:
        - Time Complexity: O(n + m)
        - Space Complexity: O(1)
        - No recursion (avoids stack overhead)
        """

        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next

        # Attach remaining nodes
        tail.next = list1 if list1 else list2

        return dummy.next
