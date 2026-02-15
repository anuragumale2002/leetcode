from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # If array is empty, return 0
        if not nums:
            return 0
        
        # 'write' pointer:
        # Points to position where next unique element should be placed.
        # First element is always unique.
        write = 1
        
        # Start reading from second element
        for read in range(1, len(nums)):
            
            # Since array is sorted,
            # if current number is different from previous,
            # it means we found a new unique element.
            if nums[read] != nums[read - 1]:
                
                # Place this unique element at 'write' position
                nums[write] = nums[read]
                
                # Move write pointer forward
                write += 1
        
        # 'write' now represents total number of unique elements
        return write
