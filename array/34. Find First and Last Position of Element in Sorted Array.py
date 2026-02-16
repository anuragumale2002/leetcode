from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        We perform two binary searches:
        
        1. Find leftmost index:
           - When nums[mid] >= target, move right pointer.
           - Keep shrinking toward left boundary.
           
        2. Find rightmost index:
           - When nums[mid] <= target, move left pointer.
           - Keep shrinking toward right boundary.
           
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        
        def findLeft():
            l, r = 0, len(nums) - 1
            res = -1
            
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    if nums[mid] == target:
                        res = mid
                    r = mid - 1
            return res
        
        def findRight():
            l, r = 0, len(nums) - 1
            res = -1
            
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    if nums[mid] == target:
                        res = mid
                    l = mid + 1
            return res
        
        return [findLeft(), findRight()]
