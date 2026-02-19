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




"""
char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) {
        char* res = (char*)malloc(1);
        res[0] = '\0';
        return res;
    }

    // If only one string, return it directly
    if (strsSize == 1) {
        char* res = (char*)malloc(strlen(strs[0]) + 1);
        strcpy(res, strs[0]);
        return res;
    }

    int i = 0;

    while (strs[0][i] != '\0') {
        char current = strs[0][i];

        // Compare with all other strings
        for (int j = 1; j < strsSize; j++) {
            // If mismatch or string ends
            if (strs[j][i] == '\0' || strs[j][i] != current) {
                char* res = (char*)malloc(i + 1);
                strncpy(res, strs[0], i);
                res[i] = '\0';
                return res;
            }
        }
        i++;
    }

    // Entire first string is common prefix
    char* res = (char*)malloc(i + 1);
    strcpy(res, strs[0]);
    return res;
}
"""