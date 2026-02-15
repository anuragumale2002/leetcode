from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Sort the array first.
        # WHY? 
        # 1. Allows two-pointer technique.
        # 2. Makes it easy to skip duplicates.
        nums.sort()
        
        n = len(nums)
        result = []
        
        # First loop: pick the first number of quadruplet
        for i in range(n - 3):
            
            # Skip duplicate values for i
            # WHY? To avoid duplicate quadruplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # ---- EARLY PRUNING (important optimization) ----
            
            # If smallest possible sum with current i is already > target,
            # no need to continue (array is sorted).
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            
            # If largest possible sum with current i is still < target,
            # skip this i.
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            
            # Second loop: pick second number
            for j in range(i + 1, n - 2):
                
                # Skip duplicates for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # ---- MORE EARLY PRUNING ----
                
                # Smallest sum with current i and j
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                
                # Largest sum with current i and j
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue
                
                # Now we use two pointers for remaining two numbers
                left = j + 1
                right = n - 1
                
                while left < right:
                    
                    # Calculate current 4-number sum
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        # Found valid quadruplet
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Move both pointers inward
                        left += 1
                        right -= 1
                        
                        # Skip duplicates for left pointer
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        
                        # Skip duplicates for right pointer
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    
                    elif total < target:
                        # Need bigger sum → move left forward
                        left += 1
                    else:
                        # Need smaller sum → move right backward
                        right -= 1
        
        return result
