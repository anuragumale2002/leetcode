from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies nums in-place to the next lexicographically greater permutation.
        
        Algorithm Explanation:
        ----------------------
        1. Traverse from right to left to find the first index 'i'
           such that nums[i] < nums[i+1].
           This identifies the pivot point where permutation change begins.
           
        2. If such pivot exists:
           - Traverse again from right to find index 'j'
             such that nums[j] > nums[i].
           - Swap nums[i] and nums[j].
           
        3. Reverse the subarray from i+1 to end.
           Why? Because the suffix is guaranteed to be in decreasing order.
           Reversing makes it the smallest possible arrangement.
           
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(nums)
        
        # Step 1: Find pivot
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If pivot found, find element just larger than nums[i]
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
