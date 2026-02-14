from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If list is empty, no common prefix
        if not strs:
            return ""

        # Start by assuming the first string is the prefix
        prefix = strs[0]

        # Compare prefix with every other string
        for str_ in strs[1:]:

            i = 0

            # Compare characters one by one
            while (
                i < len(str_) and        # don't go past current string
                i < len(prefix) and      # don't go past current prefix
                str_[i] == prefix[i]     # characters must match
            ):
                i += 1

            # After loop ends:
            # i is the length of matching characters
            prefix = prefix[0:i]

        return prefix