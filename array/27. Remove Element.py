from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # 'left' scans from beginning
        left = 0
        
        # 'right' represents the current effective length of array
        # Elements beyond 'right' are ignored
        right = len(nums)
        
        # Process elements while left pointer is inside valid range
        while left < right:
            
            # If current element equals val,
            # replace it with last unchecked element
            if nums[left] == val:
                
                # Move last valid element into current position
                nums[left] = nums[right - 1]
                
                # Reduce effective array size
                right -= 1
                
                # IMPORTANT:
                # Do NOT increment left here,
                # because swapped element needs to be checked
            else:
                # If current element is valid,
                # move to next position
                left += 1
        
        # 'left' is count of elements not equal to val
        return left
