class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            char = s[right]
            
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            char_map[char] = right
            current_window_size = right - left + 1
            if current_window_size > max_length:
                max_length = current_window_size
                
        return max_length