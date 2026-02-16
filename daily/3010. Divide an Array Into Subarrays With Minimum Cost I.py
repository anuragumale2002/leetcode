from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        """
        We must split array into exactly 3 subarrays.
        
        Cost of each subarray = its first element.
        
        The first subarray must start at index 0,
        so nums[0] is always included.
        
        We need to pick two more starting points.
        To minimize cost, we choose the two smallest
        elements from nums[1:].
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        
        first_min = float('inf')
        second_min = float('inf')
        
        for num in nums[1:]:
            if num < first_min:
                second_min = first_min
                first_min = num
            elif num < second_min:
                second_min = num
        
        return nums[0] + first_min + second_min
