from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Ultra-Optimized O(n) Time, O(1) Space Solution

        ---------------------------------------------------
        CORE IDEA
        ---------------------------------------------------

        The smallest missing positive must lie in range [1, n+1],
        where n = length of array.

        Why?
        - If numbers 1..n all exist → answer is n+1
        - Otherwise, first missing in that range.

        ---------------------------------------------------
        STRATEGY: CYCLIC INDEX PLACEMENT
        ---------------------------------------------------

        Goal:
            Place each number x at index x-1.

        For example:
            If nums[i] = 3
            It should be placed at index 2.

        We repeatedly swap until:
            nums[i] is either:
                - Out of range
                - Already in correct position
                - Duplicate

        ---------------------------------------------------
        WHY THIS WORKS
        ---------------------------------------------------

        After placement:
            If index i does NOT contain i+1,
            then i+1 is missing.

        ---------------------------------------------------
        TIME COMPLEXITY
        ---------------------------------------------------

        O(n)
        Each number is swapped at most once.

        ---------------------------------------------------
        SPACE COMPLEXITY
        ---------------------------------------------------

        O(1)
        We modify array in-place.
        """

        n = len(nums)

        # Step 1: Place each number in its correct index
        for i in range(n):
            while (
                1 <= nums[i] <= n and
                nums[nums[i] - 1] != nums[i]
            ):
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        # Step 2: Find first index where value is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all positions are correct
        return n + 1