class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Generates all valid combinations of n pairs of parentheses.

        Optimal Backtracking Approach:
        - Only builds valid states.
        - Prunes invalid sequences early.

        Time Complexity: O(Cn)  (Catalan number)
        Space Complexity: O(n) recursion stack
        """

        result = []
        
        def backtrack(current: list[str], open_count: int, close_count: int):
            # If valid combination completed
            if len(current) == 2 * n:
                result.append("".join(current))
                return
            
            # Add '(' if we still can
            if open_count < n:
                current.append('(')
                backtrack(current, open_count + 1, close_count)
                current.pop()
            
            # Add ')' if valid
            if close_count < open_count:
                current.append(')')
                backtrack(current, open_count, close_count + 1)
                current.pop()

        backtrack([], 0, 0)
        return result
