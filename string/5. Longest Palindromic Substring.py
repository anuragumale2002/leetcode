class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            # Case 1: Center is a single character (odd length)
            len1 = self._expand_around_center(s, i, i)
            # Case 2: Center is between two characters (even length)
            len2 = self._expand_around_center(s, i, i + 1)
            
            # Take the maximum of the two expansion types
            max_len = max(len1, len2)
            
            # If we found a new longest palindrome, update our pointers
            if max_len > (end - start):
                # Calculate new start and end indices
                # max_len - 1 handles the offset for even lengths correctly
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]

    def _expand_around_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Returns the length of the palindrome found
        # (right - 1) - (left + 1) + 1 simplifies to right - left - 1
        return right - left - 1



# Super Optimized CODE:

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n < 2:
#             return s

#         start = 0
#         best_len = 1
#         i = 0

#         while i < n:
#             # If remaining chars can't beat current best, stop early (practical pruning)
#             if (n - i) * 2 + 1 <= best_len:
#                 break

#             left = i
#             right = i

#             # 1) collapse duplicates: treat s[left..right] as one center block
#             while right + 1 < n and s[right + 1] == s[left]:
#                 right += 1

#             # next i starts after this block
#             i = right + 1

#             # 2) expand around the block
#             while left - 1 >= 0 and right + 1 < n and s[left - 1] == s[right + 1]:
#                 left -= 1
#                 right += 1

#             length = right - left + 1
#             if length > best_len:
#                 best_len = length
#                 start = left

#         return s[start:start + best_len]





# Manacher’s Algorithm For Substrings Palindrome


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return ""

#         # 1. Transform string: "aba" -> "#a#b#a#"
#         # This handles even-length palindromes by making everything odd
#         T = "#" + "#".join(s) + "#"
#         n = len(T)
#         P = [0] * n      # Array to store the radius of palindrome at each center
#         C = 0            # Center of the current rightmost palindrome
#         R = 0            # Right boundary of the current rightmost palindrome

#         for i in range(n):
#             # 2. Use symmetry to jump-start the radius at index i
#             # i_mirror is the reflection of i across center C
#             if i < R:
#                 i_mirror = 2 * C - i
#                 P[i] = min(R - i, P[i_mirror])
            
#             # 3. Attempt to expand beyond the mirrored radius
#             while (i + 1 + P[i] < n and 
#                    i - 1 - P[i] >= 0 and 
#                    T[i + 1 + P[i]] == T[i - 1 - P[i]]):
#                 P[i] += 1

#             # 4. If the new palindrome expands past R, update C and R
#             if i + P[i] > R:
#                 C = i
#                 R = i + P[i]

#         # 5. Find the maximum radius in P
#         max_len = max(P)
#         center_index = P.index(max_len)
        
#         # 6. Map back to the original string
#         # The start in original string is (center - radius) // 2
#         start = (center_index - max_len) // 2
#         return s[start : start + max_len]




# Brute Force


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return ""
        
#         longest = ""
#         n = len(s)
        
#         for i in range(n):
#             for j in range(i, n):
#                 substring = s[i : j + 1]
#                 if len(substring) > len(longest) and self.is_palindrome(substring):
#                     longest = substring
                    
#         return longest

#     def is_palindrome(self, sub: str) -> bool:
#         return sub == sub[::-1]