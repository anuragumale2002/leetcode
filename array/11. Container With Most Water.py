from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        h = height
        l, r = 0, len(h) - 1
        best = 0

        while l < r:
            hl = h[l]
            hr = h[r]
            width = r - l
            if hl < hr:
                area = hl * width
                l += 1
            else:
                area = hr * width
                r -= 1

            if area > best:
                best = area

        return best