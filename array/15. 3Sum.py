from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array
        
        for i in range(len(nums)):
            # Optimization: If the current number is > 0, the sum cannot be 0 
            # (since all numbers to the right are also positive)
            if nums[i] > 0:
                break
                
            # Skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 2: Initialize two pointers
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                
                if three_sum < 0:
                    l += 1  # Need a larger value
                elif three_sum > 0:
                    r -= 1  # Need a smaller value
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # Step 3: Skip duplicates for the pointers
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                        
        return res