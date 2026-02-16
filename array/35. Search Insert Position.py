from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        We perform a lower_bound binary search.
        
        We maintain search space [l, r).
        Invariant:
        - All elements before l are < target
        - All elements at or after r are >= target
        
        When loop ends, l == r is the correct insert position.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        
        l, r = 0, len(nums)
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return l
