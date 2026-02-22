from typing import List 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Ultra-Optimized Combination Sum

        ---------------------------------------
        WHY THIS APPROACH IS EFFICIENT
        ---------------------------------------

        1) We use BACKTRACKING (DFS).
           - At every step we decide whether to include a number.
           - We keep subtracting from target.

        2) We SORT the array.
           - Enables early pruning.
           - If current number > remaining target → break.
           - Prevents unnecessary recursion.

        3) We pass index instead of slicing array.
           - Avoids O(n) memory copying.
           - Keeps space usage minimal.

        4) We allow reuse of same element:
           - We call DFS with same index (not index + 1).
           - That allows unlimited reuse.

        5) We prevent duplicates:
           - We never revisit earlier indices.
           - This ensures combinations stay sorted.

        ---------------------------------------
        HOW RECURSION WORKS
        ---------------------------------------

        Suppose:
            candidates = [2,3,6,7]
            target = 7

        Example path:
            pick 2 → remaining 5
            pick 2 → remaining 3
            pick 3 → remaining 0  ✅ store [2,2,3]

        If remaining becomes negative:
            stop recursion immediately (pruning).

        ---------------------------------------
        TIME COMPLEXITY
        ---------------------------------------

        Worst case: O(2^t) where t = target
        (branching depends on smallest candidate)

        But pruning makes it much faster in practice.

        ---------------------------------------
        SPACE COMPLEXITY
        ---------------------------------------

        O(target) recursion depth (worst case)
        Output space not counted.
        """

        candidates.sort()  # Sorting enables pruning
        res = []
        path = []

        def dfs(start, remaining):
            # Base case: exact target reached
            if remaining == 0:
                res.append(path[:])  # copy current combination
                return

            for i in range(start, len(candidates)):

                num = candidates[i]

                # Pruning: if number exceeds remaining target, stop
                if num > remaining:
                    break

                # Choose
                path.append(num)

                # Recurse (i instead of i+1 because reuse allowed)
                dfs(i, remaining - num)

                # Undo (Backtrack)
                path.pop()

        dfs(0, target)
        return res