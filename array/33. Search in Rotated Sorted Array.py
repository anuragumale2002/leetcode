from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Modified Binary Search.
        
        Why it works:
        - In rotated sorted array, one half is always sorted.
        - We identify the sorted half.
        - Check if target lies inside that half.
        - Narrow search space accordingly.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # Left half sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # Right half sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
