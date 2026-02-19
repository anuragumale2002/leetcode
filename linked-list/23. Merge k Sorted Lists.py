# Definition for singly-linked list.

import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists using a min-heap.

        Time Complexity: O(N log k)
        Space Complexity: O(k)
        """

        heap = []
        
        # Push first node of each list into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        tail = dummy
        
        while heap:
            _, i, node = heapq.heappop(heap)
            
            tail.next = node
            tail = tail.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
