class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure A is the shorter array
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
            
        total = len(A) + len(B)
        half = total // 2
        
        # Binary search range on the smaller array
        l, r = 0, len(A) - 1
        
        while True:
            i = (l + r) // 2  # Partition index for A
            j = half - i - 2  # Partition index for B (adjusted for 0-indexing)
            
            # Handle edge cases where partition is at the very beginning or end
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            # Valid partition found
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total: median is the minimum of the right half
                if total % 2:
                    return min(Aright, Bright)
                # Even total: average of max(lefts) and min(rights)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            # Binary search adjustment
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
                


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         merged = nums1 + nums2
#         merged.sort()

#         n = len(merged)

#         if n % 2 == 1:
#             return float(merged[n // 2])
#         else:
#             mid1 = merged[n // 2 - 1]
#             mid2 = merged[n // 2]
#             return (mid1 + mid2) / 2.0


# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))