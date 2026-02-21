class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        """
        Constructs the lexicographically largest special binary string.

        Approach:
        - Treat '1' as '(' and '0' as ')'
        - Split into top-level special substrings
        - Recursively optimize inner substrings
        - Sort in descending order
        - Concatenate

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """

        count = 0
        start = 0
        substrings = []

        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1

            # Found a balanced special substring
            if count == 0:
                # Recursively process inside
                inner = self.makeLargestSpecial(s[start + 1:i])
                substrings.append("1" + inner + "0")
                start = i + 1

        # Sort descending for lexicographically largest
        substrings.sort(reverse=True)

        return "".join(substrings)
