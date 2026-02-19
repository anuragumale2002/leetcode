class Solution:
    def isValid(self, s: str) -> bool:
        """
        Checks whether the input string of brackets is valid.

        Optimal Approach:
        - Use stack to track opening brackets.
        - Match each closing bracket with the top of stack.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            # If closing bracket
            if ch in mapping:
                # Stack empty or mismatch
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack
