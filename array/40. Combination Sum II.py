from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Ultra-Optimized Combination Sum II

        ---------------------------------------
        KEY DIFFERENCE FROM COMBINATION SUM I
        ---------------------------------------

        1) Each number can be used ONLY ONCE.
           → So recursion goes to i + 1 (not i).

        2) Input may contain duplicates.
           → We must skip duplicate numbers at same recursion depth.

        ---------------------------------------
        WHY SORTING IS NECESSARY
        ---------------------------------------

        Sorting allows:
        - Early pruning (if num > remaining → break)
        - Easy duplicate skipping
        - Maintaining non-decreasing order (avoid permutations)

        ---------------------------------------
        HOW DUPLICATE SKIPPING WORKS
        ---------------------------------------

        Condition:
            if i > start and candidates[i] == candidates[i - 1]:
                continue

        Meaning:
        - If this number is same as previous
        - And we are at same recursion level
        - Then skip it

        This prevents duplicate combinations like:
            [1,2,5]
            [1,2,5]  (generated again from duplicate 1)

        ---------------------------------------
        RECURSION LOGIC
        ---------------------------------------

        At each step:
            1. If remaining == 0 → store answer
            2. Loop from 'start' to end
            3. Skip duplicates
            4. If num > remaining → break (pruning)
            5. Choose number
            6. Recurse with i + 1 (no reuse)
            7. Backtrack

        ---------------------------------------
        TIME COMPLEXITY
        ---------------------------------------

        Worst case: O(2^n)
        (Each element either chosen or not)

        Pruning + duplicate skipping reduces branching.

        ---------------------------------------
        SPACE COMPLEXITY
        ---------------------------------------

        O(n) recursion depth
        Output space not counted.
        """

        candidates.sort()  # Crucial for pruning & duplicate handling
        res = []
        path = []

        def dfs(start, remaining):

            # Base case: target reached
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):

                num = candidates[i]

                # Skip duplicates at same recursion depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Pruning: stop if number exceeds remaining target
                if num > remaining:
                    break

                # Choose
                path.append(num)

                # Move to next index (no reuse allowed)
                dfs(i + 1, remaining - num)

                # Backtrack
                path.pop()

        dfs(0, target)
        return res